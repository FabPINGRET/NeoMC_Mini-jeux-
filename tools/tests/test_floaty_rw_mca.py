"""tools/floaty : fl_terrain_rw (réécriture des commandes d'un chunk, d'un .mca) et fl_mca (reconstruction) sur de faux .mca : chunk qui grandit
d'un secteur, gzip / brut réécrits en zlib, LZ4 / externe / corrompu recopiés tels quels, en-tête corrompu, plafond de secteurs, horodatages,
panneaux NBT et JSON, chaînes MUTF-8 / trop longues, vérification de relecture.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v
"""
import gzip
import json
import random
import sys
import unittest
import zlib
from collections import Counter
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / 'tools' / 'floaty'))
import test_floaty_signs as TS  # noqa: E402  (holder, faces, comp, json_msg, chunk, EMPTY, MODERN, JSON_FORMAT)
import test_floaty_terrain as TT  # noqa: E402  (mca, be, nbt, chunk_blocks)
import fl_mca  # noqa: E402
import fl_nbt  # noqa: E402
import fl_rewrite  # noqa: E402
import fl_terrain as F  # noqa: E402
import fl_terrain_cmd as C  # noqa: E402
import fl_terrain_rw as RW  # noqa: E402

mca, be, nbt, chunk_blocks = TT.mca, TT.be, TT.nbt, TT.chunk_blocks
Str, Int, Lst = TT.Str, TT.Int, TT.Lst
ARC = 'region/r.2.0.mca'
OLD, NEW = 'tellraw @a "x"', 'tellraw @a[tag=mg.flw] "x"'
R_NOOP = fl_rewrite.NOOP


def run(raw, ctx=None):
    """NBT brut d'un chunk -> (nouveau NBT ou None, res, [Found])."""
    root, spans = fl_nbt.loads_spans(raw)
    finds = F.scan_chunk(raw, ARC, 0, Counter(), {k: [] for k in F.A_VERIFIER}, root)
    new, res = RW.rewrite_chunk(raw, root, spans, finds, ctx or C.Ctx())
    return new, res, finds


def commands(raw):
    root = fl_nbt.loads(raw)
    return sorted(f.command for f in F.blocks_of(root, ARC) + F.signs_of(root, ARC)[0])


def header_ts(data):
    """Horodatages non nuls dans l'en-tête (la 2e moitié est recopiée telle quelle)."""
    ts = b''.join((1700000000 + i).to_bytes(4, 'big') for i in range(1024))
    return data[:4096] + ts + data[8192:]


def sized(n):
    """Chunk d'un bloc de commande (OLD) et n caractères hexadécimaux incompressibles."""
    rnd = random.Random(7)
    filler = ''.join(rnd.choice('0123456789abcdef') for _ in range(n))
    return nbt({'DataVersion': Int(4903), 'filler': Str(filler), 'block_entities': Lst(10, [be('command_block', 1, 2, 3, OLD)])})


def growing():
    """Un chunk qui tient dans 1 secteur et en prend 2 une fois réécrit (OLD -> NEW)."""
    for n in range(7000, 9000, 4):
        raw = sized(n)
        if fl_mca.sectors(fl_mca.record(raw)) == 1 and fl_mca.sectors(fl_mca.record(raw.replace(OLD.encode(), NEW.encode()))) == 2:
            return raw
    raise AssertionError('aucun chunk de test ne change de secteur')


