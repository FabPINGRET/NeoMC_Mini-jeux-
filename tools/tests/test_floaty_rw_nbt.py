"""tools/floaty : fl_nbt.loads_spans / encode_str (remplacement d'une chaîne NBT par une autre de longueur différente, sans rien casser d'autre).
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v
"""
import struct
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / 'tools' / 'floaty'))
import test_floaty_terrain as TT  # noqa: E402  (nbt, Str / Int / Comp / Lst)
import fl_nbt  # noqa: E402

Str, Int, Comp, Lst, nbt = TT.Str, TT.Int, TT.Comp, TT.Lst, TT.nbt


def sample():
    return nbt({'n': Int(7), 'a': Str('hello'), 'l': Lst(8, ['x', 'yy', 'zzz']), 'c': Comp({'k': Str('v'), 'in': Comp({'deep': Str('d')})}),
                'cl': Lst(10, [{'s': Str('un')}, {'s': Str('deux')}]), 'z': Str('fin')})


def splice(raw, span, new):
    return raw[:span[0]] + fl_nbt.encode_str(new) + raw[span[1]:]


class Spans(unittest.TestCase):
    def test_root_is_loads_and_spans_cover_exactly_the_strings(self):
        raw = sample()
        root, spans = fl_nbt.loads_spans(raw)
        self.assertEqual(root, fl_nbt.loads(raw))
        s = spans[(id(root), 'a')]
        self.assertEqual((struct.unpack('>H', raw[s[0]:s[0] + 2])[0], raw[s[0] + 2:s[1]]), (5, b'hello'))
        self.assertEqual(raw[spans[(id(root['c']['in']), 'deep')][0] + 2:spans[(id(root['c']['in']), 'deep')][1]], b'd')
        self.assertEqual(sorted(raw[a + 2:b].decode() for a, b in spans.values()), sorted(
            ['hello', 'x', 'yy', 'zzz', 'v', 'd', 'un', 'deux', 'fin']))                  # les chaînes seulement : pas l'Int, pas les noms

    def test_replaced_string_of_other_length_reads_back_everywhere(self):
        raw = sample()
        root, spans = fl_nbt.loads_spans(raw)
        edits = [(root, 'a', 'beaucoup plus long que hello'), (root['l'], 1, ''), (root['c']['in'], 'deep', 'é€'),
                 (root['cl'][1], 's', 'x' * 300), (root, 'z', 'f')]
        buf = raw
        for box, key, new in sorted(edits, key=lambda e: spans[(id(e[0]), e[1])][0], reverse=True):      # du plus loin au plus près
            buf = splice(buf, spans[(id(box), key)], new)
        want = fl_nbt.loads(raw)
        for box, key, new in edits:
            box[key] = new
        got = fl_nbt.loads(buf)
        self.assertEqual(got, root)
        self.assertNotEqual(got, want)
        self.assertEqual((got['a'], got['l'], got['c']['in']['deep'], got['n']), ('beaucoup plus long que hello', ['x', '', 'zzz'], 'é€', 7))

    def test_list_of_lists_and_non_compound_root(self):
        raw = nbt({'ll': Lst(9, [(8, ['a', 'b']), (8, ['c'])]), 'e': Lst(10, [])})
        root, spans = fl_nbt.loads_spans(raw)
        self.assertEqual(sorted(raw[a + 2:b].decode() for a, b in spans.values()), ['a', 'b', 'c'])
        with self.assertRaises(ValueError):
            fl_nbt.loads_spans(b'\x09\x00\x00')


EMOJI = chr(0x1F600)
PAIR = b'\xed\xa0\xbd\xed\xb8\x80'                          # U+1F600 en MUTF-8 : D83D DE00, 2 x 3 octets


