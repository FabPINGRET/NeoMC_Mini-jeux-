"""tools/floaty : cas limites relevés en revue (aller-retour de Command:, --adopt et git, manifeste hostile, clés SNBT entre guillemets,
filtre auteur, LastOutput). Fausse carte en dossier temporaire uniquement : aucun clean n'est lancé sur le vrai dépôt.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'floaty'))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import fl_owned as O  # noqa: E402
import fl_rewrite as R  # noqa: E402
import gen_floaty as G  # noqa: E402
from test_floaty_gen import DESINSTALLER, MANIFEST, NEEDS_GIT, git_init, isolate_fr, nbt_bytes, snapshot  # noqa: E402

ROOTS = ['main_quest:root']


def rw(line):
    return R.rewrite_line(line, ROOTS)


class CommandEscapes(unittest.TestCase):
    def test_roundtrip_double_quotes_backslash_unchanged(self):
        line = r'setblock ~ ~ ~ chest{Command:"scoreboard players set a\\b v 0",auto:1b}'
        self.assertEqual(rw(line), [line])

    def test_roundtrip_single_quotes_escaped_quote_unchanged(self):
        line = r"setblock ~ ~ ~ chest{Command:'tag @s add it\'s',auto:1b}"
        self.assertEqual(rw(line), [line])

    def test_roundtrip_escaped_double_quote_unchanged(self):
        line = r'setblock ~ ~ ~ chest{Command:"tag @s add \"x\" \\ y"}'
        self.assertEqual(rw(line), [line])

    def test_rewritten_keeps_backslash_escape(self):
        self.assertEqual(rw(r'setblock ~ ~ ~ chest{Command:"give @a stick \\ x",auto:1b}'),
                         [r'setblock ~ ~ ~ chest{Command:"give @a[tag=mg.flw] stick \\ x",auto:1b}'])
        self.assertEqual(rw(r"setblock ~ ~ ~ chest{Command:'give @a stick \\ it\'s'}"),
                         [r"setblock ~ ~ ~ chest{Command:'give @a[tag=mg.flw] stick \\ it\'s'}"])

    def test_quoted_snbt_key_is_rewritten(self):
        self.assertEqual(rw('setblock ~ ~ ~ chest{"Command":"tag @a add x"}'),
                         ['setblock ~ ~ ~ chest{"Command":"tag @a[tag=mg.flw] add x"}'])
        self.assertEqual(rw("setblock ~ ~ ~ chest{'Command':'tag @a add x'}"),
                         ["setblock ~ ~ ~ chest{'Command':'tag @a[tag=mg.flw] add x'}"])

    def test_author_in_data_string_keeps_command(self):
        out = rw("data merge block ~ ~ ~ {LastOutput:'[\"LordDrewpicus joined\"]'}")
        self.assertEqual(out, ['data merge block ~ ~ ~ {}'])

    def test_author_inside_string_kept_outside_dropped(self):
        self.assertEqual(rw('tellraw @a {"text":"LordDrewpicus"}'), ['tellraw @a[tag=mg.flw] {"text":"LordDrewpicus"}'])
        self.assertEqual(rw('execute as LordDrewpicus run say hi'), [])
        self.assertEqual(rw('tellraw LordDrewpicus {"text":"x"}'), [])

    def test_last_output_removed_in_every_position(self):
        for src, want in (("{Command:\"x\",LastOutput:'a',auto:1b}", '{Command:"x",auto:1b}'),
                          ("{LastOutput:'a',auto:1b}", '{auto:1b}'),
                          ('{auto:1b,LastOutput:"a \\"q\\" b"}', '{auto:1b}'),
                          ("{\"LastOutput\":'a'}", '{}'),
                          ("{auto:1b,LastOutput:'a',x:1b,LastOutput:'b'}", '{auto:1b,x:1b}')):
            self.assertEqual(rw('data merge block ~ ~ ~ ' + src), ['data merge block ~ ~ ~ ' + want], src)

    def test_unclosed_last_output_left_alone(self):
        line = "data merge block ~ ~ ~ {LastOutput:'a"
        self.assertEqual(rw(line), [line])


class AdoptAndManifest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        self.map, self.repo = self.tmp / 'map', self.tmp / 'outer' / 'repo'
        isolate_fr(self, self.tmp / 'frdir')
        self.put(self.map / G.PACK / 'boss/function/a.mcfunction', 'say a\n')
        self.put(self.map / G.PACK / 'minecraft/function/tick.mcfunction', 'say t\n')
        self.put(self.map / G.PACK / 'minecraft/function/load.mcfunction', 'say l\n')
        self.put(self.map / G.BIOMES / 'virion.json', '{}')
        (self.map / 'level.dat').write_bytes(nbt_bytes())
        self.put(self.repo / 'data/mg/function/keep.mcfunction', 'say mg')
        self.put(self.repo / DESINSTALLER, 'say d\nfunction mg:elyrace/uninstall\n')
        self.sentinel = self.tmp / 'outer' / 'sentinel.txt'     # voisin de repo : doit survivre à tout
        self.put(self.sentinel, 'keep')

    @staticmethod
    def put(p, txt):
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(txt, encoding='utf-8', newline='\n')

    def tree(self):
        return snapshot(self.tmp)

    def manifest_lines(self):
        return (self.repo / MANIFEST).read_text(encoding='utf-8').split('\n')[:-1]

    def refused(self, **kw):
        before = self.tree()
        with self.assertRaises(SystemExit):
            G.generate(self.map, self.repo, **kw)
        self.assertEqual(self.tree(), before)

    def track(self, *paths):
        git_init(self.repo)
        subprocess.run(['git', 'add', '-f', '--'] + list(paths), cwd=self.repo, check=True)

    @NEEDS_GIT
    def test_adopt_preexisting_minecraft_file(self):
        biome = 'data/minecraft/worldgen/biome/virion.json'
        git_init(self.repo)
        self.put(self.repo / biome, '{"old":1}')
        self.refused()                                           # sans --adopt : refusé
        G.generate(self.map, self.repo, adopt=True)
        self.assertEqual((self.repo / biome).read_text(encoding='utf-8'), '{}')
        self.assertIn(biome, self.manifest_lines())
        G.generate(self.map, self.repo)                          # adopté : la relance passe sans --adopt
        self.assertTrue((self.repo / biome).exists())

    def test_adopt_refuses_protected_namespace_from_map(self):
        self.put(self.map / G.PACK / 'mg/function/x.mcfunction', 'say x')
        self.refused(adopt=True)
        self.assertTrue((self.repo / 'data/mg/function/keep.mcfunction').exists())

    def test_adopt_refuses_protected_namespace_in_manifest(self):
        for ns in ('mg', 'minecraft', 'floaty'):
            self.put(self.repo / MANIFEST, f'data/{ns}/\n')
            self.refused(adopt=True)
        self.assertEqual((self.repo / 'data/mg/function/keep.mcfunction').read_text(encoding='utf-8'), 'say mg')

    def test_adopt_does_not_adopt_data_mg(self):
        G.generate(self.map, self.repo, adopt=True)
        self.assertNotIn('data/mg/', self.manifest_lines())
        self.assertTrue((self.repo / 'data/mg/function/keep.mcfunction').exists())

    # B1 : load() acceptait `data/../` et `data/./` (le motif d'id autorise les points) ; clean() aurait fait rmtree de la racine du dépôt
    # ou de data/. Ici repo = tmp/outer/repo : tout est jetable, le voisin sentinel est vérifié.
    def test_manifest_dotdot_dir_refused_before_deletion(self):
        self.put(self.repo / MANIFEST, 'data/../\n')
        self.refused()
        self.assertTrue(self.sentinel.exists())

    def test_manifest_dot_dir_refused_before_deletion(self):
        self.put(self.repo / MANIFEST, 'data/./\n')
        self.refused()
        self.assertTrue((self.repo / 'data/mg/function/keep.mcfunction').exists())

    def test_check_refuses_namespace_that_resolves_outside_data(self):
        for ns in ('..', '.', 'a/../..', '.hidden'):
            with self.assertRaises(SystemExit, msg=ns):
                O.check(self.repo, [ns], [])
        self.assertTrue(self.sentinel.exists())

    # Windows retire le point / l'espace final : « mg. » désignerait « mg » une fois résolu, et clean() viderait data/mg
    def test_trailing_dot_namespace_refused_in_manifest_and_check(self):
        for ns in ('mg.', 'minecraft.', 'floaty.', 'boss.', 'boss '):
            with self.subTest(ns):
                self.put(self.repo / MANIFEST, f'data/{ns}/\n')
                self.refused()
                with self.assertRaises(SystemExit):
                    O.check(self.repo, [ns], [])
        self.assertTrue((self.repo / 'data/mg/function/keep.mcfunction').exists())

    def test_minecraft_manifest_lines_must_be_json_files(self):
        for line in ('data/minecraft/x.json.', 'data/minecraft/', 'data/minecraft/tags'):
            with self.subTest(line):
                self.put(self.repo / MANIFEST, line + '\n')
                self.refused()

    def test_check_refuses_minecraft_paths_that_do_not_resolve_to_themselves(self):
        for rel in ('data/minecraft/../mg/x.json', 'data/minecraft/a/../../mg/x.json', 'data/mg/x.json'):
            with self.subTest(rel):
                with self.assertRaises(SystemExit):
                    O.check(self.repo, [], [rel])
        self.assertTrue(self.sentinel.exists())

    def test_clean_does_not_swallow_deletion_errors(self):
        self.put(self.repo / 'data/boss/function/old.mcfunction', 'say old')
        with mock.patch.object(O.shutil, 'rmtree', side_effect=PermissionError('verrouillé')):
            with self.assertRaises(PermissionError):
                O.clean(self.repo, ['boss'], [])
        O.clean(self.repo, ['absent'], [])                       # un dossier absent n'est pas une erreur

    # B2 : --adopt consulte git ; un chemin suivi est refusé avant toute suppression
    @NEEDS_GIT
    def test_adopt_refuses_tracked_namespace(self):
        self.put(self.repo / 'data/boss/function/mine.mcfunction', 'say versionné')
        self.track('data/boss/function/mine.mcfunction')
        self.refused(adopt=True)
        self.assertTrue((self.repo / 'data/boss/function/mine.mcfunction').exists())
        self.assertFalse((self.repo / MANIFEST).exists())

    @NEEDS_GIT
    def test_adopt_refuses_tracked_minecraft_file(self):
        biome = 'data/minecraft/worldgen/biome/virion.json'
        self.put(self.repo / biome, '{"old":1}')
        self.track(biome)
        self.refused(adopt=True)
        self.assertEqual((self.repo / biome).read_text(encoding='utf-8'), '{"old":1}')

    @NEEDS_GIT
    def test_adopt_untracked_namespace_passes_in_git_repo(self):
        git_init(self.repo)
        self.put(self.repo / 'data/boss/function/old.mcfunction', 'say old')
        G.generate(self.map, self.repo, adopt=True)
        self.assertFalse((self.repo / 'data/boss/function/old.mcfunction').exists())
        self.assertTrue((self.repo / 'data/boss/function/a.mcfunction').exists())

    @NEEDS_GIT
    def test_adopt_outside_a_git_repo_refused(self):
        self.put(self.repo / 'data/boss/function/old.mcfunction', 'say old')
        with mock.patch.dict(os.environ, {'GIT_CEILING_DIRECTORIES': str(self.tmp)}):      # git ne remonte pas au-dessus du dossier temporaire
            self.refused(adopt=True)
        self.assertTrue((self.repo / 'data/boss/function/old.mcfunction').exists())

    def test_adopt_without_git_refused(self):
        self.put(self.repo / 'data/boss/function/old.mcfunction', 'say old')
        with mock.patch.object(O.subprocess, 'run', side_effect=FileNotFoundError('git')):
            self.refused(adopt=True)
        self.assertTrue((self.repo / 'data/boss/function/old.mcfunction').exists())

    def test_adopt_with_nothing_to_adopt_does_not_call_git(self):
        with mock.patch.object(O.subprocess, 'run', side_effect=FileNotFoundError('git')) as run:
            G.generate(self.map, self.repo, adopt=True)
        run.assert_not_called()


if __name__ == '__main__':
    unittest.main()
