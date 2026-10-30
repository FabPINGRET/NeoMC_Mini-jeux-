"""tools/floaty, lot L3 : invariants sur la sortie RÉELLE (data/mg/function/floaty/*, fichiers suivis, data/<ns de la carte>/**).
Sautés si la sortie générée est absente (la CI n'a pas la carte). Complète test_floaty_catchup_wire.py / test_floaty_core.py (faux dépôt).
Lancer : python -m unittest discover -s tools/tests -v
"""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'floaty'))
import fl_wire as W  # noqa: E402

DATA = ROOT / 'data'
MG = DATA / 'mg' / 'function'
FL = MG / 'floaty'
MAP_NS = [p for p in DATA.iterdir() if p.is_dir() and p.name not in ('mg', 'minecraft')] if DATA.exists() else []


def real(rel):
    return (MG / (rel + '.mcfunction')).read_text(encoding='utf-8').replace('\r\n', '\n').split('\n')


def code(rel):
    return [l for l in real(rel) if l.strip() and not l.startswith('#')]


def need_output(tc):
    if not (FL / 'enter.mcfunction').exists():
        raise unittest.SkipTest('sortie de gen_floaty absente')


class Lifecycle(unittest.TestCase):
    setUpClass = classmethod(need_output)

    def test_enter_tags_after_svid_control_and_survie_vault_save(self):
        e = code('floaty/enter')
        flw = e.index('tag @s add mg.flw')
        ctrl = [i for i, l in enumerate(e) if 'mg.svid matches 1..' in l]
        self.assertEqual(len(ctrl), 2)                      # assign + refus
        self.assertTrue(all(i < flw for i in ctrl))
        # la survie est quittée (donc vault_save) AVANT enter, par menu_go
        m = code('floaty/menu_go')
        self.assertLess(m.index('execute if entity @s[tag=mg.surv] run function mg:survie/leave'), m.index(m[-1]))
        self.assertIn('mg:survie/vault_save', '\n'.join(code('survie/leave')))
        # rien dans enter n'écrase le coffre de survie (y 100 / 101)
        self.assertNotIn('vault_save', '\n'.join(e))

    def test_leave_order_and_resets(self):
        lv = code('floaty/leave')
        idx = lambda s: next(i for i, l in enumerate(lv) if s in l)
        self.assertLess(idx('vault_save'), idx('reset_player'))
        self.assertLess(idx('vault_save'), idx('xp set @s 0 levels'))
        self.assertLess(idx('vault_save'), idx('tag @s remove mg.flw'))
        for needed in ('tag @s remove mg.flw', 'function mg:floaty/attrs', 'function mg:floaty/reset_scores', 'function mg:floaty/bars'):
            self.assertIn(needed, lv)
        self.assertNotIn('clear @s', lv)                    # clear fait par reset_player (après la sauvegarde)

    def test_leave_attributes_are_reset_by_attr_reset_or_attrs(self):
        self.assertIn('function mg:core/attr_reset', code('core/reset_player'))
        base = '\n'.join(code('core/attr_reset') + code('floaty/attrs'))
        for a in ('max_health', 'scale', 'fall_damage_multiplier', 'movement_speed', 'jump_strength', 'sneaking_speed', 'armor',
                  'attack_damage', 'step_height'):
            self.assertRegex(base, r'attribute @s minecraft:%s base (set|reset)' % a, a)
        self.assertEqual(len(code('floaty/attrs')), len(W.EXTRA_ATTRS))

    def test_bars_called_after_tag_removal_and_cover_install_bars(self):
        bars = '\n'.join(code('floaty/bars'))
        inst = (DATA / 'floaty' / 'function' / 'install.mcfunction').read_text(encoding='utf-8')
        for b in re.findall(r'^bossbar add (\S+) ', inst, re.M):
            self.assertIn(f'bossbar set {b} players @a[tag=mg.flw]', bars)

    def test_reset_scores_only_resets_self(self):
        for l in code('floaty/reset_scores'):
            self.assertRegex(l, r'^scoreboard players reset @s \S+$')

    def test_strayed_intruder_never_touch_admin_play_out(self):
        for f in ('strayed', 'intruder', 'pre_tick'):
            for l in code('floaty/' + f):
                self.assertNotRegex(l, r'tag [^ ]+ (add|remove) mg\.(admin|play|out)', f)
        lv = '\n'.join(code('floaty/leave'))
        self.assertNotRegex(lv, r'mg\.admin')
        self.assertIn('tag=!mg.admin', '\n'.join(code('floaty/pre_tick')))       # les admins ne sont jamais renvoyés


