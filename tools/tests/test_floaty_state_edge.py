"""tools/floaty, fl_state : cas limites de valeurs (displayName à guillemets / antislash / unicode, bornes de bossbar, scores négatifs, noms de
faux joueurs spéciaux) sur de faux .dat en dossier temporaire. Complète test_floaty_state.py (mêmes aides, sans rejouer ses tests).
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_floaty_state as T  # noqa: E402  (module : unittest rejouerait ses tests si on importait la classe)
import fl_state as S  # noqa: E402

Str, Int, Comp, Lst = T.Str, T.Int, T.Comp, T.Lst
WEIRD = 'a"b\\c é☠ \\"x'
FAKES = ['#x', '$y', '-1', '$-1', '#a.b', '#', '$', '1', '#a-b']


def board(objs, scores=()):
    return {'data': Comp({'Objectives': Lst(10, objs), 'PlayerScores': Lst(10, list(scores))})}


class StateEdge(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.map = Path(tmp.name)
        self.mc = self.map / 'data' / 'minecraft'
        self.mc.mkdir(parents=True)

    def put(self, rel, fields):
        (self.mc / rel).write_bytes(T.dat(fields))

    def build(self):
        return S.build(self.map, 'LordDrewpicus')

    def test_displayname_with_quotes_backslash_unicode_roundtrips(self):
        self.put('scoreboard.dat', board([{'Name': Str('O'), 'DisplayName': Str(WEIRD)},
                                          {'Name': Str('P'), 'DisplayName': Comp({'text': Str(WEIRD), 'bold': T.Byte(1)})}]))
        st = self.build()
        lines = {l.split()[3]: l.split(' ', 5)[5] for l in st.install if l.startswith('scoreboard objectives add ')}
        self.assertEqual(json.loads(lines['O']), WEIRD)
        self.assertEqual(json.loads(lines['P']), {'text': WEIRD, 'bold': True})
        self.assertIn('é☠', lines['O'])                                   # unicode laissé tel quel (ensure_ascii=False)
        self.assertEqual(st.counts['objectives'], 1 + 1)
        self.assertTrue(all('\n' not in l for l in st.install))

    def test_bossbar_name_and_team_title_with_special_characters(self):
        self.put('scoreboard.dat', {'data': Comp({'Teams': Lst(10, [{'Name': Str('t'), 'DisplayName': Str(WEIRD),
                                                                      'MemberNamePrefix': Str(WEIRD)}])})})
        self.put('custom_boss_events.dat', {'data': Comp({'boss:q': Comp({'Name': Str(WEIRD)})})})
        st = self.build()
        self.assertEqual(json.loads([l for l in st.install if l.startswith('team add')][0].split(' ', 3)[3]), WEIRD)
        self.assertEqual(json.loads([l for l in st.install if 'prefix' in l][0].split(' ', 4)[4]), WEIRD)
        self.assertEqual(json.loads([l for l in st.install if l.startswith('bossbar add')][0].split(' ', 3)[3]), WEIRD)

    def test_bossbar_bounds_refused_and_counted(self):
        bars = {'boss:neg': Comp({'Name': Str('n'), 'Max': Int(-5), 'Value': Int(-1)}), 'boss:zero': Comp({'Name': Str('z'), 'Max': Int(0)}),
                'boss:min': Comp({'Name': Str('m'), 'Max': Int(1), 'Value': Int(0)}), 'boss:big': Comp({'Name': Str('b'), 'Max': Int(2147483647)}),
                'boss:float': Comp({'Name': Str('f'), 'Max': (5, 3.0), 'Value': (4, 2)})}    # Value long : un entier NBT, accepté
        self.put('custom_boss_events.dat', {'data': Comp(bars)})
        st = self.build()
        got = [l for l in st.install if l.startswith('bossbar set') and (' max ' in l or ' value ' in l)]
        self.assertEqual(sorted(got), ['bossbar set boss:big max 2147483647', 'bossbar set boss:float value 2',
                                'bossbar set boss:min max 1', 'bossbar set boss:min value 0'])
        self.assertEqual(st.counts['bossbar_props_invalid'], 2 + 1 + 1)    # neg : 2 ; zero : 1 ; float : Max 3.0 refusé
        self.assertEqual(st.counts['bossbars'], 5)                         # une propriété refusée ne retire pas la bossbar
        self.assertEqual(sum(l.startswith('bossbar remove') for l in st.uninstall), 5)

    def test_bossbar_max_comes_before_value(self):
        self.put('custom_boss_events.dat', {'data': Comp({'boss:a': Comp({'Name': Str('a'), 'Max': Int(10), 'Value': Int(7)})})})
        ls = self.build().install
        self.assertLess(ls.index('bossbar set boss:a max 10'), ls.index('bossbar set boss:a value 7'))

    def test_negative_and_extreme_scores_kept(self):
        self.put('scoreboard.dat', board([{'Name': Str('V'), 'DisplayName': Str('V')}], [
            {'Name': Str('#neg'), 'Objective': Str('V'), 'Score': Int(-5)},
            {'Name': Str('#min'), 'Objective': Str('V'), 'Score': Int(-2147483648)},
            {'Name': Str('#max'), 'Objective': Str('V'), 'Score': Int(2147483647)}]))
        st = self.build()
        self.assertEqual(sorted(l for l in st.install if l.startswith('scoreboard players set')),
                         ['scoreboard players set #max V 2147483647', 'scoreboard players set #min V -2147483648', 'scoreboard players set #neg V -5'])
        self.assertEqual(st.counts['scores_invalid'], 0)

    def test_fake_player_names_with_special_prefixes(self):
        self.put('scoreboard.dat', board([{'Name': Str('V'), 'DisplayName': Str('V')}],
                                         [{'Name': Str(n), 'Objective': Str('V'), 'Score': Int(i)} for i, n in enumerate(FAKES)]))
        st = self.build()
        self.assertEqual(sorted(l for l in st.install if l.startswith('scoreboard players set')),
                         sorted(f'scoreboard players set {n} V {i}' for i, n in enumerate(FAKES)))
        self.assertEqual((st.counts['scores'], st.counts['scores_invalid'], st.counts['scores_players']), (len(FAKES), 0, 0))

    def test_unusable_player_names_refused(self):
        bad = ['@a', '*', '@s x', '', 'a b', 'a\tb', ' #x']
        self.put('scoreboard.dat', board([{'Name': Str('V'), 'DisplayName': Str('V')}],
                                         [{'Name': Str(n), 'Objective': Str('V'), 'Score': Int(1)} for n in bad]))
        st = self.build()
        self.assertEqual([l for l in st.install if l.startswith('scoreboard players')], [])
        self.assertEqual(st.counts['scores_invalid'], len(bad))

    def test_author_as_fake_name_prefix_is_still_a_real_player(self):
        self.put('scoreboard.dat', board([{'Name': Str('V'), 'DisplayName': Str('V')}],
                                         [{'Name': Str('LordDrewpicus'), 'Objective': Str('V'), 'Score': Int(1)},
                                          {'Name': Str('#LordDrewpicus'), 'Objective': Str('V'), 'Score': Int(2)}]))
        st = self.build()
        self.assertEqual([l for l in st.install if l.startswith('scoreboard players')], ['scoreboard players set #LordDrewpicus V 2'])
        self.assertEqual(st.players, ['LordDrewpicus'])


if __name__ == '__main__':
    unittest.main()
