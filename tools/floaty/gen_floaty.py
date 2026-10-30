"""Importe la carte d'aventure « Scourge of the Floaty Isles » (26.2) dans le datapack, pour la dimension mg:floaty.

    python tools/floaty/gen_floaty.py --map <dossier de la carte extraite> [--adopt]      (carte : hors dépôt, en lecture seule)

Lit <carte>/datapacks/scourge/data/<ns>/ (+ biomes de <carte>/datapacks/biomes), <carte>/level.dat (spawn) et <carte>/data/minecraft/
(scoreboard.dat, custom_boss_events.dat, scheduled_events.dat, command_storage_*.dat : voir fl_state), réécrit chaque .mcfunction avec fl_rewrite (sélecteurs
cantonnés à la dimension, gamerule, schedule...) et écrit dans data/<ns>/ du dépôt (espaces de noms d'origine conservés). Génère aussi :
- data/floaty/function/sched/<ns>/<chemin>.mcfunction : un trampoline par fonction planifiée (relance `in mg:floaty positioned <spawn>`),
  celles des fonctions de la carte ET celles des commandes du terrain (tools/floaty/terrain_sched.txt, écrit par build_terrain.py :
  ordre : build (écrit la liste), gen_floaty (trampolines), build de nouveau, voir README) ;
- data/floaty/function/map/tick.mcfunction et map/load.mcfunction : le contenu (réécrit) de minecraft:tick / minecraft:load de la carte
  (vide si la carte n'en a pas) — NON branchés sur #minecraft:tick / load : mg:floaty/lobby_tick et session_start (L3) les appellent
  `in mg:floaty positioned <spawn>` ;
- data/floaty/function/install.mcfunction / uninstall.mcfunction : objectifs, équipes, scores des faux joueurs, bossbars, storage et
  schedules en attente de la carte (fl_state) ; uninstall est appelé par mg:desinstaller (une ligne y est ajoutée, après mg:elyrace/uninstall) ;
- data/mg/dimension/floaty.json : dimension plate et vide (même contenu que ombrelune.json, the_void) ;
- L3 (main : prepare_wire avant generate, wire après ; modèle tools/arcade/gen_filon.py, à lancer après lui) : data/mg/function/floaty/*
  (fl_wire : enter / leave / menu_go / pre_tick / lobby_tick / coffre Floaty ; fl_catchup : rattrapage cu/*, témoins ajoutés aux fonctions de la
  carte), patchs idempotents des fichiers suivis du coeur (fl_core), `gamerule advance_time|random_tick_speed` et `time set|add` RETIRÉS (voir fl_rewrite).
  À relancer APRÈS (le menu et sb/auto ne sont pas régénérés ici) : `python tools/lobby/gen_sidebar.py .` (sb/auto) puis, si le bouton du menu
  a bougé (patch_menu), `python tools/rating/gen_rating.py .` (rate/d/main_menu*.mcfunction) ; gen_tp_general.py n'est pas relancé (voir fl_core).
Tout est lu, validé et réécrit EN MÉMOIRE avant la première suppression : une carte incomplète ou illisible ne touche à rien.
Filtre d'import (include) : on exclut ce qui écraserait ou polluerait le vanilla / le reste du pack (advancements `minecraft:`,
tags vanilla étendus, tags de fonction tick/load, recettes vanilla, biome small_end_islands, .DS_Store, .bdstudio, fichiers hors dossier,
ids de ressource invalides). On garde les tags propres `hb_*` (restent sous minecraft: : #minecraft:hb_projectiles résout), trim_pattern +
leurs recettes, les biomes sous minecraft:worldgen/biome (les régions les référencent par id), les advancements des espaces de noms de la
carte (annonce dans le chat forcée à false : display.announce_to_chat ; condition joueur « dans mg:floaty » ajoutée à chaque critère,
sauf minecraft:impossible qui ne se déclenche que par commande), JSON normalisés en LF. Un dossier d'espace de noms de la carte dont le nom
n'est pas un nom valide (fl_owned.NS) est écarté (compté dans invalid).
Idempotent : relance = même sortie. Propriété et suppressions : voir fl_owned (manifeste owned.txt ; --adopt au premier passage).
"""
import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / 'tools' / 'lib'))
import fl_catchup as CU  # noqa: E402
import fl_core  # noqa: E402
import fl_nbt  # noqa: E402
import fl_owned as O  # noqa: E402
import fl_rewrite as R  # noqa: E402
import fl_state  # noqa: E402
import fl_summary  # noqa: E402
import fl_wire  # noqa: E402
import mcfn  # noqa: E402