class Session(unittest.TestCase):
    setUpClass = classmethod(need_output)

    def simulate(self, counts):
        """Rejoue les 3 premières lignes de lobby_tick pour chaque tick (n joueurs mg.flw) ; renvoie (starts, ends, map ticks)."""
        flw, starts, ends, ticks = 0, 0, 0, 0
        lines = code('floaty/lobby_tick')
        for n in counts:
            for l in lines[1:]:
                m = re.match(r'execute (if|unless) score \$flw mg\.st matches (\S+) (?:(if|unless) entity @a\[tag=mg\.flw\] )?(?:in mg:floaty )?'
                             r'(?:positioned \S+ \S+ \S+ )?run function (\S+)$', l)
                self.assertTrue(m, l)
                sc, rng, en, fn = m.groups()
                lo, hi = (int(rng.split('..')[0]), 10 ** 9) if rng.endswith('..') else (int(rng), int(rng))
                ok = (lo <= flw <= hi) == (sc == 'if')
                if en:
                    ok = ok and ((n > 0) == (en == 'if'))
                if not ok:
                    continue
                if fn == 'mg:floaty/session_start':
                    starts += 1
                    flw = 1
                elif fn == 'mg:floaty/session_end':
                    ends += 1
                    flw = 0
                elif fn == 'floaty:map/tick':
                    ticks += 1
        return starts, ends, ticks

    def test_transitions_once_each(self):
        self.assertEqual(self.simulate([0, 0, 1, 1, 2, 1, 0, 0, 1, 0]), (2, 2, 5))   # ticks de carte : 4 (1er passage) + 1 (2e)

    def test_no_players_no_session_no_map_tick(self):
        self.assertEqual(self.simulate([0] * 5), (0, 0, 0))

    def test_stable_presence_starts_once(self):
        s, e, t = self.simulate([3] * 6)
        self.assertEqual((s, e, t), (1, 0, 6))

    def test_session_functions_set_flag_and_use_one_zone(self):
        self.assertIn('scoreboard players set $flw mg.st 1', code('floaty/session_start'))
        self.assertIn('scoreboard players set $flw mg.st 0', code('floaty/session_end'))
        self.assertIn('scoreboard players set $flw mg.st 0', code('core/load'))
        self.assertIn(f'execute in mg:floaty run forceload add {W.FORCE}', code('floaty/session_start'))
        self.assertIn(f'execute in mg:floaty run forceload remove {W.FORCE}', code('floaty/session_end'))
        self.assertNotIn('forceload add', '\n'.join(code('floaty/session_end')))
        self.assertNotIn('forceload remove', '\n'.join(code('floaty/session_start')))

    def test_every_forceload_in_pack_uses_the_floaty_zone(self):
        n = 0
        for p in list(MG.rglob('*.mcfunction')):
            for l in p.read_text(encoding='utf-8').split('\n'):
                if 'in mg:floaty run forceload' in l:
                    self.assertTrue(l.rstrip().endswith(W.FORCE), (p.name, l))
                    n += 1
        self.assertGreaterEqual(n, 4)        # session_start, session_end, load, desinstaller

    def test_map_tick_only_from_lobby_tick_guarded(self):
        hits = [p for p in DATA.rglob('*.mcfunction') if 'floaty:map/tick' in p.read_text(encoding='utf-8')]
        self.assertEqual([p.name for p in hits], ['lobby_tick.mcfunction'])
        l = next(l for l in code('floaty/lobby_tick') if 'floaty:map/tick' in l)
        self.assertTrue(l.startswith('execute if score $flw mg.st matches 1.. in mg:floaty '))


class Catchup(unittest.TestCase):
    setUpClass = classmethod(need_output)

    def matching(self, lines, k):
        out = []
        for l in lines:
            m = re.match(r'execute (if|unless) score \$flsp mg\.st matches (\S+) in mg:floaty run', l)
            if not m:
                continue
            lo, hi = (int(m.group(2)[:-2]), 10 ** 9) if m.group(2).endswith('..') else (int(m.group(2)), int(m.group(2)))
            if (lo <= k <= hi) == (m.group(1) == 'if'):
                out.append(l)
        return out

    def test_tp_and_spawnpoint_exactly_one_per_checkpoint_including_zero(self):
        tp = code('floaty/cu/tp')
        sp = [l for l in code('floaty/cu/run') if ' run spawnpoint @s ' in l]
        n = sum(' if score' in ' ' + l for l in tp)
        self.assertGreater(n, 5)
        for k in range(0, n + 1):
            self.assertEqual(len(self.matching(tp, k)), 1, f'tp k={k}')
            self.assertEqual(len(self.matching(sp, k)), 1, f'spawnpoint k={k}')

    def test_checkpoint_zero_goes_to_map_spawn_never_null_coordinates(self):
        only = self.matching(code('floaty/cu/tp'), 0)[0]
        self.assertTrue(only.endswith('tp @s 1274.5 209 181.5'))
        for l in code('floaty/cu/tp') + code('floaty/cu/run'):
            self.assertNotRegex(l, r'(tp|spawnpoint) @s 0(\.5)? 0 0(\.5)?\b', l)

    def test_hearts_guard_zero_counter_never_sets_attribute(self):
        run = code('floaty/cu/run')
        g = [l for l in run if 'HeartContainers' in l]
        self.assertEqual(len(g), 2)
        self.assertTrue(all('if score Inventory HeartContainers matches 1.. ' in l for l in g))
        self.assertEqual(code('floaty/cu/hp'), ['$attribute @s minecraft:max_health base set $(h)'])
        self.assertNotIn('max_health', '\n'.join(run))

    def test_only_map_advancements_regranted(self):
        grants = [l for l in code('floaty/cu/run') if 'advancement grant' in l]
        self.assertGreater(len(grants), 10)
        ns_dirs = {p.name for p in MAP_NS}
        for l in grants:
            m = re.match(r'execute if score \$fla\d+ mg\.fla matches 1 run advancement grant @s only (\w+):(\S+)$', l)
            self.assertTrue(m, l)
            self.assertIn(m.group(1), ns_dirs, l)
            self.assertTrue((DATA / m.group(1) / 'advancement' / (m.group(2) + '.json')).exists(), l)
        ids = [re.search(r'\$fla(\d+)', l).group(1) for l in grants]
        self.assertEqual(len(ids), len(set(ids)))

    def test_run_calls_hp_and_flags_reset_on_new_game(self):
        self.assertIn('mg:floaty/cu/hp with storage mg:floaty cu', '\n'.join(code('floaty/cu/run')))
        ini = (DATA / 'game' / 'function' / 'initialize.mcfunction').read_text(encoding='utf-8')
        self.assertIn('scoreboard players set $flsp mg.st 0', ini)
        self.assertIn('scoreboard players reset * mg.fla', ini)

    def test_reconnect_catchup_guarded_and_before_return(self):
        r = code('core/reconnect')
        c = r.index('execute if entity @s[tag=mg.flw] run function mg:floaty/cu/run')
        self.assertLess(c, r.index('execute if entity @s[tag=mg.surv] run return 0'))
        self.assertEqual(sum('floaty/cu/run' in l for l in r), 1)


