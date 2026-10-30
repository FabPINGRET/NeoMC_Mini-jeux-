"""Zip du terrain de « Scourge of the Floaty Isles » à copier À LA MAIN dans la dimension mg:floaty du serveur.

    PYTHONUTF8=1 python tools/floaty/build_terrain.py --map <dossier de la carte> --out <dossier de sortie> [--dimension minecraft:overworld]
                                                      [--no-rewrite] [--root <racine du dépôt>]

La carte (hors dépôt) est lue en LECTURE SEULE. Le zip (floaty_terrain.zip) contient exactement ce qui va dans
`<monde du serveur>/dimensions/mg/floaty/` : region/ (+ entities/ et poi/ s'ils existent) de la dimension de la carte qui porte le
terrain, plus un fichier VERSION à la racine (dimension d'origine, nom et date de la carte, nombre de fichiers, sha256 du CONTENU : de chaque
fichier, dans l'ordre trié, « chemin NUL taille NUL octets »). Reproductible : ordre trié, dates et attributs fixes, VERSION en dernier ->
deux builds de la même carte donnent le même zip, octet pour octet (même zlib).
RÉÉCRITURE (par défaut) : en une passe par fichier (scan + réécriture, fl_terrain_rw) les commandes des blocs de commande, minecarts et
panneaux sont cantonnées à mg:floaty comme celles des fonctions (L1) : sélecteurs bornés, say -> tellraw, schedule -> trampoline, et
retirées (NOOP) si elles changeraient l'état du serveur entier (gamerule, time, weather... : fl_terrain_cmd), si elles visent une AUTRE
dimension que celle de la carte (`in <dimension source>` devient `in mg:floaty`) ou si ce sont des `advancement ... everything` (raison
`eclate`). Un chunk à commandes que le lecteur NBT strict ne lit pas reste tel quel : avertissement sur stderr + `illisible_cmd` du rapport.
Le zip et le rapport d'un build précédent sont supprimés dès que --out est accepté : aucun échec ne laisse un ancien zip. Les fichiers poi/
et les fichiers sans commande à changer sont recopiés tels quels. VERSION 2 : + `source-sha256` (sha256 des octets de la carte, même format que
content-sha256), `command-rewrite: on`, `rewritten-commands: N` (commandes modifiées ou remplacées par NOOP). `--no-rewrite` : aucune
réécriture, zip identique octet pour octet à celui de L5 / L6a (VERSION 1 : sans ces lignes). Les cibles `schedule function` des commandes
réécrites sont écrites triées dans <racine du dépôt>/tools/floaty/terrain_sched.txt (SEULE écriture hors --out ; relue par gen_floaty, qui
génère les trampolines floaty:sched/...). Ordre : build (écrit la liste), gen_floaty (trampolines), build de nouveau (le rapport liste
les cibles encore sans trampoline). --root : un dépôt NeoMC (data/mg/function/core/load.mcfunction), ni dans la carte ni dans --out
(fl_terrain_paths ; seulement avec réécriture). À côté : floaty_terrain_report.txt, la
liste des blocs de commande et des panneaux à run_command du terrain, avant et après réécriture (fl_terrain_report). Le temps du build va
sur stderr seulement (le rapport reste déterministe).
Dimension : layout 26.x `<carte>/dimensions/<ns>/<nom>/region/*.mca` (anciens `region/`, `DIM-1/`, `DIM1/` aussi). Une seule dimension avec
des régions = retenue ; zéro ou plusieurs = erreur qui les liste (aucune devinette : choisir avec --dimension). --out : jamais dans la carte ni
dans le dépôt.
"""
import argparse
import datetime
import hashlib
import os
import sys
import time
import zipfile
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import fl_mca  # noqa: E402
import fl_nbt  # noqa: E402
import fl_terrain_paths  # noqa: E402
import fl_terrain_report  # noqa: E402
import fl_terrain_rw  # noqa: E402

SUBDIRS = ('entities', 'poi', 'region')          # ordre trié ; region/ est obligatoire
SUFFIXES = ('.mca', '.mcc')
ZIP_NAME, REPORT_NAME = 'floaty_terrain.zip', 'floaty_terrain_report.txt'
SCHED_FILE = Path('tools') / 'floaty' / 'terrain_sched.txt'      # sous la racine du dépôt : lu par gen_floaty
SCHED_HEAD = '# cibles `schedule function` des commandes du terrain : ecrit par build_terrain.py, lu par gen_floaty.py (un trampoline chacune)'
FIXED_DATE = (2026, 1, 1, 0, 0, 0)               # comme tools/resourcepack/gen_rp.py
LEGACY = {'region': 'minecraft:overworld', 'DIM-1': 'minecraft:the_nether', 'DIM1': 'minecraft:the_end'}
SHA_MARK, SRC_MARK, RW_MARK = '@@SHA256@@', '@@SRC256@@', '@@REWRITTEN@@'


