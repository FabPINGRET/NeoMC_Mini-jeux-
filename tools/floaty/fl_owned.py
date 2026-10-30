"""Propriété des fichiers du générateur floaty : manifeste tools/floaty/owned.txt et garde-fous AVANT toute suppression.

Le manifeste liste ce que gen_floaty a posé et peut donc effacer à la relance :
    data/<ns>/                     un dossier d'espace de noms de la carte (effacé en entier)
    data/minecraft/<chemin>.json   un fichier posé sous minecraft (tags hb_*, trim_pattern, recettes, biomes), effacé un par un
Un nom d'espace de noms valide commence et finit par [a-z0-9_-] (jamais « . » ni « .. » ; pas de point final : Windows le retire, « mg. »
désignerait « mg »), et reste directement sous data/ une fois résolu (même nom). Un fichier minecraft se résout sous data/minecraft/ à
l'identique (pas de « .. », de point ou d'espace final).
En plus, toujours possédés (chemins fixes, hors manifeste) : FIXED_DIRS et FIXED_FILES — dans data/floaty ce sont UNIQUEMENT
function/sched/ (trampolines de schedule), function/map/ (tick, load réécrits de la carte), function/install et function/uninstall ;
et data/mg/dimension/floaty.json. Tout autre fichier de data/floaty (le câblage de L3, par exemple) n'est jamais effacé.
Jamais effacés : data/mg (sauf dimension/floaty.json), data/minecraft hors manifeste, tout dossier data/<ns> absent du manifeste.

Premier passage (manifeste absent ou incomplet, sortie déjà présente mais non commitée) : `gen_floaty.py --adopt` déclare possédés
les dossiers data/<ns> et les fichiers data/minecraft que CE passage va écrire et qui existent déjà. Sans --adopt, un tel dossier /
fichier non listé fait refuser la relance, avant toute suppression. Avec --adopt, git est consulté (git ls-files, cwd = racine) : un
chemin suivi par git est refusé (il serait versionné pour autre chose), et sans git --adopt est refusé. Le manifeste réécrit ensuite
ne liste que ce que le passage produit.
"""
import re
import shutil
import subprocess
from pathlib import Path

OWNED = Path('tools') / 'floaty' / 'owned.txt'
PROTECTED = {'mg', 'minecraft', 'floaty'}          # jamais vidés ni écrasés comme espace de noms de la carte
NS = re.compile(r'[a-z0-9_-](?:[a-z0-9_.-]*[a-z0-9_-])?')     # ni « . » ni espace en fin : Windows les retire (« mg. » désignerait « mg »)
_DIR = re.compile(r'data/(' + NS.pattern + r')/')
FIXED_DIRS = ('data/floaty/function/sched', 'data/floaty/function/map')
FIXED_FILES = ('data/floaty/function/install.mcfunction', 'data/floaty/function/uninstall.mcfunction', 'data/mg/dimension/floaty.json')


def load(root):
    """(espaces de noms, fichiers minecraft) du manifeste ; SystemExit si une ligne est invalide."""
    dirs, files = set(), set()
    p = Path(root) / OWNED
    for l in (p.read_text(encoding='utf-8').split('\n') if p.exists() else []):
        l = l.strip()
        if not l:
            continue
        m = _DIR.fullmatch(l)
        if m:
            dirs.add(m.group(1))
        elif l.startswith('data/minecraft/') and l.endswith('.json'):     # un fichier .json (jamais un dossier ni « data/minecraft/ »)
            files.add(l)
        else:
            raise SystemExit(f'{OWNED} : ligne invalide {l!r}')
    return dirs, files


def tracked(root, paths):
    """Ceux des chemins (posix, relatifs à root) que git suit (git ls-files, cwd = root). SystemExit si git est indisponible."""
    if not paths:
        return []
    try:
        r = subprocess.run(['git', '--literal-pathspecs', 'ls-files', '-z', '--'] + list(paths), cwd=root, capture_output=True)
    except OSError as e:
        raise SystemExit(f'--adopt refusé : git est indisponible ({e}), impossible de vérifier que les chemins ne sont pas versionnés')
    if r.returncode != 0:
        raise SystemExit('--adopt refusé : git ls-files a échoué (dépôt git absent ?) : ' + r.stderr.decode('utf-8', errors='replace').strip())
    return [p for p in r.stdout.decode('utf-8').split('\0') if p]


def check(root, namespaces, mc_files, adopt=False):
    """Tous les garde-fous, avant la moindre suppression. -> (espaces de noms à vider, fichiers minecraft à effacer)."""
    root = Path(root)
    owned_ns, owned_files = load(root)
    bad = [f'espace de noms protégé : {ns}' for ns in sorted(set(namespaces) | owned_ns) if ns in PROTECTED]
    bad += [f'data/{ns}/ existe et n\'est pas au manifeste (--adopt au premier passage)' for ns in namespaces
            if ns not in PROTECTED and ns not in owned_ns and not adopt and (root / 'data' / ns).exists()]
    bad += [f'{rel} existe déjà et n\'est pas au manifeste (--adopt au premier passage)' for rel in mc_files
            if (root / rel).exists() and rel not in owned_files and not adopt]
    data, mc = (root / 'data').resolve(), (root / 'data' / 'minecraft').resolve()
    for ns in sorted(owned_ns | set(namespaces)):
        target = (root / 'data' / ns).resolve()
        if not NS.fullmatch(ns) or target.parent != data or target.name != ns:       # name : « mg. » se résout en « mg » sous Windows
            bad.append(f'data/{ns}/ : pas un dossier d\'espace de noms directement sous data/')
    for rel in sorted(owned_files | set(mc_files)):
        try:
            same = (root / rel).resolve().relative_to(mc).as_posix() == rel[len('data/minecraft/'):]
        except ValueError:
            same = False
        if not same:
            bad.append(f'{rel} : hors de data/minecraft ou chemin non canonique (« .. », point ou espace final)')
    existing = {rel for rel in mc_files if adopt and (root / rel).exists()}
    if adopt and not bad:
        candidates = [f'data/{ns}' for ns in namespaces if ns not in owned_ns and (root / 'data' / ns).exists()] + sorted(existing - owned_files)
        bad += [f'{p} est suivi par git : --adopt refusé (il serait effacé puis réécrit)' for p in tracked(root, candidates)]
    if bad:
        raise SystemExit('abandon (rien n\'a été supprimé) :\n  ' + '\n  '.join(bad))
    return sorted(owned_ns | set(namespaces)), sorted(owned_files | existing)


def clean(root, namespaces, files):
    """Efface les dossiers et fichiers vérifiés par check, plus FIXED_DIRS / FIXED_FILES (rien d'autre dans data/floaty)."""
    root = Path(root)
    for p in [root / 'data' / ns for ns in namespaces] + [root / d for d in FIXED_DIRS]:
        if p.exists():                                  # pas d'ignore_errors : un dossier qu'on n'a pas pu vider doit faire échouer le run
            shutil.rmtree(p)
    for rel in tuple(files) + FIXED_FILES:
        (root / rel).unlink(missing_ok=True)


def save(root, namespaces, mc_files):
    p = Path(root) / OWNED
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join([f'data/{ns}/' for ns in sorted(namespaces)] + sorted(mc_files)) + '\n')
