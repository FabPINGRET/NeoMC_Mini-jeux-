"""🗺 Terra Nova RPG : les quatre régions autour de la vallée (exécuté par gen_terranova.py, après la vallée).

Carte en croix : vallée de la colonie (x, z de -96 à 95) au centre, reliée par un col à chaque région.
  Nord  : Marais des Brumes   x -96..95,   z -256..-97   (col x -30)
  Est   : Plaines d'Ambre     x 96..255,   z -96..95     (col z 30)
  Ouest : Canyon des Renégats x -256..-97, z -96..95     (col z 6)
  Sud   : Mont Cendre         x -96..95,   z 96..255     (col x -24)
Chaque région : relief (falaises au bord, couloir du col ouvert), biome du datapack (couleurs, brume, particules, musique),
structures, végétation (« place feature »), marqueurs d'apparition par espèce, lieux à découvrir et balises de voyage.
Utilise : noise, js, w, DIM, rnd (non : tirages propres rw), HX, G.
"""
import math as _m
import random as _r

import functools as _ft

rw = _r.Random(7331)


@_ft.lru_cache(maxsize=None)
def _hc(seed, i, j):
    return _r.Random(seed * 1000003 + i * 7919 + j * 104729).uniform(-1, 1)


def noise(seed, cell, x, z):
    """Bruit de valeur lissé (même formule que gen_terranova.noise, avec cache)."""
    fx, fz = x / cell, z / cell
    i, j = _m.floor(fx), _m.floor(fz)
    tx, tz = fx - i, fz - j
    sx, sz = tx * tx * (3 - 2 * tx), tz * tz * (3 - 2 * tz)
    a, b, c, d = _hc(seed, i, j), _hc(seed, i + 1, j), _hc(seed, i, j + 1), _hc(seed, i + 1, j + 1)
    return (a + (b - a) * sx) * (1 - sz) + (c + (d - c) * sx) * sz
REGIONS = {
    'n': {'name': 'Marais des Brumes', 'rect': (-96, -256, 96, -96), 'lv': 4, 'col': 'dark_aqua', 'biome': 'mg:tv_marais'},
    'e': {'name': 'Plaines d\'Ambre', 'rect': (96, -96, 256, 96), 'lv': 8, 'col': 'gold', 'biome': 'mg:tv_plaines'},
    'w': {'name': 'Canyon des Renégats', 'rect': (-256, -96, -96, 96), 'lv': 12, 'col': 'red', 'biome': 'mg:tv_canyon'},
    's': {'name': 'Mont Cendre', 'rect': (-96, 96, 96, 256), 'lv': 16, 'col': 'dark_red', 'biome': 'mg:tv_volcan'},
}
VALLEY_BIOME = 'mg:tv_jungle'
# col : (région, axe du bord, coordonnée du couloir)  axe 'z' = bord horizontal (nord/sud), le couloir suit x = c
# PASSES, PASS_Y : définis dans gen_terranova.py (falaises de la vallée creusées aux mêmes endroits)
PASS_GATE = {'n': (-30, -90), 's': (-24, 90), 'e': (90, 30), 'w': (-90, 6)}   # barrière (côté vallée)


def pass_open(key, x, z):
    """Distance au couloir du col de la région key (None si on n'est pas dans la bande du bord)."""
    ax, c = PASSES[key]
    return abs(x - c) if ax == 'z' else abs(z - c)


def rim(x, z, rect, key, depth=12, rise=30):
    """Hausse du relief près du bord de la région (falaises), sauf dans le couloir du col (côté vallée)."""
    x0, z0, x1, z1 = rect
    d = {'w': x - x0, 'e': x1 - 1 - x, 'n': z - z0, 's': z1 - 1 - z}
    inner = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}[key]     # côté de la région qui touche la vallée
    e = min(d.values())
    if e >= depth:
        return 0, False
    side = min(d, key=d.get)
    if side == inner:
        po = pass_open(key, x, z)
        if po <= 3:
            return 0, True
        if po <= 7:
            return ((depth - e) / depth) ** 2 * rise * (po - 3) / 4, False
    return ((depth - e) / depth) ** 2 * rise, False


def in_rect(x, z, rect):
    x0, z0, x1, z1 = rect
    return x0 <= x < x1 and z0 <= z < z1


def lerp(a, b, t):
    return a + (b - a) * t


