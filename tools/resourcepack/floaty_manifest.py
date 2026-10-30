"""Manifeste Floaty : quels fichiers de la carte remplacent du vanilla, et les définitions vanilla à envelopper (floaty_split.py).
Outil de dev, hors de gen_rp.py : à relancer quand la carte ou la version de Minecraft change, puis à commiter floaty_vanilla.json.
Usage : NEOMC_MC_JAR=<minecraft-X-client.jar> NEOMC_FLOATY_RP=<dossier ou .zip du pack de la carte>
        NEOMC_MC_ASSETS=<dossier assets du lanceur, avec indexes/ et objects/> NEOMC_MC_ASSET_INDEX=<id de l'index, ex. 32>
        python tools/resourcepack/floaty_manifest.py [sortie.json]
(NEOMC_FLOATY_RP : même variable que gen_rp.py ; sortie par défaut : floaty_vanilla.json à côté de ce fichier. Le jar ne contient pas les sons :
l'index d'assets donne les chemins de sons vanilla et le sounds.json vanilla.)

Un fichier de la carte « remplace » du vanilla s'il existe dans le jar ou dans l'index d'assets ; un X.png.mcmeta prend le statut de X.png (il anime
une texture vanilla même si le jar n'a pas de .mcmeta pour elle). Fermeture : textures item remplacées -> modèles vanilla qui les lisent (et leurs
enfants par parent) -> items/*.json vanilla qui lisent ces modèles, plus les items remplacés par la carte et ceux qui lisent un modèle qu'elle remplace.
sounds.json est classé par événement, pas par fichier : il reste tel quel dans le pack serveur, donc aucun événement vanilla ne doit y subsister
(seuls les music.* vides, retirés par floaty_filter, sont tolérés) : sinon le manifeste s'arrête.
Contenu du manifeste : names_sha256 (empreinte des chemins de la carte), version (id et pack_format ressources du jar), replaced (par catégorie),
dropped (fichiers neufs sans effet, écartés des deux packs : DROP_RULES), sounds (événements neufs / retirés), items et models (copies JSON de
Mojang, le strict nécessaire).
"""
import importlib.util
import json
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
MC = 'assets/minecraft/'
CATEGORIES = ('items', 'models', 'textures_item', 'textures_block', 'textures_entity', 'textures_particle', 'textures_painting',
              'textures_other', 'sounds', 'mcmeta', 'other')
# Fichiers neufs de la carte sans effet (décision de Maxime) : jamais livrés. Un fichier qui existe dans le jar ne peut pas y figurer.
DROP_RULES = [re.compile(p) for p in (
    r'assets/minecraft/textures/trims/(models/armor|color_palettes)/(template|circles|spider)[^/]*',
    r'assets/minecraft/textures/entity/equipment/wings/elytra_old\.png(\.mcmeta)?',
    r'assets/minecraft/textures/misc/enchanted_item_glint\.png\.mcmeta',
    r'assets/minecraft/textures/misc/enchanted_glint_entity\.png(\.mcmeta)?',
)]


def load(name):
    """Module voisin chargé par chemin (floaty_rp.py et floaty_split.py s'exécutent aussi dans gen_rp)."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


fr = load('floaty_rp')
fs = load('floaty_split')
READ_ERRORS = fr.FLOATY_READ_ERRORS + (KeyError,)


def category(name):
    """Catégorie d'un chemin remplacé : items, models, textures_<dossier>, sounds, mcmeta, other."""
    if name.endswith('.png.mcmeta'):
        return 'mcmeta'
    if not name.startswith(MC):
        return 'other'
    parts = name[len(MC):].split('/')
    if parts[0] in ('items', 'models', 'sounds'):
        return parts[0]
    if parts[0] == 'textures':
        sub = 'textures_' + parts[1] if len(parts) > 2 else 'textures_other'
        return sub if sub in CATEGORIES else 'textures_other'
    return 'other'


def in_vanilla(name, jar_names, assets):
    """Vrai si le chemin existe dans le jar ou dans l'index d'assets ; un X.png.mcmeta prend le statut de X.png."""
    base = name[:-len('.mcmeta')] if name.endswith('.png.mcmeta') else name
    return any(n in jar_names or n in assets for n in (name, base))