class TimeNeutral(unittest.TestCase):
    setUpClass = classmethod(need_output)
    BAD = re.compile(r'(^|[\s:$])(gamerule (advance_time|random_tick_speed)|time (set|add))\b')
    DANGLING = re.compile(r'(^|\s)run\s*$')

    def test_no_global_time_state_in_map_output(self):
        n = 0
        for ns in MAP_NS:
            for p in ns.rglob('*.mcfunction'):
                for i, l in enumerate(p.read_text(encoding='utf-8').split('\n'), 1):
                    n += 1
                    if l.startswith('#'):
                        continue
                    self.assertIsNone(self.BAD.search(l), f'{p.relative_to(DATA)}:{i}: {l}')
                    self.assertIsNone(self.DANGLING.search(l), f'{p.relative_to(DATA)}:{i}: run sans commande')
        self.assertGreater(n, 1000)

    def test_detector_catches_bad_lines(self):
        for l in ('gamerule advance_time false', 'execute in mg:floaty run time set 6000', '$time add 5', 'execute as @a run gamerule random_tick_speed 3'):
            self.assertTrue(self.BAD.search(l), l)
        for l in ('time query daytime', 'data modify entity @s x_time set value 1'):
            self.assertIsNone(self.BAD.search(l), l)
        self.assertTrue(self.DANGLING.search('execute if x run'))
        self.assertIsNone(self.DANGLING.search('function a:chase_run'))


class Uninstall(unittest.TestCase):
    setUpClass = classmethod(need_output)

    def test_everything_l3_creates_is_removed(self):
        d = '\n'.join(code('desinstaller'))
        load = '\n'.join(code('core/load'))
        self.assertIn('scoreboard objectives add mg.fla dummy', load)
        self.assertIn('scoreboard objectives remove mg.fla', d)
        files = [p for p in FL.rglob('*.mcfunction')] + [MG / 'core' / n for n in ('pull_all.mcfunction', 'optout.mcfunction', 'request.mcfunction')]
        tags, roots = set(), set()
        for p in files:
            t = p.read_text(encoding='utf-8')
            tags |= set(re.findall(r'tag @\S+ add (mg\.f?l?\w*(?:flw|pullw|pulls))\b', t))
            roots |= set(re.findall(r'storage mg:floaty (\w+)', t))
        self.assertTrue({'mg.flw', 'mg.pullw'} <= tags, tags)
        for t in tags - {'mg.pulls'}:
            self.assertRegex(d, r'tag @a remove %s\b' % re.escape(t))
        self.assertTrue({'v', 'cu'} <= roots, roots)
        for r in roots:
            self.assertIn(f'data remove storage mg:floaty {r}', d)
        self.assertIn(f'execute in mg:floaty run forceload remove {W.FORCE}', d)

    def test_every_mg_objective_used_by_floaty_functions_exists(self):
        load_all = '\n'.join((MG / 'core' / 'load.mcfunction').read_text(encoding='utf-8').split('\n'))
        used = set()
        for p in FL.rglob('*.mcfunction'):
            used |= set(re.findall(r'\b(mg\.fla)\b', p.read_text(encoding='utf-8')))
        for o in used:
            self.assertIn(f'scoreboard objectives add {o} dummy', load_all)


if __name__ == '__main__':
    unittest.main()
