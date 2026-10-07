"""Génère le Circuit Champignon (kart) : terrain, piste, décor, et tables de jeu (points de passage, grille, boîtes à objets).

    python gen_kart.py ../../data/mg              # régénère data/mg/function/kart/build_*.mcfunction + tables
    python gen_kart.py ../../data/mg apercu.png   # + aperçu vu du ciel
"""
import math, os, random, sys, zlib, struct

OUT = os.path.join(sys.argv[1], 'function', 'kart')
os.makedirs(OUT, exist_ok=True)
ZC = 16500                  # centre du circuit (x 0, z 16500)
HX, HZ = 140, 110           # demi-taille de la carte
YB, ROAD = 48, 64           # dessous de l'île, dessus de la route (le kart roule en y 65)
SEA = 62
HW = 6.5                    # demi-largeur piste (route + bordures), murs juste au-delà
random.seed(61)

def W(z): return ZC + z

# ------------------------------------------------------------------ tracé (spline fermée)
WP = [(-60, 85), (40, 88), (95, 75), (125, 40), (120, 0), (95, -15), (70, 5), (45, 20), (20, 5), (25, -30),
      (55, -55), (100, -70), (115, -95), (70, -102), (0, -98), (-60, -100), (-110, -85), (-128, -45), (-115, -5),
      (-85, 5), (-70, 35), (-105, 55), (-110, 80), (-85, 92)]

def catmull(p0, p1, p2, p3, t):
    t2, t3 = t * t, t * t * t
    return tuple(0.5 * ((2 * p1[i]) + (-p0[i] + p2[i]) * t + (2 * p0[i] - 5 * p1[i] + 4 * p2[i] - p3[i]) * t2 + (-p0[i] + 3 * p1[i] - 3 * p2[i] + p3[i]) * t3) for i in (0, 1))

raw = []
n = len(WP)
for i in range(n):
    p0, p1, p2, p3 = WP[(i - 1) % n], WP[i], WP[(i + 1) % n], WP[(i + 2) % n]
    for k in range(40):
        raw.append(catmull(p0, p1, p2, p3, k / 40))
# rééchantillonnage tous les 0,5 bloc
pts = [raw[0]]
acc = 0.0
for a, b in zip(raw, raw[1:] + raw[:1]):
    d = math.dist(a, b)
    while acc + d >= 0.5:
        t = (0.5 - acc) / d
        a = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
        d = math.dist(a, b)
        pts.append(a)
        acc = 0.0
    acc += d
NP = len(pts)
LENGTH = NP * 0.5
# départ : échantillon le plus proche de (-30, 85), la piste est parcourue dans l'ordre des échantillons
S0 = min(range(NP), key=lambda i: math.dist(pts[i], (-30, 86)))
pts = pts[S0:] + pts[:S0]

def tangent(i):
    a, b = pts[(i - 2) % NP], pts[(i + 2) % NP]
    L = math.dist(a, b) or 1
    return ((b[0] - a[0]) / L, (b[1] - a[1]) / L)

def yaw_of(dx, dz):
    return round(math.degrees(math.atan2(-dx, dz)), 1)

# contrôle : pas de croisement (échantillons non voisins à moins de 18 blocs)
worst = 99
for i in range(0, NP, 4):
    for j in range(i + 80, NP - (80 if i < 80 else 0), 4):
        worst = min(worst, math.dist(pts[i], pts[j]))
print('longueur', round(LENGTH), 'blocs ; écart mini entre portions de piste', round(worst, 1))

# ------------------------------------------------------------------ éléments de piste (par position le long du tracé)
def at_frac(f): return int(f * NP) % NP
START = 0
BOOSTS = [at_frac(f) for f in (0.07, 0.30, 0.55, 0.80)]
ITEMROWS = [at_frac(f) for f in (0.13, 0.38, 0.63, 0.88)]
# saut au-dessus du ruisseau : sur la portion entre (-115,-5) et (-85,5)
JUMP = min(range(NP), key=lambda i: math.dist(pts[i], (-100, 1)))
CASTLE = min(range(NP), key=lambda i: math.dist(pts[i], (0, -98)))

# ------------------------------------------------------------------ grille de recherche
buck = {}
for i, (x, z) in enumerate(pts):
    buck.setdefault((math.floor(x / 4), math.floor(z / 4)), []).append(i)

