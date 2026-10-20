"""Kart, Royaume Koopa : la façade tools/kart/gen_kart2.py exécute ses 5 parts (exec) dans l'ordre d'origine du script.
Lancer depuis la racine du dépôt : python -m unittest discover -s tools/tests -v   (la racine est dérivée de ce fichier).
"""
import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KART = ROOT / 'tools' / 'kart'
FACADE = KART / 'gen_kart2.py'
SOURCE_MAX = 500                                        # plafond dur (cible 300)
# ordre d'exécution : tracé, terrain, décor, lieux, dangers (random.seed(62) : flux global, l'ordre fait la sortie)
PARTS = ('kart2_track_part.py', 'kart2_terrain_part.py', 'kart2_deco_part.py', 'kart2_places_part.py', 'kart2_hazards_part.py')


def exec_targets(path):
    """Noms de fichier des exec(open(os.path.join(..., 'x.py'), ...).read()) de path, dans l'ordre du source."""
    found = []
    for node in ast.walk(ast.parse(path.read_text(encoding='utf-8'))):
        if not (isinstance(node, ast.Call) and getattr(node.func, 'id', None) == 'exec' and node.args):
            continue
        opened = node.args[0].func.value if isinstance(node.args[0], ast.Call) and isinstance(node.args[0].func, ast.Attribute) else None
        if not (isinstance(opened, ast.Call) and getattr(opened.func, 'id', None) == 'open' and opened.args):
            continue
        join = opened.args[0]
        if isinstance(join, ast.Call) and join.args and isinstance(join.args[-1], ast.Constant):
            found.append((node.lineno, join.args[-1].value))
    return [name for _, name in sorted(found)]


class K2Parts(unittest.TestCase):
    def test_facade_execs_parts_in_order(self):
        self.assertEqual(tuple(exec_targets(FACADE)), PARTS)

    def test_sources_size(self):
        for p in (FACADE,) + tuple(KART / n for n in PARTS):
            n = len(p.read_text(encoding='utf-8').splitlines())
            self.assertLessEqual(n, SOURCE_MAX, '%s : %d lignes (plafond %d)' % (p.name, n, SOURCE_MAX))

    def test_parts_not_imported(self):
        stems = {Path(n).stem for n in PARTS}
        for p in sorted((ROOT / 'tools').rglob('*.py')):
            for node in ast.walk(ast.parse(p.read_text(encoding='utf-8'))):
                if isinstance(node, ast.Import):
                    names = [a.name.split('.')[-1] for a in node.names]
                elif isinstance(node, ast.ImportFrom):
                    names = [(node.module or '').split('.')[-1]] + [a.name for a in node.names]
                else:
                    continue
                bad = stems & set(names)
                self.assertFalse(bad, '%s importe la part %s' % (p.relative_to(ROOT), ', '.join(sorted(bad))))

    def test_seed_before_first_exec(self):
        """random.seed(62) est un flux global : il doit être posé avant que la première part ne tire un nombre."""
        tree = ast.parse(FACADE.read_text(encoding='utf-8'))
        seeds = [n.lineno for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                 and n.func.attr == 'seed' and getattr(n.func.value, 'id', None) == 'random']
        execs = [n.lineno for n in ast.walk(tree) if isinstance(n, ast.Call) and getattr(n.func, 'id', None) == 'exec']
        self.assertTrue(seeds and execs, 'random.seed ou exec introuvable dans la façade')
        self.assertLess(min(seeds), min(execs))


if __name__ == '__main__':
    unittest.main()