def smooth(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def polyline(pts, step=1.0):
    out = []
    for (x1, z1), (x2, z2) in zip(pts, pts[1:]):
        n = max(1, int(max(abs(x2 - x1), abs(z2 - z1)) / step))
        for s in range(n):
            out.append((x1 + (x2 - x1) * s / n, z1 + (z2 - z1) * s / n))
    out.append(pts[-1])
    return out


def cells_near(path, r):
    S = set()
    for (px, pz) in path:
        for dx in range(-r, r + 1):
            for dz in range(-r, r + 1):
                if dx * dx + dz * dz <= r * r + 1:
                    S.add((round(px) + dx, round(pz) + dz))
    return S


# ================================================================ relief par région : colonne -> (h, dessus, dessous, fluide, niveau du fluide)
COL = {}            # (x, z) -> dict
ROADS = {}          # région -> ensemble de cases de chemin

# ---------------------------------------------------------------- Nord : Marais des Brumes
RN = REGIONS['n']['rect']
LAG = (10, -196)                                # lagune (antre du spinosaure), île au centre
ECHO = (-30, -122)                              # Poste Écho (camp)
STATION = (-62, -168)                           # station de recherche engloutie
MOTHER = (55, -178)                             # Arbre-Mère
JETTY = (62, -118)                              # ponton des pêcheurs
N_ROAD = polyline([(-30, -97), (-30, -115), (-34, -128), (-52, -150), (-60, -160)]) + \
    polyline([(-34, -128), (-20, -150), (-8, -172), (2, -184)]) + polyline([(-30, -115), (10, -116), (55, -118)])
ROADS['n'] = cells_near(N_ROAD, 1)
for x in range(RN[0], RN[2]):
    for z in range(RN[1], RN[3]):
        add, corridor = rim(x, z, RN, 'n')
        raw = 62.3 + 1.7 * noise(31, 16, x, z) + 0.9 * noise(32, 6, x, z) + 0.5 * noise(33, 3, x, z)
        dl = _m.hypot(x - LAG[0], z - LAG[1])
        top, under, fl, fll = 'grass_block', 'dirt', None, 0
        if dl < 9:
            h = 64
            top = 'mossy_stone_bricks' if dl < 7.5 else 'mud_bricks'
        elif dl < 34:
            h, fl, fll = 61, 'water', 62
            top = 'mud' if (x + z) % 3 else 'clay'
        elif raw < 61.7:
            h, fl, fll = 60, 'water', 62
            top = 'mud' if noise(34, 5, x, z) > 0 else 'clay'
        else:
            h = max(63, round(raw))
            top = 'mud' if raw < 62.4 else ('moss_block' if noise(35, 7, x, z) > 0.45 else 'grass_block')
            under = 'mud' if raw < 62.4 else 'dirt'
        dz0 = RN[3] - 1 - z
        if dz0 < 16 and pass_open('n', x, z) <= 6:
            h, fl = round(lerp(PASS_Y, h, smooth(dz0 / 16))), None
            top = 'dirt_path' if pass_open('n', x, z) <= 1 else 'grass_block'
        if corridor:
            h, fl, top = PASS_Y, None, 'dirt_path' if pass_open('n', x, z) <= 1 else 'grass_block'
        if add:
            h = round(h + add)
            fl = None if h > 62 else fl
            top = 'stone' if add > 6 else top
            under = 'stone' if add > 6 else under
        if (x, z) in ROADS['n'] and not fl and dl >= 34:
            top = 'dirt_path'
        COL[(x, z)] = (h, top, under, fl, fll)

# ---------------------------------------------------------------- Est : Plaines d'Ambre
RE = REGIONS['e']['rect']
LAKE = (178, -22)
DELTA = (128, 6)                                 # Camp Delta
SPIRES = [(222, 58), (232, 44), (214, 72), (238, 66), (206, 52), (226, 80), (244, 50)]
BONES = (150, 62)                                # cimetière des géants
NEST = (228, 24)                                  # le Pic du Nid (donjon)
E_ROAD = polyline([(97, 30), (112, 22), (128, 8), (150, -6), (165, -18)]) + polyline([(128, 8), (140, 40), (150, 56)]) + \
    polyline([(150, 56), (190, 60), (210, 60)])
ROADS['e'] = cells_near(E_ROAD, 1)
for x in range(RE[0], RE[2]):
    for z in range(RE[1], RE[3]):
        add, corridor = rim(x, z, RE, 'e')
        raw = 67 + 3.5 * noise(41, 42, x, z) + 1.4 * noise(42, 13, x, z) + 0.5 * noise(43, 5, x, z)
        top, under, fl, fll = 'grass_block', 'dirt', None, 0
        dl = _m.hypot(x - LAKE[0], z - LAKE[1])
        h = round(raw)
        if dl < 20:
            bowl = 62 - 3 * (1 - dl / 20) ** 0.6
            if dl < 15:
                h, fl, fll, top = round(bowl), 'water', 62, 'sand' if dl > 11 else 'clay'
            else:
                h = round(lerp(63, raw, (dl - 15) / 5))
                top = 'sand'
        elif noise(44, 9, x, z) > 0.55:
            top = 'coarse_dirt'
        dx0 = x - RE[0]
        if dx0 < 16 and pass_open('e', x, z) <= 6:
            h = round(lerp(PASS_Y, h, smooth(dx0 / 16)))
        if corridor:
            h, top = PASS_Y, 'dirt_path' if pass_open('e', x, z) <= 1 else 'grass_block'
        if add:
            h = round(h + add)
            top = under = 'stone' if add > 6 else top
            under = 'stone' if add > 6 else 'dirt'
        if (x, z) in ROADS['e'] and not fl:
            top = 'dirt_path'
        COL[(x, z)] = (h, top, under, fl, fll)

# ---------------------------------------------------------------- Ouest : Canyon des Renégats
RW = REGIONS['w']['rect']
FORT = (-200, 4)
MINE = (-215, -55)                                # mine abandonnée (mesa forcée)
ARCH = (-150, -58)
LOOKOUT = (-142, 62)                             # Belvédère (camp)
W_ROUTE = polyline([(-97, 6), (-120, 4), (-140, 16), (-165, 6), (-180, 4)]) + polyline([(-140, 16), (-142, 40), (-142, 56)]) + \
    polyline([(-120, 4), (-135, -20), (-148, -45), (-150, -58)]) + polyline([(-150, -58), (-172, -56), (-186, -55)])
ROADS['w'] = cells_near(W_ROUTE, 1)
W_FLOOR = cells_near(W_ROUTE, 6)
STRATA = ['orange_terracotta', 'terracotta', 'yellow_terracotta', 'white_terracotta', 'red_terracotta', 'light_gray_terracotta',
          'brown_terracotta', 'orange_terracotta', 'red_terracotta', 'terracotta']
for x in range(RW[0], RW[2]):
    for z in range(RW[1], RW[3]):
        add, corridor = rim(x, z, RW, 'w')
        m = noise(51, 30, x, z) + 0.35 * noise(52, 11, x, z)
        floor = 64 + round(1.2 * noise(53, 8, x, z))
        top, under, fl, fll = 'red_sand', 'red_sandstone', None, 0
        if (x, z) in W_FLOOR or _m.hypot(x - FORT[0], z - FORT[1]) < 30 or _m.hypot(x - ARCH[0], z - ARCH[1]) < 9:
            m = min(m, -0.2)
        if _m.hypot(x - MINE[0], z - MINE[1]) < 24 and x < -192:
            m = 0.5
        if m > 0.18:
            h = 84 + 2 * round(noise(54, 14, x, z))
            top, under = 'red_sand' if noise(55, 6, x, z) > 0.2 else 'coarse_dirt', 'strata'
        elif m > 0.06:
            h = 74 + round(2 * noise(54, 14, x, z))
            top, under = 'red_sand', 'strata'
        else:
            h = floor
            top = 'red_sand' if noise(56, 7, x, z) > -0.3 else 'terracotta'
        dx0 = RW[2] - 1 - x
        if dx0 < 14 and pass_open('w', x, z) <= 6:
            h = round(lerp(PASS_Y, h, smooth(dx0 / 14)))
        if corridor:
            h, top, under = PASS_Y, 'dirt_path' if pass_open('w', x, z) <= 1 else 'red_sand', 'red_sandstone'
        if add:
            h = round(h + add)
            top, under = 'red_sand', 'strata'
        if (x, z) in ROADS['w'] and h < 70:
            top = 'dirt_path'
        COL[(x, z)] = (h, top, under, fl, fll)

# ---------------------------------------------------------------- Sud : Mont Cendre
RS = REGIONS['s']['rect']
VOLC = (0, 186)
CALD_Y = 98                                       # sol de la caldeira (arène du Roi Tyran)
REFUGE = (-26, 122)                               # Refuge du Cendre (camp)
BRIDGE = (58, 176)                                # pont d'obsidienne (au-dessus d'une faille de lave)
S_PATH = [(-24, 97), (-24, 112), (-40, 138), (-54, 176), (-46, 214), (-14, 240), (24, 238), (52, 214), (60, 182), (48, 150),
          (18, 136), (-12, 142), (-30, 160), (-32, 186), (-22, 208), (0, 214), (0, 203)]
S_ROAD = polyline(S_PATH, 0.5)
ROAD_LEN = len(S_ROAD)
S_ROADH = {}
for i, (px, pz) in enumerate(S_ROAD):
    y = lerp(PASS_Y, CALD_Y, smooth(i / (ROAD_LEN - 1)) * 0.5 + i / (ROAD_LEN - 1) * 0.5)
    for dx in range(-2, 3):
        for dz in range(-2, 3):
            c = (round(px) + dx, round(pz) + dz)
            if dx * dx + dz * dz <= 5 and c not in S_ROADH:
                S_ROADH[c] = round(y)
S_ROADH = {c: y for c, y in S_ROADH.items() if in_rect(c[0], c[1], REGIONS['s']['rect'])}
BR_Y = S_ROADH[min(S_ROADH, key=lambda c: _m.hypot(c[0] - BRIDGE[0], c[1] - BRIDGE[1]))]
ROADS['s'] = {c for c in S_ROADH}


def volc_h(x, z):
    d = _m.hypot(x - VOLC[0], z - VOLC[1])
    base = 64 + 2.5 * noise(61, 20, x, z) + 0.8 * noise(62, 6, x, z)
    if d < 15:
        return CALD_Y, d
    if d < 19:                                     # bord de la caldeira
        return round(lerp(CALD_Y + 10, 116, (d - 15) / 4)), d
    cone = 116 * 1.0 - (d - 19) * 0.95 + 2.5 * noise(63, 9, x, z)
    return round(max(base, cone)), d


for x in range(RS[0], RS[2]):
    for z in range(RS[1], RS[3]):
        add, corridor = rim(x, z, RS, 's')
        h, d = volc_h(x, z)
        top, under, fl, fll = 'basalt', 'blackstone', None, 0
        n1 = noise(64, 8, x, z)
        if d < 15:
            top, under = ('polished_blackstone' if (x + z) % 2 else 'blackstone') if d < 13 else 'magma_block', 'blackstone'
        elif h > 92:
            top = 'blackstone' if n1 > 0.2 else ('tuff' if n1 > -0.3 else 'basalt')
            under = 'tuff'
        elif h > 70:
            top = 'tuff' if n1 > 0.3 else ('basalt' if n1 > -0.2 else 'coarse_dirt')
            under = 'tuff'
        else:
            top = 'coarse_dirt' if n1 > 0.1 else ('basalt' if n1 > -0.35 else 'gray_concrete_powder')
            under = 'dirt'
            if noise(65, 10, x, z) > 0.62:               # mares de lave dans les champs de basalte
                h, fl, fll, top = 62, 'lava', 63, 'magma_block'
        if abs(z - BRIDGE[1]) <= 3 and abs(x - BRIDGE[0]) <= 8:                   # faille de lave sous le pont
            h, fl, fll, top = BR_Y - 7, 'lava', BR_Y - 6, 'magma_block'
        dz0 = z - RS[1]
        if dz0 < 16 and pass_open('s', x, z) <= 6:
            h = round(lerp(PASS_Y, h, smooth(dz0 / 16)))
        if corridor:
            h, top = PASS_Y, 'dirt_path' if pass_open('s', x, z) <= 1 else 'coarse_dirt'
        if (x, z) in S_ROADH and fl is None:
            h, top = S_ROADH[(x, z)], 'dirt_path' if abs(hash((x, z)) % 7) else 'coarse_dirt'
        if add:
            h = round(h + add)
            top = under = 'blackstone' if add > 6 else top
        COL[(x, z)] = (h, top, under, fl, fll)

# pont d'obsidienne : la route passe au-dessus de la faille (le pont est posé dans les structures)
for (x, z), y in S_ROADH.items():
    if (x, z) in COL and COL[(x, z)][3] == 'lava':
        COL[(x, z)] = COL[(x, z)]


# ================================================================ commandes de relief (colonnes identiques fusionnées le long de z)
def col_segments(x, z, clear_to=None):
    h, top, under, fl, fll = COL[(x, z)]
    seg = []
    if under == 'strata':
        y = 56
        while y < h:
            band = STRATA[((y - 56) // 3) % len(STRATA)]
            y2 = min(h - 1, y + 2 - (y - 56) % 3)
            seg.append((y, y2, band))
            y = y2 + 1
    elif h - 1 >= 56:
        seg.append((56, h - 1, under))
    seg.append((h, h, top))
    if fl and fll > h:
        seg.append((h + 1, fll, fl))
    if clear_to:
        y0 = max(h, fll if fl else h) + 1
        if clear_to >= y0:
            seg.append((y0, clear_to, 'air'))
    return tuple(seg)


def terrain_cmds(cells, clear_to=None):
    out = []
    byx = {}
    for (x, z) in cells:
        byx.setdefault(x, []).append(z)
    for x in sorted(byx):
        zs = sorted(byx[x])
        i = 0
        while i < len(zs):
            z = zs[i]
            key = col_segments(x, z, clear_to)
            j = i
            while j + 1 < len(zs) and zs[j + 1] == zs[j] + 1 and col_segments(x, zs[j + 1], clear_to) == key:
                j += 1
            for (y1, y2, b) in key:
                out.append(f'fill {x} {y1} {z} {x} {y2} {zs[j]} minecraft:{b}')
            i = j + 1
    return out


R_TERRAIN = {k: terrain_cmds([c for c in COL if in_rect(c[0], c[1], REGIONS[k]['rect'])], clear_to=None) for k in REGIONS}


def ground(x, z):
    """Hauteur où l'on marche (au-dessus du sol ou du fluide)."""
    h, top, under, fl, fll = COL[(x, z)]
    return (fll if fl else h) + 1


# ================================================================ structures
RS_CMD = {k: [] for k in REGIONS}


def F(k, x1, y1, z1, x2, y2, z2, b, mode=''):
    RS_CMD[k].append(f'fill {x1} {y1} {z1} {x2} {y2} {z2} minecraft:{b}{" " + mode if mode else ""}')


def B(k, x, y, z, b):
    RS_CMD[k].append(f'setblock {x} {y} {z} minecraft:{b}')


import tv_structs as TS


def gh_any(x, z, default=64):
    if (x, z) in COL:
        return COL[(x, z)][0]
    return H.get((x, z), default)


def camp(k, cx, cz, y, wood='spruce', roof='green_wool'):
    """Camp avancé détaillé (plate-forme sur pilotis, cabane, tour de guet, balise de voyage au centre)."""
    RS_CMD[k].extend(TS.camp(cx, cz, y, gh_any, wood, roof.replace('_wool', '')).cmds())


def flatten(k, cx, cz, r, y, top):
    F(k, cx - r, y, cz - r, cx + r, y, cz + r, top)
    F(k, cx - r, y + 1, cz - r, cx + r, y + 12, cz + r, 'air')
    F(k, cx - r, 56, cz - r, cx + r, y - 1, cz + r, 'dirt', 'replace minecraft:air')


# ---------- Nord
camp('n', ECHO[0], ECHO[1], 64, 'mangrove', 'cyan_wool')
for i, (px, pz) in enumerate(N_ROAD):                       # passerelle sur pilotis au-dessus de l'eau
    x, z = round(px), round(pz)
    if (x, z) in COL and COL[(x, z)][3] == 'water':
        F('n', x - 1, 63, z - 1, x + 1, 63, z + 1, 'spruce_planks')
        if i % 6 == 0:
            F('n', x - 1, 59, z - 1, x - 1, 64, z - 1, 'spruce_fence')
            B('n', x - 1, 65, z - 1, 'lantern')
# station de recherche engloutie (2 niveaux, labo, serveurs, inondée, à moitié effondrée) + drone écrasé
sx, sz = STATION
RS_CMD['n'].extend(TS.station(sx, sz).cmds())
DATA_PTS = [(sx - 5, 64, sz + 3), (sx + 16, 66, sz + 11), (sx + 5, 64, sz - 3)]

# lagune : île de l'antre (anneau de pierres, totems d'ossements)
lx, lz = LAG
for a in range(0, 360, 30):
    px, pz = round(lx + 7.5 * _m.cos(_m.radians(a))), round(lz + 7.5 * _m.sin(_m.radians(a)))
    F('n', px, 65, pz, px, 67 + (a // 30) % 2, pz, 'mossy_cobblestone_wall')
for a in range(15, 360, 90):
    px, pz = round(lx + 20 * _m.cos(_m.radians(a))), round(lz + 20 * _m.sin(_m.radians(a)))
    F('n', px, 62, pz, px, 66, pz, 'bone_block')
    F('n', px - 1, 66, pz, px + 1, 66, pz, 'bone_block')
# Arbre-Mère : donjon du nord (tronc creux, escalier, paliers, nid au sommet)
mx, mz = MOTHER
mg_ = ground(mx, mz) - 1
_v, DG_N_ALPHA, DG_N_DOOR = TS.tree_heart(mx, mz, mg_)
RS_CMD['n'].extend(_v.cmds())

# ponton des pêcheurs
jx, jz = JETTY
F('n', jx - 2, 63, jz, jx + 12, 63, jz + 2, 'spruce_planks')
F('n', jx + 6, 63, jz, jx + 8, 63, jz + 2, 'air')
for a in (0, 4, 10):
    F('n', jx + a, 58, jz - 1, jx + a, 64, jz - 1, 'spruce_log')
B('n', jx + 11, 64, jz + 1, 'barrel[facing=up]')
F('n', jx - 2, 63, jz + 3, jx - 2, 66, jz + 3, 'spruce_fence')
B('n', jx - 2, 67, jz + 3, 'lantern')

# ---------- Est
camp('e', DELTA[0], DELTA[1], ground(*DELTA) - 1, 'birch', 'white_wool')
dx_, dz_ = DELTA
gy = ground(*DELTA) - 1
F('e', dx_ + 8, gy + 1, dz_ - 8, dx_ + 10, gy + 10, dz_ - 6, 'stripped_birch_log', 'outline')          # tour de guet
F('e', dx_ + 9, gy + 1, dz_ - 7, dx_ + 9, gy + 10, dz_ - 7, 'ladder[facing=south]')
F('e', dx_ + 7, gy + 11, dz_ - 9, dx_ + 11, gy + 11, dz_ - 5, 'birch_slab')
B('e', dx_ + 9, gy + 11, dz_ - 7, 'air')
F('e', dx_ + 7, gy + 12, dz_ - 9, dx_ + 11, gy + 12, dz_ - 5, 'birch_fence', 'outline')
F('e', dx_ + 9, gy + 13, dz_ - 7, dx_ + 9, gy + 17, dz_ - 7, 'iron_bars')
B('e', dx_ + 9, gy + 18, dz_ - 7, 'lightning_rod')
F('e', dx_ - 10, gy + 1, dz_ - 9, dx_ - 8, gy + 3, dz_ - 7, 'hay_block')
# les Aiguilles (pitons rocheux, nids de ptéranodons au sommet)
NESTS = []
for i, (px, pz) in enumerate(SPIRES):
    top_y = 86 + (i * 7) % 15
    g0 = ground(px, pz) - 1
    r0 = 3 + i % 2
    for y in range(g0 - 1, top_y + 1):
        t = (y - g0) / max(1, top_y - g0)
        r = max(1, round(r0 * (1 - 0.55 * t)))
        F('e', px - r, y, pz - r, px + r, y, pz + r, ['andesite', 'stone', 'tuff', 'stone'][(y // 4 + i) % 4])
    F('e', px - 2, top_y + 1, pz - 2, px + 2, top_y + 1, pz + 2, 'hay_block', 'outline')
    B('e', px, top_y + 1, pz, 'sniffer_egg')
    NESTS.append((px, top_y + 2, pz))
# cimetière des géants (squelette de sauropode en blocs d'os, à moitié enterré)
bx_, bz_ = BONES
by_ = ground(bx_, bz_) - 1
for i in range(-14, 15):                                                  # colonne vertébrale
    y = by_ + round(5 - abs(i) * 0.25)
    B('e', bx_ + i, y, bz_, 'bone_block[axis=x]')
    if i % 3 == 0 and abs(i) < 9:                                            # côtes
        for s in (-1, 1):
            F('e', bx_ + i, y - 1, bz_ + s, bx_ + i, y - 1, bz_ + 3 * s, 'bone_block[axis=z]')
            F('e', bx_ + i, by_, bz_ + 4 * s, bx_ + i, y - 2, bz_ + 4 * s, 'bone_block[axis=y]')
for i in range(1, 10):                                                     # cou couché, crâne
    B('e', bx_ + 14 + i, by_ + 1 + i // 3, bz_ + i // 2, 'bone_block[axis=x]')
F('e', bx_ + 24, by_ + 3, bz_ + 4, bx_ + 26, by_ + 5, bz_ + 6, 'bone_block')
B('e', bx_ + 26, by_ + 4, bz_ + 5, 'air')
for i in range(1, 9):
    B('e', bx_ - 14 - i, by_ + 3 - i // 3, bz_ - i // 3, 'bone_block[axis=x]')
# point d'eau : roseaux et rochers
lx_, lz_ = LAKE

# ---------- Ouest
fx, fz = FORT
fy = 64
RS_CMD['w'].extend(TS.fort(fx, fz, fy).cmds())
CELL = (fx + 10, fy + 1, fz + 10)
# arche rouge
ax_, az_ = ARCH
for t in range(0, 181, 6):
    a = _m.radians(t)
    px, py = round(ax_ + 9 * _m.cos(a)), round(64 + 16 * _m.sin(a))
    F('w', px - 1, py, az_ - 2, px + 1, py + 2, az_ + 2, STRATA[(py // 3) % len(STRATA)])
F('w', ax_ - 11, 64, az_ - 3, ax_ - 7, 70, az_ + 3, 'red_terracotta')
F('w', ax_ + 7, 64, az_ - 3, ax_ + 11, 70, az_ + 3, 'red_terracotta')
# belvédère (camp sur un piton, escalier)
lkx, lkz = LOOKOUT
for y in range(64, 80):
    F('w', lkx - 7, y, lkz - 7, lkx + 7, y, lkz + 7, STRATA[(y // 3) % len(STRATA)])
camp('w', lkx, lkz, 80, 'acacia', 'orange_wool')
for i in range(16):                                                          # escalier en colimaçon
    a = _m.radians(i * 30)
    px, pz = round(lkx + 8 * _m.cos(a)), round(lkz + 8 * _m.sin(a))
    F('w', px - 1, 64 + i, pz - 1, px + 1, 64 + i, pz + 1, 'smooth_red_sandstone')
    F('w', px - 1, 65 + i, pz - 1, px + 1, 68 + i, pz + 1, 'air')

# ---------- Sud
camp('s', REFUGE[0], REFUGE[1], ground(*REFUGE) - 1, 'dark_oak', 'gray_wool')
brx, brz = BRIDGE
by2 = max(S_ROADH.get((brx + dx, brz), 0) for dx in range(-8, 9)) or 92
for x in range(brx - 7, brx + 8):
    for z in range(brz - 2, brz + 3):
        if (x, z) in S_ROADH:
            B('s', x, S_ROADH[(x, z)], z, 'obsidian')
            B('s', x, S_ROADH[(x, z)] + 1, z, 'air')
for (x, z), y in S_ROADH.items():                                             # parapets du pont
    if COL[(x, z)][3] == 'lava':
        F('s', x, y - 4, z, x, y, z, 'obsidian')
        B('s', x, y + 1, z, 'air')
# caldeira : temple en ruine (dallage, estrade, colonnade brisée, crâne géant, cascades de lave), faille temporelle
vx, vz = VOLC
F('s', vx - 2, CALD_Y + 1, vz + 15, vx + 2, CALD_Y + 9, vz + 20, 'air')             # brèche du chemin dans le bord
F('s', vx - 2, CALD_Y, vz + 15, vx + 2, CALD_Y, vz + 20, 'polished_blackstone')
RIFT = (vx, CALD_Y + 1, vz - 9)                                               # la faille temporelle (fin du jeu)
RS_CMD['s'].extend(TS.caldera(vx, vz, CALD_Y, vz - 10).cmds())
# donjon du sud : tube de lave dans le flanc ouest du volcan
TUBE_Y = 90
_v, DG_S_ALPHA, DG_S_DOOR = TS.lava_tube(vx, vz, -46, TUBE_Y)
RS_CMD['s'].extend(_v.cmds())
# donjon de l'est : le Pic du Nid
_v, DG_E_ALPHA, DG_E_DOOR = TS.spire_nest(NEST[0], NEST[1], ground(*NEST) - 1)
RS_CMD['e'].extend(_v.cmds())
# donjon de l'ouest : la mine abandonnée (dans une mesa)
_v, DG_W_ALPHA, DG_W_DOOR = TS.mine(MINE[0], MINE[1], 64, 86)
RS_CMD['w'].extend(_v.cmds())
DUNGEONS = [('n', 'arbre', 'Cœur de l\'Arbre-Mère', 'dilo', DG_N_ALPHA, DG_N_DOOR),
            ('e', 'pic', 'Pic du Nid', 'ptera', DG_E_ALPHA, DG_E_DOOR),
            ('w', 'mine', 'Mine abandonnée', 'raptor', DG_W_ALPHA, DG_W_DOOR),
            ('s', 'tube', 'Tube de lave', 'carno', DG_S_ALPHA, DG_S_DOOR)]

# ================================================================ végétation (place feature) et décor naturel
R_VEG = {k: [] for k in REGIONS}
_used = {k: [] for k in REGIONS}


def free(k, x, z, keep=()):
    if (x, z) not in COL or not in_rect(x, z, REGIONS[k]['rect']):
        return False
    x0, z0, x1, z1 = REGIONS[k]['rect']
    if min(x - x0, x1 - 1 - x, z - z0, z1 - 1 - z) < 8:
        return False
    if (x, z) in ROADS[k] or any((x + a, z + b) in ROADS[k] for a in (-2, 0, 2) for b in (-2, 0, 2)):
        return False
    return all(_m.hypot(x - a, z - b) >= r for (a, b, r) in keep)


def veg(k, feature, n, min_d, ok, keep=(), fluid=None, at=None):
    pts, tries = [], 0
    x0, z0, x1, z1 = REGIONS[k]['rect']
    while len(pts) < n and tries < n * 60:
        tries += 1
        x, z = rw.randrange(x0, x1), rw.randrange(z0, z1)
        if not free(k, x, z, keep) or not ok(x, z):
            continue
        if fluid is not None and COL[(x, z)][3] != fluid:
            continue
        if any(abs(x - a) < min_d and abs(z - b) < min_d and _m.hypot(x - a, z - b) < min_d for a, b in pts + _used[k]):
            continue
        pts.append((x, z))
        y = (at(x, z) if at else ground(x, z))
        R_VEG[k].append(f'place feature minecraft:{feature} {x} {y} {z}')
    if min_d >= 3:
        _used[k].extend(pts)
    return pts


DRY = lambda k: (lambda x, z: COL[(x, z)][3] is None)
N_KEEP = [(MOTHER[0], MOTHER[1], 16), (ECHO[0], ECHO[1], 10), (STATION[0], STATION[1], 22), (LAG[0], LAG[1], 35), (MOTHER[0], MOTHER[1], 12), (JETTY[0], JETTY[1], 9)]
veg('n', 'tall_mangrove', 16, 9, lambda x, z: COL[(x, z)][1] in ('mud', 'grass_block', 'moss_block'), N_KEEP)
veg('n', 'mangrove', 45, 6, lambda x, z: COL[(x, z)][1] in ('mud', 'grass_block', 'moss_block'), N_KEEP)
veg('n', 'swamp_oak', 60, 6, DRY('n'), N_KEEP)
veg('n', 'huge_brown_mushroom', 6, 10, DRY('n'), N_KEEP)
veg('n', 'huge_red_mushroom', 6, 10, DRY('n'), N_KEEP)
veg('n', 'moss_patch', 30, 4, DRY('n'), N_KEEP, at=lambda x, z: ground(x, z) - 1)
veg('n', 'firefly_bush', 50, 2, DRY('n'), N_KEEP)
veg('n', 'large_fern', 120, 2, DRY('n'), N_KEEP)
veg('n', 'grass', 200, 1, DRY('n'), N_KEEP)
veg('n', 'sugar_cane', 30, 3, lambda x, z: COL[(x, z)][3] is None and any(COL.get((x + a, z + b), (0, 0, 0, None))[3] == 'water' for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))), N_KEEP)
veg('n', 'waterlily', 160, 2, lambda x, z: True, [(STATION[0], STATION[1], 12)], fluid='water', at=lambda x, z: 63)
veg('n', 'seagrass_short', 60, 2, lambda x, z: True, (), fluid='water', at=lambda x, z: COL[(x, z)][0] + 1)
E_KEEP = [(NEST[0], NEST[1], 12), (DELTA[0], DELTA[1], 12), (LAKE[0], LAKE[1], 21), (BONES[0] + 4, BONES[1], 22)] + [(a, b, 7) for a, b in SPIRES]
veg('e', 'acacia', 70, 9, DRY('e'), E_KEEP)
veg('e', 'oak', 10, 14, DRY('e'), E_KEEP)
veg('e', 'fallen_oak_tree', 8, 12, DRY('e'), E_KEEP)
veg('e', 'forest_rock', 28, 10, DRY('e'), E_KEEP)
veg('e', 'pile_hay', 5, 20, DRY('e'), E_KEEP)
veg('e', 'bush', 90, 3, DRY('e'), E_KEEP)
veg('e', 'dead_bush', 40, 3, DRY('e'), E_KEEP)
veg('e', 'dry_grass', 220, 1, DRY('e'), E_KEEP)
veg('e', 'tall_grass', 240, 1, DRY('e'), E_KEEP)
veg('e', 'wildflower', 60, 2, DRY('e'), E_KEEP)
veg('e', 'sugar_cane', 20, 3, lambda x, z: 15 <= _m.hypot(x - LAKE[0], z - LAKE[1]) < 18, ())
W_KEEP = [(MINE[0] + 22, MINE[1], 8), (FORT[0], FORT[1], 30), (ARCH[0], ARCH[1], 12), (LOOKOUT[0], LOOKOUT[1], 12)]
veg('w', 'dead_bush', 160, 2, lambda x, z: COL[(x, z)][1] == 'red_sand', W_KEEP)
veg('w', 'cactus', 50, 4, lambda x, z: COL[(x, z)][1] == 'red_sand' and COL[(x, z)][0] < 70, W_KEEP)
veg('w', 'dry_grass', 120, 1, lambda x, z: COL[(x, z)][0] > 72, W_KEEP)
veg('w', 'trees_badlands', 18, 12, lambda x, z: COL[(x, z)][0] > 80, W_KEEP)
S_KEEP = [(-46, VOLC[1], 8), (REFUGE[0], REFUGE[1], 10), (VOLC[0], VOLC[1], 22), (BRIDGE[0], BRIDGE[1], 10)]
veg('s', 'large_basalt_columns', 10, 18, lambda x, z: COL[(x, z)][0] < 72 and COL[(x, z)][3] is None, S_KEEP)
veg('s', 'small_basalt_columns', 30, 8, lambda x, z: COL[(x, z)][3] is None, S_KEEP)
veg('s', 'sulfur_spike', 60, 5, lambda x, z: COL[(x, z)][3] is None and COL[(x, z)][0] > 70, S_KEEP)
veg('s', 'dead_bush', 60, 3, lambda x, z: COL[(x, z)][1] == 'coarse_dirt', S_KEEP)
veg('s', 'fallen_spruce_tree', 6, 15, lambda x, z: COL[(x, z)][1] == 'coarse_dirt', S_KEEP)
veg('s', 'patch_fire', 20, 8, lambda x, z: COL[(x, z)][1] == 'basalt' and COL[(x, z)][3] is None, S_KEEP, at=lambda x, z: ground(x, z))
# fumerolles de magma / sulfure sur les pentes
for i in range(90):
    x, z = rw.randrange(RS[0] + 10, RS[2] - 10), rw.randrange(RS[1] + 10, RS[3] - 10)
    if free('s', x, z, S_KEEP) and COL[(x, z)][3] is None and COL[(x, z)][0] > 68:
        y = COL[(x, z)][0]
        R_VEG['s'].append(f'fill {x - 1} {y} {z - 1} {x + 1} {y} {z + 1} minecraft:{rw.choice(["magma_block", "sulfur", "potent_sulfur", "magma_block"])} replace #mg:tv_ground')


# ================================================================ apparitions, lieux, balises de voyage
def pick(k, n, min_d, ok, keep=()):
    pts, tries = [], 0
    x0, z0, x1, z1 = REGIONS[k]['rect']
    while len(pts) < n and tries < 20000:
        tries += 1
        x, z = rw.randrange(x0 + 10, x1 - 10), rw.randrange(z0 + 10, z1 - 10)
        if (x, z) not in COL or not ok(x, z) or not all(_m.hypot(x - a, z - b) >= r for (a, b, r) in keep):
            continue
        if all(_m.hypot(x - a, z - b) >= min_d for a, b in pts):
            pts.append((x, z))
    return pts


# (région, espèce, nombre de points, écart) : marqueurs mg.tvs<espèce> de la région
SPAWN_PLAN = {
    'n': [('dilo', 14, 18), ('compy', 12, 18), ('raptor', 5, 30), ('pachy', 0, 0)],
    'e': [('trike', 8, 26), ('stego', 7, 26), ('ankylo', 5, 30), ('galli', 10, 22), ('brachio', 3, 40), ('ptera', 0, 0), ('raptor', 4, 30)],
    'w': [('raptor', 10, 22), ('ptera', 8, 24), ('dilo', 4, 30), ('sixer', 0, 0)],
    's': [('carno', 6, 30), ('ankylo', 6, 26), ('raptor', 6, 26), ('compy', 6, 22)],
}
MARKERS = []          # (x, y, z, tags)
KEEP_SP = {'n': [(ECHO[0], ECHO[1], 24), (LAG[0], LAG[1], 36)], 'e': [(DELTA[0], DELTA[1], 26)], 'w': [(LOOKOUT[0], LOOKOUT[1], 20), (FORT[0], FORT[1], 30)],
           's': [(REFUGE[0], REFUGE[1], 24), (VOLC[0], VOLC[1], 22)]}
for k, plan in SPAWN_PLAN.items():
    for sp, n, d in plan:
        if n == 0:
            continue
        ok = (lambda x, z: COL[(x, z)][3] is None and COL[(x, z)][1] not in ('stone', 'blackstone'))
        for (x, z) in pick(k, n, d, ok, KEEP_SP[k]):
            MARKERS.append((x + 0.5, ground(x, z), z + 0.5, f'"mg.tv","mg.trsp","mg.trsp_{k}","mg.trsp_{sp}"'))
for (x, y, z) in NESTS:                                                     # ptéranodons des Aiguilles
    MARKERS.append((x + 0.5, y + 3, z + 0.5, '"mg.tv","mg.trsp","mg.trsp_e","mg.trsp_ptera"'))
for i in range(10):                                                         # renégats autour et dans le fort
    a = _m.radians(i * 36)
    r = 8 if i % 2 else 15
    x, z = round(FORT[0] + r * _m.cos(a)), round(FORT[1] + r * _m.sin(a))
    MARKERS.append((x + 0.5, 65, z + 0.5, '"mg.tv","mg.trsp","mg.trsp_w","mg.trsp_sixer"'))

# lieux à découvrir : (clé, nom, région, x, y, z, rayon, xp)
POIS = [
    ('colonie', 'Colonie Terra Nova', 'v', 0, 65, 0, 20, 0),
    ('cascade', 'Gué de la rivière', 'v', -25, 64, -56, 8, 40),
    ('echo', 'Poste Écho', 'n', ECHO[0], 65, ECHO[1], 8, 60),
    ('station', 'Station engloutie', 'n', STATION[0], 64, STATION[1], 12, 80),
    ('lagune', 'Lagune de l\'Antre', 'n', LAG[0], 65, LAG[1], 26, 80),
    ('mere', 'Arbre-Mère', 'n', MOTHER[0], ground(*MOTHER), MOTHER[1], 10, 80),
    ('ponton', 'Ponton des pêcheurs', 'n', JETTY[0], 64, JETTY[1], 8, 50),
    ('delta', 'Camp Delta', 'e', DELTA[0], ground(*DELTA), DELTA[1], 8, 60),
    ('eau', 'Point d\'eau', 'e', LAKE[0], 63, LAKE[1], 18, 60),
    ('aiguilles', 'Les Aiguilles', 'e', SPIRES[0][0], ground(*SPIRES[0]), SPIRES[0][1], 18, 80),
    ('geants', 'Cimetière des géants', 'e', BONES[0], ground(*BONES), BONES[1], 14, 80),
    ('fort', 'Fort des Renégats', 'w', FORT[0], 65, FORT[1], 26, 100),
    ('arche', 'Arche rouge', 'w', ARCH[0], 65, ARCH[1], 10, 60),
    ('belvedere', 'Belvédère', 'w', LOOKOUT[0], 81, LOOKOUT[1], 9, 80),
    ('refuge', 'Refuge du Cendre', 's', REFUGE[0], ground(*REFUGE), REFUGE[1], 8, 60),
    ('pont', 'Pont d\'obsidienne', 's', BRIDGE[0], BR_Y + 1, BRIDGE[1], 9, 80),
    ('caldeira', 'Caldeira du Roi', 's', VOLC[0], CALD_Y + 1, VOLC[1], 15, 120),
    ('dg_arbre', 'Cœur de l\'Arbre-Mère', 'n', DG_N_DOOR[0], DG_N_DOOR[1], DG_N_DOOR[2], 6, 80),
    ('dg_pic', 'Pic du Nid', 'e', DG_E_DOOR[0], DG_E_DOOR[1], DG_E_DOOR[2], 6, 80),
    ('dg_mine', 'Mine abandonnée', 'w', DG_W_DOOR[0], DG_W_DOOR[1], DG_W_DOOR[2], 6, 80),
    ('dg_tube', 'Tube de lave', 's', DG_S_DOOR[0], DG_S_DOOR[1], DG_S_DOOR[2], 6, 80),
]
# balises de voyage : (n°, clé, nom, x, y, z) — y = pied du joueur
CAMPS = [(1, 'colonie', 'Colonie', 0.5, 65, 4.5), (2, 'echo', 'Poste Écho', ECHO[0] + 2.5, 65, ECHO[1] + 0.5),
         (3, 'delta', 'Camp Delta', DELTA[0] + 2.5, ground(*DELTA), DELTA[1] + 0.5),
         (4, 'belvedere', 'Belvédère', LOOKOUT[0] + 2.5, 81, LOOKOUT[1] + 0.5),
         (5, 'refuge', 'Refuge du Cendre', REFUGE[0] + 2.5, ground(*REFUGE), REFUGE[1] + 0.5)]


# ================================================================ vallée : cols, chemins vers les cols, pont sur la rivière
V_PATHS = {'n': [(0, -30), (-10, -42), (-22, -58), (-30, -80), (-30, -96)], 'e': [(0, 30), (30, 34), (64, 32), (96, 30)],
           's': [(0, 30), (-10, 52), (-24, 80), (-24, 96)], 'w': [(-65, 8), (-96, 6)]}
V_ROAD = set()
for k, pts in V_PATHS.items():
    V_ROAD |= cells_near(polyline(pts), 1)
V_PATCH = []                                       # commandes « vallée » (ajoutées à la construction des régions)
for (x, z) in sorted(V_ROAD):
    if (x, z) in H and max(abs(x), abs(z)) > WALL:
        h = H[(x, z)]
        if h <= 62:                                    # pont / gué sur la rivière
            V_PATCH.append(f'setblock {x} 63 {z} minecraft:spruce_planks')
        else:
            V_PATCH.append(f'setblock {x} {h} {z} minecraft:dirt_path')
            V_PATCH.append(f'fill {x} {h + 1} {z} {x} {h + 3} {z} minecraft:air replace #mg:tv_pass')
for k, (gx, gz) in PASS_GATE.items():               # portique du col (côté vallée), barrière posée par la session
    gy = H[(gx, gz)] if (gx, gz) in H else PASS_Y
    ax, c = PASSES[k]
    if ax == 'z':
        V_PATCH += [f'fill {gx - 4} {gy + 1} {gz} {gx - 4} {gy + 7} {gz} minecraft:stripped_spruce_log',
                    f'fill {gx + 4} {gy + 1} {gz} {gx + 4} {gy + 7} {gz} minecraft:stripped_spruce_log',
                    f'fill {gx - 4} {gy + 8} {gz} {gx + 4} {gy + 8} {gz} minecraft:dark_oak_log[axis=x]',
                    f'setblock {gx - 4} {gy + 9} {gz} minecraft:lantern', f'setblock {gx + 4} {gy + 9} {gz} minecraft:lantern']
    else:
        V_PATCH += [f'fill {gx} {gy + 1} {gz - 4} {gx} {gy + 7} {gz - 4} minecraft:stripped_spruce_log',
                    f'fill {gx} {gy + 1} {gz + 4} {gx} {gy + 7} {gz + 4} minecraft:stripped_spruce_log',
                    f'fill {gx} {gy + 8} {gz - 4} {gx} {gy + 8} {gz + 4} minecraft:dark_oak_log[axis=z]',
                    f'setblock {gx} {gy + 9} {gz - 4} minecraft:lantern', f'setblock {gx} {gy + 9} {gz + 4} minecraft:lantern']


# ================================================================ biomes (couleurs, brume, particules, musique)
def biome(name, sky, fog, water, wfog, grass=None, foliage=None, particles=None, music=None, fog_end=None, amb=None):
    attrs_ = {'minecraft:visual/sky_color': sky, 'minecraft:visual/fog_color': fog, 'minecraft:visual/water_fog_color': wfog,
              'minecraft:gameplay/monsters_burn': False}
    if particles:
        attrs_['minecraft:visual/ambient_particles'] = particles
    if music:
        attrs_['minecraft:audio/background_music'] = {'default': {'max_delay': 12000, 'min_delay': 3000, 'sound': music}}
    if fog_end:
        attrs_['minecraft:visual/fog_start_distance'] = 0
        attrs_['minecraft:visual/fog_end_distance'] = fog_end
    if amb:
        attrs_['minecraft:audio/ambient_sounds'] = amb
    eff = {'water_color': water}
    if grass:
        eff['grass_color'] = grass
    if foliage:
        eff['foliage_color'] = foliage
    d = {'attributes': attrs_, 'carvers': [], 'downfall': 0.8, 'effects': eff, 'features': [], 'has_precipitation': False,
         'spawn_costs': {}, 'spawners': {k: [] for k in ('ambient', 'axolotls', 'creature', 'misc', 'monster', 'underground_water_creature',
                                                          'water_ambient', 'water_creature')}, 'temperature': 0.9}
    p = os.path.join(C.D, 'worldgen', 'biome', name.split(':')[1] + '.json')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(d, f, separators=(',', ':'), sort_keys=True)
        f.write('\n')


biome(VALLEY_BIOME, '#77a8ff', '#c0d8ff', '#3f8fb4', '#24576e', grass='#59c93c', foliage='#30bb0b', music='minecraft:music.overworld.jungle',
      particles=[{'particle': {'type': 'minecraft:spore_blossom_air'}, 'probability': 0.002}])
biome('mg:tv_marais', '#6f8f86', '#93a89a', '#4d6b5a', '#2b3d33', grass='#6a7039', foliage='#6a7039', music='minecraft:music.overworld.swamp',
      particles=[{'particle': {'type': 'minecraft:mycelium'}, 'probability': 0.02}], fog_end=72)
biome('mg:tv_plaines', '#7fb3ff', '#e8d9b0', '#3f8fb4', '#2a5f7a', grass='#bfb755', foliage='#aea42a', music='minecraft:music.overworld.badlands')
biome('mg:tv_canyon', '#8fb0e0', '#e0b090', '#4a7fa8', '#30506a', grass='#90814d', foliage='#9e814d', music='minecraft:music.overworld.desert',
      particles=[{'particle': {'type': 'minecraft:white_ash'}, 'probability': 0.004}])
biome('mg:tv_volcan', '#3a2a2a', '#5a3a30', '#3f76e4', '#30140a', music='minecraft:music.nether.basalt_deltas',
      particles=[{'particle': {'type': 'minecraft:white_ash'}, 'probability': 0.09}, {'particle': {'type': 'minecraft:lava'}, 'probability': 0.0004}],
      fog_end=96, amb={'loop': 'minecraft:ambient.basalt_deltas.loop',
                       'additions': {'sound': 'minecraft:ambient.basalt_deltas.additions', 'tick_chance': 0.0111}})


def biome_fill(rect, b):
    x0, z0, x1, z1 = rect
    out = []
    for x in range(x0, x1, 16):
        for z in range(z0, z1, 16):
            out.append(f'fillbiome {x} 48 {z} {min(x + 15, x1 - 1)} 175 {min(z + 15, z1 - 1)} {b}')
    return out


R_BIOME = {k: biome_fill(v['rect'], v['biome']) for k, v in REGIONS.items()}
V_BIOME = biome_fill((-96, -96, 96, 96), VALLEY_BIOME)


# ================================================================ bords de la carte (barrières), ouvertures des cols
def walls():
    L = ['# Bords de la carte en croix (barrières invisibles), ouvertures des cols']
    seg = []
    # vallée : 4 côtés intérieurs avec ouverture
    for k, (ax, c) in PASSES.items():
        if k == 'n':
            seg += [('z', -97, -96, c - 4), ('z', -97, c + 4, 95)]
        if k == 's':
            seg += [('z', 96, -96, c - 4), ('z', 96, c + 4, 95)]
        if k == 'e':
            seg += [('x', 96, -96, c - 4), ('x', 96, c + 4, 95)]
        if k == 'w':
            seg += [('x', -97, -96, c - 4), ('x', -97, c + 4, 95)]
    # extérieur des régions
    seg += [('z', -257, -96, 95), ('x', -97, -256, -97), ('x', 96, -256, -97),          # nord
            ('z', 256, -96, 95), ('x', -97, 96, 255), ('x', 96, 96, 255),               # sud
            ('x', 256, -96, 95), ('z', -97, 96, 255), ('z', 96, 96, 255),               # est
            ('x', -257, -96, 95), ('z', -97, -256, -97), ('z', 96, -256, -97)]          # ouest
    for ax, v, a, b in seg:
        if ax == 'z':
            L.append(f'fill {a} 50 {v} {b} 160 {v} minecraft:barrier')
        else:
            L.append(f'fill {v} 50 {a} {v} 160 {b} minecraft:barrier')
    return L


w('terra/walls', walls())
w('terra/walls_old', ['# Ancien bord de la vallée (avant les régions) : retiré, remplacé par mg:terra/walls',
                      f'fill {-HX - 1} 50 {-HX - 1} {-HX - 1} 150 {HX} minecraft:air replace minecraft:barrier',
                      f'fill {HX} 50 {-HX - 1} {HX} 150 {HX} minecraft:air replace minecraft:barrier',
                      f'fill {-HX} 50 {-HX - 1} {HX - 1} 150 {-HX - 1} minecraft:air replace minecraft:barrier',
                      f'fill {-HX} 50 {HX} {HX - 1} 150 {HX} minecraft:air replace minecraft:barrier'])
with open(os.path.join(C.D, 'tags', 'block', 'tv_ground.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'values': ['minecraft:basalt', 'minecraft:blackstone', 'minecraft:tuff', 'minecraft:coarse_dirt', 'minecraft:gray_concrete_powder']}, f, indent=2)
    f.write('\n')
FL_REGIONS = {'n': '-96 -256 95 -97', 'e': '96 -96 255 95', 'w': '-256 -96 -97 95', 's': '-96 96 95 255'}
# ================================================================ colonie : labo du Dr Ossei (est), forge de Jo (ouest), balise de voyage
VSTRUCT = []


def V(c):
    VSTRUCT.append(c)


Gc = G
VSTRUCT.extend(TS.lab(Gc).cmds())                                                            # labo du Dr Ossei
VSTRUCT.extend(TS.forge(Gc).cmds())                                                          # forge de Jo
V(f'setblock -5 {Gc} 12 minecraft:lodestone')                                                 # balise de la colonie
V(f'setblock -5 {Gc + 1} 12 minecraft:lightning_rod')
LAB_NPC = (15.5, Gc + 1, -7.5)
FORGE_NPC = (-11.5, Gc + 1, 7.5)
COLONY_BEACON = (-5, Gc, 12)
# œufs d'ambre (quête du Dr Ossei) : 2 dans la vallée, 1 par région
EGGS = [(-58, H[(-58, -24)] + 1, -24), (66, H[(66, 58)] + 1, 58), (MOTHER[0] - 2, mg_ + 13, MOTHER[1] - 1),
        (BONES[0] + 26, ground(*BONES) + 3, BONES[1] + 5), (ARCH[0], 65, ARCH[1]), (BRIDGE[0] + 10, ground(BRIDGE[0] + 10, BRIDGE[1] - 8), BRIDGE[1] - 8)]

# ================================================================ trésors cachés (3 par zone) : position du coffre (sol), décor posé à la session
CACHES = []
_v_ok = lambda x, z: (x, z) in H and max(abs(x), abs(z)) > 34 and edge(x, z) > 12 and H[(x, z)] > 62
for i in range(400):
    if len([c for c in CACHES if c[0] == 'v']) >= 3:
        break
    x, z = rw.randrange(-90, 90), rw.randrange(-90, 90)
    if _v_ok(x, z) and all(_m.hypot(x - a, z - b) > 40 for k_, a, y_, b in CACHES):
        CACHES.append(('v', x, H[(x, z)] + 1, z))
for k in ('n', 'e', 'w', 's'):
    ok = (lambda x, z: COL[(x, z)][3] is None and COL[(x, z)][1] not in ('stone', 'blackstone', 'dirt_path'))
    for (x, z) in pick(k, 3, 50, ok, KEEP_SP[k]):
        CACHES.append((k, x, ground(x, z), z))
