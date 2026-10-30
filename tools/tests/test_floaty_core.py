"""tools/floaty, lot L3 : patchs des fichiers suivis (fl_core) sur un faux dépôt (idempotence, abandon sans modification)
et exclusions Floaty dans les vrais fichiers suivis du pack (comme les tests de gen_filon).
Lancer : python -m unittest discover -s tools/tests -v
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'floaty'))
import fl_core as K  # noqa: E402

REAL = ROOT / 'data' / 'mg' / 'function'


def build_fake(root):
    """Un fichier par cible, avec juste les ancres de PATCHES (une ligne chacune), et un menu avec le bouton du Filon."""
    files = {}
    for kind, rel, a, b, *_ in K.PATCHES:
        files.setdefault(rel, []).append(a)
    fn = Path(root) / 'data' / 'mg' / 'function'
    for rel, ls in files.items():
        p = fn / (rel + '.mcfunction')
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text('\n'.join(['# tete'] + ls + ['# fin']) + '\n', encoding='utf-8', newline='\n')
    d = Path(root) / 'data' / 'mg' / 'dialog'
    d.mkdir(parents=True, exist_ok=True)
    (d / 'main_menu.json').write_text(json.dumps({'actions': [
        {'action': {'command': 'trigger mg.sv set 8'}}, {'action': {'command': K.AFTER_BUTTON}}, {'action': {'command': 'trigger mg.menu'}}]}), encoding='utf-8')


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in Path(root).rglob('*') if p.is_file()}


class FakeRepo(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        build_fake(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_apply_twice_is_stable(self):
        K.check(self.tmp)
        K.apply(self.tmp)
        one = snapshot(self.tmp)
        K.check(self.tmp)
        K.apply(self.tmp)
        self.assertEqual(snapshot(self.tmp), one)

    def test_every_patch_lands(self):
        K.apply(self.tmp)
        fn = Path(self.tmp) / 'data' / 'mg' / 'function'
        for kind, rel, a, b, *_ in K.PATCHES:
            text = (fn / (rel + '.mcfunction')).read_text(encoding='utf-8')
            for l in (b if kind == 'patch' else [b]):
                self.assertIn(l, text, rel)

    def test_missing_anchor_aborts_without_change(self):
        p = Path(self.tmp) / 'data' / 'mg' / 'function' / 'core' / 'tick.mcfunction'
        p.write_text('# plus d\'ancre\n', encoding='utf-8')
        before = snapshot(self.tmp)
        with self.assertRaises(SystemExit):
            K.check(self.tmp)
        self.assertEqual(snapshot(self.tmp), before)

    def test_duplicated_anchor_aborts(self):
        p = Path(self.tmp) / 'data' / 'mg' / 'function' / 'core' / 'tick.mcfunction'
        p.write_text(p.read_text(encoding='utf-8') + 'function mg:ombre/pre_tick\n', encoding='utf-8')
        with self.assertRaises(SystemExit):
            K.check(self.tmp)

    def test_missing_file_aborts(self):
        (Path(self.tmp) / 'data' / 'mg' / 'function' / 'core' / 'request.mcfunction').unlink()
        with self.assertRaises(SystemExit):
            K.check(self.tmp)

    def test_menu_button_once_after_filon(self):
        K.apply(self.tmp)
        K.apply(self.tmp)
        cmds = [a['action']['command'] for a in json.loads((Path(self.tmp) / 'data' / 'mg' / 'dialog' / 'main_menu.json').read_text(encoding='utf-8'))['actions']]
        self.assertEqual(cmds, ['trigger mg.sv set 8', K.AFTER_BUTTON, K.BUTTON, 'trigger mg.menu'])

    def test_menu_without_filon_button_aborts(self):
        p = Path(self.tmp) / 'data' / 'mg' / 'dialog' / 'main_menu.json'
        p.write_text(json.dumps({'actions': [{'action': {'command': 'trigger mg.menu'}}]}), encoding='utf-8')
        with self.assertRaises(SystemExit):
            K.check(self.tmp)


def real(rel):
    p = REAL / (rel + '.mcfunction')
    return p.read_text(encoding='utf-8').replace('\r\n', '\n').split('\n')


class RealTracked(unittest.TestCase):
    """Les fichiers suivis du dépôt : Floaty y est branché (ces tests valent aussi sans la carte)."""

    def setUp(self):
        if 'function mg:floaty/lobby_tick' not in real('core/tick'):
            self.skipTest('Floaty pas encore branché (gen_floaty non lancé)')

    def test_core_tick_calls_after_ombre_and_filon(self):
        t = real('core/tick')
        self.assertEqual(t.index('function mg:floaty/pre_tick'), t.index('function mg:ombre/pre_tick') + 1)
        self.assertEqual(t.index('function mg:floaty/lobby_tick'), t.index('function mg:filon/lobby_tick') + 1)

    def test_survie_leave_and_cmd_dispatch(self):
        self.assertIn('execute if entity @s[tag=mg.flw] run return run function mg:floaty/leave', real('survie/leave'))
        self.assertIn('execute if score @s mg.sv matches 10 run function mg:floaty/menu_go', real('survie/cmd'))

    def test_pull_all_optout_request(self):
        pa = '\n'.join(real('core/pull_all'))
        self.assertIn('tag=!mg.fnw,tag=!mg.flw] add mg.pulls', pa)
        self.assertIn('tag @a[tag=mg.flw] add mg.pullw', pa)
        self.assertIn('execute as @a[tag=mg.pullw] in minecraft:overworld run function mg:floaty/leave', pa)
        self.assertIn('tag @a[tag=mg.spectate] remove mg.pullw', pa)
        self.assertIn('execute if entity @s[tag=mg.pullw] in minecraft:overworld run function mg:floaty/enter', real('core/optout'))
        self.assertIn('tag @s remove mg.pullw', real('core/optout'))
        self.assertIn('tag @a remove mg.pullw', real('core/request'))

    def test_survie_tick_excludes_floaty_wherever_it_excludes_filon(self):
        n = 0
        for l in real('survie/tick'):
            if 'tag=!mg.fnw' in l and 'from_overworld' in l or 'tag=!mg.fnw,tag=!mg.flw,tag=!mg.svg2' in l:
                self.assertIn('tag=!mg.flw', l)
                n += 1
        self.assertEqual(n, 2)

    def test_reconnect_catchup_before_survie_return(self):
        r = real('core/reconnect')
        c = r.index('execute if entity @s[tag=mg.flw] run function mg:floaty/cu/run')
        self.assertLess(c, r.index('execute if entity @s[tag=mg.surv] run return 0'))

    def test_tpg_survie_leaves_floaty_first(self):
        s = real('tpg/survie')
        self.assertLess(next(i for i, l in enumerate(s) if 'mg:floaty/leave' in l), next(i for i, l in enumerate(s) if 'survie/enter' in l))

    def test_load_and_desinstaller(self):
        self.assertIn('scoreboard players set $flw mg.st 0', real('core/load'))
        self.assertIn('scoreboard objectives add mg.fla dummy', real('core/load'))
        self.assertIn('execute in mg:floaty run forceload remove -9776 416 -9761 431', real('core/load'))       # chunk forcé persisté : libéré au load
        d = real('desinstaller')
        self.assertIn('scoreboard objectives remove mg.fla', d)
        leave = d.index('execute as @a[tag=mg.flw] in minecraft:overworld run function mg:floaty/leave')
        self.assertEqual(d.count('execute as @a[tag=mg.flw] in minecraft:overworld run function mg:floaty/leave'), 1)
        self.assertEqual(leave, d.index('execute as @a[tag=mg.fnw] in minecraft:overworld run function mg:filon/leave') + 1)
        # vault_save lit mg.svid / mg.svvx : les joueurs partent AVANT la suppression de mg.st, mg.svid, mg.svvx et de l'état de la carte
        for gone in ('scoreboard objectives remove mg.svid', 'scoreboard objectives remove mg.svvx', 'scoreboard objectives remove mg.st'):
            self.assertLess(leave, d.index(gone), gone)
        self.assertLess(leave, d.index('function floaty:uninstall'))
        self.assertIn('execute in mg:floaty run forceload remove -9776 416 -9761 431', d)
        self.assertIn('tag @a remove mg.pullw', d)

    def test_sidebar_excludes_floaty(self):
        self.assertIn('tag=!mg.flw', '\n'.join(real('sb/auto')))

    def test_menu_button(self):
        d = json.loads((ROOT / 'data' / 'mg' / 'dialog' / 'main_menu.json').read_text(encoding='utf-8'))
        self.assertEqual([a['action'].get('command') for a in d['actions']].count('trigger mg.sv set 10'), 1)


if __name__ == '__main__':
    unittest.main()