class Chunk(unittest.TestCase):
    def test_blocks_minecarts_rewritten_and_reread(self):
        cmds = [be('command_block', 1, 2, 3, OLD), be('chain_command_block', 2, 2, 3, 'gamerule doDaylightCycle false'),
                be('chest', 3, 2, 3, 'ignored')]
        new, res, _ = run(chunk_blocks(cmds))
        self.assertEqual(commands(new), sorted([NEW, R_NOOP]))
        self.assertEqual({a for _, a, _ in res.values()}, {'reecrit', 'noop'})
        cart = nbt({'Entities': Lst(10, [{'id': Str('minecraft:command_block_minecart'), 'Pos': Lst(6, [1.5, 64.0, -2.5]),
                                          'Command': Str('time set day')}])})
        new, _, _ = run(cart)
        self.assertEqual(fl_nbt.loads(new)['Entities'][0]['Command'], R_NOOP)

    def test_nothing_to_change_gives_none(self):
        self.assertIsNone(run(chunk_blocks([be('command_block', 1, 2, 3, 'scoreboard players add x y 1')]))[0])

    def test_nbt_sign_click_event(self):
        sign = TS.holder('sign', (1, 2, 3), front_text=TS.faces([TS.comp('', OLD), TS.EMPTY, TS.EMPTY, TS.EMPTY])['front_text'])
        raw = TS.chunk(TS.MODERN, [sign])
        new, res, _ = run(raw)
        self.assertEqual(commands(new), [NEW])
        self.assertEqual([a for _, a, _ in res.values()], ['reecrit'])
        got = fl_nbt.loads(new)['block_entities'][0]['front_text']['messages'][0]['click_event']
        self.assertEqual((got['action'], got['command']), ('run_command', NEW))
        self.assertEqual(len(new) - len(raw), len(NEW) - len(OLD))             # le reste du chunk est recopié octet pour octet

    def test_json_sign_is_redumped_compact(self):
        for cmd, want in ((OLD, NEW), ('/' + OLD, '/' + NEW)):
            with self.subTest(cmd):
                sign = TS.holder('sign', (1, 2, 3), front_text=TS.faces([TS.json_msg(cmd), '{}', '{}', '{}'], ctype=8)['front_text'])
                new, res, _ = run(TS.chunk(TS.JSON_FORMAT, [sign]))
                msg = fl_nbt.loads(new)['block_entities'][0]['front_text']['messages'][0]
                self.assertEqual(msg, json.dumps({'text': '', 'clickEvent': {'action': 'run_command', 'value': want}},
                                                 separators=(',', ':'), ensure_ascii=True))
                self.assertEqual(commands(new), [want])
                self.assertEqual(len(res), 1)

    def test_json_sign_keeps_non_bmp_characters_as_ascii_escapes(self):
        sign = TS.holder('sign', (1, 2, 3), front_text=TS.faces([TS.json_msg('say \U0001F334'), '{}', '{}', '{}'], ctype=8)['front_text'])
        raw = TS.chunk(TS.JSON_FORMAT, [sign])
        self.assertTrue(fl_nbt.loads(raw)['block_entities'][0]['front_text']['messages'][0].isascii())      # source : échappement ASCII
        new, _, _ = run(raw)
        msg = fl_nbt.loads(new)['block_entities'][0]['front_text']['messages'][0]
        self.assertTrue(msg.isascii())                                                  # reste échappé : jamais d'UTF-8 sur 4 octets
        self.assertEqual(json.loads(msg)['clickEvent']['value'], 'tellraw @a[tag=mg.flw] "\U0001F334"')
        self.assertNotIn('\U0001F334'.encode('utf-8'), new)
        self.assertEqual(commands(new), ['tellraw @a[tag=mg.flw] "\U0001F334"'])

    def test_json_sign_with_unchanged_command_is_not_touched(self):
        sign = TS.holder('sign', (1, 2, 3), front_text=TS.faces([TS.json_msg('scoreboard players add x y 1'), '{}', '{}', '{}'], ctype=8)['front_text'])
        self.assertIsNone(run(TS.chunk(TS.JSON_FORMAT, [sign]))[0])            # inverse : pas de ré-encodage inutile

    def test_true_mutf8_source_is_rewritten_and_written_back_as_mutf8(self):
        pair = b'\xed\xa0\xbd\xed\xb8\x80'                                              # U+1F600 en MUTF-8 : paire de substitution
        raw = chunk_blocks([be('command_block', 1, 2, 3, 'say AAAAAA')]).replace(b'AAAAAA', pair)
        new, res, finds = run(raw)
        self.assertEqual([(a, r) for _, a, r in res.values()], [('reecrit', None)])
        self.assertEqual(commands(new), ['tellraw @a[tag=mg.flw] "\U0001F600"'])
        self.assertIn(b'"' + pair + b'"', new)                                         # relu par le lecteur strict, écrit en paires
        self.assertNotIn('\U0001F600'.encode('utf-8'), new)
        self.assertEqual(len(finds), 1)

    def test_nul_in_a_source_string_round_trips_as_c0_80(self):
        raw = nbt({'DataVersion': Int(4903), 'filler': Str('AAAA'), 'block_entities': Lst(10, [be('command_block', 1, 2, 3, 'say BBBB')])})
        raw = raw.replace(b'AAAA', b'a\xc0\x80b').replace(b'BBBB', b'x\xc0\x80y')
        new, _, _ = run(raw)
        self.assertEqual(fl_nbt.loads(new)['filler'], 'a\0b')                          # chaîne non touchée : octets C0 80 recopiés tels quels
        self.assertIn(b'a\xc0\x80b', new)
        cmd, = commands(new)
        self.assertEqual(cmd, 'tellraw @a[tag=mg.flw] ' + json.dumps('x\0y'))          # le NUL de la commande est échappé dans le texte JSON
        self.assertNotIn(b'\0', fl_nbt.encode_str(cmd)[2:])
        self.assertEqual(fl_nbt.loads(new)['block_entities'][0]['Command'], cmd)

    def test_utf8_four_byte_chunk_is_not_read_so_not_rewritten(self):
        raw = chunk_blocks([be('command_block', 1, 2, 3, 'say \U0001F600')])           # l'encodeur de test écrit l'UTF-8 sur 4 octets
        with self.assertRaises(ValueError):
            fl_nbt.loads_spans(raw)
        stats = Counter()
        self.assertEqual(list(F.scan_chunk(raw, ARC, 0, stats, {k: [] for k in F.A_VERIFIER}, None)), [])
        self.assertEqual(stats['illisible'], 1)
        p = RW.Pass(True)
        data = mca([(0, raw, 2)])
        self.assertIs(p.file(ARC, data), data)                                          # le fichier reste tel quel, le chunk est compté
        self.assertEqual((p.files, p.after, p.stats['illisible']), (0, [], 1))
        self.assertEqual(p.unread_cmd, [(ARC, 64, 0)])                                  # signalé : fichier, cx, cz (raison illisible_cmd du rapport)
        ok = TT.nbt({'DataVersion': TT.Int(4903), 'block_entities': TT.Lst(10, [TT.be('command_block', 1, 2, 3, 'say hi')])})
        quiet = TT.nbt({'DataVersion': TT.Int(4903), 'note': TT.Str('\U0001F600')})     # illisible, mais sans command_block ni run_command
        p = RW.Pass(True)
        p.file(ARC, mca([(0, ok, 2), (1, quiet, 2)]))
        self.assertEqual((p.unread_cmd, p.stats['illisible']), ([], 0))                 # inverse : lisible, ou sans commande : rien à signaler
        self.assertEqual(RW.Pass(False).unread_cmd, [])                                 # inverse : --no-rewrite ne lit pas, donc ne signale pas
        q = RW.Pass(False)
        q.file(ARC, data)
        self.assertEqual(q.unread_cmd, [])

    def test_defensive_mutf8_check_leaves_a_chunk_whose_source_string_is_invalid(self):
        raw = chunk_blocks([be('command_block', 1, 2, 3, OLD)])
        root, spans = fl_nbt.loads_spans(raw)
        finds = F.scan_chunk(raw, ARC, 0, Counter(), {k: [] for k in F.A_VERIFIER}, root)
        bad = raw.replace(OLD.encode(), b'tellraw @a "\xf0"')                            # même longueur, octet de tête 0xF0 : plus du MUTF-8
        new, res = RW.rewrite_chunk(bad, root, spans, finds, C.Ctx())
        self.assertEqual((new, [(a, r) for _, a, r in res.values()]), (None, [('laisse', 'mutf8')]))

    def test_string_too_long_after_rewrite_is_left_alone(self):
        long_bytes = 'tellraw @a "' + '€' * 21840 + '"'                             # 65533 octets : tient ; +12 avec le tag : non
        long_chars = 'say ' + 'a' * 32770                                               # plus de 32767 caractères une fois en tellraw
        other = be('command_block', 9, 2, 3, OLD)
        for cmd, why in ((long_bytes, 'chaine'), (long_chars, 'trop_long')):
            with self.subTest(why):
                new, res, _ = run(chunk_blocks([be('command_block', 1, 2, 3, cmd), other]))
                self.assertEqual(sorted(r for _, a, r in res.values() if a == 'laisse'), [why])
                self.assertEqual(commands(new), sorted([cmd, NEW]))                    # l'autre commande du chunk est réécrite quand même

    def test_reread_mismatch_keeps_the_original_chunk(self):
        raw = chunk_blocks([be('command_block', 1, 2, 3, OLD)])
        with mock.patch.object(RW.fl_nbt, 'loads', return_value={}):
            new, res, _ = run(raw)
        self.assertEqual((new, [(a, r) for _, a, r in res.values()]), (None, [('laisse', 'verif')]))

    def test_nan_double_in_the_chunk_does_not_fail_the_verification(self):
        raw = nbt({'DataVersion': Int(4903), 'Pos': Lst(6, [float('nan'), 1.0]), 'block_entities': Lst(10, [be('command_block', 1, 2, 3, OLD)])})
        new, res, _ = run(raw)
        self.assertEqual([(a, r) for _, a, r in res.values()], [('reecrit', None)])      # pas de 'verif' : un NaN égale un NaN
        self.assertEqual(commands(new), [NEW])
        self.assertTrue(RW._equal({'a': [float('nan')]}, {'a': [float('nan')]}))
        self.assertFalse(RW._equal({'a': [float('nan')]}, {'a': [1.0]}))               # inverse : un NaN n'égale pas un autre nombre

    def test_chunk_over_the_sector_cap_is_left(self):
        raw = growing()
        with mock.patch.object(fl_mca, 'MAX_SECTORS', 1):
            new, res, _ = run(raw)
        self.assertEqual((new, [(a, r) for _, a, r in res.values()]), (None, [('laisse', 'taille')]))
        self.assertIsNotNone(run(raw)[0])                                            # inverse : sous le plafond réel, réécrit


