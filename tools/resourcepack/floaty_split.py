# ------------------------------------------------------------------ Floaty : scission des fichiers de la carte (pack serveur forcé / pack optionnel)
# Exécuté par gen_rp.py (exec), après floaty_extra : FLOATY_EXTRA, FLOATY_OPT = floaty_split(floaty_extra(OUT, keep_same=True), PACK_FMT).
# Que des fonctions pures (préfixe floaty_ : mêmes globals que gen_rp), importables telles quelles (tools/tests/test_floaty_split.py).
# Seule lecture : le manifeste floaty_vanilla.json (produit par floaty_manifest.py avec le jar client), sauf si le test en passe un.
#
# Un fichier de la carte tombe dans l'une de ces cases (floaty_classify) :
#   drop   : écarté des deux packs (liste « dropped » du manifeste : fichiers neufs sans effet) ;
#   wrap   : items/X.json qui remplace un item vanilla -> pack serveur, enveloppé dans un select sur minecraft:context_dimension :
#            cas mg:floaty = le modèle de la carte, repli = la définition vanilla telle quelle (hors de Floaty, rien ne change) ;
#   rename : texture item remplacée (+ .mcmeta) ou modèle item remplacé -> pack serveur sous assets/floaty/ (jamais lu hors des modèles floaty:) ;
#   opt    : tout autre fichier qui remplace du vanilla (blocs, entités, particules, tableaux...) -> pack optionnel ;
#   server : fichier neuf -> pack serveur ; les modèles et items JSON neufs qui lisent une texture item ou un modèle renommé sont réécrits vers
#            floaty: (seule la carte les lit), sinon octets inchangés.
# Les items vanilla dont un modèle lit une texture item remplacée (compass, brush...) sont enveloppés aussi, même si la carte ne les définit
# pas, et leurs modèles vanilla sont recopiés sous floaty: avec leurs textures réécrites (liste « items » / « models » du manifeste).
# Gardes (SystemExit qui liste les chemins) : la carte ne doit rien mettre sous assets/floaty/ (espace de noms des fichiers générés) ; PACK_FMT doit
# couvrir la version du jar du manifeste ; l'empreinte des chemins de la carte doit égaler names_sha256 ; chaque définition vanilla attendue doit
# être dans le manifeste ; les événements du sounds.json de la carte doivent être ceux du manifeste (neufs : il reste dans le pack forcé, donc aucun
# événement vanilla) ; aucune clé générée n'en écrase une autre. Elles disent de relancer le manifeste (la carte ou le jar a changé), sauf quand le
# problème vient d'un fichier que le manifeste ne règle pas (assets/floaty/, sounds.json qui n'est pas un objet, collision, JSON illisible ou sans « model »).
# Les fichiers identiques à ceux de NeoMC se retirent APRÈS la scission (floaty_rp.floaty_settle) : l'empreinte porte sur toute la carte.
import copy
import hashlib
import json
import os

FLOATY_MANIFEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'floaty_vanilla.json')
FLOATY_NS = 'floaty'
FLOATY_DIM = 'mg:floaty'                      # dimension de la carte : le seul cas où les remplacements s'appliquent côté pack serveur
FLOATY_MC = 'assets/minecraft/'
FLOATY_RESERVED = f'assets/{FLOATY_NS}/'
FLOATY_SNDJSON = FLOATY_MC + 'sounds.json'
FLOATY_ITEMS = FLOATY_MC + 'items/'
FLOATY_TEX_ITEM = FLOATY_MC + 'textures/item/'
FLOATY_MODEL_ITEM = FLOATY_MC + 'models/item/'
FLOATY_REF_KEYS = ('model', 'base')           # clés d'une définition d'item qui portent une référence de modèle (base : modèle « special »)
FLOATY_RERUN = 'relancer tools/resourcepack/floaty_manifest.py avec NEOMC_MC_JAR (jar client), NEOMC_FLOATY_RP (pack de la carte), NEOMC_MC_ASSETS et NEOMC_MC_ASSET_INDEX (assets du lanceur), puis commiter floaty_vanilla.json'


def floaty_names_digest(names):
    """Empreinte SHA-256 de la liste triée des chemins de la carte (une ligne par chemin)."""
    return hashlib.sha256('\n'.join(sorted(names)).encode('utf-8')).hexdigest()


def floaty_stop(title, paths, rerun=True):
    """SystemExit : titre, chemins en cause (triés), consigne de relancer le manifeste (sauf rerun=False : problème qu'il ne règle pas)."""
    lines = ''.join(f'\n  {p}' for p in sorted(paths))
    return SystemExit(f'floaty : {title}{lines}' + (f'\n{FLOATY_RERUN}' if rerun else ''))


