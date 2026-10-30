"""tools/floaty : traduction française branchée dans gen_floaty (fl_fr) et extraction des textes (fr_extract), sur une fausse carte en dossier
temporaire (voir FakeMap de test_floaty_gen.py) : table vide = sortie identique octet pour octet, une entrée = la seule occurrence visée,
clés protégées calculées sur les lignes réécrites, fr/ créé sans rien écraser, advancements et barres de boss, extraction.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'floaty'))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import fl_fr  # noqa: E402
import fl_tr  # noqa: E402
import fr_extract as X  # noqa: E402
import gen_floaty as G  # noqa: E402
import test_floaty_gen as TG  # noqa: E402  (module, pas FakeMap seul : unittest rejouerait ses tests ici)
from test_floaty_state import BARS, dat  # noqa: E402

TALK = '\n'.join([
    'tellraw @a [{"text":"<"},{"text":"Araxion"},{"text":"> Hello there."}]',
    'say Hello there.',
    'title @a title {"text":"Hello there."}',
    'setblock ~ ~ ~ chest{Command:"say Hello there."}',
    'execute if entity @a[name="Sword"] run tellraw @a "Hello there. Friend"',
    'give @s stick[custom_name=\'{"text":"Sword"}\']',
    'setblock 1 2 3 chest{lock:{components:{"minecraft:custom_name":"Sword"}}}',
    ''])
ADV = {'parent': 'main_quest:root', 'display': {'title': {'text': 'Quest title'}, 'description': 'Quest text', 'announce_to_chat': True},
       'criteria': {'c': {'trigger': 'minecraft:tick', 'conditions': {'player': [{'condition': 'x', 'name': 'Quest text'}]}}}}
HELLO = {'Hello there.': 'Bonjour.'}
TALK_LINES = (0, 1, 2, 3)                       # indices des lignes de talk.mcfunction qui portent exactement « Hello there. » dans un emplacement de texte


class Base(unittest.TestCase):
    """FakeMap (ses fixtures, sans ses tests) + npc/talk, npc/other et un advancement ; self.fr : dossier des traductions (absent au départ)."""
    FILES = {**TG.FakeMap.FILES, 'npc/function/talk.mcfunction': TALK, 'npc/function/other.mcfunction': 'say Hello there.\n',
             'main_quest/advancement/q3.json': json.dumps(ADV)}
    BIOMES = TG.FakeMap.BIOMES
    put = staticmethod(TG.FakeMap.put)
    tree = TG.FakeMap.tree

    setUp = TG.FakeMap.setUp

    def table(self, name='a.json', **data):
        self.put(self.fr / name, json.dumps(data or HELLO, ensure_ascii=False))

    def read(self, rel):
        return (self.repo / rel).read_text(encoding='utf-8')

    def lines(self, rel):
        return self.read('data/npc/function/' + rel + '.mcfunction').split('\n')

    def baseline(self):
        """Sortie d'avant la traduction (table=None) : {chemin : octets} ; le dépôt est ensuite remis comme au départ pour la relance."""
        G.generate(self.map, self.repo, table=None)
        return self.tree()


class Identity(Base):
    def test_empty_table_is_byte_identical_to_no_translation(self):
        before = self.baseline()
        st, n, *_ = G.generate(self.map, self.repo)                              # fr/ absent : table vide
        self.assertEqual(self.tree(), before)
        self.assertEqual((st.tr.translated, st.tr.refused), (0, 0))
        self.assertGreater(st.tr.missing, 0)                                      # des textes lus, aucun traduit
        self.assertEqual(sorted(p.name for p in self.fr.iterdir()), ['GLOSSAIRE.md', 'ctx.json', 'protected.txt'])
        G.generate(self.map, self.repo)                                           # fr/ présent mais vide de tables : même sortie
        self.assertEqual(self.tree(), before)

    def test_table_none_reads_and_writes_nothing_of_fr(self):
        st, n, *_ = G.generate(self.map, self.repo, table=None)
        self.assertIsNone(st.tr)
        self.assertNotIn('fr', n)
        self.assertFalse(self.fr.exists())


