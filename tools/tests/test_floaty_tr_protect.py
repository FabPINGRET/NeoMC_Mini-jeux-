"""tools/floaty : zones protégées de fl_scan et cas inverses de leur correctif (`/` de tête, `if|unless block`, filtres de fill / clone, clé
`"lock"` entre guillemets, ligne illisible). Chaque test pose la zone protégée (jamais traduite) ET son cas inverse (le texte voisin l'est).
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v
"""
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / 'tools' / 'floaty'))
import fl_scan as C  # noqa: E402
import fl_tr as T  # noqa: E402
from test_floaty_tr import FIX, run  # noqa: E402

TB = {'Ximglie': 'X', 'Hello': 'Bonjour'}


def keys_of(line):
    """Clés protégées relevées par fl_scan sur une ligne."""
    prot = set()
    C.scan(line, prot)
    return prot


class SlashAndPosition(unittest.TestCase):
    def test_leading_slash_protects_clear_predicate(self):
        line = '''setblock ~ ~ ~ command_block{Command:"/clear @a stick[custom_name='Ximglie']"}'''
        self.assertEqual(run(line, TB)[0], line)
        self.assertEqual(T.protected_keys([line])[0], {'Ximglie'})
        for bare in ("/clear @a stick[custom_name='Ximglie']", "$/clear @a stick[custom_name='Ximglie']", "execute as @a run /clear @s stick[lore=['Ximglie']]"):
            self.assertEqual(run(bare, TB)[0], bare, bare)
            self.assertEqual(keys_of(bare), {'Ximglie'}, bare)

    def test_leading_slash_tellraw_and_title_translated(self):
        line = '''setblock ~ ~ ~ command_block{Command:'/tellraw @a "Hello"'}'''
        out, st = run(line, TB)
        self.assertEqual((out, st.translated), (line.replace('Hello', 'Bonjour'), 1))
        self.assertEqual(run('/title @a title "Hello"', TB)[0], '/title @a title "Bonjour"')
        self.assertEqual(run('execute as @a run /tellraw @a "Hello"', TB)[0], 'execute as @a run /tellraw @a "Bonjour"')

    def test_function_path_and_mid_line_slash_are_not_commands(self):
        for line in ("function a:b/clear @a stick[custom_name='Ximglie']", "function a:b/c/clear @a stick[lore=['Ximglie']]",
                     "say /clear @a stick[custom_name='Ximglie']", "say http://clear @a stick[custom_name='Ximglie']"):
            self.assertEqual(keys_of(line), set(), line)
        self.assertEqual(run("function a:b/clear @a stick[custom_name='Ximglie']", TB)[0], "function a:b/clear @a stick[custom_name='X']")


class BlockPredicate(unittest.TestCase):
    def test_if_block_predicate_unchanged(self):
        for line in ('execute if block 1 2 3 chest{CustomName:"Ximglie"} run say hi', 'execute if block ~ ~1 ~ chest{CustomName:"Ximglie"} run say hi',
                     'execute unless block ^ ^ ^-1 minecraft:chest[facing=north]{"minecraft:custom_name":"Ximglie"} run say hi',
                     'execute if block ~-1 ~ ~2 oak_sign{front_text:{messages:["Ximglie","","",""]}} run say hi',
                     "execute if block 1 2 3 barrel{components:{custom_name:'Ximglie'}} run say hi"):
            self.assertEqual(run(line, TB)[0], line, line)
            self.assertIn('Ximglie', keys_of(line), line)

    def test_text_after_the_predicate_still_translated(self):
        line = 'execute if block ~ ~1 ~ chest{CustomName:"Ximglie"} run tellraw @a "Hello"'
        self.assertEqual(run(line, TB)[0], line.replace('"Hello"', '"Bonjour"'))
        free = 'execute if block 1 2 3 stone run tellraw @a "Hello"'
        self.assertEqual((run(free, TB)[0], keys_of(free)), (free.replace('Hello', 'Bonjour'), set()))
        self.assertEqual(run('execute if block 1 2', TB)[0], 'execute if block 1 2')       # trop court : rien à protéger, rien d'abîmé