def floaty_id(ref):
    """Identifiant sans « minecraft: » (« minecraft:item/x » et « item/x » -> « item/x ») ; un autre espace de noms est gardé tel quel."""
    ns, _, rest = ref.rpartition(':')
    return rest if ns in ('', 'minecraft') else ref


def floaty_sets(man):
    """Index du manifeste : rep (chemins remplacés), drop (écartés), tex (ids des textures item renommées), mod (ids des modèles renommés)."""
    rep = {p for paths in man['replaced'].values() for p in paths}
    tex = {p[len(FLOATY_MC + 'textures/'):-len('.png')] for p in man['replaced'].get('textures_item', [])}
    mod = {p[len(FLOATY_MC + 'models/'):-len('.json')] for p in list(man['models']) + man['replaced'].get('models', []) if p.startswith(FLOATY_MODEL_ITEM)}
    return {'rep': rep, 'drop': set(man['dropped']), 'tex': tex, 'mod': mod}


def floaty_classify(path, ix):
    """'drop' | 'wrap' | 'rename' | 'opt' | 'server' pour un chemin de la carte (ix : floaty_sets)."""
    if path in ix['drop']:
        return 'drop'
    if path not in ix['rep']:
        return 'server'
    if path.startswith(FLOATY_ITEMS):
        return 'wrap'
    if path.startswith((FLOATY_TEX_ITEM, FLOATY_MODEL_ITEM)):
        return 'rename'
    return 'opt'


def floaty_rename(path):
    """assets/minecraft/... -> assets/floaty/... (textures et modèles item uniquement)."""
    if not path.startswith((FLOATY_TEX_ITEM, FLOATY_MODEL_ITEM)):
        raise ValueError(f'rien à renommer : {path}')
    return f'assets/{FLOATY_NS}/' + path[len(FLOATY_MC):]


def floaty_ref(ref, ids):
    """floaty:<id> si ref désigne un modèle renommé (ids), sinon ref inchangée."""
    i = floaty_id(ref)
    return f'{FLOATY_NS}:{i}' if i in ids else ref


def floaty_refs(node, ix):
    """Copie d'une définition d'item où chaque référence (clés model / base) à un modèle renommé pointe sur floaty:."""
    if isinstance(node, dict):
        return {k: floaty_ref(v, ix['mod']) if k in FLOATY_REF_KEYS and isinstance(v, str) else floaty_refs(v, ix) for k, v in node.items()}
    if isinstance(node, list):
        return [floaty_refs(v, ix) for v in node]
    return node


def floaty_model(model, ix):
    """Copie d'un modèle vanilla renommé : textures item remplacées et parent renommé pointent sur floaty:."""
    out = copy.deepcopy(model)
    if isinstance(out.get('textures'), dict):
        out['textures'] = {k: f'{FLOATY_NS}:{floaty_id(v)}' if isinstance(v, str) and floaty_id(v) in ix['tex'] else v for k, v in out['textures'].items()}
    if isinstance(out.get('parent'), str):
        out['parent'] = floaty_ref(out['parent'], ix['mod'])
    return out


def floaty_wrap_item(vanilla, case):
    """Définition d'item enveloppée : cas mg:floaty = case (modèle de la carte ou vanilla, refs déjà réécrites), repli = modèle vanilla intact.
    Les autres clés de premier niveau de la définition vanilla sont conservées."""
    select = {'type': 'minecraft:select', 'property': 'minecraft:context_dimension',
              'cases': [{'when': FLOATY_DIM, 'model': case}], 'fallback': copy.deepcopy(vanilla['model'])}
    return {'model': select, **{k: copy.deepcopy(v) for k, v in vanilla.items() if k != 'model'}}


def floaty_encode(obj):
    """JSON déterministe : ordre des clés conservé, indent 2, UTF-8, LF."""
    return (json.dumps(obj, indent=2, ensure_ascii=False) + '\n').encode('utf-8')


def floaty_parse(path, data):
    """JSON d'un fichier de la carte ; SystemExit qui nomme le fichier s'il est illisible."""
    try:
        return json.loads(data.decode('utf-8'))
    except ValueError as e:
        raise SystemExit(f'floaty : {path} illisible (JSON) : {e}')


