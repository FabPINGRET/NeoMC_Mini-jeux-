"""Dédoublonnage après la scission (tools/resourcepack/floaty_rp.py : floaty_extra(keep_same=True) + floaty_settle) : l'empreinte du manifeste porte sur
TOUTE la carte, y compris les fichiers déjà identiques dans NeoMC ; ceux-ci ne sont retirés qu'ensuite. Un fichier généré par la scission (assets/floaty/...,
item enveloppé) ou venu de la carte qui existe dans NeoMC avec un autre contenu arrête le build en listant les chemins.
Fixtures synthétiques partagées avec test_floaty_split.py (importées) ; le dossier out (celui de gen_rp) est un dossier temporaire.
Lancer : python -m unittest discover -s tools/tests -v (racine dérivée de ce fichier).
"""
import copy
import importlib.util
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))          # fixtures de test_floaty_split (même dossier, comme test_floaty_chunks)
from test_floaty_split import APPLE, EXTRA, MANIFEST, MC, PACK_FMT, RP, SWORD, fs  # noqa: E402

spec = importlib.util.spec_from_file_location('floaty_rp', RP / 'floaty_rp.py')
fr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fr)

SAME = MC + 'textures/block/new.png'                 # fichier neuf de la carte (b'new'), aussi présent à l'identique dans NeoMC


def put(base, files):
    for rel, data in files.items():
        p = Path(base) / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)


class Settle(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.out = Path(tmp.name) / 'out'
        put(self.out, {'pack.mcmeta': b'{"pack": {}}', SAME: EXTRA[SAME]})
        src = Path(tmp.name) / 'map_rp'
        put(src, EXTRA)
        self.env = {fr.FLOATY_ENV: str(src)}

    def extra(self, keep_same):
        with redirect_stdout(io.StringIO()):
            return fr.floaty_extra(str(self.out), self.env, keep_same)

    def test_keep_same_keeps_the_identical_files_and_default_drops_them(self):
        self.assertIn(SAME, self.extra(True))
        self.assertNotIn(SAME, self.extra(False))
        self.assertEqual(sorted(self.extra(True)), sorted(set(self.extra(False)) | {SAME}))        # rien d'autre ne change

    def test_digest_needs_the_identical_files_then_settle_drops_them(self):
        server, opt = fs.floaty_split(self.extra(True), PACK_FMT, copy.deepcopy(MANIFEST))          # empreinte sur toute la carte : passe
        self.assertIn(SAME, server)
        server, opt = fr.floaty_settle(server, opt, str(self.out))
        self.assertNotIn(SAME, server)                                                           # puis retiré : déjà dans le pack NeoMC
        self.assertIn(MC + 'textures/block/stone.png', opt)                                       # le reste du pack optionnel est intact
        with self.assertRaises(SystemExit) as cm:                                                # cas inverse : retiré AVANT, l'empreinte ne colle plus
            fs.floaty_split(self.extra(False), PACK_FMT, copy.deepcopy(MANIFEST))
        self.assertIn('ne correspond plus', str(cm.exception))

    def test_identical_optional_file_is_dropped_and_inputs_are_not_modified(self):
        stone = MC + 'textures/block/stone.png'
        put(self.out, {stone: b'stone'})
        server, opt = {SAME: b'new', 'a': b'a'}, {stone: b'stone', 'b': b'b'}
        before = copy.deepcopy((server, opt))
        got = fr.floaty_settle(server, opt, str(self.out))
        self.assertEqual(got, ({'a': b'a'}, {'b': b'b'}))
        self.assertEqual((server, opt), before)

    def test_generated_file_in_conflict_with_neomc_is_listed(self):
        server, opt = fs.floaty_split(self.extra(True), PACK_FMT, copy.deepcopy(MANIFEST))
        renamed, wrapped = 'assets/floaty/models/item/apple.json', APPLE
        put(self.out, {renamed: b'autre', wrapped: b'{}'})
        with self.assertRaises(SystemExit) as cm:
            fr.floaty_settle(server, opt, str(self.out))
        msg = str(cm.exception)
        self.assertIn('2 fichier(s)', msg)
        self.assertIn(renamed, msg)
        self.assertIn(wrapped, msg)

    def test_generated_file_identical_to_neomc_is_not_a_conflict(self):
        server, opt = fs.floaty_split(self.extra(True), PACK_FMT, copy.deepcopy(MANIFEST))
        put(self.out, {SWORD: server[SWORD], 'assets/floaty/models/item/apple.json': server['assets/floaty/models/item/apple.json']})
        server, opt = fr.floaty_settle(server, opt, str(self.out))
        self.assertNotIn(SWORD, server)
        self.assertNotIn('assets/floaty/models/item/apple.json', server)
        self.assertIn(APPLE, server)                                                              # l'autre item enveloppé reste

    def test_optional_file_in_conflict_with_neomc_is_listed(self):
        put(self.out, {MC + 'textures/block/stone.png': b'autre'})
        with self.assertRaises(SystemExit) as cm:
            fr.floaty_settle({}, {MC + 'textures/block/stone.png': b'stone'}, str(self.out))
        self.assertIn(MC + 'textures/block/stone.png', str(cm.exception))


if __name__ == '__main__':
    unittest.main()