class TerrainError(Exception):
    """Entrée inutilisable : message clair, rien n'est écrit."""


def _has_regions(d):
    r = d / 'region'
    return r.is_dir() and any(p.suffix == '.mca' for p in r.iterdir())


def find_dimensions(map_dir):
    """Carte -> {id de dimension: dossier} de chaque dimension qui a au moins un .mca sous region/."""
    map_dir, out = Path(map_dir), {}
    dims = map_dir / 'dimensions'
    for ns in sorted(dims.iterdir()) if dims.is_dir() else []:
        for d in sorted(ns.iterdir()) if ns.is_dir() else []:
            if _has_regions(d):
                out[f'{ns.name}:{d.name}'] = d
    for sub, dim_id in LEGACY.items():
        d = map_dir if sub == 'region' else map_dir / sub
        if _has_regions(d) and dim_id not in out:
            out[dim_id] = d
    return out


def pick_dimension(dims, wanted, map_dir):
    """-> (id, dossier). wanted = --dimension ou None ; ambiguïté ou absence = TerrainError (liste des dimensions trouvées)."""
    def listing():
        return ', '.join(f'{k} ({sum(1 for _ in (v / "region").glob("*.mca"))} regions)' for k, v in dims.items())
    if wanted:
        if wanted not in dims:
            raise TerrainError(f'dimension {wanted} introuvable sous {map_dir} (avec des regions : {listing() or "aucune"})')
        return wanted, dims[wanted]
    if not dims:
        raise TerrainError(f'aucune dimension avec des regions (.mca) sous {map_dir} (cherche dimensions/<ns>/<nom>/region, region/, DIM-1/, DIM1/)')
    if len(dims) > 1:
        raise TerrainError(f'plusieurs dimensions portent du terrain : {listing()} - pas de devinette, choisir avec --dimension <id>')
    return next(iter(dims.items()))


def collect(dim_dir):
    """Dossier de dimension -> [(nom dans le zip, chemin)] trié : region/, entities/, poi/ (fichiers .mca / .mcc uniquement)."""
    files = []
    for sub in SUBDIRS:
        d = dim_dir / sub
        if d.is_dir():
            files += [(f'{sub}/{p.name}', p) for p in d.iterdir() if p.is_file() and p.suffix in SUFFIXES]
    return sorted(files)


