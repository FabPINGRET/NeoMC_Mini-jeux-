"""Overlay de recharge (use_cooldown) dans la hotbar : armes (gun/cd_*), arc Murder, canon sonique Terra Nova ; absent des snipers duel/TDM.
Lobby et Neo GTA : barre de durabilité (gun/bar) à la place.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FUNC = ROOT / 'data' / 'mg' / 'function'
sys.path[:0] = [str(ROOT / 'tools' / 'arcade'), str(ROOT / 'tools' / 'duel')]
import guns                                             # noqa: E402
import duel_play                                        # noqa: E402

ARROW_CD = int(re.search(r'^ARROW_CD = (\d+)', (ROOT / 'tools/arcade/gen_murder.py').read_text(encoding='utf-8'), re.M).group(1))
GAMES = (('duel', 'prot_tick', 'spawn'), ('tdm', 'prot_tick', 'spawn_do'))
ITEMS = ROOT / 'resourcepack' / 'assets' / 'mg' / 'items'
BAR_OFF = '*[custom_data~{mg_gun:1b},!minecraft:unbreakable]'
RESET = '{function:"minecraft:set_components",components:{"minecraft:unbreakable":{},"minecraft:damage":0}}'
SLOTS = [f'hotbar.{i}' for i in range(9)] + ['weapon.offhand']
NEW_GROUPS = {'mg:gun$(n)': 'gun/', 'mg:mmbow': 'mm/', 'mg:tvsonic': 'terra/'}


def lines(rel):
    return (FUNC / (rel + '.mcfunction')).read_text(encoding='utf-8').splitlines()


def code(rel):
    return [l for l in lines(rel) if l and not l.startswith('#')]


def run_lines(rel, needle):
    return [l for l in lines(rel) if needle in l]


class GunCooldown(unittest.TestCase):
    def test_files_and_cd_set(self):
        for f in ('cd_set', 'cd_n', 'cd_r', 'cd_hand'):
            self.assertTrue((FUNC / 'gun' / (f + '.mcfunction')).is_file(), f'gun/{f} absent : lancer tools/arcade/gen_*.py')
        self.assertEqual(code('gun/cd_set'), [
            '$item modify entity @s weapon.mainhand {function:"minecraft:set_components",components:{"minecraft:use_cooldown":{seconds:$(s)f,cooldown_group:"mg:gun$(n)"}}}',
            '$item modify entity @s weapon.mainhand {function:"minecraft:set_custom_data",tag:{gcr:$(m)b}}'])

    def test_cd_hand_reload_values(self):
        hand = lines('gun/cd_hand')
        for n, (_, _, _, _, _, rl, *_r) in guns.GUNS.items():
            want = f'run function mg:gun/cd_r {{n:{n},s:{rl / 20:g},h:{(rl // 2) / 20:g}}}'
            self.assertEqual(len([l for l in hand if l.endswith(want) and f'{{gun:{n}}}' in l and f'mg.g{n} matches ..1' in l]), 1, f'cd_hand arme {n} : {want}')

    def test_cd_n_values(self):
        cdn = lines('gun/cd_n')
        for n, (_, _, _, cd, *_r) in guns.GUNS.items():
            if n != 5:
                for g in (1, 2):
                    want = f'[custom_data~{{gun:{n},gcr:{g}b}}] run return run function mg:gun/cd_set {{n:{n},s:0.05,m:0}}'
                    self.assertEqual(len([l for l in cdn if l.endswith(want)]), 1, f'cd_n arme {n} gcr {g}')
            else:
                self.assertEqual(len([l for l in cdn if l.endswith(f'cd_set {{n:5,s:{cd / 20:g},m:0}}')]), 1, 'cd_n Sniper cadence')
                self.assertEqual(len([l for l in cdn if 'mg.zdbl' in l and l.endswith(f'cd_set {{n:5,s:{max(1, cd * 2 // 3) / 20:g},m:3}}')]), 1, 'cd_n Sniper Double Tap')

    def test_group_only_in_cd_set(self):
        for l in code('gun/cd_set'):
            self.assertIn(re.findall(r'cooldown_group:"([^"]*)"', l), ([], ['mg:gun$(n)']), l)
        for f in ('cd_n', 'cd_r', 'cd_hand'):
            self.assertFalse(run_lines(f'gun/{f}', 'cooldown_group'), f'gun/{f} fixe un groupe')

    def test_tick_line(self):
        tick = lines('gun/tick')
        hand = [i for i, l in enumerate(tick) if l.endswith('run function mg:gun/cd_hand')]
        hud = [i for i, l in enumerate(tick) if l.endswith('run function mg:gun/hud')]
        self.assertEqual((len(hand), len(hud)), (1, 1))
        self.assertLess(hand[0], hud[0])
        self.assertIn('tag=!mg.gtw', tick[hand[0]])
        self.assertIn('mg_gun:1b', tick[hand[0]])


class LobbyBar(unittest.TestCase):
    """Lobby et Neo GTA : pas d'use_cooldown (tir au clic gauche, gcd partagé) mais une barre de durabilité (gun/bar, gun/bar_set)."""

    def test_bar_totals(self):
        bar = lines('gun/bar')
        for n, (_, _, _, _, _, rl, *_r) in guns.GUNS.items():
            got = [l for l in bar if f'mg.grt matches {n} ' in l]
            self.assertEqual(len(got), 1, f'gun/bar arme {n}')
            self.assertTrue(got[0].endswith(f'run scoreboard players set $gbt mg.st {rl}'), got[0])
            self.assertIn(f'{{gun:{n}}}', got[0], 'la recharge ne compte que pour l\'arme en main')
        cd = guns.GUNS[5][3]
        snp = [l for l in bar if 'mg.gcd matches 1..' in l and l.endswith(f'$gbt mg.st {cd}')]
        self.assertEqual(len(snp), 1, 'cadence : Sniper seul')
        self.assertIn('{gun:5}', snp[0])
        self.assertIn('unless score @s mg.grl matches 1..', snp[0])
        self.assertEqual(len([l for l in bar if 'mg.gcd matches 1..' in l and '$gbt mg.st' in l]), 1)

    def test_bar_set_and_reset(self):
        item = [l for l in code('gun/bar_set') if l.startswith('item modify')]
        self.assertEqual(len(item), 1)
        self.assertLess(item[0].index('"!minecraft:unbreakable":{}'), item[0].index('minecraft:set_damage'))   # set_damage ignore un objet incassable
        self.assertIn('target:{type:"minecraft:fixed",name:"$gbar"},score:"mg.st",scale:0.001', item[0])
        self.assertEqual(code('gun/bar_set')[0], 'execute unless score $gbt mg.st matches 1.. run return 0')
        sets = code('gun/bar_set')
        low = [l for l in sets if l.startswith('execute if score $gbar mg.st matches ..')]
        self.assertEqual(len(low), 1)
        self.assertTrue(low[0].startswith('execute if score $gbar mg.st matches ..0 run scoreboard players set $gbar mg.st 1'), 'plancher 1 : set_damage 0 = objet cassé')
        self.assertIn('execute if score $gbar mg.st matches 1000.. run scoreboard players set $gbar mg.st 999', sets)
        self.assertEqual(code('gun/bar')[-1], 'function mg:gun/bar_clear', 'rien à montrer : remise à zéro (dernière ligne, return run avant)')
        self.assertFalse(run_lines('gun/bar', 'item modify'), 'gun/bar ne modifie plus l\'objet lui-même')

    def test_bar_clear(self):
        self.assertTrue((FUNC / 'gun' / 'bar_clear.mcfunction').is_file(), 'gun/bar_clear absent : lancer tools/arcade/gen_*.py')
        clear = code('gun/bar_clear')
        self.assertEqual(clear[0], f'execute unless items entity @s hotbar.* {BAR_OFF} unless items entity @s weapon.offhand {BAR_OFF} run return 0', 'garde')
        self.assertEqual(clear[1:], [f'execute if items entity @s {sl} {BAR_OFF} run item modify entity @s {sl} {RESET}' for sl in SLOTS], 'une ligne par case')
        for l in clear:
            self.assertEqual(l.count('{'), l.count('}'), l)
            self.assertNotIn('lrpg', l)
            self.assertNotIn('rpg:1b', l)

    def test_bazookas_never_cleared(self):
        """Bazooka lobby (lrpg, mg_gun) et bazooka GTA (rpg:1b, sans mg_gun) sont incassables : le balayage ne les touche pas."""
        give = ' '.join(code('lobby/rpg_give'))
        self.assertIn('custom_data={rpg:1b,lrpg:1b,mg_gun:1b},unbreakable={}', give)
        found = 0
        for p in (FUNC / 'gta').rglob('*.mcfunction'):
            for l in p.read_text(encoding='utf-8').splitlines():
                if 'custom_data={rpg:1b' in l and 'item replace' in l:
                    found += 1
                    self.assertNotIn('mg_gun', l, p.name)
                    self.assertIn('unbreakable={}', l, p.name)
        self.assertGreaterEqual(found, 1)

    def test_lobby_tick(self):
        tick = lines('lobby/guns_tick')
        bar = [i for i, l in enumerate(tick) if l.endswith('run function mg:gun/bar')]
        self.assertEqual(len(bar), 1)
        reload_ = [i for i, l in enumerate(tick) if l.endswith('run function mg:gun/reload_tick')]
        sneak = [i for i, l in enumerate(tick) if l.endswith('run function mg:gun/sneak')]
        hud = [i for i, l in enumerate(tick) if l.endswith('run function mg:gun/hud')]
        guard = [i for i, l in enumerate(tick) if l == 'execute unless score $state mg.st matches 0 run return 0']
        self.assertEqual((len(reload_), len(sneak), len(hud), len(guard)), (1, 1, 1, 1))
        self.assertTrue(bar[0] < guard[0] < reload_[0] < sneak[0] < hud[0], 'barre et remise à zéro avant le garde $state')
        for needle in ('tag=!mg.play', 'tag=!mg.surv', 'tag=!mg.gtw', '{lrpg:1b}', '{mg_gun:1b}'):
            self.assertIn(needle, tick[bar[0]])
        clear = [i for i, l in enumerate(tick) if l.endswith('run function mg:gun/bar_clear')]
        self.assertEqual(len(clear), 2)
        self.assertTrue(all(bar[0] < i < guard[0] for i in clear), 'remise à zéro avant le garde $state')
        for i in clear:
            for needle in ('tag=!mg.play', 'tag=!mg.surv', 'tag=!mg.gtw'):
                self.assertIn(needle, tick[i])
        self.assertEqual([l.split(' run ')[0].split('] ', 1)[1] for l in (tick[i] for i in clear)],
                         ['unless items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}]',
                          'if items entity @s weapon.mainhand *[custom_data~{lrpg:1b}]'], 'main sans mg_gun, puis bazooka du lobby')

    def test_gta_tick(self):
        tick = lines('gta/tick')
        bar = [i for i, l in enumerate(tick) if l.endswith('run function mg:gun/bar')]
        self.assertEqual(len(bar), 1)
        for fn in ('gun/reload_tick', 'gun/sneak'):
            idx = [i for i, l in enumerate(tick) if l.endswith(f'run function mg:{fn}')]
            self.assertEqual(len(idx), 1, fn)
            self.assertLess(idx[0], bar[0], f'{fn} avant la barre')
        self.assertTrue(any(l.startswith('scoreboard players remove @a[tag=mg.gtw,scores={mg.gcd=1..}]') for l in tick[:bar[0]]), 'gcd décompté avant la barre')
        self.assertIn('@a[tag=mg.gtw]', tick[bar[0]])
        self.assertIn('{mg_gun:1b}', tick[bar[0]])                                   # exclut le bazooka (rpg:1b, sans chargeur)
        self.assertNotIn('rpg', tick[bar[0]])
        clear = [i for i, l in enumerate(tick) if l.endswith('run function mg:gun/bar_clear')]
        self.assertEqual(len(clear), 1)
        self.assertEqual(tick[clear[0]], 'execute as @a[tag=mg.gtw] unless items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run function mg:gun/bar_clear',
                         'main sans mg_gun (bazooka GTA compris)')
        self.assertLess(bar[0], clear[0])
        hud = [i for i, l in enumerate(tick) if l.endswith('run function mg:gta/hud')]
        self.assertTrue(hud and bar[0] < min(hud), 'barre avant le HUD')

    def test_zombies_infection_unchanged(self):
        self.assertFalse(run_lines('gun/tick', 'gun/bar'), 'Zombies / Infection gardent use_cooldown (gun/cd_*)')


