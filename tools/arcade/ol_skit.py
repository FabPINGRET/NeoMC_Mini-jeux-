"""🏰 Ombrelune : état partagé (SPOTS, DUNGEONS, ARENAS, LORE, CHESTS) et outils de construction (tours, créneaux, maisons).
Module importé par les modules ol_* de constructions et par la façade ol_structs.
"""
import math
import random

from tv_build import AIR
import ol_world as W


G = W.G
SPOTS = {}            # nom -> (x, y, z) (pieds), lieux utiles au jeu
DUNGEONS = {}         # clé -> dict (salles, portes, entrée, coffre)
ARENAS = {}           # clé -> dict (centre, rayon, points)
LORE = []             # (région, x, y, z) pages du grimoire
CHESTS = []           # (région, x, y, z) coffres cachés


def spot(name, x, y, z):
    SPOTS[name] = (x + 0.5, y, z + 0.5)


# ================================================================ outils génériques
def dir_vec(facing):
    return {'north': (0, -1), 'south': (0, 1), 'east': (1, 0), 'west': (-1, 0)}[facing]


def opp(facing):
    return {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}[facing]


def cone_roof(v, cx, cz, y, r, mat, h=None, tip='lightning_rod'):
    """Toit conique (tours rondes)."""
    h = h or r * 2
    for i in range(h):
        rr = r * (1 - i / h) + 0.3
        for x in range(math.floor(cx - rr), math.ceil(cx + rr) + 1):
            for z in range(math.floor(cz - rr), math.ceil(cz + rr) + 1):
                d = math.hypot(x - cx, z - cz)
                if rr - 1.2 < d <= rr:
                    v.set(x, y + i, z, mat)
    if tip:
        v.set(round(cx), y + h, round(cz), tip)


def round_tower(v, cx, cz, y0, r, h, wall, floor=None, windows='glass_pane', crenel=None, roof=None, roof_h=None, floors=()):
    for y in range(y0, y0 + h):
        for x in range(cx - r - 1, cx + r + 2):
            for z in range(cz - r - 1, cz + r + 2):
                d = math.hypot(x - cx, z - cz)
                if d <= r + 0.5:
                    if d > r - 0.6:
                        v.set(x, y, z, wall(x, y, z) if callable(wall) else wall)
                    else:
                        v.set(x, y, z, AIR)
    if floor:
        for fy in (y0 - 1,) + tuple(floors):
            for x in range(cx - r, cx + r + 1):
                for z in range(cz - r, cz + r + 1):
                    if math.hypot(x - cx, z - cz) <= r - 0.5:
                        v.set(x, fy, z, floor)
    for fy in floors:
        for k in range(4):
            a = math.pi / 2 * k + math.pi / 4
            wx, wz = round(cx + r * math.cos(a)), round(cz + r * math.sin(a))
            v.set(wx, fy + 2, wz, windows)
            v.set(wx, fy + 3, wz, windows)
    top = y0 + h
    if crenel:
        for x in range(cx - r - 1, cx + r + 2):
            for z in range(cz - r - 1, cz + r + 2):
                d = math.hypot(x - cx, z - cz)
                if r - 0.6 < d <= r + 0.5:
                    v.set(x, top, z, crenel if (x + z) % 2 == 0 else AIR)
                elif d <= r - 0.6:
                    v.set(x, top - 1, z, floor or wall)
    if roof:
        cone_roof(v, cx, cz, top, r + 1, roof, roof_h)


def crenels(v, x1, z1, x2, z2, y, mat):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for z in range(min(z1, z2), max(z1, z2) + 1):
            if (x + z) % 2 == 0:
                v.set(x, y, z, mat)


def flimsy(b):
    """Vrai si le bloc b (None = case vide) ne peut pas servir de dos à une échelle : air, escalier, dalle, vitre, barrière, muret,
    trappe, tapis, barreaux, lanterne, chaîne. Jamais une porte ni une autre échelle (dos à dos)."""
    name = b.split('[')[0] if b else None
    return name is None or name == AIR or name.endswith(('_stairs', '_slab', '_pane', '_fence', '_wall', '_trapdoor', '_carpet', 'lantern')) \
        or name in ('iron_bars', 'iron_chain')


def brace_ladders(v, mat):
    """Étaie chaque échelle : si la case derrière (dos de l'échelle) est flimsy (vide ou non porteuse), y pose mat."""
    for (x, y, z), b in list(v.v.items()):
        if not b.startswith('ladder[facing='):
            continue
        dx, dz = dir_vec(b[len('ladder[facing='):].split(',')[0].rstrip(']'))
        if flimsy(v.get(x - dx, y, z - dz)):
            v.set(x - dx, y, z - dz, mat)


LATE = frozenset({'ladder'})      # blocs à support émis après tout le reste de la structure (un plancher posé ensuite écraserait l'échelle)


def struct_cmds(v):
    """Commandes de construction d'une structure, telles que gen_ombrelune les écrit (échelles en fin de passe)."""
    return v.cmds(late=LATE)


