"""tools/floaty : fl_snbt (lecteur SNBT à positions) et fl_tr (traduction française des textes visibles : emplacements, zones protégées,
table fr/*.json + ctx.json). Les lignes FIX sont de vraies lignes de la sortie data/ (une par forme de texte relevée dans la carte).
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / 'tools' / 'floaty'))
import fl_snbt as S  # noqa: E402
import fl_tr as T  # noqa: E402

FIX = {
    'split': r'''execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Araxion","color":"#D47453"},{"text":"> A little man just dug through the wall with frightening speed. All he said to me was \"hello, you've got a beautiful light-up hat, I don't have no parents,\" or something to that effect, before zipping away down that hole and into the tunnels beneath ","color":"white"},{"text":"Valor Tower","color":"red"},{"text":".","color":"white"}]''',
    'keybind': r'''execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Hopper","color":"green"},{"text":"> So, you've come to me for jumping advice, eh? Shhh sh sh it's alright, I'll teach ya. My secret is, ready for this? My secret is pressing ","color":"white"},{"keybind":"key.jump"},{"text":". Pretty cool right? Try it!"}]''',
    'lore': r'''execute as @a[gamemode=!spectator,tag=mg.flw] run summon item ~ 89 ~ {Invulnerable:1b,Item:{id:"minecraft:lapis_lazuli",count:1,components:{"minecraft:custom_name":{"color":"aqua","text":"Blitzite"},"minecraft:lore":["A shard of","frozen lightning"]}}}''',
    'give': r'''give @p[tag=mg.flw] lever[can_place_on={blocks:'emerald_block'},tooltip_display={hidden_components:[can_place_on]},custom_name='Small Key',lore=['Can be placed on a','keyhole in this area'],enchantment_glint_override=true] 1''',
    'entity': r'''summon breeze ~ ~ ~ {PersistenceRequired:1b,Tags:["enemy","p_smoke"],CustomName:"Promised Smoke"}''',
    'plain': r'''execute as @a[scores={DeathFlag=1},tag=mg.flw] if score @s DeathCount matches 2..68 run tellraw @a[tag=mg.flw] [{"selector":"@s"}," has died ",{"score":{"name":"@s","objective":"DeathCount"}}," times"]''',
    'subtitle': r'''title @a[tag=mg.flw] subtitle "Thanks for playing!"''',
    'actionbar': r'''title @a[tag=mg.flw] actionbar {"text":"The evil has been driven from this place...","italic":true,"color":"gold"}''',
    'sign': r'''execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ if items entity @p[gamemode=!spectator,tag=mg.flw] weapon.mainhand breeze_rod[minecraft:custom_model_data={strings:['1']}] if score abnormazoid_1 bool matches 0..1 run setblock -451 27 37 minecraft:oak_wall_sign[facing=south,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:["","","",""]},components:{},front_text:{color:"white",has_glowing_text:1b,messages:["",{color:"gold",text:"Smilewalker"},"",{italic:1b,text:"Glen"}]},is_waxed:0b}''',
    'display': r'''summon text_display -10340 92 446 {NoGravity:1b,Silent:1b,billboard:"center",Tags:["pretzel_letter","new"],brightness:{sky:15,block:15},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[3f,3f,3f]},text:{"bold":false,"text":"A"}}''',
    'old': r'''give @s writable_book[custom_name='{"bold":true,"color":"aqua","text":"Adventure Notes"}',lore=['"For writing down"','"important information"','"along your journey!"'],writable_book_content={pages:[""]}]''',
    'command': r'''setblock ~ ~ ~ minecraft:command_block[conditional=false,facing=down]{Command:'execute positioned ~ ~2 ~ as @a[distance=..10,tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Blabber Stone","color":"yellow"},{"text":"> ","color":"white"}]',CustomName:'{"text":"@"}',LastExecution:47611700L,SuccessCount:0,TrackOutput:1b,UpdateLastExecution:1b,auto:0b,conditionMet:1b,powered:0b} replace''',
    'newline': r'''execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Spoom-Ee IV","color":"#D47453"},{"text":"> I... have not.","color":"white"}]''',
    'quote': r'''tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"?","color":"yellow"},{"color":"white","text":"> Welcome to the halls of the dead, \"hero.\""},{"text":" ⇒","color":"light_purple"}]''',
    'hover': r'''tellraw @a[tag=mg.flw] [{"color":"red","text":"🗡 "},{"color":"dark_aqua","text":"You are playing version "},{"bold":true,"color":"red","text":"1.1"},{"color":"dark_aqua","text":"! "},{"click_event":{"action":"open_url","url":"https://docs.google.com/spreadsheets/d/1m5XCaQkFlEDZ0vLP0hi3wWfV4Ne-iPye0oSr94pXmc8/edit?usp=sharing"},"color":"aqua","hover_event":{"action":"show_text","value":[{"text":"https://docs.google.com/spreadsheets/d/1m5XCaQkFlEDZ0vLP0hi3wWfV4Ne-iPye0oSr94pXmc8/edit?usp=sharing"}]},"text":"Click here to check if there's an update available","underlined":true},{"color":"dark_aqua","text":"."},{"color":"red","text":" 🗡"}]''',
    'lock': r'''setblock -9987 200 254 minecraft:green_shulker_box[facing=east]{components:{},lock:{components:{"minecraft:custom_name":'"Ximglie"'}}}''',
    'nbt': r'''execute positioned 142 59 -54 as @a[scores={BellRung=1..},distance=..10,tag=mg.flw] if entity @s[nbt={SelectedItem:{id:"minecraft:mace",count:1,components:{"minecraft:custom_name":"Knowledge & Learning"}}}] run playsound minecraft:item.mace.smash_ground_heavy master @a[tag=mg.flw] 142 59 -54 1 0.1''',
    'clear': r'''clear @a[tag=spine_showing,tag=mg.flw] flint[minecraft:custom_model_data={strings:['16']}]''',
    'merge': r'''data merge block -11710 218 294 {front_text:{messages:["Virometer:","",{"score":{"name":"ta_lab_a_results","objective":"Value"},"color":"dark_aqua","bold":true},""]}}''',
    'bossbar': r'''bossbar add boss:attestor {"color":"gold","text":"Attestor Golem","italic":true}''',
}


def leaves_of(line):
    """Tous les Leaf d'une ligne (chaînes de premier niveau, et chaînes des groupes SNBT lisibles)."""
    i, out = 0, []
    while i < len(line):
        if line[i] in '"\'':
            leaf = S.string(line, i)
            if leaf is None:
                break
            out.append(leaf)
            i = leaf.b
            continue
        r = S.parse(line, i) if line[i] in '{[' else None      # un `[...]` d'item (clé=valeur) n'est pas du SNBT : on avance d'un caractère
        if r:
            out.extend(S.leaves(r[0]))
        i = r[1] if r else i + 1
    return out


