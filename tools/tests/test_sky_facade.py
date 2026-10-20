"""Élytra : tools/sky/gen_sky.py est une façade ; chaque fonction vit dans son module sky_* et les constantes partagées
sont le même objet partout (pas de copie). Lancer depuis la racine du dépôt : python -m unittest discover -s tools/tests -v
"""
import ast
import importlib
import sys
import types
import unittest
from pathlib import Path

SKY = Path(__file__).resolve().parents[2] / 'tools' / 'sky'
SOURCE_MAX = 500                                        # plafond dur (cible 300)
# module -> fonctions / classes définies à son niveau (la façade ne définit que W et main)
SPLIT = {
    'sky_track': ['axis_of'],
    'sky_vox': ['Vox', 'to_cmds'],
    'sky_shapes': ['edge', 'tree', 'island', 'cliff', 'tower', 'arch', 'cloud', 'ring', 'spike', 'pillar', 'wind_column'],
    'sky_layout': ['seg_dist', 'path_dist', 'box_path_clear', 'sec_order', 'build'],
    'sky_game': ['disc', 'pad_lines', 'pad1_floor', 'pad3_floor', 'game'],
    'sky_modes': ['tparts', 'modes'],
}
# module propriétaire -> objets partagés (les modules qui les importent doivent voir le même objet)
SHARED = {
    'sky_track': ['NS', 'RINGS', 'N', 'PATH', 'AXES', 'PAD1', 'PAD3', 'PADR', 'ZONE', 'PERCH1', 'PERCH3', 'ARENA', 'FLOOR3', 'RING_COLS'],
    'sky_vox': ['Vox', 'to_cmds'],
    'sky_shapes': ['COLS', 'COL_Y0', 'COL_Y1', 'COL_R', 'island', 'ring'],
    'sky_game': ['ELY', 'ROCK', 'WIND', 'SKYITEM'],
}

if str(SKY) not in sys.path:
    sys.path.insert(0, str(SKY))
import gen_sky   # noqa: E402

MODULES = {name: importlib.import_module(name) for name in SPLIT}


class SkyFacade(unittest.TestCase):
    def test_functions_defined_in_split_modules(self):
        for modname, names in SPLIT.items():
            for name in names:
                obj = getattr(MODULES[modname], name)
                self.assertIsInstance(obj, (types.FunctionType, type), name)
                self.assertEqual(obj.__module__, modname, '%s défini hors de %s' % (name, modname))

    def test_facade_defines_only_W_and_main(self):
        own = [k for k, v in vars(gen_sky).items() if isinstance(v, types.FunctionType) and v.__module__ == gen_sky.__name__]
        self.assertEqual(own, ['W', 'main'])

    def test_shared_names_not_redefined(self):
        """Un objet partagé n'est défini qu'une fois : aucun autre module ne le (ré)assigne ni ne le redéfinit au niveau module."""
        for modname in SPLIT:
            tree = ast.parse((SKY / (modname + '.py')).read_text(encoding='utf-8'))
            defined = set()
            for node in tree.body:
                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                    defined.add(node.name)
                elif isinstance(node, ast.Assign):
                    defined.update(n.id for t in node.targets for n in ast.walk(t) if isinstance(n, ast.Name))
            for owner, names in SHARED.items():
                if owner != modname:
                    self.assertFalse(defined & set(names), '%s redéfinit %s (propriétaire : %s)' % (modname, sorted(defined & set(names)), owner))

    def test_modules_do_not_import_facade(self):
        for p in sorted(SKY.glob('sky_*.py')):
            for node in ast.walk(ast.parse(p.read_text(encoding='utf-8'))):
                names = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module] if isinstance(node, ast.ImportFrom) else []
                self.assertNotIn('gen_sky', names, '%s importe la façade (import circulaire)' % p.name)

    def test_sources_size(self):
        for p in sorted(SKY.glob('*.py')):
            n = len(p.read_text(encoding='utf-8').splitlines())
            self.assertLessEqual(n, SOURCE_MAX, '%s : %d lignes (plafond %d)' % (p.name, n, SOURCE_MAX))


if __name__ == '__main__':
    unittest.main()
