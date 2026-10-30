"""Aucune fonction `data/mg/function/**` sans appelant : toute fonction doit etre referencee (function/schedule, tag #mg:, macro mg:prefixe$(...)),
ou figurer dans ALLOWED (commandes a taper par un admin/OP, documentees dans README.md).
Lancer depuis n'importe ou : python -m unittest discover -s tools/tests -v   (la racine du depot est derivee de ce fichier).
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FUNC = ROOT / 'data' / 'mg' / 'function'
REF = re.compile(r'mg:([a-z0-9_./-]+)')
MACRO = re.compile(r'mg:([a-z0-9_./-]+)\$\(')
# argument de macro lancee par `function mg:$(f)` (ex. lobby/theme/spot) ; avec « / » : les noms de familles (f:"lab") ne masquent pas une fonction racine
MACRO_ARG = re.compile(r'\bf:"([a-z0-9_.-]+/[a-z0-9_./-]+)"')

# Points d'entree admin : noms exacts, ou prefixe de dossier se terminant par « / » (couvre aussi la fonction racine `xxx`).
ALLOWED = (
    'installer', 'desinstaller', 'load', 'tick', 'rp_on', 'rp_off',    # installation, rechargement, resource pack (README.md)
    'menu', 'nettoyer_plateforme',                                      # README.md l.214/255/353 et l.210/251 : commandes OP
    'bb/clear_old', 'duel/build_all', 'foot/build_start', 'kart/build_koopa',   # README.md l.314, 83, 313, 17, 29
    'lobby/fish/build', 'parkour/build', 'party/build', 'plot/build', 'pvpc/build_start',              # README.md l.18, 14, 31, 33/315, 16
    'setup_lobby',                                                      # README.md : reconstruit seulement le spawn (OP)
    'sky/wipe',                                                         # OP : efface le decor Elytra avant reconstruction
    'setup/', 'admin/', 'diag/', 'perf/', 'aide/',                      # menus et outils d'administration
)


def functions():
    """Noms (sans extension) de toutes les fonctions du datapack."""
    return {p.relative_to(FUNC).with_suffix('').as_posix() for p in FUNC.rglob('*.mcfunction')}


def scanned_files():
    """Fichiers ou chercher des references : data/ (.mcfunction, .json) et tools/**/*.py (hors ce test, qui cite des noms en exemple)."""
    data = [p for p in (ROOT / 'data').rglob('*') if p.suffix in ('.mcfunction', '.json')]
    return data + [p for p in (ROOT / 'tools').rglob('*.py') if p.resolve() != Path(__file__).resolve()]


def own_name(path):
    """Nom de la fonction que ce fichier definit (None pour un .json ou un .py) : ses auto-citations ne comptent pas comme appel."""
    if path.suffix == '.mcfunction' and FUNC in path.parents:
        return path.relative_to(FUNC).with_suffix('').as_posix()
    return None


def references():
    """(noms references, prefixes de macro) lus dans les sources, plus les `values` des tags de fonctions."""
    refs, prefixes = set(), set()
    for p in scanned_files():
        text = p.read_text(encoding='utf-8', errors='replace')
        refs.update((set(REF.findall(text)) | set(MACRO_ARG.findall(text))) - {own_name(p)})
        prefixes.update(MACRO.findall(text))
    for tag in (ROOT / 'data' / 'mg' / 'tags' / 'function').glob('*.json'):
        for value in json.loads(tag.read_text(encoding='utf-8')).get('values', []):
            value = value['id'] if isinstance(value, dict) else value
            refs.add(value.removeprefix('mg:'))
    return refs, prefixes


def allowed(name):
    return any(name == a or (a.endswith('/') and (name.startswith(a) or name == a[:-1])) for a in ALLOWED)


def orphans():
    refs, prefixes = references()
    return sorted(n for n in functions()
                  if n not in refs and not any(n.startswith(p) for p in prefixes) and not allowed(n))


class NoOrphanFunction(unittest.TestCase):
    def test_functions_found(self):
        self.assertTrue(functions(), f'aucune fonction dans {FUNC} : lancer les generateurs (README.md, Ordre des generateurs)')

    def test_no_orphan(self):
        found = orphans()
        self.assertFalse(found, f'{len(found)} fonction(s) jamais referencee(s) : retirer du generateur, ou ajouter a ALLOWED si point d\'entree admin :\n  '
                         + '\n  '.join(found))


if __name__ == '__main__':
    unittest.main()
