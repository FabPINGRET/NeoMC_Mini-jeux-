"""tools/floaty : build_terrain.py (zip du terrain + rapport des blocs de commande), sur une fausse carte construite ici (fichiers .mca
synthétiques : en-tête + chunks zlib, NBT encodé par les aides de test_floaty_state) — la vraie carte n'est pas nécessaire (la CI ne
l'a pas). Lecture des chunks (non lus / à vérifier) : test_floaty_chunks ; panneaux : test_floaty_signs ; risques : test_floaty_classify.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v
"""
import contextlib
import hashlib
import io
import struct
import sys
import tempfile
import unittest
import zipfile
import zlib
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / 'tools' / 'floaty'))
import test_floaty_state as T  # noqa: E402  (encodeur NBT : payload / name / dat / Str / Int / Byte / Comp / Lst)
import build_terrain as B  # noqa: E402
import fl_terrain as F  # noqa: E402
import fl_terrain_report as R  # noqa: E402

Str, Int, Byte, Comp, Lst = T.Str, T.Int, T.Byte, T.Comp, T.Lst


def be(kind, x, y, z, cmd):
    return {'id': Str('minecraft:' + kind), 'x': Int(x), 'y': Int(y), 'z': Int(z), 'Command': Str(cmd), 'auto': Byte(1)}


def nbt(fields):
    return b'\x0a' + T.name('') + T.payload(10, fields)


def chunk_blocks(blocks):
    """Chunk 26.x minimal : block entities sous la racine, plus un faux palette qui contient aussi « command_block »."""
    return nbt({'DataVersion': Int(4903), 'block_entities': Lst(10, blocks),
                'sections': Lst(10, [{'palette': Lst(10, [{'Name': Str('minecraft:command_block')}])}])})


