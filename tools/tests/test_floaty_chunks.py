"""tools/floaty : lecture des chunks (.mca) par fl_terrain.scan_file et sections « non lus » / « a verifier » du rapport (fl_terrain_report),
sur de faux .mca (aides de test_floaty_terrain). Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v
"""
import contextlib
import io
import sys
import unittest
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / 'tools' / 'floaty'))
import test_floaty_terrain as TT  # noqa: E402  (Base, mca, nbt, be, chunk_blocks, Str / Int / Comp / Lst)
import build_terrain as B  # noqa: E402
import fl_terrain as F  # noqa: E402
import fl_terrain_report as R  # noqa: E402

be, nbt, mca, chunk_blocks = TT.be, TT.nbt, TT.mca, TT.chunk_blocks
Str, Int, Comp, Lst = TT.Str, TT.Int, TT.Comp, TT.Lst
NOTHING = nbt({'DataVersion': Int(4903), 'sections': Lst(10, [{'palette': Lst(10, [{'Name': Str('minecraft:command_block')}])}])})


class Scan(TT.Base):
    def scan_bytes(self, body):
        path = self.dim / 'region' / 'r.2.0.mca'
        path.write_bytes(body)
        stats = Counter()
        finds, pending = F.scan_file(path, stats)
        return finds, stats, pending

    def test_unreadable_chunks_counted_not_fatal(self):
        raw = chunk_blocks(self.cmds)
        finds, stats, _ = self.scan_bytes(mca([(0, raw, 2), (1, raw, 4), (2, raw, 3)]))
        self.assertEqual((stats['lz4'], stats['chunks']), (1, 3))
        self.assertEqual(len(finds), 6)                                       # chunk zlib + chunk brut (type 3), 3 blocs de commande chacun
        text = self.build()['report'].read_text(encoding='utf-8')
        self.assertIn('lz4 1', text)
        self.assertIn('NON analyses', text)

    def test_each_unread_kind_has_its_counter(self):
        cases = {
            'corrompu': (b'ceci n est pas du zlib', 2),                       # type 2 mais octets quelconques : zlib.error
            'illisible': (b'command_block mais pas un NBT', 3),               # pré-filtre positif, NBT invalide
            'externe': (b'x', 130),                                           # 128 + 2 : chunk dans un .mcc
            'inconnu': (b'x', 5),
            'lz4': (chunk_blocks(self.cmds), 4),
        }
        for want, (data, ctype) in cases.items():
            with self.subTest(want):
                finds, stats, _ = self.scan_bytes(mca([(0, data, ctype)], compress=False))
                self.assertEqual((finds, stats['chunks']), ([], 1))
                self.assertEqual({k: v for k, v in stats.items() if k != 'chunks'}, {want: 1})
        self.assertEqual(F.UNREAD, ('lz4', 'externe', 'inconnu', 'corrompu', 'illisible'))
        self.assertEqual(F.A_VERIFIER, ('sans_bloc', 'rc_hors_panneau', 'panneau_illisible'))

    def test_header_entry_inside_header_is_corrupt(self):
        head = bytearray(8192)
        head[0:4] = ((1 << 8) | 1).to_bytes(4, 'big')                         # offset 1 secteur : en plein dans l'en-tête
        finds, stats, _ = self.scan_bytes(bytes(head) + b'\0' * 4096)
        self.assertEqual((finds, stats['corrompu'], stats['chunks']), ([], 1, 0))

    def test_legacy_chunk_format(self):
        legacy = nbt({'Level': Comp({
            'TileEntities': Lst(10, [be('command_block', 1, 2, 3, 'say ancien')]),
            'Entities': Lst(10, [{'id': Str('minecraft:command_block_minecart'), 'Pos': Lst(6, [4.5, 5.0, -6.5]), 'Command': Str('time set day')}])})})
        finds, stats, _ = self.scan_bytes(mca([(0, legacy, 2)]))
        self.assertEqual(sorted((f.kind, f.pos, f.command) for f in finds),
                         [('command_block', (1, 2, 3), 'say ancien'), ('command_block_minecart', (4, 5, -7), 'time set day')])
        self.assertEqual(stats['sans_bloc'], 0)

    def test_block_without_coordinates_is_tolerated(self):
        chunk = nbt({'block_entities': Lst(10, [{'id': Str('minecraft:command_block'), 'Command': Str('say x')}])})
        finds, _, _ = self.scan_bytes(mca([(0, chunk, 2)]))
        self.assertEqual([f.pos for f in finds], [(0, 0, 0)])

    def test_truncated_file_counted(self):
        path = self.dim / 'region' / 'r.2.0.mca'
        path.write_bytes(path.read_bytes()[:8192 + 10])
        stats = Counter()
        self.assertEqual(F.scan_file(path, stats)[0], [])
        self.assertEqual(stats['corrompu'], 2)                                # les deux entrées de l'en-tête pointent hors du fichier

    def test_prefilter_hit_without_block_is_counted_and_located(self):
        finds, stats, pending = self.scan_bytes(mca([(0, NOTHING, 2), (1, chunk_blocks(self.cmds), 2)]))
        self.assertEqual((len(finds), stats['sans_bloc']), (3, 1))
        self.assertEqual(pending, {'sans_bloc': [('region/r.2.0.mca', 64, 0)], 'rc_hors_panneau': [],
                                   'panneau_illisible': []})                  # chunk 0 du fichier r.2.0 : cx = 2 * 32

    def test_sans_bloc_position_is_region_origin_plus_index(self):
        path = self.dim / 'region' / 'r.-2.1.mca'
        path.write_bytes(mca([(5 + 3 * 32, NOTHING, 2), (1023, NOTHING, 2)]))        # index = x + 32 * z
        _, pending = F.scan_file(path, Counter())
        self.assertEqual(pending['sans_bloc'], [('region/r.-2.1.mca', -64 + 5, 32 + 3), ('region/r.-2.1.mca', -64 + 31, 32 + 31)])
        other = self.dim / 'region' / 'bizarre.mca'                                 # nom hors r.X.Z.mca : coordonnées relatives au fichier
        other.write_bytes(mca([(33, NOTHING, 2)]))
        self.assertEqual(F.scan_file(other, Counter())[1]['sans_bloc'], [('region/bizarre.mca', 1, 1)])

    def test_string_selectors_are_totalled_in_stats(self):
        sel = [be('command_block', 1, 2, 3, 'tellraw @s {"text":"@a"}'), be('command_block', 2, 2, 3, 'say @e')]
        _, stats, _ = self.scan_bytes(mca([(0, chunk_blocks(sel), 2)]))
        self.assertEqual(stats['sel_chaine'], 1)


