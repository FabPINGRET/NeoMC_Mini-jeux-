"""tools/floaty : cas limites de fl_snbt (échappements 26.2, clés entre guillemets simples, positions) et de fl_tr (ré-encodage d'une
traduction piégeuse, aller-retour d'une table vide sur des lignes réelles de data/ hors mg, copiées en dur : le test ne lit pas data/).
"""
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / 'tools' / 'floaty'))
import fl_snbt as S  # noqa: E402
import fl_tr as T  # noqa: E402

# Traduction qui mélange tout ce qu'un encodeur doit échapper : ' " \ et retour à la ligne.
BU = chr(92) + 'u'      # antislash + u construits : un \u littéral serait converti en caractère à l'écriture du fichier
NASTY ='L\'a "b" c\\d\ne'

REAL = (
    r'''execute if entity @s[tag=no_warp] at @s run tellraw @s {"text":"You can't use this right now...","color":"gray","italic":true}''',
    r'''item replace entity @s hotbar.0 with minecraft:iron_sword[unbreakable={},custom_name=[{"text":"Couteau","color":"gray","italic":false}]]''',
    r'''title @s subtitle [{"text":"Plus de coeur","color":"red"}]''',
    r'''give @s quartz[custom_model_data={strings:["7"]},custom_name={"bold":true,"color":"green","text":"Plant Scales"},enchantment_glint_override=true,lore=[{"color":"aqua","text":"They're bursting with"},[{"color":"green","italic":true,"text":"Sprouting "},{"color":"aqua","text":"energy..."}]]] 1''',
    r'''execute if score boss:st BossHealth matches 6 run bossbar set boss:st value 6''',
    r'''summon arrow ~ ~ ~ {pickup:2b,damage:50d,crit:1b,Tags:["cactus_bomb_arrow"],CustomName:{"color":"light_purple","text":"Brain Cactus"},SoundEvent:"item.spear.hit"}''',
    r'''title @s title {"text":"Coeur de l'Arbre-Mere","color":"yellow","bold":true}''',
    r'''summon wither_skeleton -239 34 -114 {PersistenceRequired:1b,Health:12f,Tags:["whisper","enemy"],CustomName:"Whisper"}''',
)


def run(line, glob, ctx_id='t:f'):
    """-> (ligne traduite, Stats) avec une table globale {anglais: français}."""
    tb = T.Table()
    for k, v in glob.items():
        tb.add(k, v, 'test')
    st = T.Stats(tb)
    return T.translate_line(line, ctx_id, st), st


class Escapes(unittest.TestCase):
    def check(self, src, value, q='"'):
        """La chaîne `src` seule : valeur décodée et positions (a, b) couvrent tout le texte."""
        leaf = S.string(src, 0)
        self.assertIsNotNone(leaf, src)
        self.assertEqual((leaf.v, leaf.a, leaf.b, leaf.q), (value, 0, len(src), q), src)
        # mêmes valeurs et positions via parse, au milieu d'un texte (décalage non nul)
        pre = 'xy '
        r = S.parse(pre + src + ' zz', len(pre))
        self.assertEqual((r[0].v, r[0].a, r[0].b, r[1]), (value, len(pre), len(pre) + len(src), len(pre) + len(src)), src)

    def test_hex_escapes(self):
        self.check(r'"a\x41b"', 'aAb')
        self.check(r'"\xe9"', 'é')
        self.check('"' + BU + '00e9' + BU + '20AC"', 'é€')
        self.check(r'"\U0001F600"', '😀')
        self.check(r'"\U000000e9"', 'é')

    def test_named_escape(self):
        self.check(r'"\N{LATIN SMALL LETTER E WITH ACUTE}!"', 'é!')
        self.check(r'"x\N{SNOWMAN}y"', 'x☃y')

    def test_letter_escapes(self):
        self.check(r'"a\sb"', 'a b')
        self.check(r'"\b\f"', '\b\f')
        self.check(r'"\n\t\r"', '\n\t\r')
        self.check(r'"\\ \" \'"', '\\ " \'')

    def test_single_quote_string(self):
        self.check(r"'a\'b\"c \x41'", 'a\'b"c A', "'")
        self.check(r"'say \"hi\"'", 'say "hi"', "'")

    def test_single_quote_key_and_positions(self):
        src = r"""{'k\x41':'v""" + BU + '00e9\',"b":"w"}'
        r = S.parse(src)
        self.assertEqual(sorted(r[0]), ['b', 'kA'])
        v = r[0]['kA']
        self.assertEqual((v.v, v.q, src[v.a:v.b]), ('vé', "'", "'v" + BU + "00e9'"))
        w = r[0]['b']
        self.assertEqual((w.v, w.q, src[w.a:w.b]), ('w', '"', '"w"'))
        self.assertEqual(r[1], len(src))

    def test_bad_escapes_give_none(self):
        for bad in (r'"\x4"', r'"\xZZ"', r'"\u12"', r'"\U0011FFFF"', r'"\N{NO SUCH NAME}"', r'"\N"', r'"\q"', '"a\\'):
            warns = []
            self.assertIsNone(S.parse(bad, warns=warns), bad)
            self.assertTrue(warns, bad)

    def test_unclosed_and_empty(self):
        self.assertIsNone(S.parse('"abc'))
        self.assertIsNone(S.parse("'abc\\'"))
        self.assertEqual(S.parse('""')[0].v, '')
        self.assertEqual(S.parse("''")[0].v, '')

    # Bug de prod connu (reporté, 🔵) : une paire de surrogates 😀 n'est pas recombinée.
    @unittest.expectedFailure
    def test_surrogate_pair_is_combined(self):
        self.assertEqual(S.parse('"' + BU + 'D83D' + BU + 'DE00"')[0].v, '😀')

    # Bug de prod connu (reporté, 🔵) : encode laisse en clair les contrôles < U+0020 hors \n \r \t ; json.loads (strict) les refuse.
    @unittest.expectedFailure
    def test_encode_escapes_control_characters(self):
        self.assertEqual(json.loads(S.encode('a\x01b\x1f')), 'a\x01b\x1f')