class Encode(unittest.TestCase):
    def test_prefix_and_limits_count_encoded_bytes(self):
        self.assertEqual(fl_nbt.encode_str('é'), b'\x00\x02\xc3\xa9')
        self.assertEqual(fl_nbt.encode_str('a' * 65535)[:2], b'\xff\xff')
        self.assertEqual(fl_nbt.encode_str('€' * 21845)[:2], b'\xff\xff')
        for bad in ('a' * 65536, '€' * 21846, EMOJI * 10923, '\0' * 32768):          # 65538 octets pour 10923 emojis, 65536 pour 32768 NUL
            with self.subTest(len(bad)):
                with self.assertRaises(ValueError):
                    fl_nbt.encode_str(bad)

    def test_emoji_is_a_surrogate_pair_of_two_three_byte_units(self):
        self.assertEqual(fl_nbt.encode_str(EMOJI), b'\x00\x06' + PAIR)
        self.assertEqual(fl_nbt.mutf8_decode(PAIR), EMOJI)

    def test_nul_is_c0_80(self):
        self.assertEqual(fl_nbt.encode_str('x\0y'), b'\x00\x04x\xc0\x80y')
        self.assertEqual(fl_nbt.mutf8_decode(b'x\xc0\x80y'), 'x\0y')

    def test_round_trip_of_every_kind_of_character(self):
        for s in ('', 'abc', 'é€', EMOJI, 'a' + EMOJI + 'b\0c€', chr(0xD83D), chr(0xDE00) + chr(0xD83D), EMOJI * 3):
            with self.subTest(s):
                self.assertEqual(fl_nbt.mutf8_decode(fl_nbt.mutf8_encode(s)), s)

    def test_strict_decoder_rejects_what_java_would_not_write(self):
        for bad in (EMOJI.encode('utf-8'), b'\xf0\x9f\x98\x80', b'\xf8\x88\x80\x80\x80', b'\xff', b'\x80', b'\xc3', b'\xe2\x82', b'\xc3\x28',
                    b'\xc1\x81', b'\xe0\x80\x80', b'\xe0\x9f\xbf'):          # 0xF0, tête invalide, tronqué, continuation fausse, formes trop longues
            with self.subTest(bad):
                with self.assertRaises(ValueError):
                    fl_nbt.mutf8_decode(bad)

    def test_a_chunk_with_utf8_four_byte_string_is_unreadable_not_replaced(self):
        raw = nbt({'a': Str(EMOJI)})                     # l'encodeur de test écrit de l'UTF-8 sur 4 octets : ce que Java refuse
        self.assertIn(EMOJI.encode('utf-8'), raw)
        with self.assertRaises(ValueError):
            fl_nbt.loads(raw)
        with self.assertRaises(ValueError):
            fl_nbt.loads_spans(raw)

    def test_replaced_emoji_string_is_read_back_identically_by_the_strict_reader(self):
        raw = sample()
        root, spans = fl_nbt.loads_spans(raw)
        new = splice(raw, spans[(id(root), 'a')], 'x' + EMOJI + '\0')
        self.assertEqual(fl_nbt.loads(new)['a'], 'x' + EMOJI + '\0')
        self.assertIn(PAIR, new)
        self.assertNotIn(EMOJI.encode('utf-8'), new)

    def test_lone_surrogate_in_a_value_or_a_key_gives_encodable_snbt(self):
        raw = nbt({'a b': Str('AAA'), 'k': Str('é')})
        root, spans = fl_nbt.loads_spans(raw)
        lone = splice(raw, spans[(id(root), 'a b')], chr(0xD83D))                 # valeur : un surrogate isolé (Java l'accepte)
        lone = lone.replace(b'\x00\x03a b', b'\x00\x03' + b'\xed\xa0\xbd')        # clé non nue : le même surrogate isolé
        got = fl_nbt.loads(lone, snbt=True)
        text = fl_nbt.snbt(got)
        self.assertEqual(text.encode('utf-8').decode('utf-8'), text)               # s'encode : gen_floaty n'échoue plus (UnicodeEncodeError)
        self.assertEqual(text, '{"\\ud83d":"\\ud83d",k:"é"}')                       # échappé seulement là où il le faut : é reste en clair
        self.assertEqual(fl_nbt.loads(lone)[chr(0xD83D)], chr(0xD83D))             # inverse : la lecture sans snbt garde le surrogate tel quel
        self.assertEqual(fl_nbt.snbt(fl_nbt.loads(nbt({'a b': Str('é€')}), snbt=True)), '{"a b":"é€"}')      # inverse : texte normal, en clair


if __name__ == '__main__':
    unittest.main()
