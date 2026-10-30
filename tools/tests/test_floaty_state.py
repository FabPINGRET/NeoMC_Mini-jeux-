"""tools/floaty : fl_state (scoreboard.dat / custom_boss_events.dat / command_storage_*.dat -> install et uninstall) et lecture SNBT de fl_nbt,
sur de faux .dat (NBT gzip construit ici) en dossier temporaire — la vraie carte n'est pas nécessaire (la CI ne l'a pas).
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import gzip
import struct
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'floaty'))
import fl_nbt  # noqa: E402
import gen_floaty  # noqa: E402,F401   (pose tools/lib dans sys.path : fl_state importe mcfn)
import fl_state as S  # noqa: E402

UUID = '74ec4699-b99c-475c-8c7a-d97d46ca6365'
_FMT = {1: '>b', 2: '>h', 3: '>i', 4: '>q', 5: '>f', 6: '>d'}


def name(s):
    b = s.encode('utf-8')
    return struct.pack('>H', len(b)) + b


def payload(t, v):
    """Encodeur NBT minimal : v = valeur Python du type t (compound : {nom: (type, valeur)}, liste : (type des éléments, [valeurs]))."""
    if t in _FMT:
        return struct.pack(_FMT[t], v)
    if t == 7:
        return struct.pack('>i', len(v)) + v
    if t == 8:
        return name(v)
    if t == 9:
        sub, items = v
        return bytes([sub]) + struct.pack('>i', len(items)) + b''.join(payload(sub, x) for x in items)
    if t == 10:
        return b''.join(bytes([ct]) + name(k) + payload(ct, cv) for k, (ct, cv) in v.items()) + b'\x00'
    if t == 11:
        return struct.pack('>i', len(v)) + b''.join(struct.pack('>i', x) for x in v)
    raise ValueError(t)


def dat(fields):
    return gzip.compress(b'\x0a' + name('') + payload(10, fields))


def Str(v): return 8, v
def Int(v): return 3, v
def Byte(v): return 1, v
def Comp(d): return 10, d
def Lst(sub, items): return 9, (sub, items)


BOARD = {'data': Comp({
    'Objectives': Lst(10, [
        {'Name': Str('Kills'), 'DisplayName': Str('Kills'), 'CriteriaName': Str('playerKillCount')},
        {'Name': Str('Value'), 'DisplayName': Comp({'text': Str('V'), 'bold': Byte(1)})},
        {'Name': Str('Hp'), 'DisplayName': Str('Hp'), 'CriteriaName': Str('health'), 'RenderType': Str('hearts')},
        {'Name': Str('bad name'), 'DisplayName': Str('x')}]),
    'Teams': Lst(10, [
        {'Name': Str('hero'), 'DisplayName': Str('Hero'), 'TeamColor': Str('gold'), 'AllowFriendlyFire': Byte(0),
         'CollisionRule': Str('never'), 'Players': Lst(8, ['Alice', UUID])}]),
    'PlayerScores': Lst(10, [
        {'Name': Str('#fake'), 'Objective': Str('Value'), 'Score': Int(5)},
        {'Name': Str('20'), 'Objective': Str('Value'), 'Score': Int(20)},
        {'Name': Str('Time'), 'Objective': Str('Kills'), 'Score': Int(9)},          # ressemble à un pseudo, mais n'est pas un joueur
        {'Name': Str('Alice'), 'Objective': Str('Kills'), 'Score': Int(3)},          # membre d'équipe : vrai joueur
        {'Name': Str('LordDrewpicus'), 'Objective': Str('Kills'), 'Score': Int(1)},  # l'auteur
        {'Name': Str(UUID), 'Objective': Str('Value'), 'Score': Int(7)},             # entité du monde d'origine
        {'Name': Str('#unset'), 'Objective': Str('Value'), 'Locked': Byte(1)},       # Score absent = 0 (le codec n'écrit pas le défaut)
        {'Name': Str('x y'), 'Objective': Str('Value'), 'Score': Int(2)},            # inutilisable dans une commande
        {'Name': Str('#ghost'), 'Objective': Str('Ghost'), 'Score': Int(2)}])})}     # objectif non déclaré

BARS = {'data': Comp({
    'boss:a': Comp({'Name': Comp({'text': Str('A'), 'bold': Byte(1)}), 'Color': Str('red'), 'Overlay': Str('notched_6'), 'Max': Int(6),
                    'Value': Int(6), 'Visible': Byte(1), 'Players': Lst(11, [[1, 2, 3, 4]])}),
    'Bad Id': Comp({'Name': Str('x')})})}

STORE = {'data': Comp({'contents': Comp({
    'st': Comp({'flag': Byte(1), 'big': (4, 5), 'arr': (11, [1, 2]), 'name': Str('a"b'), 'odd key': Int(2), 'a.b': Int(1)}),
    'Bad': Comp({'a': Int(1)})})})}
STORE_MG = {'data': Comp({'contents': Comp({'x': Comp({'a': Int(1)})})})}

INSTALL = [
    'scoreboard objectives add Hp health "Hp"', 'scoreboard objectives modify Hp rendertype hearts',
    'scoreboard objectives add Kills playerKillCount "Kills"', 'scoreboard objectives add Value dummy {"text":"V","bold":true}',
    'team add hero "Hero"', 'team modify hero friendlyFire false', 'team modify hero color gold', 'team modify hero collisionRule never',
    'scoreboard players set Time Kills 9', 'scoreboard players set #fake Value 5', 'scoreboard players set #unset Value 0',
    'scoreboard players set 20 Value 20',
    'bossbar add boss:a {"text":"A","bold":true}', 'bossbar set boss:a color red', 'bossbar set boss:a style notched_6',
    'bossbar set boss:a max 6', 'bossbar set boss:a value 6', 'bossbar set boss:a visible true',
    r'data merge storage foo:st {flag:1b,big:5L,arr:[I;1,2],name:"a\"b","odd key":2,a.b:1}']
UNINSTALL = ['execute unless data storage mg:floaty installed run return 0',
             'bossbar remove boss:a', 'team remove hero', 'scoreboard objectives remove Hp',
             'scoreboard objectives remove Kills', 'scoreboard objectives remove Value',
             'data remove storage foo:st flag', 'data remove storage foo:st big', 'data remove storage foo:st arr',
             'data remove storage foo:st name', 'data remove storage foo:st "odd key"', 'data remove storage foo:st "a.b"',
             'data remove storage mg:floaty installed']

# cas limites : propriétés absentes (défauts), refusées, équipe invalide, Score absent / non entier
BOARD_EDGE = {'data': Comp({
    'Objectives': Lst(10, [{'Name': Str('Hp'), 'DisplayName': Str('Hp'), 'RenderType': Int(3)},
                           {'Name': Str('Ok'), 'DisplayName': Str('Ok'), 'RenderType': Str('he arts')}]),
    'Teams': Lst(10, [{'Name': Str('bad team'), 'DisplayName': Str('x')},
                      {'Name': Str('t'), 'DisplayName': Str('T'), 'CollisionRule': Int(1), 'TeamColor': Str('gold')}]),
    'PlayerScores': Lst(10, [{'Name': Str('#z'), 'Objective': Str('Hp'), 'Locked': Byte(1)},
                             {'Name': Str('#f'), 'Objective': Str('Hp'), 'Score': Str('x')}])})}
BARS_EDGE = {'data': Comp({
    'boss:b': Comp({'Name': Str('B'), 'Color': Str('purple')}),                                   # Visible, Max, Value, Overlay absents
    'boss:c': Comp({'Name': Str('C'), 'Color': Int(3), 'Overlay': Str('bad-x'), 'Max': Int(0), 'Value': Int(-1), 'Visible': Byte(0)})})}


def event(fn, at, kind='minecraft:function'):
    return {'trigger_time': (4, at), 'callback': Comp({'id': Str(fn), 'type': Str(kind)}), 'id': Str(fn)}


EVENTS = {'data': Comp({'events': Lst(10, [event('game:a', 1010), event('game:b', 1000), event('game:nope', 1500),
                                           event('game:tag', 1005, 'minecraft:function_tag')])})}
TRAMPOLINES = {'game:a': 'floaty:sched/game/a', 'game:b': 'floaty:sched/game/b', 'game:c': 'floaty:sched/game/c'}


class FakeMapState(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.map = Path(tmp.name)
        self.mc = self.map / 'data' / 'minecraft'
        self.mc.mkdir(parents=True)

    def put(self, rel, fields):
        (self.mc / rel).write_bytes(dat(fields))

    def full(self):
        self.put('scoreboard.dat', BOARD)
        self.put('custom_boss_events.dat', BARS)
        self.put('command_storage_foo.dat', STORE)
        self.put('command_storage_mg.dat', STORE_MG)
        return S.build(self.map, 'LordDrewpicus')

    def test_install_lines(self):
        st = self.full()
        self.assertEqual(st.install[1:3], ['execute if data storage mg:floaty installed run return 0', 'data modify storage mg:floaty installed set value 1b'])
        self.assertEqual(st.install[3:], INSTALL)
        self.assertFalse([l for l in st.install if 'setdisplay' in l])

    def test_uninstall_is_symmetric(self):
        st = self.full()
        self.assertEqual(st.uninstall[1:], UNINSTALL)             # sans trampoline : la garde suit directement l'en-tete

    def test_uninstall_is_a_noop_unless_installed(self):
        """Sans la garde, désinstaller une dimension jamais installée viderait des objectifs / équipes qui ne sont pas à la carte."""
        self.assertEqual(self.full().uninstall[1], 'execute unless data storage mg:floaty installed run return 0')

    def test_schedule_clear_runs_before_the_guard(self):
        """Un trampoline replanifie par la carte doit etre annule meme si floaty n'est plus installe : schedule clear AVANT la garde."""
        st = S.build(self.map, 'x', TRAMPOLINES)
        guard = st.uninstall.index('execute unless data storage mg:floaty installed run return 0')
        self.assertEqual(st.uninstall[1:guard], ['schedule clear floaty:sched/game/a', 'schedule clear floaty:sched/game/b',
                                                 'schedule clear floaty:sched/game/c'])
        self.assertFalse([l for l in st.uninstall[guard + 1:] if l.startswith('schedule clear')])

    def test_counts_and_skipped_rules(self):
        c = self.full().counts
        self.assertEqual((c['objectives'], c['teams'], c['scores'], c['bossbars'], c['storage']), (3, 1, 4, 1, 1))
        self.assertEqual((c['scores_players'], c['scores_uuid'], c['scores_invalid']), (2, 1, 2))
        self.assertEqual((c['objectives_invalid'], c['bossbars_invalid'], c['storage_skipped']), (1, 1, 2))   # storage : « foo:Bad » et mg:x
        self.assertNotIn('scores_unset', c)
        self.assertEqual(self.full().players, ['Alice', 'LordDrewpicus'])    # noms (sans doublon) des vrais joueurs dont un score est écarté

    def test_missing_files_give_empty_sections(self):
        st = S.build(self.map, 'LordDrewpicus')
        self.assertEqual(len(st.install), 3)
        self.assertEqual(st.uninstall[1:], ['execute unless data storage mg:floaty installed run return 0', 'data remove storage mg:floaty installed'])
        self.assertEqual({k: v for k, v in st.counts.items() if v}, {})

    def test_absent_score_is_zero_and_absent_bossbar_properties_use_the_command_defaults(self):
        self.put('scoreboard.dat', BOARD_EDGE)
        self.put('custom_boss_events.dat', BARS_EDGE)
        st = S.build(self.map, 'LordDrewpicus')
        self.assertIn('scoreboard players set #z Hp 0', st.install)
        self.assertEqual([l for l in st.install if 'boss:b' in l],
                         ['bossbar add boss:b "B"', 'bossbar set boss:b color purple', 'bossbar set boss:b visible false'])
        self.assertEqual([l for l in st.install if 'boss:c' in l], ['bossbar add boss:c "C"', 'bossbar set boss:c visible false'])
        self.assertEqual([l for l in st.install if l.startswith('team ')], ['team add t "T"', 'team modify t color gold'])   # pas d'option absente

    def test_invalid_values_are_refused_and_counted(self):
        self.put('scoreboard.dat', BOARD_EDGE)
        self.put('custom_boss_events.dat', BARS_EDGE)
        c = S.build(self.map, 'LordDrewpicus').counts
        self.assertEqual((c['teams_invalid'], c['teams']), (1, 1))
        self.assertEqual(c['options_invalid'], 3)               # rendertype Int, rendertype « he arts », collisionRule Int
        self.assertEqual(c['bossbar_props_invalid'], 4)         # Color Int, Overlay « bad-x », Max 0, Value -1
        self.assertEqual((c['scores'], c['scores_invalid']), (1, 1))     # #z installé ; #f : Score non entier
        self.assertEqual(c['objectives'], 2)                    # une option refusée ne retire pas l'objectif

    def test_scheduled_events_use_trampolines_with_remaining_delay(self):
        self.put('scheduled_events.dat', EVENTS)
        (self.map / 'level.dat').write_bytes(dat({'Data': Comp({'Time': (4, 1000)})}))       # racine « Data » : celle du vrai level.dat
        st = S.build(self.map, 'LordDrewpicus', TRAMPOLINES)
        self.assertEqual(st.install[3:], ['schedule function floaty:sched/game/b 1t replace',      # reste 0 -> au moins 1 tick
                                          'schedule function floaty:sched/game/a 10t replace'])
        self.assertEqual(st.uninstall[1:5], ['schedule clear floaty:sched/game/a', 'schedule clear floaty:sched/game/b',
                                             'schedule clear floaty:sched/game/c',            # c : aucun event en attente, mais la carte peut la replanifier
                                             'execute unless data storage mg:floaty installed run return 0'])
        self.assertEqual(st.uninstall[-1], 'data remove storage mg:floaty installed')
        c = st.counts
        self.assertEqual((c['sched_events'], c['sched_installed'], c['sched_missing'], c['sched_other']), (3, 2, 1, 1))
        self.assertEqual(st.sched_missing, ['game:nope'])

    def test_scheduled_events_without_level_time_or_trampolines(self):
        self.put('scheduled_events.dat', EVENTS)
        self.assertEqual([l for l in S.build(self.map, 'x', TRAMPOLINES).install if l.startswith('schedule')],
                         ['schedule function floaty:sched/game/a 1t replace', 'schedule function floaty:sched/game/b 1t replace'])
        none = S.build(self.map, 'x')
        self.assertFalse([l for l in none.install if l.startswith('schedule')])
        self.assertEqual(none.sched_missing, ['game:a', 'game:b', 'game:nope'])

    def test_unreadable_dat_raises(self):
        (self.mc / 'scoreboard.dat').write_bytes(b'pas du nbt')
        with self.assertRaises(Exception):
            S.build(self.map, 'LordDrewpicus')

    def test_component_converts_style_bytes_to_booleans(self):
        self.assertEqual(S.component({'bold': 1, 'italic': 0, 'extra': [{'obfuscated': 1, 'text': 't'}, 'x'], 'x': 1}),
                         {'bold': True, 'italic': False, 'extra': [{'obfuscated': True, 'text': 't'}, 'x'], 'x': 1})