PACK = Path('datapacks') / 'scourge' / 'data'
BIOMES = Path('datapacks') / 'biomes' / 'data' / 'minecraft' / 'worldgen' / 'biome'
TERRAIN_SCHED = Path('tools') / 'floaty' / 'terrain_sched.txt'       # écrit par build_terrain.py (même chemin : build_terrain.SCHED_FILE)
SKIP_BIOMES = {'small_end_islands'}
VALID_PATH = re.compile(r'[a-z0-9_./-]+')
# dimension plate et vide : même contenu que data/mg/dimension/ombrelune.json (gen_ombrelune, gen_gta et gen_terranova l'écrivent aussi en dur)
DIMENSION = {'type': 'minecraft:overworld', 'generator': {'type': 'minecraft:flat', 'settings': {
    'biome': 'minecraft:the_void', 'layers': [], 'lakes': False, 'features': False, 'structure_overrides': []}}}
IN_DIMENSION = {'condition': 'minecraft:entity_properties', 'entity': 'this',        # format 26.2 : clés d'entity predicate namespacées
                'predicate': {'minecraft:location': {'dimension': R.DIM}}}
UNINSTALL_CALL = 'function floaty:uninstall'
DES_ANCHOR = 'function mg:elyrace/uninstall'                      # dernière ligne de mg:desinstaller : on s'ajoute juste après


def include(ns, rel, trims=frozenset()):
    """rel = chemin posix sous data/<ns>/ ; True si le fichier est importé. trims = noms des trim_pattern propres à la carte."""
    name = rel.rsplit('/', 1)[-1]
    if '/' not in rel or name.startswith('.') or not name.endswith(('.mcfunction', '.json')):
        return False                                # .DS_Store, .bdstudio, fichiers hors dossier (utility/*.mcfunction)
    if name.endswith('.mcfunction') and not rel.startswith('function/'):
        return False
    if ns != 'minecraft':
        return True
    top = rel.split('/')[0]
    if top == 'tags':
        return name.startswith('hb_')               # tags propres à la carte ; les autres étendent des tags vanilla
    if top == 'trim_pattern':
        return True
    if top == 'recipe':                             # recette de trim seulement si le motif est à la carte (sinon : recette vanilla)
        return name.endswith('_armor_trim.json') and name[:-len('_armor_trim.json')] in trims
    return False                                    # advancement (écrase le vanilla), function (tick / load : voir generate)


def collect(pack, biomes=None, invalid=None):
    """[(ns, rel, Path)] triés des fichiers à importer (biomes -> ns 'minecraft', rel 'worldgen/biome/x.json').
    Un chemin hors [a-z0-9_./-] (majuscule, espace : id de ressource invalide, la carte d'origine ne le charge pas non plus)
    est écarté et ajouté à invalid."""
    out, trims = [], set()
    tp = pack / 'minecraft' / 'trim_pattern'
    if tp.is_dir():
        trims = {p.stem for p in tp.glob('*.json')}
    for nsdir in sorted(p for p in pack.iterdir() if p.is_dir()):
        if not O.NS.fullmatch(nsdir.name):              # « .git », « .. », majuscule... : jamais un dossier à écrire sous data/
            if invalid is not None:
                invalid.append(f'{nsdir.name}/')
            continue
        for p in sorted(q for q in nsdir.rglob('*') if q.is_file()):
            rel = p.relative_to(nsdir).as_posix()
            if not include(nsdir.name, rel, trims):
                continue
            if VALID_PATH.fullmatch(rel):
                out.append((nsdir.name, rel, p))
            elif invalid is not None:
                invalid.append(f'{nsdir.name}/{rel}')
    if biomes and biomes.is_dir():
        out += [('minecraft', 'worldgen/biome/' + p.name, p) for p in sorted(biomes.glob('*.json'))
                if p.stem not in SKIP_BIOMES and not p.name.startswith('.')]
    return out


def read_json(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))


def advancement_roots(items):
    """Ids des advancements sans parent dans les espaces de noms de la carte (racines des onglets : revoke from <racine> les couvre tous)."""
    return sorted(f'{ns}:{rel[len("advancement/"):-len(".json")]}' for ns, rel, p in items
                  if ns != 'minecraft' and rel.startswith('advancement/') and 'parent' not in read_json(p))


def terrain_targets(root):
    """Fonctions planifiées par les commandes du terrain : lignes de <root>/tools/floaty/terrain_sched.txt (écrit par build_terrain.py, trié ;
    # = commentaire). Fichier absent : aucune (le terrain n'a pas encore été reconstruit avec réécriture). Un id qui n'est pas `ns:chemin`
    avec des segments valides (R.valid_function_id : ni `..`, ni segment vide) : SystemExit, rien n'a été modifié (l'id sert de chemin de fichier)."""
    path = Path(root) / TERRAIN_SCHED
    if not path.is_file():
        return []
    ids = sorted({l.strip() for l in path.read_text(encoding='ascii').splitlines() if l.strip() and not l.startswith('#')})
    bad = [i for i in ids if not R.valid_function_id(i)]
    if bad:
        raise SystemExit(f'abandon (rien n\'a ete modifie) : {TERRAIN_SCHED.as_posix()} contient un id de fonction invalide : {bad[0]}')
    return ids


