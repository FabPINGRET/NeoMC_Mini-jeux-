"""tools/floaty : L6b de bout en bout sur une petite carte synthétique (un .mca à plusieurs chunks : bloc de commande, chaîne, panneau
run_command, chunks intacts ; un fichier entities/ avec un minecart ; un .mca dont une entrée d'en-tête est corrompue), build_terrain avec
et sans réécriture : zip reproductible, chunks relus par le lecteur strict, chunks intacts recopiés octet pour octet, horodatages, comptes du
rapport, --no-rewrite sans effet sur les commandes, aller-retour MUTF-8 (emoji + NUL). Plus deux tests qui FIGENT des limites connues (🔵 du
tour 4 de la revue). Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v
"""
import hashlib
import struct
import sys
import tempfile
import unittest
import zipfile
import zlib
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / 'tools' / 'floaty'))
import test_floaty_signs as TS  # noqa: E402  (holder / faces / comp : panneaux)
import test_floaty_terrain as TT  # noqa: E402  (level_dat, be, mca)
import build_terrain as B  # noqa: E402
import fl_mca  # noqa: E402
import fl_nbt  # noqa: E402
import fl_rewrite  # noqa: E402
import fl_terrain as F  # noqa: E402
import fl_terrain_cmd as C  # noqa: E402

Str, Int, Byte, Comp, Lst = TT.Str, TT.Int, TT.Byte, TT.Comp, TT.Lst
EMOJI_NUL = 'x\U0001F600\x00y'                     # hors plan basique + NUL : MUTF-8 = surrogates CESU-8 et C0 80
NOOP = fl_rewrite.NOOP
STAMPS = {0: 1700000001, 1: 1700000002, 2: 1700000003, 7: 1700000004}
OVERWORLD = 'minecraft:overworld'


def enc_name(s):
    return fl_nbt.encode_str(s)                    # préfixe u16 + MUTF-8 : l'octet exact que lit Java


def payload(t, v):
    """Comme test_floaty_state.payload, mais les chaînes et les noms passent par fl_nbt.encode_str (MUTF-8)."""
    if t == 8:
        return enc_name(v)
    if t == 9:
        sub, items = v
        return bytes([sub]) + struct.pack('>i', len(items)) + b''.join(payload(sub, x) for x in items)
    if t == 10:
        return b''.join(bytes([ct]) + enc_name(k) + payload(ct, cv) for k, (ct, cv) in v.items()) + b'\x00'
    return TT.T.payload(t, v)


def root(fields):
    return b'\x0a' + enc_name('') + payload(10, fields)


def chunk(blocks):
    return root({'DataVersion': Int(4903), 'block_entities': Lst(10, blocks),
                 'sections': Lst(10, [{'palette': Lst(10, [{'Name': Str('minecraft:command_block')}])}])})


def stamped(raw_mca, stamps):
    """.mca de TT.mca + horodatages non nuls (2e secteur de l'en-tête)."""
    head = bytearray(raw_mca)
    for i, ts in stamps.items():
        head[4096 + 4 * i:4096 + 4 * i + 4] = struct.pack('>I', ts)
    return bytes(head)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def strict_chunks(data):
    """Octets d'un .mca -> {index: racine NBT relue par le lecteur STRICT} ; les chunks non lisibles lèvent."""
    return {i: fl_nbt.loads(raw) for i, raw in fl_mca.payloads(data, Counter())}


def record(data, i):
    off, length, _ = fl_mca.locate(data, i)
    return data[off:off + 4 + length]


def commands(data):
    """Commandes (blocs, panneaux) de tous les chunks d'un .mca, relus en strict -> liste triée de (index, commande)."""
    return sorted((i, f.command) for i, r in strict_chunks(data).items() for f in F.blocks_of(r, 'region/x.mca') + F.signs_of(r, 'region/x.mca')[0])