def run(line, glob=None, ctx=None, protected=(), ctx_id='t:f'):
    """-> (ligne traduite, Stats) avec une petite table : glob {anglais: français}, ctx {'ns:chemin': {anglais: français}}."""
    tb = T.Table(protected)
    for k, v in (glob or {}).items():
        tb.add(k, v, 'test')
    for cid, d in (ctx or {}).items():
        for k, v in d.items():
            tb.add(k, v, 'test', cid)
    st = T.Stats(tb)
    return T.translate_line(line, ctx_id, st), st


class Snbt(unittest.TestCase):
    def test_roundtrip_byte_for_byte(self):
        for name, line in FIX.items():
            ls = leaves_of(line)
            self.assertTrue(ls, name)
            for lf in ls:
                self.assertEqual(S.encode(lf.v, lf.q), line[lf.a:lf.b], name)
            spliced = line
            for lf in sorted(ls, reverse=True):
                spliced = spliced[:lf.a] + S.encode(lf.v, lf.q) + spliced[lf.b:]
            self.assertEqual(spliced, line, name)

    def test_decode_escapes_positions_and_types(self):
        text = r"""x:{a:'l\'été \\ é\n',"b c":["q\"z"],d:1b,e:[I;1,2],f:true}"""
        node, end = S.parse(text, 2)
        self.assertEqual(end, len(text))
        self.assertEqual(node['a'].v, "l'été \\ é\n")
        self.assertEqual((node['a'].q, node['a'].a), ("'", 5))
        self.assertEqual(text[node['a'].a:node['a'].b], r"""'l\'été \\ é\n'""")
        self.assertEqual(node['b c'][0].v, 'q"z')
        self.assertEqual((node['d'].v, node['f'].v), ('1b', 'true'))
        self.assertIsInstance(node['d'], S.Raw)
        self.assertEqual((node['e'].kind, [x.v for x in node['e']]), ('I', ['1', '2']))

    def test_errors_give_none_and_warning_never_raise(self):
        for bad in ('"abc', "{a:'x", '[1,2', '{a 1}', r'"\q"', '{"a":}', '[' * 5000):
            w = []
            self.assertIsNone(S.parse(bad, 0, w), bad[:20])
            self.assertEqual(len(w), 1, bad[:20])

    def test_encode_quote_and_escapes(self):
        self.assertEqual(S.encode('l\'a "b" \\ \n', "'"), r"""'l\'a "b" \\ \n'""")
        self.assertEqual(S.encode('l\'a "b"', '"'), r'''"l'a \"b\""''')
        for q in '"\'':
            self.assertEqual(S.string(S.encode('é\n\t\\x\'"', q), 0).v, 'é\n\t\\x\'"')