def nearest(x, z):
    best, bi = 1e9, -1
    cx, cz = math.floor(x / 4), math.floor(z / 4)
    for gx in range(cx - 3, cx + 4):
        for gz in range(cz - 3, cz + 4):
            for i in buck.get((gx, gz), ()):
                d = (pts[i][0] - x) ** 2 + (pts[i][1] - z) ** 2
                if d < best: best, bi = d, i
    return (math.sqrt(best), bi) if bi >= 0 else (99, -1)

def along(i, j):
    """distance le long de la piste de i vers j (avant)."""
    return ((j - i) % NP) * 0.5

# ------------------------------------------------------------------ bruit
def hsh(ix, iz, s):
    n = (ix * 374761393 + iz * 668265263 + s * 982451653) & 0xffffffff
    n = ((n ^ (n >> 13)) * 1274126177) & 0xffffffff
    return ((n ^ (n >> 16)) & 0xffff) / 65535.0
def vn(x, z, sc, s):
    gx, gz = x / sc, z / sc
    x0, z0 = math.floor(gx), math.floor(gz)
    fx, fz = gx - x0, gz - z0
    u, v = fx * fx * (3 - 2 * fx), fz * fz * (3 - 2 * fz)
    a, b, c, d = hsh(x0, z0, s), hsh(x0 + 1, z0, s), hsh(x0, z0 + 1, s), hsh(x0 + 1, z0 + 1, s)
    return (a * (1 - u) + b * u) * (1 - v) + (c * (1 - u) + d * u) * v

def island(x, z):
    e = ((abs(x) / (HX - 6)) ** 4 + (abs(z) / (HZ - 6)) ** 4) ** 0.25
    return e + (vn(x, z, 20, 3) - 0.5) * 0.06

LAKE = (-28, 50, 13)
CREEK_W = 2.5