class HandAnimation(unittest.TestCase):
    """La barre change le damage à chaque tick : sans hand_animation_on_swap:false, l'animation de changement d'objet se rejouerait."""

    def test_gun_items(self):
        want = {f'gun_{m}.json' for m in {g[1] for g in guns.GUNS.values()}} | {'gun_rpg.json'}
        got = {p.name: p for p in ITEMS.glob('gun_*.json')}
        self.assertEqual(set(got), want)
        for name, p in got.items():
            d = json.loads(p.read_text(encoding='utf-8'))
            self.assertIs(d.get('hand_animation_on_swap'), False, name)        # champ racine, à côté de « model »
            self.assertIn('model', d, name)
            self.assertNotIn('hand_animation_on_swap', d['model'], name)


class SniperCooldown(unittest.TestCase):
    def test_duel_tdm(self):
        """Le clic droit ouvre la lunette (plus de tir) : l'overlay de recharge vanilla est retiré des snipers duel / TDM."""
        for game in ('duel', 'tdm'):
            for p in sorted((FUNC / game).rglob('*.mcfunction')):
                txt = p.read_text(encoding='utf-8')
                for needle in ('use_cooldown', 'mg:dlsn', 'mg:tmsn'):
                    self.assertNotIn(needle, txt, f'{p.relative_to(FUNC).as_posix()} : {needle}')
        self.assertEqual(duel_play.SHOT_CD / 20, 2)         # la recharge du tir (mg.dlcd / mg.tmcd) reste de 2 s

    def test_murder_and_terra(self):
        for f in ('det_kit', 'drop_at', 'drop_here', 'gold_newbow'):
            txt = '\n'.join(lines(f'mm/{f}'))
            self.assertIn('mg:mmbow', txt, f)
            self.assertIn(f'seconds:{ARROW_CD / 20:g}f', txt, f)
        self.assertRegex('\n'.join(lines('terra/buy')), r'seconds:4f,cooldown_group:"mg:tvsonic"')