class File(unittest.TestCase):
    def pass_over(self, data, rewrite=True):
        p = RW.Pass(rewrite)
        return p, p.file(ARC, data)

    def test_growth_of_one_sector_shifts_the_next_chunks_only(self):
        grown, other = growing(), chunk_blocks([be('command_block', 5, 70, 9, 'scoreboard players add x y 1')])
        data = header_ts(mca([(0, grown, 2), (1, other, 2), (2, other, 2)]))
        p, out = self.pass_over(data)
        self.assertEqual(p.files, 1)
        old = [fl_mca.locate(data, i) for i in range(3)]
        new = [fl_mca.locate(out, i) for i in range(3)]
        self.assertEqual([n[0] - o[0] for n, o in zip(new, old)], [0, 4096, 4096])      # chunk 0 : 1 -> 2 secteurs ; les suivants glissent d'un secteur
        for i in (1, 2):
            self.assertEqual(out[new[i][0]:new[i][0] + 4 + new[i][1]], data[old[i][0]:old[i][0] + 4 + old[i][1]])      # recopiés octet pour octet
        self.assertEqual(commands(fl_mca.decode(2, out[new[0][0] + 5:new[0][0] + 4 + new[0][1]])), [NEW])
        self.assertEqual(out[4096:8192], data[4096:8192])                               # horodatages recopiés
        self.assertEqual(len(out) - len(data), 4096)
        self.assertEqual(p.after[0].action, 'reecrit')

    def test_gzip_and_raw_chunks_are_rewritten_as_zlib(self):
        raw = chunk_blocks([be('command_block', 1, 2, 3, OLD)])
        data = mca([(0, gzip.compress(raw), 1), (1, raw, 3), (2, zlib.compress(raw), 2)], compress=False)
        p, out = self.pass_over(data)
        self.assertEqual(p.files, 1)
        for i in range(3):
            off, length, ctype = fl_mca.locate(out, i)
            self.assertEqual(ctype, 2)
            self.assertEqual(commands(zlib.decompress(out[off + 5:off + 4 + length])), [NEW])
        self.assertEqual(Counter(c.action for c in p.after), {'reecrit': 3})

    def test_lz4_external_and_corrupt_entries_are_copied_as_is(self):
        raw = chunk_blocks([be('command_block', 1, 2, 3, OLD)])
        data = mca([(0, zlib.compress(raw), 2), (1, b'lz4 quelconque', 4), (2, b'x', 130), (3, b'zz pas du zlib', 2), (4, zlib.compress(raw), 2)],
                   compress=False)
        p, out = self.pass_over(data)
        self.assertEqual((p.stats['lz4'], p.stats['externe'], p.stats['corrompu']), (1, 1, 1))
        for i in (1, 2, 3):
            a, b = fl_mca.locate(data, i), fl_mca.locate(out, i)
            self.assertEqual(out[b[0]:b[0] + 4 + b[1]], data[a[0]:a[0] + 4 + a[1]])
        for i in (0, 4):
            off, length, _ = fl_mca.locate(out, i)
            self.assertEqual(commands(zlib.decompress(out[off + 5:off + 4 + length])), [NEW])

    def test_corrupt_header_entry_leaves_the_whole_file(self):
        raw = chunk_blocks([be('command_block', 1, 2, 3, OLD)])
        data = bytearray(mca([(0, raw, 2)]))
        data[4 * 9:4 * 9 + 4] = ((900 << 8) | 1).to_bytes(4, 'big')                       # entrée 9 : hors du fichier
        p, out = self.pass_over(bytes(data))
        self.assertEqual((out, p.files, p.stats['corrompu']), (bytes(data), 0, 1))
        self.assertEqual([(c.action, c.reason, c.new) for c in p.after], [('laisse', 'en_tete', OLD)])
        with self.assertRaises(fl_mca.McaError):
            fl_mca.rebuild(bytes(data), {0: raw})

    def test_unchanged_files_are_returned_as_is_and_poi_is_skipped(self):
        data = mca([(0, chunk_blocks([be('command_block', 1, 2, 3, 'scoreboard players add x y 1')]), 2)])
        p = RW.Pass(True)
        self.assertIs(p.file(ARC, data), data)
        poi = mca([(0, chunk_blocks([be('command_block', 1, 2, 3, OLD)]), 2)])
        self.assertIs(p.file('poi/r.2.0.mca', poi), poi)                                # poi/ : ni scanné ni réécrit
        self.assertEqual((p.files, [f.command for f in p.finds]), (0, ['scoreboard players add x y 1']))

    def test_rewrite_off_scans_but_never_changes(self):
        data = mca([(0, chunk_blocks([be('command_block', 1, 2, 3, OLD)]), 2)])
        p, out = self.pass_over(data, rewrite=False)
        self.assertEqual((out, p.after, len(p.finds)), (data, [], 1))

    def test_check_rejects_a_broken_rebuild(self):
        raw = chunk_blocks([be('command_block', 1, 2, 3, OLD)])
        data = header_ts(mca([(0, raw, 2), (1, raw, 2)]))
        good = fl_mca.rebuild(data, {0: raw})
        fl_mca.check(data, good, {0: raw})
        broken = bytearray(good)
        broken[4096] ^= 1                                                              # horodatage modifié
        with self.assertRaises(fl_mca.VerifyError):
            fl_mca.check(data, bytes(broken), {0: raw})
        with self.assertRaises(fl_mca.VerifyError):
            fl_mca.check(data, good, {0: raw + b'\0'})                                 # chunk relu différent de ce qu'on voulait écrire


if __name__ == '__main__':
    unittest.main()
