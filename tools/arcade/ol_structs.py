"""🏰 Ombrelune : constructions (cité de Havreclair, villages, repaires des boss, donjons). Module importé par gen_ombrelune.py.

Chaque bâtisseur remplit un Vox (tv_build) en coordonnées absolues. Les lieux utiles au jeu (PNJ, balises, coffres, leviers,
arènes, salles des donjons) sont notés dans SPOTS / DUNGEONS / ARENAS.
"""
import math
import random
import zlib

from tv_build import Vox, AIR
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


def brace_ladders(v, mat):
    """Étaie chaque échelle : si la case derrière (dos de l'échelle) est vide ou non porteuse (air, escalier, dalle, vitre, barrière,
    muret, trappe, tapis, barreaux, lanterne, chaîne), y pose mat. Jamais une porte ni une autre échelle (dos à dos)."""
    for (x, y, z), b in list(v.v.items()):
        if not b.startswith('ladder[facing='):
            continue
        dx, dz = dir_vec(b[len('ladder[facing='):].split(',')[0].rstrip(']'))
        back = v.get(x - dx, y, z - dz)
        name = back.split('[')[0] if back else None
        if name is None or name == AIR or name.endswith(('_stairs', '_slab', '_pane', '_fence', '_wall', '_trapdoor', '_carpet', 'lantern')) \
                or name in ('iron_bars', 'iron_chain'):
            v.set(x - dx, y, z - dz, mat)


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


