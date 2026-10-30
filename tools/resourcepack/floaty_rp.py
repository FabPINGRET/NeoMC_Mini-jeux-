# ------------------------------------------------------------------ Scourge of the Floaty Isles : textures de la carte fusionnées dans le zip
# Exécuté par gen_rp.py (exec) : n'utilise aucun nom de gen_rp ; gen_rp appelle floaty_extra(OUT), floaty_split (floaty_split.py : pack serveur /
# pack optionnel), puis floaty_write(zf, ...) pour le zip serveur et floaty_write_opt(...) pour releases/floaty_optional_resourcepack.zip.
# Que des fonctions, importables telles quelles (tools/tests/test_floaty_rp.py).
#
# Source : variable d'environnement NEOMC_FLOATY_RP = dossier OU .zip du resource pack de la carte (racine = pack.mcmeta + assets/).
#   Le pack livré avec la carte : resourcepacks/resources.zip (identique à « Scourge Assets.zip » et au dossier rp/ extrait).
#   Variable ABSENTE : étape ignorée avec un avertissement (le zip commité contient les textures Floaty, un build sans la variable les
#   retire), pas d'erreur (CI, autres contributeurs). Variable définie mais vide : erreur.
# Seul assets/ est repris (le pack.mcmeta et le pack.png de la carte sont ignorés) ; __MACOSX/ (racine), .DS_Store et assets/*/lang/
# (décision de Maxime : la langue de la carte n'est pas importée) sont sautés. Tout autre nom sous assets/ doit valoir
# assets/[a-z0-9_.-/]+ sans « .. », sans segment vide ni AppleDouble « ._* », sans doublon : sinon erreur qui les liste.
# sounds.json est réécrit (JSON, ordre de la source conservé, indent 2, déterministe) sans les événements music.* « replace: true +
# sounds: [] » (ils coupent la musique vanilla) avant la détection de conflit. Rien sous assets/mg/ (namespace NeoMC) : erreur.
# Les fichiers sont ajoutés au ZIP seulement : le dossier resourcepack/ (suivi par git) ne reçoit rien, donc pas de reste d'une fusion
# précédente et un build sans variable redonne exactement le zip d'avant.
# Un fichier de la carte qui existe déjà dans le pack NeoMC avec un contenu différent = erreur listant tous les chemins, rien n'est écrit
# (identique à l'octet : toléré). Les fichiers fusionnables (atlases/, font/, sounds.json) ne sont pas fusionnés : à traiter à la main.
import json
import os
import re
import sys
import zipfile
import zlib
from collections import Counter

FLOATY_ENV = 'NEOMC_FLOATY_RP'
FLOATY_SOUNDS = 'assets/minecraft/sounds.json'
FLOATY_DATE = (2026, 1, 1, 0, 0, 0)                       # même date fixe que le zip de gen_rp (zip reproductible)
FLOATY_MERGEABLE = ('assets/minecraft/atlases/', 'assets/minecraft/font/', 'assets/minecraft/sounds.json')
FLOATY_NAME = re.compile(r'assets/[a-z0-9_.\-/]+')
FLOATY_READ_ERRORS = (ValueError, OSError, zipfile.BadZipFile, RuntimeError, NotImplementedError, zlib.error, EOFError)   # RuntimeError : zip chiffré


def floaty_select(names):
    """(retenus, invalides) parmi les chemins d'archive : ignorés sans bruit hors assets/, __MACOSX/ racine, .DS_Store et lang/."""
    kept, bad, seen = [], [], set()
    for n in names:
        parts = n.split('/')
        if '\\' in n or n.startswith('/') or re.match(r'[A-Za-z]:', n):
            bad.append(n)
            continue
        if parts[0] == '__MACOSX' or parts[-1] == '.DS_Store' or parts[0] != 'assets':
            continue
        if not FLOATY_NAME.fullmatch(n) or '..' in parts or '' in parts or parts[-1].startswith('._'):
            bad.append(n)
        elif n in seen:
            bad.append(f'{n} (en double)')
        else:
            seen.add(n)
            if not (len(parts) > 3 and parts[2] == 'lang'):
                kept.append(n)
    return kept, bad