def read_assets(assets_dir, index_id):
    """(chemins « assets/<clé> » de l'index, noms d'événements du sounds.json vanilla) pour le dossier d'assets du lanceur et l'id d'index."""
    with open(os.path.join(assets_dir, 'indexes', index_id + '.json'), encoding='utf-8') as fh:
        objects = json.load(fh)['objects']
    digest = objects['minecraft/sounds.json']['hash']
    with open(os.path.join(assets_dir, 'objects', digest[:2], digest), encoding='utf-8') as fh:
        events = set(json.load(fh))
    return {'assets/' + k for k in objects}, events


def classify_sounds(data, vanilla_events):
    """{'new': [...], 'dropped': [...]} : événements du sounds.json de la carte (octets, ou None). dropped = ceux que floaty_filter retire
    (music.* vides). SystemExit si un événement vanilla reste : sounds.json n'est pas enveloppé, il s'appliquerait à tout le serveur."""
    if data is None:
        return {'new': [], 'dropped': []}
    every = set(json.loads(data.decode('utf-8')))
    probe = {fr.FLOATY_SOUNDS: data}
    fr.floaty_filter(probe)
    kept = set(json.loads(probe[fr.FLOATY_SOUNDS].decode('utf-8')))
    vanilla = sorted(kept & set(vanilla_events))
    if vanilla:
        raise SystemExit('manifeste : sounds.json de la carte redéfinit des événements vanilla (pack serveur forcé : ils toucheraient tout le serveur) :\n  '
                         + '\n  '.join(vanilla))
    return {'new': sorted(kept), 'dropped': sorted(every - kept)}


def jar_version(jar_names, jar_read):
    """{'id', 'resource': [major, minor]} du version.json du jar."""
    if 'version.json' not in jar_names:
        raise SystemExit('manifeste : version.json absent du jar')
    v = json.loads(jar_read('version.json').decode('utf-8'))
    return {'id': v['id'], 'resource': [v['pack_version']['resource_major'], v['pack_version'].get('resource_minor', 0)]}


