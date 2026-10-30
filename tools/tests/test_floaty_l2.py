"""tools/floaty, lot L2 : install / uninstall, mg:desinstaller, dimension mg:floaty, condition de dimension des advancements, périmètre des
fichiers possédés dans data/floaty, espaces de noms invalides, et « lire avant de supprimer » (une carte incomplète ou illisible ne touche à rien).
Fausse carte en dossier temporaire (voir FakeMap de test_floaty_gen.py).
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'floaty'))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen_floaty as G  # noqa: E402
import test_floaty_gen as TG  # noqa: E402  (module, pas FakeMap seul : unittest rejouerait ses tests ici)
DESINSTALLER = TG.DESINSTALLER
from test_floaty_state import BARS, BOARD, dat, event  # noqa: E402
from test_floaty_state import Comp, Lst  # noqa: E402

EVENTS = {'data': Comp({'events': Lst(10, [event('boss:b', 40), event('boss:zzz', 50)])})}    # boss:b est planifiée par boss:a ; boss:zzz non
COND = {'condition': 'minecraft:entity_properties', 'entity': 'this', 'predicate': {'minecraft:location': {'dimension': 'mg:floaty'}}}
FN = 'data/floaty/function/'


class OnlyInDimension(unittest.TestCase):
    def test_impossible_untouched_other_triggers_restricted(self):
        adv = {'criteria': {'cmd': {'trigger': 'minecraft:impossible'}, 'bare': {'trigger': 'impossible'},
                            'kill': {'trigger': 'minecraft:player_killed_entity', 'conditions': {'entity': []}},
                            'tick': {'trigger': 'minecraft:tick'}, 'none': {}}}
        self.assertEqual(G.only_in_dimension(adv), 2)
        c = adv['criteria']
        self.assertEqual(c['cmd'], {'trigger': 'minecraft:impossible'})
        self.assertEqual(c['bare'], {'trigger': 'impossible'})
        self.assertEqual(c['kill']['conditions'], {'entity': [], 'player': [COND]})
        self.assertEqual(c['tick']['conditions'], {'player': [COND]})
        self.assertEqual(c['none'], {})

    def test_existing_player_conditions_kept_and_idempotent(self):
        other = {'condition': 'minecraft:random_chance', 'chance': 0.5}
        adv = {'criteria': {'a': {'trigger': 'minecraft:tick', 'conditions': {'player': [other]}},
                            'b': {'trigger': 'minecraft:tick', 'conditions': {'player': other}}}}
        self.assertEqual(G.only_in_dimension(adv), 2)
        self.assertEqual(adv['criteria']['a']['conditions']['player'], [other, COND])
        self.assertEqual(adv['criteria']['b']['conditions']['player'], [other, COND])
        self.assertEqual(G.only_in_dimension(adv), 0)
        self.assertEqual(adv['criteria']['a']['conditions']['player'], [other, COND])

    def test_condition_matches_vanilla_26_2_format(self):
        """Même forme que data/minecraft/advancement/nether/ride_strider_in_overworld_lava.json du serveur 26.2 (clés namespacées)."""
        self.assertEqual(list(G.IN_DIMENSION), ['condition', 'entity', 'predicate'])
        self.assertEqual(G.IN_DIMENSION['predicate'], {'minecraft:location': {'dimension': 'mg:floaty'}})


class Generated(unittest.TestCase):
    """Même fausse carte que FakeMap (ses fixtures et ses aides, sans ses tests), plus scoreboard.dat et custom_boss_events.dat."""
    FILES, BIOMES = TG.FakeMap.FILES, TG.FakeMap.BIOMES
    put = staticmethod(TG.FakeMap.put)
    tree, manifest, refused = TG.FakeMap.tree, TG.FakeMap.manifest, TG.FakeMap.refused

    def setUp(self):
        TG.FakeMap.setUp(self)
        (self.map / 'data' / 'minecraft').mkdir(parents=True)
        (self.map / 'data' / 'minecraft' / 'scoreboard.dat').write_bytes(dat(BOARD))
        (self.map / 'data' / 'minecraft' / 'custom_boss_events.dat').write_bytes(dat(BARS))

    def read(self, rel):
        return (self.repo / rel).read_text(encoding='utf-8')

    def untouched(self):
        """generate échoue (SystemExit ou lecture impossible) sans rien supprimer ni écrire."""
        before = self.tree()
        with self.assertRaises((Exception, SystemExit)):
            G.generate(self.map, self.repo)
        self.assertEqual(self.tree(), before)

    # --- install / uninstall / desinstaller / dimension
    def test_install_uninstall_files(self):
        st, n, *_ = G.generate(self.map, self.repo)
        install, uninstall = self.read(FN + 'install.mcfunction'), self.read(FN + 'uninstall.mcfunction')
        self.assertIn('execute if data storage mg:floaty installed run return 0\n', install)
        self.assertIn('scoreboard players set #fake Value 5\n', install)
        self.assertNotIn('Alice', install)
        self.assertIn('execute unless data storage mg:floaty installed run return 0\n', uninstall)
        self.assertIn('scoreboard objectives remove Kills\n', uninstall)
        self.assertIn('bossbar remove boss:a\n', uninstall)
        self.assertEqual({k: n['state'][k] for k in ('objectives', 'teams', 'scores', 'bossbars')}, {'objectives': 3, 'teams': 1, 'scores': 4, 'bossbars': 1})

    def test_pending_schedules_use_the_generated_trampolines(self):
        (self.map / 'data' / 'minecraft' / 'scheduled_events.dat').write_bytes(dat(EVENTS))
        st, n, *_ = G.generate(self.map, self.repo)
        self.assertIn('schedule function floaty:sched/boss/b 1t replace\n', self.read(FN + 'install.mcfunction'))     # level.dat sans Time : 1 tick
        self.assertIn('schedule clear floaty:sched/boss/b\n', self.read(FN + 'uninstall.mcfunction'))
        self.assertTrue((self.repo / (FN + 'sched/boss/b.mcfunction')).exists())
        self.assertEqual(n['sched_missing'], ['boss:zzz'])
        self.assertEqual((n['state']['sched_events'], n['state']['sched_installed']), (2, 1))

    def test_desinstaller_calls_uninstall_once(self):
        G.generate(self.map, self.repo)
        want = 'say d\nfunction mg:elyrace/uninstall\nfunction floaty:uninstall\n'
        self.assertEqual(self.read(DESINSTALLER), want)
        G.generate(self.map, self.repo)
        self.assertEqual(self.read(DESINSTALLER), want)

    def test_dimension_json_is_flat_void_like_ombrelune(self):
        G.generate(self.map, self.repo)
        text = self.read('data/mg/dimension/floaty.json')
        self.assertEqual(text, json.dumps(G.DIMENSION, indent=2) + '\n')
        self.assertNotIn('\r', text)
        ombre = ROOT / 'data' / 'mg' / 'dimension' / 'ombrelune.json'
        if ombre.exists():
            self.assertEqual(json.loads(text), json.loads(ombre.read_text(encoding='utf-8')))

    def test_advancement_criteria_restricted_to_dimension(self):
        self.put(self.map / G.PACK / 'main_quest/advancement/q3.json', json.dumps({'parent': 'main_quest:root', 'criteria': {
            'cmd': {'trigger': 'minecraft:impossible'}, 'kill': {'trigger': 'minecraft:player_killed_entity'},
            'eat': {'trigger': 'minecraft:consume_item', 'conditions': {'item': {}}}}}))
        st, *_ = G.generate(self.map, self.repo)
        self.assertEqual((st.criteria, st.criteria_total), (2, 3))
        c = json.loads(self.read('data/main_quest/advancement/q3.json'))['criteria']
        self.assertEqual(c['cmd'], {'trigger': 'minecraft:impossible'})
        self.assertEqual(c['kill']['conditions']['player'], [COND])
        self.assertEqual(c['eat']['conditions'], {'item': {}, 'player': [COND]})

    # --- périmètre de data/floaty
    def test_only_generated_parts_of_floaty_are_owned(self):
        self.put(self.repo / (FN + 'tick.mcfunction'), 'say à moi (L3)')
        self.put(self.repo / (FN + 'l3/setup.mcfunction'), 'say l3')
        self.put(self.repo / 'data/floaty/tags/function/x.json', '{"values":[]}')
        self.put(self.repo / (FN + 'map/stale.mcfunction'), 'say périmé')
        self.put(self.repo / (FN + 'sched/stale/x.mcfunction'), 'say périmé')
        G.generate(self.map, self.repo)
        for rel in ('tick.mcfunction', 'l3/setup.mcfunction'):
            self.assertTrue((self.repo / FN / rel).exists(), rel)
        self.assertTrue((self.repo / 'data/floaty/tags/function/x.json').exists())
        self.assertEqual(self.read(FN + 'tick.mcfunction'), 'say à moi (L3)')
        self.assertFalse((self.repo / (FN + 'map/stale.mcfunction')).exists())
        self.assertFalse((self.repo / (FN + 'sched/stale')).exists())
        self.assertTrue((self.repo / (FN + 'map/tick.mcfunction')).exists())
        self.assertTrue((self.repo / (FN + 'install.mcfunction')).exists())

    # --- espaces de noms invalides (B6)
    def test_invalid_namespace_folders_are_dropped(self):
        for ns in ('.hidden', 'Bad', 'with space'):
            self.put(self.map / G.PACK / ns / 'function/x.mcfunction', 'say x')
        invalid = []
        got = {ns for ns, _, _ in G.collect(self.map / G.PACK, None, invalid)}
        self.assertFalse(got & {'.hidden', 'Bad', 'with space'})
        self.assertTrue({'.hidden/', 'Bad/', 'with space/'} <= set(invalid))
        G.generate(self.map, self.repo)
        self.assertEqual({p.name for p in (self.repo / 'data').iterdir()} & {'.hidden', 'Bad', 'with space'}, set())

    # --- lire avant de supprimer (B7)
    def test_missing_tick_and_load_give_empty_functions(self):
        G.generate(self.map, self.repo)
        for f in ('tick', 'load'):
            (self.map / G.PACK / f'minecraft/function/{f}.mcfunction').unlink()
        G.generate(self.map, self.repo)
        for f in ('tick', 'load'):
            lines = self.read(f'{FN}map/{f}.mcfunction').split('\n')
            self.assertEqual(len(lines), 3)                                           # en-tête, remarque, fin de fichier
            self.assertIn('absent de la carte', lines[1])
        self.assertTrue((self.repo / 'data/boss/function/a.mcfunction').exists())     # le reste de la sortie est intact


    def test_incomplete_or_unreadable_map_touches_nothing(self):
        cases = {
            'level.dat absent': lambda: (self.map / 'level.dat').unlink(),
            'level.dat illisible': lambda: (self.map / 'level.dat').write_bytes(b'x'),
            'scoreboard.dat illisible': lambda: (self.map / 'data/minecraft/scoreboard.dat').write_bytes(b'pas du nbt'),
            'advancement JSON invalide': lambda: self.put(self.map / G.PACK / 'main_quest/advancement/q1.json', '{ pas du json'),
            'mcfunction non UTF-8': lambda: (self.map / G.PACK / 'boss/function/a.mcfunction').write_bytes(b'say \xff\xfe\x80'),
            'desinstaller absent': lambda: (self.repo / DESINSTALLER).unlink(),
            'desinstaller sans ancre': lambda: self.put(self.repo / DESINSTALLER, 'say d\n'),
        }
        for label, sabotage in cases.items():
            with self.subTest(label):
                self.setUp()                                      # carte et dépôt neufs pour chaque cas
                G.generate(self.map, self.repo)                   # une sortie complète existe déjà : c'est elle qui ne doit pas bouger
                sabotage()
                self.untouched()


class RealRepoCollisions(unittest.TestCase):
    """Le dépôt généré (si présent) : install ne crée aucun objectif / équipe / bossbar que le reste du pack crée aussi. Sinon uninstall,
    appelé par mg:desinstaller, supprimerait celui du pack (data/mg en tête). Les espaces de noms de la carte sont ceux du manifeste."""
    ADD = re.compile(r'^\s*\$?(?:execute .*? run )?(scoreboard objectives add|team add|bossbar add) (\S+)', re.M)

    def test_install_creates_nothing_the_rest_of_the_pack_creates(self):
        install = ROOT / 'data' / 'floaty' / 'function' / 'install.mcfunction'
        manifest = ROOT / 'tools' / 'floaty' / 'owned.txt'
        if not install.exists():
            self.skipTest('sortie de gen_floaty absente')
        self.assertTrue(manifest.exists(), 'install.mcfunction est là mais tools/floaty/owned.txt manque : on ne sait pas quels dossiers sont ceux de la carte')
        ours = set(self.ADD.findall(install.read_text(encoding='utf-8')))
        self.assertTrue(ours)
        owned = {l.strip().split('/')[1] for l in manifest.read_text(encoding='utf-8').split('\n') if l.strip().endswith('/')}
        clash = []
        for ns in sorted(p.name for p in (ROOT / 'data').iterdir() if p.is_dir() and p.name not in owned):
            for f in sorted((ROOT / 'data' / ns).rglob('*.mcfunction')):
                if f == install:
                    continue
                clash += [f'{f.relative_to(ROOT).as_posix()} : {k} {v}' for k, v in set(self.ADD.findall(f.read_text(encoding='utf-8'))) & ours]
        self.assertEqual(clash, [])


if __name__ == '__main__':
    unittest.main()