def spiral_well(v, cx, cz, r, y1, y2, step, per_turn=12, head=3, keep=()):
    """Colimaçon praticable autour de (cx, cz), marches de y1 à y2 : la marche i (hauteur y1 + i) occupe tous les blocs de l'anneau
    r - 1.5 < d <= r + 0.5 dont l'angle (sens de Vox.spiral) tombe dans le secteur i % per_turn, donc deux marches consécutives se touchent
    par une face. Trois passes : (a) AIR sur les cases vides (None) de l'anneau élargi r - 2 < d <= r + 1, de y1 à y2 + head ;
    (b) AIR sur `head` cases au-dessus de chaque marche (perce les planchers), sauf cases de marche et blocs dont le nom est dans keep ;
    (c) pose des marches (sans remplacer un bloc keep : un tronc fait aussi une marche). Renvoie [(y, [(x, z), ...]), ...]."""
    def ring(lo, hi):
        n = math.ceil(hi)
        return [(x, z) for x in range(cx - n, cx + n + 1) for z in range(cz - n, cz + n + 1) if lo < math.hypot(x - cx, z - cz) <= hi]

    def kept(x, y, z):
        b = v.get(x, y, z)
        return b is not None and b.split('[')[0] in keep

    sectors = {}
    for (x, z) in ring(r - 1.5, r + 0.5):
        k = int((math.atan2(z - cz, x - cx) % (2 * math.pi)) * per_turn / (2 * math.pi) + 1e-9) % per_turn
        sectors.setdefault(k, []).append((x, z))
    steps = [(y1 + i, sectors.get(i % per_turn, [])) for i in range(y2 - y1 + 1)]
    for (x, z) in ring(r - 2, r + 1):
        for y in range(y1, y2 + head + 1):
            if v.get(x, y, z) is None:
                v.set(x, y, z, AIR)
    cells = {(x, y, z) for y, xz in steps for (x, z) in xz}
    for y, xz in steps:
        for (x, z) in xz:
            for yy in range(y + 1, y + head + 1):
                if (x, yy, z) not in cells and not kept(x, yy, z):
                    v.set(x, yy, z, AIR)
    for y, xz in steps:
        for (x, z) in xz:
            if not kept(x, y, z):
                v.set(x, y, z, step)
    return steps


def stone_mix(r, base='stone_bricks', moss='mossy_stone_bricks', crack='cracked_stone_bricks', pm=0.12, pc=0.08):
    def f(x, y, z):
        q = r.random()
        return moss if q < pm else (crack if q < pm + pc else base)
    return f


# ---------------------------------------------------------------- maison médiévale à colombages (intérieur meublé)
HOUSE_STYLES = [
    dict(frame='stripped_spruce_log', post='spruce_log', fill='white_terracotta', base='cobblestone', roof='spruce', roof_b='spruce_planks', floor='spruce_planks'),
    dict(frame='stripped_dark_oak_log', post='dark_oak_log', fill='smooth_sandstone', base='stone_bricks', roof='dark_oak', roof_b='dark_oak_planks', floor='oak_planks'),
    dict(frame='stripped_oak_log', post='oak_log', fill='mud_bricks', base='cobblestone', roof='deepslate_tile', roof_b='deepslate_tiles', floor='spruce_planks'),
    dict(frame='stripped_birch_log', post='birch_log', fill='calcite', base='stone_bricks', roof='brick', roof_b='bricks', floor='birch_planks'),
    dict(frame='stripped_spruce_log', post='spruce_log', fill='packed_mud', base='mossy_cobblestone', roof='mangrove', roof_b='mangrove_planks', floor='spruce_planks'),
]


