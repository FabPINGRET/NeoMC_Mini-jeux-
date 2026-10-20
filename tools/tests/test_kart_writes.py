"""Kart : chaque write('<nom>', ...) littéral des générateurs correspond à un fichier de data/mg/function/kart/tN/, et plus aucun mm_*.
Lancer depuis la racine du dépôt : python -m unittest discover -s tools/tests -v   (la racine est dérivée de ce fichier).
"""
import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KART = ROOT / 'tools' / 'kart'
# circuit -> sources qui l'écrivent (façade + parts)
SOURCES = {
    't1': ('gen_kart.py',),
    't2': ('gen_kart2.py',) + tuple(sorted(p.name for p in KART.glob('kart2_*_part.py'))),
    't3': ('gen_arena.py',),
}


def literal_writes(path):
    """Noms (littéraux) passés en premier argument à write(...) ; les f-strings sont ignorées."""
    names = set()
    for n in ast.walk(ast.parse(path.read_text(encoding='utf-8'))):
        if not (isinstance(n, ast.Call) and getattr(n.func, 'id', None) == 'write' and n.args):
            continue
        a = n.args[0]
        if isinstance(a, ast.Constant) and isinstance(a.value, str):
            names.add(a.value)
        elif isinstance(a, ast.JoinedStr) and a.values and isinstance(a.values[0], ast.Constant) \
                and isinstance(a.values[0].value, str) and a.values[0].value.startswith('mm_'):
            names.add(a.values[0].value)    # f-string commençant par mm_ : attrapée par le test « plus de minimap »
    return sorted(names)


class KartWrites(unittest.TestCase):
    def test_writes_match_data(self):
        for tn, sources in SOURCES.items():
            names = sorted({w for s in sources for w in literal_writes(KART / s)})
            self.assertTrue(names, '%s : aucun write() littéral trouvé' % tn)
            for name in names:
                self.assertFalse(name.startswith('mm_'), '%s : write(%r) : la minimap n\'est plus générée' % (tn, name))
                f = ROOT / 'data' / 'mg' / 'function' / 'kart' / tn / (name + '.mcfunction')
                self.assertTrue(f.is_file(), '%s : write(%r) sans fichier %s' % (tn, name, f.relative_to(ROOT)))


if __name__ == '__main__':
    unittest.main()