def refs(node, out):
    """Identifiants de modèle (clés model / base) d'une définition d'item."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k in fs.FLOATY_REF_KEYS and isinstance(v, str):
                out.add(fs.floaty_id(v))
            else:
                refs(v, out)
    elif isinstance(node, list):
        for v in node:
            refs(v, out)
    return out


def reading_models(jar_names, jar_read, tex_ids, roots, skip):
    """Ids (« item/x ») des modèles vanilla qui lisent une texture de tex_ids, ou dont le parent en lit une / est dans roots. skip : chemins ignorés."""
    info = {}
    for n in sorted(jar_names):
        if n.startswith(MC + 'models/') and n.endswith('.json') and n not in skip:
            m = json.loads(jar_read(n).decode('utf-8'))
            texs = {fs.floaty_id(v) for v in (m.get('textures') or {}).values() if isinstance(v, str)}
            parent = fs.floaty_id(m['parent']) if isinstance(m.get('parent'), str) else None
            info[n[len(MC + 'models/'):-len('.json')]] = (bool(texs & tex_ids), parent)
    hit = {i for i, (direct, _) in info.items() if direct}
    grew = True
    while grew:                                      # les enfants qui héritent d'une texture par leur parent
        grew = False
        for i, (_, parent) in info.items():
            if i not in hit and parent in (hit | roots):
                hit.add(i)
                grew = True
    return hit


def build_manifest(map_names, jar_names, jar_read, assets=frozenset(), vanilla_events=frozenset(), sounds_json=None):
    """Manifeste (dict) pour les chemins de la carte et un jar (jar_names : ensemble des chemins, jar_read : chemin -> octets).
    assets : chemins vanilla de l'index d'assets (sons), vanilla_events : événements du sounds.json vanilla, sounds_json : octets de celui de la carte."""
    names = sorted(map_names)
    cats = {c: [] for c in CATEGORIES}
    dropped = []
    for n in names:
        matched = any(r.fullmatch(n) for r in DROP_RULES)
        if n != fr.FLOATY_SOUNDS and in_vanilla(n, jar_names, assets):          # sounds.json : classé par événement (classify_sounds)
            if matched:
                raise SystemExit(f'manifeste : une règle DROP_RULES écarterait un fichier qui remplace du vanilla : {n}')
            cats[category(n)].append(n)
        elif matched:
            dropped.append(n)
    tex_ids = {p[len(MC + 'textures/'):-len('.png')] for p in cats['textures_item'] if p.startswith(fs.FLOATY_TEX_ITEM)}
    replaced_models = {p[len(MC + 'models/'):-len('.json')] for p in cats['models']}
    item_models = {i for i in replaced_models if i.startswith('item/')}          # les autres vont au pack optionnel : aucun item à envelopper
    hit = reading_models(jar_names, jar_read, tex_ids, item_models, set(cats['models']))
    outside = sorted(i for i in hit if not i.startswith('item/'))
    if outside:
        raise SystemExit('manifeste : modèle(s) vanilla hors models/item/ qui lisent une texture item remplacée :\n  ' + '\n  '.join(outside))
    models = {f'{MC}models/{i}.json': json.loads(jar_read(f'{MC}models/{i}.json').decode('utf-8')) for i in sorted(hit - replaced_models)}
    wrapped = set(cats['items'])
    for n in sorted(jar_names):
        if n.startswith(MC + 'items/') and n.endswith('.json') and n not in wrapped:
            if refs(json.loads(jar_read(n).decode('utf-8')), set()) & (hit | item_models):
                wrapped.add(n)
    items = {n: json.loads(jar_read(n).decode('utf-8')) for n in sorted(wrapped)}
    return {'names_sha256': fs.floaty_names_digest(names), 'version': jar_version(jar_names, jar_read), 'replaced': cats, 'dropped': dropped,
            'sounds': classify_sounds(sounds_json, vanilla_events), 'items': items, 'models': models}


def summary(man):
    """Une ligne de comptes par catégorie, puis items / modèles / écartés / sons."""
    counts = ' '.join(f'{c}={len(p)}' for c, p in man['replaced'].items() if p)
    snd = man['sounds']
    return (f'remplacés : {counts} | items enveloppés={len(man["items"])} modèles vanilla={len(man["models"])} écartés={len(man["dropped"])}'
            f' | événements de sons neufs={len(snd["new"])} retirés={len(snd["dropped"])} | {man["version"]["id"]} ressources {man["version"]["resource"]}')


def main(argv, env):
    """Lit le jar, la carte et l'index d'assets (variables, cf. l'en-tête), écrit le manifeste (argv[0] ou floaty_vanilla.json)."""
    jar, rp = env.get('NEOMC_MC_JAR', '').strip(), env.get(fr.FLOATY_ENV, '').strip()
    assets, index = env.get('NEOMC_MC_ASSETS', '').strip(), env.get('NEOMC_MC_ASSET_INDEX', '').strip()
    if not (jar and rp and assets and index):
        sys.exit(f'usage : NEOMC_MC_JAR=<client.jar> {fr.FLOATY_ENV}=<pack de la carte> NEOMC_MC_ASSETS=<dossier assets> NEOMC_MC_ASSET_INDEX=<id> '
                 f'python {os.path.basename(__file__)} [sortie.json]')
    try:
        files = fr.floaty_collect(rp)
        vanilla_assets, vanilla_events = read_assets(assets, index)
        with zipfile.ZipFile(jar) as zf:
            man = build_manifest(list(files), set(zf.namelist()), zf.read, vanilla_assets, vanilla_events, files.get(fr.FLOATY_SOUNDS))
    except READ_ERRORS as e:
        sys.exit(f'manifeste : {type(e).__name__} : {e}')
    out = argv[0] if argv else fs.FLOATY_MANIFEST
    with open(out, 'wb') as fh:
        fh.write(fs.floaty_encode(man))
    print(f'manifeste : {out}\nmanifeste : {summary(man)}')


if __name__ == '__main__':
    main(sys.argv[1:], os.environ)