class FillCloneFilter(unittest.TestCase):
    def test_fill_replace_filter_unchanged_placed_block_translated(self):
        line = 'fill 1 2 3 4 5 6 chest{CustomName:"Hello"} replace barrel{CustomName:"Ximglie"}'
        self.assertEqual(run(line, TB)[0], 'fill 1 2 3 4 5 6 chest{CustomName:"Bonjour"} replace barrel{CustomName:"Ximglie"}')
        self.assertEqual(keys_of(line), {'Ximglie'})
        tilde = 'execute at @s run fill ~ ~ ~ ~1 ~1 ~1 stone replace chest{front_text:{messages:["Ximglie"]}}'
        self.assertEqual(run(tilde, TB)[0], tilde)
        self.assertEqual(keys_of(tilde), {'Ximglie'})

    def test_fill_without_filter_translates_everything(self):
        for line in ('fill 1 2 3 4 5 6 chest{CustomName:"Hello"}', 'fill 1 2 3 4 5 6 chest{CustomName:"Hello"} replace', 'fill 1 2 3 4 5 6 chest{CustomName:"Hello"} keep'):
            self.assertEqual(run(line, TB)[0], line.replace('Hello', 'Bonjour'), line)
            self.assertEqual(keys_of(line), set(), line)

    def test_clone_filtered_unchanged(self):
        line = 'clone 1 2 3 4 5 6 7 8 9 filtered chest{CustomName:"Ximglie"} move'
        self.assertEqual((run(line, TB)[0], keys_of(line)), (line, {'Ximglie'}))
        dims = 'clone from minecraft:overworld 1 2 3 4 5 6 to minecraft:the_nether 7 8 9 filtered chest{CustomName:"Ximglie"}'
        self.assertEqual((run(dims, TB)[0], keys_of(dims)), (dims, {'Ximglie'}))
        for strict in ('clone from minecraft:overworld 1 2 3 4 5 6 to minecraft:the_nether 7 8 9 strict filtered chest{CustomName:"Ximglie"} move',     # filtre = 16e mot
                       'clone 1 2 3 4 5 6 7 8 9 strict filtered chest{CustomName:"Ximglie"}'):
            self.assertEqual((run(strict, TB)[0], keys_of(strict)), (strict, {'Ximglie'}), strict)
        for other in ('clone 1 2 3 4 5 6 7 8 9 masked', 'clone ~ ~ ~ ~ ~ ~ ~ ~ ~ replace move'):
            self.assertEqual((run(other, TB)[0], keys_of(other)), (other, set()), other)

    def test_item_replace_is_not_a_filter(self):
        line = "item replace entity @s weapon.mainhand with stick[custom_name='Hello']"
        self.assertEqual(run(line, TB)[0], line.replace('Hello', 'Bonjour'))
        self.assertEqual(keys_of(line), set())
        self.assertEqual(run(FIX['command'], {'Blabber Stone': 'Pierre'})[0], FIX['command'].replace('Blabber Stone', 'Pierre'))      # `} replace` de setblock


class QuotedLock(unittest.TestCase):
    LOCK = '''setblock ~ ~ ~ chest{%s:{components:{"minecraft:custom_name":'"Ximglie"'}},CustomName:"Hello"}'''

    def test_quoted_lock_key_unchanged_neighbour_translated(self):
        for key in ('"lock"', "'lock'", '"minecraft:lock"', '"lock" '):
            line = self.LOCK % key
            self.assertEqual(run(line, TB)[0], line.replace('"Hello"', '"Bonjour"'), key)
            self.assertIn('Ximglie', keys_of(line), key)
        bare = self.LOCK % 'lock'
        self.assertEqual(run(bare, TB)[0], bare.replace('"Hello"', '"Bonjour"'))

    def test_lock_as_a_plain_word_is_text(self):
        line = 'tellraw @a ["lock", {"text":"lock"}]'
        self.assertEqual(run(line, {'lock': 'verrou'})[0], 'tellraw @a ["verrou", {"text":"verrou"}]')
        self.assertEqual(keys_of(line), set())


class UnreadableLines(unittest.TestCase):
    BAD = '''setblock ~ ~ ~ chest{lock:{components:{"minecraft:custom_name":'"Ximglie"'}'''      # le verrou n'est pas fermé : Bad avant de le protéger

    def test_unreadable_lock_line_protects_all_its_strings_and_warns(self):
        prot, st = T.protected_keys([self.BAD])
        self.assertIn('Ximglie', prot)
        self.assertEqual([line for _, line in st.warns], [self.BAD])
        self.assertEqual(st.errors, 1)
        self.assertEqual(run("give @s stick[custom_name='Ximglie']", TB, protected=prot)[0], "give @s stick[custom_name='Ximglie']")

    def test_readable_lines_give_no_warning_and_no_extra_protection(self):
        prot, st = T.protected_keys([FIX['lock'], FIX['entity']])
        self.assertEqual((st.warns, st.errors), ([], 0))
        self.assertIn('Ximglie', prot)
        self.assertNotIn('Promised Smoke', prot)        # le nom d'entité de la 2e ligne n'est pas une zone protégée

    def test_unreadable_nested_command_warns(self):
        line = '''setblock ~ ~ ~ command_block{Command:'clear @s stick[custom_name="Ximglie"'}'''     # le crochet de la commande imbriquée n'est pas fermé
        prot, st = T.protected_keys([line])
        self.assertEqual(len(st.warns), 1)
        self.assertIn('Ximglie', prot)


class Details(unittest.TestCase):
    def test_protected_key_absent_from_table_is_not_missing(self):
        out, st = run("give @s stick[custom_name='Ximglie',lore=['Hello']]", {}, protected={'Ximglie'})
        self.assertEqual((st.missing_keys, st.refused, st.missing), ({'Hello': 1}, 0, 1))
        _, st = run("give @s stick[custom_name='Ximglie']", {'Ximglie': 'X'}, protected={'Ximglie'})
        self.assertEqual((st.refused, st.missing), (1, 0))

    def test_table_load_needs_a_directory(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                T.Table.load(Path(d) / 'absent')
            (Path(d) / 'f.json').write_text('[]', encoding='utf-8')
            with self.assertRaises(ValueError):
                T.Table.load(Path(d) / 'f.json')
            self.assertEqual(T.Table.load(d).glob, {})


if __name__ == '__main__':
    unittest.main()