class Sections(TT.Base):
    """Rapport : non lus d'un côté, à vérifier de l'autre, seulement les clés non nulles ; compteurs et pluriel."""

    def report(self, regions, out=None):
        (self.dim / 'region' / 'r.2.0.mca').write_bytes(regions)
        return self.build(out or self.out)

    def test_clean_map_has_no_chunk_section_and_no_zero_line(self):
        text = self.report(mca([(0, chunk_blocks(self.cmds), 2)]))['report'].read_text(encoding='utf-8')
        for absent in ('## Chunks non lus', '## Chunks a verifier', 'lz4', 'sans_bloc', 'rc_hors_panneau', 'panneau_illisible', ' 0 blocs /'):
            self.assertNotIn(absent, text)
        self.assertIn('- chunks a enregistrement complet : 2 (lisibles ou non) ; 0 chunk non lu, 0 a verifier', text)    # region + entities
        self.assertIn('- selecteurs en chaine non examines : 0', text)

    def test_unread_and_to_check_are_separate_sections(self):
        r = self.report(mca([(0, NOTHING, 3), (1, b'x', 4), (2, b'x', 4), (3, b'zz', 2)], compress=False))     # zz en type 2 : zlib invalide
        text = r['report'].read_text(encoding='utf-8')
        self.assertIn('## Chunks non lus (lz4 2, corrompu 1) : NON analyses', text)
        self.assertNotIn('sans_bloc', text.split('## Chunks non lus')[1].split('## Chunks a verifier')[0])
        self.assertIn('## Chunks a verifier (sans_bloc 1)', text)
        self.assertIn('- sans_bloc : command_block present', text)
        self.assertIn('  region/r.2.0.mca chunk (64, 0)', text.split('## Chunks a verifier')[1])
        self.assertIn('3 chunks non lus, 1 a verifier', text)
        self.assertEqual(R.chunk_totals(r['stats'], r['pending']), (3, 1))

    def test_unreadable_sign_section_and_chunk_counted_once(self):
        sign = {'id': Str('minecraft:sign'), 'x': Int(1), 'y': Int(2), 'z': Int(3), 'Text1': Str('{"clickEvent":{"action":"run_command"')}
        book = {'id': Str('minecraft:chest'), 'x': Int(2), 'y': Int(2), 'z': Int(3), 'Items': Lst(8, ['run_command'])}
        text = self.report(mca([(0, nbt({'block_entities': Lst(10, [sign, book])}), 2)]))['report'].read_text(encoding='utf-8')
        self.assertIn('## Chunks a verifier (rc_hors_panneau 1, panneau_illisible 1)', text)
        self.assertIn('- panneau_illisible : panneau avec plus de run_command', text)
        self.assertIn('0 chunk non lu, 1 a verifier', text)                                      # deux raisons, un seul chunk

    def test_string_selectors_counter_in_report(self):
        sel = [be('command_block', 1, 2, 3, 'tellraw @s {"text":"@a"}'), be('command_block', 2, 2, 3, 'say @e')]
        text = self.report(mca([(0, chunk_blocks(sel), 2)]))['report'].read_text(encoding='utf-8')
        self.assertIn('- selecteurs en chaine non examines : 1', text)

    def test_totals_line_plural(self):
        for args, want in [((0, 0), '0 chunk non lu, 0 a verifier'), ((1, 1), '1 chunk non lu, 1 a verifier'),
                           ((2, 5), '2 chunks non lus, 5 a verifier')]:
            with self.subTest(args):
                self.assertEqual(R.totals_line(*args), want)

    def test_stdout_line_and_scan_time_on_stderr_only(self):
        (self.dim / 'region' / 'r.2.0.mca').write_bytes(mca([(0, NOTHING, 3), (1, b'x', 4)], compress=False))     # type 3 : NBT brut
        err, out = io.StringIO(), io.StringIO()
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(out):
            self.assertEqual(B.main(['--map', str(self.map), '--out', str(self.out), '--root', str(self.tmp / 'repo')]), 0)
        self.assertIn('1 chunk non lu, 1 a verifier', out.getvalue())
        self.assertRegex(err.getvalue(), r'build : \d+\.\d s')
        self.assertNotRegex(out.getvalue(), r'build : \d')
        self.assertNotRegex((self.out / B.REPORT_NAME).read_text(encoding='utf-8'), r'build : \d')     # le rapport ne porte aucun temps


if __name__ == '__main__':
    unittest.main()
