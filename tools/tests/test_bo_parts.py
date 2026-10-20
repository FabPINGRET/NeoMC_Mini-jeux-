"""Bombardier : tools/arcade/gen_bomber.py execute ses 4 parts (bomber_*.py) dans l'ordre d'origine, sans jamais les importer.
Lancer depuis la racine du depot : python -m unittest discover -s tools/tests -v   (la racine est derivee de ce fichier).
"""
import ast
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCADE = ROOT / 'tools' / 'arcade'
FACADE = ARCADE / 'gen_bomber.py'
SOURCE_MAX = 500                                        # plafond dur (cible 300)
PARTS = ('bomber_city.py', 'bomber_park.py', 'bomber_export.py', 'bomber_game.py')


def exec_parts(path):
    """Noms de fichiers des appels exec(open(os.path.join(..., 'x.py'), ...).read()) de la facade, dans l'ordre du source."""
    found = []
    for node in ast.walk(ast.parse(path.read_text(encoding='utf-8'))):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'exec' and node.args):
            continue
        subs = list(ast.walk(node.args[0]))
        if not any(isinstance(s, ast.Name) and s.id == '__file__' for s in subs):     # ignore les exec qui ne lisent pas un fichier voisin
            continue
        for sub in subs:
            if isinstance(sub, ast.Constant) and isinstance(sub.value, str) and sub.value.endswith('.py'):
                found.append((node.lineno, node.col_offset, sub.value))
    return [name for _, _, name in sorted(found)]


class BomberParts(unittest.TestCase):
    def test_facade_execs_parts_in_order(self):
        self.assertEqual(tuple(exec_parts(FACADE)), PARTS)

    def test_sources_size(self):
        for p in [FACADE] + [ARCADE / n for n in PARTS]:
            n = len(p.read_text(encoding='utf-8').splitlines())
            self.assertLessEqual(n, SOURCE_MAX, '%s : %d lignes (plafond %d)' % (p.name, n, SOURCE_MAX))

    def test_parts_not_imported(self):
        pat = re.compile(r'^\s*(?:import|from)\s+(?:%s)\b' % '|'.join(re.escape(n[:-3]) for n in PARTS), re.M)
        for p in sorted((ROOT / 'tools').rglob('*.py')):
            self.assertIsNone(pat.search(p.read_text(encoding='utf-8')), '%s importe une part de gen_bomber' % p.relative_to(ROOT))


if __name__ == '__main__':
    unittest.main()