class GroupsAndSyntax(unittest.TestCase):
    def test_groups_unique_per_game(self):
        found = {}
        for p in FUNC.rglob('*.mcfunction'):
            for g in re.findall(r'cooldown_group:"(mg:[^"]*)"', p.read_text(encoding='utf-8')):
                found.setdefault(g, set()).add(p.relative_to(FUNC).as_posix())
        for g, folder in NEW_GROUPS.items():
            self.assertIn(g, found)
            self.assertTrue(all(f.startswith(folder) for f in found[g]), f'{g} hors de {folder} : {sorted(found[g])}')
        for n in range(1, 9):                           # mg:gun<n> est composé par macro : jamais écrit en dur
            self.assertNotIn(f'mg:gun{n}', found)
        print('groupes :', sorted(found))

    def test_syntax(self):
        files = [f'gun/cd_{x}' for x in ('set', 'n', 'r', 'hand')] + ['gun/bar', 'gun/bar_set', 'gun/bar_clear'] + [f'{g}/{f}' for g, p, s in GAMES for f in (p, s, 'kit')]
        files += [f'mm/{f}' for f in ('det_kit', 'drop_at', 'drop_here', 'gold_newbow')] + ['terra/buy']
        for rel in files:
            for l in code(rel):
                if 'use_cooldown' in l or rel.startswith('gun/'):
                    for a, b in ('{}', '[]', '()'):
                        self.assertEqual(l.count(a), l.count(b), f'{rel} : {a}{b} déséquilibrés : {l[:90]}')
        for rel in files:                               # périmètre du changement seulement (d'autres fonctions du dépôt ont `$(` dans des dialogues)
            for l in code(rel):
                if '$(' in l:
                    self.assertTrue(l.startswith('$'), f'{rel} : macro sans préfixe $ : {l[:90]}')


if __name__ == '__main__':
    unittest.main()
