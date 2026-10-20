"""Duel / TDM sniper : clic gauche = tir, clic droit = lunette (boîte de clic de gun/cl_*), cache de lunette lisible par le client.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import json
import struct
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FUNC = ROOT / 'data' / 'mg' / 'function'
FONT = ROOT / 'resourcepack' / 'assets' / 'mg' / 'font'
TEXT = ROOT / 'resourcepack' / 'assets' / 'mg' / 'textures'
GAMES = (('duel', 'dl'), ('tdm', 'tm'))
CLIENT_ATLAS = 256            # côté de l'atlas de police du client : un glyphe plus large manque (rectangle blanc)


def lines(rel):
    return (FUNC / (rel + '.mcfunction')).read_text(encoding='utf-8').splitlines()


def code(rel):
    return [l for l in lines(rel) if l and not l.startswith('#')]


class ScopeOnClick(unittest.TestCase):
    def test_scope_driven_by_gads(self):
        for game, k in GAMES:
            scope = code(f'{game}/scope')
            on = [l for l in scope if f'function mg:{game}/scope_on' in l]
            self.assertEqual(len(on), 1, f'{game}/scope')
            self.assertNotIn('is_sneaking', on[0], f'{game}/scope : la lunette ne dépend plus de l\'accroupi')
            self.assertIn('tag=mg.gads', on[0])
            self.assertIn(f'tag @s add mg.{k}cr', '\n'.join(scope), f'{game}/scope : posture mg.{k}cr')
            self.assertIn(f'tag @s remove mg.{k}cr', '\n'.join(scope))

    def test_ray_uses_crouch_tag(self):
        for game, k in GAMES:
            ray = '\n'.join(code(f'{game}/ray'))
            self.assertIn(f'mg.{k}cr', ray)
            self.assertNotIn(f'mg.{k}sc', ray, f'{game}/ray : la hauteur de tête suit l\'accroupi, pas la lunette')

    def test_kits_two_item_models(self):
        for game, k in GAMES:
            kit = [l for l in code(f'{game}/kit') if f'custom_data={{mg_{k}:1b}}' in l]
            self.assertEqual(len(kit), 2, f'{game}/kit')
            rp = [l for l in kit if 'item_model="mg:gun_sniper"' in l]
            vanilla = [l for l in kit if 'item_model="minecraft:spyglass"' in l]
            self.assertEqual((len(rp), len(vanilla)), (1, 1), f'{game}/kit')
            self.assertTrue(rp[0].startswith('execute if score $rp mg.st matches 1 run item replace'))
            self.assertTrue(vanilla[0].startswith('execute unless score $rp mg.st matches 1 run item replace'))
            self.assertNotIn('use_cooldown', '\n'.join(kit))
            self.assertIn('Clic gauche : tir', rp[0])
            self.assertIn('Clic droit : lunette', rp[0])

    def test_spawn_lowers_scope(self):
        for game, spawn in (('duel', 'spawn'), ('tdm', 'spawn_do')):
            self.assertIn('execute if entity @s[tag=mg.gads] run function mg:gun/cl_unaim', code(f'{game}/{spawn}'))
        self.assertIn('execute if entity @s[tag=mg.gads] run function mg:gun/cl_unaim', code('duel/stop'))


class ClickBox(unittest.TestCase):
    def test_eligibility(self):
        tick = code('gun/cl_tick')
        for tag, key, extra in (('mg.dl', 'mg_dl', 'gamemode=!spectator'), ('mg.play', 'mg_tm', 'gamemode=adventure')):
            want = (f'execute as @a[tag={tag},{extra}] if items entity @s weapon.mainhand '
                    f'minecraft:warped_fungus_on_a_stick[custom_data~{{{key}:1b}}] run tag @s add mg.gcw')
            self.assertEqual(tick.count(want), 1, key)
            self.assertLess(tick.index(want), tick.index('execute as @a[tag=mg.gads,tag=!mg.gcw] run function mg:gun/cl_unaim'))

    def test_foreign_attack_routed(self):
        follow = code('gun/cl_follow')
        foreign = [i for i, l in enumerate(follow) if 'cl_foreign' in l]
        self.assertEqual(len(foreign), 1)
        self.assertIn('on attacker unless entity @s[tag=mg.gcme]', follow[foreign[0]])
        self.assertLess(foreign[0], follow.index('data remove entity @s attack'))
        route = code('gun/cl_foreign')
        self.assertEqual(sum('mg:duel/box_knife' in l for l in route), 1)
        self.assertEqual(sum('mg:tdm/box_knife' in l for l in route), 1)
        self.assertTrue((FUNC / 'duel' / 'box_knife.mcfunction').is_file())
        self.assertTrue((FUNC / 'tdm' / 'box_knife.mcfunction').is_file())
        self.assertTrue(any('mg.dlsh' in l for l in code('duel/box_knife')))
        self.assertTrue(any('mg.tmen' in l for l in code('tdm/box_knife')), 'pas de coup ami au TDM')

    def test_armed_player_on_foreign_box_keeps_his_clicks(self):
        """Tireur armé à moins de 1,3 bloc : le ciblage peut prendre la boîte adverse, ses clics restent les siens."""
        route = code('gun/cl_foreign')
        left = [i for i, l in enumerate(route) if l == 'execute if entity @s[tag=mg.gcw] run return run function mg:gun/cl_left']
        self.assertEqual(left, [0], 'le tir de l\'attaquant armé passe avant le routage couteau')
        follow = code('gun/cl_follow')
        right = [i for i, l in enumerate(follow) if 'on target unless entity @s[tag=mg.gcme] if entity @s[tag=mg.gcw] run function mg:gun/cl_right' in l]
        self.assertEqual(len(right), 1)
        self.assertLess(right[0], follow.index('data remove entity @s interaction'))

    def test_shoot_needs_sniper_in_main_hand(self):
        for game, k in GAMES:
            shoot = code(f'{game}/shoot')
            self.assertIn(f'execute unless items entity @s weapon.mainhand minecraft:warped_fungus_on_a_stick[custom_data~{{mg_{k}:1b}}] run return 0', shoot)
            self.assertFalse([l for l in shoot if 'weapon.*' in l], f'{game}/shoot : le sniper en main gauche ne tire pas')

    def test_lobby_reticle_kept_for_lobby_only(self):
        for l in code('gun/cl_ret'):
            if 'mg.gads' in l:
                self.assertIn('tag=!mg.dl', l)
                self.assertIn('tag=!mg.play', l)


class MeleeAdvancements(unittest.TestCase):
    def test_hurt_entity_is_a_player(self):
        """Frapper la boîte de clic (une interaction) déclenche aussi player_hurt_entity : l'entité frappée doit être un joueur."""
        for name, fn in (('duel_melee', 'mg:duel/melee_adv'), ('tdm_melee', 'mg:tdm/melee_adv')):
            adv = json.loads((ROOT / 'data' / 'mg' / 'advancement' / (name + '.json')).read_text(encoding='utf-8'))
            self.assertEqual(adv['rewards'], {'function': fn})
            hit = adv['criteria']['hit']
            self.assertEqual(hit['trigger'], 'minecraft:player_hurt_entity')
            self.assertEqual(hit['conditions']['entity'], [{
                'condition': 'minecraft:entity_properties', 'entity': 'this',
                'predicate': {'minecraft:entity_type': 'minecraft:player'}}], name)


class ScopeTexture(unittest.TestCase):
    def test_font_bitmaps_fit_client_atlas(self):
        seen = 0
        for font in sorted(FONT.glob('*.json')):
            for prov in json.loads(font.read_text(encoding='utf-8')).get('providers', []):
                if prov.get('type') != 'bitmap' or not prov['file'].startswith('mg:'):
                    continue
                png = TEXT / prov['file'][3:]
                head = png.read_bytes()[:24]
                self.assertEqual(head[:8], b'\x89PNG\r\n\x1a\n', png.name)
                w, h = struct.unpack('>II', head[16:24])
                self.assertLessEqual(max(w, h), CLIENT_ATLAS, f'{png.name} : {w}x{h} dépasse l\'atlas de police ({CLIENT_ATLAS} px)')
                seen += 1
        self.assertGreater(seen, 0)

    def test_scope_size(self):
        w, h = struct.unpack('>II', (TEXT / 'font' / 'gta_scope.png').read_bytes()[16:24])
        self.assertEqual((w, h), (256, 128))


if __name__ == '__main__':
    unittest.main()
