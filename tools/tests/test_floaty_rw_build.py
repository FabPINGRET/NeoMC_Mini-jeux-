"""tools/floaty : build_terrain avec réécriture (zip reproductible, VERSION 2, carte intacte, --no-rewrite = octets d'origine, build qui échoue sans
zip) et trampolines du terrain (terrain_sched.txt écrit par le build, lu par gen_floaty, trampoline généré, plus aucun manquant).
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v
"""
import contextlib
import hashlib
import io
import re
import sys
import unittest
import zipfile
from collections import Counter
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / 'tools' / 'floaty'))
import test_floaty_gen as TG  # noqa: E402  (FakeMap : carte de datapack + dépôt minimal)
import test_floaty_terrain as TT  # noqa: E402  (Base : carte de terrain ; mca, be, chunk_blocks)
import build_terrain as B  # noqa: E402
import fl_mca  # noqa: E402
import fl_nbt  # noqa: E402
import fl_rewrite  # noqa: E402
import fl_terrain as F  # noqa: E402
import gen_floaty as G  # noqa: E402

be, mca, chunk_blocks = TT.be, TT.mca, TT.chunk_blocks
ARC = 'region/r.2.0.mca'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()           # noqa: E731


def chunks(data):
    """Octets d'un .mca -> [(index, racine NBT relue)]."""
    return [(i, fl_nbt.loads(raw)) for i, raw in fl_mca.payloads(data, Counter())]


def zip_commands(path, arc):
    """Commandes des chunks de l'entrée `arc` du zip -> [(index, commande)] (chunks relus en entier)."""
    with zipfile.ZipFile(path) as zf:
        data = zf.read(arc)
    return [(i, f.command) for i, root in chunks(data) for f in F.blocks_of(root, arc)]