class E2E(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        self.map = self.tmp / 'map'
        self.dim = self.map / 'dimensions' / 'minecraft' / 'overworld'
        for sub in ('region', 'entities', 'poi'):
            (self.dim / sub).mkdir(parents=True)
        (self.map / 'level.dat').write_bytes(TT.level_dat())
        marker = self.tmp / 'repo' / 'data' / 'mg' / 'function' / 'core' / 'load.mcfunction'
        marker.parent.mkdir(parents=True)
        marker.write_text('say load', encoding='utf-8')
        sign = TS.holder('sign', (4, 70, 9), front_text=TS.faces([TS.comp('go', 'give @a diamond')] + [TS.EMPTY] * 3)['front_text'])
        self.blocks = [TT.be('command_block', 1, 70, 9, 'say \U0001F600 hi'),
                       {**TT.be('chain_command_block', 2, 70, 9, 'kill @e[type=item]'), 'conditionMet': Byte(1), 'CustomName': Str(EMOJI_NUL)},
                       TT.be('command_block', 3, 70, 9, 'gamerule doDaylightCycle false'), sign]
        self.intact = [root({'DataVersion': Int(4903), 'sections': Lst(10, [])}),
                       chunk([TS.holder('chest', (8, 70, 9), CustomName=Str(EMOJI_NUL))]),
                       root({'DataVersion': Int(4903), 'Status': Str('minecraft:full'), 'sections': Lst(10, [])})]
        region = TT.mca([(0, chunk(self.blocks), 2), (1, self.intact[0], 2), (2, self.intact[1], 2), (7, self.intact[2], 2)])
        self.src_region = stamped(region, STAMPS)
        (self.dim / 'region' / 'r.0.0.mca').write_bytes(self.src_region)
        (self.dim / 'entities' / 'r.0.0.mca').write_bytes(stamped(TT.mca([(4, root({'Entities': Lst(10, [
            {'id': Str('minecraft:command_block_minecart'), 'Pos': Lst(6, [1.5, 64.0, -2.5]), 'Command': Str('say hi')}])}), 2)]), {4: 1700000009}))
        bad = bytearray(TT.mca([(0, chunk([TT.be('command_block', 1, 70, 9, 'say hi')]), 2)]))
        bad[4 * 9:4 * 9 + 4] = (0xFFFF << 8 | 1).to_bytes(4, 'big')               # chunk 9 : offset hors du fichier
        self.src_bad = bytes(bad)
        (self.dim / 'region' / 'r.1.0.mca').write_bytes(self.src_bad)
        (self.dim / 'poi' / 'r.0.0.mca').write_bytes(TT.mca([]))

    def build(self, name, **kw):
        return B.build(self.map, self.tmp / name, **{'pack_root': self.tmp / 'repo', **kw})

    def entry(self, r, arc):
        with zipfile.ZipFile(r['zip']) as zf:
            return zf.read(arc)

    def test_rewritten_zip_is_reproducible_and_chunks_are_read_back_strictly(self):
        a, b = self.build('a'), self.build('b')
        self.assertEqual(sha(a['zip']), sha(b['zip']))                             # octets identiques
        self.assertEqual(a['report'].read_bytes(), b['report'].read_bytes())
        data = self.entry(a, 'region/r.0.0.mca')
        self.assertEqual(sorted(strict_chunks(data)), [0, 1, 2, 7])                # tous relus en strict, aucun perdu
        for arc in ('region/r.0.0.mca', 'entities/r.0.0.mca'):
            self.assertEqual(Counter(), Counter({k: v for k, v in self._payload_stats(self.entry(a, arc)).items() if k != 'chunks'}), arc)

    @staticmethod
    def _payload_stats(data):
        st = Counter()
        list(fl_mca.payloads(data, st))
        return st

    def test_commands_are_rewritten_by_kind(self):
        data = self.entry(self.build('a'), 'region/r.0.0.mca')
        self.assertEqual([c for _, c in commands(data)], sorted([
            'tellraw @a[tag=mg.flw] "\U0001F600 hi"', 'kill @e[type=item,distance=0..]', NOOP, 'give @a[tag=mg.flw] diamond']))
        cart = strict_chunks(self.entry(self.build('b'), 'entities/r.0.0.mca'))[4]
        self.assertEqual(cart['Entities'][0]['Command'], 'tellraw @a[tag=mg.flw] "hi"')

    def test_untouched_chunks_are_byte_identical_and_timestamps_kept(self):
        data = self.entry(self.build('a'), 'region/r.0.0.mca')
        for i in (1, 2, 7):                                                        # sans commande : enregistrement recopié tel quel
            self.assertEqual(record(data, i), record(self.src_region, i), i)
        self.assertNotEqual(record(data, 0), record(self.src_region, 0))           # inverse : le chunk à commandes a bien changé
        self.assertEqual(data[4096:8192], self.src_region[4096:8192])              # horodatages conservés
        self.assertEqual(struct.unpack_from('>I', data, 4096 + 4 * 7)[0], STAMPS[7])
        self.assertEqual(self.entry(self.build('b'), 'entities/r.0.0.mca')[4096 + 16:4096 + 20], struct.pack('>I', 1700000009))

    def test_emoji_and_nul_survive_the_mutf8_round_trip(self):
        data = self.entry(self.build('a'), 'region/r.0.0.mca')
        chain = [b for b in strict_chunks(data)[0]['block_entities'] if b['id'] == 'minecraft:chain_command_block'][0]
        self.assertEqual(chain['CustomName'], EMOJI_NUL)                           # champ voisin du Command réécrit : intact
        self.assertEqual(strict_chunks(data)[2]['block_entities'][0]['CustomName'], EMOJI_NUL)       # chunk intact : idem
        raw = next(r for i, r in fl_mca.payloads(data, Counter()) if i == 0)
        self.assertIn(b'\xc0\x80', raw)                                            # le NUL est écrit C0 80, jamais 00
        self.assertIn(fl_nbt.encode_str('tellraw @a[tag=mg.flw] "\U0001F600 hi"'), raw)      # l'emoji de la commande réécrite : CESU-8 (2 x 3 octets)
        self.assertNotIn('\U0001F600'.encode('utf-8'), raw)                        # jamais l'UTF-8 sur 4 octets

    def test_corrupted_header_file_is_copied_as_is_and_reported(self):
        r = self.build('a')
        self.assertEqual(self.entry(r, 'region/r.1.0.mca'), self.src_bad)          # en-tête corrompu : rien n'est réécrit
        left = [(c.action, c.reason, c.new) for c in r['after'] if c.found.file == 'region/r.1.0.mca']
        self.assertEqual(left, [('laisse', 'en_tete', 'say hi')])
        self.assertEqual(r['stats']['corrompu'], 1)

    def test_report_counts(self):
        r = self.build('a')
        self.assertEqual(len(r['finds']), 6)                                       # 4 blocs/panneau + 1 minecart + 1 du fichier à en-tête corrompu
        by = Counter((c.action, c.reason) for c in r['after'])
        self.assertEqual(by, {('reecrit', None): 4, ('noop', 'risque_dur'): 1, ('laisse', 'en_tete'): 1})
        self.assertEqual(r['rewritten'], 5)                                        # réécrites + NOOP ; le « laisse » n'en est pas
        self.assertEqual(r['files_rebuilt'], 2)                                    # region/r.0.0 + entities/r.0.0
        report = r['report'].read_text(encoding='utf-8')
        self.assertIn('6 commandes du terrain', report)
        self.assertIn('rewritten-commands: 5', self.entry(r, 'VERSION').decode())

    def test_no_rewrite_touches_no_command(self):
        r = self.build('n', rewrite=False)
        with zipfile.ZipFile(r['zip']) as zf:
            for arc, p in B.collect(self.dim):
                self.assertEqual(zf.read(arc), p.read_bytes(), arc)                # octet pour octet, corrompu compris
        self.assertEqual(r['after'], [])
        self.assertEqual(r['rewritten'], 0)
        self.assertIn('say \U0001F600 hi', [c for _, c in commands(self.entry(r, 'region/r.0.0.mca'))])
        self.assertNotEqual(sha(r['zip']), sha(self.build('a')['zip']))            # inverse : la réécriture, elle, change le zip

    def test_source_map_is_never_written(self):
        before = TT.snapshot(self.map)
        self.build('a')
        self.build('n', rewrite=False)
        self.assertEqual(TT.snapshot(self.map), before)

    # --- limites connues (🔵 du tour 4) : ces tests FIGENT le comportement actuel, ce ne sont pas des corrections -----------------------

    def test_known_limit_execute_in_overworld_run_say_selector_is_a_hard_noop(self):
        # LIMITE CONNUE : L1 ne sait pas analyser `say @p hi` derrière un `execute in minecraft:overworld run` (sélecteur dans le texte du
        # say) : la commande entière devient un NOOP risque_dur au lieu d'être cantonnée. Figé tel quel ; à rouvrir si L1 l'apprend.
        for dim in (OVERWORLD, 'minecraft:the_nether'):
            with self.subTest(dim):
                self.assertEqual(C.rewrite_command('execute in minecraft:overworld run say @p hi', C.Ctx(dim)), (NOOP, 'noop', 'risque_dur'))

    def test_known_limit_data_modify_command_set_value_is_a_hard_noop(self):
        # LIMITE CONNUE : une commande qui écrit une autre commande (`data modify ... Command set value "execute in minecraft:overworld
        # run ..."`) n'est pas analysée : NOOP risque_dur. Figé tel quel ; inverse : la même valeur sans `execute in` est laissée telle quelle.
        for dim in (OVERWORLD, 'minecraft:the_nether'):
            with self.subTest(dim):
                ctx = C.Ctx(dim)
                self.assertEqual(C.rewrite_command('data modify block 1 2 3 Command set value "execute in minecraft:overworld run say hi"', ctx),
                                 (NOOP, 'noop', 'risque_dur'))
                self.assertEqual(C.rewrite_command('data modify block 1 2 3 Command set value "say hi"', ctx), (None, 'inchange', None))


if __name__ == '__main__':
    unittest.main()
