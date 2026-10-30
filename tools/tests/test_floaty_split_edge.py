"""Cas limites de la scission Floaty (floaty_split.py, floaty_rp.py, gen_rp.py) non couverts ailleurs.
Fixtures synthétiques partagées avec test_floaty_split.py (importées).
- gen_rp.py de bout en bout dans une copie temporaire (outils + data/mg/function, manifeste factice : la copie est la seule façon de rediriger les
  sorties hors de releases/ sans toucher au code de prod). Copie ~90 Mo : ~30 s ; ignoré si NEOMC_SKIP_RP_E2E est posée.
- sounds.json de la carte illisible / pas un objet, clés de premier niveau de la carte écartées au profit de celles de vanilla,
  floaty_write_opt avec un pack optionnel vide, PACK_FMT à bornes entières (🔵 connu, épinglé en échec attendu).
Lancer : python -m unittest discover -s tools/tests -v (racine dérivée de ce fichier).
"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))          # fixtures de test_floaty_split (même dossier, comme test_floaty_chunks)
from test_floaty_split import EXTRA, MANIFEST, MC, PACK_FMT, RP, ROOT, SWORD, fs, js, mdl, plus, split  # noqa: E402

spec = importlib.util.spec_from_file_location('floaty_rp', RP / 'floaty_rp.py')
fr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fr)

SND = MC + 'sounds.json'


class SoundsGuard(unittest.TestCase):
    def stops(self, data, needle):
        extra, man = plus({SND: data})
        with self.assertRaises(SystemExit) as cm:
            split(extra, man)
        msg = str(cm.exception)
        self.assertIn(needle, msg)
        self.assertNotIn('floaty_manifest.py', msg)               # le manifeste n'y peut rien : pas de consigne de relance

    def test_sounds_json_not_an_object(self):
        self.stops(b'[]', 'objet JSON')
        self.stops(b'"x"', 'objet JSON')

    def test_sounds_json_unreadable(self):
        self.stops(b'{pas du json', 'illisible')

    def test_sounds_json_empty_object_passes(self):
        server, _ = split()                                       # EXTRA porte déjà un sounds.json vide : octets conservés
        self.assertEqual(server[SND], b'{}')


class WrapEdge(unittest.TestCase):
    def test_map_top_level_keys_other_than_model_are_dropped_for_vanilla_ones(self):
        """La carte redéfinit oversized_in_gui : seule la valeur vanilla (True) est gardée, la clé de la carte n'ajoute rien."""
        map_item = {'model': {'type': 'minecraft:model', 'model': 'item/sword'}, 'oversized_in_gui': False, 'extra_key': 1}
        extra, man = plus({SWORD: js(map_item)})
        server, _ = split(extra, man)
        out = json.loads(server[SWORD].decode('utf-8'))
        self.assertEqual({k: v for k, v in out.items() if k != 'model'}, {'oversized_in_gui': True})
        self.assertEqual(list(out)[0], 'model')

    def test_vanilla_item_without_extra_key_stays_a_single_key_definition(self):
        server, _ = split()
        out = json.loads(server[MC + 'items/apple.json'].decode('utf-8'))
        self.assertEqual(list(out), ['model'])
        self.assertEqual(out['model']['fallback'], mdl('minecraft:item/apple'))

    def test_empty_extra_gives_two_empty_packs_even_with_an_empty_manifest(self):
        self.assertEqual(fs.floaty_split({}, PACK_FMT, {}), ({}, {}))          # variable absente : le manifeste n'est même pas lu