class OneEntry(Base):
    def test_only_the_targeted_occurrences_change(self):
        before = self.baseline()
        self.table()
        st, *_ = G.generate(self.map, self.repo)
        after = self.tree()
        changed = {p for p in after if after[p] != before.get(p)}
        self.assertEqual(changed, {'data/npc/function/talk.mcfunction', 'data/npc/function/other.mcfunction'})
        old, new = before['data/npc/function/talk.mcfunction'].decode().split('\n'), self.lines('talk')
        self.assertEqual(new, [l.replace('Hello there.', 'Bonjour.') if i in TALK_LINES else l for i, l in enumerate(old)])
        self.assertIn('Bonjour.', new[3])
        self.assertEqual(self.lines('other')[0], 'tellraw @a[tag=mg.flw] "Bonjour."')
        self.assertEqual(st.tr.translated, 5)                                      # 4 de talk + 1 de other ; « Hello there. Friend » n'est pas la clé
        self.assertIn('Hello there. Friend', new[4])
        self.assertEqual(self.tree(), after)                                       # idempotent

    def test_ctx_overrides_one_function_and_may_live_in_fr(self):
        self.table()
        self.put(self.fr / 'ctx.json', json.dumps({'npc:other': {'Hello there.': 'Salut.'}}))
        G.generate(self.map, self.repo)
        self.assertEqual(self.lines('other')[0], 'tellraw @a[tag=mg.flw] "Salut."')
        self.assertIn('Bonjour.', self.lines('talk')[1])

    def test_advancement_title_translated_criteria_names_protected(self):
        self.table('b.json', **{'Quest title': 'Titre', 'Quest text': 'Texte'})
        st, *_ = G.generate(self.map, self.repo)
        d = json.loads(self.read('data/main_quest/advancement/q3.json'))
        self.assertEqual(d['display']['title'], {'text': 'Titre'})
        self.assertEqual(d['display']['description'], 'Quest text')               # comparée dans un critère : jamais traduite
        self.assertIs(d['display']['announce_to_chat'], False)
        self.assertEqual(d['parent'], 'main_quest:root')
        self.assertIn(G.IN_DIMENSION, d['criteria']['c']['conditions']['player'])
        self.assertEqual((st.tr.translated, st.tr.refused), (1, 1))

    def test_install_bossbar_is_translated(self):
        (self.map / 'data' / 'minecraft').mkdir(parents=True, exist_ok=True)
        (self.map / 'data' / 'minecraft' / 'custom_boss_events.dat').write_bytes(dat(BARS))
        self.table('c.json', A='Alpha')
        G.generate(self.map, self.repo)
        self.assertIn('bossbar add boss:a {"text":"Alpha","bold":true}\n', self.read('data/floaty/function/install.mcfunction'))


class Protection(Base):
    def test_compared_names_refused_and_written_to_protected_txt(self):
        before = self.baseline()
        self.table('d.json', Sword='Epee')
        st, n, *_ = G.generate(self.map, self.repo)
        self.assertEqual(self.tree(), before)
        self.assertEqual((st.tr.translated, st.tr.refused, n['fr']['refused']), (0, 1, 1))
        text = (self.fr / 'protected.txt').read_text(encoding='utf-8')
        self.assertIn('"Sword"\n', text.split(fl_fr.MARK)[1])

    def test_manual_section_kept_and_applied(self):
        before = self.baseline()
        self.put(self.fr / 'protected.txt', '# a la main\n"Hello there."\n' + fl_fr.MARK + '\n"old key"\n')
        self.table()
        st, n, *_ = G.generate(self.map, self.repo)
        self.assertEqual(self.tree(), before)                                      # la clé manuelle bloque la traduction
        text = (self.fr / 'protected.txt').read_text(encoding='utf-8')
        manual, auto = text.split(fl_fr.MARK)
        self.assertEqual(manual, '# a la main\n"Hello there."\n')
        self.assertNotIn('old key', auto)                                          # section calculée : régénérée
        self.assertEqual(n['fr']['manual'], 1)
        G.generate(self.map, self.repo)
        self.assertEqual((self.fr / 'protected.txt').read_text(encoding='utf-8'), text)

    def test_bad_protected_line_is_refused(self):
        self.put(self.fr / 'protected.txt', 'pas du json\n')
        with self.assertRaises(ValueError):
            G.generate(self.map, self.repo)

    def test_fr_created_with_files_never_overwritten(self):
        self.put(self.fr / 'ctx.json', '{"npc:other": {}}')
        self.put(self.fr / 'GLOSSAIRE.md', 'le mien')
        G.generate(self.map, self.repo)
        self.assertEqual((self.fr / 'ctx.json').read_text(encoding='utf-8'), '{"npc:other": {}}')
        self.assertEqual((self.fr / 'GLOSSAIRE.md').read_text(encoding='utf-8'), 'le mien')
        self.assertTrue((self.fr / 'protected.txt').exists())

    def test_conflicting_table_stops_before_any_write(self):
        G.generate(self.map, self.repo)
        before = self.tree()
        self.table('a.json')
        self.table('b.json', **{'Hello there.': 'Autre'})
        with self.assertRaises(ValueError):
            G.generate(self.map, self.repo)
        self.assertEqual(self.tree(), before)


