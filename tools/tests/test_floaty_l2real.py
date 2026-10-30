"""tools/floaty, lot L2 : propriétés de la sortie RÉELLE data/floaty/function/{install,uninstall}.mcfunction (aller-retour, gardes, verbes, JSON).
Sautés si la sortie générée est absente (la CI n'a pas la carte) ; si install est là, tools/floaty/owned.txt doit l'être aussi.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FN = ROOT / 'data' / 'floaty' / 'function'
GUARD = 'mg:floaty installed'
VERBS = {'scoreboard', 'team', 'bossbar', 'data', 'schedule', 'execute'}


def lines(p):
    return [l for l in p.read_text(encoding='utf-8').split('\n') if l.strip() and not l.startswith('#')]


def title(rest):
    """Texte après un identifiant : composant JSON (chaîne, objet ou liste), parsé ; ValueError s'il ne l'est pas."""
    return json.loads(rest)


class RealGenerated(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not (FN / 'install.mcfunction').exists():
            raise unittest.SkipTest('sortie de gen_floaty absente')
        cls.manifest_ok = (ROOT / 'tools' / 'floaty' / 'owned.txt').exists()
        cls.inst, cls.unin = lines(FN / 'install.mcfunction'), lines(FN / 'uninstall.mcfunction')

    def test_owned_manifest_exists_when_install_does(self):
        self.assertTrue(self.manifest_ok, 'install.mcfunction est là mais tools/floaty/owned.txt manque')

    def created(self, prefix):
        return {l.split()[len(prefix.split())] for l in self.inst if l.startswith(prefix + ' ')}

    def removed(self, prefix):
        return {l.split()[len(prefix.split())] for l in self.unin if l.startswith(prefix + ' ')}

    # 1. aller-retour
    def test_round_trip_objectives_teams_bossbars(self):
        for kind, add, rem in (('objectifs', 'scoreboard objectives add', 'scoreboard objectives remove'),
                               ('équipes', 'team add', 'team remove'), ('bossbars', 'bossbar add', 'bossbar remove')):
            with self.subTest(kind):
                made, gone = self.created(add), self.removed(rem)
                self.assertTrue(made, kind)
                self.assertEqual(made, gone)
                self.assertEqual(len([l for l in self.inst if l.startswith(add + ' ')]), len(made), 'doublon dans install')
                self.assertEqual(len([l for l in self.unin if l.startswith(rem + ' ')]), len(gone), 'doublon dans uninstall')

    def test_every_modify_and_set_targets_a_created_object(self):
        bars, teams, objs = self.created('bossbar add'), self.created('team add'), self.created('scoreboard objectives add')
        for l in self.inst:
            w = l.split()
            if l.startswith('bossbar set '):
                self.assertIn(w[2], bars, l)
            elif l.startswith('team modify '):
                self.assertIn(w[2], teams, l)
            elif l.startswith('scoreboard objectives modify '):
                self.assertIn(w[3], objs, l)
            elif l.startswith('scoreboard players set '):
                self.assertIn(w[4], objs, l)

    # 2. gardes
    def test_install_guard_first_and_flag_set_once(self):
        self.assertEqual(self.inst[0], f'execute if data storage {GUARD} run return 0')
        flags = [i for i, l in enumerate(self.inst) if l == f'data modify storage {GUARD} set value 1b']
        self.assertEqual(flags, [1])        # posé une seule fois, juste après la garde (avant le reste)
        self.assertEqual([l for l in self.inst if ' run return ' in l], [self.inst[0]])

    def test_uninstall_inverse_guard_and_flag_removed_last(self):
        g = self.unin.index(f'execute unless data storage {GUARD} run return 0')
        self.assertTrue(all(l.startswith('schedule clear ') for l in self.unin[:g]))       # les schedule clear passent AVANT la garde
        self.assertEqual(self.unin[-1], f'data remove storage {GUARD}')
        self.assertEqual(sum(GUARD in l for l in self.unin), 2)
        self.assertEqual([l for l in self.unin if ' run return ' in l], [self.unin[g]])

    # 3. verbes
    def test_only_expected_verbs(self):
        for name, ls in (('install', self.inst), ('uninstall', self.unin)):
            for l in ls:
                self.assertIn(l.split()[0], VERBS, f'{name} : {l}')
            self.assertFalse([l for l in ls if re.search(r'objectives setdisplay|^(say|kill|tp|gamerule) ', l)])
            self.assertFalse([l for l in ls if l.startswith('execute') and ' run ' in l and not l.endswith('return 0')])

    def test_uninstall_verbs_are_removals(self):
        g = self.unin.index(f'execute unless data storage {GUARD} run return 0')
        for l in self.unin[:g] + self.unin[g + 1:]:
            self.assertRegex(l, r'^(bossbar remove|team remove|scoreboard objectives remove|data remove storage|schedule clear) ')

    # 4. composants texte parsables
    def test_text_components_are_valid_json(self):
        n = 0
        for l in self.inst:
            if l.startswith('scoreboard objectives add '):
                rest = l.split(' ', 5)[5]
            elif l.startswith('bossbar add ') or l.startswith('team add '):
                rest = l.split(' ', 3)[3]
            else:
                continue
            with self.subTest(l[:80]):
                self.assertIsInstance(title(rest), (str, dict, list))
                n += 1
        self.assertGreater(n, 50)

    def test_prefix_suffix_components_are_valid_json(self):
        for l in self.inst:
            if l.startswith('team modify ') and l.split()[3] in ('prefix', 'suffix'):
                title(l.split(' ', 4)[4])

    # 5. dimension
    def test_dimension_floaty_equals_ombrelune(self):
        d = ROOT / 'data' / 'mg' / 'dimension'
        self.assertTrue((d / 'floaty.json').exists())
        self.assertEqual(json.loads((d / 'floaty.json').read_text(encoding='utf-8')), json.loads((d / 'ombrelune.json').read_text(encoding='utf-8')))


if __name__ == '__main__':
    unittest.main()