class Build(TT.Base):
    def build(self, out=None, **kw):
        return B.build(self.map, out or self.out, **{'pack_root': self.tmp / 'repo', **kw})          # réécriture par défaut

    def test_two_builds_identical_map_intact_and_version_2(self):
        before = TT.snapshot(self.map)
        a, b = self.build(self.tmp / 'a'), self.build(self.tmp / 'b')
        self.assertEqual((sha(a['zip']), a['sha']), (sha(b['zip']), b['sha']))
        self.assertEqual(a['report'].read_bytes(), b['report'].read_bytes())
        self.assertEqual(TT.snapshot(self.map), before)
        with zipfile.ZipFile(a['zip']) as zf:
            version = zf.read('VERSION').decode()
            self.assertEqual(zf.namelist()[-1], 'VERSION')
        self.assertTrue(version.startswith('neomc-floaty-terrain 2\n'))
        for line in ('command-rewrite: on', 'rewritten-commands: 4', f'source-sha256: {a["source_sha"]}'):
            self.assertIn(line, version)
        self.assertEqual(a['rewritten'], 4)                                       # gamerule + 2 tellraw/execute + minecart time

    def test_source_sha_is_the_sha_of_the_unrewritten_build(self):
        rw, plain = self.build(self.tmp / 'a'), self.build(self.tmp / 'b', rewrite=False)
        self.assertEqual(rw['source_sha'], plain['sha'])
        self.assertNotEqual(rw['sha'], plain['sha'])

    def test_no_rewrite_zip_is_the_source_and_version_1(self):
        r = self.build(rewrite=False)
        with zipfile.ZipFile(r['zip']) as zf:
            for arc, p in B.collect(self.dim):
                self.assertEqual(zf.read(arc), p.read_bytes(), arc)
            version = zf.read('VERSION').decode()
        self.assertTrue(version.startswith('neomc-floaty-terrain 1\n'))
        for absent in ('command-rewrite', 'source-sha256', 'rewritten-commands', 'rewritten-blocks'):
            self.assertNotIn(absent, version)
        self.assertEqual((r['after'], r['sched']), ([], []))
        self.assertFalse((self.tmp / 'repo' / B.SCHED_FILE).exists())               # --no-rewrite n'écrit rien hors --out

    def test_rewritten_zip_content_and_untouched_entries(self):
        r = self.build()
        self.assertEqual(sorted(c for _, c in zip_commands(r['zip'], ARC)), sorted([
            fl_rewrite.NOOP, 'tellraw @a[tag=mg.flw] {"text":"x"}', 'execute in mg:floaty as @a[tag=x,tag=mg.flw] run scoreboard players add @s mg.st 1']))
        with zipfile.ZipFile(r['zip']) as zf:
            self.assertEqual(zf.read('poi/r.2.0.mca'), (self.dim / 'poi' / 'r.2.0.mca').read_bytes())          # jamais réécrit
            self.assertEqual(zf.read('region/r.0.0.mca'), (self.dim / 'region' / 'r.0.0.mca').read_bytes())     # sans commande : copié tel quel
            cart = chunks(zf.read('entities/r.2.0.mca'))[0][1]
        self.assertEqual(cart['Entities'][0]['Command'], fl_rewrite.NOOP)
        self.assertEqual(r['files_rebuilt'], 2)

    def test_failed_verification_gives_no_zip_and_no_report(self):
        self.out.mkdir()
        (self.out / B.ZIP_NAME).write_bytes(b'zip d\'un build precedent')               # déjà là : ne doit pas survivre à un build qui échoue
        (self.out / B.REPORT_NAME).write_text('rapport d\'un build precedent', encoding='utf-8')
        with mock.patch.object(fl_mca, 'check', side_effect=fl_mca.VerifyError('boom')):
            with self.assertRaises(B.TerrainError) as cm:
                self.build()
        self.assertIn('ne se relit pas comme prevu', str(cm.exception))
        self.assertEqual(list(self.out.iterdir()), [])

    def test_successful_build_replaces_a_previous_zip(self):
        self.out.mkdir()
        (self.out / B.ZIP_NAME).write_bytes(b'ancien')
        r = self.build()
        self.assertTrue(zipfile.is_zipfile(r['zip']))                                  # inverse : un build qui réussit remplace l'ancien

    def test_ambiguous_dimension_removes_the_previous_zip_and_report(self):
        self.out.mkdir()
        (self.out / B.ZIP_NAME).write_bytes(b'zip d\'un build precedent')
        (self.out / B.REPORT_NAME).write_text('rapport d\'un build precedent', encoding='utf-8')
        other = self.map / 'dimensions' / 'mg' / 'autre' / 'region'
        other.mkdir(parents=True)
        (other / 'r.0.0.mca').write_bytes(mca([]))
        with self.assertRaises(B.TerrainError) as cm:
            self.build()
        self.assertIn('plusieurs dimensions', str(cm.exception))
        self.assertEqual(list(self.out.iterdir()), [])                                 # l'ancien zip ne survit pas à un build refusé
        self.assertTrue(zipfile.is_zipfile(self.build(dimension='minecraft:overworld')['zip']))      # inverse : la dimension choisie, le build passe

    def test_refused_out_keeps_whatever_is_there(self):
        inside = self.map / 'out'
        inside.mkdir()
        (inside / B.ZIP_NAME).write_bytes(b'pas a nous')
        with self.assertRaises(B.TerrainError):
            self.build(inside)
        self.assertEqual((inside / B.ZIP_NAME).read_bytes(), b'pas a nous')            # inverse : un --out refusé n'est jamais nettoyé

    def test_failed_sched_write_leaves_no_zip(self):
        with mock.patch.object(B, 'write_sched', side_effect=OSError('disque plein')):
            with self.assertRaises(OSError):
                self.build()
        self.assertEqual(list(self.out.iterdir()), [])                                 # pas de zip sans la liste de trampolines qui va avec

    def test_source_dimension_is_rewritten_and_another_one_is_a_noop(self):
        d = self.map / 'DIM-1' / 'region'
        d.mkdir(parents=True)
        cmds = [be('command_block', 1, 70, 9, 'execute in minecraft:the_nether run say hi'),
                be('command_block', 2, 70, 9, 'execute in minecraft:overworld run say hi'),
                be('command_block', 3, 70, 9, 'execute in minecraft:the_nether run kill @e[type=item]')]
        (d / 'r.0.0.mca').write_bytes(mca([(0, chunk_blocks(cmds), 2)]))
        r = self.build(dimension='minecraft:the_nether')
        self.assertEqual([c for _, c in zip_commands(r['zip'], 'region/r.0.0.mca')], [
            'execute in mg:floaty run tellraw @a[tag=mg.flw] "hi"', fl_rewrite.NOOP, 'execute in mg:floaty run kill @e[type=item,distance=0..]'])
        self.assertEqual([c.reason for c in r['after'] if c.action == 'noop'], ['risque_dur'])      # l'overworld est ici une AUTRE dimension
        r = self.build(dimension='minecraft:overworld')                                # inverse : la source est l'overworld, le nether n'y est pas lu
        self.assertEqual([c for _, c in zip_commands(r['zip'], ARC)].count(fl_rewrite.NOOP), 1)       # seul le gamerule du Base est un NOOP

    def test_unreadable_chunk_with_a_command_is_reported_and_does_not_fail_the_build(self):
        bad = chunk_blocks([be('command_block', 1, 70, 9, 'say \U0001F600')])          # UTF-8 sur 4 octets : le lecteur strict le refuse
        (self.dim / 'region' / 'r.3.0.mca').write_bytes(mca([(0, bad, 2)]))
        seen = []
        r = self.build(progress=seen.append)
        self.assertEqual(r['unread_cmd'], [('region/r.3.0.mca', 96, 0)])
        self.assertTrue(any(m.startswith('(!) 1 chunk(s)') and 'illisible_cmd' in m for m in seen), seen)       # avertissement sur stderr
        report = r['report'].read_text(encoding='utf-8')
        self.assertIn('## illisible_cmd : 1 chunk(s)', report)
        self.assertIn('  region/r.3.0.mca chunk (96, 0)', report)
        with zipfile.ZipFile(r['zip']) as zf:
            self.assertEqual(zf.read('region/r.3.0.mca'), (self.dim / 'region' / 'r.3.0.mca').read_bytes())      # recopié tel quel
        seen.clear()
        (self.dim / 'region' / 'r.3.0.mca').unlink()                                   # inverse : carte lisible : ni avertissement ni section
        r = self.build(progress=seen.append)
        self.assertEqual((r['unread_cmd'], [m for m in seen if 'illisible_cmd' in m]), ([], []))
        self.assertNotIn('illisible_cmd', r['report'].read_text(encoding='utf-8'))
        plain = self.build(self.tmp / 'n', rewrite=False)                              # inverse : sans réécriture, rien n'est lu ni signalé
        self.assertNotIn('illisible_cmd', plain['report'].read_text(encoding='utf-8'))

    def test_noop_eclate_is_counted_and_listed_in_the_report(self):
        cmds = [be('command_block', 1, 70, 9, 'advancement revoke @s everything'), be('command_block', 2, 70, 9, 'tellraw @a "advancement grant x everything"')]
        (self.dim / 'region' / 'r.3.0.mca').write_bytes(mca([(0, chunk_blocks(cmds), 2)]))
        report = self.build()['report'].read_text(encoding='utf-8')
        self.assertIn('- NOOP (eclate) : 1', report)
        self.assertIn('- eclate : 1', report)                                          # « Non reecrits » : le compte par raison
        self.assertRegex(report, r'(?m)^eclate\t1 70 9\t.*\tadvancement revoke @s everything$')
        self.assertNotRegex(report, r'(?m)^eclate\t2 70 9\t')                          # inverse : le texte d'un tellraw n'est pas un `everything`

    def test_root_must_be_a_neomc_repo_outside_the_map_and_out(self):
        bad_marker = self.tmp / 'vide'
        bad_marker.mkdir()
        inside_map, inside_out = self.map / 'repo', self.out / 'repo'
        for repo in (inside_map, inside_out):                                           # un vrai dépôt (marqueur présent) mais au mauvais endroit
            (repo / 'data' / 'mg' / 'function' / 'core').mkdir(parents=True)
            (repo / 'data' / 'mg' / 'function' / 'core' / 'load.mcfunction').write_text('x', encoding='utf-8')
        for root in (bad_marker, inside_map, inside_out, self.tmp / 'nexistepas'):
            with self.subTest(root.name):
                with self.assertRaises(B.TerrainError) as cm:
                    B.build(self.map, self.out, pack_root=root)
                self.assertIn('--root', str(cm.exception))
        self.assertFalse((bad_marker / B.SCHED_FILE).exists())                          # rien d'écrit dans une racine refusée
        self.assertEqual(sorted(p.name for p in self.out.iterdir()), ['repo'])          # ni zip ni rapport (seul le faux dépôt de ce test)

    def test_root_is_not_checked_without_rewrite(self):
        self.assertTrue(zipfile.is_zipfile(B.build(self.map, self.out, rewrite=False, pack_root=self.tmp / 'nexistepas')['zip']))

    def test_main_prints_rewrite_line_and_takes_no_rewrite_option(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            self.assertEqual(B.main(['--map', str(self.map), '--out', str(self.out), '--root', str(self.tmp / 'repo')]), 0)
            on = out.getvalue()
            self.assertEqual(B.main(['--map', str(self.map), '--out', str(self.tmp / 'n'), '--root', str(self.tmp / 'repo'), '--no-rewrite']), 0)
        self.assertRegex(on, r'reecriture : 4 commandes modifiees, 2 fichiers reconstruits, 0 cibles schedule')
        self.assertNotIn('reecriture :', out.getvalue()[len(on):])
        self.assertRegex(err.getvalue(), r'build : \d+\.\d s')


class Pipeline(TT.Base):
    """gen_floaty lit terrain_sched.txt (écrit par le build) et génère les trampolines des cibles des commandes du terrain."""

    def setUp(self):
        super().setUp()
        TG.isolate_fr(self, self.tmp / 'frdir')
        for rel, txt in TG.FakeMap.FILES.items():
            TG.FakeMap.put(self.map / G.PACK / rel, txt)
        for name in TG.FakeMap.BIOMES:
            TG.FakeMap.put(self.map / G.BIOMES / name, '{}')
        self.repo = self.tmp / 'repo'
        TG.FakeMap.put(self.repo / 'data/mg/function/keep.mcfunction', 'say mg')
        TG.FakeMap.put(self.repo / TG.DESINSTALLER, 'say d\nfunction mg:elyrace/uninstall\n')
        TG.FakeMap.put(self.repo / 'data/minecraft/tags/dialog/quick_actions.json', '{"values":["mine"]}')
        cmds = [be('command_block', 1, 70, 9, 'schedule function boss:b 10t'), be('command_block', 2, 70, 9, 'schedule function zone:gone 5t'),
                be('command_block', 3, 70, 9, 'schedule function boss:b 20t')]
        (self.dim / 'region' / 'r.2.0.mca').write_bytes(mca([(0, chunk_blocks(cmds), 2)]))

    def build(self):
        return B.build(self.map, self.out, pack_root=self.repo)

    def test_targets_are_written_sorted_versioned_and_reported(self):
        r = self.build()
        text = (self.repo / B.SCHED_FILE).read_text(encoding='ascii')
        self.assertEqual(text.splitlines()[1:], ['boss:b', 'zone:gone'])           # triées, sans doublon
        self.assertTrue(text.startswith('#') and text.endswith('\n') and '\r' not in text)
        self.assertEqual(G.terrain_targets(self.repo), ['boss:b', 'zone:gone'])
        self.assertEqual(r['sched_missing'], ['boss:b', 'zone:gone'])
        report = r['report'].read_text(encoding='utf-8')
        self.assertIn('cibles schedule distinctes : 2 ; sans trampoline dans le depot : 2', report)
        self.assertIn('  sans trampoline : zone:gone', report)
        stamp = (self.repo / B.SCHED_FILE).stat().st_mtime_ns
        self.build()
        self.assertEqual((self.repo / B.SCHED_FILE).stat().st_mtime_ns, stamp)    # fichier à jour : pas réécrit

    def test_gen_floaty_generates_the_terrain_trampolines_and_nothing_is_missing(self):
        self.build()
        st, n, spawn, roots, missing = G.generate(self.map, self.repo)
        tramp = self.repo / 'data' / 'floaty' / 'function' / 'sched'
        for target in ('boss/b', 'zone/gone'):
            self.assertTrue((tramp / (target + '.mcfunction')).is_file(), target)
        self.assertTrue({'boss:b', 'zone:gone'} <= st.sched)
        self.assertEqual(missing, ['zone:gone'])                                   # la fonction n'existe pas dans la carte : signalé, pas caché
        text = (tramp / 'zone' / 'gone.mcfunction').read_text(encoding='utf-8')
        self.assertIn('function zone:gone', text)
        again = self.build()
        self.assertEqual(again['sched_missing'], [])
        self.assertIn('toutes ont leur trampoline dans le depot', again['report'].read_text(encoding='utf-8'))

    def test_without_the_list_gen_floaty_only_has_the_map_targets(self):
        st, *_ = G.generate(self.map, self.repo)
        self.assertEqual(st.sched, {'boss:b'})                                     # la carte n'en planifie qu'un
        self.assertEqual(G.terrain_targets(self.repo), [])
        self.assertFalse((self.repo / 'data' / 'floaty' / 'function' / 'sched' / 'zone').exists())

    def test_terrain_targets_refuses_dot_dot_and_empty_segments(self):
        for bad in ('a:../b', 'a:b//c', 'a:b/', 'nocolon', '..:x', 'A:b'):
            with self.subTest(bad):
                TG.FakeMap.put(self.repo / G.TERRAIN_SCHED, f'good:one\n{bad}\n')
                with self.assertRaises(SystemExit) as cm:
                    G.terrain_targets(self.repo)
                self.assertIn(bad, str(cm.exception))
        TG.FakeMap.put(self.repo / G.TERRAIN_SCHED, 'good:one\na.b:c.d/e-f_1\n')
        self.assertEqual(G.terrain_targets(self.repo), ['a.b:c.d/e-f_1', 'good:one'])          # inverse : ids valides acceptés

    def test_terrain_targets_ignores_comments_and_blank_lines(self):
        TG.FakeMap.put(self.repo / G.TERRAIN_SCHED, '# commentaire\n\nb:z\n  a:y  \n#a:x\n')
        self.assertEqual(G.terrain_targets(self.repo), ['a:y', 'b:z'])
        self.assertEqual(re.sub(r'\s', '', G.TERRAIN_SCHED.as_posix()), 'tools/floaty/terrain_sched.txt')
        self.assertEqual(B.SCHED_FILE, G.TERRAIN_SCHED)                            # les deux scripts parlent du même fichier


if __name__ == '__main__':
    unittest.main()