# ================================================================ HAVRECLAIR
def city():
    v = Vox(101)
    r = v.r
    Y = G
    WALL = 58
    sm = stone_mix(r)
    # ---- sol : douves, pavés
    for x in range(-67, 68):
        for z in range(-67, 68):
            m = max(abs(x), abs(z))
            if 61 <= m <= 65:
                v.fill(x, Y - 4, z, x, Y - 4, z, 'mud')
                v.fill(x, Y - 3, z, x, Y - 1, z, 'water')
                v.set(x, Y, z, AIR)
            elif m in (60, 66):
                v.fill(x, Y - 3, z, x, Y, z, 'stone_bricks' if m == 60 else 'mossy_cobblestone')
    # rues : croix principale, rue circulaire, place
    for x in range(-WALL + 3, WALL - 2):
        for z in range(-WALL + 3, WALL - 2):
            m = max(abs(x), abs(z))
            road = abs(x) <= 3 or abs(z) <= 3 or 50 <= m <= 53
            if road:
                q = r.random()
                v.set(x, Y, z, 'stone_bricks' if q < 0.5 else ('cobblestone' if q < 0.8 else ('andesite' if q < 0.93 else 'mossy_cobblestone')))
            else:
                v.set(x, Y, z, 'grass_block')
    for x in range(-14, 15):
        for z in range(-14, 15):
            d = math.hypot(x, z)
            if d <= 13.5:
                ring = int(d) % 4
                v.set(x, Y, z, ['polished_andesite', 'chiseled_stone_bricks' if (x + z) % 2 else 'stone_bricks', 'polished_diorite', 'smooth_stone'][ring])
    # fontaine et statue du Chevalier de l'Aube
    for x in range(-5, 6):
        for z in range(-5, 6):
            d = math.hypot(x, z)
            if d <= 5.4:
                v.set(x, Y, z, 'chiseled_stone_bricks' if d > 4.4 else 'water')
                if 4.4 < d <= 5.4:
                    v.set(x, Y + 1, z, 'stone_brick_wall')
                if d <= 4.4:
                    v.set(x, Y - 1, z, 'prismarine_bricks')
    v.fill(-1, Y, -1, 1, Y + 2, 1, 'chiseled_quartz_block')
    v.fill(0, Y + 3, 0, 0, Y + 5, 0, 'quartz_pillar')
    v.set(0, Y + 6, 0, 'gold_block')
    v.fill(-1, Y + 4, 0, 1, Y + 4, 0, 'quartz_slab[type=top]')
    v.set(0, Y + 7, 0, 'end_rod')
    for (x, z) in ((-2, 0), (2, 0), (0, -2), (0, 2)):
        v.set(x, Y + 1, z, 'water')
    spot('plaza', 0, Y + 1, 8)
    spot('waystone_hub', 6, Y + 1, 6)
    v.set(6, Y + 1, 6, 'lodestone')
    v.set(6, Y + 2, 6, 'amethyst_cluster[facing=up]')
    # lampadaires des rues
    for k in range(-50, 51, 10):
        if abs(k) > 14:
            for (x, z) in ((4, k), (-4, k), (k, 4), (k, -4)):
                v.set(x, Y + 1, z, 'polished_blackstone_wall')
                v.set(x, Y + 2, z, 'polished_blackstone_wall')
                v.set(x, Y + 3, z, 'lantern')
    for a in range(0, 360, 45):
        x, z = round(12 * math.cos(math.radians(a))), round(12 * math.sin(math.radians(a)))
        v.fill(x, Y + 1, z, x, Y + 2, z, 'spruce_fence')
        v.set(x, Y + 3, z, 'lantern')
    # ---- remparts
    for x in range(-WALL, WALL + 1):
        for z in range(-WALL, WALL + 1):
            m = max(abs(x), abs(z))
            if WALL - 2 <= m <= WALL:
                v.fill(x, Y - 3, z, x, Y + 9, z, sm)
                if m == WALL:
                    v.set(x, Y + 10, z, 'stone_brick_wall' if (x + z) % 2 else AIR)
                    if (x + z) % 2 == 0:
                        v.set(x, Y + 10, z, 'stone_bricks')
                        v.set(x, Y + 11, z, 'stone_brick_slab')
                elif m == WALL - 2:
                    v.set(x, Y + 10, z, 'stone_brick_wall')
                v.set(x, Y + 9, z, 'stone_bricks' if m < WALL else v.get(x, Y + 9, z))
    # meurtrières
    for k in range(-WALL + 4, WALL - 3, 4):
        for (x, z) in ((k, -WALL), (k, WALL), (-WALL, k), (WALL, k)):
            v.set(x, Y + 6, z, 'iron_bars')
    # tours d'angle et de flanc
    for (cx, cz) in [(-WALL, -WALL), (WALL, -WALL), (-WALL, WALL), (WALL, WALL), (-WALL, -29), (-WALL, 29), (WALL, -29), (WALL, 29),
                     (-29, -WALL), (29, -WALL), (-29, WALL), (29, WALL)]:
        corner = abs(cx) == WALL and abs(cz) == WALL
        rr = 5 if corner else 4
        round_tower(v, cx, cz, Y - 3, rr, 17 if corner else 15, sm, floor='spruce_planks', floors=(Y + 6,),
                    crenel='stone_bricks', roof='blue_terracotta' if corner else None, roof_h=9)
        v.lamp(cx, Y + 12, cz)
    # portes (N, S, E, O) : passage 5 de large, herse, tours de flanc
    for facing, (gx, gz) in (('north', (0, -WALL)), ('south', (0, WALL)), ('west', (-WALL, 0)), ('east', (WALL, 0))):
        along_x = facing in ('north', 'south')
        for k in range(-2, 3):
            for t in range(-2, 1):
                x, z = (gx + k, gz + t * (1 if gz > 0 else -1)) if along_x else (gx + t * (1 if gx > 0 else -1), gz + k)
                v.fill(x, Y + 1, z, x, Y + 6, z, AIR)
                v.set(x, Y, z, 'stone_bricks')
        for k in (-6, 6):
            x, z = (gx + k, gz) if along_x else (gx, gz + k)
            round_tower(v, x, z, Y - 3, 2, 15, sm, floor='spruce_planks', crenel='stone_bricks')
        # arche
        for k in range(-2, 3):
            x, z = (gx + k, gz) if along_x else (gx, gz + k)
            v.set(x, Y + 7, z, 'chiseled_stone_bricks' if k == 0 else 'stone_bricks')
            v.set(x, Y + 6, z, 'iron_bars' if abs(k) <= 1 else 'stone_brick_stairs[facing=' + ('east' if (k < 0) == along_x else 'west') + ',half=top]'
                  if along_x else 'iron_bars')
        bx, bz = (gx + 0, gz) if along_x else (gx, gz)
        for k in (-4, 4):
            x, z = (gx + k, gz + (1 if gz < 0 else -1) * -1) if along_x else (gx + (1 if gx < 0 else -1) * -1, gz + k)
            v.set(x, Y + 5, z, 'blue_wall_banner[facing=' + facing + ']')
        # pont sur les douves
        for t in range(1, 10):
            for k in range(-2, 3):
                dx_, dz_ = dir_vec(facing)
                x, z = (gx + k + dx_ * t, gz + dz_ * t) if along_x else (gx + dx_ * t, gz + k + dz_ * t)
                v.set(x, Y, z, 'spruce_planks' if abs(k) < 2 else 'stripped_spruce_log[axis=' + ('z' if along_x else 'x') + ']')
                v.set(x, Y - 1, z, AIR if 3 <= t <= 7 else 'stone_bricks')
                if abs(k) == 2:
                    v.set(x, Y + 1, z, 'spruce_fence')
                    if t in (1, 9):
                        v.set(x, Y + 2, z, 'lantern')
        spot('gate_' + facing, gx + dir_vec(facing)[0] * 12, Y + 1, gz + dir_vec(facing)[1] * 12)
    # ---- château (nord)
    castle(v, Y)
    temple(v, Y)
    mage_tower(v, Y)
    guild(v, Y)
    tavern(v, Y)
    forge_b(v, Y)
    market(v, Y)
    stables(v, Y)
    alchemist(v, Y)
    # ---- maisons (quartiers restants)
    taken = [(-22, -50, 22, -24), (22, -46, 45, -18), (-42, -42, -26, -26), (-46, -18, -20, -2), (-46, 6, -22, 26), (20, 6, 42, 24),
             (14, -15, 46, -4), (22, 28, 44, 46), (-46, 28, -28, 44)]
    houses = []
    rh = random.Random(77)

    def free(box):
        if any(not (box[2] < a or box[0] > c or box[3] < b or box[1] > d) for (a, b, c, d) in taken):
            return False
        if max(abs(box[0]), abs(box[2]), abs(box[1]), abs(box[3])) > 48:
            return False
        if box[0] <= 4 and box[2] >= -4:
            return False
        if any(math.hypot(px_, pz_) < 15 for px_ in (box[0], box[2]) for pz_ in (box[1], box[3])):
            return False
        return not (box[1] <= 4 and box[3] >= -4)
    # rangées de maisons mitoyennes le long des rues (façade sur la rue)
    ROWS = [('z', 5, 'west'), ('z', -11, 'east'), ('x', 5, 'north'), ('x', -11, 'south'),
            ('x', -49, 'north'), ('x', 43, 'south'), ('z', -49, 'west'), ('z', 43, 'east')]
    for axis, band, facing in ROWS:
        t = -49
        while t < 49:
            w_ = rh.randint(5, 7)
            if axis == 'z':                      # rangée le long de z, profondeur selon x
                x1, z1, ww, dd = band, t, 7, w_
            else:
                x1, z1, ww, dd = t, band, w_, 7
            box = (x1, z1, x1 + ww - 1, z1 + dd - 1)
            if free(box):
                taken.append(box)
                houses.append(house(v, x1, z1, ww, dd, Y, facing, rh.choice(HOUSE_STYLES), floors=rh.choice([2, 2, 3]), r=rh))
                t += w_
            else:
                t += 1
    for _ in range(6000):
        w_, d_ = rh.randint(5, 8), rh.randint(5, 8)
        x1, z1 = rh.randint(-48, 48 - w_), rh.randint(-48, 48 - d_)
        box = (x1 - 1, z1 - 1, x1 + w_, z1 + d_)
        if not free(box):
            continue
        cx, cz = x1 + w_ // 2, z1 + d_ // 2
        # porte vers la rue la plus proche (croix ou rue circulaire)
        cands = [(abs(cx) - 4, 'west' if cx > 0 else 'east'), (abs(cz) - 4, 'north' if cz > 0 else 'south'),
                 (50 - abs(cx), 'east' if cx > 0 else 'west'), (50 - abs(cz), 'south' if cz > 0 else 'north')]
        facing = min(cands)[1]
        taken.append(box)
        houses.append(house(v, x1, z1, w_, d_, Y, facing, rh.choice(HOUSE_STYLES), floors=rh.choice([1, 2, 2, 3]), r=rh))
    # jardinets et arbres dans ce qui reste
    for _ in range(600):
        x, z = rh.randint(-48, 48), rh.randint(-48, 48)
        if free((x - 1, z - 1, x + 1, z + 1)) and v.get(x, Y, z) == 'grass_block' and v.get(x, Y + 1, z) is None:
            q = rh.random()
            if q < 0.08:
                v.fill(x, Y + 1, z, x, Y + 4, z, 'oak_log')
                for dx in range(-2, 3):
                    for dz in range(-2, 3):
                        for dy in (4, 5, 6):
                            if abs(dx) + abs(dz) + (dy - 4) <= 3 and v.get(x + dx, Y + dy, z + dz) is None:
                                v.set(x + dx, Y + dy, z + dz, 'oak_leaves[persistent=true]')
                taken.append((x - 2, z - 2, x + 2, z + 2))
            elif q < 0.5:
                v.set(x, Y + 1, z, rh.choice(['short_grass', 'poppy', 'dandelion', 'cornflower', 'oxeye_daisy', 'azure_bluet', 'bush', 'short_grass']))
    # un lampadaire devant une porte de maison la bloque : on l'enlève (AIR explicite, le monde est déjà construit)
    for k in range(-50, 51, 10):
        if abs(k) > 14:
            for (x, z) in ((4, k), (-4, k), (k, 4), (k, -4)):
                if any('_door[' in (v.get(x + ddx, Y + 1, z + ddz) or '') for ddx, ddz in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    v.fill(x, Y + 1, z, x, Y + 3, z, AIR)
    # échelles intérieures des maisons : dos étayé
    brace_ladders(v, 'stripped_spruce_log')
    SPOTS['city_houses'] = houses
    # arbres et jardins dans les espaces verts
    return v


def castle(v, Y):
    r = random.Random(5)
    sm = stone_mix(r, 'stone_bricks', 'mossy_stone_bricks', 'cracked_stone_bricks', 0.06, 0.05)
    x1, z1, x2, z2 = -20, -50, 20, -26
    # cour et enceinte intérieure
    v.fill(x1, Y, z1, x2, Y, z2, 'polished_andesite')
    v.walls(x1, z1, x2, z2, Y + 1, Y + 6, sm)
    crenels(v, x1, z1, x2, z1, Y + 7, 'stone_bricks')
    crenels(v, x1, z2, x2, z2, Y + 7, 'stone_bricks')
    crenels(v, x1, z1, x1, z2, Y + 7, 'stone_bricks')
    crenels(v, x2, z1, x2, z2, Y + 7, 'stone_bricks')
    v.fill(-2, Y + 1, z2, 2, Y + 5, z2, AIR)
    v.fill(-2, Y + 6, z2, 2, Y + 6, z2, 'chiseled_stone_bricks')
    for x in (-3, 3):
        v.set(x, Y + 4, z2 + 1, 'blue_wall_banner[facing=south]')
    # donjon
    kx1, kz1, kx2, kz2 = -13, -47, 13, -31
    v.fill(kx1, Y, kz1, kx2, Y, kz2, 'polished_deepslate')
    for f, (ya, yb) in enumerate(((Y + 1, Y + 8), (Y + 9, Y + 15), (Y + 16, Y + 21))):
        v.walls(kx1, kz1, kx2, kz2, ya, yb, sm)
        v.fill(kx1 + 1, ya + (1 if f else 0), kz1 + 1, kx2 - 1, yb, kz2 - 1, AIR)   # sans effacer le plancher de l'étage du dessous
        v.fill(kx1 + 1, yb + 1, kz1 + 1, kx2 - 1, yb + 1, kz2 - 1, 'dark_oak_planks')
        for x in range(kx1 + 3, kx2 - 1, 4):
            v.fill(x, ya + 2, kz1, x, ya + 4, kz1, 'blue_stained_glass_pane' if f else 'glass_pane')
            if f or abs(x) > 3:   # pas de vitre au-dessus de la porte
                v.fill(x, ya + 2, kz2, x, ya + 4, kz2, 'blue_stained_glass_pane' if f else 'glass_pane')
    v.fill(kx1, Y + 22, kz1, kx2, Y + 22, kz2, 'stone_bricks')
    crenels(v, kx1, kz1, kx2, kz1, Y + 23, 'stone_bricks')
    crenels(v, kx1, kz2, kx2, kz2, Y + 23, 'stone_bricks')
    crenels(v, kx1, kz1, kx1, kz2, Y + 23, 'stone_bricks')
    crenels(v, kx2, kz1, kx2, kz2, Y + 23, 'stone_bricks')
    # salle du trône (rez-de-chaussée)
    v.fill(-1, Y, kz1 + 2, 1, Y, kz2, 'red_carpet' if False else 'red_wool')
    v.fill(-1, Y + 1, kz1 + 2, 1, Y + 1, kz2 - 1, 'red_carpet')
    v.fill(-2, Y + 1, kz1 + 1, 2, Y + 1, kz1 + 2, 'polished_deepslate')
    v.set(0, Y + 2, kz1 + 1, 'dark_oak_stairs[facing=south]')
    v.set(-1, Y + 2, kz1 + 1, 'gold_block')
    v.set(1, Y + 2, kz1 + 1, 'gold_block')
    v.fill(-1, Y + 3, kz1 + 1, 1, Y + 4, kz1 + 1, 'blue_wool')
    for x in (-8, -4, 4, 8):
        v.fill(x, Y + 1, kz1 + 3, x, Y + 8, kz1 + 3, 'quartz_pillar')
        v.fill(x, Y + 1, kz2 - 3, x, Y + 8, kz2 - 3, 'quartz_pillar')
        v.set(x, Y + 6, kz1 + 4, 'blue_wall_banner[facing=south]')
    for x in range(-10, 11, 5):
        v.lamp(x, Y + 7, (kz1 + kz2) // 2, kind='lantern')
    v.fill(-2, Y + 1, kz2, 2, Y + 4, kz2, AIR)
    v.door(-1, Y + 1, kz2, 'south', 'dark_oak', width=1)
    v.door(1, Y + 1, kz2, 'south', 'dark_oak', width=1)
    v.set(0, Y + 1, kz2, AIR)
    spot('throne', 0, Y + 1, kz1 + 4)
    spot('regent', 2, Y + 1, kz1 + 3)
    # tours du donjon
    for (cx, cz) in ((kx1, kz1), (kx2, kz1), (kx1, kz2), (kx2, kz2)):
        round_tower(v, cx, cz, Y + 1, 3, 26, sm, floor='spruce_planks', crenel='stone_bricks', roof='blue_terracotta', roof_h=8)
    # escalier intérieur
    v.stair_run(kx2 - 2, Y + 1, kz2 - 4, 0, -1, 9, 'dark_oak_stairs', 'north', support='stone_bricks')   # pied hors de l'anneau de la tour SE
    v.fill(kx2 - 2, Y + 9, kz1 + 5, kx2 - 2, Y + 9, kz2 - 4, AIR)
    # étage 2 -> 3 : volée du côté ouest, en sens inverse
    v.stair_run(kx1 + 2, Y + 10, kz1 + 5, 0, 1, 7, 'dark_oak_stairs', 'south', support='stone_bricks')
    v.fill(kx1 + 2, Y + 16, kz1 + 5, kx1 + 2, Y + 16, kz2 - 6, AIR)
    # bannières et drapeaux
    v.fill(0, Y + 23, (kz1 + kz2) // 2, 0, Y + 30, (kz1 + kz2) // 2, 'spruce_fence')
    v.fill(1, Y + 28, (kz1 + kz2) // 2, 3, Y + 30, (kz1 + kz2) // 2, 'blue_wool')
    # caserne (contre l'enceinte ouest de la cour)
    v.fill(x1 + 1, Y + 1, z2 - 6, x1 + 7, Y + 4, z2 - 1, 'spruce_planks', hollow=True)
    v.fill(x1 + 1, Y + 5, z2 - 6, x1 + 7, Y + 5, z2 - 1, 'spruce_slab')
    v.set(x1 + 7, Y + 1, z2 - 3, AIR)
    v.set(x1 + 7, Y + 2, z2 - 3, AIR)
    for z in range(z2 - 5, z2 - 1, 2):
        v.bed(x1 + 2, Y + 1, z, 'west', 'blue')
    for z in range(z2 - 5, z2 - 1):
        v.set(x1 + 9, Y + 1, z, 'armor_stand' if False else 'spruce_fence')
    spot('aldric', 6, Y + 1, z2 - 4)
    # jardin de la cour
    for x in range(14, 23):
        for z in range(z2 - 5, z2):
            v.set(x, Y, z, 'grass_block')
            if (x + z) % 3 == 0:
                v.set(x, Y + 1, z, r.choice(['rose_bush', 'peony', 'lilac']) + '[half=lower]')
                v.set(x, Y + 2, z, v.get(x, Y + 1, z).replace('lower', 'upper'))


def temple(v, Y):
    """Temple de l'Aube (nord-est) : nef, vitraux, clocher, autel de la Pierre-Lune."""
    r = random.Random(6)
    x1, z1, x2, z2 = 24, -44, 43, -20
    mat = lambda x, y, z: 'calcite' if r.random() < 0.7 else 'smooth_quartz'
    v.fill(x1, Y, z1, x2, Y, z2, 'polished_diorite')
    # nef (le long de z)
    nx1, nx2 = 28, 39
    v.walls(nx1, z1, nx2, z2, Y + 1, Y + 12, mat)
    v.fill(nx1 + 1, Y + 1, z1 + 1, nx2 - 1, Y + 12, z2 - 1, AIR)
    for z in range(z1 + 2, z2 - 1, 4):
        v.fill(nx1, Y + 3, z, nx1, Y + 9, z, 'yellow_stained_glass_pane')
        v.fill(nx2, Y + 3, z, nx2, Y + 9, z, 'orange_stained_glass_pane')
        v.fill(nx1, Y + 1, z + 2, nx1, Y + 12, z + 2, 'quartz_pillar')
        v.fill(nx2, Y + 1, z + 2, nx2, Y + 12, z + 2, 'quartz_pillar')
    # rosace (pignon sud)
    for y in range(Y + 4, Y + 12):
        for x in range(nx1 + 1, nx2):
            d = math.hypot(x - 33, y - (Y + 8))
            if d < 3.6:
                v.set(x, y, z2, 'magenta_stained_glass_pane' if d < 1.5 else ('yellow_stained_glass_pane' if d < 2.6 else 'light_blue_stained_glass_pane'))
    v.gable_roof(nx1, z1, nx2, z2, Y + 13, 'z', 'deepslate_tile_stairs', 'deepslate_tile_slab', 'deepslate_tiles')
    # transept
    v.walls(x1, -34, x2, -28, Y + 1, Y + 10, mat)
    v.fill(x1 + 1, Y + 1, -33, x2 - 1, Y + 10, -29, AIR)
    v.fill(nx1 + 1, Y + 1, -33, nx2 - 1, Y + 10, -29, AIR)
    v.gable_roof(x1, -34, x2, -28, Y + 11, 'x', 'deepslate_tile_stairs', 'deepslate_tile_slab', 'deepslate_tiles')
    # entrée (sud)
    v.fill(31, Y + 1, z2, 35, Y + 4, z2, AIR)
    v.fill(31, Y + 5, z2, 35, Y + 5, z2, 'chiseled_quartz_block')
    # bancs, tapis, autel
    v.fill(32, Y + 1, z1 + 4, 34, Y + 1, z2 - 1, 'yellow_carpet')
    for z in range(z1 + 9, z2 - 2, 2):
        for x in (30, 31, 36, 37):
            v.set(x, Y + 1, z, 'spruce_stairs[facing=north]')
    v.fill(31, Y + 1, z1 + 2, 35, Y + 1, z1 + 3, 'polished_diorite')
    v.fill(32, Y + 2, z1 + 2, 34, Y + 2, z1 + 2, 'chiseled_quartz_block')
    v.set(33, Y + 3, z1 + 2, 'amethyst_cluster[facing=up]')
    v.set(33, Y + 2, z1 + 3, 'enchanting_table')
    spot('altar', 33, Y + 1, z1 + 5)
    spot('liora_t', 35, Y + 1, z1 + 5)
    for x in (30, 37):
        v.set(x, Y + 1, z1 + 2, 'candle[candles=4,lit=true]')
    for z in range(z1 + 4, z2 - 1, 6):
        v.lamp(33, Y + 11, z, kind='soul_lantern' if False else 'lantern')
    # clocher (coin sud-ouest)
    v.fill(nx1 - 4, Y + 1, z2 - 4, nx1, Y + 22, z2, mat)
    v.fill(nx1 - 3, Y + 1, z2 - 3, nx1 - 1, Y + 22, z2 - 1, AIR)
    for (x, z) in ((nx1 - 2, z2 - 4), (nx1 - 2, z2), (nx1 - 4, z2 - 2), (nx1, z2 - 2)):
        v.fill(x, Y + 17, z, x, Y + 20, z, AIR)
    v.set(nx1 - 2, Y + 20, z2 - 2, 'bell[attachment=ceiling,facing=north]')
    v.fill(nx1 - 2, Y + 21, z2 - 2, nx1 - 2, Y + 21, z2 - 2, 'iron_chain')
    cone_roof(v, nx1 - 2, z2 - 2, Y + 23, 3, 'deepslate_tiles', 8, 'lightning_rod')


def mage_tower(v, Y):
    r = random.Random(8)
    cx, cz = -34, -34
    wall = lambda x, y, z: 'purpur_block' if (y % 7 == 0) else ('deepslate_bricks' if r.random() < 0.8 else 'cracked_deepslate_bricks')
    round_tower(v, cx, cz, Y + 1, 6, 34, wall, floor='dark_oak_planks', floors=(Y + 9, Y + 17, Y + 25), roof='purple_terracotta', roof_h=14)
    v.spiral(cx, cz, 4, Y + 1, Y + 33, 'polished_deepslate_slab[type=top]', per_turn=16)
    for fy in (Y + 9, Y + 17, Y + 25):
        for k in range(16):
            a = 2 * math.pi * k / 16
            x, z = round(cx + 5 * math.cos(a)), round(cz + 5 * math.sin(a))
            if k % 4 == 0:
                v.set(x, fy + 1, z, 'bookshelf')
                v.set(x, fy + 2, z, 'bookshelf')
        v.lamp(cx, fy + 6, cz, kind='soul_lantern')
    v.set(cx, Y + 1, cz, 'enchanting_table')
    v.set(cx + 1, Y + 1, cz, 'brewing_stand')
    v.set(cx - 1, Y + 1, cz, 'lectern[facing=east]')
    v.fill(cx + 6, Y + 1, cz, cx + 6, Y + 2, cz, AIR)
    v.door(cx + 6, Y + 1, cz, 'east', 'dark_oak')
    spot('liora', cx + 2, Y + 1, cz + 2)
    for a in range(0, 360, 60):
        x, z = round(cx + 8 * math.cos(math.radians(a))), round(cz + 8 * math.sin(math.radians(a)))
        v.set(x, Y + 1, z, 'amethyst_block')
        v.set(x, Y + 2, z, 'amethyst_cluster[facing=up]')


def guild(v, Y):
    """Guilde des aventuriers (ouest) : tableau des contrats, maître d'armes."""
    x1, z1, x2, z2 = -44, -16, -22, -4
    st = HOUSE_STYLES[1]
    v.fill(x1, Y, z1, x2, Y, z2, 'stone_bricks')
    v.fill(x1 + 1, Y, z1 + 1, x2 - 1, Y, z2 - 1, 'spruce_planks')
    v.frame_walls(x1, z1, x2, z2, Y + 1, Y + 6, 'smooth_sandstone', 'dark_oak_log', 'stripped_dark_oak_log', step=3)
    v.fill(x1 + 1, Y + 1, z1 + 1, x2 - 1, Y + 6, z2 - 1, AIR)
    v.windows(x1, z1, x2, z2, Y + 2, 2, 'glass_pane', every=3)
    v.gable_roof(x1, z1, x2, z2, Y + 7, 'x', 'dark_oak_stairs', 'dark_oak_slab', 'dark_oak_planks')
    v.fill(x2, Y + 1, -11, x2, Y + 3, -9, AIR)
    v.set(x2 + 1, Y + 4, -12, 'red_wall_banner[facing=east]')
    v.set(x2 + 1, Y + 4, -8, 'red_wall_banner[facing=east]')
    # tableau des contrats (mur nord, intérieur)
    v.fill(-36, Y + 2, z1 + 1, -30, Y + 4, z1 + 1, 'spruce_planks')
    v.fill(-37, Y + 1, z1 + 1, -37, Y + 5, z1 + 1, 'stripped_spruce_log')
    v.fill(-29, Y + 1, z1 + 1, -29, Y + 5, z1 + 1, 'stripped_spruce_log')
    spot('board', -33, Y + 1, z1 + 2)
    # mannequins d'entraînement, râtelier
    for x in (-42, -40):
        v.set(x, Y + 1, z2 - 2, 'hay_block')
        v.set(x, Y + 2, z2 - 2, 'carved_pumpkin[facing=east]')
    v.fill(-26, Y + 1, z1 + 1, -24, Y + 1, z1 + 1, 'barrel[facing=up]')
    v.set(-25, Y + 2, z1 + 1, 'grindstone[face=floor,facing=north]')
    for x in range(-42, -24, 6):
        v.lamp(x, Y + 5, -10)
    spot('orren', -27, Y + 1, -10)


def tavern(v, Y):
    """Taverne du Sanglier Doré (sud-ouest), deux étages, comptoir, tables, cheminée."""
    x1, z1, x2, z2 = -44, 8, -24, 24
    r = random.Random(9)
    v.fill(x1, Y, z1, x2, Y, z2, 'cobblestone')
    v.fill(x1 + 1, Y, z1 + 1, x2 - 1, Y, z2 - 1, 'spruce_planks')
    v.frame_walls(x1, z1, x2, z2, Y + 1, Y + 4, 'cobblestone', 'spruce_log', 'stripped_spruce_log', step=4)
    v.frame_walls(x1, z1, x2, z2, Y + 5, Y + 8, 'white_terracotta', 'spruce_log', 'stripped_spruce_log', step=4)
    v.fill(x1 + 1, Y + 1, z1 + 1, x2 - 1, Y + 8, z2 - 1, AIR)
    v.fill(x1 + 1, Y + 5, z1 + 1, x2 - 1, Y + 5, z2 - 1, 'spruce_planks')
    v.fill(x1 + 2, Y + 5, z1 + 5, x1 + 4, Y + 5, z1 + 7, AIR)   # trou d'étage au-dessus de la volée
    v.stair_run(x1 + 2, Y + 1, z1 + 8, 0, -1, 5, 'spruce_stairs', 'north', support='spruce_planks')
    v.windows(x1, z1, x2, z2, Y + 2, 2, 'glass_pane', every=4)
    v.windows(x1, z1, x2, z2, Y + 6, 2, 'glass_pane', every=4)
    v.gable_roof(x1, z1, x2, z2, Y + 9, 'x', 'spruce_stairs', 'spruce_slab', 'spruce_planks')
    v.fill(x2, Y + 1, 15, x2, Y + 2, 16, AIR)
    v.door(x2, Y + 1, 15, 'east', 'spruce', width=2)
    v.set(x2 + 1, Y + 4, 13, 'yellow_wall_banner[facing=east]')
    # comptoir
    v.fill(x1 + 8, Y + 1, z2 - 4, x1 + 16, Y + 1, z2 - 4, 'spruce_planks')
    v.fill(x1 + 8, Y + 2, z2 - 4, x1 + 16, Y + 2, z2 - 4, 'spruce_slab')
    v.fill(x1 + 8, Y + 1, z2 - 1, x1 + 16, Y + 2, z2 - 1, 'barrel[facing=north]')
    spot('innkeeper', x1 + 12, Y + 1, z2 - 2)
    # tables
    for (tx, tz) in ((x1 + 5, z1 + 4), (x1 + 11, z1 + 4), (x1 + 16, z1 + 4), (x1 + 5, z1 + 9), (x1 + 11, z1 + 9), (x1 + 16, z1 + 9)):
        v.table(tx, Y + 1, tz, 'spruce_pressure_plate', 'spruce_fence')
        v.set(tx + 1, Y + 1, tz, 'spruce_stairs[facing=west]')
        v.set(tx - 1, Y + 1, tz, 'spruce_stairs[facing=east]')
        v.set(tx, Y + 3, tz, 'candle[candles=3,lit=true]') if False else None
    # cheminée
    v.fill(x1 + 1, Y + 1, z1 + 12, x1 + 1, Y + 14, z1 + 14, 'bricks')
    v.set(x1 + 2, Y + 1, z1 + 13, 'campfire[lit=true,facing=east]')
    v.set(x1 + 2, Y + 2, z1 + 12, 'brick_stairs[facing=south,half=top]')
    for x in range(x1 + 4, x2 - 2, 5):
        v.lamp(x, Y + 3, z1 + 7)
    # chambres (étage)
    for k, x in enumerate(range(x1 + 6, x2 - 2, 5)):
        v.bed(x, Y + 6, z2 - 2, 'south', ['red', 'yellow', 'green'][k % 3])


def forge_b(v, Y):
    """Forge (sud-est) : atelier ouvert, cheminée, enclumes, lave."""
    x1, z1, x2, z2 = 22, 8, 40, 22
    v.fill(x1, Y, z1, x2, Y, z2, 'polished_andesite')
    v.fill(x1, Y + 1, z1, x2, Y + 5, z1, 'stone_bricks')
    v.fill(x1, Y + 1, z1, x1, Y + 5, z2, 'stone_bricks')
    for (x, z) in ((x2, z1), (x2, z2), (x1, z2), (31, z2), (x2, 15)):
        v.fill(x, Y + 1, z, x, Y + 5, z, 'stripped_dark_oak_log')
    v.fill(x1, Y + 6, z1, x2, Y + 6, z2, 'dark_oak_slab')
    v.fill(x1 + 1, Y + 1, z1 + 1, x1 + 4, Y + 1, z1 + 4, 'bricks')
    v.fill(x1 + 1, Y + 2, z1 + 1, x1 + 4, Y + 12, z1 + 4, 'bricks', hollow=True)
    v.fill(x1 + 2, Y + 1, z1 + 2, x1 + 3, Y + 1, z1 + 3, 'lava')
    v.fill(x1 + 2, Y + 2, z1 + 4, x1 + 3, Y + 3, z1 + 4, 'iron_bars')
    v.set(x1 + 6, Y + 1, z1 + 2, 'anvil[facing=east]')
    v.set(x1 + 9, Y + 1, z1 + 2, 'chipped_anvil[facing=east]')
    v.set(x1 + 12, Y + 1, z1 + 1, 'blast_furnace[facing=south]')
    v.set(x1 + 13, Y + 1, z1 + 1, 'blast_furnace[facing=south]')
    v.set(x1 + 15, Y + 1, z1 + 1, 'smithing_table')
    v.set(x1 + 16, Y + 1, z1 + 1, 'grindstone[face=floor,facing=south]')
    v.set(x1 + 2, Y + 1, z2 - 2, 'water_cauldron[level=3]')
    v.fill(x1 + 6, Y + 1, z2 - 1, x1 + 12, Y + 1, z2 - 1, 'barrel[facing=up]')
    spot('blacksmith', x1 + 8, Y + 1, z1 + 4)
    for x in (x1 + 6, x1 + 12):
        v.lamp(x, Y + 5, z1 + 8)


def market(v, Y):
    """Marché (est de la place) : étals à auvents colorés."""
    cols = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'cyan', 'lime']
    k = 0
    for x0 in range(17, 44, 7):
        for z0, face in ((-13, 'south'), (-8, 'north')):
            c = cols[k % len(cols)]
            k += 1
            v.fill(x0, Y + 1, z0, x0 + 4, Y + 1, z0, 'spruce_planks' if face == 'south' else 'oak_planks')
            for (x, z) in ((x0, z0), (x0 + 4, z0)):
                v.fill(x, Y + 1, z, x, Y + 3, z, 'spruce_fence')
            v.fill(x0, Y + 4, z0 - (1 if face == 'south' else 0), x0 + 4, Y + 4, z0 + (0 if face == 'south' else 1), f'{c}_wool')
            v.set(x0 + 2, Y + 2, z0, ['melon', 'pumpkin', 'hay_block', 'barrel[facing=up]', 'composter', 'bee_nest[facing=south]'][k % 6])
    spot('merchant', 24, Y + 1, -10)
    spot('armorer', 31, Y + 1, -10)
    spot('trader', 38, Y + 1, -10)


def stables(v, Y):
    x1, z1, x2, z2 = 24, 30, 42, 44
    v.fill(x1, Y, z1, x2, Y, z2, 'coarse_dirt')
    v.fill(x1, Y + 1, z1, x2, Y + 1, z2, 'oak_fence', outline=True)
    v.fill(x1 + 8, Y + 1, z1, x1 + 10, Y + 1, z1, AIR)
    v.fill(x1, Y + 1, z2 - 5, x2, Y + 4, z2, 'oak_planks', hollow=True)
    v.fill(x1 + 1, Y + 1, z2 - 4, x2 - 1, Y + 4, z2 - 1, AIR)
    v.fill(x1, Y + 5, z2 - 6, x2, Y + 5, z2, 'oak_slab')
    for x in range(x1 + 2, x2 - 1, 4):
        v.fill(x, Y + 1, z2 - 5, x + 1, Y + 3, z2 - 5, AIR)
        v.set(x, Y + 1, z2 - 2, 'hay_block')
        v.set(x + 1, Y + 1, z2 - 1, 'water_cauldron[level=3]')
    for x in range(x1 + 3, x2 - 2, 6):
        v.set(x, Y + 1, z1 + 4, 'hay_block')
    spot('stablemaster', x1 + 9, Y + 1, z1 + 2)
    spot('stable_pen', (x1 + x2) // 2, Y + 1, z1 + 6)


def alchemist(v, Y):
    x1, z1, x2, z2 = -44, 30, -30, 42
    house(v, x1, z1, x2 - x1 + 1, z2 - z1 + 1, Y, 'north', dict(frame='stripped_mangrove_log', post='mangrove_log', fill='green_terracotta',
                                                                  base='mossy_stone_bricks', roof='mangrove', roof_b='mangrove_planks', floor='spruce_planks'), floors=2)
    v.set(x1 + 3, Y + 1, z1 + 3, 'brewing_stand')
    v.set(x1 + 4, Y + 1, z1 + 3, 'water_cauldron[level=3]')
    v.set(x1 + 5, Y + 1, z1 + 3, 'brewing_stand')
    spot('alchemist', x1 + 6, Y + 1, z1 - 2)
    for x in range(x1, x2 + 1, 2):
        if x == x1 + 6:                          # place de Fenna : AIR explicite (un ancien pot a pu être construit)
            v.set(x, Y + 1, z1 - 2, AIR)
        else:
            v.set(x, Y + 1, z1 - 2, 'potted_red_mushroom' if x % 4 else 'potted_crimson_fungus')


# ================================================================ VALDOR
def village(cx, cz, y, n_houses, seed, style_ids=(0, 1, 2, 3), name='village', well=True, fields=True):
    v = Vox(seed)
    r = random.Random(seed)
    # place centrale
    for x in range(cx - 6, cx + 7):
        for z in range(cz - 6, cz + 7):
            if math.hypot(x - cx, z - cz) <= 6.5:
                v.set(x, y, z, 'gravel' if r.random() < 0.3 else 'cobblestone')
    if well:
        v.fill(cx - 1, y + 1, cz - 1, cx + 1, y + 1, cz + 1, 'cobblestone', hollow=False)
        v.set(cx, y + 1, cz, 'water')
        for (x, z) in ((cx - 1, cz - 1), (cx + 1, cz - 1), (cx - 1, cz + 1), (cx + 1, cz + 1)):
            v.fill(x, y + 2, z, x, y + 3, z, 'oak_fence')
        v.fill(cx - 1, y + 4, cz - 1, cx + 1, y + 4, cz + 1, 'oak_slab')
        v.set(cx, y + 3, cz, 'iron_chain')
    spots = []
    angs = [i * 2 * math.pi / n_houses + r.uniform(-0.2, 0.2) for i in range(n_houses)]
    for i, a in enumerate(angs):
        d = r.uniform(13, 17)
        w_, dd = r.randint(6, 9), r.randint(6, 8)
        hx, hz = round(cx + d * math.cos(a) - w_ / 2), round(cz + d * math.sin(a) - dd / 2)
        ddx, ddz = cx - (hx + w_ / 2), cz - (hz + dd / 2)
        facing = ('east' if ddx > 0 else 'west') if abs(ddx) > abs(ddz) else ('south' if ddz > 0 else 'north')
        door = house(v, hx, hz, w_, dd, y, facing, HOUSE_STYLES[r.choice(style_ids)], floors=r.choice([1, 2]), r=r)
        spots.append(door)
        # chemin vers la place
        px, pz = door[0], door[2]
        for t in range(20):
            qx, qz = round(px + (cx - px) * t / 20), round(pz + (cz - pz) * t / 20)
            if v.get(qx, y, qz) is None:
                v.set(qx, y, qz, 'dirt_path')
    if fields:
        for (fx, fz) in ((cx + 22, cz - 8), (cx - 28, cz + 6)):
            for x in range(fx, fx + 9):
                for z in range(fz, fz + 9):
                    if (x - fx) % 4 == 0:
                        v.set(x, y, z, 'water')
                    else:
                        v.set(x, y, z, 'farmland[moisture=7]')
                        v.set(x, y + 1, z, r.choice(['wheat[age=7]', 'carrots[age=7]', 'potatoes[age=7]', 'wheat[age=5]']))
            v.fill(fx - 1, y + 1, fz - 1, fx + 9, y + 1, fz + 9, 'oak_fence', outline=True)
            v.set(fx + 4, y + 1, fz - 1, 'oak_fence_gate[facing=north]')
    # lanternes
    for a in range(0, 360, 90):
        x, z = round(cx + 7.5 * math.cos(math.radians(a + 45))), round(cz + 7.5 * math.sin(math.radians(a + 45)))
        v.fill(x, y + 1, z, x, y + 2, z, 'spruce_fence')
        v.set(x, y + 3, z, 'lantern')
    return v, spots


def brumecombe():
    cx, cz = W.P['brumecombe']
    y = 66
    v, doors = village(cx, cz, y, 7, 201)
    spot('tessa', cx + 2, y + 1, cz + 2)
    spot('waystone_w', cx - 3, y + 1, cz - 3)
    v.set(cx - 3, y + 1, cz - 3, 'lodestone')
    v.set(cx - 3, y + 2, cz - 3, 'amethyst_cluster[facing=up]')
    spot('village_w', cx, y + 1, cz)
    # auberge (plus grande) au nord de la place
    house(v, cx - 6, cz - 30, 12, 9, y, 'south', HOUSE_STYLES[0], floors=2)
    spot('farmer', cx + 22, y + 1, cz - 10)
    return v


def windmill():
    cx, cz = W.P['mill']
    y = 66
    v = Vox(202)
    round_tower(v, cx, cz, y + 1, 4, 14, lambda x, yy, z: 'white_terracotta' if yy % 4 else 'stripped_oak_log', floor='oak_planks', floors=(y + 7,))
    cone_roof(v, cx, cz, y + 15, 5, 'spruce_planks', 6, None)
    # ailes (croix devant la tour, face sud)
    for k in range(-9, 10):
        v.set(cx + k, y + 13, cz + 6, 'oak_fence' if abs(k) > 1 else 'stripped_oak_log[axis=z]')
        v.set(cx, y + 13 + k, cz + 6, 'oak_fence' if abs(k) > 1 else 'stripped_oak_log[axis=z]')
        if abs(k) > 2:
            v.set(cx + k, y + 14 if k > 0 else y + 12, cz + 6, 'white_wool')
            v.set(cx + (1 if k < 0 else -1), y + 13 + k, cz + 6, 'white_wool')
    v.set(cx, y + 13, cz + 5, 'stripped_oak_log[axis=z]')
    v.fill(cx, y + 1, cz + 4, cx, y + 2, cz + 4, AIR)
    v.door(cx, y + 1, cz + 4, 'south', 'oak')
    for k in range(3):
        v.set(cx - 2 + k * 2, y + 1, cz - 2, 'hay_block')
    return v


def bandit_fort():
    """Fort des brigands de Brennic : palissade, tours de guet, tentes, grande hutte (arène du boss dans la cour)."""
    x1, z1, x2, z2 = -222, -60, -188, -24
    y = 70
    v = Vox(203)
    r = v.r
    cx, cz = (x1 + x2) // 2, (z1 + z2) // 2
    v.fill(x1, y, z1, x2, y, z2, 'coarse_dirt')
    for x in range(x1, x2 + 1):
        for z in range(z1, z2 + 1):
            if r.random() < 0.3:
                v.set(x, y, z, r.choice(['dirt_path', 'gravel', 'podzol']))
    for x in range(x1, x2 + 1):
        for z in range(z1, z2 + 1):
            if x in (x1, x2) or z in (z1, z2):
                hgt = 6 + r.randint(0, 1)
                v.fill(x, y - 2, z, x, y + hgt, z, 'spruce_log')
                if (x + z) % 2 == 0:
                    v.set(x, y + hgt + 1, z, 'spruce_fence')
    # porte est (vers le village)
    v.fill(x2, y + 1, cz - 2, x2, y + 7, cz + 2, AIR)
    v.fill(x2, y + 6, cz - 3, x2, y + 6, cz + 3, 'stripped_spruce_log[axis=z]')
    for zz in (cz - 3, cz + 3):
        v.fill(x2 + 1, y + 1, zz, x2 + 1, y + 9, zz, 'spruce_log')
        v.set(x2 + 1, y + 10, zz, 'skeleton_skull')
    # chemin de ronde
    for x in range(x1 + 1, x2):
        for z in (z1 + 1, z2 - 1):
            v.set(x, y + 4, z, 'spruce_slab[type=top]')
    for z in range(z1 + 1, z2):
        for x in (x1 + 1, x2 - 1):
            v.set(x, y + 4, z, 'spruce_slab[type=top]')
    # tours de guet
    for (tx, tz) in ((x1 + 2, z1 + 2), (x2 - 2, z1 + 2), (x1 + 2, z2 - 2), (x2 - 2, z2 - 2)):
        for (px_, pz_) in ((tx - 1, tz - 1), (tx + 1, tz - 1), (tx - 1, tz + 1), (tx + 1, tz + 1)):
            v.fill(px_, y + 1, pz_, px_, y + 11, pz_, 'spruce_log')
        v.fill(tx - 2, y + 10, tz - 2, tx + 2, y + 10, tz + 2, 'spruce_planks')
        v.fill(tx - 2, y + 11, tz - 2, tx + 2, y + 11, tz + 2, 'spruce_fence', outline=True)
        v.fill(tx - 2, y + 14, tz - 2, tx + 2, y + 14, tz + 2, 'dark_oak_slab')
        v.fill(tx, y + 1, tz, tx, y + 10, tz, 'ladder[facing=north]')
        v.fill(tx, y + 1, tz + 1, tx, y + 9, tz + 1, 'spruce_log')       # dos de l'échelle
        v.set(tx, y + 12, tz, AIR)                                         # sortie haute dégagée (AIR explicite : l'ancien feu de camp)
        v.set(tx + 1, y + 11, tz + 1, 'campfire[lit=true]')                # remplace le haut du poteau d'angle (tx+1, tz+1)
    # grande hutte de Brennic (ouest)
    hx1, hz1, hx2, hz2 = x1 + 3, cz - 6, x1 + 13, cz + 6
    v.fill(hx1, y + 1, hz1, hx2, y + 5, hz2, 'spruce_planks', hollow=True)
    v.fill(hx1 + 1, y + 1, hz1 + 1, hx2 - 1, y + 5, hz2 - 1, AIR)
    v.gable_roof(hx1, hz1, hx2, hz2, y + 6, 'z', 'spruce_stairs', 'spruce_slab', 'spruce_planks')
    v.fill(hx2, y + 1, cz - 1, hx2, y + 3, cz + 1, AIR)
    v.set(hx1 + 1, y + 1, cz, 'chest[facing=east]')
    v.fill(hx1 + 1, y + 1, hz1 + 1, hx1 + 3, y + 1, hz1 + 1, 'barrel[facing=up]')
    v.set(hx1 + 2, y + 1, cz, 'dark_oak_stairs[facing=east]')
    v.set(hx1 + 2, y + 2, cz - 1, 'red_wall_banner[facing=east]') if False else None
    # tentes
    for (tx, tz, c) in ((cx + 6, z1 + 6, 'red'), (cx + 12, z1 + 6, 'brown'), (cx + 6, z2 - 7, 'green'), (cx + 12, z2 - 7, 'red')):
        for i in range(4):
            v.fill(tx - 2 + i, y + 1 + i, tz - 2, tx - 2 + i, y + 1 + i, tz + 2, f'{c}_wool')
            v.fill(tx + 3 - i, y + 1 + i, tz - 2, tx + 3 - i, y + 1 + i, tz + 2, f'{c}_wool')
        v.set(tx, y + 1, tz, f'{c}_bed[facing=north,part=foot]')
        v.set(tx, y + 1, tz - 1, f'{c}_bed[facing=north,part=head]')
    # feu de camp central, caisses
    v.set(cx, y + 1, cz, 'campfire[lit=true]')
    for (x, z) in ((cx + 3, cz + 3), (cx - 3, cz + 3), (cx + 3, cz - 3)):
        v.set(x, y + 1, z, 'spruce_log[axis=x]')
    for _ in range(14):
        x, z = r.randint(x1 + 3, x2 - 3), r.randint(z1 + 3, z2 - 3)
        if v.get(x, y + 1, z) in (None, AIR):
            v.set(x, y + 1, z, r.choice(['barrel[facing=up]', 'hay_block', 'composter', 'chest[facing=north]']))
    ARENAS['brennic'] = dict(c=(cx + 0.5, y + 1, cz + 0.5), r=18, home=(hx2 + 2.5, y + 1, cz + 0.5))
    spot('fort_gate', x2 + 4, y + 1, cz)
    LORE.append(('w', hx1 + 1, y + 1, cz + 3))
    return v


# ================================================================ DONJONS (générique) : enfilade de salles sous terre
DUN_THEMES = {
    'crypt': dict(wall='stone_bricks', alt='mossy_stone_bricks', crack='cracked_stone_bricks', floor='polished_andesite', pillar='chiseled_stone_bricks',
                  light='soul_lantern', deco=['cobweb', 'skeleton_skull', 'candle[candles=3,lit=true]', 'chiseled_stone_bricks'], door='iron_bars'),
    'nest': dict(wall='mossy_cobblestone', alt='mossy_stone_bricks', crack='cobblestone', floor='moss_block', pillar='oak_log',
                 light='verdant_froglight', deco=['cobweb', 'cobweb', 'cobweb', 'brown_mushroom'], door='cobweb'),
    'ice': dict(wall='packed_ice', alt='blue_ice', crack='snow_block', floor='packed_ice', pillar='blue_ice', light='sea_lantern',
                deco=['snow', 'ice', 'powder_snow', 'blue_ice'], door='iron_bars'),
    'sunken': dict(wall='prismarine_bricks', alt='mossy_stone_bricks', crack='dark_prismarine', floor='prismarine', pillar='prismarine_bricks',
                   light='sea_lantern', deco=['seagrass', 'moss_carpet', 'kelp_plant', 'sea_pickle[pickles=3,waterlogged=false]'], door='iron_bars'),
    'tomb': dict(wall='cut_sandstone', alt='chiseled_sandstone', crack='smooth_sandstone', floor='smooth_sandstone', pillar='chiseled_red_sandstone',
                 light='lantern', deco=['skeleton_skull', 'decorated_pot', 'cobweb', 'dead_bush'], door='iron_bars'),
    'forge': dict(wall='nether_bricks', alt='red_nether_bricks', crack='cracked_nether_bricks', floor='polished_blackstone', pillar='chiseled_nether_bricks',
                  light='shroomlight', deco=['magma_block', 'chain', 'blackstone', 'soul_lantern'], door='iron_bars'),
    'mine': dict(wall='deepslate_bricks', alt='deepslate_tiles', crack='cracked_deepslate_bricks', floor='polished_deepslate', pillar='stripped_spruce_log',
                 light='lantern', deco=['iron_ore', 'deepslate_gold_ore', 'cobweb', 'rail'], door='iron_bars'),
    'souls': dict(wall='polished_blackstone_bricks', alt='cracked_polished_blackstone_bricks', crack='gilded_blackstone', floor='soul_soil', pillar='crying_obsidian',
                  light='soul_lantern', deco=['soul_fire', 'wither_skeleton_skull', 'chain', 'soul_lantern'], door='iron_bars'),
}


def dungeon(key, region, entry, y_floor, theme, rooms_dir, name, alpha):
    """Donjon : escalier depuis l'entrée (x, z, y du sol), puis 4 salles reliées par des couloirs dans la direction rooms_dir.
    Salles 1-3 : vagues de monstres (portes fermées tant qu'il en reste), salle 4 : l'alpha, puis le trésor."""
    t = DUN_THEMES[theme]
    v = Vox(zlib.crc32(key.encode()) & 0xffff)
    r = v.r

    def wl(x, y, z):
        q = r.random()
        return t['alt'] if q < 0.18 else (t['crack'] if q < 0.28 else t['wall'])
    ex, ez, ey = entry
    dx, dz = dir_vec(rooms_dir)
    # escalier en descente (largeur 3) de ey à y_floor
    n = ey - y_floor
    sx, sz = ex, ez
    for i in range(n + 1):
        yy = ey - i
        for k in (-1, 0, 1):
            x, z = (sx + dx * i + (k if dz else 0), sz + dz * i + (k if dx else 0))
            v.fill(x, yy - 1, z, x, yy - 1, z, t['floor'])
            v.fill(x, yy, z, x, yy + 3, z, AIR)
        for k in (-2, 2):
            x, z = (sx + dx * i + (k if dz else 0), sz + dz * i + (k if dx else 0))
            v.fill(x, yy - 1, z, x, yy + 4, z, wl)
        x, z = sx + dx * i, sz + dz * i
        v.set(x - (0 if dz else 0), yy + 4, z, wl(0, 0, 0))
        for k in (-1, 0, 1):
            xx, zz = (x + (k if dz else 0), z + (k if dx else 0))
            v.set(xx, yy + 4, zz, wl(0, 0, 0))
        if i % 4 == 0:
            v.set(x, yy + 3, z, t['light'] + ('[hanging=true]' if t['light'] in ('lantern', 'soul_lantern') else ''))
    # salles
    cx, cz = sx + dx * (n + 4), sz + dz * (n + 4)
    rooms = []
    links = []
    sizes = [(7, 5), (8, 6), (8, 6), (11, 9)]
    pos = 0
    for i, (half, hgt) in enumerate(sizes):
        pos += half + (0 if i == 0 else 4)
        rx, rz = cx + dx * pos, cz + dz * pos
        y = y_floor
        v.fill(rx - half - 1, y - 1, rz - half - 1, rx + half + 1, y + hgt + 1, rz + half + 1, wl)
        v.fill(rx - half, y, rz - half, rx + half, y + hgt, rz + half, AIR)
        v.fill(rx - half, y - 1, rz - half, rx + half, y - 1, rz + half, t['floor'])
        for (px_, pz_) in ((rx - half + 2, rz - half + 2), (rx + half - 2, rz - half + 2), (rx - half + 2, rz + half - 2), (rx + half - 2, rz + half - 2)):
            v.fill(px_, y, pz_, px_, y + hgt, pz_, t['pillar'])
            v.set(px_ + (1 if px_ < rx else -1), y + hgt - 1, pz_, t['light'] + ('[hanging=false]' if t['light'] in ('lantern', 'soul_lantern') else ''))
        for _ in range(half * 2):
            x, z = r.randint(rx - half, rx + half), r.randint(rz - half, rz + half)
            if abs(x - rx) > 1 and abs(z - rz) > 1 and v.get(x, y, z) == AIR:
                b = r.choice(t['deco'])
                if b == 'chain':
                    v.set(x, y + hgt, z, 'iron_chain')
                else:
                    v.set(x, y, z, b)
        rooms.append(dict(c=(rx + 0.5, y, rz + 0.5), half=half, h=hgt))
        pos += half
        if i < len(sizes) - 1:
            links.append((rx, rz, half))
        rooms[-1]['door'] = (rx + dx * (half + 1), y, rz + dz * (half + 1))
    # couloirs vers la salle suivante (porte au bout) : creusés après TOUTES les coques, sinon la coque de la salle suivante les rebouche ;
    # le tronçon half+2 n'appartient à aucune coque et le sous-sol est vide : murs / plafond only=(None,) comme le couloir d'entrée
    for (rx, rz, half) in links:
        for k in range(1, 5):
            xx, zz = rx + dx * (half + k), rz + dz * (half + k)
            for w_ in (-1, 0, 1):
                x, z = (xx + (w_ if dz else 0), zz + (w_ if dx else 0))
                v.fill(x, y_floor, z, x, y_floor + 2, z, AIR)
                v.set(x, y_floor - 1, z, t['floor'])
                v.fill(x, y_floor + 3, z, x, y_floor + 3, z, wl, only=(None,))
            for w_ in (-2, 2):
                x, z = (xx + (w_ if dz else 0), zz + (w_ if dx else 0))
                v.fill(x, y_floor - 1, z, x, y_floor + 3, z, wl, only=(None,))
    # couloir d'entrée : de l'escalier (n) à la coque de la salle 1 (n + 3) ; sous la croûte le sous-sol est vide, d'où les murs only=(None,)
    for k in range(n + 1, n + 4):
        xx, zz = sx + dx * k, sz + dz * k
        for w_ in (-1, 0, 1):
            x, z = (xx + (w_ if dz else 0), zz + (w_ if dx else 0))
            v.fill(x, y_floor, z, x, y_floor + 2, z, AIR)
            v.set(x, y_floor - 1, z, t['floor'])
            v.fill(x, y_floor + 3, z, x, y_floor + 3, z, wl, only=(None,))
        for w_ in (-2, 2):
            x, z = (xx + (w_ if dz else 0), zz + (w_ if dx else 0))
            v.fill(x, y_floor - 1, z, x, y_floor + 3, z, wl, only=(None,))
    # trésor derrière la dernière salle
    last = rooms[-1]
    tx, tz = round(last['c'][0] - 0.5) + dx * (last['half'] - 1), round(last['c'][2] - 0.5) + dz * (last['half'] - 1)
    v.set(tx, y_floor, tz, 'chest[facing=' + opp(rooms_dir) + ']')
    v.fill(tx - (1 if dz else 0), y_floor - 1, tz - (1 if dx else 0), tx + (1 if dz else 0), y_floor - 1, tz + (1 if dx else 0), 'gold_block')
    DUNGEONS[key] = dict(region=region, name=name, alpha=alpha, theme=theme, entry=(ex + 0.5, ey, ez + 0.5), rooms=rooms, dir=rooms_dir,
                         chest=(tx, y_floor, tz), y=y_floor)
    return v


# ================================================================ SYLVANOR
def giant_tree(v, cx, cz, y, h, r, plats, seed):
    rr = random.Random(seed)
    for yy in range(y - 2, y + h):
        rad = r + (2 if yy < y + 3 else 0) * (1 - (yy - y + 2) / 5) if yy < y + 3 else r * (1 - 0.25 * (yy - y) / h)
        for x in range(cx - r - 3, cx + r + 4):
            for z in range(cz - r - 3, cz + r + 4):
                d = math.hypot(x - cx, z - cz)
                if d <= rad + 0.3:
                    v.set(x, yy, z, 'jungle_wood' if d > rad - 1.2 else 'stripped_jungle_wood')
    # racines
    for a in range(0, 360, 45):
        for k in range(r, r + 7):
            x, z = round(cx + k * math.cos(math.radians(a))), round(cz + k * math.sin(math.radians(a)))
            yy = y + max(-1, 3 - (k - r))
            v.fill(x, y - 1, z, x, yy, z, 'jungle_wood')
    # couronne
    top = y + h
    for x in range(cx - 14, cx + 15):
        for z in range(cz - 14, cz + 15):
            for yy in range(top - 4, top + 6):
                d = math.hypot(x - cx, z - cz) + abs(yy - top) * 1.6
                if d < 13 - rr.random() * 2:
                    if v.get(x, yy, z) is None:
                        v.set(x, yy, z, 'azalea_leaves[persistent=true]' if rr.random() < 0.15 else 'jungle_leaves[persistent=true]')
    # plateformes circulaires + rambardes
    for py in plats:
        pr = r + 5
        for x in range(cx - pr, cx + pr + 1):
            for z in range(cz - pr, cz + pr + 1):
                d = math.hypot(x - cx, z - cz)
                if r + 0.5 < d <= pr:
                    v.set(x, py, z, 'birch_planks' if d < pr - 0.5 else 'stripped_birch_log[axis=y]')
                    if d > pr - 1:
                        v.set(x, py + 1, z, 'birch_fence')
        for a in range(0, 360, 60):
            x, z = round(cx + (r + 1) * math.cos(math.radians(a))), round(cz + (r + 1) * math.sin(math.radians(a)))
            v.set(x, py + 1, z, 'lantern')
    # escalier en colimaçon autour du tronc
    for i, yy in enumerate(range(y + 1, max(plats) + 1)):
        a = 2 * math.pi * i / 24
        for rr_ in (r + 1, r + 2):
            x, z = round(cx + rr_ * math.cos(a)), round(cz + rr_ * math.sin(a))
            v.set(x, yy, z, 'birch_slab[type=top]' if v.get(x, yy, z) in (None, AIR) else v.get(x, yy, z))
            v.fill(x, yy + 1, z, x, yy + 3, z, AIR, only=(None, AIR, 'jungle_leaves[persistent=true]', 'azalea_leaves[persistent=true]'))


def rope_bridge(v, a, b, y):
    (x1, z1), (x2, z2) = a, b
    n = max(1, round(max(abs(x2 - x1), abs(z2 - z1))))
    for i in range(n + 1):
        t = i / n
        x, z = round(x1 + (x2 - x1) * t), round(z1 + (z2 - z1) * t)
        sag = round(2 * math.sin(math.pi * t))
        yy = y - sag
        v.set(x, yy, z, 'bamboo_mosaic' if i % 2 else 'birch_planks')
        for k in (-1, 1):
            if abs(x2 - x1) > abs(z2 - z1):
                v.set(x, yy, z + k, 'birch_slab')
                v.set(x, yy + 1, z + k, 'birch_fence')
            else:
                v.set(x + k, yy, z, 'birch_slab')
                v.set(x + k, yy + 1, z, 'birch_fence')


def aelindor():
    cx, cz = W.P['aelindor']
    y = 68
    v = Vox(301)
    trees = [(cx, cz, 5, 44, (y + 10, y + 20, y + 32)), (cx - 15, cz + 12, 3, 34, (y + 10, y + 20)), (cx + 15, cz + 10, 3, 34, (y + 10, y + 20)),
             (cx + 2, cz - 16, 3, 32, (y + 10, y + 20))]
    for i, (tx, tz, rr, h, plats) in enumerate(trees):
        giant_tree(v, tx, tz, y + 1, h, rr, plats, 300 + i)
    for (tx, tz, rr, h, plats) in trees[1:]:
        rope_bridge(v, (cx + (tx - cx) * 0.35, cz + (tz - cz) * 0.35), (tx - (tx - cx) * 0.3, tz - (tz - cz) * 0.3), y + 10)
        rope_bridge(v, (cx + (tx - cx) * 0.35, cz + (tz - cz) * 0.35), (tx - (tx - cx) * 0.3, tz - (tz - cz) * 0.3), y + 20)
    # salle de la reine (plateforme haute de l'arbre central) : trône de bouleau, tapis
    py = y + 32
    v.fill(cx - 2, py + 1, cz - 9, cx + 2, py + 1, cz - 8, 'moss_carpet')
    v.set(cx, py + 1, cz - 9, 'birch_stairs[facing=south]')
    spot('elyndra', cx, py + 1, cz - 7)
    # la couronne d'un arbre voisin déborde sur la salle : on dégage le feuillage autour de la reine
    v.fill(cx - 10, py + 1, cz - 10, cx + 10, py + 3, cz + 10, AIR, only=('jungle_leaves[persistent=true]', 'azalea_leaves[persistent=true]'))
    spot('waystone_nw', cx + 4, y + 1, cz + 9)
    v.set(cx + 4, y + 1, cz + 9, 'lodestone')
    v.set(cx + 4, y + 2, cz + 9, 'amethyst_cluster[facing=up]')
    spot('elf_ground', cx - 8, y + 1, cz + 8)
    # maisons elfiques au sol (blanches, toits de feuilles)
    for (hx, hz) in ((cx - 18, cz - 8), (cx + 18, cz - 6), (cx - 6, cz + 18)):
        round_tower(v, hx, hz, y + 1, 3, 5, 'calcite', floor='birch_planks', windows='light_blue_stained_glass_pane')
        cone_roof(v, hx, hz, y + 6, 4, 'flowering_azalea_leaves[persistent=true]', 4, 'end_rod')
        v.fill(hx + 3, y + 1, hz, hx + 3, y + 2, hz, AIR)
    # fontaines de lumière
    for (fx, fz) in ((cx + 8, cz + 4), (cx - 8, cz - 2)):
        v.set(fx, y + 1, fz, 'chiseled_quartz_block')
        v.set(fx, y + 2, fz, 'pearlescent_froglight')
    LORE.append(('nw', cx + 6, py + 1, cz + 2))
    return v


def spider_lair():
    """Antre de la reine-araignée Ysh'tar : cratère tapissé de toiles, œufs, os."""
    x0, z0 = W.P['spider_lair']
    y = 72
    v = Vox(302)
    r = v.r
    for x in range(x0 - 18, x0 + 19):
        for z in range(z0 - 14, z0 + 15):
            d = math.hypot((x - x0) / 1.25, z - z0)
            if d <= 11:
                v.set(x, y - 1, z, 'moss_block' if r.random() < 0.6 else 'coarse_dirt')
                v.fill(x, y, z, x, y + 12, z, AIR)
                if r.random() < 0.06:
                    v.set(x, y, z, 'cobweb')
            elif d <= 14:
                hh = round(6 + (d - 11) * 2 + r.random() * 2)
                v.fill(x, y - 1, z, x, y + hh, z, 'mossy_cobblestone' if r.random() < 0.5 else 'stone')
    # toiles en voûte
    for _ in range(140):
        x, z = r.randint(x0 - 13, x0 + 13), r.randint(z0 - 10, z0 + 10)
        if math.hypot((x - x0) / 1.25, z - z0) < 11:
            v.set(x, y + r.randint(7, 12), z, 'cobweb')
    # cocons
    for _ in range(10):
        x, z = r.randint(x0 - 12, x0 + 12), r.randint(z0 - 9, z0 + 9)
        if math.hypot((x - x0) / 1.25, z - z0) < 10:
            v.fill(x, y, z, x, y + 1, z, 'white_wool')
            v.set(x, y + 2, z, 'cobweb')
    # entrée (côté est)
    v.fill(x0 + 11, y, z0 - 2, x0 + 18, y + 5, z0 + 2, AIR)
    v.fill(x0 + 11, y - 1, z0 - 2, x0 + 18, y - 1, z0 + 2, 'coarse_dirt')
    ARENAS['ystar'] = dict(c=(x0 + 0.5, y, z0 + 0.5), r=13)
    return v


def shrine():
    x0, z0 = W.P['shrine_nw']
    y = 69
    v = Vox(303)
    for a in range(0, 360, 30):
        x, z = round(x0 + 7 * math.cos(math.radians(a))), round(z0 + 7 * math.sin(math.radians(a)))
        hgt = v.r.randint(2, 6)
        v.fill(x, y + 1, z, x, y + hgt, z, 'mossy_stone_bricks' if v.r.random() < 0.5 else 'quartz_pillar')
    for x in range(x0 - 4, x0 + 5):
        for z in range(z0 - 4, z0 + 5):
            if math.hypot(x - x0, z - z0) <= 4.5:
                v.set(x, y, z, 'mossy_stone_bricks' if (x + z) % 3 else 'chiseled_stone_bricks')
    v.set(x0, y + 1, z0, 'lectern[facing=south]')
    LORE.append(('nw', x0, y + 1, z0 + 1))
    return v


# ================================================================ GIVRECROC
def longhouse(v, x1, z1, L, wdt, y, axis, r):
    """Longue maison nordique (rondins, toit très pentu)."""
    if axis == 'x':
        x2, z2 = x1 + L - 1, z1 + wdt - 1
    else:
        x2, z2 = x1 + wdt - 1, z1 + L - 1
    v.fill(x1, y, z1, x2, y, z2, 'spruce_planks')
    v.walls(x1, z1, x2, z2, y + 1, y + 3, 'stripped_spruce_log[axis=y]')
    v.fill(x1 + 1, y + 1, z1 + 1, x2 - 1, y + 3, z2 - 1, AIR)
    v.gable_roof(x1, z1, x2, z2, y + 4, axis, 'dark_oak_stairs', 'dark_oak_slab', 'spruce_planks', overhang=1)
    if axis == 'x':
        v.fill(x1, y + 1, (z1 + z2) // 2, x1, y + 2, (z1 + z2) // 2, AIR)
        v.set(x1 - 1, y + 4, (z1 + z2) // 2 - 1, 'skeleton_skull') if False else None
        v.set((x1 + x2) // 2, y + 1, (z1 + z2) // 2, 'campfire[lit=true]')
    else:
        v.fill((x1 + x2) // 2, y + 1, z1, (x1 + x2) // 2, y + 2, z1, AIR)
        v.set((x1 + x2) // 2, y + 1, (z1 + z2) // 2, 'campfire[lit=true]')
    for k in range(2):
        v.bed(x1 + 1 + k * 2, y + 1, z2 - 2, 'north', 'white')
    v.set(x2 - 1, y + 1, z1 + 1, 'barrel[facing=up]')


def hrafnheim():
    cx, cz = W.P['hrafnheim']
    y = 74
    v = Vox(401)
    r = v.r
    for x in range(cx - 22, cx + 23):
        for z in range(cz - 18, cz + 19):
            if r.random() < 0.15:
                v.set(x, y, z, 'snow_block')
    # palissade
    for x in range(cx - 21, cx + 22):
        for z in range(cz - 17, cz + 18):
            if x in (cx - 21, cx + 21) or z in (cz - 17, cz + 17):
                if abs(x - cx) <= 2 or abs(z - cz) <= 2:
                    continue
                v.fill(x, y - 1, z, x, y + 5 + (1 if (x + z) % 2 else 0), z, 'spruce_log')
    # grande halle du jarl (nord)
    longhouse(v, cx - 8, cz - 15, 17, 9, y, 'x', r)
    for x in (cx - 6, cx + 6):
        v.set(x, y + 4, cz - 10, 'white_wall_banner[facing=south]') if False else None
    spot('bjorn', cx, y + 1, cz - 13)            # derrière le feu de camp de la halle (cz - 11)
    for (hx, hz, ax) in ((cx - 18, cz - 4, 'z'), (cx + 12, cz - 4, 'z'), (cx - 18, cz + 6, 'z'), (cx + 12, cz + 6, 'z')):
        longhouse(v, hx, hz, 9, 6, y, ax, r)
    # braseros
    for (bx, bz) in ((cx - 4, cz + 2), (cx + 4, cz + 2), (cx, cz + 10)):
        v.set(bx, y + 1, bz, 'cobblestone_wall')
        v.set(bx, y + 2, bz, 'campfire[lit=true]')
    spot('waystone_n', cx + 3, y + 1, cz + 6)
    v.set(cx + 3, y + 1, cz + 6, 'lodestone')
    v.set(cx + 3, y + 2, cz + 6, 'amethyst_cluster[facing=up]')
    spot('furrier', cx - 6, y + 1, cz + 8)
    LORE.append(('n', cx - 15, y + 1, cz - 2))
    return v


def giant_hold():
    """Forteresse de glace du géant Hrimgar (sur un plateau) : enceinte, colonnes, trône, arène."""
    x0, z0 = W.P['giant_hold']
    y = 104
    v = Vox(402)
    r = v.r
    ice = lambda x, yy, z: 'packed_ice' if r.random() < 0.7 else ('blue_ice' if r.random() < 0.6 else 'snow_block')
    R = 16
    for x in range(x0 - R - 2, x0 + R + 3):
        for z in range(z0 - R - 2, z0 + R + 3):
            d = math.hypot(x - x0, z - z0)
            if d <= R:
                v.set(x, y, z, 'packed_ice' if (x + z) % 2 else 'snow_block')
                v.fill(x, y + 1, z, x, y + 16, z, AIR)
            elif d <= R + 1.5:
                hh = 10 + (3 if (round(math.degrees(math.atan2(z - z0, x - x0))) // 15) % 2 else 0)
                v.fill(x, y - 3, z, x, y + hh, z, ice)
    for a in range(0, 360, 30):
        x, z = round(x0 + (R - 3) * math.cos(math.radians(a))), round(z0 + (R - 3) * math.sin(math.radians(a)))
        v.fill(x, y + 1, z, x, y + 9 + r.randint(0, 4), z, 'blue_ice')
    # trône (nord)
    v.fill(x0 - 3, y + 1, z0 - R + 2, x0 + 3, y + 2, z0 - R + 3, 'packed_ice')
    v.fill(x0 - 1, y + 3, z0 - R + 2, x0 + 1, y + 8, z0 - R + 2, 'blue_ice')
    # entrée (sud), escalier de neige
    v.fill(x0 - 2, y + 1, z0 + R - 1, x0 + 2, y + 6, z0 + R + 2, AIR)
    ARENAS['hrimgar'] = dict(c=(x0 + 0.5, y + 1, z0 + 0.5), r=R - 1)
    LORE.append(('n', x0 + 2, y + 1, z0 - R + 4))
    return v


# ================================================================ FANGEBRUME
def stilt_village():
    cx, cz = W.P['stilts']
    y = 63
    v = Vox(501)
    r = v.r
    deck = y + 4
    huts = []
    for i in range(8):
        a = i * 2 * math.pi / 8 + 0.3
        hx, hz = round(cx + 14 * math.cos(a)), round(cz + 12 * math.sin(a))
        huts.append((hx, hz))
        v.fill(hx - 3, y - 3, hz - 3, hx - 3, deck, hz - 3, 'mangrove_log')
        v.fill(hx + 3, y - 3, hz - 3, hx + 3, deck, hz - 3, 'mangrove_log')
        v.fill(hx - 3, y - 3, hz + 3, hx - 3, deck, hz + 3, 'mangrove_log')
        v.fill(hx + 3, y - 3, hz + 3, hx + 3, deck, hz + 3, 'mangrove_log')
        v.fill(hx - 3, deck, hz - 3, hx + 3, deck, hz + 3, 'mangrove_planks')
        v.fill(hx - 2, deck + 1, hz - 2, hx + 2, deck + 3, hz + 2, 'mud_bricks', hollow=True)
        v.fill(hx - 1, deck + 1, hz - 1, hx + 1, deck + 3, hz + 1, AIR)
        v.gable_roof(hx - 2, hz - 2, hx + 2, hz + 2, deck + 4, 'x', 'mangrove_stairs', 'mangrove_slab', 'mangrove_planks')
        ddx, ddz = (cx - hx), (cz - hz)
        if abs(ddx) > abs(ddz):
            ex = hx + (2 if ddx > 0 else -2)
            v.fill(ex, deck + 1, hz, ex, deck + 2, hz, AIR)
        else:
            ez = hz + (2 if ddz > 0 else -2)
            v.fill(hx, deck + 1, ez, hx, deck + 2, ez, AIR)
        v.set(hx, deck + 3, hz, 'lantern[hanging=true]')
    # passerelles vers la plateforme centrale
    v.fill(cx - 5, deck, cz - 5, cx + 5, deck, cz + 5, 'mangrove_planks')
    v.fill(cx - 5, deck + 1, cz - 5, cx + 5, deck + 1, cz + 5, 'mangrove_fence', outline=True)
    for (x, z) in ((cx - 5, cz - 5), (cx + 5, cz - 5), (cx - 5, cz + 5), (cx + 5, cz + 5)):
        v.fill(x, y - 3, z, x, deck - 1, z, 'mangrove_log')
    for (hx, hz) in huts:
        n = max(abs(hx - cx), abs(hz - cz))
        for i in range(n):
            x, z = round(cx + (hx - cx) * i / n), round(cz + (hz - cz) * i / n)
            if v.get(x, deck, z) is None:
                v.set(x, deck, z, 'mangrove_slab[type=top]')
    for (x, z) in ((cx, cz - 5), (cx, cz + 5), (cx - 5, cz), (cx + 5, cz)):
        v.set(x, deck + 1, z, AIR)
    # échelle d'accès (côté ouest)
    v.fill(cx - 6, y, cz, cx - 6, deck, cz, 'ladder[facing=west]')
    v.fill(cx - 7, y - 1, cz - 1, cx - 7, y, cz + 1, 'mangrove_planks')
    v.set(cx, deck + 1, cz, 'cauldron')
    spot('maelle', cx + 2, deck + 1, cz + 2)
    spot('waystone_ne', cx - 2, deck + 1, cz - 2)
    v.set(cx - 2, deck + 1, cz - 2, 'lodestone')
    v.set(cx - 2, deck + 2, cz - 2, 'amethyst_cluster[facing=up]')
    spot('herbalist', cx - 3, deck + 1, cz + 3)
    LORE.append(('ne', huts[3][0], deck + 1, huts[3][1]))
    brace_ladders(v, 'mangrove_log')
    return v


def witch_isle():
    x0, z0 = W.P['witch_isle']
    y = 64
    v = Vox(502)
    r = v.r
    # tour tordue
    for i, yy in enumerate(range(y + 1, y + 26)):
        ox = round(1.5 * math.sin(i / 5))
        oz = round(1.5 * math.cos(i / 7))
        rr = 4 if i < 18 else 3
        for x in range(x0 - rr - 2, x0 + rr + 3):
            for z in range(z0 - rr - 2, z0 + rr + 3):
                d = math.hypot(x - x0 - ox, z - z0 - oz)
                if d <= rr + 0.4:
                    v.set(x, yy, z, ('dark_oak_planks' if r.random() < 0.6 else 'mangrove_planks') if d > rr - 0.7 else AIR)
    cone_roof(v, x0 + round(1.5 * math.sin(25 / 5)), z0 + round(1.5 * math.cos(25 / 7)), y + 26, 5, 'purple_terracotta', 9, 'end_rod')
    v.fill(x0 - 1, y + 1, z0 + 3, x0 + 1, y + 3, z0 + 5, AIR)
    for (x, z) in ((x0 - 2, z0 - 1), (x0 + 2, z0 - 1)):
        v.set(x, y + 1, z, 'cauldron')
    # plancher et arène autour de la tour (sur l'île)
    for x in range(x0 - 10, x0 + 11):
        for z in range(z0 - 10, z0 + 11):
            d = math.hypot(x - x0, z - z0)
            if 5 < d <= 10:
                v.set(x, y, z, 'mud' if r.random() < 0.5 else 'moss_block')
    ARENAS['morvaine'] = dict(c=(x0 + 0.5, y + 1, z0 + 7.5), r=12)
    # totems (3) sur la rive
    tot = []
    for a in (200, 300, 60):
        x, z = round(x0 + 24 * math.cos(math.radians(a))), round(z0 + 24 * math.sin(math.radians(a)))
        gy = W.ground(x, z) if (x, z) in W.H else y
        v.fill(x, gy, z, x, gy + 3, z, 'stripped_dark_oak_log')
        v.set(x, gy + 4, z, 'carved_pumpkin[facing=south]')
        v.set(x, gy + 5, z, 'soul_lantern')
        tot.append((x + 0.5, gy, z + 0.5))
    SPOTS['totems'] = tot
    # ponton (passerelle depuis la rive sud)
    for z in range(z0 + 10, z0 + 30):
        v.set(x0, y, z, 'mangrove_planks')
        v.set(x0 - 1, y, z, 'mangrove_slab[type=top]')
        v.set(x0 + 1, y, z, 'mangrove_slab[type=top]')
        if z % 4 == 0:
            v.fill(x0 + 2, y - 4, z, x0 + 2, y + 1, z, 'mangrove_log')
            v.set(x0 + 2, y + 2, z, 'soul_lantern')
    LORE.append(('ne', x0 - 1, y + 1, z0 + 1))
    return v


# ================================================================ AZHAR
def oasis_town():
    cx, cz = W.P['oasis']
    y = 64
    v = Vox(601)
    r = v.r
    for (hx, hz, w_, d_, h_) in ((cx - 16, cz - 14, 8, 7, 5), (cx - 6, cz - 14, 7, 7, 4), (cx - 16, cz + 6, 9, 8, 6), (cx - 5, cz + 8, 7, 7, 4),
                                 (cx + 2, cz - 15, 8, 6, 5), (cx - 17, cz - 4, 6, 7, 4)):
        v.fill(hx, y, hz, hx + w_ - 1, y, hz + d_ - 1, 'smooth_sandstone')
        v.fill(hx, y + 1, hz, hx + w_ - 1, y + h_, hz + d_ - 1, 'sandstone', hollow=True)
        v.fill(hx + 1, y + 1, hz + 1, hx + w_ - 2, y + h_, hz + d_ - 2, AIR)
        v.fill(hx, y + h_ + 1, hz, hx + w_ - 1, y + h_ + 1, hz + d_ - 1, 'smooth_sandstone_slab')
        v.fill(hx, y + h_ + 2, hz, hx + w_ - 1, y + h_ + 2, hz + d_ - 1, 'sandstone_wall', outline=True)
        v.fill(hx + w_ // 2, y + 1, hz + d_ - 1, hx + w_ // 2, y + 2, hz + d_ - 1, AIR)
        for x in range(hx + 2, hx + w_ - 1, 3):
            v.set(x, y + 3, hz, 'orange_stained_glass_pane')
        v.set(hx + 1, y + 1, hz + 1, 'decorated_pot')
        v.set(hx + w_ - 2, y + 1, hz + 1, 'barrel[facing=up]')
        v.set(hx + w_ // 2, y + h_, hz + d_ // 2, 'lantern[hanging=true]')
    # dôme du marchand (centre)
    for x in range(cx - 5, cx + 6):
        for z in range(cz - 5, cz + 6):
            for yy in range(y + 1, y + 12):
                d = math.hypot(x - cx, z - cz, (yy - y - 6) * 1.1) if False else math.sqrt((x - cx) ** 2 + (z - cz) ** 2 + max(0, yy - y - 6) ** 2 * 1.2)
                if yy <= y + 6:
                    if math.hypot(x - cx, z - cz) <= 5 and math.hypot(x - cx, z - cz) > 4:
                        v.set(x, yy, z, 'cut_sandstone')
                elif 4 < d <= 5.2:
                    v.set(x, yy, z, 'cyan_terracotta' if (yy - y) % 2 else 'white_terracotta')
    v.fill(cx - 1, y + 1, cz + 4, cx + 1, y + 3, cz + 5, AIR)
    v.set(cx, y + 1, cz, 'cartography_table')
    spot('kassim', cx + 2, y + 1, cz + 1)
    # tentes du bazar
    for i, (tx, tz) in enumerate(((cx + 5, cz + 10), (cx + 10, cz + 12), (cx - 2, cz + 16))):
        c = ['red', 'orange', 'blue'][i]
        v.fill(tx - 2, y + 3, tz - 2, tx + 2, y + 3, tz + 2, f'{c}_wool')
        for (x, z) in ((tx - 2, tz - 2), (tx + 2, tz - 2), (tx - 2, tz + 2), (tx + 2, tz + 2)):
            v.fill(x, y + 1, z, x, y + 2, z, 'birch_fence')
        v.set(tx, y + 1, tz, r.choice(['barrel[facing=up]', 'decorated_pot', 'hay_block']))
    spot('waystone_e', cx + 6, y + 1, cz - 4)
    v.set(cx + 6, y + 1, cz - 4, 'lodestone')
    v.set(cx + 6, y + 2, cz - 4, 'amethyst_cluster[facing=up]')
    spot('sandmerchant', cx + 5, y + 1, cz + 9)
    return v


def pyramid():
    """Pyramide de Sethkar : 4 côtés en gradins, entrée nord, couloir, salle des scarabées (3 socles), chambre funéraire (arène)."""
    x0, z0 = W.P['pyramid']
    y = 64
    v = Vox(602)
    r = v.r
    B = 24
    for i in range(B):
        yy = y + 1 + i
        hb = B - i
        for x in range(x0 - hb, x0 + hb + 1):
            for z in range(z0 - hb, z0 + hb + 1):
                if max(abs(x - x0), abs(z - z0)) >= hb - 1:
                    v.set(x, yy, z, 'smooth_sandstone' if r.random() < 0.7 else ('cut_sandstone' if r.random() < 0.7 else 'chiseled_sandstone'))
                else:
                    v.set(x, yy, z, 'sandstone')
    v.set(x0, y + B + 1, z0, 'gold_block')
    # salle intérieure (chambre funéraire) : 21 × 21 × 9
    v.fill(x0 - 10, y + 1, z0 - 10, x0 + 10, y + 9, z0 + 10, AIR)
    v.fill(x0 - 10, y, z0 - 10, x0 + 10, y, z0 + 10, 'smooth_sandstone')
    for x in range(x0 - 10, x0 + 11):
        for z in range(z0 - 10, z0 + 11):
            if (x + z) % 6 == 0:
                v.set(x, y, z, 'orange_terracotta' if (x - z) % 4 else 'blue_terracotta')
    for (px_, pz_) in ((x0 - 6, z0 - 6), (x0 + 6, z0 - 6), (x0 - 6, z0 + 6), (x0 + 6, z0 + 6)):
        v.fill(px_, y + 1, pz_, px_, y + 9, pz_, 'chiseled_red_sandstone')
        v.set(px_ + (1 if px_ < x0 else -1), y + 6, pz_, 'lantern[hanging=false]')
    v.fill(x0 - 2, y + 1, z0 + 6, x0 + 2, y + 1, z0 + 8, 'gold_block')
    v.fill(x0 - 1, y + 2, z0 + 7, x0 + 1, y + 2, z0 + 7, 'chiseled_sandstone')
    ARENAS['sethkar'] = dict(c=(x0 + 0.5, y + 1, z0 + 0.5), r=10)
    # couloir d'entrée (nord) et salle des scarabées
    v.fill(x0 - 1, y + 1, z0 - B, x0 + 1, y + 4, z0 - 11, AIR)
    v.fill(x0 - 1, y, z0 - B, x0 + 1, y, z0 - 11, 'cut_sandstone')
    v.fill(x0 - 6, y + 1, z0 - 18, x0 + 6, y + 6, z0 - 13, AIR)
    v.fill(x0 - 6, y, z0 - 18, x0 + 6, y, z0 - 13, 'smooth_sandstone')
    sock = []
    for i, x in enumerate((x0 - 4, x0, x0 + 4)):
        v.set(x, y + 1, z0 - 17, 'chiseled_sandstone')
        v.set(x, y + 2, z0 - 17, 'decorated_pot')
        sock.append((x + 0.5, y + 1, z0 - 15.5))
    SPOTS['scarab_sockets'] = sock
    SPOTS['pyr_door'] = (x0, y + 1, z0 - 11)        # porte scellée (sable) vers la chambre
    v.fill(x0 - 1, y + 1, z0 - 11, x0 + 1, y + 3, z0 - 11, 'chiseled_sandstone')
    for z in range(z0 - B + 2, z0 - 11, 3):
        v.set(x0 - 1, y + 3, z, 'lantern[hanging=false]') if False else v.set(x0 - 2, y + 3, z, 'lantern') if False else None
    spot('pyr_entry', x0, y + 1, z0 - B - 2)
    LORE.append(('e', x0 + 5, y + 1, z0 - 14))
    return v


def obelisks():
    x0, z0 = W.P['obelisks']
    y = W.ground(x0, z0) - 1
    v = Vox(603)
    for (dx, dz) in ((-6, 0), (6, 0), (0, -6), (0, 6)):
        x, z = x0 + dx, z0 + dz
        gy = W.ground(x, z) - 1
        v.fill(x - 1, gy - 2, z - 1, x + 1, gy + 1, z + 1, 'cut_sandstone')
        v.fill(x, gy + 2, z, x, gy + 12, z, 'chiseled_sandstone')
        v.set(x, gy + 13, z, 'gold_block')
    LORE.append(('e', x0, W.ground(x0, z0), z0))
    return v


# ================================================================ PYRECENDRE
def bastion():
    cx, cz = W.P['bastion']
    y = 66
    v = Vox(701)
    r = v.r
    wl = lambda x, yy, z: 'polished_blackstone_bricks' if r.random() < 0.75 else 'cracked_polished_blackstone_bricks'
    x1, z1, x2, z2 = cx - 14, cz - 14, cx + 14, cz + 14
    v.fill(x1, y, z1, x2, y, z2, 'polished_blackstone')
    v.walls(x1, z1, x2, z2, y + 1, y + 7, wl)
    crenels(v, x1, z1, x2, z1, y + 8, 'polished_blackstone_bricks')
    crenels(v, x1, z2, x2, z2, y + 8, 'polished_blackstone_bricks')
    crenels(v, x1, z1, x1, z2, y + 8, 'polished_blackstone_bricks')
    crenels(v, x2, z1, x2, z2, y + 8, 'polished_blackstone_bricks')
    for (gx, gz, ax) in ((cx, z1, 'x'), (x1, cz, 'z'), (x2, cz, 'z'), (cx, z2, 'x')):
        if ax == 'x':
            v.fill(gx - 2, y + 1, gz, gx + 2, y + 5, gz, AIR)
        else:
            v.fill(gx, y + 1, gz - 2, gx, y + 5, gz + 2, AIR)
    for (tx, tz) in ((x1, z1), (x2, z1), (x1, z2), (x2, z2)):
        round_tower(v, tx, tz, y + 1, 3, 12, wl, floor='polished_blackstone', crenel='polished_blackstone_bricks')
        v.set(tx, y + 12, tz, 'campfire[lit=true]')
    # forge naine, salle commune
    v.fill(cx - 8, y + 1, cz - 10, cx + 8, y + 5, cz - 4, 'stone_bricks', hollow=True)
    v.fill(cx - 7, y + 1, cz - 9, cx + 7, y + 5, cz - 5, AIR)
    v.fill(cx - 8, y + 6, cz - 10, cx + 8, y + 6, cz - 4, 'polished_blackstone_slab')
    v.fill(cx - 1, y + 1, cz - 4, cx + 1, y + 3, cz - 4, AIR)
    v.set(cx - 5, y + 1, cz - 8, 'anvil[facing=east]')
    v.set(cx + 5, y + 1, cz - 8, 'blast_furnace[facing=south]')
    v.fill(cx - 2, y + 1, cz - 9, cx + 2, y + 1, cz - 9, 'lava')
    v.fill(cx - 2, y + 2, cz - 9, cx + 2, y + 2, cz - 9, 'iron_bars')
    spot('durgan', cx, y + 1, cz - 6)
    spot('waystone_se', cx + 4, y + 1, cz + 4)
    v.set(cx + 4, y + 1, cz + 4, 'lodestone')
    v.set(cx + 4, y + 2, cz + 4, 'amethyst_cluster[facing=up]')
    for (x, z) in ((cx - 6, cz + 6), (cx + 8, cz + 8), (cx - 9, cz - 1)):
        v.set(x, y + 1, z, 'magma_block')
        v.set(x, y + 2, z, 'campfire[lit=true]')
    LORE.append(('se', cx - 6, y + 1, cz - 8))
    return v


def caldera():
    """Nid d'Ignarok dans la caldeira : ossements, œufs de dragon, colonnes d'obsidienne, mares de lave."""
    x0, z0 = W.VX, W.VZ
    y = W.CALD_Y
    v = Vox(702)
    r = v.r
    for x in range(x0 - 16, x0 + 17):
        for z in range(z0 - 16, z0 + 17):
            d = math.hypot(x - x0, z - z0)
            if d <= 15.5:
                v.set(x, y, z, 'blackstone' if r.random() < 0.6 else ('basalt' if r.random() < 0.6 else 'magma_block'))
                v.fill(x, y + 1, z, x, y + 22, z, AIR)
                if 12.5 < d and r.random() < 0.25:
                    v.set(x, y, z, 'lava')
    for a in range(15, 360, 45):
        x, z = round(x0 + 12 * math.cos(math.radians(a))), round(z0 + 12 * math.sin(math.radians(a)))
        v.fill(x, y + 1, z, x, y + 6 + r.randint(0, 6), z, 'obsidian' if r.random() < 0.7 else 'crying_obsidian')
    # cage thoracique géante
    for k in range(-6, 7, 3):
        for i in range(10):
            a = math.pi * i / 9
            x, yy = x0 + k, y + round(7 * math.sin(a))
            z = z0 - 4 + round(5 * math.cos(a))
            v.set(x, yy, z, 'bone_block')
    v.fill(x0 - 7, y + 1, z0 - 4, x0 + 7, y + 1, z0 - 4, 'bone_block[axis=x]')
    for (x, z) in ((x0 + 6, z0 + 6), (x0 + 7, z0 + 5), (x0 + 5, z0 + 7)):
        v.set(x, y + 1, z, 'dragon_egg') if False else v.set(x, y + 1, z, 'sniffer_egg')
    ARENAS['ignarok'] = dict(c=(x0 + 0.5, y + 1, z0 + 0.5), r=14)
    LORE.append(('se', x0 - 10, y + 1, z0 + 8))
    return v


# ================================================================ KHAZGARDE
def dwarf_camp():
    cx, cz = W.P['dwarf_camp']
    y = 66
    v = Vox(801)
    r = v.r
    for i, (tx, tz) in enumerate(((cx - 12, cz - 6), (cx + 12, cz - 6), (cx - 12, cz + 6), (cx + 12, cz + 6), (cx, cz - 10))):
        c = ['gray', 'brown', 'light_gray', 'brown', 'blue'][i]
        for k in range(4):
            v.fill(tx - 3 + k, y + 1 + k, tz - 2, tx - 3 + k, y + 1 + k, tz + 2, f'{c}_wool')
            v.fill(tx + 3 - k, y + 1 + k, tz - 2, tx + 3 - k, y + 1 + k, tz + 2, f'{c}_wool')
        v.set(tx, y + 1, tz, 'barrel[facing=up]')
    v.set(cx, y + 1, cz, 'campfire[lit=true]')
    v.set(cx + 4, y + 1, cz + 2, 'anvil[facing=north]')
    v.set(cx + 5, y + 1, cz + 2, 'smithing_table')
    spot('thrain', cx - 2, y + 1, cz - 4)
    spot('waystone_s', cx + 3, y + 1, cz - 3)
    v.set(cx + 3, y + 1, cz - 3, 'lodestone')
    v.set(cx + 3, y + 2, cz - 3, 'amethyst_cluster[facing=up]')
    LORE.append(('s', cx + 12, y + 1, cz + 8))
    return v


def dwarf_gate():
    """Porte de Khazgarde taillée dans la falaise (z ≈ 140) + grande salle creusée dans la montagne (arène du Colosse)."""
    x0, zf = W.P['kgate']
    y = 66
    v = Vox(802)
    r = v.r
    deep = lambda x, yy, z: 'deepslate_bricks' if r.random() < 0.7 else ('deepslate_tiles' if r.random() < 0.5 else 'cracked_deepslate_bricks')
    # parvis
    v.fill(x0 - 14, y, zf - 10, x0 + 14, y, zf - 1, 'polished_deepslate')
    for z in range(zf - 10, zf):
        for x in (x0 - 14, x0 + 14):
            v.set(x, y + 1, z, 'deepslate_brick_wall')
    # façade : cadre de la porte, statues
    v.fill(x0 - 12, y, zf, x0 + 12, y + 30, zf + 1, deep)
    v.fill(x0 - 5, y + 1, zf, x0 + 5, y + 14, zf + 1, AIR)
    for yy in range(y + 15, y + 19):
        hw = 5 - (yy - y - 15)
        v.fill(x0 - hw, yy, zf, x0 + hw, yy, zf + 1, AIR)
    v.fill(x0 - 6, y + 1, zf - 1, x0 - 6, y + 16, zf - 1, 'polished_deepslate')
    v.fill(x0 + 6, y + 1, zf - 1, x0 + 6, y + 16, zf - 1, 'polished_deepslate')
    v.fill(x0 - 6, y + 17, zf - 1, x0 + 6, y + 17, zf - 1, 'chiseled_deepslate')
    # portes de pierre (fermées tant que les runes ne sont pas activées) : bloc témoin
    SPOTS['kgate_door'] = (x0 - 4, y + 1, zf, x0 + 4, y + 13, zf + 1)
    for sx in (-9, 9):
        x = x0 + sx
        v.fill(x - 1, y + 1, zf - 2, x + 1, y + 3, zf - 1, 'polished_deepslate')
        v.fill(x, y + 4, zf - 2, x, y + 14, zf - 2, 'chiseled_deepslate')
        v.fill(x - 1, y + 10, zf - 2, x + 1, y + 11, zf - 2, 'deepslate_tiles')
        v.set(x, y + 15, zf - 2, 'gold_block')
        v.set(x, y + 16, zf - 2, 'lightning_rod')
    # pierres runiques (4) sur le parvis
    runes = []
    for i, x in enumerate((x0 - 10, x0 - 4, x0 + 4, x0 + 10)):
        z = zf - 7
        v.set(x, y + 1, z, 'chiseled_tuff_bricks')
        v.set(x, y + 2, z, 'chiseled_tuff')
        runes.append((x + 0.5, y + 1, z + 0.5))
    SPOTS['runes'] = runes
    # grande salle creusée
    hz1, hz2 = zf + 2, zf + 64
    for z in range(hz1, hz2 + 1):
        for x in range(x0 - 16, x0 + 17):
            v.fill(x, y + 1, z, x, y + 22, z, AIR)
            v.set(x, y, z, 'polished_deepslate' if (x + z) % 2 else 'deepslate_tiles')
        for x in (x0 - 17, x0 + 17):
            v.fill(x, y - 1, z, x, y + 23, z, deep)
        v.fill(x0 - 17, y + 23, z, x0 + 17, y + 23, z, deep)
    v.fill(x0 - 17, y - 1, hz2 + 1, x0 + 17, y + 23, hz2 + 1, deep)
    v.fill(x0 - 17, y - 1, hz1 - 1, x0 - 6, y + 23, hz1 - 1, deep)
    v.fill(x0 + 6, y - 1, hz1 - 1, x0 + 17, y + 23, hz1 - 1, deep)
    for z in range(hz1 + 4, hz2 - 2, 8):
        for x in (x0 - 10, x0 + 10):
            v.fill(x - 1, y + 1, z - 1, x + 1, y + 22, z + 1, 'polished_deepslate')
            v.fill(x - 2, y + 18, z - 2, x + 2, y + 18, z + 2, 'chiseled_deepslate')
            v.set(x + 2, y + 8, z, 'lantern[hanging=false]') if False else None
            v.set(x, y + 8, z - 2, 'lantern') if False else None
        v.fill(x0 - 15, y, z, x0 - 13, y, z + 2, 'lava')
        v.fill(x0 + 13, y, z, x0 + 15, y, z + 2, 'lava')
    for z in range(hz1 + 2, hz2, 6):
        v.lamp(x0, y + 20, z, kind='lantern')
        v.set(x0, y + 21, z, 'iron_chain')
        v.set(x0, y + 22, z, 'iron_chain')
    # trône du roi (fond) et arène du Colosse
    v.fill(x0 - 4, y + 1, hz2 - 3, x0 + 4, y + 2, hz2, 'polished_deepslate')
    v.fill(x0 - 1, y + 3, hz2 - 1, x0 + 1, y + 6, hz2 - 1, 'gold_block')
    v.set(x0, y + 3, hz2 - 2, 'deepslate_brick_stairs[facing=north]')
    ARENAS['colosse'] = dict(c=(x0 + 0.5, y + 1, hz2 - 16 + 0.5), r=16)
    # piliers runiques du Colosse (4) : leviers
    lev = []
    for (dx, dz) in ((-12, -24), (12, -24), (-12, -6), (12, -6)):
        x, z = x0 + dx, hz2 + dz
        v.fill(x, y + 1, z, x, y + 4, z, 'chiseled_tuff_bricks')
        v.set(x, y + 5, z, 'light_blue_stained_glass')
        lev.append((x + 0.5, y + 1, z + 0.5))
    SPOTS['colosse_pillars'] = lev
    LORE.append(('s', x0 + 14, y + 1, hz1 + 3))
    spot('kgate_in', x0, y + 1, hz1 + 4)
    return v


# ================================================================ TERRES D'OMBRE
def rebel_camp():
    cx, cz = W.P['rebels']
    y = 64
    v = Vox(901)
    r = v.r
    for x in range(cx - 14, cx + 15):
        for z in range(cz - 14, cz + 15):
            d = max(abs(x - cx), abs(z - cz))
            if d == 14 and (abs(x - cx) > 2 and abs(z - cz) > 2):
                v.fill(x, y + 1, z, x, y + 2, z, 'spruce_fence' if r.random() < 0.6 else 'dark_oak_fence')
    for i, (tx, tz) in enumerate(((cx - 8, cz - 8), (cx + 8, cz - 8), (cx - 8, cz + 8), (cx + 8, cz + 8))):
        c = ['red', 'blue', 'white', 'yellow'][i]
        for k in range(4):
            v.fill(tx - 3 + k, y + 1 + k, tz - 2, tx - 3 + k, y + 1 + k, tz + 2, f'{c}_wool')
            v.fill(tx + 3 - k, y + 1 + k, tz - 2, tx + 3 - k, y + 1 + k, tz + 2, f'{c}_wool')
    v.set(cx, y + 1, cz, 'soul_campfire[lit=true]')
    v.fill(cx - 2, y + 1, cz + 3, cx + 2, y + 1, cz + 3, 'spruce_planks')
    v.set(cx, y + 2, cz + 3, 'cartography_table') if False else v.set(cx, y + 1, cz + 4, 'cartography_table')
    spot('aldric_sw', cx + 2, y + 1, cz + 2)
    spot('waystone_sw', cx - 3, y + 1, cz + 2)
    v.set(cx - 3, y + 1, cz + 2, 'lodestone')
    v.set(cx - 3, y + 2, cz + 2, 'amethyst_cluster[facing=up]')
    LORE.append(('sw', cx + 9, y + 1, cz + 10))
    return v


def citadel():
    """Citadelle de Malveth : enceinte noire, 3 pylônes dans la cour, donjon (trône de Malveth), sommet (arène de Nyxar)."""
    x1, z1, x2, z2 = -206, 144, -138, 212
    y = 66
    v = Vox(902)
    r = v.r
    wl = lambda x, yy, z: 'polished_blackstone_bricks' if r.random() < 0.7 else ('cracked_polished_blackstone_bricks' if r.random() < 0.6 else 'gilded_blackstone')
    cx, cz = (x1 + x2) // 2, (z1 + z2) // 2
    v.fill(x1, y, z1, x2, y, z2, 'polished_blackstone')
    v.walls(x1, z1, x2, z2, y + 1, y + 14, wl)
    for k in (0, 1):
        v.walls(x1 + 1 + k, z1 + 1 + k, x2 - 1 - k, z2 - 1 - k, y + 1, y + 13, wl)
    crenels(v, x1, z1, x2, z1, y + 15, 'polished_blackstone_bricks')
    crenels(v, x1, z2, x2, z2, y + 15, 'polished_blackstone_bricks')
    crenels(v, x1, z1, x1, z2, y + 15, 'polished_blackstone_bricks')
    crenels(v, x2, z1, x2, z2, y + 15, 'polished_blackstone_bricks')
    for (tx, tz) in ((x1, z1), (x2, z1), (x1, z2), (x2, z2), (cx, z1), (cx, z2), (x1, cz), (x2, cz)):
        round_tower(v, tx, tz, y + 1, 5, 22, wl, floor='polished_blackstone', crenel='polished_blackstone_bricks', roof='black_concrete', roof_h=10)
        v.set(tx, y + 23, tz, 'soul_lantern') if False else None
    # porte (est, vers le camp rebelle)
    v.fill(x2 - 5, y + 1, cz - 2, x2 + 5, y + 9, cz + 2, AIR)       # traverse aussi l'anneau (rayon 5) de la tour de la porte ; 5 de large comme les barreaux
    v.fill(x2 - 5, y + 10, cz - 2, x2 + 5, y + 10, cz + 2, 'chiseled_polished_blackstone')
    v.fill(x2, y + 1, cz - 2, x2, y + 8, cz + 2, 'iron_bars')
    v.fill(x2, y + 1, cz - 4, x2, y + 9, cz - 3, wl)                  # flancs des barreaux : l'intérieur de la tour (rayon 5) les laissait contourner
    v.fill(x2, y + 1, cz + 3, x2, y + 9, cz + 4, wl)
    v.fill(x2, y + 9, cz - 2, x2, y + 9, cz + 2, wl)                  # fente au-dessus des barreaux
    SPOTS['cit_gate'] = (x2, y + 1, cz - 2, x2, y + 8, cz + 2)
    spot('cit_out', x2 + 6, y + 1, cz)
    # pylônes de la cour
    pyl = []
    for (dx, dz) in ((18, -16), (18, 16), (-4, 22)):
        x, z = cx + dx, cz + dz
        v.fill(x - 1, y + 1, z - 1, x + 1, y + 2, z + 1, 'crying_obsidian')
        v.fill(x, y + 3, z, x, y + 9, z, 'obsidian')
        v.set(x, y + 10, z, 'respawn_anchor[charges=4]')
        pyl.append((x + 0.5, y + 1, z + 0.5))
    SPOTS['pylons'] = pyl
    # donjon central (salle du trône au rez-de-chaussée, sommet = arène de Nyxar)
    kx1, kz1, kx2, kz2 = cx - 14, cz - 14, cx + 14, cz + 14
    v.walls(kx1, kz1, kx2, kz2, y + 1, y + 34, wl)
    v.fill(kx1 + 1, y + 1, kz1 + 1, kx2 - 1, y + 33, kz2 - 1, AIR)
    v.fill(kx1, y + 35, kz1, kx2, y + 35, kz2, 'polished_blackstone_bricks')
    crenels(v, kx1, kz1, kx2, kz1, y + 36, 'polished_blackstone_bricks')
    crenels(v, kx1, kz2, kx2, kz2, y + 36, 'polished_blackstone_bricks')
    crenels(v, kx1, kz1, kx1, kz2, y + 36, 'polished_blackstone_bricks')
    crenels(v, kx2, kz1, kx2, kz2, y + 36, 'polished_blackstone_bricks')
    for x in range(kx1 + 3, kx2 - 2, 5):
        for (zz) in (kz1, kz2):
            v.fill(x, y + 4, zz, x, y + 12, zz, 'purple_stained_glass_pane')
    v.fill(kx2, y + 1, cz - 2, kx2, y + 6, cz + 2, AIR)
    # trône de Malveth (ouest de la salle)
    v.fill(kx1 + 1, y + 1, cz - 4, kx1 + 4, y + 2, cz + 4, 'crying_obsidian')
    v.fill(kx1 + 1, y + 3, cz - 1, kx1 + 1, y + 9, cz + 1, 'obsidian')
    v.set(kx1 + 2, y + 3, cz, 'polished_blackstone_stairs[facing=east]')
    for z in range(kz1 + 3, kz2 - 2, 6):
        for x in range(kx1 + 6, kx2 - 2, 7):
            v.fill(x, y + 1, z, x, y + 33, z, 'polished_blackstone')
            v.set(x, y + 20, z + 1, 'soul_lantern') if False else None
    for z in range(kz1 + 4, kz2 - 3, 5):
        v.lamp(cx, y + 30, z, kind='soul_lantern')
    ARENAS['malveth'] = dict(c=(cx + 0.5, y + 1, cz + 0.5), r=13, throne=(kx1 + 3.5, y + 3, cz + 0.5))
    # escalier vers le sommet (coin sud-est intérieur), en colimaçon carré
    sx, sz = kx2 - 3, kz2 - 3
    for i, yy in enumerate(range(y + 1, y + 35)):
        k = i % 8
        dx, dz = [(0, 0), (-1, 0), (-2, 0), (-2, -1), (-2, -2), (-1, -2), (0, -2), (0, -1)][k]
        v.set(sx + dx, yy, sz + dz, 'polished_blackstone_brick_slab[type=top]')
    v.fill(sx - 2, y + 35, sz - 2, sx, y + 35, sz, AIR)
    ARENAS['nyxar'] = dict(c=(cx + 0.5, y + 36, cz + 0.5), r=13)
    LORE.append(('sw', kx1 + 5, y + 1, kz1 + 4))
    return v


def soul_well_entry():
    x0, z0 = W.P['soul_well']
    y = 64
    v = Vox(903)
    for x in range(x0 - 5, x0 + 6):
        for z in range(z0 - 5, z0 + 6):
            d = math.hypot(x - x0, z - z0)
            if d <= 5.4:
                v.set(x, y, z, 'polished_blackstone_bricks')
    for a in range(0, 360, 45):
        x, z = round(x0 + 5 * math.cos(math.radians(a))), round(z0 + 5 * math.sin(math.radians(a)))
        v.fill(x, y + 1, z, x, y + 4, z, 'polished_blackstone_wall' if a % 90 else 'crying_obsidian')
        v.set(x, y + 5, z, 'soul_lantern') if a % 90 == 0 else None
    return v


# ================================================================ entrées des donjons (petits bâtiments) + donjons
def chapel():
    x0, z0 = W.P['crypt']
    y = 66
    v = Vox(204)
    r = v.r
    v.fill(x0 - 5, y + 1, z0 - 8, x0 + 5, y + 7, z0 + 4, 'stone_bricks', hollow=True)
    v.fill(x0 - 4, y + 1, z0 - 7, x0 + 4, y + 7, z0 + 3, AIR)
    v.ruin(x0 - 5, y + 1, z0 - 8, x0 + 5, y + 7, z0 + 4, 0.25, {'stone_bricks': 'mossy_stone_bricks'})
    v.fill(x0 - 1, y + 1, z0 + 4, x0 + 1, y + 4, z0 + 4, AIR)
    # tombes
    for i in range(10):
        x, z = x0 - 9 + (i % 5) * 4, z0 + 7 + (i // 5) * 4
        v.set(x, y + 1, z, 'cobblestone_wall' if r.random() < 0.5 else 'mossy_cobblestone_wall')
        v.set(x, y, z + 1, 'coarse_dirt')
    return v


def all_structures():
    """Liste (nom, région, Vox) de toutes les constructions, avec les donjons."""
    S = []
    S.append(('city', 'hub', city()))
    S += [('brumecombe', 'w', brumecombe()), ('windmill', 'w', windmill()), ('bandit_fort', 'w', bandit_fort()), ('chapel', 'w', chapel())]
    S += [('aelindor', 'nw', aelindor()), ('spider_lair', 'nw', spider_lair()), ('shrine', 'nw', shrine())]
    S += [('hrafnheim', 'n', hrafnheim()), ('giant_hold', 'n', giant_hold())]
    S += [('stilts', 'ne', stilt_village()), ('witch_isle', 'ne', witch_isle())]
    S += [('oasis', 'e', oasis_town()), ('pyramid', 'e', pyramid()), ('obelisks', 'e', obelisks())]
    S += [('bastion', 'se', bastion()), ('caldera', 'se', caldera())]
    S += [('dwarf_camp', 's', dwarf_camp()), ('dwarf_gate', 's', dwarf_gate())]
    S += [('rebels', 'sw', rebel_camp()), ('citadel', 'sw', citadel()), ('soul_well', 'sw', soul_well_entry())]
    # donjons : (clé, région, entrée x z y, sol, thème, direction, nom, alpha)
    cx, cz = W.P['crypt']
    S.append(('dg_crypt', 'w', dungeon('crypt', 'w', (cx, cz - 4, 67), 50, 'crypt', 'south', 'Cryptes de Valdor', 'Seigneur des cryptes')))
    x, z = W.P['spider_nest']
    S.append(('dg_nest', 'nw', dungeon('nest', 'nw', (x, z, 71), 54, 'nest', 'north', 'Nid des tisseuses', 'Tisseuse alpha')))
    x, z = W.P['ice_cave']
    S.append(('dg_ice', 'n', dungeon('ice', 'n', (x, z, 87), 66, 'ice', 'east', 'Grotte de givre', 'Wendigo des glaces')))
    x, z = W.P['sunken']
    S.append(('dg_sunken', 'ne', dungeon('sunken', 'ne', (x, z, 64), 48, 'sunken', 'east', 'Temple englouti', 'Gardien noyé')))
    x, z = W.P['tombs']
    S.append(('dg_tomb', 'e', dungeon('tomb', 'e', (x, z, 65), 48, 'tomb', 'west', 'Tombeaux d\'Azhar', 'Momie royale')))
    x, z = W.P['forge_r']
    S.append(('dg_forge', 'se', dungeon('forge', 'se', (x, z, 71), 52, 'forge', 'south', 'Forge écarlate', 'Forgeron calciné')))
    x, z = W.P['mines']
    mx, mz = x, 126
    S.append(('dg_mine', 's', dungeon('mine', 's', (mx, mz, 67), 48, 'mine', 'south', 'Mines profondes', 'Contremaître maudit')))
    x, z = W.P['soul_well']
    S.append(('dg_souls', 'sw', dungeon('souls', 'sw', (x, z + 6, 65), 46, 'souls', 'south', 'Puits des âmes', 'Gardien des âmes')))
    return S
