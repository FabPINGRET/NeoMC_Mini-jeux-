"""tools/floaty : cas limites de revue du lot L6a (classement des commandes du terrain, panneaux, rapport) : texte de panneau « [Shop] »,
falling_block seul dans entities/, run_command imbriqué dans la commande d'un panneau, spawner à passager (findings de revue corrigés
en L6b), puis build_terrain.main de bout en bout (zip reproductible, carte intacte, stdout / rapport cohérents).
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v
"""
import contextlib
import hashlib
import io
import re
import sys
import unittest
import zlib
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / 'tools' / 'floaty'))
import test_floaty_terrain as TT  # noqa: E402  (Base, mca, nbt, snapshot, Str / Int / Comp / Lst)
import test_floaty_signs as TS  # noqa: E402  (holder, faces, comp, chunk, json_msg, EMPTY, MODERN, JSON_FORMAT)
import build_terrain as B  # noqa: E402
import fl_terrain as F  # noqa: E402

mca, nbt, Str, Int, Comp, Lst = TT.mca, TT.nbt, TT.Str, TT.Int, TT.Comp, TT.Lst
holder, faces, comp, chunk, EMPTY = TS.holder, TS.faces, TS.comp, TS.chunk, TS.EMPTY
NOTHING = nbt({'DataVersion': Int(4903), 'sections': Lst(10, [{'palette': Lst(10, [{'Name': Str('minecraft:command_block')}])}])})


class Scan(TT.Base):
    def scan(self, raw, sub='region'):
        path = self.dim / sub / 'r.2.0.mca'
        path.write_bytes(mca([(0, raw, 2)]))
        stats = Counter()
        finds, pending = F.scan_file(path, stats)
        return finds, stats, pending

    def test_literal_bracket_text_among_json_messages_is_not_unreadable(self):
        # (a) « [Shop] » est du texte nu de panneau (pas du JSON valide) : ni trouvaille, ni panneau_illisible
        sign = holder('sign', (1, 2, 3), **faces(front=['[Shop]', TS.json_msg('stop'), '"abc"', '""'], ctype=8))
        finds, stats, pending = self.scan(chunk(TS.JSON_FORMAT, [sign]))
        self.assertEqual([f.command for f in finds], ['stop'])                 # le voisin lisible garde sa commande
        self.assertEqual((stats['panneau_illisible'], pending['panneau_illisible']), (0, []))
        only = holder('sign', (1, 2, 3), **faces(front=['[Shop]', '""', '""', '""'], ctype=8))
        finds, stats, pending = self.scan(chunk(TS.JSON_FORMAT, [only]))
        self.assertEqual((finds, stats['panneau_illisible'], pending['panneau_illisible']), ([], 0, []))

    def test_literal_bracket_text_old_text1_format(self):
        sign = holder('sign', (1, 2, 3), Text1=Str('[Shop]'), Text2=Str('[Shop] 5$'), Text3=Str('""'), Text4=Str('""'))
        finds, stats, _ = self.scan(chunk(2500, [sign]))
        self.assertEqual((finds, stats['panneau_illisible']), ([], 0))

    def test_falling_block_alone_in_entities_file_is_sans_bloc(self):
        # (b) chunk d'un fichier entities/ : l'entité falling_block porte une Command, aucun bloc n'existe dans ce chunk
        falling = {'id': Str('minecraft:falling_block'), 'Pos': Lst(6, [1.0, 2.0, 3.0]), 'BlockState': Comp({'Name': Str('minecraft:command_block')}),
                   'TileEntityData': Comp({'Command': Str('stop'), 'id': Str('minecraft:command_block')})}
        _, stats, pending = self.scan(nbt({'Entities': Lst(10, [falling])}), sub='entities')
        self.assertEqual(stats['sans_bloc'], 1)
        self.assertEqual(pending['sans_bloc'], [('entities/r.2.0.mca', 64, 0)])

    # Finding de revue L6a (faux panneau_illisible, corrigé en L6b) : la commande d'un panneau qui contient elle-même un clickEvent
    # run_command faisait compter 2 run_command pour 1 commande extraite. Attendu : 0 illisible.
    def test_sign_command_containing_run_command_is_not_unreadable(self):
        cmd = 'tellraw @s {"text":"x","clickEvent":{"action":"run_command","value":"/trigger t"}}'
        sign = holder('sign', (1, 2, 3), **faces(front=[comp(cmd=cmd), EMPTY, EMPTY, EMPTY]))
        finds, stats, pending = self.scan(chunk(TS.MODERN, [sign]))
        self.assertEqual([f.command for f in finds], [cmd])
        self.assertEqual((stats['panneau_illisible'], pending['panneau_illisible']), (0, []))

    # Finding de revue L6a (corrigé en L6b) : command_block_minecart passager dans SpawnData.entity.Passengers d'un spawner (porteur sans
    # `Pos`) n'est ni trouvé ni signalé ; attendu : sans_bloc 1.
    def test_spawner_with_minecart_passenger_is_sans_bloc(self):
        pass_ = {'id': Str('minecraft:command_block_minecart'), 'Command': Str('stop')}
        spawner = holder('mob_spawner', (4, 2, 3), SpawnData=Comp({'entity': Comp({
            'id': Str('minecraft:zombie'), 'Passengers': Lst(10, [pass_])})}))
        real = TT.be('command_block', 1, 2, 3, 'say ok')
        _, stats, pending = self.scan(chunk(TS.MODERN, [real, spawner]))
        self.assertEqual((stats['sans_bloc'], len(pending['sans_bloc'])), (1, 1))


