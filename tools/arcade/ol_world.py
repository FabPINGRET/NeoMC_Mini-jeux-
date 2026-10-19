"""🌙 Ombrelune : relief, régions, biomes, végétation (module importé par gen_ombrelune.py).

Carte 480 × 480 (x, z de -240 à 239) en 9 cases de 160 :
    nw Forêt de Sylvanor   | n Pics de Givrecroc      | ne Marais de Fangebrume
    w  Plaines de Valdor   | hub Havreclair (cité)    | e  Sables d'Azhar
    sw Terres d'Ombre      | s Khazgarde (montagnes)  | se Pyrecendre (volcan)
Entre deux cases voisines : une crête, percée d'un col là où la campagne fait passer (anneau w → nw → n → ne → e → se → s → sw,
plus les quatre portes de la cité). Bord de la carte : hautes montagnes et barrières.
"""
import functools
import math
import random

CELL = 160
HALF = 240                      # x, z de -HALF à HALF - 1
G = 64                          # sol de la cité (on marche à y 65)
BASE_Y = 40                     # bas du terrain plein (donjons enterrés au-dessus)
WATER = 62

REGIONS = {  # clé : (case i, j), nom, couleur, niveaux conseillés, biome
    'hub': ((0, 0), 'Havreclair', 'gold', (1, 35), 'mg:ol_hub'),
    'w': ((-1, 0), 'Plaines de Valdor', 'green', (1, 4), 'mg:ol_valdor'),
    'nw': ((-1, -1), 'Forêt de Sylvanor', 'dark_green', (4, 8), 'mg:ol_sylvanor'),
    'n': ((0, -1), 'Pics de Givrecroc', 'aqua', (8, 12), 'mg:ol_givrecroc'),
    'ne': ((1, -1), 'Marais de Fangebrume', 'dark_aqua', (12, 16), 'mg:ol_fangebrume'),
    'e': ((1, 0), 'Sables d\'Azhar', 'yellow', (16, 20), 'mg:ol_azhar'),
    'se': ((1, 1), 'Pyrecendre', 'red', (20, 24), 'mg:ol_pyrecendre'),
    's': ((0, 1), 'Khazgarde', 'gray', (24, 28), 'mg:ol_khazgarde'),
    'sw': ((-1, 1), 'Terres d\'Ombre', 'dark_purple', (28, 32), 'mg:ol_ombre'),
}
ORDER = ['w', 'nw', 'n', 'ne', 'e', 'se', 's', 'sw']
KEY_OF = {v[0]: k for k, v in REGIONS.items()}


