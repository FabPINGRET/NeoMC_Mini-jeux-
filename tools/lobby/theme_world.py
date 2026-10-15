"""Modèle du spawn pour les décors saisonniers (importé par gen_themes.py et les modules theme_*, jamais lancé seul).

load(F) relit les fonctions de construction du spawn (lobby/*build*, parkour/build) et remplit sur place W (bloc d'origine
de chaque position), DYN (zones modifiées ailleurs) et PLOTS : les autres modules peuvent donc importer ces noms avant
l'appel (load est idempotent). CH reçoit les remplacements d'un thème : (x, y, z) -> (bloc d'origine, bloc du thème), via change().
RESERVED : boîtes où rien n'est posé (ni bloc ni animal), cf. reserve() ; free() les exclut, change() et les points d'apparition
des animaux passent par free(). Règle : RESERVED est à l'appelant (reserve() avant ou après load(), load() n'y touche pas) ;
les socles d'élytra sont dans PAD_BOXES, reconstruit par load().
Contrainte : load() ignore les fonctions sous .../theme/ (setblock/fill des thèmes eux-mêmes) : tout fichier généré pour un
nouveau thème ou une nouvelle fonctionnalité doit donc rester sous lobby/theme/, sinon ses blocs seraient pris pour des zones
modifiées par un jeu.
"""
import glob
import os
import re

G = 63                                   # sol du spawn (pieds en y 64)
LIM = 78                                 # zone décorée : |x|, |z| <= LIM (forceload du spawn : -80..80)
LOBBY_BOX = 'x=-80,y=30,z=-80,dx=160,dy=120,dz=160'   # le spawn (volume de sélecteur)
LOBBY = f'@a[{LOBBY_BOX},tag=!mg.play,tag=!mg.surv,gamemode=!spectator]'

PLOTS = []                               # parcelles (jamais touchées) : (wx1, wx2, wz1, wz2)
CMD = re.compile(r'^(setblock|fill) (-?\d+) (-?\d+) (-?\d+)(?: (-?\d+) (-?\d+) (-?\d+))? (.+)$')
W = {}                                   # (x, y, z) -> bloc (l'air n'est pas stocké)
DYN = []                                 # boîtes modifiées ailleurs (jeux, animations) : on n'y touche pas
CH = {}                                  # (x, y, z) -> (bloc d'origine, bloc du thème), rempli par un thème
RESERVED = []                            # boîtes (x1, x2, y1, y2, z1, z2) sans décor ni animal (cf. reserve), jamais vidé par load
PAD_BOXES = []                           # idem, pour les socles d'élytra : reconstruit à chaque load
# socles du parcours d'élytra (elytra/build) : centre (x, z) ; panneaux flottants jusqu'à y 68, d'où la boîte de hauteur 9
ELYTRA_PADS = [(16, -9), (32, -15), (16, -21)]
PAD_MARGIN = 4                           # socle de 5x5 (±2) + 2 blocs autour


def reserve(x1, x2, y1, y2, z1, z2):
    """Interdit toute pose (blocs d'un thème, point d'apparition d'animal) dans cette boîte ; ex. les futurs PNJ du spawn."""
    RESERVED.append((min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2), min(z1, z2), max(z1, z2)))


def reserved(x, y, z):
    return any(a <= x <= b and c <= y <= d and e <= z <= f for a, b, c, d, e, f in RESERVED + PAD_BOXES)


def inplot(x, z):
    return any(a - 1 <= x <= b + 1 and c - 1 <= z <= d + 1 for a, b, c, d in PLOTS)


# ------------------------------------------------------------------ reconstitution des blocs du spawn
def block_and_mode(rest):
    depth = 0
    for i, ch in enumerate(rest):
        if ch in '[{':
            depth += 1
        elif ch in ']}':
            depth -= 1
        elif ch == ' ' and depth == 0:
            return rest[:i], rest[i + 1:].split(' ')
    return rest, []


def clip(a, b):
    return max(min(a, b), -LIM - 2), min(max(a, b), LIM + 2)


def apply(line, dynamic):
    m = CMD.match(line.strip())
    if not m:
        return
    x1, y1, z1 = int(m[2]), int(m[3]), int(m[4])
    x2, y2, z2 = (x1, y1, z1) if m[5] is None else (int(m[5]), int(m[6]), int(m[7]))
    xa, xb = clip(x1, x2)
    za, zb = clip(z1, z2)
    if xa > xb or za > zb:
        return
    ya, yb = min(y1, y2), max(y1, y2)
    blk, mode = block_and_mode(m[8])
    if dynamic or (m[1] == 'fill' and mode and mode[0] in ('replace', 'hollow', 'outline')):
        DYN.append((xa, xb, ya, yb, za, zb))
        return
    keep = bool(mode) and mode[0] == 'keep'
    air = blk in ('minecraft:air', 'air')
    for x in range(xa, xb + 1):
        for z in range(za, zb + 1):
            for y in range(ya, yb + 1):
                k = (x, y, z)
                if air:
                    W.pop(k, None)
                elif not (keep and k in W):
                    W[k] = blk


def num(p):
    m = re.search(r'build_(\d+)', p)
    return int(m[1]) if m else 99


