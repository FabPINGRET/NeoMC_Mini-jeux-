"""Spawn du lobby : tools/lobby/gen_lobby.py (façade) exécute ses parts spawn_*.py (exec) dans l'ordre du fichier d'origine.
Lancer depuis la racine du dépôt : python -m unittest discover -s tools/tests -v   (la racine est dérivée de ce fichier).
"""
import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOBBY = ROOT / 'tools' / 'lobby'
FACADE = LOBBY / 'gen_lobby.py'
SKIP_DIRS = {'claude-bridge', '__pycache__'}            # comme test_tools_hygiene (claude-bridge : pas du Python)
SOURCE_MAX = 500                                       # plafond dur (cible 300)
PARTS = ('spawn_plaza.py', 'spawn_track.py', 'spawn_nature.py', 'spawn_deco.py', 'spawn_kart.py', 'spawn_secrets.py')


def exec_targets(tree):
    """Noms de fichiers des exec(open(os.path.join(..., 'x.py'), ...).read()) de l'arbre, dans l'ordre du source."""
    found = []
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and getattr(node.func, 'id', None) == 'exec' and node.args):
            continue
        sub = list(ast.walk(node))
        if not any(isinstance(n, ast.Name) and n.id == '__file__' for n in sub):
            continue
        for lit in sub:
            if isinstance(lit, ast.Constant) and isinstance(lit.value, str) and lit.value.endswith('.py'):
                found.append((node.lineno, node.col_offset, lit.value))
    return [name for _, _, name in sorted(found)]


class LobbyParts(unittest.TestCase):
    def test_facade_execs_parts_in_order(self):
        tree = ast.parse(FACADE.read_text(encoding='utf-8'))
        self.assertEqual(tuple(exec_targets(tree)), PARTS)

    def test_sources_size(self):
        for name in ('gen_lobby.py',) + PARTS:
            n = len((LOBBY / name).read_text(encoding='utf-8').splitlines())
            self.assertLessEqual(n, SOURCE_MAX, '%s : %d lignes (plafond %d)' % (name, n, SOURCE_MAX))

    def test_parts_not_imported(self):
        """Une part n'a de sens que dans les globals de la façade : aucun `import spawn_x` / `from spawn_x` dans tools/."""
        stems = {p[:-3] for p in PARTS}
        for p in sorted((ROOT / 'tools').rglob('*.py')):
            if set(p.relative_to(ROOT / 'tools').parts) & SKIP_DIRS:
                continue
            for node in ast.walk(ast.parse(p.read_bytes())):
                if isinstance(node, ast.Import):
                    mods = [a.name for a in node.names]
                elif isinstance(node, ast.ImportFrom):
                    mods = [node.module or '']
                else:
                    continue
                for mod in mods:
                    self.assertNotIn(mod.split('.')[0], stems, '%s importe la part %s' % (p.relative_to(ROOT).as_posix(), mod))


if __name__ == '__main__':
    unittest.main()