def mca(chunks, compress=True):
    """[(index 0..1023, NBT brut, type de compression)] -> octets d'un .mca (en-tête 8 Ko + chunks alignés sur 4 Ko).
    compress=False : les octets sont écrits tels quels même sous le type 2 (pour fabriquer un chunk zlib invalide)."""
    header, body = bytearray(8192), b''
    for idx, raw, ctype in chunks:
        data = zlib.compress(raw) if ctype == 2 and compress else raw
        rec = struct.pack('>IB', len(data) + 1, ctype) + data
        rec += b'\0' * (-len(rec) % 4096)
        header[4 * idx:4 * idx + 4] = ((2 + len(body) // 4096) << 8 | len(rec) // 4096).to_bytes(4, 'big')
        body += rec
    return bytes(header) + body


def level_dat(spawn=(1274, 209, 181)):
    return T.dat({'Data': Comp({'LevelName': Str('Fausse carte'), 'LastPlayed': (4, 1788549987225),
                                'spawn': Comp({'pos': (11, list(spawn)), 'dimension': Str('minecraft:overworld')})})})


def snapshot(root):
    return {p.relative_to(root).as_posix(): (p.stat().st_size, p.stat().st_mtime_ns, hashlib.sha256(p.read_bytes()).hexdigest())
            for p in sorted(root.rglob('*')) if p.is_file()}


class Base(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        self.map, self.out = self.tmp / 'map', self.tmp / 'out'
        self.dim = self.map / 'dimensions' / 'minecraft' / 'overworld'
        for sub in ('region', 'entities', 'poi', 'data'):
            (self.dim / sub).mkdir(parents=True)
        (self.map / 'level.dat').write_bytes(level_dat())
        self.cmds = [be('command_block', 5, 70, 9, 'gamerule doDaylightCycle false'),
                     be('chain_command_block', 6, 70, 9, 'tellraw @a {"text":"x"}'),
                     be('repeating_command_block', 7, 70, 9, 'execute in mg:floaty as @a[tag=x] run scoreboard players add @s mg.st 1'),
                     be('chest', 8, 70, 9, 'ignored')]
        (self.dim / 'region' / 'r.2.0.mca').write_bytes(mca([(0, chunk_blocks(self.cmds), 2),
                                                             (1, nbt({'DataVersion': Int(4903), 'sections': Lst(10, [])}), 2)]))
        (self.dim / 'region' / 'r.0.0.mca').write_bytes(mca([]))
        (self.dim / 'entities' / 'r.2.0.mca').write_bytes(mca([(3, nbt({'Entities': Lst(10, [
            {'id': Str('minecraft:command_block_minecart'), 'Pos': Lst(6, [1.5, 64.0, -2.5]), 'Command': Str('time set day')}])}), 2)]))
        (self.dim / 'poi' / 'r.2.0.mca').write_bytes(mca([]))
        (self.dim / 'data' / 'world_border.dat').write_bytes(b'ne doit pas etre exporte')
        marker = self.tmp / 'repo' / 'data' / 'mg' / 'function' / 'core' / 'load.mcfunction'          # faux dépôt : ce que check_root exige
        marker.parent.mkdir(parents=True)
        marker.write_text('say load', encoding='utf-8')

    def build(self, out=None, **kw):
        """Par défaut SANS réécriture (zip et rapport de L5 / L6a : les tests de ce fichier) et avec un faux dépôt dans le dossier temporaire
        (terrain_sched.txt n'est jamais écrit dans le vrai dépôt) ; la réécriture : test_floaty_rewrite_*."""
        return B.build(self.map, out or self.out, **{'rewrite': False, 'pack_root': self.tmp / 'repo', **kw})


class Zip(Base):
    def test_reproducible_and_content(self):
        r1 = self.build(self.tmp / 'a')
        r2 = self.build(self.tmp / 'b')
        sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()           # noqa: E731
        self.assertEqual(sha(r1['zip']), sha(r2['zip']))
        self.assertEqual(r1['sha'], r2['sha'])
        self.assertEqual(r1['report'].read_bytes(), r2['report'].read_bytes())
        with zipfile.ZipFile(r1['zip']) as zf:
            names = zf.namelist()
            self.assertEqual(names, ['entities/r.2.0.mca', 'poi/r.2.0.mca', 'region/r.0.0.mca', 'region/r.2.0.mca', 'VERSION'])
            self.assertEqual({i.date_time for i in zf.infolist()}, {(2026, 1, 1, 0, 0, 0)})
            self.assertEqual(zf.read('region/r.2.0.mca'), (self.dim / 'region' / 'r.2.0.mca').read_bytes())
            version = zf.read('VERSION').decode()
            h = hashlib.sha256()
            for n in names[:-1]:                                              # le sha du VERSION = sha du CONTENU (chemin, taille, octets)
                data = zf.read(n)
                h.update(f'{n}\0{len(data)}\0'.encode() + data)
        self.assertIn(f'content-sha256: {h.hexdigest()}', version)
        for line in ('source-dimension: minecraft:overworld', 'map-name: Fausse carte', 'map-last-played: 2026-09-04T', 'regions: 2'):
            self.assertIn(line, version)
        self.assertEqual(r1['sha'], h.hexdigest())

    def test_content_change_changes_sha(self):
        a = self.build(self.tmp / 'a')
        (self.dim / 'region' / 'r.0.0.mca').write_bytes(mca([(0, chunk_blocks([]), 2)]))
        self.assertNotEqual(a['sha'], self.build(self.tmp / 'b')['sha'])

    def test_map_never_written(self):
        before = snapshot(self.map)
        self.build()
        self.assertEqual(snapshot(self.map), before)
        self.assertEqual(sorted(p.name for p in self.out.iterdir()), ['floaty_terrain.zip', 'floaty_terrain_report.txt'])

    def test_out_inside_map_or_repo_refused(self):
        in_repo = ROOT / 'tools' / 'zz_floaty_terrain_out'
        for bad in (self.map / 'out', self.dim / 'region', in_repo):
            with self.assertRaises(B.TerrainError, msg=str(bad)):
                self.build(bad)
        self.assertFalse(in_repo.exists())                                    # refusé AVANT toute création de dossier
        self.assertFalse((self.map / 'out').exists())

    def test_out_guard_resolves_dotdot_and_refuses_a_file(self):
        for bad in (self.map / 'sub' / '..' / 'out', ROOT / 'tools' / '..' / 'zz_floaty_terrain_out2'):
            with self.assertRaises(B.TerrainError, msg=str(bad)):
                self.build(bad)
        self.assertFalse((ROOT / 'zz_floaty_terrain_out2').exists())
        as_file = self.tmp / 'un_fichier'
        as_file.write_text('x')
        with self.assertRaises(B.TerrainError) as cm:
            self.build(as_file)
        self.assertIn('est un fichier', str(cm.exception))
        self.assertEqual(as_file.read_text(), 'x')

    def test_failed_scan_leaves_no_old_report(self):
        self.build()
        report = self.out / B.REPORT_NAME
        self.assertTrue(report.exists())
        with mock.patch.object(F, 'scan_chunk', side_effect=RuntimeError('boom')):
            with self.assertRaises(RuntimeError):
                self.build()
        self.assertFalse(report.exists())                                     # ni rapport ni zip d'un build précédent : un build qui échoue ne laisse rien
        self.assertEqual(list(self.out.iterdir()), [])

    def test_no_part_left_on_keyboard_interrupt(self):
        files = [('region/r.2.0.mca', self.dim / 'region' / 'r.2.0.mca')]
        self.out.mkdir()
        with mock.patch.object(B.os, 'replace', side_effect=KeyboardInterrupt):
            with self.assertRaises(KeyboardInterrupt):
                B.write_zip(self.out / B.ZIP_NAME, files, lambda sha, src: 'v')
            with self.assertRaises(KeyboardInterrupt):
                B.write_report(self.out / B.REPORT_NAME, 'texte')
        self.assertEqual(list(self.out.iterdir()), [])                        # ni .part ni fichier final

    def test_spawn_region_note(self):
        self.assertIn('region r.2.0 presente', self.build()['report'].read_text(encoding='utf-8'))
        (self.dim / 'region' / 'r.2.0.mca').unlink()
        self.assertIn('ABSENTE', self.build(self.tmp / 'b')['report'].read_text(encoding='utf-8'))


class Dimensions(Base):
    def test_none_found(self):
        empty = self.tmp / 'vide'
        (empty / 'dimensions' / 'minecraft' / 'overworld' / 'region').mkdir(parents=True)
        with self.assertRaises(B.TerrainError) as cm:
            B.build(empty, self.out, pack_root=self.tmp / 'repo')
        self.assertIn('aucune dimension', str(cm.exception))
        self.assertFalse(self.out.exists())

    def test_ambiguous_lists_them_and_wanted_picks(self):
        other = self.map / 'dimensions' / 'minecraft' / 'the_nether' / 'region'
        other.mkdir(parents=True)
        (other / 'r.0.0.mca').write_bytes(mca([]))
        with self.assertRaises(B.TerrainError) as cm:
            self.build()
        msg = str(cm.exception)
        self.assertIn('minecraft:overworld', msg)
        self.assertIn('minecraft:the_nether', msg)
        self.assertIn('--dimension', msg)
        self.assertEqual(self.build(dimension='minecraft:the_nether')['dim'], 'minecraft:the_nether')
        with self.assertRaises(B.TerrainError):
            self.build(dimension='mg:inconnue')

    def test_legacy_layout_and_main_exit_code(self):
        legacy = self.tmp / 'old'
        (legacy / 'region').mkdir(parents=True)
        (legacy / 'region' / 'r.0.0.mca').write_bytes(mca([]))
        self.assertEqual(list(B.find_dimensions(legacy)), ['minecraft:overworld'])
        err, out = io.StringIO(), io.StringIO()
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(out):
            self.assertEqual(B.main(['--map', str(self.tmp / 'vide'), '--out', str(self.out), '--root', str(self.tmp / 'repo')]), 1)
            self.assertEqual(B.main(['--map', str(self.map), '--out', str(self.out), '--root', str(self.tmp / 'repo')]), 0)
        self.assertIn('erreur : carte introuvable', err.getvalue())
        self.assertIn('sha256', out.getvalue())


class Report(Base):
    def test_blocks_listed_with_coordinates(self):
        text = self.build()['report'].read_text(encoding='utf-8')
        for line in ('5 70 9\tcommand_block\tauto\tgamerule\tgamerule doDaylightCycle false',
                     '6 70 9\tchain_command_block\tauto\tselecteur_global\t',
                     '7 70 9\trepeating_command_block\tauto\tselecteur_global\t',     # @a[tag=x] : pas de tag=mg.flw ni de position
                     '1 64 -3\tcommand_block_minecart\t-\ttime\ttime set day'):
            self.assertIn(line, text)
        self.assertNotIn('ignored', text)                                     # un coffre n'est pas un bloc de commande
        self.assertIn('4 commandes du terrain (blocs, minecarts, panneaux)', text)
        self.assertIn('a risque : 4 blocs, 4 commandes distinctes', text)

    def test_line_is_one_line_without_tab(self):
        f = F.Found('command_block', (1, 2, 3), 'say a\tb\n  c\r\nd', True, 'region/r.0.0.mca')
        self.assertEqual(R._line(f, ['say']), '1 2 3\tcommand_block\tauto\tsay\tsay a b c d')

    def test_examples_most_serious_first(self):
        text = self.build()['report'].read_text(encoding='utf-8')
        sections = {s.splitlines()[0]: [l for l in s.splitlines()[1:] if l] for s in text.split('## ')[1:]}
        ex = next(v for k, v in sections.items() if 'les plus preoccupantes' in k)
        self.assertEqual([l.split(']')[0] for l in ex], ['- [gamerule', '- [time', '- [selecteur_global', '- [selecteur_global'])
        verbs = next(v for k, v in sections.items() if k.startswith('selecteur_global par commande'))
        self.assertEqual(sorted((l.split(':')[0].strip('- ').strip(), int(l.split(':')[1])) for l in verbs), [('scoreboard', 1), ('tellraw', 1)])


if __name__ == '__main__':
    unittest.main()