def map_info(map_dir):
    """level.dat de la carte -> {name, played (ISO UTC), spawn (x, y, z), spawn_dim} ; clés absentes si illisible (jamais fatal)."""
    try:
        d = fl_nbt.load(Path(map_dir) / 'level.dat')
        d = d.get('Data', d)
        info = {'spawn': tuple(fl_nbt.spawn(d)), 'spawn_dim': d.get('spawn', {}).get('dimension')}
        if d.get('LevelName'):
            info['name'] = str(d['LevelName'])
        if isinstance(d.get('LastPlayed'), int):
            info['played'] = datetime.datetime.fromtimestamp(d['LastPlayed'] / 1000, datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        return info
    except (OSError, ValueError, EOFError, zlib.error, AttributeError, TypeError):
        return {}


def _entry(arc):
    info = zipfile.ZipInfo(arc, date_time=FIXED_DATE)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3                       # unix quel que soit l'OS qui construit (sinon l'en-tête diffère)
    info.external_attr = 0o644 << 16
    return info


def write_zip(zpath, files, header, transform=None):
    """Écrit le zip (fichier .part puis renommage) ; -> (sha256 du contenu écrit, sha256 des octets source : même format, calculé pendant
    la même lecture). Un fichier est lu en entier une fois ; transform(arc, octets) -> octets à écrire (les mêmes si rien ne change).
    header(sha, source_sha) -> texte du VERSION, écrit en dernier."""
    h, hs, tmp = hashlib.sha256(), hashlib.sha256(), Path(str(zpath) + '.part')
    try:
        with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zf:
            for arc, p in files:
                size = p.stat().st_size
                data = p.read_bytes()
                if len(data) != size:
                    raise TerrainError(f'{p} a change pendant la lecture ({size} -> {len(data)} octets)')
                out = transform(arc, data) if transform else data
                hs.update(f'{arc}\0{size}\0'.encode() + data)
                h.update(f'{arc}\0{len(out)}\0'.encode() + out)
                info = _entry(arc)
                info.file_size = len(out)        # connue d'avance : zip64 décidé à l'ouverture
                with zf.open(info, 'w') as dst:
                    for i in range(0, len(out), 1 << 20):
                        dst.write(out[i:i + (1 << 20)])
            sha, src = h.hexdigest(), hs.hexdigest()
            zf.writestr(_entry('VERSION'), header(sha, src).encode('utf-8'))
        os.replace(tmp, zpath)
    except BaseException:
        tmp.unlink(missing_ok=True)              # jamais de zip partiel laissé à côté
        raise
    return sha, src


def write_report(path, text):
    """Écrit le rapport de façon atomique (fichier .part puis renommage ; .part retiré quoi qu'il arrive)."""
    tmp = Path(str(path) + '.part')
    try:
        tmp.write_text(text, encoding='utf-8', newline='\n')
        os.replace(tmp, path)
    except BaseException:
        tmp.unlink(missing_ok=True)
        raise


def file_sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while buf := f.read(1 << 20):
            h.update(buf)
    return h.hexdigest()


def version_text(dim_id, info, files, rewrite=False):
    """-> (texte du VERSION avec marqueurs de sha, nombre de régions). Sans réécriture : le VERSION 1 de L5 / L6a (zip identique) ; avec :
    VERSION 2 (source-sha256, command-rewrite, rewritten-commands, ce dernier remplacé par build)."""
    regions = sum(1 for arc, _ in files if arc.startswith('region/') and arc.endswith('.mca'))
    lines = [f'neomc-floaty-terrain {2 if rewrite else 1}', f'content-sha256: {SHA_MARK}']     # le sha n'est connu qu'après la copie
    lines += [f'source-sha256: {SRC_MARK}'] if rewrite else []
    lines += [f'source-dimension: {dim_id}']
    lines += [f'map-name: {" ".join(info["name"].split())}'] if 'name' in info else []
    lines += [f'map-last-played: {info["played"]}'] if 'played' in info else []
    lines += ['command-rewrite: on', f'rewritten-commands: {RW_MARK}'] if rewrite else []
    return '\n'.join(lines + [f'files: {len(files)}', f'regions: {regions}', '']), regions


def write_sched(repo, targets):
    """Cibles schedule (triées) -> <repo>/tools/floaty/terrain_sched.txt, sans toucher le fichier s'il est déjà à jour (LF, ASCII)."""
    path = Path(repo) / SCHED_FILE
    text = '\n'.join([SCHED_HEAD] + sorted(targets)) + '\n'
    if not path.is_file() or path.read_bytes() != text.encode('ascii'):
        path.parent.mkdir(parents=True, exist_ok=True)
        write_report(path, text)


def build(map_dir, out_dir, dimension=None, progress=None, rewrite=True, pack_root=None):
    """Zip + rapport. -> dict (dim, zip, report, sha, source_sha, zip_sha, files, regions, finds, after, stats, pending, build_s...).
    rewrite : voir l'en-tête ; pack_root : racine du dépôt (ROOT par défaut) : terrain_sched.txt et trampolines (fl_terrain_paths.check_root,
    vérifiée seulement avec réécriture : sans elle le dépôt n'est ni lu ni écrit)."""
    map_dir, repo = Path(map_dir), Path(pack_root or ROOT)
    if not map_dir.is_dir():
        raise TerrainError(f'carte introuvable : {map_dir}')
    try:
        out = fl_terrain_paths.check_out(out_dir, map_dir, ROOT, repo)
        if rewrite:
            repo = fl_terrain_paths.check_root(repo, map_dir, out)
    except fl_terrain_paths.PathError as e:
        raise TerrainError(str(e)) from e
    zpath, report = out / ZIP_NAME, out / REPORT_NAME
    for stale in (zpath, report):                # le zip et le rapport d'un build précédent ne survivent à AUCUN échec, même avant la lecture
        stale.unlink(missing_ok=True)
    dim_id, dim_dir = pick_dimension(find_dimensions(map_dir), dimension, map_dir)
    files, info = collect(dim_dir), map_info(map_dir)
    notes = []
    if info.get('spawn_dim') and info['spawn_dim'] != dim_id:
        notes.append(f'(!) le spawn de la carte est dans {info["spawn_dim"]}, pas dans {dim_id}')
    if 'spawn' in info:
        rx, rz = info['spawn'][0] >> 9, info['spawn'][2] >> 9
        ok = f'region/r.{rx}.{rz}.mca' in {a for a, _ in files}
        notes.append(f'spawn      : {info["spawn"]} -> region r.{rx}.{rz} {"presente" if ok else "(!) ABSENTE"} dans {dim_id}')
    else:
        notes.append('(!) level.dat illisible : spawn non verifie, VERSION sans nom ni date')
    text, regions = version_text(dim_id, info, files, rewrite)
    out.mkdir(parents=True, exist_ok=True)
    run, done = fl_terrain_rw.Pass(rewrite, dim_id), [0]            # dim_id : ses `in <dim>` deviennent `in mg:floaty` (fl_terrain_cmd.Ctx)
    total = sum(1 for a, _ in files if a.endswith('.mca') and not a.startswith('poi/'))

    def transform(arc, data):
        try:
            res = run.file(arc, data)
        except fl_mca.VerifyError as e:
            raise TerrainError(f'{arc} : la reconstruction ne se relit pas comme prevu ({e}) : build abandonne, aucun zip') from e
        if arc.endswith('.mca') and not arc.startswith('poi/'):
            done[0] += 1
            if progress and done[0] % 25 == 0:
                progress(f'  scan {done[0]}/{total}')
        return res

    t0 = time.perf_counter()
    sha, src = write_zip(zpath, files, lambda s, h: text.replace(SHA_MARK, s, 1).replace(SRC_MARK, h, 1).replace(RW_MARK, str(run.rewritten()), 1),
                         transform)
    build_s = time.perf_counter() - t0               # jamais dans le rapport (déterministe) : main l'écrit sur stderr
    targets = run.sched_targets()
    if rewrite:
        try:
            write_sched(repo, targets)
        except BaseException:
            zpath.unlink(missing_ok=True)            # pas de zip sans la liste des trampolines qui va avec
            raise
    if run.unread_cmd and progress:
        progress(f'(!) {len(run.unread_cmd)} chunk(s) avec des commandes que le lecteur NBT strict ne lit pas : NON reecrits (illisible_cmd, voir le rapport)')
    ctx = {'map': map_dir, 'dim': dim_id, 'sha': sha, 'source_sha': src, 'zip_sha': file_sha256(zpath), 'zip_size': zpath.stat().st_size,
           'unread_cmd': run.unread_cmd, 'files': len(files), 'regions': regions, 'notes': notes, 'rewrite': rewrite, 'rewritten': run.rewritten(),
           'files_rebuilt': run.files, 'effects': run.effects(), 'sched': targets, 'sched_missing': fl_terrain_paths.missing_trampolines(repo, targets)}
    write_report(report, fl_terrain_report.report_text(ctx, run.finds, run.stats, run.sorted_pending(),
                                                  run.after if rewrite else None))
    return dict(ctx, zip=zpath, report=report, finds=run.finds, after=run.after, stats=run.stats, pending=run.sorted_pending(), build_s=build_s)


def main(argv=None):
    ap = argparse.ArgumentParser(description='Zip du terrain Floaty (region/ entities/ poi/) + rapport des blocs de commande.')
    ap.add_argument('--map', required=True, help='dossier de la carte (lecture seule)')
    ap.add_argument('--out', required=True, help='dossier de sortie (hors depot, hors carte)')
    ap.add_argument('--dimension', help="id de la dimension de la carte a exporter (obligatoire s'il y en a plusieurs avec du terrain)")
    ap.add_argument('--no-rewrite', action='store_true', help='ne reecrit aucune commande du terrain (zip identique a celui de L5 / L6a, VERSION 1)')
    ap.add_argument('--root', default=str(ROOT), help='racine du depot NeoMC (defaut : celle de ce script) : terrain_sched.txt et trampolines')
    a = ap.parse_args(argv)
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    try:
        r = build(a.map, a.out, a.dimension, lambda m: print(m, file=sys.stderr), not a.no_rewrite, a.root)
    except TerrainError as e:
        print(f'erreur : {e}', file=sys.stderr)
        return 1
    print(f'dimension {r["dim"]} : {r["files"]} fichiers, {r["regions"]} regions')
    print(f'zip     : {r["zip"]} ({r["zip_size"]} octets) sha256 {r["zip_sha"]}')
    print(f'contenu : sha256 {r["sha"]} (VERSION)')
    if r['rewrite']:
        print(f'reecriture : {r["rewritten"]} commandes modifiees, {r["files_rebuilt"]} fichiers reconstruits, {len(r["sched"])} cibles schedule '
              f'({len(r["sched_missing"])} sans trampoline dans le depot)')
    print(f'rapport : {r["report"]} ({len(r["finds"])} commandes ; {fl_terrain_report.totals_line(*fl_terrain_report.chunk_totals(r["stats"], r["pending"]))})')
    print(f'build : {r["build_s"]:.1f} s (scan, reecriture, zip)', file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
