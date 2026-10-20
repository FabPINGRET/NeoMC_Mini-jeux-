"""Hygiène des générateurs (tools/**/*.py) : cliquet de taille et interdiction de recopier les helpers de tools/lib/mcfn.py.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).

- OVERSIZE : les fichiers déjà au-dessus du plafond dur (500 lignes) avec leur taille actuelle. Un fichier hors liste doit rester
  ≤ 500, un fichier listé ne doit pas grossir, et un fichier redescendu à ≤ 500 doit être retiré de la liste.
- ALLOWED : les `def` de niveau module (hors lib/ et tests/) qui portent un nom de helper de mcfn.py (patch, replace, sub, go_range, js,
  ou w / wr / _write quand leur corps appelle `open`). Tout autre générateur passe par mcfn ; ajouter une copie fait échouer le test.
  Le scan ne voit que les `def` de niveau module : ni les lambdas, ni les `def` sous `if` / `try`.
"""
import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / 'tools'
CAP = 500
SKIP_DIRS = {'claude-bridge', 'tests', '__pycache__'}      # claude-bridge : pas du Python ; tests : ce dossier
HELPERS = {'patch', 'replace', 'sub', 'go_range', 'js', 'drop_lines'}
WRITERS = {'w', 'wr', '_write'}

OVERSIZE = {
    'tools/arcade/gen_bowling.py': 739,
    'tools/arcade/gen_chameleon.py': 579,
    'tools/arcade/gen_golf.py': 887,
    'tools/arcade/gen_tennis.py': 613,
    'tools/arcade/gen_villa.py': 516,
    'tools/arcade/gen_zombies.py': 815,
    'tools/arcade/ol_quest.py': 847,
    'tools/arcade/ol_world.py': 620,
    'tools/arcade/tv_dinos.py': 540,
    'tools/arcade/tv_rpg.py': 938,
    'tools/arcade/tv_structs.py': 723,
    'tools/arcade/tv_world.py': 843,
    'tools/bedwars/gen_maps.py': 830,
    'tools/dropper/gen_dropper_adv.py': 750,
    'tools/kart/gen_kart.py': 530,
    'tools/kart/write_kart.py': 754,
    'tools/mini-party/gen_board.py': 924,
    'tools/tnttag/gen_maps.py': 983,
}

ALLOWED = {
    ('tools/arcade/common.py', 'patch'),         # traduit les lignes (_tx) puis délègue à mcfn.Fn.patch
    ('tools/dropper/gen_dropper_adv.py', 'wr'),
    ('tools/elyrace/wire_elyrace2.py', 'go_range'),
    ('tools/kart/write_kart.py', 'wr'),
    ('tools/lobby/gen_pvpcave.py', 'w'),
    ('tools/lobby/gen_pvpcave.py', 'js'),
    ('tools/lobby/gen_pvpcave.py', 'patch'),
    ('tools/mobarena/scale_waves.py', 'w'),
    ('tools/party_pool.py', 'w'),
    ('tools/variantes/var_common.py', 'patch'),  # idempotence par sous-chaîne + paramètre count : pas celui de mcfn
}


def sources():
    """Chemin relatif (posix) → Path de chaque .py de tools/, hors claude-bridge et tests."""
    return {p.relative_to(ROOT).as_posix(): p for p in sorted(TOOLS.rglob('*.py'))
            if not (set(p.relative_to(TOOLS).parts) & SKIP_DIRS)}


def calls_open(fn):
    return any(isinstance(c, ast.Call) and getattr(c.func, 'id', None) == 'open' for c in ast.walk(fn))


def copies():
    """{(chemin, nom)} des helpers de mcfn.py redéfinis au niveau module (lib/ exclu : c'est leur maison)."""
    found = set()
    for rel, p in sources().items():
        if 'lib' in p.relative_to(TOOLS).parts:
            continue
        for node in ast.parse(p.read_bytes()).body:
            if isinstance(node, ast.FunctionDef) and (node.name in HELPERS or (node.name in WRITERS and calls_open(node))):
                found.add((rel, node.name))
    return found


def size_problems(sizes, oversize):
    """sizes {chemin: nb lignes}, oversize {chemin: plafond listé} → liste de problèmes (vide = OK)."""
    problems = []
    for rel, n in sizes.items():
        if rel not in oversize and n > CAP:
            problems.append(f'{rel} : {n} lignes (> {CAP}), hors OVERSIZE : le découper')
        elif rel in oversize and n > oversize[rel]:
            problems.append(f'{rel} : {n} lignes, plafond {oversize[rel]} (ne doit pas grossir) : extraire du code')
        elif rel in oversize and n <= CAP:
            problems.append(f'{rel} : {n} lignes (≤ {CAP}) : le retirer de OVERSIZE')
    problems += [f'{rel} : listé dans OVERSIZE mais introuvable' for rel in oversize if rel not in sizes]
    return problems


class FileSize(unittest.TestCase):
    def test_size_ratchet(self):
        sizes = {rel: len(p.read_text(encoding='utf-8').splitlines()) for rel, p in sources().items()}
        problems = size_problems(sizes, OVERSIZE)
        self.assertFalse(problems, '\n' + '\n'.join(problems))

    def test_unlisted_over_cap_is_problem(self):
        p = size_problems({'a.py': CAP + 1}, {})
        self.assertEqual(len(p), 1)
        self.assertIn('hors OVERSIZE', p[0])

    def test_listed_growing_is_problem(self):
        p = size_problems({'a.py': 701}, {'a.py': 700})
        self.assertEqual(len(p), 1)
        self.assertIn('ne doit pas grossir', p[0])

    def test_listed_back_under_cap_is_problem(self):
        p = size_problems({'a.py': CAP}, {'a.py': 700})
        self.assertEqual(len(p), 1)
        self.assertIn('retirer de OVERSIZE', p[0])

    def test_no_problem_cases(self):
        self.assertEqual(size_problems({'a.py': CAP, 'b.py': 700, 'c.py': 650}, {'b.py': 700, 'c.py': 700}), [])

    def test_listed_missing_is_problem(self):
        self.assertEqual(len(size_problems({}, {'gone.py': 600})), 1)


class NoCopiedHelpers(unittest.TestCase):
    def test_helpers_only_in_lib(self):
        found = copies()
        added = sorted(found - ALLOWED)
        gone = sorted(ALLOWED - found)
        msg = ''
        if added:
            msg += '\nhelper recopié (utiliser tools/lib/mcfn.py) : ' + ', '.join(f'{r}:{n}' for r, n in added)
        if gone:
            msg += '\nretirer de ALLOWED (plus défini) : ' + ', '.join(f'{r}:{n}' for r, n in gone)
        self.assertFalse(msg, msg)


if __name__ == '__main__':
    unittest.main()
