"""tools/floaty : fl_mca.locate (entrées d'en-tête corrompues : nombre de secteurs nul, longueur qui dépasse les secteurs annoncés) et
fl_mca.check (chunk perdu, apparu, modifié, plages qui se chevauchent, nombre de secteurs incohérent) ; en-tête écrit vérifié à la main.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v
"""
import struct
import sys
import unittest
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / 'tools' / 'floaty'))
import test_floaty_rw_mca as M  # noqa: E402  (mca, be, chunk_blocks, growing, OLD, NEW)
import fl_mca  # noqa: E402
import fl_terrain_rw as RW  # noqa: E402

mca, be, chunk_blocks = M.mca, M.be, M.chunk_blocks
OLD, NEW = M.OLD, M.NEW


def two_chunks():
    raw = chunk_blocks([be('command_block', 1, 2, 3, OLD)])
    return raw, mca([(0, raw, 2), (1, raw, 2)])


def set_entry(data, i, sector, count):
    out = bytearray(data)
    out[4 * i:4 * i + 4] = (sector << 8 | count).to_bytes(4, 'big')
    return bytes(out)


class Locate(unittest.TestCase):
    def test_valid_entry(self):
        _, data = two_chunks()
        off, length, ctype = fl_mca.locate(data, 0)
        self.assertEqual((off, ctype), (2 * 4096, 2))
        self.assertLessEqual(4 + length, 4096)
        self.assertIsNone(fl_mca.locate(data, 5))                                       # entrée vide

    def test_zero_sector_count_is_corrupt(self):
        _, data = two_chunks()
        bad = set_entry(data, 0, 2, 0)                                                 # offset valide, 0 secteur annoncé
        self.assertIs(fl_mca.locate(bad, 0), False)
        stats = Counter()
        self.assertEqual([i for i, _ in fl_mca.payloads(bad, stats)], [1])
        self.assertEqual(stats['corrompu'], 1)
        with self.assertRaises(fl_mca.McaError):
            fl_mca.rebuild(bad, {1: chunk_blocks([])})

    def test_length_beyond_the_announced_sectors_is_corrupt(self):
        _, data = two_chunks()
        bad = bytearray(data)
        struct.pack_into('>I', bad, 2 * 4096, 4093)                                    # 4 + 4093 > 1 secteur, mais le fichier est assez long
        self.assertIs(fl_mca.locate(bytes(bad), 0), False)
        self.assertEqual(len(bad) - 2 * 4096 >= 4 + 4093, True)                         # c'est bien le seul critère qui joue
        with self.assertRaises(fl_mca.McaError):
            fl_mca.rebuild(bytes(bad), {1: chunk_blocks([])})
        struct.pack_into('>I', bad, 2 * 4096, 4092)                                    # inverse : 4 + 4092 = 1 secteur pile, accepté
        self.assertEqual(fl_mca.locate(bytes(bad), 0)[1], 4092)

    def test_pass_leaves_the_file_whole_for_either_corruption(self):
        raw, data = two_chunks()
        bad_length = bytearray(data)
        struct.pack_into('>I', bad_length, 2 * 4096, 4093)
        for name, bad in (('count', set_entry(data, 0, 2, 0)), ('length', bytes(bad_length))):
            with self.subTest(name):
                p = RW.Pass(True)
                out = p.file(M.ARC, bad)
                self.assertEqual((out, p.files, p.stats['corrompu']), (bad, 0, 1))
                self.assertEqual([(c.action, c.reason, c.new) for c in p.after], [('laisse', 'en_tete', OLD)])


class Check(unittest.TestCase):
    def setUp(self):
        self.raw, self.data = two_chunks()
        self.good = fl_mca.rebuild(self.data, {0: self.raw})

    def fails(self, new, pattern, old=None, changes=None):
        with self.assertRaisesRegex(fl_mca.VerifyError, pattern):
            fl_mca.check(self.data if old is None else old, new, {0: self.raw} if changes is None else changes)

    def test_a_faithful_rebuild_passes(self):
        fl_mca.check(self.data, self.good, {0: self.raw})
        fl_mca.check(self.data, self.data, {})

    def test_lost_chunk(self):
        self.fails(set_entry(self.good, 1, 0, 0), 'perdu')
        self.fails(set_entry(self.good, 1, 900, 1), 'perdu')                           # entrée corrompue : même verdict

    def test_appeared_chunk(self):
        only_first = mca([(0, self.raw, 2)])
        self.fails(self.data, 'apparu', old=only_first, changes={})

    def test_modified_chunk_that_should_have_been_copied(self):
        off, length, _ = fl_mca.locate(self.good, 1)
        bad = bytearray(self.good)
        bad[off + 4 + length - 1] ^= 1                                                 # un octet du chunk 1 : toujours localisable, plus identique
        self.fails(bytes(bad), 'modifié')

    def test_overlapping_sector_ranges(self):
        sector = int.from_bytes(self.good[0:3], 'big')
        self.fails(set_entry(self.good, 1, sector, 1), 'chevauchent')                  # le chunk 1 pointe sur le même secteur (même contenu)

    def test_sector_range_beyond_the_file(self):
        self.fails(self.good[:-100], 'chevauchent|corrompu|perdu')

    def test_inconsistent_sector_count(self):
        sector = int.from_bytes(self.good[0:3], 'big')
        self.fails(set_entry(self.good, 0, sector, 2), 'secteurs incohérent')          # annonce 2 secteurs pour un enregistrement qui en tient 1

    def test_header_bytes_of_a_rebuild_by_hand(self):
        grown = M.growing()
        small = chunk_blocks([be('command_block', 5, 70, 9, 'scoreboard players add x y 1')])
        data = mca([(0, grown, 2), (1, small, 2)])
        out = fl_mca.rebuild(data, {0: grown.replace(OLD.encode(), NEW.encode())})
        self.assertEqual(out[0:4], b'\x00\x00\x02\x02')                                  # chunk 0 : secteur 2, 2 secteurs (il a grandi)
        self.assertEqual(out[4:8], b'\x00\x00\x04\x01')                                  # chunk 1 : glisse au secteur 4, 1 secteur
        self.assertEqual(out[8:4096], b'\0' * (4096 - 8))
        self.assertEqual(len(out), (2 + 2 + 1) * 4096)


if __name__ == '__main__':
    unittest.main()