def read_lines(p):
    ls = p.read_text(encoding='utf-8-sig').split('\n')
    if ls and ls[-1] == '':
        ls.pop()
    return [l.rstrip('\r') for l in ls]


def rewrite_file(p, roots, st, fn_id=None):
    """Lignes réécrites du fichier p ; avec st.catchup (Registry) et fn_id, les témoins du rattrapage (fl_catchup) y sont ajoutés."""
    out = []
    for l in read_lines(p):
        out += R.rewrite_line(l, roots, st)
    reg = getattr(st, 'catchup', None)
    return CU.instrument(fn_id, out, reg) if reg is not None and fn_id else out


def json_text(p, ns, rel, st):
    """Texte LF du JSON à copier ; advancement de la carte : display.announce_to_chat forcé à false (pas d'annonce dans le chat du
    serveur) et critères restreints à la dimension (only_in_dimension)."""
    if ns == 'minecraft' or not rel.startswith('advancement/'):
        return p.read_text(encoding='utf-8-sig')           # lecture texte : CRLF -> LF
    d = read_json(p)
    disp = d.get('display')
    if isinstance(disp, dict) and disp.get('announce_to_chat') is not False:
        disp['announce_to_chat'] = False
        st.announce += 1
    st.criteria_total += len(d.get('criteria', {}))
    st.criteria += only_in_dimension(d)
    return json.dumps(d, indent=4, ensure_ascii=False) + '\n'


def only_in_dimension(adv):
    """Ajoute à chaque critère de l'advancement (dict) la condition joueur « dans mg:floaty » ; renvoie le nombre de critères modifiés.
    Hors minecraft:impossible (jamais déclenché que par `advancement grant`, pas par le jeu). Les conditions `player` existantes sont gardées
    (une liste de conditions loot est un ET) ; un critère déjà restreint n'est pas modifié une seconde fois."""
    n = 0
    for c in adv.get('criteria', {}).values():
        trigger = c.get('trigger') if isinstance(c, dict) else None
        if not trigger or str(trigger).removeprefix('minecraft:') == 'impossible':
            continue
        conds = c.setdefault('conditions', {})
        cur = conds.get('player')
        terms = [] if cur is None else cur if isinstance(cur, list) else [cur]
        if IN_DIMENSION not in terms:
            conds['player'] = terms + [IN_DIMENSION]
            n += 1
    return n


def render(items, pack, roots, spawn, st, n):
    """Tout ce qui sera écrit (sauf install / uninstall : voir generate), calculé EN MÉMOIRE (lectures et réécritures de la carte comprises) :
    une carte incomplète ou illisible lève ici, avant toute suppression. -> (fonctions [(ns, nom, lignes)], JSON [(chemin sous data/, texte)],
    ids des fonctions de la carte). tick / load absents de la carte : fonctions vides (une carte sans boucle est valable)."""
    fns, files, names = [], [], set()
    for ns, rel, p in items:
        if rel.endswith('.mcfunction'):
            name = rel[len('function/'):-len('.mcfunction')]
            fns.append((ns, name, rewrite_file(p, roots, st, f'{ns}:{name}')))
            names.add(f'{ns}:{name}')
            n['mcfunction'] += 1
        else:
            files.append((f'{ns}/{rel}', json_text(p, ns, rel, st)))
            n['json'] += 1
    for f in ('tick', 'load'):
        src = pack / 'minecraft' / 'function' / (f + '.mcfunction')
        head = f'# {f} de la carte Scourge (minecraft:{f}) : à appeler `execute in {R.DIM} positioned {" ".join(map(str, spawn))} run`'
        fns.append(('floaty', f'map/{f}', [head] + (rewrite_file(src, roots, st) if src.is_file() else ['# (absent de la carte)'])))
    fns += [('floaty', R.sched_name(fn).split(':', 1)[1], R.trampoline(fn, spawn)) for fn in sorted(st.sched)]
    files.append(('mg/dimension/floaty.json', json.dumps(DIMENSION, indent=2) + '\n'))
    return fns, files, names


def check_desinstaller(root):
    """mg:desinstaller doit exister et porter l'ancre (ou déjà l'appel) : sinon SystemExit, avant toute suppression."""
    des = mcfn.Fn(str(root / 'data' / 'mg' / 'function'))
    if not os.path.exists(des.path('desinstaller')):
        raise SystemExit('abandon (rien n\'a été supprimé) : data/mg/function/desinstaller.mcfunction introuvable')
    lines = des.lines_of('desinstaller')
    if UNINSTALL_CALL not in lines and lines.count(DES_ANCHOR) != 1:
        raise SystemExit(f'abandon (rien n\'a été supprimé) : desinstaller : ancre {DES_ANCHOR!r} trouvée {lines.count(DES_ANCHOR)} fois')
    return des