class EndToEnd(TT.Base):
    """build_terrain.main sur une mini-carte avec 3 chunks problématiques injectés : 1 corrompu, 1 sans_bloc, 1 panneau illisible."""

    def setUp(self):
        super().setUp()
        sign = holder('sign', (1, 2, 3), Text1=Str('{"clickEvent":{"action":"run_command","value":"op X"}'))
        z = zlib.compress          # compress=False : mca() n'encode rien, on compresse ici les chunks sains
        (self.dim / 'region' / 'r.2.0.mca').write_bytes(mca([
            (0, z(TT.chunk_blocks(self.cmds)), 2),                             # sain : 3 blocs de commande
            (1, b'zz pas du zlib', 2),                                         # corrompu (octets non zlib sous le type 2)
            (2, z(NOTHING), 2),                                                # sans_bloc : palette command_block, aucun bloc
            (3, z(chunk(TS.MODERN, [sign])), 2)], compress=False))             # panneau illisible

    def run_main(self, out, *extra):
        err, so = io.StringIO(), io.StringIO()
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(so):
            code = B.main(['--map', str(self.map), '--out', str(out), '--root', str(self.tmp / 'repo'), *extra])
        return code, so.getvalue(), err.getvalue()

    def test_main_zip_is_reproducible_and_map_untouched(self):
        before = TT.snapshot(self.map)
        c1, _, _ = self.run_main(self.tmp / 'a')
        c2, _, _ = self.run_main(self.tmp / 'b')
        self.assertEqual((c1, c2), (0, 0))
        sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()           # noqa: E731
        self.assertEqual(sha(self.tmp / 'a' / B.ZIP_NAME), sha(self.tmp / 'b' / B.ZIP_NAME))
        self.assertEqual(TT.snapshot(self.map), before)                        # octets, taille ET mtime : rien n'a été écrit dans la carte

    def test_stdout_and_report_agree_with_injected_chunks(self):
        code, out, _ = self.run_main(self.out)
        self.assertEqual(code, 0)
        text = (self.out / B.REPORT_NAME).read_text(encoding='utf-8')
        want = '1 chunk non lu, 2 a verifier'                                  # corrompu ; sans_bloc + panneau_illisible (2 chunks distincts)
        self.assertIn(want, out)
        self.assertIn(want, text)
        self.assertIn('## Chunks non lus (corrompu 1)', text)
        self.assertIn('## Chunks a verifier (sans_bloc 1, panneau_illisible 1)', text)
        self.assertIn('  region/r.2.0.mca chunk (66, 0)', text)               # index 2 -> sans_bloc
        self.assertIn('  region/r.2.0.mca chunk (67, 0)', text)               # index 3 -> panneau illisible
        self.assertEqual(len(re.findall(r'^  region/r\.2\.0\.mca chunk \(', text, re.M)), 2)
        self.assertIn('4 commandes du terrain', text)                          # 3 blocs de commande + 1 minecart de entities/ (le coffre ignoré)
        self.assertIn(f'(4 commandes ; {want})', out)


if __name__ == '__main__':
    unittest.main()
