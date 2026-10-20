"""Terra Nova : tools/arcade/gen_terranova.py est une façade qui exécute ses parts tv_*.py (exec) dans l'ordre d'origine.
Lancer depuis la racine du dépôt : python -m unittest discover -s tools/tests -v   (la racine est dérivée de ce fichier).
"""
import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCADE = ROOT / 'tools' / 'arcade'
FACADE = ARCADE / 'gen_terranova.py'
SKIP_DIRS = {'claude-bridge', '__pycache__'}            # comme test_tools_hygiene : pas du Python / caches
SOURCE_MAX = 500                                       # plafond dur (cible 300)
# les 6 parts issues de la découpe, dans l'ordre d'exécution
PARTS = ('tv_relief.py', 'tv_colony.py', 'tv_gear.py', 'tv_combat.py', 'tv_missions.py', 'tv_loop.py')
# suite complète des exec à nom littéral de la façade : les exec de tv_world.py et tv_rpg.py (anciens) restent à leur place relative
# (tv_dino_fn.py est exécuté depuis tv_combat.py, pas depuis la façade)
EXEC_ORDER = ('tv_relief.py', 'tv_colony.py', 'tv_world.py', 'tv_gear.py', 'tv_combat.py', 'tv_missions.py', 'tv_loop.py', 'tv_rpg.py')


def exec_names(path):
    """Noms de fichiers des exec(open(os.path.join(..., 'x.py'), ...).read()[, globals]) d'un source, dans l'ordre du texte."""
    found = []
    for node in ast.walk(ast.parse(path.read_bytes())):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'exec'):
            continue
        for sub in ast.walk(node):
            if isinstance(sub, ast.Constant) and isinstance(sub.value, str) and sub.value.endswith('.py'):
                found.append(((node.lineno, node.col_offset), sub.value))
    return tuple(name for _, name in sorted(found))


class TvParts(unittest.TestCase):
    def test_facade_execs_parts_in_order(self):
        self.assertEqual(exec_names(FACADE), EXEC_ORDER)
        self.assertEqual(tuple(n for n in EXEC_ORDER if n in PARTS), PARTS)
        self.assertEqual(exec_names(ARCADE / 'tv_combat.py'), ('tv_dino_fn.py',))

    def test_sources_size(self):
        for name in ('gen_terranova.py',) + PARTS:
            n = len((ARCADE / name).read_text(encoding='utf-8').splitlines())
            self.assertLessEqual(n, SOURCE_MAX, '%s : %d lignes (plafond %d)' % (name, n, SOURCE_MAX))

    def test_parts_not_imported(self):
        stems = [p[:-3] for p in PARTS]
        for path in sorted((ROOT / 'tools').rglob('*.py')):
            if path.name == Path(__file__).name or SKIP_DIRS & set(path.parts):
                continue
            for node in ast.walk(ast.parse(path.read_bytes())):
                mods = ([a.name for a in node.names] if isinstance(node, ast.Import)
                        else [node.module or ''] if isinstance(node, ast.ImportFrom) else [])
                for mod in mods:
                    self.assertNotIn(mod.split('.')[0], stems, '%s importe la part %s' % (path.relative_to(ROOT), mod))


if __name__ == '__main__':
    unittest.main()
