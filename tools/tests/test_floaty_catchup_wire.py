"""tools/floaty, lot L3 : rattrapage (fl_catchup) et fonctions de branchement (fl_wire), fonctions pures, sans la carte.
Lancer : python -m unittest discover -s tools/tests -v
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'floaty'))
import fl_catchup as C  # noqa: E402
import fl_wire as W  # noqa: E402

SP = 'spawnpoint @a[tag=mg.flw] '
GR = 'advancement grant @a[tag=mg.flw] only '


class Instrument(unittest.TestCase):
    def test_spawnpoint_marker_same_prefix_and_index_by_distinct_coordinates(self):
        reg = C.Registry()
        out = C.instrument('dungeon:1/a', [SP + '1 2 3', 'execute if score a b matches 1 run ' + SP + '4 5 6 90 0', SP + '1 2 3'], reg)
        self.assertEqual(out, [SP + '1 2 3', 'scoreboard players set $flsp mg.st 1',
                               'execute if score a b matches 1 run ' + SP + '4 5 6 90 0',
                               'execute if score a b matches 1 run scoreboard players set $flsp mg.st 2',
                               SP + '1 2 3', 'scoreboard players set $flsp mg.st 1'])
        self.assertEqual(reg.counts()['spawn_sites'], 3)
        self.assertEqual(reg.counts()['checkpoints'], 2)

    def test_macro_prefix_is_kept(self):
        out = C.instrument('x:y', ['$execute if score $(a) b matches 1 run ' + SP + '1 2 3'], C.Registry())
        self.assertEqual(out[1], '$execute if score $(a) b matches 1 run scoreboard players set $flsp mg.st 1')

    def test_grant_marker_and_distinct_ids(self):
        reg = C.Registry()
        out = C.instrument('x:y', [GR + 'main_quest:a', GR + 'main_quest:b', GR + 'main_quest:a'], reg)
        self.assertEqual(out[1], 'scoreboard players set $fla1 mg.fla 1')
        self.assertEqual(out[3], 'scoreboard players set $fla2 mg.fla 1')
        self.assertEqual(out[5], 'scoreboard players set $fla1 mg.fla 1')
        self.assertEqual((reg.grant_sites, len(reg.advancements)), (3, 2))

    def test_individual_and_through_not_tracked(self):
        reg = C.Registry()
        ls = ['advancement grant @s only a:b', 'advancement grant @p only a:b', 'spawnpoint @s 1 2 3',
              'advancement grant @a[tag=mg.flw] through main_quest:root']
        self.assertEqual(C.instrument('x:y', ls, reg), ls)
        self.assertEqual(reg.counts()['grant_sites'], 0)
        self.assertEqual(len(reg.other), 1)          # le `through` est compté, pas suivi

    def test_store_prefix_is_skipped_not_duplicated(self):
        reg = C.Registry()
        ls = ['execute store result score a b run ' + SP + '1 2 3']
        self.assertEqual(C.instrument('x:y', ls, reg), ls)
        self.assertEqual(len(reg.skipped), 1)

    def test_initialize_resets_flags(self):
        out = C.instrument('game:initialize', ['say x'], C.Registry())
        self.assertEqual(out[1:], ['scoreboard players set $flsp mg.st 0', 'scoreboard players reset * mg.fla'])
        self.assertEqual(C.instrument('game:other', ['say x'], C.Registry()), ['say x'])


class Functions(unittest.TestCase):
    def setUp(self):
        self.reg = C.Registry()
        C.instrument('x:y', [SP + '10 64 -20 90 0', SP + '30 70 40', GR + 'main_quest:a', GR + 'sidequest:b'], self.reg)
        self.fns = C.functions(self.reg, (1274, 209, 181))

    def test_three_functions(self):
        self.assertEqual(sorted(self.fns), ['floaty/cu/hp', 'floaty/cu/run', 'floaty/cu/tp'])

    def test_run_spawnpoint_by_index_and_default(self):
        run = self.fns['floaty/cu/run']
        self.assertIn('execute unless score $flsp mg.st matches 1.. in mg:floaty run spawnpoint @s 1274 209 181', run)
        self.assertIn('execute if score $flsp mg.st matches 1 in mg:floaty run spawnpoint @s 10 64 -20 90 0', run)
        self.assertIn('execute if score $flsp mg.st matches 2 in mg:floaty run spawnpoint @s 30 70 40', run)

    def test_run_stops_before_hearts_when_game_not_started(self):
        run = self.fns['floaty/cu/run']
        stop = run.index('execute unless score mainstory Story matches 0.. run return 0')
        self.assertLess(max(i for i, l in enumerate(run) if 'spawnpoint' in l), stop)
        self.assertGreater(min(i for i, l in enumerate(run) if 'max_health' in l or 'cu/hp' in l), stop)
        self.assertGreater(min(i for i, l in enumerate(run) if 'advancement grant' in l), stop)

    def test_run_hearts_is_twice_the_counter(self):
        run = '\n'.join(self.fns['floaty/cu/run'])
        self.assertIn('store result storage mg:floaty cu.h int 2 run scoreboard players get Inventory HeartContainers', run)
        self.assertEqual(self.fns['floaty/cu/hp'][1], '$attribute @s minecraft:max_health base set $(h)')

    def test_run_regrants_each_tracked_advancement(self):
        run = self.fns['floaty/cu/run']
        self.assertIn('execute if score $fla1 mg.fla matches 1 run advancement grant @s only main_quest:a', run)
        self.assertIn('execute if score $fla2 mg.fla matches 1 run advancement grant @s only sidequest:b', run)

    def test_tp_to_block_centre_or_spawn(self):
        tp = self.fns['floaty/cu/tp']
        self.assertIn('execute if score $flsp mg.st matches 1 in mg:floaty run tp @s 10.5 64 -19.5 90 0', tp)
        self.assertIn('execute unless score $flsp mg.st matches 1.. in mg:floaty run tp @s 1274.5 209 181.5', tp)


class Wire(unittest.TestCase):
    VAULT = {k: ['# src'] + [f'$data modify block $(x) 10{i % 2} -30000 Items set value {i}' for i in range(41)] for k in ('save', 'load')}
    INSTALL = ['scoreboard objectives add a dummy', 'scoreboard objectives add hp health', 'scoreboard objectives add t trigger',
               'bossbar add floaty:b1 "x"', 'bossbar add floaty:b2 "y"']

    def setUp(self):
        self.fn = W.functions(self.INSTALL, (1274, 209, 181), {'floaty/cu/run': ['# r'], 'floaty/cu/tp': ['# t']}, self.VAULT)

    def test_vault_is_shifted_by_two(self):
        s = self.fn['floaty/vault_save']
        self.assertEqual(sum('-30000' in l for l in s), 41)
        self.assertFalse([l for l in s if ' 100 -30000' in l or ' 101 -30000' in l])
        self.assertTrue([l for l in s if '$(x) 102 -30000' in l] and [l for l in s if '$(x) 103 -30000' in l])
        self.assertIn('$execute unless block $(x) 103 -30000 minecraft:barrel run setblock $(x) 103 -30000 minecraft:barrel', self.fn['floaty/vault_make'])

    def test_vault_format_change_aborts(self):
        bad = {'save': ['# s', '$data modify block $(x) 100 -30000 Items set value 1'], 'load': self.VAULT['load']}
        with self.assertRaises(SystemExit):
            W.vault_functions(bad)

    def test_lobby_tick_session_and_map_tick(self):
        t = self.fn['floaty/lobby_tick']
        self.assertEqual(t[1], 'execute unless score $setup mg.st matches 1 run return 0')
        self.assertIn('execute unless score $flw mg.st matches 1 if entity @a[tag=mg.flw] run function mg:floaty/session_start', t)
        self.assertIn('execute if score $flw mg.st matches 1 unless entity @a[tag=mg.flw] run function mg:floaty/session_end', t)
        self.assertIn('execute if score $flw mg.st matches 1.. in mg:floaty positioned 1274 209 181 run function floaty:map/tick', t)

    def test_session_forceload_and_load(self):
        self.assertIn('execute in mg:floaty run forceload add -9776 416 -9761 431', self.fn['floaty/session_start'])
        self.assertIn('execute in mg:floaty positioned 1274 209 181 run function floaty:map/load', self.fn['floaty/session_start'])
        self.assertIn('execute in mg:floaty run forceload remove -9776 416 -9761 431', self.fn['floaty/session_end'])

    def test_pre_tick_strayed_and_intruder(self):
        p = self.fn['floaty/pre_tick']
        self.assertIn('execute as @a[tag=mg.flw] at @s unless dimension mg:floaty run function mg:floaty/strayed', p)
        self.assertIn('execute as @a[tag=!mg.flw,tag=!mg.admin] at @s if dimension mg:floaty run function mg:floaty/intruder', p)
        self.assertEqual(self.fn['floaty/strayed'][1], 'execute in minecraft:overworld run function mg:floaty/leave')
        self.assertIn('unless entity @s[tag=mg.play] unless entity @s[tag=mg.out]', self.fn['floaty/intruder'][1])

    def test_enter_order(self):
        e = self.fn['floaty/enter']
        idx = {l: i for i, l in enumerate(e)}
        self.assertLess(idx['function floaty:install'], idx['tag @s add mg.flw'])
        self.assertLess(idx['tag @s add mg.flw'], idx['function mg:floaty/cu/run'])
        self.assertLess(idx['function mg:floaty/cu/run'], idx['function mg:floaty/cu/tp'])
        self.assertLess(idx['execute in minecraft:overworld run function mg:floaty/vault_load with storage mg:floaty v'], idx['function mg:floaty/cu/run'])
        self.assertIn('execute if entity @s[tag=mg.flw] run return 0', e)       # déjà dans la carte : rien
        self.assertLess(e.index('execute unless score @s mg.svid matches 1.. in minecraft:overworld run function mg:survie/assign'),
                        e.index('function floaty:install'))

    def test_enter_without_vault_slot_says_so(self):
        e = self.fn['floaty/enter']
        l = next(l for l in e if l.startswith('execute unless score @s mg.svid matches 1.. run return'))
        self.assertIn('run return run tellraw @s {"text":"⚠ Aucun emplacement de coffre libre : Floaty indisponible.","color":"red"}', l)
        self.assertLess(e.index(l), e.index('function floaty:install'))             # rien n'est modifié avant ce refus

    def test_leave_saves_vault_then_resets(self):
        lv = self.fn['floaty/leave']
        self.assertEqual(lv[1], 'execute unless entity @s[tag=mg.flw] run return 0')
        sv = next(i for i, l in enumerate(lv) if 'vault_save' in l)
        rm = lv.index('tag @s remove mg.flw')
        self.assertLess(sv, rm)
        self.assertLess(rm, lv.index('function mg:floaty/bars'))                 # bars APRES le retrait du tag
        self.assertIn('execute in minecraft:overworld run function mg:core/reset_player', lv)

    def test_bars_and_reset_scores(self):
        b = '\n'.join(self.fn['floaty/bars'])
        for n in ('floaty:b1', 'floaty:b2'):
            self.assertIn(f'bossbar set {n} players @a[tag=mg.flw]', b)
        self.assertEqual(self.fn['floaty/reset_scores'][1:], ['scoreboard players reset @s hp'])      # ni dummy ni trigger

    def test_reset_scores_includes_per_player_timers_present_in_install(self):
        inst = self.INSTALL + [f'scoreboard objectives add {o} dummy "{o}"' for o in ('shrink_timer', 'HBWard', 'jump_flag_buffer', 'Story')]
        r = W.functions(inst, (1, 2, 3), {}, self.VAULT)['floaty/reset_scores']
        for o in ('shrink_timer', 'HBWard', 'jump_flag_buffer'):
            self.assertIn(f'scoreboard players reset @s {o}', r)
        self.assertNotIn('scoreboard players reset @s Story', r)                         # état du groupe : jamais remis par un joueur
        self.assertNotIn('scoreboard players reset @s grow_timer', r)                    # absent de install : ignoré

    def test_menu_go_leaves_other_worlds_then_enters(self):
        m = self.fn['floaty/menu_go']
        self.assertEqual(m[-1], 'execute in minecraft:overworld run function mg:floaty/enter')
        self.assertLess(m.index('execute if entity @s[tag=mg.surv] run function mg:survie/leave'), len(m) - 1)


if __name__ == '__main__':
    unittest.main()