# ------------------------------------------------------------------ colonnes
col = {}
ROADSET = set()
for x in range(-HX, HX + 1):
    for z in range(-HZ, HZ + 1):
        d, si = nearest(x, z)
        e = island(x, z)
        if d <= 14:
            e = min(e, 0.9)                                   # l'île englobe toujours la piste et ses abords
        if e > 1.0:
            continue                                          # vide autour de l'île
        c = {'h': ROAD, 'top': 'grass_block', 'sub': 'dirt', 'core': 'stone', 'water': None, 'd': d, 'i': si, 'wall': False}
        h = ROAD + (vn(x, z, 14, 1) - 0.4) * 3                 # petites collines
        if d > 9:
            h += max(0, (d - 9) * 0.25) * vn(x, z, 30, 2)      # monte doucement loin de la piste
        h = min(h, ROAD + 7)
        if d <= 11:
            t = max(0, (d - 8) / 3)
            h = ROAD * (1 - t) + h * t
        h = round(h)
        if e > 0.96:
            h = min(h, ROAD - 1 - int((e - 0.96) * 60))        # falaise vers le vide
            c['top'] = 'stone' if e > 0.985 else 'grass_block'
        # lac du terrain intérieur
        lx, lz, lr = LAKE
        dl = math.hypot(x - lx, (z - lz) * 1.2)
        if dl < lr and d > 10:
            h = ROAD - 3; c.update(water=SEA + 1, top='sand', sub='sand')
        elif dl < lr + 2 and d > 10:
            h = ROAD; c['top'] = 'sand'
        # ruisseau traversé par le saut
        jx, jz = pts[JUMP]
        tx, tz = tangent(JUMP)
        along_c = (x - jx) * tx + (z - jz) * tz
        if abs(along_c) <= CREEK_W and abs((x - jx) * -tz + (z - jz) * tx) < 40:
            h = ROAD - 3; c.update(water=ROAD - 1, top='sand', sub='sand', creek=True)
        elif abs(along_c) <= CREEK_W + 1.5 and abs((x - jx) * -tz + (z - jz) * tx) < 40:
            c['top'] = 'sand'
        # piste
        if d <= HW and not c.get('creek'):
            h = ROAD
            if d <= 4.5: c['top'] = 'gray_concrete'
            elif d <= 5.0: c['top'] = 'white_concrete'
            else: c['top'] = 'red_concrete' if (si // 6) % 2 else 'white_concrete'
            ROADSET.add((x, z))
        elif HW < d <= HW + 1.2 and not c.get('creek'):
            c['wall'] = True
            if h < ROAD: h = ROAD
        if c['top'] == 'grass_block' and vn(x, z, 7, 5) > 0.72 and d > 8:
            c['top'] = 'moss_block'
        c['h'] = h
        col[(x, z)] = c

# ligne d'arrivée en damier, tremplin, plaques de boost
def stamp(i, w_from, w_to, l_from, l_to, block_fn):
    cx, cz = pts[i]; tx, tz = tangent(i); nx, nz = -tz, tx
    for a in [l_from + k * 0.5 for k in range(int((l_to - l_from) * 2) + 1)]:
        for b in [w_from + k * 0.5 for k in range(int((w_to - w_from) * 2) + 1)]:
            x, z = round(cx + tx * a + nx * b), round(cz + tz * a + nz * b)
            if (x, z) in col and (x, z) in ROADSET:
                col[(x, z)]['top'] = block_fn(round(a), round(b))
stamp(START, -4.5, 4.5, -1, 1, lambda a, b: 'black_concrete' if (a + b) % 2 else 'white_concrete')
for bi in BOOSTS:
    stamp(bi, -2, 2, 0, 3, lambda a, b: 'orange_glazed_terracotta')
stamp((JUMP - int((CREEK_W + 4) * 2)) % NP, -4.5, 4.5, 0, 1.5, lambda a, b: 'lime_concrete')
# pas de route dans le ruisseau : le tremplin fait sauter par-dessus
for (x, z), c in col.items():
    if c.get('creek'):
        ROADSET.discard((x, z))

# ------------------------------------------------------------------ émission du terrain
def sig(c): return (c['h'], c['top'], c['sub'], c['core'], c['water'])
terrain, seen = [], set()
for x in range(-HX, HX + 1):
    for z in range(-HZ, HZ + 1):
        if (x, z) not in col or (x, z) in seen: continue
        s = sig(col[(x, z)])
        w = 1
        while w < 16 and (x, z + w) in col and (x, z + w) not in seen and sig(col[(x, z + w)]) == s: w += 1
        hh = 1
        while hh < 16 and all((x + hh, z + k) in col and (x + hh, z + k) not in seen and sig(col[(x + hh, z + k)]) == s for k in range(w)): hh += 1
        for a in range(hh):
            for k in range(w): seen.add((x + a, z + k))
        h, top, sub, core, water = s
        x1, x2, z1, z2 = x, x + hh - 1, W(z), W(z + w - 1)
        if h - 4 >= YB: terrain.append(f'fill {x1} {YB} {z1} {x2} {h - 4} {z2} minecraft:{core}')
        terrain.append(f'fill {x1} {max(YB, h - 3)} {z1} {x2} {h - 1} {z2} minecraft:{sub}')
        terrain.append(f'fill {x1} {h} {z1} {x2} {h} {z2} minecraft:{top}')
        if water and h + 1 <= water:
            terrain.append(f'fill {x1} {h + 1} {z1} {x2} {water} {z2} minecraft:water')

# murs invisibles de la piste (barrières sur 3 blocs) + pneus et barrières visibles par endroits
walls = []
for (x, z), c in col.items():
    if c['wall']:
        walls.append(f'fill {x} {ROAD + 1} {W(z)} {x} {ROAD + 3} {W(z)} minecraft:barrier')
        if (c['i'] // 10) % 5 == 0:
            walls.append(f'setblock {x} {ROAD + 1} {W(z)} minecraft:black_concrete')
        elif (c['i'] // 10) % 5 == 2:
            walls.append(f'setblock {x} {ROAD + 1} {W(z)} minecraft:oak_fence')

# ------------------------------------------------------------------ décor
occ = set()
def free(x, z, r):
    return all((x + a, z + b) not in occ for a in range(-r, r + 1) for b in range(-r, r + 1))
def take(x, z, r):
    for a in range(-r, r + 1):
        for b in range(-r, r + 1): occ.add((x + a, z + b))
def ground_ok(x, z, r, dmin):
    for a in range(-r, r + 1):
        for b in range(-r, r + 1):
            c = col.get((x + a, z + b))
            if not c or c['water'] or c['d'] < dmin or c['top'] in ('stone', 'sand'): return False
    return True
def H(x, z): return col[(x, z)]['h']
deco = []
def B(s): deco.append(s)

def tree(x, z):
    y = H(x, z) + 1; t = random.randint(4, 6); k = random.choice(['oak', 'birch'])
    B(f'fill {x} {y} {W(z)} {x} {y + t - 1} {W(z)} minecraft:{k}_log')
    B(f'fill {x - 2} {y + t - 2} {W(z - 2)} {x + 2} {y + t - 1} {W(z + 2)} minecraft:{k}_leaves[persistent=true] replace air')
    B(f'fill {x - 1} {y + t} {W(z - 1)} {x + 1} {y + t + 1} {W(z + 1)} minecraft:{k}_leaves[persistent=true] replace air')

def pipe(x, z, hgt):
    y = H(x, z) + 1
    for a in range(-2, 3):
        for b in range(-2, 3):
            if a * a + b * b <= 5:
                B(f'fill {x + a} {y} {W(z + b)} {x + a} {y + hgt - 2} {W(z + b)} minecraft:green_concrete')
    for a in range(-3, 4):
        for b in range(-3, 4):
            if a * a + b * b <= 10:
                B(f'fill {x + a} {y + hgt - 1} {W(z + b)} {x + a} {y + hgt} {W(z + b)} minecraft:lime_concrete')
    B(f'fill {x - 1} {y + hgt} {W(z - 1)} {x + 1} {y + hgt} {W(z + 1)} minecraft:black_concrete')

def mushroom(x, z):
    y = H(x, z) + 1; t = random.randint(5, 8)
    B(f'fill {x - 1} {y} {W(z - 1)} {x + 1} {y + t - 1} {W(z + 1)} minecraft:white_concrete')
    r = 4
    for dy in range(3):
        rr = r - dy
        for a in range(-rr, rr + 1):
            for b in range(-rr, rr + 1):
                if a * a + b * b <= rr * rr + 1:
                    spot = (a * 3 + b * 5 + dy * 7) % 11 == 0
                    B(f'setblock {x + a} {y + t + dy} {W(z + b)} minecraft:{"white_concrete" if spot else "red_concrete"}')

def qblock(x, y, z):
    B(f'fill {x} {y} {W(z)} {x + 1} {y + 1} {W(z + 1)} minecraft:yellow_concrete')
    B(f'setblock {x} {y} {W(z)} minecraft:orange_concrete')
    B(f'setblock {x + 1} {y + 1} {W(z + 1)} minecraft:orange_concrete')

def cloud(x, y, z):
    for a in range(-4, 5):
        for b in range(-2, 3):
            if a * a / 16 + b * b / 4 <= 1:
                B(f'setblock {x + a} {y} {W(z + b)} minecraft:white_wool')
    B(f'fill {x - 2} {y + 1} {W(z - 1)} {x + 2} {y + 1} {W(z + 1)} minecraft:white_wool')

def flowerbed(x, z):
    c = col[(x, z)]
    if c['top'] in ('grass_block', 'moss_block'):
        B(f'setblock {x} {c["h"] + 1} {W(z)} minecraft:{random.choice(["poppy", "dandelion", "cornflower", "oxeye_daisy", "red_tulip", "short_grass", "short_grass"])}')

# Château (à cheval sur la piste, tunnel)
cx, cz = pts[CASTLE]; tx, tz = tangent(CASTLE); nx, nz = -tz, tx
cyaw_x = abs(tx) > abs(tz)       # piste plutôt est-ouest ?
CX, CZ = round(cx), round(cz)
if cyaw_x:
    sx1, sx2, sz1, sz2 = CX - 8, CX + 8, CZ - 14, CZ + 14     # long le long de z (perpendiculaire à la piste)
else:
    sx1, sx2, sz1, sz2 = CX - 14, CX + 14, CZ - 8, CZ + 8
castle = [f'fill {sx1} {ROAD + 1} {W(sz1)} {sx2} {ROAD + 12} {W(sz2)} minecraft:stone_bricks hollow',
          f'fill {sx1 + 1} {ROAD + 1} {W(sz1 + 1)} {sx2 - 1} {ROAD + 11} {W(sz2 - 1)} minecraft:air']
# tunnel : la piste traverse (ouvertures aux deux bouts, couloir dégagé et éclairé)
if cyaw_x:
    castle += [f'fill {sx1} {ROAD + 1} {W(CZ - 6)} {sx2} {ROAD + 6} {W(CZ + 6)} minecraft:air',
               f'fill {sx1} {ROAD + 7} {W(CZ - 6)} {sx2} {ROAD + 7} {W(CZ + 6)} minecraft:stone_bricks',
               f'fill {sx1} {ROAD + 1} {W(CZ - 7)} {sx2} {ROAD + 6} {W(CZ - 7)} minecraft:stone_bricks',
               f'fill {sx1} {ROAD + 1} {W(CZ + 7)} {sx2} {ROAD + 6} {W(CZ + 7)} minecraft:stone_bricks']
    for k in range(sx1 + 2, sx2, 4):
        castle.append(f'setblock {k} {ROAD + 7} {W(CZ)} minecraft:sea_lantern')
else:
    castle += [f'fill {CX - 6} {ROAD + 1} {W(sz1)} {CX + 6} {ROAD + 6} {W(sz2)} minecraft:air',
               f'fill {CX - 6} {ROAD + 7} {W(sz1)} {CX + 6} {ROAD + 7} {W(sz2)} minecraft:stone_bricks',
               f'fill {CX - 7} {ROAD + 1} {W(sz1)} {CX - 7} {ROAD + 6} {W(sz2)} minecraft:stone_bricks',
               f'fill {CX + 7} {ROAD + 1} {W(sz1)} {CX + 7} {ROAD + 6} {W(sz2)} minecraft:stone_bricks']
    for k in range(sz1 + 2, sz2, 4):
        castle.append(f'setblock {CX} {ROAD + 7} {W(k)} minecraft:sea_lantern')
for (ox, oz) in ((sx1, sz1), (sx1, sz2), (sx2, sz1), (sx2, sz2)):
    castle += [f'fill {ox - 2} {ROAD + 1} {W(oz - 2)} {ox + 2} {ROAD + 18} {W(oz + 2)} minecraft:white_concrete',
               f'fill {ox - 3} {ROAD + 19} {W(oz - 3)} {ox + 3} {ROAD + 19} {W(oz + 3)} minecraft:red_concrete',
               f'fill {ox - 2} {ROAD + 20} {W(oz - 2)} {ox + 2} {ROAD + 20} {W(oz + 2)} minecraft:red_concrete',
               f'fill {ox - 1} {ROAD + 21} {W(oz - 1)} {ox + 1} {ROAD + 22} {W(oz + 1)} minecraft:red_concrete',
               f'setblock {ox} {ROAD + 23} {W(oz)} minecraft:gold_block']
castle += [f'fill {CX - 4} {ROAD + 13} {W(CZ - 4)} {CX + 4} {ROAD + 24} {W(CZ + 4)} minecraft:white_concrete',
           f'fill {CX - 5} {ROAD + 25} {W(CZ - 5)} {CX + 5} {ROAD + 25} {W(CZ + 5)} minecraft:red_concrete',
           f'fill {CX - 3} {ROAD + 26} {W(CZ - 3)} {CX + 3} {ROAD + 27} {W(CZ + 3)} minecraft:red_concrete',
           f'fill {CX - 1} {ROAD + 28} {W(CZ - 1)} {CX + 1} {ROAD + 29} {W(CZ + 1)} minecraft:red_concrete',
           f'setblock {CX} {ROAD + 30} {W(CZ)} minecraft:gold_block',
           f'fill {CX - 1} {ROAD + 17} {W(CZ - 5)} {CX + 1} {ROAD + 19} {W(CZ - 5)} minecraft:yellow_stained_glass',
           f'fill {CX - 1} {ROAD + 17} {W(CZ + 5)} {CX + 1} {ROAD + 19} {W(CZ + 5)} minecraft:yellow_stained_glass']
take(CX, CZ, 16)

# Portique de départ et tribunes
sx, sz = pts[START]; tx, tz = tangent(START); nx, nz = -tz, tx
gantry = []
for side in (-1, 1):
    px, pz = round(sx + nx * 8 * side), round(sz + nz * 8 * side)
    gantry.append(f'fill {px} {ROAD + 1} {W(pz)} {px} {ROAD + 8} {W(pz)} minecraft:black_concrete')
for b in range(-8, 9):
    x, z = round(sx + nx * b), round(sz + nz * b)
    gantry.append(f'setblock {x} {ROAD + 9} {W(z)} minecraft:{"black_concrete" if b % 2 else "white_concrete"}')
    if b in (-3, 0, 3):
        gantry.append(f'setblock {x} {ROAD + 8} {W(z)} minecraft:sea_lantern')
for k in range(-14, 15):
    for row in range(5):
        x, z = round(sx + tx * k + nx * (10 + row)), round(sz + tz * k + nz * (10 + row))
        if (x, z) in col and (x, z) not in ROADSET:
            colr = ['red', 'blue', 'yellow', 'lime', 'orange'][(k // 3) % 5]
            gantry.append(f'fill {x} {ROAD + 1} {W(z)} {x} {ROAD + 1 + row} {W(z)} minecraft:{colr}_concrete')
            occ.add((x, z))

# Tuyaux, champignons, blocs ?, arbres, nuages, fleurs
for (x, z, hgt) in ((60, 40, 5), (-40, -50, 4), (80, -40, 6), (-10, 20, 4), (-135 + 15, 20, 5), (100, 95, 4), (30, -80, 5)):
    if (x, z) in col and ground_ok(x, z, 3, 9) and free(x, z, 4):
        pipe(x, z, hgt); take(x, z, 4)
for _ in range(40):
    x, z = random.randint(-HX + 10, HX - 10), random.randint(-HZ + 10, HZ - 10)
    if (x, z) in col and ground_ok(x, z, 4, 12) and free(x, z, 5):
        mushroom(x, z); take(x, z, 5)
for i in range(0, NP, 110):
    tx, tz = tangent(i); nx, nz = -tz, tx
    x, z = round(pts[i][0] + nx * 10), round(pts[i][1] + nz * 10)
    if (x, z) in col:
        qblock(x, ROAD + 7, z)
for _ in range(160):
    x, z = random.randint(-HX + 5, HX - 5), random.randint(-HZ + 5, HZ - 5)
    if (x, z) in col and ground_ok(x, z, 2, 10) and free(x, z, 3):
        tree(x, z); take(x, z, 3)
for _ in range(14):
    cloud(random.randint(-HX + 10, HX - 10), random.randint(92, 105), random.randint(-HZ + 10, HZ - 10))
for (x, z), c in col.items():
    if (x, z) not in occ and c['d'] > 8 and not c['water'] and random.random() < 0.06:
        flowerbed(x, z)

# ------------------------------------------------------------------ tables de jeu
K = int(LENGTH / 10)                  # points de passage tous les ~10 blocs
CPS = []
for k in range(K):
    i = int(k * NP / K)
    x, z = pts[i]; tx, tz = tangent(i)
    CPS.append((round(x, 1), round(z, 1), yaw_of(tx, tz)))
# un point de passage ne doit pas tomber dans le ruisseau (secours sur l'eau) : on le recale sur la route
fixed = []
for (x, z, yw) in CPS:
    c = col.get((round(x), round(z)))
    if c and c.get('creek'):
        ii = (nearest(x, z)[1] + 16) % NP
        x, z = round(pts[ii][0], 1), round(pts[ii][1], 1)
    fixed.append((x, z, yw))
CPS = fixed

def write(name, lines):
    with open(os.path.join(OUT, name + '.mcfunction'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')

# passage d'un point (le joueur doit être à moins de 9 blocs du point attendu)
write('cp_check', [f'# Point de passage attendu (mg.kcp) atteint ? ({K} points par tour)'] +
      [f'execute if score @s mg.kcp matches {k} positioned {x} {ROAD + 1} {W(0) + z} if entity @e[type=minecraft:block_display,tag=mg.kk,distance=..9] run return run function mg:kart/cp_pass'
       for k, (x, z, yw) in enumerate(CPS)])
write('cp_tp', ['# Remise en piste (@s = kart) au point de passage $ki, tourné vers la suite'] +
      [f'execute if score $ki mg.st matches {k} run return run tp @s {x} {ROAD + 1} {W(0) + z} {yw} 0' for k, (x, z, yw) in enumerate(CPS)])
# grille de départ : 2 colonnes, rangées de 4 blocs derrière la ligne
tx, tz = tangent(START); nx, nz = -tz, tx
yaw0 = yaw_of(tx, tz)
grid = ['# Place le kart @s sur la grille (n° $gi, 1..16)']
for g in range(16):
    row, colm = g // 2, g % 2
    back = 4 + row * 4
    side = -2.5 if colm == 0 else 2.5
    x, z = pts[START][0] - tx * back + nx * side, pts[START][1] - tz * back + nz * side
    grid.append(f'execute if score $gi mg.st matches {g + 1} run return run tp @s {round(x, 1)} {ROAD + 1} {round(W(0) + z, 1)} {yaw0} 0')
write('grid_tp', grid)
# portillon de départ (devant la grille)
gate_on, gate_off = ['# Portillon de départ fermé (pendant le compte à rebours)'], ['# Portillon ouvert']
for b in range(-6, 7):
    x, z = round(pts[START][0] - tx * 1.5 + nx * b), round(pts[START][1] - tz * 1.5 + nz * b)
    gate_on.append(f'fill {x} {ROAD + 1} {W(z)} {x} {ROAD + 2} {W(z)} minecraft:barrier')
    gate_off.append(f'fill {x} {ROAD + 1} {W(z)} {x} {ROAD + 2} {W(z)} minecraft:air')
write('gate_on', gate_on); write('gate_off', gate_off)
# boîtes à objets
boxes = ['# Boîtes à objets (4 rangées de 4)', 'kill @e[type=minecraft:item_display,tag=mg.kbox]', 'kill @e[type=minecraft:text_display,tag=mg.kboxq]']
for r, i in enumerate(ITEMROWS):
    tx, tz = tangent(i); nx, nz = -tz, tx
    for b in (-3, -1, 1, 3):
        x, z = pts[i][0] + nx * b, pts[i][1] + nz * b
        boxes.append(f'summon minecraft:item_display {round(x, 1)} {ROAD + 2} {round(W(0) + z, 1)} {{Tags:["mg.kbox","mg.fx"],item:{{id:"minecraft:yellow_stained_glass"}},'
                     f'transformation:{{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.1f,1.1f,1.1f]}},interpolation_duration:10}}')
        boxes.append(f'summon minecraft:text_display {round(x, 1)} {ROAD + 1.7} {round(W(0) + z, 1)} {{Tags:["mg.kboxq","mg.fx"],billboard:"center",text:[{{"text":"?","color":"gold","bold":true}}],background:0,'
                     f'transformation:{{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}}}')
write('boxes', boxes)

# zone chargée pendant la construction et les courses
# (forceload refuse plus de 256 chunks par commande : la zone est coupée en deux moitiés)
FL = [f'forceload add {-HX} {W(-HZ)} -1 {W(HZ)}', f'forceload add 0 {W(-HZ)} {HX} {W(HZ)}']
FR = [f'forceload remove {-HX} {W(-HZ)} -1 {W(HZ)}', f'forceload remove 0 {W(-HZ)} {HX} {W(HZ)}']
write('fl_add', ['# Zone du circuit chargée (construction, course)'] + FL)
write('fl_remove', ['# Zone du circuit libérée, puis zones permanentes rétablies'] + FR + ['function mg:core/forceloads'])

# construction en plusieurs ticks
clear = ['# Circuit : nettoyage de la zone']
for x in range(-HX, HX + 1, 16):
    for z in range(-HZ, HZ + 1, 16):
        clear.append(f'fill {x} {YB} {W(z)} {min(x + 15, HX)} {ROAD + 40} {W(min(z + 15, HZ))} minecraft:air')
parts = [clear]
CH = 6000
for i in range(0, len(terrain), CH):
    parts.append(['# Circuit : terrain'] + terrain[i:i + CH])
parts.append(['# Circuit : murs, château, départ'] + walls + castle + gantry)
for i in range(0, len(deco), CH):
    parts.append(['# Circuit : décor'] + deco[i:i + CH])
parts.append(['# Circuit : fin', 'function mg:kart/fl_remove', 'data modify storage mg:kart built set value 1b',
              'tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Circuit Champignon construit.","color":"green"}]'])
write('build', ['# (OP) Construit le Circuit Champignon : zone chargée, puis construction dès que tous ses chunks sont prêts',
                'function mg:kart/fl_add', 'scoreboard players set $kbw mg.st 0', 'schedule function mg:kart/build_wait 20t'])
write('build_wait', ['# Attend que toute la zone du circuit soit chargée (60 s au plus), puis construit',
                     'execute if function mg:kart/loaded_all run return run function mg:kart/build_1',
                     'scoreboard players add $kbw mg.st 1',
                     'execute if score $kbw mg.st matches 60.. run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Circuit : zone toujours pas chargée, construction annulée.","color":"red"}]',
                     'schedule function mg:kart/build_wait 20t'])
lo = ['# Vrai si toute la zone du circuit est chargée (un point tous les 32 blocs ; un test de bloc échoue hors zone chargée)']
for x in list(range(-HX, HX + 1, 32)) + [HX]:
    for z in list(range(-HZ, HZ + 1, 32)) + [HZ]:
        lo.append(f'execute store success score $kld mg.st unless block {x} {ROAD} {W(z)} minecraft:bedrock')
        lo.append('execute if score $kld mg.st matches 0 run return fail')
lo.append('return 1')
write('loaded_all', lo)
for k, p in enumerate(parts, 1):
    if k < len(parts): p = p + [f'schedule function mg:kart/build_{k + 1} 2t']
    write(f'build_{k}', p)
# ------------------------------------------------------------------ minimap (tableau de droite) : 15 lignes x 24 cases
MMC, MMR = 24, 15
cells = []
for r in range(MMR):
    row = []
    for c in range(MMC):
        x1 = -HX + c * (2 * HX + 1) // MMC; x2 = -HX + (c + 1) * (2 * HX + 1) // MMC
        z1 = -HZ + r * (2 * HZ + 1) // MMR; z2 = -HZ + (r + 1) * (2 * HZ + 1) // MMR
        kinds = set()
        for x in range(x1, x2):
            for z in range(z1, z2):
                cc = col.get((x, z))
                if cc is None: continue
                if (x, z) in ROADSET: kinds.add('road')
                elif cc['water']: kinds.add('water')
                else: kinds.add('grass')
        sx, sz = pts[START]
        if x1 <= sx < x2 and z1 <= sz < z2: color = 'white'
        elif 'road' in kinds: color = 'gray'
        elif 'water' in kinds: color = 'dark_aqua'
        elif 'grass' in kinds: color = 'dark_green'
        else: color = 'black'
        row.append('{text:"█",color:"%s"}' % color)
    cells.append('l%d:[%s]' % (r, ','.join(row)))
write('mm_base', ['# Minimap : carte de base (générée)', 'data modify storage mg:kart base set value {' + ','.join(cells) + '}'])
write('mm_show', ['# Minimap : affiche les 15 lignes dans le tableau de droite (macro, storage mg:kart mm)'] +
      [f'$scoreboard players display name m{r:02d} mg.kmap $(l{r})' for r in range(MMR)])
write('mm_init', ['# Minimap : lignes du tableau (ordre de haut en bas)'] + [f'scoreboard players set m{r:02d} mg.kmap {MMR - r}' for r in range(MMR)])

with open(os.path.join(OUT, 'const.mcfunction'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(f'# Constantes du circuit (générées)\nscoreboard players set $kK mg.st {K}\nscoreboard players set $kLaps mg.st 3\n'
            f'scoreboard players set #kmx0 mg.st {HX}\nscoreboard players set #kmz0 mg.st {ZC - HZ}\nscoreboard players set #kmc mg.st {MMC}\n'
            f'scoreboard players set #kmw mg.st {2 * HX + 1}\nscoreboard players set #kmr mg.st {MMR}\nscoreboard players set #kmh mg.st {2 * HZ + 1}\n')
print('points de passage', K, '| commandes terrain', len(terrain), 'décor', len(deco), '| étapes', len(parts))

# ------------------------------------------------------------------ aperçu PNG
if len(sys.argv) > 2:
    w, hgt, sc = (2 * HX + 1), (2 * HZ + 1), 3
    px = bytearray(w * sc * hgt * sc * 3)
    def rect(x1, y1, x2, y2, rgb):
        for yy in range(max(0, y1), min(hgt * sc, y2 + 1)):
            for xx in range(max(0, x1), min(w * sc, x2 + 1)):
                k = (yy * w * sc + xx) * 3; px[k:k + 3] = bytes(rgb)
    COL = {'grass_block': (95, 160, 60), 'moss_block': (80, 140, 50), 'gray_concrete': (70, 70, 75), 'white_concrete': (235, 235, 235),
           'red_concrete': (200, 40, 40), 'black_concrete': (20, 20, 20), 'orange_glazed_terracotta': (240, 140, 20),
           'lime_concrete': (120, 220, 40), 'sand': (225, 210, 150), 'stone': (125, 125, 125)}
    for (x, z), c in col.items():
        rgb = (40, 110, 200) if c['water'] else COL.get(c['top'], (255, 0, 255))
        if c['wall']: rgb = (120, 60, 30)
        f = 1 + (c['h'] - ROAD) * 0.03
        rgb = tuple(max(0, min(255, int(v * f))) for v in rgb)
        X, Z = (x + HX) * sc, (z + HZ) * sc
        rect(X, Z, X + sc - 1, Z + sc - 1, rgb)
    for (x, z) in occ:
        if (x, z) in col:
            X, Z = (x + HX) * sc, (z + HZ) * sc; rect(X, Z, X + 1, Z + 1, (30, 70, 30))
    for (x, z, yw) in CPS:
        X, Z = int((x + HX) * sc), int((z + HZ) * sc); rect(X - 1, Z - 1, X + 1, Z + 1, (255, 255, 0))
    for i in ITEMROWS:
        X, Z = int((pts[i][0] + HX) * sc), int((pts[i][1] + HZ) * sc); rect(X - 3, Z - 3, X + 3, Z + 3, (255, 220, 0))
    raw = b''.join(bytes([0]) + bytes(px[y * w * sc * 3:(y + 1) * w * sc * 3]) for y in range(hgt * sc))
    def chunk(t, d): return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    with open(sys.argv[2], 'wb') as f:
        f.write(bytes([137, 80, 78, 71, 13, 10, 26, 10]) + chunk(b'IHDR', struct.pack('>IIBBBBB', w * sc, hgt * sc, 8, 2, 0, 0, 0))
                + chunk(b'IDAT', zlib.compress(raw, 6)) + chunk(b'IEND', b''))
    print('aperçu', sys.argv[2])