class TableAndWarnings(unittest.TestCase):
    def test_load_skips_ctx_json_inside_fr_dir(self):
        with tempfile.TemporaryDirectory() as t:
            fr = Path(t) / 'fr'
            TG.FakeMap.put(fr / 'a.json', '{"Hello": "Salut"}')
            TG.FakeMap.put(fr / 'ctx.json', '{"a:b": {"Hello": "Allô"}}')
            tb = fl_tr.Table.load(fr, fr / 'ctx.json')
            self.assertEqual((tb.get('x:y', 'Hello'), tb.get('a:b', 'Hello')), ('Salut', 'Allô'))

    def test_unreadable_line_is_reported_and_all_its_strings_protected(self):
        with tempfile.TemporaryDirectory() as t:
            pr = fl_fr.protect([('a', 'b', ['tellraw @a[tag=x {"text":"Broken"}'])], set(), Path(t) / 'absent')
        self.assertEqual(len(pr.warns), 1)
        self.assertIn('Broken', pr.keys)                                           # illisible : toutes ses chaînes sont protégées


class Extract(Base):
    def run_extract(self):
        out = self.fr.parent / 'out'
        rows, text = X.extract(self.map, self.repo, self.fr, out)
        return rows, text, out

    def entries(self, out, ns):
        return {e['key']: e for e in map(json.loads, (out / f'todo_{ns}.jsonl').read_text(encoding='utf-8').splitlines())}

    def test_extract_lists_keys_with_context_and_writes_nothing_to_the_repo(self):
        G.generate(self.map, self.repo, table=None)
        before = self.tree()
        rows, text, out = self.run_extract()
        self.assertEqual(self.tree(), before)                                      # ni data/, ni fr/ : rien d'écrit hors de out
        self.assertFalse(self.fr.exists())
        npc = self.entries(out, 'npc')
        hello = npc['Hello there.']
        self.assertEqual((hello['n'], hello['slot']), (5, 'tellraw'))
        self.assertEqual(hello['where'], 'npc:other:1')
        self.assertEqual(npc['Araxion']['where'], 'npc:talk:1')
        self.assertEqual(npc['Araxion']['message'], '<Araxion> Hello there.')
        self.assertEqual(npc['Hello there. Friend']['where'], 'npc:talk:5')
        self.assertNotIn('Sword', npc)                                             # protégée : jamais à traduire
        self.assertEqual(self.entries(out, 'main_quest')['Quest title']['slot'], 'advancement title')
        self.assertIn(f'occurrences : {len(rows)} ;', text)
        self.assertIn('npc', (out / 'stats.txt').read_text(encoding='utf-8'))

    def test_extracted_keys_are_exactly_the_ones_the_table_meets(self):
        rows, _, out = self.run_extract()
        keys = {r[0] for r in rows}
        self.table('all.json', **{k: 'FR ' + k for k in keys})
        st, *_ = G.generate(self.map, self.repo)
        self.assertEqual((st.tr.missing, st.tr.translated), (0, len(rows)))


if __name__ == '__main__':
    unittest.main()