def house(v, x1, z1, w, d, y, facing, style, floors=2, r=None, sign=None, shop=None):
    """Maison de w × d (extérieur), porte au milieu du côté facing. Renvoie la position devant la porte."""
    r = r or random.Random(x1 * 31 + z1)
    s = style
    x2, z2 = x1 + w - 1, z1 + d - 1
    fh = 4                                       # hauteur d'un étage
    top = y + fh * floors
    v.fill(x1, y, z1, x2, y, z2, s['base'])
    v.fill(x1 + 1, y, z1 + 1, x2 - 1, y, z2 - 1, s['floor'])
    for f in range(floors):
        yb = y + 1 + f * fh
        wall = s['base'] if f == 0 and r.random() < 0.5 else s['fill']
        v.walls(x1, z1, x2, z2, yb, yb + fh - 2, wall)
        v.fill(x1 + 1, yb, z1 + 1, x2 - 1, yb + fh - 2, z2 - 1, AIR)
        for x in list(range(x1, x2 + 1, 3)) + [x2]:
            v.fill(x, yb, z1, x, yb + fh - 2, z1, s['post'])
            v.fill(x, yb, z2, x, yb + fh - 2, z2, s['post'])
        for z in list(range(z1, z2 + 1, 3)) + [z2]:
            v.fill(x1, yb, z, x1, yb + fh - 2, z, s['post'])
            v.fill(x2, yb, z, x2, yb + fh - 2, z, s['post'])
        v.fill(x1, yb + fh - 1, z1, x2, yb + fh - 1, z1, f'{s["frame"]}[axis=x]')
        v.fill(x1, yb + fh - 1, z2, x2, yb + fh - 1, z2, f'{s["frame"]}[axis=x]')
        v.fill(x1, yb + fh - 1, z1, x1, yb + fh - 1, z2, f'{s["frame"]}[axis=z]')
        v.fill(x2, yb + fh - 1, z1, x2, yb + fh - 1, z2, f'{s["frame"]}[axis=z]')
        v.fill(x1 + 1, yb + fh - 1, z1 + 1, x2 - 1, yb + fh - 1, z2 - 1, s['floor'])
        # fenêtres (entre les poteaux)
        for x in range(x1 + 1, x2):
            if (x - x1) % 3 != 0:
                for z in (z1, z2):
                    if r.random() < 0.55:
                        v.set(x, yb + 1, z, 'glass_pane' if f else 'brown_stained_glass_pane')
        for z in range(z1 + 1, z2):
            if (z - z1) % 3 != 0:
                for x in (x1, x2):
                    if r.random() < 0.55:
                        v.set(x, yb + 1, z, 'glass_pane' if f else 'brown_stained_glass_pane')
        # mobilier
        cx, cz = (x1 + x2) // 2, (z1 + z2) // 2
        if f == floors - 1:
            v.bed(x1 + 1, yb, z1 + 2, 'north', r.choice(['red', 'blue', 'green', 'brown', 'cyan']))
            v.set(x1 + 2, yb, z1 + 1, 'chest[facing=south]')
        if f == 0:
            v.set(x2 - 1, yb, z2 - 1, r.choice(['furnace[facing=west]', 'smoker[facing=west]', 'barrel[facing=up]']))
            v.set(x2 - 1, yb, z1 + 1, 'crafting_table')
            v.table(cx, yb, cz)
            v.set(cx + 1, yb, cz, 'spruce_stairs[facing=west]')
            v.set(cx - 1, yb, cz, 'spruce_stairs[facing=east]')
        v.lamp(cx, yb + fh - 2, cz)
        if f < floors - 1:                        # échelle vers l'étage
            v.fill(x1 + 1, yb, z2 - 1, x1 + 1, yb + fh - 1, z2 - 1, 'ladder[facing=north]')
            v.set(x1 + 1, yb + fh - 1, z2 - 1, 'ladder[facing=north]')
    # porte
    dx, dz = dir_vec(facing)
    if facing in ('north', 'south'):
        dxp, dzp = (x1 + x2) // 2, (z1 if facing == 'north' else z2)
    else:
        dxp, dzp = (x1 if facing == 'west' else x2), (z1 + z2) // 2
    v.set(dxp, y + 1, dzp, AIR)
    v.set(dxp, y + 2, dzp, AIR)
    v.door(dxp, y + 1, dzp, facing, s['roof'] if s['roof'] in ('spruce', 'dark_oak', 'mangrove', 'oak', 'birch') else 'spruce')
    v.set(dxp + dx, y, dzp + dz, s['base'])
    v.set(dxp + dx, y + 3, dzp + dz, 'lantern[hanging=false]') if False else None
    if sign:
        v.set(dxp + dx + (1 if facing in ('north', 'south') else 0), y + 3, dzp + dz + (0 if facing in ('north', 'south') else 1),
              f'{sign}_wall_banner[facing={facing}]')
    # toit à pignon (faîtage le long du grand côté)
    axis = 'x' if w >= d else 'z'
    stairs = s['roof'] + '_stairs'
    slab = s['roof'] + '_slab'
    v.gable_roof(x1, z1, x2, z2, top, axis, stairs, slab, s['roof_b'])
    # cheminée
    if r.random() < 0.7:
        chx, chz = (x2 - 1, z1 + 1) if r.random() < 0.5 else (x1 + 1, z2 - 1)
        v.fill(chx, top, chz, chx, top + max(w, d) // 2 + 1, chz, 'bricks')
        v.set(chx, top + max(w, d) // 2 + 2, chz, 'campfire[lit=true,signal_fire=false]')
    # jardinière
    if r.random() < 0.6 and facing in ('north', 'south'):
        zz = z1 - 1 if facing == 'north' else z2 + 1
        for x in range(x1 + 1, x2):
            if abs(x - dxp) > 1 and r.random() < 0.6:
                v.set(x, y + 1 + fh, zz, 'spruce_trapdoor[facing=' + facing + ',half=top]')
                v.set(x, y + 2 + fh, zz, r.choice(['potted_red_tulip', 'potted_poppy', 'potted_blue_orchid', 'potted_allium']))
    return (dxp + dx * 2, y + 1, dzp + dz * 2)
