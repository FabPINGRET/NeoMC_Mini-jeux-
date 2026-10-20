"""Overlay de recharge (use_cooldown) dans la hotbar : armes (gun/cd_*), snipers duel/TDM, arc Murder, canon sonique Terra Nova.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FUNC = ROOT / 'data' / 'mg' / 'function'
sys.path[:0] = [str(ROOT / 'tools' / 'arcade'), str(ROOT / 'tools' / 'duel')]
import guns                                             # noqa: E402
import duel_play                                        # noqa: E402

SECS = f'seconds:{duel_play.SHOT_CD / 20:g}f'
ARROW_CD = int(re.search(r'^ARROW_CD = (\d+)', (ROOT / 'tools/arcade/gen_murder.py').read_text(encoding='utf-8'), re.M).group(1))
GAMES = (('duel', 'mg.dlp', 'mg:dlsn', 'prot_tick', 'spawn'), ('tdm', 'mg.tmp', 'mg:tmsn', 'prot_tick', 'spawn_do'))
NEW_GROUPS = {'mg:gun$(n)': 'gun/', 'mg:dlsn': 'duel/', 'mg:tmsn': 'tdm/', 'mg:mmbow': 'mm/', 'mg:tvsonic': 'terra/'}


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


class SniperCooldown(unittest.TestCase):
    def test_duel_tdm(self):
        for game, tag, group, prot, spawn in GAMES:
            pt, sp, kit = code(f'{game}/{prot}'), code(f'{game}/{spawn}'), code(f'{game}/kit')
            arm = [i for i, l in enumerate(pt) if 'use_cooldown' in l]
            end = next(i for i, l in enumerate(pt) if l.endswith(f'tag @s remove {tag}'))
            self.assertEqual(len(arm), 9, f'{game}/{prot}')
            self.assertTrue(all(i < end for i in arm))
            for k, i in enumerate(arm):
                self.assertIn(f'hotbar.{k} ', pt[i])
                self.assertIn('matches ..0 ', pt[i])
                self.assertIn(f'{SECS},cooldown_group:"{group}"', pt[i])
            dis = [i for i, l in enumerate(sp) if '"!minecraft:use_cooldown":{}' in l]
            self.assertEqual(len(dis), 9, f'{game}/{spawn}')
            self.assertTrue(all(i > sp.index(f'tag @s add {tag}') for i in dis))
            self.assertEqual([l for l in kit if 'use_cooldown' in l], [duel_play.kit_cd(group, tag)])
            self.assertIn(f'unless entity @s[tag={tag}]', duel_play.kit_cd(group, tag))
        self.assertEqual(duel_play.SHOT_CD / 20, 2)

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
        files = [f'gun/cd_{x}' for x in ('set', 'n', 'r', 'hand')] + [f'{g}/{f}' for g, _, _, p, s in GAMES for f in (p, s, 'kit')]
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