def floaty_collect(src):
    """{chemin relatif: octets} des assets/ du pack de la carte (src : dossier ou .zip)."""
    zf = None
    if os.path.isdir(src):
        entries = []
        for root, dirs, files in os.walk(src):
            for f in files:
                p = os.path.join(root, f)
                entries.append((os.path.relpath(p, src).replace(os.sep, '/'), p))

        def read(path):
            with open(path, 'rb') as fh:
                return fh.read()
    elif zipfile.is_zipfile(src):
        zf = zipfile.ZipFile(src)
        entries = [(i.filename, i) for i in zf.infolist() if not i.filename.endswith('/')]
        read = zf.read
    else:
        raise ValueError(f'ni dossier ni .zip : {src}')
    try:
        kept, bad = floaty_select([rel for rel, _ in entries])
        if bad:
            raise ValueError(f'{len(bad)} nom(s) invalide(s) ou en double dans le pack de la carte :\n  ' + '\n  '.join(sorted(bad)))
        keep = set(kept)
        out = {rel: read(handle) for rel, handle in entries if rel in keep}
    finally:
        if zf is not None:
            zf.close()
    if not out:
        raise ValueError(f'aucun fichier assets/ dans {src}')
    return out


def floaty_dump(obj):
    """JSON réécrit : ordre des clés de la source, indent 2, UTF-8, LF."""
    return (json.dumps(obj, indent=2, ensure_ascii=False) + '\n').encode('utf-8')


def floaty_filter(extra):
    """Réécrit sounds.json sans les music.* « replace: true + sounds: [] ». Modifie extra."""
    if FLOATY_SOUNDS not in extra:
        return
    try:
        snd = json.loads(extra[FLOATY_SOUNDS].decode('utf-8'))
    except ValueError as e:
        raise ValueError(f'sounds.json illisible : {e}')
    if not isinstance(snd, dict) or not all(isinstance(v, dict) for v in snd.values()):
        raise ValueError('sounds.json : un objet JSON dont chaque entrée est un objet est attendu')
    extra[FLOATY_SOUNDS] = floaty_dump({k: v for k, v in snd.items() if not (k.startswith('music.') and v.get('replace') and v.get('sounds') == [])})


def floaty_scope(extra):
    """Résumé de portée (fichiers par sous-dossier hors textures/, puis textures) ; ValueError si la carte touche assets/mg/."""
    mg = sorted(p for p in extra if p.startswith('assets/mg/'))
    if mg:
        raise ValueError(f'{len(mg)} fichier(s) sous assets/mg/ (namespace NeoMC, jamais à la carte) :\n  ' + '\n  '.join(mg))
    kinds, textures = Counter(), 0
    for p in extra:
        parts = p.split('/')
        if parts[2:3] == ['textures']:
            textures += 1
        else:
            kinds['/'.join(parts[1:3])] += 1
    return 'portée hors textures : ' + ', '.join(f'{k} {v}' for k, v in sorted(kinds.items())) + f' ; textures : {textures}'


def floaty_neo_files(out):
    """{chemin relatif: chemin sur disque} de tout ce que gen_rp a produit dans le dossier out."""
    found = {}
    for root, dirs, files in os.walk(out):
        for f in files:
            p = os.path.join(root, f)
            found[os.path.relpath(p, out).replace(os.sep, '/')] = p
    return found


def floaty_conflicts(extra, neo):
    """Chemins de la carte déjà produits par NeoMC avec un contenu différent, triés (identique à l'octet : pas un conflit)."""
    bad = []
    for rel, data in extra.items():
        if rel in neo:
            with open(neo[rel], 'rb') as fh:
                if fh.read() != data:
                    bad.append(rel)
    return sorted(bad)