def generate(map_dir, root, adopt=False):
    """Importe la carte map_dir dans root/data ; renvoie (Stats, compteurs, spawn, racines, fonctions planifiées absentes).
    Les compteurs n portent aussi n['state'] : comptes de fl_state (objectifs, équipes, scores, bossbars, storage, écartés)."""
    root, pack = Path(root), Path(map_dir) / PACK
    st, n = R.Stats(), {'mcfunction': 0, 'json': 0}
    st.catchup = CU.Registry()                    # points de contrôle / avancements du groupe vus par rewrite_file (voir fl_catchup)
    items = collect(pack, Path(map_dir) / BIOMES, st.invalid)
    spawn = fl_nbt.spawn(fl_nbt.load(Path(map_dir) / 'level.dat'))
    roots = advancement_roots(items)
    namespaces = sorted({ns for ns, _, _ in items if ns != 'minecraft'})
    mc_files = sorted(f'data/minecraft/{rel}' for ns, rel, _ in items if ns == 'minecraft')
    st.sched |= set(terrain_targets(root))        # + cibles `schedule function` des commandes du terrain réécrites (build_terrain) : un trampoline chacune
    fns, files, names = render(items, pack, roots, spawn, st, n)
    state = fl_state.build(map_dir, R.AUTHOR, {fn: R.sched_name(fn) for fn in st.sched})    # après render : st.sched = les trampolines
    fns += [('floaty', 'install', state.install), ('floaty', 'uninstall', state.uninstall)]
    n['state'], n['sched_missing'], n['players'] = state.counts, state.sched_missing, state.players
    st.install = state.install                                    # lignes de floaty:install : wire en tire barres de boss et objectifs à critère
    des = check_desinstaller(root)
    dirs, owned = O.check(root, namespaces, mc_files, adopt)      # tous les garde-fous avant la moindre suppression
    O.clean(root, dirs, owned)
    O.save(root, namespaces, mc_files)                            # avant les écritures : un arrêt en cours de route reste relançable
    for ns, name, lines in fns:
        mcfn.Fn(str(root / 'data' / ns / 'function')).write(name, lines)
    for rel, text in files:
        dest = root / 'data' / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
    des.patch('desinstaller', DES_ANCHOR, [UNINSTALL_CALL])
    return st, n, spawn, roots, sorted(fn for fn in st.sched if fn not in names)


def prepare_wire(root):
    """Avant generate : tout ce que le branchement exige du pack existe (ancres des patchs, coffres de survie dont le coffre Floaty est la copie).
    -> source des coffres ; SystemExit (rien n'a été modifié) sinon."""
    fl_core.check(root)
    fn = mcfn.Fn(str(Path(root) / 'data' / 'mg' / 'function'))
    for k in ('save', 'load'):
        if not os.path.exists(fn.path(f'survie/vault_{k}')):
            raise SystemExit(f'abandon (rien n\'a été modifié) : survie/vault_{k}.mcfunction introuvable')
    vault = {k: fn.lines_of(f'survie/vault_{k}') for k in ('save', 'load')}
    fl_wire.vault_functions(vault)
    return vault


def wire(root, st, spawn, vault):
    """Après generate : écrit data/mg/function/floaty/* (fl_wire + rattrapage fl_catchup) et patche le coeur (fl_core) ; -> comptes du rattrapage."""
    mg = Path(root) / 'data' / 'mg' / 'function'
    fns = fl_wire.functions(st.install, spawn, CU.functions(st.catchup, spawn), vault)
    shutil.rmtree(mg / 'floaty', ignore_errors=True)               # fonctions générées uniquement : un passage = l'état courant
    fn = mcfn.Fn(str(mg))
    for rel, lines in sorted(fns.items()):
        fn.write(rel, lines)
    fl_core.apply(root)
    return st.catchup.counts()


def main():
    sys.stdout.reconfigure(encoding='utf-8')   # sortie console en UTF-8 (Windows : cp1252 sinon)
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--map', required=True, help='dossier de la carte extraite (contient level.dat et datapacks/)')
    ap.add_argument('--root', default=str(ROOT), help='racine du dépôt NeoMC (défaut : celle de ce script)')
    ap.add_argument('--adopt', action='store_true', help='premier passage : déclare possédés les data/<ns> déjà présents (voir fl_owned)')
    a = ap.parse_args()
    vault = prepare_wire(a.root)
    st, n, spawn, roots, missing = generate(a.map, Path(a.root), a.adopt)
    cu = wire(a.root, st, spawn, vault)
    fl_summary.show(st, n, spawn, roots, missing, cu, len(terrain_targets(a.root)))


if __name__ == '__main__':
    main()