class Slots(unittest.TestCase):
    def test_split_components(self):
        out, st = run(FIX['split'], {'Valor Tower': 'Tour Valor', 'Araxion': 'Araxion'})
        self.assertEqual(out, FIX['split'].replace('"Valor Tower"', '"Tour Valor"'))
        self.assertEqual((st.translated, st.errors), (2, 0))

    def test_dialogue_prefix_edge_spaces_and_escaped_quotes(self):
        line = r'tellraw @a [{"text":"> He said \"hi,\" to me ","color":"white"},{"text":" has died "}]'
        out, st = run(line, {'He said "hi," to me': 'Il a dit \"salut\" à moi', 'has died': 'est mort'})
        self.assertEqual(out, r'tellraw @a [{"text":"> Il a dit \"salut\" à moi ","color":"white"},{"text":" est mort "}]')
        self.assertEqual(st.translated, 2)

    def test_keybind_in_sentence(self):
        out, _ = run(FIX['keybind'], {'. Pretty cool right? Try it!': '. Sympa, non ? Essaie !'})
        self.assertEqual(out, FIX['keybind'].replace('. Pretty cool right? Try it!', '. Sympa, non ? Essaie !'))

    def test_lore_list_and_custom_name_key(self):
        out, _ = run(FIX['lore'], {'Blitzite': 'Foudrite', 'A shard of': 'Un éclat de', 'frozen lightning': 'foudre gelée'})
        self.assertEqual(out, FIX['lore'].replace('Blitzite', 'Foudrite').replace('A shard of', 'Un éclat de').replace('frozen lightning', 'foudre gelée'))

    def test_item_brackets_with_french_apostrophe(self):
        out, _ = run(FIX['give'], {'Small Key': 'Petite clé', 'Can be placed on a': "Se pose sur l'", 'keyhole in this area': 'serrure'})
        self.assertEqual(out, FIX['give'].replace("'Small Key'", "'Petite clé'").replace("'Can be placed on a'", r"'Se pose sur l\''").replace("'keyhole in this area'", "'serrure'"))
        leaf = S.parse(out, out.index('lore=') + 5)[0][0]
        self.assertEqual(leaf.v, "Se pose sur l'")

    def test_entity_custom_name(self):
        out, _ = run(FIX['entity'], {'Promised Smoke': 'Fumée promise', 'enemy': 'ennemi', 'p_smoke': 'x'})
        self.assertEqual(out, FIX['entity'].replace('Promised Smoke', 'Fumée promise'))

    def test_plain_string_elements_of_tellraw_list(self):
        out, st = run(FIX['plain'], {'has died': 'est mort', 'times': 'fois', 'DeathCount': 'x', '@s': 'x'})
        self.assertEqual(out, FIX['plain'].replace('" has died "', '" est mort "').replace('" times"', '" fois"'))
        self.assertEqual(st.translated, 2)

    def test_title_subtitle_actionbar(self):
        tb = {'Thanks for playing!': 'Merci d\'avoir joué !', 'The evil has been driven from this place...': 'Le mal a quitté ces lieux...'}
        self.assertEqual(run(FIX['subtitle'], tb)[0], 'title @a[tag=mg.flw] subtitle "Merci d\'avoir joué !"')
        self.assertEqual(run(FIX['actionbar'], tb)[0], FIX['actionbar'].replace('The evil has been driven from this place...', 'Le mal a quitté ces lieux...'))
        self.assertEqual(run('title @a[tag=mg.flw] times 5 40 5', tb)[0], 'title @a[tag=mg.flw] times 5 40 5')

    def test_sign_messages_bare_keys(self):
        out, _ = run(FIX['sign'], {'Smilewalker': 'Marchesourire', 'Glen': 'Glen', 'white': 'blanc', 'center': 'x'})
        self.assertEqual(out, FIX['sign'].replace('"Smilewalker"', '"Marchesourire"'))

    def test_text_display_text_key(self):
        out, _ = run(FIX['display'], {'A': 'Ah', 'pretzel_letter': 'x', 'new': 'x'})
        self.assertEqual(out, FIX['display'].replace('"text":"A"', '"text":"Ah"'))

    def test_old_format_json_in_string(self):
        out, _ = run(FIX['old'], {'Adventure Notes': "Carnet d'aventure", 'For writing down': 'Pour noter'})
        self.assertEqual(out, FIX['old'].replace('"text":"Adventure Notes"', r'''"text":"Carnet d\'aventure"''').replace('\'"For writing down"\'', '\'"Pour noter"\''))

    def test_nested_command_block(self):
        out, _ = run(FIX['command'], {'Blabber Stone': "Pierre d'écho"})
        self.assertEqual(out, FIX['command'].replace('Blabber Stone', r"Pierre d\'écho"))
        cmd = S.parse(out, out.index('Command:') + 8)[0].v
        self.assertIn('{"text":"Pierre d\'écho","color":"yellow"}', cmd)

    def test_newline_and_quotes_escaped_and_reread(self):
        line = r'tellraw @a {"text":"Ligne un\nLigne deux"}'
        out, _ = run(line, {'Ligne un\nLigne deux': 'Un\nDeux "x" \\ fin'})
        self.assertEqual(out, r'tellraw @a {"text":"Un\nDeux \"x\" \\ fin"}')
        self.assertEqual(S.parse(out, out.index('{'))[0]['text'].v, 'Un\nDeux "x" \\ fin')
        out, _ = run(FIX['quote'], {'Welcome to the halls of the dead, "hero."': 'Bienvenue, "héros."'})
        self.assertEqual(out, FIX['quote'].replace(r'Welcome to the halls of the dead, \"hero.\"', r'Bienvenue, \"héros.\"'))

    def test_hover_value_translated_emoji_and_click_kept(self):
        tb = {"Click here to check if there's an update available": 'Cliquez ici', 'You are playing version': 'Version jouée'}
        out, _ = run(FIX['hover'], tb)
        self.assertEqual(out, FIX['hover'].replace("Click here to check if there's an update available", 'Cliquez ici').replace('You are playing version', 'Version jouée'))
        line = 'tellraw @a {"text":"a","hover_event":{"action":"show_text","value":{"text":"Foo"}},"click_event":{"action":"open_url","url":"Foo"}}'
        self.assertEqual(run(line, {'Foo': 'Fou'})[0], line.replace('"value":{"text":"Foo"}', '"value":{"text":"Fou"}'))
        item = 'tellraw @a {"text":"a","hover_event":{"action":"show_item","id":"Foo","contents":{"text":"Foo"}}}'
        self.assertEqual(run(item, {'Foo': 'Fou'})[0], item)

    def test_bossbar_names_only(self):
        out, _ = run(FIX['bossbar'], {'Attestor Golem': 'Golem attestateur'})
        self.assertEqual(out, FIX['bossbar'].replace('Attestor Golem', 'Golem attestateur'))
        tb = {'Golem': 'Gol', 'gold': 'or', 'red': 'rouge'}
        self.assertEqual(run('bossbar set boss:x name {"text":"Golem"}', tb)[0], 'bossbar set boss:x name {"text":"Gol"}')
        for same in ('bossbar set boss:x color red', 'bossbar set boss:x players @a[tag=mg.flw]', 'bossbar set boss:x visible true'):
            self.assertEqual(run(same, tb)[0], same)

    def test_ctx_before_global(self):
        out, _ = run('tellraw @a {"text":"Key"}', {'Key': 'Clé'}, {'a:b': {'Key': 'Clef'}}, ctx_id='a:b')
        self.assertEqual(out, 'tellraw @a {"text":"Clef"}')
        self.assertEqual(run('tellraw @a {"text":"Key"}', {'Key': 'Clé'}, {'a:b': {'Key': 'Clef'}}, ctx_id='c:d')[0], 'tellraw @a {"text":"Clé"}')

    def test_tree_title_description(self):
        tree = {'display': {'title': {'text': 'Hello', 'extra': ['World']}, 'description': 'Hello'}, 'criteria': {'c': {'conditions': {'x': 'Hello'}}}}
        st = T.Stats(T.Table())
        st.table.add('Hello', 'Bonjour', 't')
        st.table.add('World', 'Monde', 't')
        out = T.translate_tree(tree, 'a:b', st)
        self.assertEqual(out['display'], {'title': {'text': 'Bonjour', 'extra': ['Monde']}, 'description': 'Bonjour'})
        self.assertEqual(out['criteria'], {'c': {'conditions': {'x': 'Hello'}}})