class WriteOptEdge(unittest.TestCase):
    def test_empty_optional_pack_has_only_its_pack_mcmeta(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'a' / 'b' / 'opt.zip'                 # dossiers parents créés
            fr.floaty_write_opt(str(path), {}, {'pack': {'description': 'é'}})
            with zipfile.ZipFile(path) as zf:
                self.assertEqual(zf.namelist(), ['pack.mcmeta'])
                self.assertEqual(json.loads(zf.read('pack.mcmeta').decode('utf-8')), {'pack': {'description': 'é'}})
                self.assertEqual(zf.infolist()[0].date_time, fr.FLOATY_DATE)

    def test_split_settle_write_chain_is_reproducible(self):
        """Chaîne réelle de gen_rp (split puis settle puis écriture) : deux écritures donnent les mêmes octets, pack.mcmeta une seule fois."""
        blobs = []
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / 'out'
            out.mkdir()
            for n in range(2):
                server, opt = fr.floaty_settle(*split(pack_fmt=PACK_FMT), str(out))
                path = Path(tmp) / f'o{n}.zip'
                fr.floaty_write_opt(str(path), opt, {'pack': PACK_FMT})
                blobs.append(path.read_bytes())
            with zipfile.ZipFile(Path(tmp) / 'o0.zip') as zf:
                names = zf.namelist()
        self.assertEqual(blobs[0], blobs[1])
        self.assertEqual(names, sorted(names))
        self.assertEqual(names.count('pack.mcmeta'), 1)


class PackFmtInt(unittest.TestCase):
    @unittest.expectedFailure
    def test_integer_formats_are_refused_cleanly(self):
        # 🔵 connu (floaty_split.py:138) : min_format entier -> TypeError (int <= list) au lieu d'un SystemExit lisible. Épinglé, non corrigé ici.
        with self.assertRaises(SystemExit):
            split(pack_fmt={'min_format': 88, 'max_format': 88})


@unittest.skipIf(os.environ.get('NEOMC_SKIP_RP_E2E'), 'NEOMC_SKIP_RP_E2E posée')
class GenRpEndToEnd(unittest.TestCase):
    """gen_rp.py exécuté pour de bon dans une copie : carte factice minuscule + manifeste factice cohérent (celui des fixtures)."""
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix='neomc_e2e_')
        cls.addClassCleanup(shutil.rmtree, cls.tmp, True)
        cls.root = Path(cls.tmp) / 'repo'
        ign = shutil.ignore_patterns('__pycache__', '*.pyc')
        shutil.copytree(ROOT / 'tools', cls.root / 'tools', ignore=ign)
        shutil.copytree(ROOT / 'data' / 'mg' / 'function', cls.root / 'data' / 'mg' / 'function')
        (cls.root / 'tools' / 'resourcepack' / 'floaty_vanilla.json').write_text(json.dumps(MANIFEST), encoding='utf-8')   # manifeste factice (copie seulement)
        cls.map = Path(cls.tmp) / 'map'
        (cls.map / 'pack.mcmeta').parent.mkdir(parents=True)
        (cls.map / 'pack.mcmeta').write_text('{"pack": {"pack_format": 1}}', encoding='utf-8')
        for rel, data in EXTRA.items():
            p = cls.map / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
        env = {**os.environ, 'NEOMC_FLOATY_RP': str(cls.map), 'PYTHONUTF8': '1'}
        cls.run1 = cls.gen(env)
        cls.bytes1 = {n: (cls.root / 'releases' / n).read_bytes() for n in ('neomc_resourcepack.zip', 'floaty_optional_resourcepack.zip')}
        cls.run2 = cls.gen(env)                                  # deuxième passage : reproductibilité

    @classmethod
    def gen(cls, env):
        return subprocess.run([sys.executable, str(cls.root / 'tools' / 'resourcepack' / 'gen_rp.py'), str(cls.root)],
                              env=env, capture_output=True, text=True, encoding='utf-8', timeout=300)

    def test_runs_ok_and_writes_both_zips(self):
        self.assertEqual(self.run1.returncode, 0, self.run1.stderr[-2000:])
        self.assertEqual(self.run2.returncode, 0, self.run2.stderr[-2000:])
        self.assertIn('pack optionnel', self.run1.stdout)

    def test_zips_are_reproducible(self):
        for n, b in self.bytes1.items():
            self.assertEqual((self.root / 'releases' / n).read_bytes(), b, n)

    def test_server_zip_content(self):
        with zipfile.ZipFile(self.root / 'releases' / 'neomc_resourcepack.zip') as zf:
            names = zf.namelist()
            self.assertEqual(len(names), len(set(names)))
            self.assertEqual(names.count('pack.mcmeta'), 1)
            for p in (SWORD, 'assets/floaty/textures/item/apple.png', MC + 'textures/block/new.png', 'assets/floaty/models/item/rod.json'):
                self.assertIn(p, names)
            self.assertNotIn(MC + 'textures/block/stone.png', names)        # remplacement global : pack optionnel seulement
            sel = json.loads(zf.read(SWORD).decode('utf-8'))['model']
            self.assertEqual(sel['property'], 'minecraft:context_dimension')
            self.assertEqual(json.loads(zf.read('pack.mcmeta').decode('utf-8'))['pack']['max_format'], [88, 99])
            self.assertTrue(any(n.startswith('assets/mg/') for n in names))

    def test_optional_zip_content(self):
        with zipfile.ZipFile(self.root / 'releases' / 'floaty_optional_resourcepack.zip') as zf:
            names = zf.namelist()
            self.assertEqual(names, sorted(names))
            self.assertEqual(names.count('pack.mcmeta'), 1)
            self.assertIn(MC + 'textures/block/stone.png', names)
            self.assertFalse(any(n.startswith(('assets/mg/', 'assets/floaty/')) for n in names))

    def test_resourcepack_folder_receives_nothing_from_the_map(self):
        self.assertFalse((self.root / 'resourcepack' / 'assets' / 'floaty').exists())
        self.assertFalse((self.root / 'resourcepack' / MC / 'textures' / 'block' / 'stone.png').exists())


if __name__ == '__main__':
    unittest.main()