def load(F):
    """F = dossier des fonctions (data/mg/function). À appeler avant toute lecture de W, DYN, PLOTS ; rappelable (repart de zéro)."""
    for d in (PLOTS, W, DYN, PAD_BOXES):
        d.clear()
    for x, z in ELYTRA_PADS:
        PAD_BOXES.append((x - PAD_MARGIN, x + PAD_MARGIN, G, G + 8, z - PAD_MARGIN, z + PAD_MARGIN))
    for l in open(os.path.join(F, 'plot', 'build_all.mcfunction'), encoding='utf-8'):
        m = re.search(r'wx1:(-?\d+),wx2:(-?\d+),wz1:(-?\d+),wz2:(-?\d+)', l)
        if m:
            PLOTS.append(tuple(int(v) for v in m.groups()))
    base = sorted(glob.glob(os.path.join(F, 'lobby', 'build_*.mcfunction')), key=num)
    base += [p for p in sorted(glob.glob(os.path.join(F, 'lobby', '*build*.mcfunction')))
             if p not in base and not p.endswith(os.sep + 'build.mcfunction')]
    base.append(os.path.join(F, 'parkour', 'build.mcfunction'))
    for p in base:
        for l in open(p, encoding='utf-8'):
            apply(l, False)
    for p in glob.glob(os.path.join(F, '**', '*.mcfunction'), recursive=True):
        if p in base or (os.sep + 'theme' + os.sep) in p or p.endswith(os.sep + 'desinstaller.mcfunction'):
            continue
        with open(p, encoding='utf-8') as f:
            lines = f.readlines()
        if lines and 'dimension mg:' in lines[0]:      # construit dans une autre dimension (ex. terra/b) : hors lobby
            continue
        for l in lines:
            if l.startswith(('setblock ', 'fill ')):
                apply(l, True)


def dyn(x, y, z):
    return any(a <= x <= b and c <= y <= d and e <= z <= f for a, b, c, d, e, f in DYN)


# ------------------------------------------------------------------ blocs : id, états, familles
def bid(b):
    return (b or 'minecraft:air').split('[')[0].split('{')[0]


def states(b):
    m = re.search(r'\[([^\]]*)\]', b or '')
    return dict(kv.split('=') for kv in m[1].split(',')) if m and m[1] else {}


PLANTS = {'minecraft:short_grass', 'minecraft:fern', 'minecraft:pink_petals', 'minecraft:dandelion', 'minecraft:poppy',
          'minecraft:blue_orchid', 'minecraft:allium', 'minecraft:azure_bluet', 'minecraft:red_tulip', 'minecraft:orange_tulip',
          'minecraft:white_tulip', 'minecraft:pink_tulip', 'minecraft:oxeye_daisy', 'minecraft:cornflower',
          'minecraft:lily_of_the_valley'}
FLOWERS = PLANTS - {'minecraft:short_grass', 'minecraft:fern', 'minecraft:pink_petals'}
NOT_SOLID = PLANTS | {'minecraft:air', 'minecraft:light', 'minecraft:barrier', 'minecraft:water', 'minecraft:vine',
                      'minecraft:glow_lichen', 'minecraft:lantern', 'minecraft:spore_blossom', 'minecraft:bamboo',
                      'minecraft:pointed_dripstone'}
GROUND = {'minecraft:grass_block', 'minecraft:moss_block', 'minecraft:podzol', 'minecraft:coarse_dirt', 'minecraft:dirt',
          'minecraft:rooted_dirt'}
DIRT = GROUND - {'minecraft:grass_block', 'minecraft:moss_block'}
WALLS = {'minecraft:stone_bricks', 'minecraft:mossy_stone_bricks', 'minecraft:cracked_stone_bricks', 'minecraft:spruce_planks',
         'minecraft:deepslate_tiles', 'minecraft:polished_deepslate', 'minecraft:cobbled_deepslate', 'minecraft:cobblestone',
         'minecraft:mossy_cobblestone', 'minecraft:stone', 'minecraft:tuff', 'minecraft:deepslate', 'minecraft:andesite',
         'minecraft:spruce_log', 'minecraft:dark_oak_log', 'minecraft:oak_log', 'minecraft:stripped_spruce_log'}
# surfaces pleines où la neige tient (le haut d'un bloc entier)
SNOWABLE = GROUND | WALLS | {'minecraft:dirt_path', 'minecraft:packed_mud', 'minecraft:calcite', 'minecraft:smooth_quartz',
                             'minecraft:polished_andesite', 'minecraft:polished_diorite', 'minecraft:white_concrete',
                             'minecraft:gray_concrete'}


def solid(x, y, z):
    return bid(W.get((x, y, z))) not in NOT_SOLID


def free(x, y, z):
    return abs(x) <= LIM and abs(z) <= LIM and not inplot(x, z) and not dyn(x, y, z) and not reserved(x, y, z)


TUFT = ('minecraft:air', 'minecraft:short_grass', 'minecraft:fern')     # ce qu'on peut remplacer au-dessus du sol


def tuft_free(up):
    """La case up (au-dessus d'un sol) est de l'air ou une touffe, sans bloc au-dessus et pas encore changée par le thème."""
    return bid(W.get(up)) in TUFT and (up[0], up[1] + 1, up[2]) not in W and up not in CH


def canopy(r=2):
    """Colonne (x, z) -> plus haut feuillage à r blocs près (horizontalement)."""
    top = {}
    for (x, y, z), b in W.items():
        if bid(b).endswith('_leaves'):
            for a in range(-r, r + 1):
                for c in range(-r, r + 1):
                    top[(x + a, z + c)] = max(top.get((x + a, z + c), y), y)
    return top


def opening(k):
    return k not in W or bid(W[k]) in PLANTS


def change(k, new):
    if k not in CH and free(*k):
        CH[k] = (W.get(k, 'minecraft:air'), new)