def rect(k):
    i, j = REGIONS[k][0]
    return (i * CELL - CELL // 2, j * CELL - CELL // 2, i * CELL + CELL // 2, j * CELL + CELL // 2)   # x0 z0 x1 z1 (x1, z1 exclus)


def region_at(x, z):
    i = math.floor((x + CELL // 2) / CELL)
    j = math.floor((z + CELL // 2) / CELL)
    return KEY_OF.get((i, j))


# cols : (région a, région b) -> coordonnée du couloir le long de la frontière
PASSES = {('hub', 'w'): 0, ('hub', 'n'): 0, ('hub', 'e'): 0, ('hub', 's'): 0,
          ('w', 'nw'): -168, ('nw', 'n'): -168, ('n', 'ne'): -150, ('ne', 'e'): 168,
          ('e', 'se'): 150, ('se', 's'): 168, ('s', 'sw'): 168}
PASS_H = {('hub', 'w'): 65, ('hub', 'n'): 66, ('hub', 'e'): 65, ('hub', 's'): 65, ('w', 'nw'): 67, ('nw', 'n'): 70,
          ('n', 'ne'): 66, ('ne', 'e'): 64, ('e', 'se'): 66, ('se', 's'): 68, ('s', 'sw'): 66}


def pass_line(a, b):
    """Frontière entre a et b : ('x', valeur) = frontière verticale x = valeur ; couloir à la coordonnée PASSES."""
    (ia, ja), (ib, jb) = REGIONS[a][0], REGIONS[b][0]
    if ia != ib:
        return 'x', max(ia, ib) * CELL - CELL // 2
    return 'z', max(ja, jb) * CELL - CELL // 2


PASS_AT = {}                      # (a, b) -> (x, z) du milieu du col
for (a, b), c in PASSES.items():
    ax, v = pass_line(a, b)
    PASS_AT[(a, b)] = (v, c) if ax == 'x' else (c, v)


# ---------------------------------------------------------------- bruit
@functools.lru_cache(maxsize=None)
def _h(seed, i, j):
    return random.Random(seed * 1000003 + i * 7919 + j * 104729).uniform(-1, 1)


def noise(seed, cell, x, z):
    fx, fz = x / cell, z / cell
    i, j = math.floor(fx), math.floor(fz)
    tx, tz = fx - i, fz - j
    sx, sz = tx * tx * (3 - 2 * tx), tz * tz * (3 - 2 * tz)
    a, b, c, d = _h(seed, i, j), _h(seed, i + 1, j), _h(seed, i, j + 1), _h(seed, i + 1, j + 1)
    return (a + (b - a) * sx) * (1 - sz) + (c + (d - c) * sx) * sz


def fbm(seed, cell, x, z, oct=3):
    v, a, c, t = 0.0, 1.0, cell, 0.0
    for o in range(oct):
        v += a * noise(seed + o * 17, c, x, z)
        t += a
        a *= 0.5
        c /= 2.1
    return v / t


def ridged(seed, cell, x, z):
    return 1 - abs(fbm(seed, cell, x, z, 3))


def lerp(a, b, t):
    return a + (b - a) * t


def smooth(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


# ---------------------------------------------------------------- lieux principaux (centre x, z)
P = {
    # Havreclair
    'city': (0, 0),
    # Valdor
    'brumecombe': (-150, 22), 'bandit_fort': (-205, -42), 'crypt': (-118, -48), 'mill': (-128, 52), 'lake_w': (-182, 40),
    # Sylvanor
    'aelindor': (-160, -165), 'spider_nest': (-212, -108), 'shrine_nw': (-110, -210), 'spider_lair': (-205, -205),
    # Givrecroc
    'hrafnheim': (0, -120), 'giant_hold': (30, -205), 'ice_cave': (-50, -190), 'ice_lake': (-42, -128),
    # Fangebrume
    'stilts': (150, -118), 'witch_isle': (205, -195), 'sunken': (118, -200),
    # Azhar
    'oasis': (128, 4), 'pyramid': (198, -28), 'tombs': (196, 48), 'obelisks': (160, 50),
    # Pyrecendre
    'bastion': (140, 110), 'volcano': (180, 180), 'forge_r': (222, 108),
    # Khazgarde
    'dwarf_camp': (0, 112), 'kgate': (0, 140), 'khall': (0, 175), 'mines': (-48, 205),
    # Ombre
    'rebels': (-108, 150), 'citadel': (-172, 178), 'soul_well': (-210, 108),
}

# plateformes aplanies : (x0, z0, x1, z1, hauteur, marge de raccord)
FLAT = [
    (-67, -67, 67, 67, G, 5),                                      # cité + douves
    (-170, 2, -128, 44, 66, 10),                                   # Brumecombe
    (-224, -62, -186, -22, 70, 8),                                 # fort des brigands
    (-130, -60, -106, -36, 66, 6),                                 # chapelle et crypte
    (-138, 44, -120, 60, 66, 5),                                   # moulin
    (-182, -186, -138, -144, 68, 10),                              # Aelindor
    (-222, -118, -202, -98, 70, 6),                                # nid d'araignées (entrée)
    (-120, -220, -100, -200, 69, 5),                               # sanctuaire
    (-224, -218, -186, -192, 72, 6),                               # antre de la reine-araignée
    (-22, -138, 22, -102, 74, 10),                                 # Hrafnheim
    (8, -226, 52, -184, 104, 10),                                  # fort du géant
    (-62, -200, -40, -180, 86, 6),                                 # grotte de glace (entrée)
    (128, -138, 172, -98, 63, 8),                                  # village sur pilotis
    (108, -212, 128, -188, 63, 5),                                 # temple englouti
    (110, -16, 146, 22, 64, 8),                                    # oasis
    (172, -54, 224, -2, 64, 8),                                    # pyramide
    (184, 36, 208, 60, 64, 6),                                     # tombeaux
    (124, 94, 156, 126, 66, 8),                                    # bastion des braises
    (210, 96, 234, 120, 70, 6),                                    # forge écarlate
    (-20, 96, 20, 126, 66, 8),                                     # camp nain
    (-124, 134, -92, 166, 64, 8),                                  # camp des rebelles
    (-210, 140, -134, 216, 66, 10),                                # citadelle
    (-222, 96, -198, 120, 64, 6),                                  # puits des âmes
]


def flat_at(x, z):
    """(hauteur visée, poids 0..1) de la plateforme la plus proche."""
    best = None
    for (x0, z0, x1, z1, h, m) in FLAT:
        dx = max(x0 - x, 0, x - x1)
        dz = max(z0 - z, 0, z - z1)
        d = math.hypot(dx, dz)
        if d <= m:
            wgt = 1.0 if d == 0 else smooth(1 - d / m)
            if best is None or wgt > best[1]:
                best = (h, wgt)
    return best


# ---------------------------------------------------------------- relief propre à chaque région
def h_hub(x, z):
    return 64.5 + 2.2 * fbm(101, 36, x, z) + 0.8 * noise(102, 7, x, z)


def h_w(x, z):
    h = 66 + 5.5 * fbm(201, 44, x, z) + 1.6 * noise(202, 11, x, z)
    lx, lz = P['lake_w']
    d = math.hypot(x - lx, (z - lz) * 1.3)
    if d < 22:
        h = lerp(h, 57, smooth(1 - d / 22) * 1.4)
    return h


def h_nw(x, z):
    return 68 + 7 * fbm(301, 34, x, z) + 2.2 * noise(302, 9, x, z)


def h_n(x, z):
    r = ridged(401, 60, x, z)
    h = 70 + 40 * r ** 2.2 + 6 * fbm(402, 18, x, z)
    lx, lz = P['ice_lake']
    d = math.hypot(x - lx, z - lz)
    if d < 26:
        h = lerp(h, 58, smooth(1 - d / 26) * 1.3)
    return h


def h_ne(x, z):
    h = 61.8 + 2.4 * fbm(501, 22, x, z) + 1.3 * noise(502, 6, x, z)
    wx, wz = P['witch_isle']
    d = math.hypot(x - wx, z - wz)
    if d < 34:
        h = lerp(h, 56, smooth((34 - d) / 14))
    if d < 11:
        h = lerp(h, 64, smooth((11 - d) / 4))
    return h


def h_e(x, z):
    dune = abs(math.sin((x * 0.06 + z * 0.035) + 3 * fbm(601, 50, x, z)))
    h = 64 + 6 * dune * (0.6 + 0.4 * fbm(602, 40, x, z)) + 1.5 * fbm(603, 16, x, z)
    ox, oz = P['oasis']
    d = math.hypot(x - ox - 14, z - oz + 2)
    if d < 11:
        h = lerp(h, 58, smooth(1 - d / 11) * 1.5)
    return h


VX, VZ = P['volcano']
CALD_Y = 116                       # sol de la caldeira (arène d'Ignarok)


def h_se(x, z):
    r = math.hypot(x - VX, z - VZ)
    cone = 66 + 58 * max(0.0, 1 - r / 74) ** 1.25
    h = cone + 3 * fbm(701, 20, x, z) + 1.5 * noise(702, 6, x, z)
    if r < 16:
        h = CALD_Y
    elif r < 21:
        h = max(h, CALD_Y + 4 + (21 - r) * 0.4)
    return h


KZ = P['kgate'][1]                 # face de la montagne (porte naine)


def h_s(x, z):
    m = 66 + 3 * fbm(801, 30, x, z)
    if z > KZ - 6:
        t = smooth((z - (KZ - 6)) / 10)
        m = lerp(m, 112 + 14 * ridged(802, 50, x, z) + 4 * fbm(803, 14, x, z), t)
    return m


def h_sw(x, z):
    h = 64 + 4 * fbm(901, 30, x, z) + 1.5 * noise(902, 8, x, z)
    sp = ridged(903, 22, x, z)
    if sp > 0.86:
        h += (sp - 0.86) * 90
    return h


HF = {'hub': h_hub, 'w': h_w, 'nw': h_nw, 'n': h_n, 'ne': h_ne, 'e': h_e, 'se': h_se, 's': h_s, 'sw': h_sw}


# ---------------------------------------------------------------- crêtes entre les cases, cols
def border_info(x, z):
    """Distance à la frontière intérieure la plus proche, clé du col de cette frontière (ou None), écart au couloir."""
    k = region_at(x, z)
    x0, z0, x1, z1 = rect(k)
    best = (99, None, 99, False)
    for side, d, nb in (('w', x - x0, (x0 - 1, z)), ('e', x1 - 1 - x, (x1, z)), ('n', z - z0, (x, z0 - 1)), ('s', z1 - 1 - z, (x, z1))):
        other = region_at(*nb)
        outer = other is None
        key = None
        if other:
            key = (k, other) if (k, other) in PASSES else ((other, k) if (other, k) in PASSES else None)
        dc = 99
        if key:
            c = PASSES[key]
            dc = abs(z - c) if side in ('w', 'e') else abs(x - c)
        if d < best[0]:
            best = (d, key, dc, outer)
    return best


RIDGE_D = 14


def ridge_h(x, z):
    return 94 + 8 * fbm(1001, 26, x, z)


def height(x, z):
    k = region_at(x, z)
    h = HF[k](x, z)
    fl = flat_at(x, z)
    if fl:
        h = lerp(h, fl[0], fl[1])
    d, key, dc, outer = border_info(x, z)
    if d < RIDGE_D + 6 and key and dc <= 9:
        ph = PASS_H[key]
        h = lerp(h, ph, smooth(1 - d / (RIDGE_D + 6)) * (1.0 if dc <= 5 else smooth((9 - dc) / 4)))
    if d < RIDGE_D:
        t = ((RIDGE_D - d) / RIDGE_D) ** 1.6
        f = 1.0
        if key and dc <= 9:
            f = 0.0 if dc <= 5 else smooth((dc - 5) / 4)
        top = ridge_h(x, z) + (22 if outer else 0)
        h = lerp(h, max(h, top), t * f)
    return max(48, min(150, round(h)))


# ---------------------------------------------------------------- matières de surface
def column(x, z, h):
    """(dessus, dessous, fluide, niveau du fluide) d'une colonne."""
    k = region_at(x, z)
    d, key, dc, outer = border_info(x, z)
    steep = d < RIDGE_D and h > 78
    n1 = noise(1101, 5, x, z)
    if k == 'hub':
        top, und = ('grass_block', 'dirt')
        if h <= WATER:
            top = 'gravel'
    elif k == 'w':
        top, und = 'grass_block', 'dirt'
        if h <= WATER:
            top = 'sand' if n1 > 0 else 'clay'
    elif k == 'nw':
        top = 'podzol' if n1 > 0.35 else ('moss_block' if n1 < -0.45 else 'grass_block')
        und = 'dirt'
    elif k == 'n':
        top, und = ('snow_block' if h > 84 or n1 > 0.2 else 'grass_block'), 'stone'
        if h > 100 and n1 < -0.3:
            top = 'packed_ice'
        if h <= WATER:
            top = 'gravel'
    elif k == 'ne':
        top = 'mud' if n1 > 0.1 else ('moss_block' if n1 < -0.4 else 'grass_block')
        und = 'mud'
    elif k == 'e':
        top, und = ('sand', 'sandstone')
        if n1 > 0.62:
            top = 'red_sand'
        ox, oz = P['oasis']
        if math.hypot(x - ox - 14, z - oz + 2) < 17 and h > WATER:
            top = 'grass_block'
    elif k == 'se':
        r = math.hypot(x - VX, z - VZ)
        top = 'basalt' if n1 > 0.2 else ('blackstone' if n1 < -0.3 else 'tuff')
        if r < 26 and h > 100:
            top = 'magma_block' if n1 > 0.45 else 'blackstone'
        und = 'blackstone'
    elif k == 's':
        top, und = ('grass_block', 'stone') if h < 84 else ('stone', 'stone')
        if h > 108:
            top = 'snow_block' if n1 > -0.2 else 'stone'
        if 84 <= h <= 108 and n1 > 0.3:
            top = 'andesite'
    else:  # sw
        top = 'soul_soil' if n1 > 0.25 else ('blackstone' if n1 < -0.35 else 'coarse_dirt')
        und = 'blackstone'
    if steep and k not in ('se', 'sw'):
        top = 'stone' if n1 > -0.2 else ('mossy_cobblestone' if k in ('nw', 'w', 'ne') else 'andesite')
        und = 'stone'
    if outer and h > 100:
        top = 'snow_block' if k in ('n', 's', 'nw') else top
    fluid, fl = None, None
    if h < WATER:
        fluid, fl = ('water', WATER)
        if k == 'n' and h < WATER:
            fluid = 'water'
    return top, und, fluid, fl


H = {}
for _x in range(-HALF, HALF):
    for _z in range(-HALF, HALF):
        H[(_x, _z)] = height(_x, _z)
COL = {c: column(c[0], c[1], H[c]) for c in H}


def ground(x, z):
    """Premier bloc d'air au-dessus du sol (ou de l'eau)."""
    h = H[(x, z)]
    f = COL[(x, z)]
    return max(h, f[3] or 0) + 1


# ---------------------------------------------------------------- routes (dessus remplacé par un chemin)
def polyline(pts, step=1.0):
    out = []
    for (x1, z1), (x2, z2) in zip(pts, pts[1:]):
        n = max(1, int(max(abs(x2 - x1), abs(z2 - z1)) / step))
        for s in range(n):
            out.append((x1 + (x2 - x1) * s / n, z1 + (z2 - z1) * s / n))
    out.append(pts[-1])
    return out


ROUTES = [
    # cité -> cols
    [(-68, 0), (-80, 0), (-104, 4), (-128, 14)],
    [(0, -68), (0, -80), (0, -100)],
    [(68, 0), (80, 0), (104, 2), (114, 2)],
    [(0, 68), (0, 80), (0, 100)],
    # Valdor
    [(-128, 14), (-150, 18), (-165, 6), (-168, -40), (-168, -80), (-168, -96)],
    [(-150, 18), (-150, 46), (-130, 52)], [(-165, 6), (-192, -20), (-200, -30)], [(-128, 14), (-118, -10), (-118, -36)],
    # Sylvanor
    [(-168, -96), (-166, -120), (-160, -144)], [(-160, -160), (-140, -168), (-110, -168), (-80, -168), (-60, -168)],
    [(-166, -120), (-195, -112)], [(-160, -186), (-180, -200), (-195, -202)],
    # Givrecroc
    [(0, -100), (0, -104)], [(-60, -168), (-30, -160), (-10, -140)], [(0, -138), (10, -160), (25, -184)],
    [(-10, -140), (-45, -150), (-50, -180)], [(10, -130), (40, -140), (60, -150), (80, -150), (100, -150)],
    # Fangebrume
    [(100, -150), (128, -130), (140, -122)], [(160, -118), (168, -100), (168, -80), (168, -60)], [(150, -138), (130, -170), (120, -186)],
    # Azhar
    [(168, -60), (160, -30), (146, -6)], [(114, 2), (128, 4)], [(146, 4), (172, -28)], [(140, 18), (160, 40), (184, 48)],
    [(160, 40), (150, 60), (150, 80), (148, 96)],
    # Pyrecendre
    [(148, 96), (140, 106)], [(156, 112), (180, 140), (172, 156)], [(150, 126), (130, 150), (100, 168), (80, 168), (60, 168)],
    [(156, 104), (210, 108)],
    # Khazgarde
    [(0, 100), (0, 126), (0, 134)], [(60, 168), (40, 150), (12, 132)], [(-12, 126), (-40, 140), (-48, 180)],
    [(-20, 132), (-60, 160), (-80, 168), (-96, 166)],
    # Ombre
    [(-96, 166), (-106, 156)], [(-120, 156), (-140, 170), (-148, 178)], [(-118, 140), (-160, 120), (-198, 110)],
]
ROAD = set()
for _pts in ROUTES:
    for (px, pz) in polyline(_pts):
        for dx in (-1, 0, 1):
            for dz in (-1, 0, 1):
                c = (round(px) + dx, round(pz) + dz)
                if c in H and max(abs(c[0]), abs(c[1])) > 67:
                    ROAD.add(c)
ROAD_TOP = {'hub': 'dirt_path', 'w': 'dirt_path', 'nw': 'dirt_path', 'n': 'gravel', 'ne': 'packed_mud', 'e': 'smooth_sandstone',
            'se': 'polished_blackstone', 's': 'cobblestone', 'sw': 'polished_blackstone_bricks'}

# ---------------------------------------------------------------- commandes du relief (colonnes fusionnées le long de z)
# Seule une croûte est posée sous la surface (7 blocs, plus ce qu'il faut pour cacher les falaises) : le reste est vide, ce qui
# allège énormément la construction (éclairage, sauvegarde) et la mémoire des chunks. Donjons et salles creusées ont leurs propres murs.
def bottom(x, z):
    h = H[(x, z)]
    lo = h - 7
    for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        n = H.get((x + dx, z + dz))
        if n is not None:
            lo = min(lo, n - 1)
    return max(BASE_Y, lo)


def terrain_cmds(k):
    x0, z0, x1, z1 = rect(k)
    out = []
    for x in range(x0, x1):
        z = z0
        while z < z1:
            def key(zz):
                c = (x, zz)
                top, und, fl, fy = COL[c]
                if c in ROAD and COL[c][2] is None:
                    top = ROAD_TOP[k] if not (ROAD_TOP[k] == 'dirt_path' and top in ('sand', 'snow_block', 'stone')) else 'gravel'
                return (H[c], top, und, fl, fy, bottom(*c))
            kk = key(z)
            z2 = z
            while z2 + 1 < z1 and key(z2 + 1) == kk:
                z2 += 1
            h, top, und, fl, fy, lo_ = kk
            if h - 4 >= lo_:
                out.append(f'fill {x} {lo_} {z} {x} {h - 4} {z2} minecraft:{"stone" if k not in ("se", "sw") else "blackstone"}')
            out.append(f'fill {x} {max(lo_, h - 3)} {z} {x} {h - 1} {z2} minecraft:{und}')
            out.append(f'fill {x} {h} {z} {x} {h} {z2} minecraft:{top}')
            if fl:
                out.append(f'fill {x} {h + 1} {z} {x} {fy} {z2} minecraft:{fl}')
            z = z2 + 1
    return out


# ---------------------------------------------------------------- végétation (« place feature ») et détails du sol
rv = random.Random(4242)
USED = set()


def free_spot(x, z, r=3):
    if (x, z) not in H:
        return False
    if any((x + dx, z + dz) in ROAD for dx in range(-2, 3) for dz in range(-2, 3)):
        return False
    fl = flat_at(x, z)
    if fl and fl[1] > 0.05:
        return False
    if COL[(x, z)][2]:
        return False
    d, key, dc, outer = border_info(x, z)
    if d < 4:
        return False
    return all((x + dx, z + dz) not in USED for dx in range(-r, r + 1) for dz in range(-r, r + 1))


def scatter(k, feature, n, spacing, cond=None, tries=None):
    x0, z0, x1, z1 = rect(k)
    out = []
    for _ in range(tries or n * 30):
        if len(out) >= n:
            break
        x, z = rv.randrange(x0 + 3, x1 - 3), rv.randrange(z0 + 3, z1 - 3)
        if not free_spot(x, z, spacing):
            continue
        if cond and not cond(x, z):
            continue
        USED.add((x, z))
        out.append(f'place feature {feature} {x} {H[(x, z)] + 1} {z}')
    return out


def top_is(*names):
    return lambda x, z: COL[(x, z)][0] in names


VEG = {k: [] for k in REGIONS}
_hub_out = lambda x, z: max(abs(x), abs(z)) > 69
VEG['hub'] += scatter('hub', 'minecraft:oak', 26, 6, _hub_out) + scatter('hub', 'minecraft:birch', 14, 6, _hub_out)
VEG['hub'] += scatter('hub', 'minecraft:grass', 160, 2, _hub_out) + scatter('hub', 'minecraft:flower_plain', 60, 2, _hub_out)
VEG['w'] += scatter('w', 'minecraft:oak', 70, 5) + scatter('w', 'minecraft:fancy_oak', 24, 7) + scatter('w', 'minecraft:birch', 30, 5)
VEG['w'] += scatter('w', 'minecraft:grass', 420, 1) + scatter('w', 'minecraft:flower_meadow', 140, 2) + scatter('w', 'minecraft:pumpkin', 6, 4)
VEG['w'] += scatter('w', 'minecraft:berry_bush', 10, 3)
VEG['nw'] += scatter('nw', 'minecraft:dark_oak', 120, 5) + scatter('nw', 'minecraft:birch_tall', 70, 4) + scatter('nw', 'minecraft:mega_spruce', 20, 7)
VEG['nw'] += scatter('nw', 'minecraft:huge_red_mushroom', 10, 6) + scatter('nw', 'minecraft:huge_brown_mushroom', 10, 6)
VEG['nw'] += scatter('nw', 'minecraft:large_fern', 160, 2) + scatter('nw', 'minecraft:taiga_grass', 300, 1) + scatter('nw', 'minecraft:forest_flowers', 60, 2)
VEG['nw'] += scatter('nw', 'minecraft:firefly_bush', 50, 3) + scatter('nw', 'minecraft:rooted_azalea_tree', 16, 6)
VEG['n'] += scatter('n', 'minecraft:spruce', 110, 4, lambda x, z: H[(x, z)] < 100) + scatter('n', 'minecraft:pine', 60, 4, lambda x, z: H[(x, z)] < 92)
VEG['n'] += scatter('n', 'minecraft:mega_pine', 14, 7, lambda x, z: H[(x, z)] < 86) + scatter('n', 'minecraft:taiga_grass', 120, 1, top_is('grass_block'))
VEG['n'] += scatter('n', 'minecraft:ice_spike', 6, 8, lambda x, z: H[(x, z)] > 96)
VEG['ne'] += scatter('ne', 'minecraft:mangrove', 70, 5) + scatter('ne', 'minecraft:swamp_oak', 60, 5)
VEG['ne'] += scatter('ne', 'minecraft:huge_brown_mushroom', 8, 6) + scatter('ne', 'minecraft:grass', 200, 1)
VEG['ne'] += scatter('ne', 'minecraft:waterlily', 50, 2, None, 2000) + scatter('ne', 'minecraft:firefly_bush', 40, 3)
VEG['e'] += scatter('e', 'minecraft:cactus', 60, 4, top_is('sand', 'red_sand')) + scatter('e', 'minecraft:dead_bush', 70, 3)
_oasis = lambda x, z: math.hypot(x - P['oasis'][0] - 14, z - P['oasis'][1] + 2) < 17
VEG['e'] += scatter('e', 'minecraft:jungle_tree_no_vine', 10, 4, _oasis, 4000) + scatter('e', 'minecraft:sugar_cane', 12, 2, _oasis, 4000)
VEG['se'] += scatter('se', 'minecraft:delta', 30, 6, lambda x, z: math.hypot(x - VX, z - VZ) > 40) + \
    scatter('se', 'minecraft:basalt_pillar', 30, 5, lambda x, z: math.hypot(x - VX, z - VZ) > 30)
VEG['se'] += scatter('se', 'minecraft:small_basalt_columns', 40, 5, lambda x, z: math.hypot(x - VX, z - VZ) > 35)
VEG['s'] += scatter('s', 'minecraft:spruce', 40, 5, lambda x, z: z < KZ - 8) + scatter('s', 'minecraft:taiga_grass', 150, 1, lambda x, z: z < KZ - 8)
VEG['sw'] += scatter('sw', 'minecraft:pale_oak', 40, 6) + scatter('sw', 'minecraft:patch_soul_fire', 30, 3, top_is('soul_soil'))
VEG['sw'] += scatter('sw', 'minecraft:pale_moss_patch', 20, 4)
# détails
VEG['hub'] += scatter('hub', 'minecraft:pile_hay', 8, 5, _hub_out) + scatter('hub', 'minecraft:wildflower', 40, 2, _hub_out)
VEG['w'] += scatter('w', 'minecraft:fallen_oak_tree', 14, 5) + scatter('w', 'minecraft:wildflower', 80, 2) + scatter('w', 'minecraft:bush', 40, 2)
VEG['nw'] += scatter('nw', 'minecraft:forest_rock', 14, 5) + scatter('nw', 'minecraft:fallen_birch_tree', 10, 5) + scatter('nw', 'minecraft:leaf_litter', 80, 2)
VEG['n'] += scatter('n', 'minecraft:fallen_spruce_tree', 10, 5, lambda x, z: H[(x, z)] < 90)
VEG['e'] += scatter('e', 'minecraft:dry_grass', 90, 2, top_is('sand', 'red_sand'))
VEG['se'] += scatter('se', 'minecraft:sulfur_spike', 16, 6, lambda x, z: math.hypot(x - VX, z - VZ) > 30) + \
    scatter('se', 'minecraft:sulfur_pool', 6, 8, lambda x, z: math.hypot(x - VX, z - VZ) > 40)

# ---------------------------------------------------------------- biomes (couleurs, brume, particules, musique)
BIOMES = {
    'mg:ol_hub': dict(sky='#86a8e0', fog='#d8c8a8', water='#3f76e4', wfog='#050533', grass='#79c05a', foliage='#59ae30',
                      music='minecraft:music.overworld.meadow'),
    'mg:ol_valdor': dict(sky='#7ba4ff', fog='#c8dcff', water='#3f76e4', wfog='#050533', grass='#8db753', foliage='#6aa03c',
                         music='minecraft:music.overworld.meadow'),
    'mg:ol_sylvanor': dict(sky='#6fa08a', fog='#9cc7a8', water='#3d8ea8', wfog='#0b2a30', grass='#4f9a5b', foliage='#3d8a4c',
                           music='minecraft:music.overworld.forest', particles=[{'particle': {'type': 'minecraft:firefly'}, 'probability': 0.003}]),
    'mg:ol_givrecroc': dict(sky='#a8c4e8', fog='#e8f0ff', water='#3d57d6', wfog='#050533', grass='#80b497', foliage='#60a17b',
                            music='minecraft:music.overworld.snowy_slopes', particles=[{'particle': {'type': 'minecraft:snowflake'}, 'probability': 0.01}], fog_end=140),
    'mg:ol_fangebrume': dict(sky='#5e7a6a', fog='#7f9a84', water='#4c6559', wfog='#232317', grass='#6a7039', foliage='#6a7039',
                             music='minecraft:music.overworld.swamp', particles=[{'particle': {'type': 'minecraft:mycelium'}, 'probability': 0.03}], fog_end=64),
    'mg:ol_azhar': dict(sky='#88b8ff', fog='#f0d8a0', water='#32a598', wfog='#050533', grass='#bfb755', foliage='#aea42a',
                        music='minecraft:music.overworld.desert', particles=[{'particle': {'type': 'minecraft:white_ash'}, 'probability': 0.002}]),
    'mg:ol_pyrecendre': dict(sky='#3a2420', fog='#5a3020', water='#3f76e4', wfog='#30140a', music='minecraft:music.nether.basalt_deltas',
                             particles=[{'particle': {'type': 'minecraft:white_ash'}, 'probability': 0.08}, {'particle': {'type': 'minecraft:lava'}, 'probability': 0.0003}],
                             fog_end=110, amb={'loop': 'minecraft:ambient.basalt_deltas.loop',
                                               'additions': {'sound': 'minecraft:ambient.basalt_deltas.additions', 'tick_chance': 0.0111}}),
    'mg:ol_khazgarde': dict(sky='#8da0b8', fog='#b8c0cc', water='#3f76e4', wfog='#050533', grass='#86b783', foliage='#68a464',
                            music='minecraft:music.overworld.stony_peaks'),
    'mg:ol_ombre': dict(sky='#2a1838', fog='#3a2848', water='#3a2a5a', wfog='#100818', grass='#4a4a5a', foliage='#4a4a5a',
                        music='minecraft:music.nether.soul_sand_valley',
                        particles=[{'particle': {'type': 'minecraft:ash'}, 'probability': 0.05}, {'particle': {'type': 'minecraft:soul'}, 'probability': 0.0004}],
                        fog_end=80, amb={'loop': 'minecraft:ambient.soul_sand_valley.loop',
                                         'additions': {'sound': 'minecraft:ambient.soul_sand_valley.additions', 'tick_chance': 0.0111}}),
}


def biome_json(sky, fog, water, wfog, grass=None, foliage=None, particles=None, music=None, fog_end=None, amb=None):
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
    return {'attributes': attrs_, 'carvers': [], 'downfall': 0.6, 'effects': eff, 'features': [], 'has_precipitation': False,
            'spawn_costs': {}, 'spawners': {k: [] for k in ('ambient', 'axolotls', 'creature', 'misc', 'monster', 'underground_water_creature',
                                                             'water_ambient', 'water_creature')}, 'temperature': 0.8}


def biome_fill(k):
    x0, z0, x1, z1 = rect(k)
    b = REGIONS[k][4]
    return [f'fillbiome {x} 0 {z} {x + 15} 220 {z + 15} {b}' for x in range(x0, x1, 16) for z in range(z0, z1, 16)]


# ---------------------------------------------------------------- bords de la carte (barrières) et forceload
# barrières sur la dernière colonne de la carte (au-dessus du relief), par région, en morceaux de 32 (limite des fill)
WALLS_R = {k: [] for k in REGIONS}
for _k in REGIONS:
    _x0, _z0, _x1, _z1 = rect(_k)
    for _a in range(_z0, _z1, 32):
        _b = min(_a + 31, _z1 - 1)
        if _x0 == -HALF:
            WALLS_R[_k].append(f'fill {_x0} 40 {_a} {_x0} 200 {_b} minecraft:barrier replace minecraft:air')
        if _x1 == HALF:
            WALLS_R[_k].append(f'fill {_x1 - 1} 40 {_a} {_x1 - 1} 200 {_b} minecraft:barrier replace minecraft:air')
    for _a in range(_x0, _x1, 32):
        _b = min(_a + 31, _x1 - 1)
        if _z0 == -HALF:
            WALLS_R[_k].append(f'fill {_a} 40 {_z0} {_b} 200 {_z0} minecraft:barrier replace minecraft:air')
        if _z1 == HALF:
            WALLS_R[_k].append(f'fill {_a} 40 {_z1 - 1} {_b} 200 {_z1 - 1} minecraft:barrier replace minecraft:air')
FL = {k: '{} {} {} {}'.format(*(lambda r: (r[0], r[1], r[2] - 1, r[3] - 1))(rect(k))) for k in REGIONS}