class Inverse(unittest.TestCase):
    """Ce qui ne doit JAMAIS bouger, même avec une table qui contient la chaîne."""
    TB = {'Ximglie': 'X', 'Knowledge & Learning': 'Y'}

    def test_lock_and_nbt_lines_unchanged(self):
        for name in ('lock', 'nbt'):
            out, st = run(FIX[name], self.TB)
            self.assertEqual(out, FIX[name], name)
            self.assertEqual((st.translated, st.missing), (0, 0), name)

    def test_items_clear_data_predicates_unchanged(self):
        lines = ["clear @s stick[custom_name='Ximglie']", "execute if items entity @s weapon.mainhand stick[custom_name='Ximglie'] run function a:b",
                 'execute unless items entity @s container.* stick[lore=["Ximglie"]] run function a:b',
                 'execute if data entity @s {CustomName:"Ximglie"} run function a:b', "execute if data block 1 2 3 Items[{components:{custom_name:'Ximglie'}}] run function a:b",
                 'execute if entity @e[name="Ximglie",limit=1] run function a:b', 'execute if entity @e[name=Ximglie] run function a:b']
        for line in lines:
            self.assertEqual(run(line, self.TB)[0], line)
        self.assertEqual(sorted(T.protected_keys(lines)[0]), ['Ximglie'])

    def test_protected_key_refused_everywhere_and_counted(self):
        prot = T.protected_keys([FIX['lock'], FIX['nbt']])[0]
        self.assertTrue({'Ximglie', 'Knowledge & Learning'} <= prot)
        line = "give @s stick[custom_name='Ximglie']"
        out, st = run(line, self.TB, protected=prot)
        self.assertEqual((out, st.refused, st.translated), (line, 1, 0))
        self.assertEqual(st.table.refused, {'Ximglie', 'Knowledge & Learning'})
        self.assertEqual(run(line, self.TB)[0], "give @s stick[custom_name='X']")

    def test_criteria_strings_are_protected(self):
        tree = {'criteria': {'c': {'conditions': {'items': [{'components': {'minecraft:custom_name': 'Ximglie'}}]}}}, 'display': {'title': 'Ximglie'}}
        self.assertEqual(T.protected_keys([], [tree])[0], {'Ximglie'})     # `display` n'y est pas : seuls les criteria comptent

    def test_click_score_selector_keybind_translate_nbt_never_translated(self):
        line = 'tellraw @a [{"score":{"name":"Hello","objective":"Hello"}},{"selector":"Hello"},{"keybind":"Hello"},{"translate":"Hello"},{"nbt":"Hello","storage":"a:b"},{"click_event":{"action":"run_command","command":"/say Hello","url":"Hello"}}]'
        out, st = run(line, {'Hello': 'Bonjour', 'say Hello': 'x', '/say Hello': 'x'})
        self.assertEqual((out, st.translated, st.missing), (line, 0, 0))

    def test_unclosed_string_keeps_line_and_warns(self):
        for line in ('tellraw @a [{"text":"Hello},{"text":"World"}]', 'tellraw @a {"text":"Hello"} {', "tellraw @a [{'text':'Hello}]"):
            out, st = run(line, {'Hello': 'Bonjour', 'World': 'Monde'})
            self.assertEqual((out, st.errors, st.translated), (line, 1, 0))
            self.assertEqual(st.warns[0][1], line)

    def test_comment_and_non_command_words_untouched(self):
        for line in ('# tellraw @a {"text":"Hello"} CustomName:"Hello"', '  #title @a title "Hello"', 'schedule clear a:b', 'data modify storage a:b title set value "Hello"',
                     'scoreboard players set title tellraw 1', 'execute if entity @e[tag="title",name="Hello"] run say "Hello"'):
            self.assertEqual(run(line, {'Hello': 'Bonjour'})[0], line, line)

    def test_empty_table_changes_nothing(self):
        for name, line in FIX.items():
            out, st = run(line)
            self.assertEqual((out, st.translated, st.errors), (line, 0, 0), name)

    def test_numbers_symbols_and_empty_texts_are_not_missing(self):
        out, st = run('tellraw @a ["", {"text":"<"}, {"text":" ⇒"}, {"text":"12"}, "...", {"text":"> "}]')
        self.assertEqual(st.missing, 0)