class Reencode(unittest.TestCase):
    def test_snbt_double_quote(self):
        pre = 'title @a title '
        out, st = run(pre + '"Hello"', {'Hello': NASTY})
        self.assertEqual(st.translated, 1)
        r = S.parse(out, len(pre))
        self.assertEqual((r[0].v, r[0].q, r[1]), (NASTY, '"', len(out)))

    def test_snbt_compound_double_quote(self):
        pre = 'title @a title '
        out, st = run(pre + '{"text":"Hello","color":"red"}', {'Hello': NASTY})
        r = S.parse(out, len(pre))
        self.assertEqual((r[0]['text'].v, r[0]['color'].v, r[1]), (NASTY, 'red', len(out)))

    def test_snbt_single_quote(self):
        pre = 'summon zombie ~ ~ ~ '
        out, st = run(pre + "{CustomName:'Hello',Silent:1b}", {'Hello': NASTY})
        self.assertEqual(st.translated, 1)
        r = S.parse(out, len(pre))
        self.assertEqual((r[0]['CustomName'].v, r[0]['CustomName'].q, r[0]['Silent'].v, r[1]), (NASTY, "'", '1b', len(out)))

    def test_json_plain_line(self):
        pre = 'tellraw @a '
        out, st = run(pre + '{"text":"Hello","color":"red"}', {'Hello': NASTY})
        self.assertEqual(json.loads(out[len(pre):]), {'text': NASTY, 'color': 'red'})
        self.assertEqual(S.parse(out, len(pre))[0]['text'].v, NASTY)

    def test_json_old_format_component_in_string(self):
        pre = 'give @s stick[custom_name='
        out, st = run(pre + """'{"text":"Hello","bold":true}']""", {'Hello': NASTY})
        self.assertEqual(st.translated, 1)
        outer = S.string(out, len(pre))
        self.assertEqual(outer.q, "'")
        inner = json.loads(outer.v)                              # le JSON imbriqué se relit...
        self.assertEqual(inner, {'text': NASTY, 'bold': True})
        self.assertEqual(S.parse(outer.v)[0]['text'].v, NASTY)   # ... avec fl_snbt aussi, même valeur
        self.assertEqual(out[outer.b:], ']')

    def test_json_old_format_lore_string(self):
        pre = 'give @s stick[lore=['
        out, st = run(pre + """'"Hello"','"Hello"']]""", {'Hello': NASTY})
        self.assertEqual(st.translated, 2)
        first = S.string(out, len(pre))
        second = S.string(out, first.b + 1)
        for leaf in (first, second):
            self.assertEqual(json.loads(leaf.v), NASTY)
            self.assertEqual(S.parse(leaf.v)[0].v, NASTY)
        self.assertEqual(out[second.b:], ']]')

    def test_idempotent_second_pass_is_stable(self):
        # la sortie ré-encodée, retraduite avec une table sans effet, reste identique
        out, _ = run('title @a title {"text":"Hello"}', {'Hello': NASTY})
        again, st = run(out, {'Unrelated': 'x'})
        self.assertEqual(again, out)
        self.assertEqual(st.translated, 0)


class EmptyTableRoundtrip(unittest.TestCase):
    def test_real_lines_identical(self):
        for line in REAL:
            out, st = run(line, {})
            self.assertEqual(out, line, line)
            self.assertEqual((st.translated, st.errors, st.refused), (0, 0, 0), line)

    def test_real_lines_identical_with_unrelated_table(self):
        for line in REAL:
            out, st = run(line, {'Zzz absent': 'Rien'})
            self.assertEqual(out, line, line)
            self.assertEqual(st.translated, 0, line)

    def test_real_line_translated_then_only_text_changes(self):
        line = REAL[5]
        out, st = run(line, {'Brain Cactus': 'Cactus-Cerveau'})
        self.assertEqual((out, st.translated), (line.replace('Brain Cactus', 'Cactus-Cerveau'), 1))


if __name__ == '__main__':
    unittest.main()
