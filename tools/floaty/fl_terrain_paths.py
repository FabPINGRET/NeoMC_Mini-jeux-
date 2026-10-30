"""Garde-fous de chemins de build_terrain : où le zip peut être écrit, quelle racine de dépôt est acceptée, trampolines présents.

    out = fl_terrain_paths.check_out(out_dir, map_dir, repo, ...)   # --out : ni dans la carte, ni dans un dépôt
    repo = fl_terrain_paths.check_root(root, map_dir, out)          # --root : un vrai dépôt NeoMC, hors carte et hors --out
    fl_terrain_paths.missing_trampolines(repo, cibles)              # cibles `schedule function` sans trampoline floaty:sched/...

Tout est refusé par fl_terrain_paths.PathError (message clair, rien n'est écrit) ; build_terrain la convertit en TerrainError.
"""
from pathlib import Path

import fl_rewrite

MARKER = Path('data') / 'mg' / 'function' / 'core' / 'load.mcfunction'      # présent dans tout dépôt NeoMC


class PathError(Exception):
    """Chemin refusé."""


def _inside(path, folder):
    return path == folder or folder in path.parents


def check_out(out, map_dir, *repos):
    """--out -> chemin résolu ; PathError s'il est dans la carte, dans un des dépôts (repos), ou si c'est un fichier."""
    out = Path(out).resolve()
    for forbidden, what in [(Path(map_dir).resolve(), 'la carte')] + [(Path(r).resolve(), 'le depot') for r in repos]:
        if _inside(out, forbidden):
            raise PathError(f'--out ({out}) ne doit pas etre dans {what} ({forbidden}) : choisir un dossier hors depot')
    if out.exists() and not out.is_dir():
        raise PathError(f'--out ({out}) est un fichier : choisir un dossier')
    return out


def check_root(root, map_dir, out):
    """--root -> chemin résolu ; PathError s'il est dans la carte ou dans --out (le build y écrit terrain_sched.txt : jamais dans ses
    propres sorties, ni dans les données lues), ou s'il n'a pas `data/mg/function/core/load.mcfunction` (pas un dépôt NeoMC)."""
    root = Path(root).resolve()
    for folder, what in ((Path(map_dir).resolve(), 'la carte'), (Path(out).resolve(), '--out')):
        if _inside(root, folder):
            raise PathError(f'--root ({root}) ne doit pas etre dans {what} ({folder}) : indiquer la racine du depot NeoMC')
    if not (root / MARKER).is_file():
        raise PathError(f'--root ({root}) n\'est pas un depot NeoMC : {MARKER.as_posix()} introuvable')
    return root


def missing_trampolines(repo, targets):
    """Cibles schedule dont le trampoline `data/floaty/function/sched/<ns>/<chemin>.mcfunction` n'existe pas sous repo."""
    fn = Path(repo) / 'data' / 'floaty' / 'function'
    return [t for t in targets if not (fn / (fl_rewrite.sched_name(t).split(':', 1)[1] + '.mcfunction')).is_file()]