class TableLoad(unittest.TestCase):
    def write(self, d, name, data):
        (Path(d) / name).write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')

    def test_load_normalizes_keys_and_applies_ctx_first(self):
        with tempfile.TemporaryDirectory() as d:
            fr = Path(d) / 'fr'
            fr.mkdir()
            self.write(fr, 'a.json', {'> Hello ': 'Salut', 'Same': 'Pareil'})
            self.write(fr, 'b.json', {'Same': 'Pareil', 'Ximglie': 'X'})       # même valeur dans deux fichiers : pas un conflit
            self.write(d, 'ctx.json', {'a:b': {'Hello': 'Allô'}})
            tb = T.Table.load(fr, Path(d) / 'ctx.json', {'Ximglie'})
            self.assertEqual((tb.get('x:y', 'Hello'), tb.get('a:b', 'Hello'), tb.get('a:b', 'Same')), ('Salut', 'Allô', 'Pareil'))
            self.assertEqual((tb.get('x:y', 'Ximglie'), tb.refused), (None, {'Ximglie'}))

    def test_conflicting_duplicate_between_files_is_refused(self):
        with tempfile.TemporaryDirectory() as d:
            self.write(d, 'a.json', {'Hello': 'Salut'})
            self.write(d, 'b.json', {' Hello': 'Allô'})
            with self.assertRaises(ValueError) as cm:
                T.Table.load(d)
            self.assertIn('a.json', str(cm.exception))
            self.assertIn('b.json', str(cm.exception))

    def test_duplicate_inside_one_file_and_bad_value_are_refused(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / 'a.json').write_text('{"Hello": "Salut", "Hello": "Allô"}', encoding='utf-8')
            with self.assertRaises(ValueError):
                T.Table.load(d)
        with tempfile.TemporaryDirectory() as d:
            self.write(d, 'a.json', {'Hello': 3})
            with self.assertRaises(ValueError):
                T.Table.load(d)


if __name__ == '__main__':
    unittest.main()