def floaty_check(extra, man, ix, pack_fmt=None):
    """Gardes (cf. l'en-tête) : espace de noms réservé, version du pack, chemins du manifeste absents de la carte, empreinte, définitions vanilla
    attendues, événements de sons. pack_fmt : PACK_FMT de gen_rp (None : version non contrôlée). SystemExit sinon."""
    reserved = [p for p in extra if p.startswith(FLOATY_RESERVED)]
    if reserved:
        raise floaty_stop(f'{len(reserved)} fichier(s) de la carte sous {FLOATY_RESERVED} (espace de noms des fichiers générés, jamais à la carte) :', reserved, False)
    version = man['version']
    if pack_fmt is not None and not pack_fmt['min_format'] <= version['resource'] <= pack_fmt['max_format']:
        raise floaty_stop(f'PACK_FMT {pack_fmt["min_format"]}..{pack_fmt["max_format"]} ne couvre pas la version du manifeste '
                          f'({version["id"]}, ressources {version["resource"]})', [])
    missing = [p for p in ix['rep'] | ix['drop'] if p not in extra]
    if missing:
        raise floaty_stop(f'{len(missing)} fichier(s) du manifeste absents de la carte :', missing)
    if floaty_names_digest(extra) != man['names_sha256']:
        raise floaty_stop('la liste des fichiers de la carte ne correspond plus au manifeste (fichiers ajoutés ou retirés, aucun chemin du manifeste ne manque)', [])
    lost = [p for p in ix['rep'] if p.startswith(FLOATY_ITEMS) and p not in man['items']]
    if lost:
        raise floaty_stop(f'{len(lost)} définition(s) vanilla attendue(s) absente(s) du manifeste :', lost)
    if FLOATY_SNDJSON in extra:                     # son contenu n'est pas dans l'empreinte : on contrôle les clés (événements)
        snd = floaty_parse(FLOATY_SNDJSON, extra[FLOATY_SNDJSON])
        if not isinstance(snd, dict):
            raise floaty_stop('sounds.json de la carte : un objet JSON est attendu :', [FLOATY_SNDJSON], False)
        known = set(man['sounds']['new'])
        unknown = [k for k in snd if k not in known]
        if unknown:
            raise floaty_stop(f'{len(unknown)} événement(s) du sounds.json de la carte absents des événements neufs du manifeste '
                              '(vanilla redéfini, ou music.* vide non retiré) :', unknown)


def floaty_put(server, path, data):
    """server[path] = data ; SystemExit si la clé existe déjà (une clé générée n'en écrase jamais une autre)."""
    if path in server:
        raise floaty_stop('collision entre fichiers générés :', [path], False)
    server[path] = data


def floaty_passthrough(path, data, ix):
    """Octets d'un fichier neuf pour le pack serveur : les modèles et items JSON qui lisent une texture item ou un modèle renommé sont réécrits
    vers floaty: (seule la carte les lit, sans risque), tout le reste et tout JSON sans changement garde ses octets."""
    if not path.endswith('.json') or not path.startswith((FLOATY_MC + 'models/', FLOATY_ITEMS)):
        return data
    doc = floaty_parse(path, data)
    if not isinstance(doc, dict):
        return data
    new = floaty_refs(doc, ix) if path.startswith(FLOATY_ITEMS) else floaty_model(doc, ix)
    return data if new == doc else floaty_encode(new)


def floaty_split(extra, pack_fmt=None, man=None):
    """(serveur, optionnel) : deux {chemin: octets} à partir de extra (floaty_extra) ; ({}, {}) si extra est vide (variable absente).
    pack_fmt : PACK_FMT de gen_rp ; man : manifeste (défaut : floaty_vanilla.json). Le pack optionnel ne reçoit que des remplacements globaux ;
    rien n'est écrit sur disque."""
    if not extra:
        return {}, {}
    if man is None:
        with open(FLOATY_MANIFEST, encoding='utf-8') as fh:
            man = json.load(fh)
    ix = floaty_sets(man)
    floaty_check(extra, man, ix, pack_fmt)
    server, opt, wrap = {}, {}, {}
    for path in sorted(extra):
        kind = floaty_classify(path, ix)
        if kind == 'server':
            floaty_put(server, path, floaty_passthrough(path, extra[path], ix))
        elif kind == 'opt':
            opt[path] = extra[path]
        elif kind == 'rename':
            is_model = path.startswith(FLOATY_MODEL_ITEM)       # un modèle remplacé : ses textures / son parent sont réécrits comme ceux de vanilla
            floaty_put(server, floaty_rename(path), floaty_encode(floaty_model(floaty_parse(path, extra[path]), ix)) if is_model else extra[path])
        elif kind == 'wrap':
            wrap[path] = floaty_parse(path, extra[path])
    for path, model in sorted(man['models'].items()):
        floaty_put(server, floaty_rename(path), floaty_encode(floaty_model(model, ix)))
    for path, vanilla in sorted(man['items'].items()):
        theirs = wrap.get(path, vanilla)                       # la carte, ou vanilla pour un item qu'elle ne définit pas
        if not isinstance(theirs, dict) or not isinstance(theirs.get('model'), dict):
            raise floaty_stop('définition d\'item sans objet « model » :', [path], False)
        floaty_put(server, path, floaty_encode(floaty_wrap_item(vanilla, floaty_refs(theirs['model'], ix))))
    return server, opt