def floaty_extra(out, env=None, keep_same=False):
    """Fichiers de la carte à ajouter au zip : {chemin: octets}, ou {} si NEOMC_FLOATY_RP est absente. Erreur de source / conflit : SystemExit.
    keep_same : garde aussi les fichiers identiques à l'octet à ceux de NeoMC (l'empreinte du manifeste porte sur toute la carte : à retirer
    ensuite avec floaty_settle, après floaty_split)."""
    env = os.environ if env is None else env
    if FLOATY_ENV not in env:
        print(f'floaty : ATTENTION {FLOATY_ENV} absente, textures Floaty NON incluses : ce zip n\'a plus les textures de la carte (ne pas le commiter ainsi)')
        return {}
    src = env[FLOATY_ENV].strip()
    if not src:
        sys.exit(f'floaty : {FLOATY_ENV} est définie mais vide : la retirer, ou donner le dossier / .zip du resource pack de la carte')
    try:
        extra = floaty_collect(src)
        floaty_filter(extra)
        scope = floaty_scope(extra)
    except FLOATY_READ_ERRORS as e:
        sys.exit(f'floaty : {FLOATY_ENV} : {e}')
    neo = floaty_neo_files(out)
    bad = floaty_conflicts(extra, neo)
    if bad:
        hint = [p for p in bad if p.startswith(FLOATY_MERGEABLE)]
        sys.exit(f"floaty : {len(bad)} fichier(s) de la carte en conflit avec le pack NeoMC, rien n'est fusionné :\n  " + '\n  '.join(bad)
                 + (f'\nfusion JSON à faire à la main pour : {", ".join(hint)}' if hint else ''))
    if not keep_same:
        extra = {rel: data for rel, data in extra.items() if rel not in neo}      # identiques à l'octet : déjà dans le pack
    verb = 'lus (les identiques à NeoMC sont retirés après la scission)' if keep_same else 'ajoutés au zip'
    print(f'floaty : {len(extra)} fichier(s) de la carte {verb} ({sum(len(d) for d in extra.values()) / 1e6:.1f} Mo) depuis {src}')
    print(f'floaty : {scope}')
    return extra


def floaty_settle(server, opt, out):
    """(server, opt) sans les fichiers identiques à l'octet à ceux de NeoMC (dossier out : déjà dans le pack) ; SystemExit qui liste les chemins
    générés par la scission (assets/floaty/..., items enveloppés) ou venus de la carte qui existent déjà dans NeoMC avec un autre contenu."""
    neo = floaty_neo_files(out)
    bad = sorted(set(floaty_conflicts(server, neo)) | set(floaty_conflicts(opt, neo)))
    if bad:
        sys.exit(f"floaty : {len(bad)} fichier(s) du pack Floaty en conflit avec le pack NeoMC, rien n'est écrit :\n  " + '\n  '.join(bad))
    return ({rel: data for rel, data in server.items() if rel not in neo}, {rel: data for rel, data in opt.items() if rel not in neo})


def floaty_write(zf, extra):
    """Ajoute extra au zip ouvert zf, triés par chemin, date fixe : à appeler après les fichiers NeoMC."""
    for rel in sorted(extra):
        info = zipfile.ZipInfo(rel, date_time=FLOATY_DATE)
        info.compress_type = zipfile.ZIP_DEFLATED
        zf.writestr(info, extra[rel])


def floaty_write_opt(path, opt, meta):
    """Écrit le pack optionnel path : opt ({chemin: octets}) plus son propre pack.mcmeta (meta, objet JSON), triés, date fixe, reproductible."""
    if 'pack.mcmeta' in opt:
        raise ValueError('pack.mcmeta est ajouté par floaty_write_opt : il ne doit pas figurer dans opt')
    files = dict(opt)
    files['pack.mcmeta'] = floaty_dump(meta)
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as zf:
        floaty_write(zf, files)
