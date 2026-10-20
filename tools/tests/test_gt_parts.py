"""Neo GTA : la façade tools/arcade/gen_gta.py exécute (exec) ses parts dans l'ordre, sans jamais les importer.
Lancer depuis la racine du dépôt : python -m unittest discover -s tools/tests -v   (la racine est dérivée de ce fichier).
"""
import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCADE = ROOT / 'tools' / 'arcade'
FACADE = ARCADE / 'gen_gta.py'
SKIP_DIRS = {'claude-bridge', '__pycache__'}            # comme test_tools_hygiene.py : claude-bridge n'est pas du Python
SOURCE_MAX = 500                                       # plafond dur (cible 300)
# ordre d'exécution : l'ordre des w() / random.* / mutations de globals de l'ancien gen_gta.py (gta_plus puis gta_city à l'endroit de l'ancien exec)
PARTS = ('gta_world.py', 'gta_session.py', 'gta_police.py', 'gta_drive.py', 'gta_heists.py', 'gta_plus.py', 'gta_city.py')


def facade_execs():
    """Noms de fichier des exec(open(os.path.join(..., 'x.py'), ...).read()) de la façade, dans l'ordre du source."""
    found = []
    for node in ast.walk(ast.parse(FACADE.read_bytes())):
        if not (isinstance(node, ast.Call) and getattr(node.func, 'id', None) == 'exec' and node.args):
            continue
        read = node.args[0]
        if not (isinstance(read, ast.Call) and getattr(read.func, 'attr', None) == 'read'):
            continue
        opened = read.func.value
        if not (isinstance(opened, ast.Call) and getattr(opened.func, 'id', None) == 'open' and opened.args):
            continue
        joined = opened.args[0]
        if (isinstance(joined, ast.Call) and getattr(joined.func, 'attr', None) == 'join' and joined.args
                and isinstance(joined.args[-1], ast.Constant) and isinstance(joined.args[-1].value, str)
                and joined.args[-1].value.endswith('.py')):
            found.append((node.lineno, node.col_offset, joined.args[-1].value))
    return [name for _, _, name in sorted(found)]


class GtParts(unittest.TestCase):
    def test_facade_execs_parts_in_order(self):
        self.assertEqual(tuple(facade_execs()), PARTS)

    def test_sources_size(self):
        for name in ('gen_gta.py',) + PARTS:
            n = len((ARCADE / name).read_text(encoding='utf-8').splitlines())
            self.assertLessEqual(n, SOURCE_MAX, '%s : %d lignes (plafond %d)' % (name, n, SOURCE_MAX))

    def test_parts_not_imported(self):
        modules = {Path(p).stem for p in PARTS}
        for path in sorted((ROOT / 'tools').rglob('*.py')):
            if set(path.relative_to(ROOT / 'tools').parts) & SKIP_DIRS:
                continue
            for node in ast.walk(ast.parse(path.read_bytes())):
                if isinstance(node, ast.Import):
                    names = {a.name.split('.')[0] for a in node.names}
                elif isinstance(node, ast.ImportFrom) and node.module:
                    names = {node.module.split('.')[0]}
                else:
                    continue
                self.assertFalse(names & modules, '%s importe une part de gen_gta : %s' % (path.relative_to(ROOT), sorted(names & modules)))


if __name__ == '__main__':
    unittest.main()
