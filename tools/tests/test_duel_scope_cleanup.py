"""Duel / TDM sniper : nettoyage des tags, ordre du tick, gardes du couteau sur boite adverse, README, police de la lunette.
Complete test_duel_scope.py (meme racine derivee de ce fichier). Lancer : python -m unittest discover -s tools/tests -v
"""
import json
import re
import struct
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FUNC = ROOT / 'data' / 'mg' / 'function'
FONT = ROOT / 'resourcepack' / 'assets' / 'mg' / 'font'
TEXT = ROOT / 'resourcepack' / 'assets' / 'mg' / 'textures'
GAMES = (('duel', 'dl'), ('tdm', 'tm'))
SNEAK = 'is_sneaking:true'


def code(rel):
    text = (FUNC / (rel + '.mcfunction')).read_text(encoding='utf-8').splitlines()
    return [l for l in text if l and not l.startswith('#')]


class Cleanup(unittest.TestCase):
    def test_crouch_tag_removed_on_exit(self):
        for rel, sel in (('duel/stop', '@s'), ('duel/remove', '@a')):
            self.assertIn(f'tag {sel} remove mg.dlcr', code(rel), rel)
        self.assertIn('tag @a remove mg.tmcr', code('tdm/cleanup'))
        gen = (ROOT / 'tools' / 'duel' / 'gen_duel.py').read_text(encoding='utf-8')
        tags = re.search(r'^TAGS = \[(.*?)\]', gen, re.S | re.M)
        self.assertIsNotNone(tags)
        self.assertIn("'mg.dlcr'", tags.group(1))

    def test_unaim_called_on_spawn_and_stop(self):
        want = 'execute if entity @s[tag=mg.gads] run function mg:gun/cl_unaim'
        for rel in ('duel/spawn', 'duel/stop', 'tdm/spawn_do'):
            self.assertEqual(code(rel).count(want), 1, rel)

    def test_ray_has_no_scope_tag(self):
        for game, k in GAMES:
            self.assertNotIn(f'mg.{k}sc', '\n'.join(code(f'{game}/ray')))


class TickOrder(unittest.TestCase):
    def test_cl_tick_before_duel_and_game_tick(self):
        tick = code('core/tick')
        idx = lambda s: [i for i, l in enumerate(tick) if s in l]
        cl, duel, game = idx('function mg:gun/cl_tick'), idx('function mg:duel/tick'), idx('function mg:core/game_tick')
        self.assertEqual((len(cl), len(game)), (1, 1))
        self.assertTrue(duel)
        self.assertLess(cl[0], min(duel))
        self.assertLess(cl[0], game[0])

    def test_cl_tick_resets_gcw_first(self):
        tick = code('gun/cl_tick')
        reset = tick.index('tag @a remove mg.gcw')
        adds = [i for i, l in enumerate(tick) if l.endswith('run tag @s add mg.gcw')]
        self.assertTrue(adds)
        self.assertLess(reset, min(adds))
        self.assertEqual(reset, 0)

    def test_cl_ret_excludes_duel_and_tdm(self):
        for l in code('gun/cl_ret'):
            if 'mg.gads' in l:
                self.assertIn('tag=!mg.dl', l)
                self.assertIn('tag=!mg.play', l)


class BoxKnife(unittest.TestCase):
    def test_duel_guards(self):
        k = code('duel/box_knife')
        self.assertIn('execute unless entity @s[tag=mg.dl,tag=!mg.dlp] run return 0', k)
        self.assertIn('execute if score @s mg.dlkc matches 1.. run return 0', k)
        self.assertTrue(any('distance=..4.5' in l and 'tag=mg.gcme' in l and 'tag=!mg.dlp' in l for l in k))
        self.assertIn('execute unless entity @a[tag=mg.dlvc] run return 0', k)
        self.assertTrue(any('function mg:duel/melee_hit' in l for l in k))
        self.assertLess(k.index('scoreboard players set @s mg.dlkc 20'), [i for i, l in enumerate(k) if 'melee_hit' in l][0])

    def test_tdm_guards(self):
        k = code('tdm/box_knife')
        self.assertIn('execute unless entity @s[tag=mg.play,tag=!mg.tmp] run return 0', k)
        self.assertIn('execute if score @s mg.tmkc matches 1.. run return 0', k)
        self.assertTrue(any('tag=mg.tmen' in l and 'distance=..4.5' in l and 'tag=!mg.tmp' in l for l in k))
        self.assertTrue(any('function mg:tdm/melee_hit' in l for l in k))
        exit_line = 'execute unless entity @a[tag=mg.tmvc] run return run tag @a remove mg.tmen'
        self.assertIn(exit_line, k, 'sortie sans victime : mg.tmen retire')
        self.assertLess(k.index(exit_line), k.index('scoreboard players set @s mg.tmkc 20'))
        self.assertIn('tag @a remove mg.tmen', k[k.index(exit_line) + 1:], 'sortie normale : mg.tmen retire aussi')

    def test_both_call_melee_hit_as_victim(self):
        for game, k in GAMES:
            hits = [l for l in code(f'{game}/box_knife') if 'melee_hit' in l]
            self.assertEqual(len(hits), 1)
            self.assertTrue(hits[0].startswith(f'execute as @a[tag=mg.{k}vc,limit=1] run'))


class ScopeLines(unittest.TestCase):
    def test_sneak_predicate_only_on_crouch_tag_lines(self):
        for game, k in GAMES:
            for l in code(f'{game}/scope'):
                if SNEAK in l:
                    self.assertIn(f'mg.{k}cr', l, l)
                if f'mg.{k}cr' in l:
                    self.assertIn(SNEAK, l, l)
            on = [l for l in code(f'{game}/scope') if 'scope_on' in l]
            self.assertEqual(len(on), 1)
            self.assertIn('mg.gads', on[0])

    def test_no_use_cooldown_in_duel_tdm(self):
        for game in ('duel', 'tdm'):
            for f in sorted((FUNC / game).glob('*.mcfunction')):
                self.assertNotIn('use_cooldown', f.read_text(encoding='utf-8'), f.name)


class ResourcePackFont(unittest.TestCase):
    def test_scope_provider(self):
        font = json.loads((FONT / 'gta.json').read_text(encoding='utf-8'))
        scope = [p for p in font['providers'] if p.get('file') == 'mg:font/gta_scope.png']
        self.assertEqual(len(scope), 1)
        self.assertEqual((scope[0]['ascent'], scope[0]['height']), (29, 64))
        self.assertEqual(scope[0]['chars'], [chr(0xE222)])
        w, h = struct.unpack('>II', (TEXT / 'font' / 'gta_scope.png').read_bytes()[16:24])
        self.assertEqual((w, h), (256, 128))


class Readme(unittest.TestCase):
    def test_scope_documented_as_right_click(self):
        rows = (ROOT / 'README.md').read_text(encoding='utf-8').splitlines()
        marks = (lambda l: l.startswith('| **🎯 TDM sniper**'),
                 lambda l: '**Armes**' in l,
                 lambda l: l.startswith('| `/trigger mg.duel set 1` / `1000`+id'))
        for i, is_row in enumerate(marks):
            found = [l for l in rows if is_row(l)]
            self.assertEqual(len(found), 1, f'README repere {i} : {len(found)} correspondances')
            low = found[0].lower()
            self.assertIn('clic droit', low, f'README repere {i}')
            self.assertIn('lunette', low, f'README repere {i}')
        self.assertNotRegex('\n'.join(rows).lower(), r'accroupi\s*=\s*lunette')


if __name__ == '__main__':
    unittest.main()