class SnbtReader(unittest.TestCase):
    def test_types_survive(self):
        raw = dat({'v': Comp({'b': Byte(1), 's': (2, -3), 'i': Int(4), 'l': (4, 5), 'f': (5, 1.5), 'd': (6, 2.25), 't': Str('x\ny'),
                              'ba': (7, b'\x01\xff'), 'ia': (11, [1, 2]), 'list': Lst(3, [1, 2]), 'cl': Lst(10, [{'k': Int(1)}]),
                              'empty': Lst(3, []), 'a b': Int(0)})})
        got = fl_nbt.snbt(fl_nbt.loads(raw, snbt=True)['v'])
        self.assertEqual(got, r'{b:1b,s:-3s,i:4,l:5L,f:1.5f,d:2.25d,t:"x\ny",ba:[B;1b,-1b],ia:[I;1,2],list:[1,2],cl:[{k:1}],empty:[],"a b":0}')

    def test_plain_read_is_unchanged(self):
        root = fl_nbt.loads(dat({'v': Comp({'b': Byte(1), 'l': (4, 5)})}))
        self.assertEqual(root, {'v': {'b': 1, 'l': 5}})
        self.assertNotIsInstance(root['v']['b'], fl_nbt.Snbt)


if __name__ == '__main__':
    unittest.main()
