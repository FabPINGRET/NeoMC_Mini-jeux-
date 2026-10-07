"""Génère le circuit 2 du kart, le Royaume Koopa : python gen_kart2.py ../../data/mg [apercu.png]

Île à z 19000 (401 x 301 blocs). Tour d'environ 1,5 km : départ en ville (tribunes, maisons Toad), Plage Koopa (lagune,
Cheep Cheep qui sautent, saut au-dessus d'un bras de mer), jungle (pont de bois, plantes Piranha, Goombas), désert
(pyramide traversée par un tunnel, Pokeys, sables mouvants), montée vers le château de Bowser (Thwomps, barres de feu,
Podoboos, canaux de lave), pont au-dessus de la lave avec un Chomp, descente et grand saut au-dessus d'une douve de lave.

Sortie : data/mg/function/kart/t2/*.mcfunction (le moteur appelle ces tables via les fonctions d'aiguillage de kart/).
"""
import math, os, random, sys, zlib, struct

OUT = os.path.join(sys.argv[1], 'function', 'kart', 't2')
os.makedirs(OUT, exist_ok=True)
PF = 'mg:kart/t2/'
ZC = 19000
HX, HZ = 250, 185
YB, ROAD, SEA = 40, 64, 62
HW = 6.5
WALLD = HW + 1.2
random.seed(62)

def W(z): return ZC + z

# ------------------------------------------------------------------ tracé 3D (x, z, hauteur au-dessus de la route de base)
WP = [(-55, 158, 0), (0, 160, 0), (60, 157, 0), (120, 150, 0), (170, 132, 0), (200, 100, 0), (205, 55, 0), (200, 15, 0),
      (180, -15, 0), (200, -50, 0), (195, -100, 0), (170, -140, 0), (130, -158, 0), (90, -150, 0), (55, -160, 0), (25, -135, 0),
      (15, -95, 2), (0, -55, 6), (-15, -25, 9), (-45, -40, 7), (-60, -80, 3), (-78, -130, 0), (-120, -160, 0), (-170, -150, 2),
      (-215, -125, 3), (-225, -80, 1), (-200, -50, 0), (-160, -40, 0), (-150, -10, 1), (-185, 10, 4), (-225, 40, 8), (-225, 85, 11),
      (-195, 110, 13), (-150, 125, 14), (-115, 115, 14), (-95, 132, 11), (-90, 148, 7), (-78, 158, 4)]

def catmull(p0, p1, p2, p3, t):
    t2, t3 = t * t, t * t * t
    return tuple(0.5 * ((2 * p1[k]) + (-p0[k] + p2[k]) * t + (2 * p0[k] - 5 * p1[k] + 4 * p2[k] - p3[k]) * t2
                        + (-p0[k] + 3 * p1[k] - 3 * p2[k] + p3[k]) * t3) for k in range(3))

raw = []
n = len(WP)
for i in range(n):
    p0, p1, p2, p3 = WP[(i - 1) % n], WP[i], WP[(i + 1) % n], WP[(i + 2) % n]
    for k in range(60):
        raw.append(catmull(p0, p1, p2, p3, k / 60))
pts3 = [raw[0]]
acc = 0.0
for a, b in zip(raw, raw[1:] + raw[:1]):
    d = math.dist(a[:2], b[:2])
    while acc + d >= 0.5:
        t = (0.5 - acc) / d
        a = tuple(a[k] + (b[k] - a[k]) * t for k in range(3))
        d = math.dist(a[:2], b[:2])
        pts3.append(a)
        acc = 0.0
    acc += d
NP = len(pts3)
S0 = min(range(NP), key=lambda i: math.dist(pts3[i][:2], (0, 160)))
pts3 = pts3[S0:] + pts3[:S0]
# hauteur lissée (moyenne glissante sur 16 blocs), arrondie au bloc : la route monte et descend par marches d'un bloc
yf = [p[2] for p in pts3]
WIN = 32
ys = [sum(yf[(i + k) % NP] for k in range(-WIN, WIN + 1)) / (2 * WIN + 1) for i in range(NP)]
YI = [max(0, round(v)) for v in ys]
pts = [(p[0], p[1]) for p in pts3]
LENGTH = NP * 0.5

def tangent(i):
    a, b = pts[(i - 2) % NP], pts[(i + 2) % NP]
    L = math.dist(a, b) or 1
    return ((b[0] - a[0]) / L, (b[1] - a[1]) / L)

def yaw_of(dx, dz):
    return round(math.degrees(math.atan2(-dx, dz)), 1)

def RY(i): return ROAD + YI[i % NP]          # dessus de la route au point i (le kart roule à RY + 1)

def frame(i):
    i %= NP
    tx, tz = tangent(i)
    return pts[i][0], pts[i][1], tx, tz, -tz, tx, RY(i)

def near_wp(x, z): return min(range(NP), key=lambda i: math.dist(pts[i], (x, z)))
def at_frac(f): return int(f * NP) % NP
def along(i, j): return ((j - i) % NP) * 0.5            # distance le long de la piste de i vers j (avant)
def sdist(i, j):                                          # distance signée de i à j (court chemin)
    d = (j - i) % NP
    if d > NP // 2: d -= NP
    return d * 0.5
def in_range(i, a, b): return (i - a) % NP <= (b - a) % NP

worst = 99
for i in range(0, NP, 4):
    for j in range(i + 90, NP - (90 if i < 90 else 0), 4):
        worst = min(worst, math.dist(pts[i], pts[j]))
steps = [abs(YI[(i + 1) % NP] - YI[i]) for i in range(NP)]
run = min((k for k in range(1, 60) if any(YI[(i + k) % NP] - YI[i] >= 2 for i in range(NP))), default=99) * 0.5
print('longueur', round(LENGTH), 'blocs | écart mini', round(worst, 1), '| hauteur max', max(YI), '| 2 marches en au moins', run, 'blocs')

# ------------------------------------------------------------------ repères de la piste
START = 0
CA = near_wp(-198, 108)          # entrée du château
CB = near_wp(-118, 117)          # sortie du château
BE = near_wp(-93, 140)           # fin du pont sur la lave
GAPL = near_wp(-64, 158)        # douve de lave (saut)
GAPW = near_wp(204, 78)         # bras de mer (saut)
PYR = near_wp(-196, -50)        # pyramide
GAPH = 3.5                      # demi-longueur des fossés
BOOSTS = [at_frac(f) for f in (0.05, 0.17, 0.33, 0.47, 0.6, 0.86)]
ITEMROWS = [at_frac(f) for f in (0.1, 0.25, 0.4, 0.53, 0.66, 0.93)]
QUICK = near_wp(-223, -100)      # sables mouvants
RIVER = [(98, -168), (92, -152), (84, -132), (70, -112)]
LAGOON = (183, 35, 9)
VOLC = (-178, 62)
LAKE = (80, 50, 42, 28)
MOUNT = (-95, 25, 34)

# ------------------------------------------------------------------ recherche
CELL = 6
buck = {}
for i, (x, z) in enumerate(pts):
    buck.setdefault((math.floor(x / CELL), math.floor(z / CELL)), []).append(i)

def nearest(x, z):
    best, bi = 1e9, -1
    cx, cz = math.floor(x / CELL), math.floor(z / CELL)
    for gx in range(cx - 4, cx + 5):
        for gz in range(cz - 4, cz + 5):
            for i in buck.get((gx, gz), ()):
                d = (pts[i][0] - x) ** 2 + (pts[i][1] - z) ** 2
                if d < best: best, bi = d, i
    return (math.sqrt(best), bi) if bi >= 0 else (99, -1)

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
    e = ((abs(x) / (HX - 6)) ** 6 + (abs(z) / (HZ - 6)) ** 6) ** (1 / 6)
    return e + (vn(x, z, 20, 3) - 0.5) * 0.05

def region(x, z):
    if (x < -130 and z > -20) or (x < -62 and z > 60): return 'volcan'
    if x < -62 and z <= -20: return 'desert'
    if z > 120 and x >= -62: return 'ville'
    if x >= 165: return 'plage'
    if z < -110: return 'jungle'
    return 'centre'

def seg_dist(px, pz, a, b):
    ax, az = a; bx, bz = b
    dx, dz = bx - ax, bz - az
    t = max(0, min(1, ((px - ax) * dx + (pz - az) * dz) / (dx * dx + dz * dz)))
    return math.hypot(px - ax - t * dx, pz - az - t * dz)
def river_d(x, z): return min(seg_dist(x, z, RIVER[k], RIVER[k + 1]) for k in range(len(RIVER) - 1))

PAL = {  # route, bordure A, bordure B, décor du mur
    'ville': ('gray_concrete', 'white_concrete', 'red_concrete', 'tire'),
    'plage': ('smooth_sandstone', 'white_concrete', 'light_blue_concrete', 'bamboo_fence'),
    'jungle': ('packed_mud', 'yellow_concrete', 'green_concrete', 'jungle_fence'),
    'desert': ('smooth_red_sandstone', 'white_concrete', 'orange_concrete', 'sandstone_wall'),
    'volcan': ('polished_blackstone_bricks', 'red_nether_bricks', 'polished_blackstone', 'nether_brick_fence'),
    'centre': ('gray_concrete', 'white_concrete', 'red_concrete', 'tire'),
    'chateau': ('polished_blackstone_bricks', 'gilded_blackstone', 'polished_blackstone', None)}

def base(x, z, reg):
    """terrain loin de la piste : hauteur, dessus, sous-couche, cœur, liquide, niveau du liquide."""
    if reg == 'ville':
        return ROAD + round((vn(x, z, 16, 1) - 0.5) * 2), 'grass_block', 'dirt', 'stone', None, 0
    if reg == 'plage':
        return ROAD - 1 + round((vn(x, z, 12, 2) - 0.3) * 2), 'sand', 'sand', 'sandstone', None, 0
    if reg == 'jungle':
        top = 'podzol' if vn(x, z, 9, 8) > 0.7 else ('moss_block' if vn(x, z, 7, 9) > 0.68 else 'grass_block')
        return ROAD + round(max(0, vn(x, z, 18, 4) - 0.35) * 9), top, 'dirt', 'stone', None, 0
    if reg == 'desert':
        top = 'red_sand' if vn(x, z, 14, 10) > 0.72 else 'sand'
        return ROAD + round(max(0, vn(x, z, 22, 5) - 0.3) * 11), top, 'sand', 'sandstone', None, 0
    if reg == 'volcan':
        v = vn(x, z, 6, 11)
        top = 'magma_block' if v > 0.8 else ('basalt' if v < 0.25 else 'blackstone')
        h = ROAD + round(vn(x, z, 15, 6) * 4)
        r = math.hypot(x - VOLC[0], z - VOLC[1])
        if r < 34:
            hc = ROAD + 44 * (1 - r / 34) ** 1.25
            if r < 5:
                return ROAD + 30, 'magma_block', 'blackstone', 'basalt', 'lava', ROAD + 31
            h = max(h, round(hc))
            top = 'basalt' if (x * 7 + z * 3) % 5 == 0 else 'blackstone'
        return h, top, 'blackstone', 'basalt', None, 0
    # centre : prairie, lac, montagne enneigée
    h = ROAD + round(max(0, vn(x, z, 20, 7) - 0.4) * 6)
    top = 'grass_block'
    lx, lz, la, lb = LAKE
    dl = math.hypot((x - lx) / la, (z - lz) / lb)
    if dl < 0.25: return ROAD + 1, 'grass_block', 'dirt', 'stone', None, 0
    if dl < 0.32: return ROAD, 'sand', 'sand', 'stone', None, 0
    if dl < 1: return ROAD - 4, 'sand', 'sand', 'stone', 'water', SEA
    if dl < 1.12: return ROAD, 'sand', 'sand', 'stone', None, 0
    mx, mz, mr = MOUNT
    r = math.hypot(x - mx, z - mz)
    if r < mr:
        h = max(h, round(ROAD + 36 * (1 - r / mr) ** 1.4))
        top = 'snow_block' if h > ROAD + 24 else ('stone' if h > ROAD + 12 else 'grass_block')
    return h, top, 'dirt', 'stone', None, 0

# ------------------------------------------------------------------ colonnes
col = {}
ROADSET = set()
for x in range(-HX, HX + 1):
    for z in range(-HZ, HZ + 1):
        d, si = nearest(x, z)
        e = island(x, z)
        if d <= 18: e = min(e, 0.9)
        if e > 1.0: continue
        reg = region(x, z)
        h, top, sub, core, liq, lvl = base(x, z, reg)
        c = {'top': top, 'sub': sub, 'core': core, 'liq': liq, 'lvl': lvl, 'd': d, 'i': si, 'wall': False, 'reg': reg,
             'bridge': False, 'roof': None, 'cwall': None}
        if reg == 'plage' and x > 215 and e <= 0.95:
            h, c['top'], c['sub'], c['liq'], c['lvl'] = 57, 'sand', 'sand', 'water', SEA
        lx, lz, lr = LAGOON
        dg = math.hypot(x - lx, z - lz)
        if dg < lr and d > 10: h, c['top'], c['sub'], c['liq'], c['lvl'] = 58, 'sand', 'sand', 'water', SEA
        if reg == 'jungle' and d > 6:
            rd = river_d(x, z)
            pond = min(math.dist((x, z), RIVER[0]), math.dist((x, z), RIVER[-1]))
            if rd < 3.5 or pond < 6: h, c['top'], c['sub'], c['liq'], c['lvl'] = 58, 'sand', 'clay', 'water', SEA
            elif rd < 5 or pond < 7.5: h, c['top'] = max(ROAD, h), 'sand'
        if si >= 0:
            ry = RY(si)
            if d <= 11 and not c['liq']:
                t = max(0, (d - 8) / 3)
                h = round(ry * (1 - t) + h * t)
            elif d <= 9 and c['liq'] and not (reg == 'jungle' and river_d(x, z) < 3.5):
                h, c['liq'] = ry, None
        if e > 0.95 and not c['liq']:
            if e > 0.975: h = min(h, ROAD - 1 - int((e - 0.975) * 80)); c['top'] = 'stone' if e > 0.988 else c['top']
            else: h = max(h, SEA + 1)
        if e > 0.95 and c['liq'] and e > 0.955: h, c['liq'], c['top'] = SEA + 1, None, 'sand'
        reg_t = region(*pts[si]) if si >= 0 else reg
        if si >= 0 and in_range(si, CA, CB) and d <= 12.5: reg_t = 'chateau'
        c['regt'] = reg_t
        if si >= 0 and d <= HW:
            ry = RY(si)
            h = ry
            road, ca, cb, _ = PAL[reg_t]
            c['top'] = road if d <= 4.5 else (ca if d <= 5.0 else (ca if (si // 6) % 2 else cb))
            c['liq'] = None
            ROADSET.add((x, z))
        elif si >= 0 and d <= WALLD:
            h = RY(si); c['wall'] = True; c['liq'] = None
            c['top'] = PAL[reg_t][1] if reg_t != 'ville' else 'white_concrete'
        c['h'] = h
        col[(x, z)] = c

def zone_set(c, h, top, liq, lvl):
    c.update(h=h, top=top, liq=liq, lvl=lvl)

for (x, z), c in col.items():
    si, d = c['i'], c['d']
    if si < 0: continue
    ry = RY(si)
    # château : canaux de lave entre la route et les murs, toit
    if in_range(si, CA, CB) and d <= 12.5:
        c['roof'] = ry + 10
        if WALLD < d <= 10.5: zone_set(c, ry - 3, 'magma_block', 'lava', ry - 1)
        elif d > 10.5: c['cwall'] = ry + 9; c['h'] = ry; c['top'] = 'nether_bricks'
    # pont au-dessus de la lave à la sortie du château
    if in_range(si, CB, BE) and d <= 17:
        if d <= WALLD: c.update(bridge=True, bed=ROAD - 3, liq='lava', lvl=ROAD - 1)
        else: zone_set(c, ROAD - 3, 'magma_block', 'lava', ROAD - 1)
    # douve de lave (saut) et bras de mer (saut)
    for g, liq, lvl, reach in ((GAPL, 'lava', ROAD - 1, 14), (GAPW, 'water', SEA, 0)):
        a = sdist(g, si)
        if abs(a) <= GAPH and d <= WALLD:
            zone_set(c, ROAD - 4, 'magma_block' if liq == 'lava' else 'sand', liq, lvl); c['wall'] = False
            ROADSET.discard((x, z)); c['gap'] = True
        elif liq == 'lava' and abs(a) <= 12 and WALLD < d <= reach:
            zone_set(c, ROAD - 3, 'magma_block', 'lava', lvl)
    # chenal du bras de mer : de la piste jusqu'à la mer (côté est) et petite crique côté ouest
    a = sdist(GAPW, si)
    if abs(a) <= GAPH and d > WALLD:
        if x > pts[GAPW][0] or d <= 11: zone_set(c, ROAD - 4, 'sand', 'water', SEA)
    if abs(a) <= GAPH + 2 and d > WALLD and not c['liq']: c['top'] = 'sand'; c['h'] = max(c['h'], ROAD - 1)
    # rivière de la jungle : pont de bois
    if c['reg'] == 'jungle' and d <= WALLD and river_d(x, z) < 4.5:
        c.update(bridge=True, bed=58, liq='water', lvl=SEA)
        if d <= HW: c['top'] = 'spruce_planks'

# ligne d'arrivée, plaques de boost, tremplins, sables mouvants
def stamp(i, w_from, w_to, l_from, l_to, block_fn):
    cx, cz, tx, tz, nx, nz, _ = frame(i)
    for a in [l_from + k * 0.5 for k in range(int((l_to - l_from) * 2) + 1)]:
        for b in [w_from + k * 0.5 for k in range(int((w_to - w_from) * 2) + 1)]:
            x, z = round(cx + tx * a + nx * b), round(cz + tz * a + nz * b)
            if (x, z) in ROADSET:
                col[(x, z)]['top'] = block_fn(round(a), round(b))
stamp(START, -4.5, 4.5, -1, 1, lambda a, b: 'black_concrete' if (a + b) % 2 else 'white_concrete')
for bi in BOOSTS:
    stamp(bi, -2, 2, 0, 3, lambda a, b: 'orange_glazed_terracotta')
for g in (GAPL, GAPW):
    stamp((g - int((GAPH + 4) * 2)) % NP, -4.5, 4.5, 0, 1.5, lambda a, b: 'lime_concrete')
stamp(QUICK, -4.5, 0.5, -6, 6, lambda a, b: 'soul_sand')

# ------------------------------------------------------------------ émission du terrain
def sig(c):
    return (c['h'], c['top'], c['sub'], c['core'], c['liq'], c['lvl'], c['bridge'], c.get('bed', 0))
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
        h, top, sub, core, liq, lvl, bridge, bed = s
        x1, x2, z1, z2 = x, x + hh - 1, W(z), W(z + w - 1)
        floor = bed if bridge else h
        if floor - 4 >= YB: terrain.append(f'fill {x1} {YB} {z1} {x2} {floor - 4} {z2} minecraft:{core}')
        terrain.append(f'fill {x1} {max(YB, floor - 3)} {z1} {x2} {floor - 1} {z2} minecraft:{sub}')
        if bridge:
            terrain.append(f'fill {x1} {bed} {z1} {x2} {bed} {z2} minecraft:{"magma_block" if liq == "lava" else "sand"}')
            terrain.append(f'fill {x1} {bed + 1} {z1} {x2} {lvl} {z2} minecraft:{liq}')
            terrain.append(f'fill {x1} {h} {z1} {x2} {h} {z2} minecraft:{top}')
        else:
            terrain.append(f'fill {x1} {h} {z1} {x2} {h} {z2} minecraft:{top}')
            if liq and h + 1 <= lvl:
                terrain.append(f'fill {x1} {h + 1} {z1} {x2} {lvl} {z2} minecraft:{liq}')

# murs : barrières sur 4 blocs, décor visible selon la zone
walls = []
for (x, z), c in col.items():
    if not c['wall']: continue
    h = c['h']
    walls.append(f'fill {x} {h + 1} {W(z)} {x} {h + 4} {W(z)} minecraft:barrier')
    deco_w = PAL[c['regt']][3]
    k = (c['i'] // 10) % 5
    if deco_w == 'tire':
        if k == 0: walls.append(f'setblock {x} {h + 1} {W(z)} minecraft:black_concrete')
        elif k == 2: walls.append(f'setblock {x} {h + 1} {W(z)} minecraft:oak_fence')
    elif deco_w and (k in (0, 1, 3) or c['bridge']):
        walls.append(f'setblock {x} {h + 1} {W(z)} minecraft:{deco_w}')

# ------------------------------------------------------------------ outils de décor
occ = set()
for (x, z), c in col.items():
    if c['d'] <= WALLD + 1 or c.get('roof') or c['liq']: occ.add((x, z))
def free(x, z, r):
    return all((x + a, z + b) not in occ for a in range(-r, r + 1) for b in range(-r, r + 1))
def take(x, z, r):
    for a in range(-r, r + 1):
        for b in range(-r, r + 1): occ.add((x + a, z + b))
def ground_ok(x, z, r, dmin, tops=None):
    for a in range(-r, r + 1):
        for b in range(-r, r + 1):
            c = col.get((x + a, z + b))
            if not c or c['liq'] or c['d'] < dmin or c.get('roof') or c['bridge'] or c.get('gap'): return False
            if tops and c['top'] not in tops: return False
    return True
def H(x, z): return col[(x, z)]['h']
def spot(reg, dmin, r, tries=4000, tops=None):
    for _ in range(tries):
        x, z = random.randint(-HX + 8, HX - 8), random.randint(-HZ + 8, HZ - 8)
        c = col.get((x, z))
        if c and c['reg'] == reg and ground_ok(x, z, r, dmin, tops) and free(x, z, r):
            take(x, z, r); return x, z
    return None

deco = []
def B(s): deco.append(s)
def sb(x, y, z, blk): B(f'setblock {x} {y} {W(z)} minecraft:{blk}')
def fl(x1, y1, z1, x2, y2, z2, blk, mode=''):
    B(f'fill {min(x1, x2)} {min(y1, y2)} {W(min(z1, z2))} {max(x1, x2)} {max(y1, y2)} {W(max(z1, z2))} minecraft:{blk}{(" " + mode) if mode else ""}')

def disc(x, y, z, r, blk, mode=''):
    for a in range(-r, r + 1):
        w = int(math.sqrt(max(0, r * r + r - a * a)))
        fl(x + a, y, z - w, x + a, y, z + w, blk, mode)

# modèles en voxels orientés : boîtes (u = devant, v = côté, y) tournées vers une direction cardinale
def cardinal(dx, dz):
    return (round(dx / abs(dx)) if abs(dx) >= abs(dz) else 0, 0 if abs(dx) >= abs(dz) else round(dz / abs(dz)))
def vox(ox, oy, oz, fwd, boxes):
    fx, fz = fwd
    sx, sz = -fz, fx
    for (u1, u2, v1, v2, y1, y2, blk) in boxes:
        xa, za = ox + fx * u1 + sx * v1, oz + fz * u1 + sz * v1
        xb, zb = ox + fx * u2 + sx * v2, oz + fz * u2 + sz * v2
        fl(xa, oy + y1, za, xb, oy + y2, zb, blk)

# ---- arbres et plantes
def tree(x, z):
    y = H(x, z) + 1; t = random.randint(4, 6); k = random.choice(['oak', 'birch'])
    fl(x, y, z, x, y + t - 1, z, f'{k}_log')
    fl(x - 2, y + t - 2, z - 2, x + 2, y + t - 1, z + 2, f'{k}_leaves[persistent=true]', 'replace air')
    fl(x - 1, y + t, z - 1, x + 1, y + t + 1, z + 1, f'{k}_leaves[persistent=true]', 'replace air')

def jungle_tree(x, z):
    y = H(x, z) + 1; t = random.randint(11, 17)
    fl(x, y, z, x + 1, y + t - 1, z + 1, 'jungle_log')
    for k, r in ((t - 3, 5), (t - 1, 4), (t + 1, 3), (t + 2, 1)):
        disc(x, y + k, z, r, 'jungle_leaves[persistent=true]', 'replace air')
    for k in range(4, t - 4, 4):
        a, b = random.choice(((-2, 0), (3, 0), (0, -2), (0, 3)))
        sb(x + a, y + k, z + b, 'jungle_log[axis=y]')
        disc(x + a, y + k + 1, z + b, 2, 'jungle_leaves[persistent=true]', 'replace air')

def palm(x, z):
    y = H(x, z) + 1; t = random.randint(6, 9)
    dx, dz = random.choice(((1, 0), (-1, 0), (0, 1), (0, -1)))
    cx, cz = x, z
    for k in range(t):
        if k and k % 3 == 0: cx += dx; cz += dz
        sb(cx, y + k, cz, 'jungle_log')
    top = y + t
    sb(cx, top, cz, 'jungle_leaves[persistent=true]')
    for ax, az in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):
        for s in range(1, 5 if ax * az == 0 else 4):
            sb(cx + ax * s, top - (1 if s >= 3 else 0), cz + az * s, 'jungle_leaves[persistent=true]')
    sb(cx + 1, top - 1, cz, 'brown_terracotta'); sb(cx, top - 1, cz + 1, 'brown_terracotta')

def bush(x, z, k='oak'):
    y = H(x, z) + 1
    fl(x, y, z, x + 1, y, z + 1, f'{k}_leaves[persistent=true]', 'replace air')
    sb(x, y + 1, z, f'{k}_leaves[persistent=true]')

def cactus(x, z):
    y = H(x, z) + 1
    fl(x, y, z, x, y + random.randint(1, 3), z, 'cactus')

def mushroom(x, z, big=False):
    y = H(x, z) + 1; t = random.randint(5, 8) + (4 if big else 0)
    fl(x - 1, y, z - 1, x + 1, y + t - 1, z + 1, 'white_concrete')
    r = 4 + (2 if big else 0)
    for dy in range(3):
        rr = r - dy
        for a in range(-rr, rr + 1):
            for b in range(-rr, rr + 1):
                if a * a + b * b <= rr * rr + 1:
                    s = (a * 3 + b * 5 + dy * 7) % 11 == 0
                    sb(x + a, y + t + dy, z + b, 'white_concrete' if s else random.choice(['red_concrete', 'red_concrete', 'red_concrete']))

def pipe(x, z, hgt, y=None):
    y = (H(x, z) + 1) if y is None else y
    for a in range(-2, 3):
        for b in range(-2, 3):
            if a * a + b * b <= 5: fl(x + a, y, z + b, x + a, y + hgt - 2, z + b, 'green_concrete')
    for a in range(-3, 4):
        for b in range(-3, 4):
            if a * a + b * b <= 10: fl(x + a, y + hgt - 1, z + b, x + a, y + hgt, z + b, 'lime_concrete')
    fl(x - 1, y + hgt, z - 1, x + 1, y + hgt, z + 1, 'black_concrete')

def qblock(x, y, z):
    fl(x, y, z, x + 1, y + 1, z + 1, 'yellow_concrete')
    sb(x, y, z, 'orange_concrete'); sb(x + 1, y + 1, z + 1, 'orange_concrete')

def cloud(x, y, z):
    for a in range(-5, 6):
        for b in range(-2, 3):
            if a * a / 25 + b * b / 4 <= 1: sb(x + a, y, z + b, 'white_wool')
    fl(x - 3, y + 1, z - 1, x + 3, y + 1, z + 1, 'white_wool')
    fl(x - 1, y + 2, z, x + 1, y + 2, z, 'white_wool')

def toad_house(x, z, fwd):
    y = H(x, z) + 1
    for a in range(-3, 4):
        for b in range(-3, 4):
            if a * a + b * b <= 10: fl(x + a, y, z + b, x + a, y + 4, z + b, 'white_terracotta')
    for a in range(-2, 3):
        for b in range(-2, 3):
            if a * a + b * b <= 5: fl(x + a, y, z + b, x + a, y + 4, z + b, 'air')
    fx, fz = fwd
    sb(x + 3 * fx, y, z + 3 * fz, 'air'); sb(x + 3 * fx, y + 1, z + 3 * fz, 'air')
    sb(x + 3 * fx - fz, y + 2, z + 3 * fz + fx, 'glass_pane'); sb(x + 3 * fx + fz, y + 2, z + 3 * fz - fx, 'glass_pane')
    sb(x, y, z, 'crafting_table')
    sb(x - fz * 2, y + 3, z + fx * 2, 'lantern')
    cap = random.choice(['red_concrete', 'red_concrete', 'blue_concrete', 'lime_concrete', 'yellow_concrete'])
    for dy, r in ((5, 5), (6, 5), (7, 4), (8, 3)):
        for a in range(-r, r + 1):
            for b in range(-r, r + 1):
                if a * a + b * b <= r * r + 1:
                    s = (a * 5 + b * 3 + dy) % 7 == 0
                    sb(x + a, y + dy, z + b, 'white_concrete' if s else cap)

def umbrella(x, z):
    y = H(x, z) + 1
    fl(x, y, z, x, y + 3, z, 'oak_fence')
    c1, c2 = random.choice((('red', 'white'), ('blue', 'white'), ('yellow', 'orange'), ('lime', 'white')))
    for a in range(-2, 3):
        for b in range(-2, 3):
            if a * a + b * b <= 5: sb(x + a, y + 4, z + b, f'{c1 if (a + b) % 2 else c2}_wool')
    sb(x, y + 5, z, f'{c1}_wool')
    sb(x + 1, y, z, f'{c2}_carpet'); sb(x + 1, y, z + 1, f'{c2}_carpet')

def lamp(x, z, y=None):
    y = (H(x, z) + 1) if y is None else y
    fl(x, y, z, x, y + 3, z, 'dark_oak_fence')
    sb(x, y + 4, z, 'lantern')

def flag(x, z, color):
    y = H(x, z) + 1
    fl(x, y, z, x, y + 6, z, 'white_concrete')
    fl(x + 1, y + 4, z, x + 3, y + 6, z, f'{color}_wool')

def rock(x, z, blk='andesite'):
    y = H(x, z)
    disc(x, y + 1, z, random.randint(1, 2), blk)
    sb(x, y + 2, z, blk)

def basalt_pillar(x, z):
    y = H(x, z) + 1
    fl(x, y, z, x, y + random.randint(3, 9), z, 'basalt')

# ------------------------------------------------------------------ structures
struct_ = []
def S(s): struct_.append(s)

# Ville : portique de départ, tribunes avec spectateurs, drapeaux, maisons Toad, fontaine, lampadaires
sx, sz, tx, tz, nx, nz, ry = frame(START)
SEATS = []
for side in (-1, 1):
    px, pz = round(sx + nx * 9 * side), round(sz + nz * 9 * side)
    fl(px, ry + 1, pz, px, ry + 10, pz, 'black_concrete')
    sb(px, ry + 11, pz, 'sea_lantern')
for b in range(-9, 10):
    x, z = round(sx + nx * b), round(sz + nz * b)
    sb(x, ry + 11, z, 'black_concrete' if b % 2 else 'white_concrete')
    sb(x, ry + 12, z, 'white_concrete' if b % 2 else 'black_concrete')
    if b in (-4, -2, 0, 2, 4): sb(x, ry + 10, z, 'redstone_lamp[lit=true]')
for side in (-1, 1):
    for k in range(-22, 23):
        for row in range(6):
            x, z = round(sx + tx * k + nx * (12 + row) * side), round(sz + tz * k + nz * (12 + row) * side)
            if (x, z) in col and (x, z) not in ROADSET:
                colr = ['red', 'blue', 'yellow', 'lime', 'orange', 'light_blue'][(k // 4) % 6]
                fl(x, ry + 1, z, x, ry + 1 + row, z, f'{colr}_concrete')
                occ.add((x, z))
                if k % 3 == 0 and row in (1, 3, 5): SEATS.append((x + 0.5, ry + 2 + row, z + 0.5, yaw_of(-nx * side, -nz * side)))
    for k in (-24, 24):
        x, z = round(sx + tx * k + nx * 14 * side), round(sz + tz * k + nz * 14 * side)
        fl(x, ry + 1, z, x, ry + 11, z, 'white_concrete')
        fl(x, ry + 9, z, x + 2, ry + 11, z, 'red_wool' if side < 0 else 'blue_wool')
for i in range(0, NP, 28):
    if region(*pts[i]) != 'ville': continue
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    for side in (-1, 1):
        x, z = round(cx + nx2 * 9.5 * side), round(cz + nz2 * 9.5 * side)
        if (x, z) in col and free(x, z, 0) and not col[(x, z)]['liq']: lamp(x, z); occ.add((x, z))
for k in range(14):
    p = spot('ville', 14, 6)
    if p:
        x, z = p
        toad_house(x, z, cardinal(*(lambda c: (pts[c][0] - x, pts[c][1] - z))(col[(x, z)]['i'])))
for k in range(10):
    p = spot('ville', 10, 1)
    if p: flag(p[0], p[1], random.choice(['red', 'blue', 'yellow', 'lime', 'orange', 'purple']))
p = spot('ville', 16, 5)
if p:
    x, z = p; y = H(x, z) + 1
    disc(x, y, z, 4, 'stone_bricks'); disc(x, y + 1, z, 3, 'water'); fl(x, y, z, x, y + 3, z, 'quartz_pillar')
    sb(x, y + 4, z, 'water')

# Plage : palmiers, parasols, rochers, tour de sauveteur
for k in range(36):
    p = spot('plage', 10, 2, tops={'sand'})
    if p: palm(*p)
for k in range(16):
    p = spot('plage', 9, 2, tops={'sand'})
    if p: umbrella(*p)
for k in range(10):
    p = spot('plage', 9, 2, tops={'sand'})
    if p: rock(*p, random.choice(['andesite', 'stone', 'tuff']))
p = spot('plage', 12, 3, tops={'sand'})
if p:
    x, z = p; y = H(x, z) + 1
    for a, b in ((-1, -1), (1, -1), (-1, 1), (1, 1)): fl(x + a, y, z + b, x + a, y + 4, z + b, 'oak_fence')
    fl(x - 1, y + 5, z - 1, x + 1, y + 5, z + 1, 'oak_planks'); fl(x - 1, y + 8, z - 1, x + 1, y + 8, z + 1, 'red_wool')
    for a, b in ((-1, -1), (1, -1), (-1, 1), (1, 1)): fl(x + a, y + 6, z + b, x + a, y + 7, z + b, 'oak_fence')

# Jungle : grands arbres, buissons, tuyaux, ruines
for k in range(70):
    p = spot('jungle', 11, 3)
    if p: jungle_tree(*p)
for k in range(90):
    p = spot('jungle', 9, 1)
    if p: bush(*p, random.choice(['oak', 'jungle', 'azalea']))
for k in range(4):
    p = spot('jungle', 14, 5)
    if p:
        x, z = p; y = H(x, z) + 1
        for a in (-4, 4):
            for b in (-4, 4): fl(x + a, y, z + b, x + a, y + random.randint(3, 7), z + b, 'mossy_stone_bricks')
        fl(x - 4, y, z - 4, x + 4, y, z + 4, 'mossy_cobblestone')
        fl(x - 1, y + 1, z - 1, x + 1, y + 1, z + 1, 'chiseled_stone_bricks')

# Désert : pyramide traversée par la piste, cactus, buissons morts, oasis, ruines
px0, pz0, ptx, ptz, pnx, pnz, pry = frame(PYR)
PX, PZ = round(px0), round(pz0)
for k in range(0, 24):
    hb = 24 - k
    S(f'fill {PX - hb} {pry + 1 + k} {W(PZ - hb)} {PX + hb} {pry + 1 + k} {W(PZ + hb)} minecraft:{"sandstone" if k % 3 else "smooth_sandstone"}')
S(f'setblock {PX} {pry + 25} {W(PZ)} minecraft:gold_block')
TUNNEL = []
for (x, z), c in col.items():
    if abs(x - PX) <= 25 and abs(z - PZ) <= 25 and c['d'] <= WALLD + 1.5 and c['i'] >= 0 and abs(sdist(PYR, c['i'])) < 40:
        TUNNEL.append(f'fill {x} {c["h"] + 1} {W(z)} {x} {c["h"] + 7} {W(z)} minecraft:air')
        if c['d'] > WALLD + 0.5:
            TUNNEL.append(f'setblock {x} {c["h"] + 4} {W(z)} minecraft:chiseled_sandstone')
        elif c['d'] < 1 and (c['i'] // 8) % 2 == 0:
            TUNNEL.append(f'setblock {x} {c["h"] + 8} {W(z)} minecraft:sea_lantern')
for (x, z), c in col.items():
    if abs(x - PX) <= 25 and abs(z - PZ) <= 25: occ.add((x, z))
for k in range(70):
    p = spot('desert', 9, 1, tops={'sand', 'red_sand'})
    if p: cactus(*p)
for k in range(60):
    p = spot('desert', 8, 0, tops={'sand', 'red_sand'})
    if p: sb(p[0], H(*p) + 1, p[1], 'dead_bush')
for k in range(8):
    p = spot('desert', 12, 3)
    if p:
        x, z = p; y = H(x, z) + 1
        fl(x, y, z, x, y + random.randint(3, 8), z, random.choice(['cut_sandstone', 'chiseled_sandstone', 'sandstone']))
        sb(x + 1, y, z, 'bone_block')
p = spot('desert', 16, 6)
if p:
    x, z = p; y = H(x, z)
    disc(x, y, z, 4, 'water'); disc(x, y - 1, z, 4, 'sand')
    for a, b in ((-6, 0), (6, 0), (0, 6), (0, -6)):
        if (x + a, z + b) in col: palm(x + a, z + b)

# Volcan : château de Bowser (murs, tours, créneaux, statue), piliers de basalte, colonnes de lave du pont
castle = []
def C(s): castle.append(s)
for (x, z), c in col.items():
    if c.get('cwall'):
        C(f'fill {x} {c["h"] + 1} {W(z)} {x} {c["cwall"]} {W(z)} minecraft:{"polished_blackstone_bricks" if (x + z) % 9 else "cracked_polished_blackstone_bricks"}')
        if c['d'] > 11.6 and (x + z) % 2 == 0: C(f'setblock {x} {c["roof"] + 1} {W(z)} minecraft:nether_brick_wall')
    if c.get('roof'):
        C(f'setblock {x} {c["roof"]} {W(z)} minecraft:nether_bricks')
        if c['d'] < 1 and (c['i'] // 10) % 2 == 0: C(f'setblock {x} {c["roof"]} {W(z)} minecraft:shroomlight')
        if WALLD < c['d'] <= 10.5 and (c['i'] // 14) % 3 == 0 and (x + z) % 3 == 0:
            C(f'setblock {x} {c["roof"] - 1} {W(z)} minecraft:soul_lantern[hanging=true]')
for (i, side) in ((CA, -1), (CA, 1), (CB, -1), (CB, 1)):
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    ox, oz = round(cx + nx2 * 14 * side), round(cz + nz2 * 14 * side)
    for a in range(-4, 5):
        for b in range(-4, 5):
            if a * a + b * b <= 17: C(f'fill {ox + a} {ry2 - 2} {W(oz + b)} {ox + a} {ry2 + 20} {W(oz + b)} minecraft:nether_bricks')
    for a in range(-5, 6):
        for b in range(-5, 6):
            if a * a + b * b <= 26 and (a + b) % 2 == 0: C(f'setblock {ox + a} {ry2 + 21} {W(oz + b)} minecraft:nether_brick_wall')
    for k, r in enumerate((4, 3, 3, 2, 1, 1)):
        for a in range(-r, r + 1):
            for b in range(-r, r + 1):
                if a * a + b * b <= r * r: C(f'setblock {ox + a} {ry2 + 22 + k} {W(oz + b)} minecraft:red_nether_bricks')
    C(f'setblock {ox} {ry2 + 28} {W(oz)} minecraft:shroomlight')
    for k in range(6, 19, 6): C(f'setblock {round(ox - nx2 * 4.5 * side)} {ry2 + k} {W(round(oz - nz2 * 4.5 * side))} minecraft:iron_bars')
    for (x, z), c in col.items():
        if (x - ox) ** 2 + (z - oz) ** 2 <= 30: occ.add((x, z))
# portes : arche d'entrée et de sortie
for i in (CA, CB):
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    for b in range(-12, 13):
        x, z = round(cx + nx2 * b), round(cz + nz2 * b)
        if abs(b) >= 8: C(f'fill {x} {ry2 + 1} {W(z)} {x} {ry2 + 13} {W(z)} minecraft:nether_bricks')
        else: C(f'fill {x} {ry2 + 11} {W(z)} {x} {ry2 + 14} {W(z)} minecraft:nether_bricks')
        if abs(b) <= 7 and b % 2 == 0: C(f'setblock {x} {ry2 + 15} {W(z)} minecraft:nether_brick_wall')
    for b in (-7, 7):
        x, z = round(cx + nx2 * b), round(cz + nz2 * b)
        C(f'setblock {x} {ry2 + 9} {W(z)} minecraft:soul_lantern[hanging=true]')
# statue de Bowser sur le toit de l'entrée, tournée vers les karts qui arrivent
cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(CA)
fwd = cardinal(-tx2, -tz2)
sox, soz, soy = round(cx), round(cz), ry2 + 15
G, Y, O, R, Wb, K = 'lime_terracotta', 'yellow_terracotta', 'orange_terracotta', 'red_wool', 'white_concrete', 'black_concrete'
STATUE = [(-1, 1, -4, -2, 0, 1, O), (-1, 1, 2, 4, 0, 1, O),                       # pieds
          (-1, 1, -3, -2, 2, 4, G), (-1, 1, 2, 3, 2, 4, G),                       # jambes
          (-2, 2, -4, 4, 5, 12, G), (1, 2, -3, 3, 5, 11, Y),                      # corps, ventre
          (-5, -3, -5, 5, 5, 13, 'green_concrete'), (-6, -6, -4, 4, 6, 12, Wb),   # carapace et bord
          (-7, -7, -3, -3, 8, 8, Wb), (-7, -7, 0, 0, 10, 10, Wb), (-7, -7, 3, 3, 8, 8, Wb), (-7, -7, 0, 0, 6, 6, Wb),  # pointes
          (-1, 3, -7, -5, 9, 10, O), (-1, 3, 5, 7, 9, 10, O), (2, 3, -7, -6, 11, 11, K), (2, 3, 6, 7, 11, 11, K),    # bras
          (-2, 3, -3, 3, 13, 18, G), (3, 5, -2, 2, 13, 15, Y), (4, 5, -2, 2, 13, 13, 'magma_block'),               # tête, museau, gueule
          (4, 5, -2, -2, 14, 14, Wb), (4, 5, 2, 2, 14, 14, Wb),                                                    # crocs
          (3, 3, -2, -1, 16, 17, Wb), (3, 3, 1, 2, 16, 17, Wb), (3, 3, -1, -1, 16, 16, K), (3, 3, 1, 1, 16, 16, K),  # yeux
          (-3, 0, -3, 3, 19, 20, R), (-4, -3, -2, 2, 14, 19, R),                                                   # cheveux
          (-1, 0, -4, -4, 19, 22, Wb), (-1, 0, 4, 4, 19, 22, Wb)]                                                   # cornes
for (u1, u2, v1, v2, y1, y2, blk) in STATUE:
    fx, fz = fwd; vx, vz = -fz, fx
    C(f'fill {sox + fx * u1 + vx * v1} {soy + y1} {W(soz + fz * u1 + vz * v1)} {sox + fx * u2 + vx * v2} {soy + y2} {W(soz + fz * u2 + vz * v2)} minecraft:{blk}')
# piles du pont au-dessus de la lave + garde-corps
for i in range(CB, CB + ((BE - CB) % NP), 14):
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    for side in (-1, 1):
        x, z = round(cx + nx2 * 6 * side), round(cz + nz2 * 6 * side)
        C(f'fill {x} {ROAD - 3} {W(z)} {x} {ry2 - 1} {W(z)} minecraft:nether_bricks')
        C(f'setblock {x} {ry2 + 1} {W(z)} minecraft:nether_brick_fence')
        C(f'setblock {x} {ry2 + 2} {W(z)} minecraft:soul_lantern')
# piles du pont de la jungle
for (x, z), c in col.items():
    if c['bridge'] and c['reg'] == 'jungle' and c['wall'] and (x + z) % 4 == 0:
        C(f'fill {x} {c["bed"] + 1} {W(z)} {x} {c["h"] - 1} {W(z)} minecraft:stripped_spruce_log')
for k in range(40):
    p = spot('volcan', 10, 1)
    if p: basalt_pillar(*p)
for k in range(14):
    p = spot('volcan', 10, 0)
    if p: sb(p[0], H(*p) + 1, p[1], random.choice(['soul_campfire', 'crying_obsidian', 'obsidian']))

# Centre : lac et son île au bloc ?, arc-en-ciel, montagne, champignons, arbres, tuyaux, nuages, blocs ? volants
lx, lz, la, lb = LAKE
qblock(lx - 2, ROAD + 5, lz - 2); fl(lx - 2, ROAD + 2, lz - 2, lx + 3, ROAD + 2, lz + 3, 'grass_block')
fl(lx - 2, ROAD + 3, lz - 2, lx + 3, ROAD + 4, lz + 3, 'yellow_concrete'); fl(lx - 1, ROAD + 3, lz - 1, lx + 2, ROAD + 4, lz + 2, 'orange_concrete')
RAIN = ['red', 'orange', 'yellow', 'lime', 'light_blue', 'blue', 'purple']
RBI = near_wp(-15, -25)
rcx, rcz, rtx, rtz, rnx, rnz, rry = frame(RBI)
for band, colr in enumerate(RAIN):
    r = 26 - band
    for a in range(0, 181):
        th = math.radians(a)
        bx, bz, y = rcx + rnx * r * math.cos(th), rcz + rnz * r * math.cos(th), round(rry + r * math.sin(th) * 0.75)
        for k in (-1, 0, 1):
            B(f'setblock {round(bx + rtx * k)} {y} {W(round(bz + rtz * k))} minecraft:{colr}_concrete')
for k in range(26):
    p = spot('centre', 14, 5)
    if p: mushroom(*p, big=random.random() < 0.3)
for k in range(70):
    p = spot('centre', 11, 3)
    if p and H(*p) < ROAD + 10: tree(*p)
for k in range(6):
    p = spot('centre', 12, 4)
    if p: pipe(*p, random.randint(4, 7))
for k in range(26):
    cloud(random.randint(-HX + 10, HX - 10), random.randint(100, 118), random.randint(-HZ + 10, HZ - 10))
for i in range(0, NP, 150):
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    x, z = round(cx + nx2 * 11), round(cz + nz2 * 11)
    if (x, z) in col and not col[(x, z)].get('roof'): qblock(x, ry2 + 8, z)
for (x, z), c in col.items():
    if (x, z) in occ or c['d'] < 9 or c['liq'] or c.get('roof'): continue
    r = random.random()
    if c['top'] == 'grass_block' and r < 0.07:
        sb(x, c['h'] + 1, z, random.choice(['poppy', 'dandelion', 'cornflower', 'oxeye_daisy', 'red_tulip', 'short_grass', 'short_grass', 'short_grass']))
    elif c['top'] in ('podzol', 'moss_block') and r < 0.18:
        sb(x, c['h'] + 1, z, random.choice(['fern', 'short_grass', 'fern']))

# ------------------------------------------------------------------ dangers (entités, recréées à chaque course)
T0 = 'left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]'
FLIP = 'left_rotation:[0f,1f,0f,0f],right_rotation:[0f,0f,0f,1f]'
def tf(s, ty=0.0, flip=True, sy=None):
    return 'transformation:{translation:[0f,%sf,0f],%s,scale:[%sf,%sf,%sf]}' % (round(ty, 3), FLIP if flip else T0, s, sy if sy else s, s)
def P(x, y, z): return f'{round(x, 2)} {round(y, 2)} {round(W(0) + z, 2)}'
def lerp(a, b, t): return tuple(a[k] + (b[k] - a[k]) * t for k in range(3))
HZT = '"mg.khz","mg.fx"'
spawn = ['# Royaume Koopa : dangers et animaux (recréés à chaque course)', 'kill @e[tag=mg.khz]']
tick = ['# Royaume Koopa : dangers (chaque tick de course)']
consts = set()
def phase(T, o):
    consts.add(T)
    tick.extend([f'scoreboard players operation $hp mg.st = $ktime mg.st', f'scoreboard players add $hp mg.st {o}',
                 f'scoreboard players operation $hp mg.st %= #h{T} mg.st'])
def at(p, cmd): tick.append(f'execute if score $hp mg.st matches {p} run {cmd}')
def hit_at(prange, pos, r, big=False):
    tick.append(f'execute if score $hp mg.st matches {prange} positioned {P(*pos)} as @e[type=minecraft:block_display,tag=mg.kart,distance=..{r}] run function {PF}{"hz_big" if big else "hz_hit"}')
HID = [0]
def nid():
    HID[0] += 1; return f'mg.kh{HID[0]}'

def road_pt(i, off, up=0.0):
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    return (cx + nx2 * off, ry2 + 1 + up, cz + nz2 * off)

# Thwomps : 3 rangées de 2 dans le château, en alternance (toujours un côté libre)
for f in (0.18, 0.5, 0.82):
    i = (CA + int(((CB - CA) % NP) * f)) % NP
    for side, o in ((-1, 0), (1, 50)):
        t = nid(); x, y, z = road_pt(i, 2.3 * side)
        bot, top = (x, y + 1.6, z), (x, y + 1.6 + 4.5, z)
        spawn.append(f'summon minecraft:item_display {P(*top)} {{Tags:["mg.kthw","{t}",{HZT}],teleport_duration:2,item:{{id:"minecraft:chiseled_stone_bricks"}},'
                     f'Rotation:[{yaw_of(-tangent(i)[0], -tangent(i)[1])}f,0f],{tf(3.2)}}}')
        phase(100, o)
        at(48, f'tp @e[tag={t}] {P(top[0], top[1] + 0.5, top[2])}')
        at(52, f'execute positioned {P(*bot)} run playsound minecraft:block.stone.hit master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 0.5')
        at(60, f'data merge entity @e[tag={t},limit=1] {{teleport_duration:2}}')
        at(60, f'tp @e[tag={t}] {P(*bot)}')
        at(62, f'execute positioned {P(x, y, z)} run particle minecraft:explosion ~ ~0.3 ~ 1.2 0.2 1.2 0 4')
        at(62, f'execute positioned {P(x, y, z)} run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..28] ~ ~ ~ 0.8 0.6')
        hit_at('61..84', (x, y, z), 2.3, big=True)
        at(85, f'data merge entity @e[tag={t},limit=1] {{teleport_duration:20}}')
        at(85, f'tp @e[tag={t}] {P(*top)}')
        at(99, f'data merge entity @e[tag={t},limit=1] {{teleport_duration:3}}')
# Barres de feu : 2 dans le château, sens opposés
for f, spd in ((0.34, 7), (0.66, -6)):
    i = (CA + int(((CB - CA) % NP) * f)) % NP
    x, y, z = road_pt(i, 0, 0.7)
    t = nid()
    spawn.append(f'summon minecraft:item_display {P(x, y, z)} {{Tags:["mg.kfbc","{t}",{HZT}],item:{{id:"minecraft:magma_block"}},brightness:{{sky:15,block:15}},{tf(0.9, flip=False)}}}')
    tick.append(f'execute as @e[tag={t}] at @s run rotate @s ~{spd} 0')
    for k in range(1, 6):
        tb = f'{t}b{k}'
        spawn.append(f'summon minecraft:item_display {P(x, y, z)} {{Tags:["mg.kfb","{tb}",{HZT}],teleport_duration:1,item:{{id:"minecraft:magma_block"}},brightness:{{sky:15,block:15}},{tf(0.55, flip=False)}}}')
        tick.append(f'execute as @e[tag={t}] at @s positioned ^ ^ ^{round(0.85 * k, 2)} run tp @e[tag={tb}] ~ ~ ~')
tick.append(f'execute as @e[tag=mg.kfb] at @s positioned ~ ~-0.7 ~ as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.05] run function {PF}hz_hit')
tick.append('execute if score $kph mg.st matches 0 as @e[tag=mg.kfb] at @s run particle minecraft:flame ~ ~ ~ 0.1 0.1 0.1 0.01 1')
# Sauteurs : Cheep Cheep (plage, par-dessus la chaussée) et Podoboos (château, d'un canal de lave à l'autre)
def leaper(i, item, span, low, o, T=100, sound='entity.salmon.flop', billboard=True):
    t = nid()
    A, E1, M, E2, Bp = (road_pt(i, -span, low), road_pt(i, -5, 0.4), road_pt(i, 0, 1.0), road_pt(i, 5, 0.4), road_pt(i, span, low))
    spawn.append(f'summon minecraft:item_display {P(*A)} {{Tags:["mg.kleap","{t}",{HZT}],teleport_duration:6,item:{{id:"minecraft:{item}"}},'
                 f'billboard:"center",brightness:{{sky:15,block:15}},{tf(1.4, 0.3, flip=False)}}}')
    phase(T, o)
    at(1, f'data merge entity @e[tag={t},limit=1] {{teleport_duration:6}}')
    at(1, f'tp @e[tag={t}] {P(*E1)}')
    at(1, f'execute positioned {P(*A)} run particle minecraft:{"splash" if "fish" in item else "lava"} ~ ~0.5 ~ 0.4 0.2 0.4 0 12')
    at(1, f'execute positioned {P(*A)} run playsound minecraft:{sound} master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 1')
    at(7, f'data merge entity @e[tag={t},limit=1] {{teleport_duration:4}}')
    at(7, f'tp @e[tag={t}] {P(*M)}')
    at(11, f'tp @e[tag={t}] {P(*E2)}')
    at(15, f'data merge entity @e[tag={t},limit=1] {{teleport_duration:6}}')
    at(15, f'tp @e[tag={t}] {P(*Bp)}')
    at(21, f'execute positioned {P(*Bp)} run particle minecraft:{"splash" if "fish" in item else "lava"} ~ ~0.5 ~ 0.4 0.2 0.4 0 12')
    at(60, f'data merge entity @e[tag={t},limit=1] {{teleport_duration:0}}')
    at(60, f'tp @e[tag={t}] {P(*A)}')
    for p in range(7, 16):
        q = lerp(E1, M, (p - 7) / 4) if p <= 11 else lerp(M, E2, (p - 11) / 4)
        hit_at(str(p), (q[0], q[1] - 0.6, q[2]), 1.5)
gi = near_wp(203, 32)
for k, o in enumerate((0, 37, 71)):
    leaper((gi + k * 14) % NP, 'tropical_fish', 12, -1.6, o)
for f, o in ((0.27, 10), (0.6, 55), (0.72, 80)):
    leaper((CA + int(((CB - CA) % NP) * f)) % NP, 'fire_charge', 8.5, -2.2, o, T=90, sound='block.lava.pop')
# Plantes Piranha : dans des tuyaux le long de la jungle, mordent le bord de la piste
PIPES = []
for k, f in enumerate((0.05, 0.2, 0.35, 0.5, 0.65, 0.8, 0.95)):
    a0, a1 = near_wp(170, -140), near_wp(25, -135)
    i = (a0 + int(((a1 - a0) % NP) * f)) % NP
    side = 1 if k % 2 else -1
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    px_, pz_ = round(cx + nx2 * (WALLD + 3) * side), round(cz + nz2 * (WALLD + 3) * side)
    if (px_, pz_) not in col: continue
    PIPES.append((px_, pz_, ry2))
    pipe(px_, pz_, 4, ry2 + 1)
    take(px_, pz_, 3)
    t = nid()
    rest = (px_ + 0.5, ry2 + 6.2, pz_ + 0.5)
    lunge = road_pt(i, (HW - 2.2) * side, 0.9)
    yaw = yaw_of(-nx2 * side, -nz2 * side)
    spawn.append(f'summon minecraft:item_display {P(*rest)} {{Tags:["mg.kpir","{t}",{HZT}],teleport_duration:10,item:{{id:"minecraft:red_mushroom_block"}},Rotation:[{yaw}f,0f],{tf(1.5)}}}')
    phase(70, k * 23)
    at(10, f'tp @e[tag={t}] {P(rest[0], rest[1] + 0.4, rest[2])}')
    at(25, f'tp @e[tag={t}] {P(*rest)}')
    at(40, f'execute positioned {P(*rest)} run playsound minecraft:entity.ravager.roar master @a[tag=mg.play,distance=..18] ~ ~ ~ 0.4 1.8')
    at(48, f'data merge entity @e[tag={t},limit=1] {{teleport_duration:3}}')
    at(48, f'tp @e[tag={t}] {P(*lunge)}')
    at(50, f'execute positioned {P(*lunge)} run playsound minecraft:entity.evoker_fangs.attack master @a[tag=mg.play,distance=..18] ~ ~ ~ 1 1.2')
    hit_at('50..55', (lunge[0], lunge[1] - 0.9, lunge[2]), 2.0)
    at(56, f'data merge entity @e[tag={t},limit=1] {{teleport_duration:10}}')
    at(56, f'tp @e[tag={t}] {P(*rest)}')
# Goombas (jungle) et Pokeys (désert) : traversent la piste en patrouille
def walker(i, item, tag, speed, T, scale, flip_start):
    a, b = road_pt(i, -4.0), road_pt(i, 4.0)
    if flip_start: a, b = b, a
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    yaw = yaw_of(b[0] - a[0], b[2] - a[2])
    t = nid()
    spawn.append(f'summon minecraft:item_display {P(a[0], a[1] + 0.5 * scale, a[2])} {{Tags:["{tag}","mg.kwalk","{t}",{HZT}],teleport_duration:1,item:{{id:"minecraft:{item}"}},'
                 f'Rotation:[{yaw}f,0f],{tf(scale)}}}')
for k, f in enumerate((0.12, 0.3, 0.42, 0.58, 0.74, 0.88)):
    a0, a1 = near_wp(170, -140), near_wp(25, -135)
    walker((a0 + int(((a1 - a0) % NP) * f)) % NP, 'brown_mushroom_block', 'mg.kgoo', 0.12, 66, 1.2, k % 2)
for k, f in enumerate((0.15, 0.35, 0.55, 0.75)):
    a0, a1 = near_wp(-80, -132), near_wp(-224, -95)
    walker((a0 + int(((a1 - a0) % NP) * f)) % NP, 'cactus', 'mg.kpok', 0.12, 66, 1.3, k % 2)
consts.add(66)
tick += ['scoreboard players operation $hw mg.st = $ktime mg.st', 'scoreboard players operation $hw mg.st %= #h66 mg.st',
         'execute as @e[tag=mg.kwalk] at @s run tp @s ^ ^ ^0.12',
         'execute if score $hw mg.st matches 0 as @e[tag=mg.kwalk] at @s run tp @s ~ ~ ~ ~180 0',
         f'execute as @e[tag=mg.kgoo,tag=!mg.kdead] at @s if entity @e[type=minecraft:block_display,tag=mg.kart,distance=..1.4] run function {PF}goo_squash',
         f'execute as @e[tag=mg.kpok] at @s positioned ~ ~-0.6 ~ as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.4] run function {PF}hz_hit',
         f'execute as @e[tag=mg.kdead] run function {PF}goo_wait']
# Chomp : bondit d'un bout à l'autre de la piste à la sortie du pont
ci = near_wp(-91, 146)
cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(ci)
side = 1
post = road_pt(ci, (WALLD + 5) * side, 0.0)
restp = road_pt(ci, (WALLD + 2.5) * side, 1.2)
farp = road_pt(ci, -(HW - 1.5) * side, 1.2)
C(f'fill {round(post[0])} {ry2 + 1} {W(round(post[2]))} {round(post[0])} {ry2 + 2} {W(round(post[2]))} minecraft:oak_log')
t = nid()
yaw = yaw_of(-nx2 * side, -nz2 * side)
spawn.append(f'summon minecraft:item_display {P(*restp)} {{Tags:["mg.kchomp","{t}",{HZT}],teleport_duration:3,item:{{id:"minecraft:coal_block"}},Rotation:[{yaw}f,0f],{tf(2.4)}}}')
links = []
for k in range(1, 6):
    tl = f'{t}l{k}'; links.append(tl)
    q = lerp((post[0], post[1] + 1.2, post[2]), restp, k / 6)
    spawn.append(f'summon minecraft:item_display {P(*q)} {{Tags:["mg.kchain","{tl}",{HZT}],teleport_duration:3,item:{{id:"minecraft:iron_block"}},{tf(0.3, flip=False)}}}')
phase(90, 0)
for p_, h_ in ((15, 0.6), (18, 0), (30, 0.6), (33, 0), (45, 0.6), (48, 0)):
    at(p_, f'tp @e[tag={t}] {P(restp[0], restp[1] + h_, restp[2])}')
at(52, f'execute positioned {P(*restp)} run playsound minecraft:entity.wolf.growl master @a[tag=mg.play,distance=..24] ~ ~ ~ 1 0.5')
at(58, f'execute positioned {P(*restp)} run playsound minecraft:entity.wolf.ambient master @a[tag=mg.play,distance=..30] ~ ~ ~ 1 0.5')
at(60, f'data merge entity @e[tag={t},limit=1] {{teleport_duration:4}}')
at(60, f'tp @e[tag={t}] {P(*farp)}')
for k, tl in enumerate(links, 1):
    at(60, f'data merge entity @e[tag={tl},limit=1] {{teleport_duration:4}}')
    at(60, f'tp @e[tag={tl}] {P(*lerp((post[0], post[1] + 1.2, post[2]), farp, k / 6))}')
    at(72, f'data merge entity @e[tag={tl},limit=1] {{teleport_duration:15}}')
    at(72, f'tp @e[tag={tl}] {P(*lerp((post[0], post[1] + 1.2, post[2]), restp, k / 6))}')
for k in range(5):
    q = lerp(road_pt(ci, (HW - 0.5) * side, 0), road_pt(ci, -(HW - 1.5) * side, 0), k / 4)
    hit_at('61..70', q, 1.8, big=True)
at(72, f'data merge entity @e[tag={t},limit=1] {{teleport_duration:15}}')
at(72, f'tp @e[tag={t}] {P(*restp)}')
# Sables mouvants : tourbillon de particules
qx, qy, qz = road_pt(QUICK, -2.0, 0.2)
tick.append(f'execute if score $kph mg.st matches 2 positioned {P(qx, qy, qz)} run particle minecraft:falling_dust{{block_state:"minecraft:sand"}} ~ ~ ~ 2 0.1 4 0 6')
# titre géant au-dessus du départ
spawn.append(f'summon minecraft:text_display {P(sx, ry + 16, sz)} {{Tags:[{HZT}],billboard:"vertical",text:[{{"text":"ROYAUME ","color":"gold","bold":true}},{{"text":"KOOPA","color":"red","bold":true}}],'
             f'background:1342177280,{tf(6, flip=False)}}}')

# animaux et spectateurs (immobiles, invulnérables)
MOB = 'NoAI:1b,Silent:1b,Invulnerable:1b,PersistenceRequired:1b'
def mob(kind, x, y, z, yaw=None, extra=''):
    yaw = random.randint(0, 359) if yaw is None else yaw
    spawn.append(f'summon minecraft:{kind} {P(x, y, z)} {{Tags:[{HZT},"mg.kmob"],{MOB},Rotation:[{yaw}f,0f]{("," + extra) if extra else ""}}}')
for (x, y, z, yw) in random.sample(SEATS, min(30, len(SEATS))):
    prof = random.choice(['farmer', 'librarian', 'cleric', 'fisherman', 'shepherd', 'armorer', 'cartographer', 'butcher'])
    typ = random.choice(['plains', 'desert', 'savanna', 'snow', 'jungle', 'taiga'])
    mob('villager', x, y, z, yw, f'VillagerData:{{profession:"minecraft:{prof}",type:"minecraft:{typ}",level:1}}')
def mob_on(reg, kind, n, dmin=10, water=None, extra=''):
    k = 0
    for _ in range(4000):
        if k >= n: break
        x, z = random.randint(-HX + 8, HX - 8), random.randint(-HZ + 8, HZ - 8)
        c = col.get((x, z))
        if not c or c['reg'] != reg or c['d'] < dmin or c.get('roof'): continue
        if water is None and (c['liq'] or (x, z) in occ): continue
        if water and c['liq'] != water: continue
        y = (c['lvl'] - 0.6 if water == 'water' else c['lvl'] + 0.1) if water else c['h'] + 1
        mob(kind, x + 0.5, y, z + 0.5, extra=extra); k += 1
mob_on('ville', 'cat', 5); mob_on('ville', 'villager', 6); mob_on('ville', 'chicken', 4)
mob_on('plage', 'turtle', 7); mob_on('plage', 'dolphin', 4, water='water'); mob_on('plage', 'tropical_fish', 10, dmin=9, water='water')
mob_on('plage', 'parrot', 4)
mob_on('jungle', 'parrot', 8); mob_on('jungle', 'ocelot', 4); mob_on('jungle', 'panda', 3); mob_on('jungle', 'frog', 5)
mob_on('jungle', 'axolotl', 4, dmin=9, water='water')
mob_on('desert', 'camel', 5); mob_on('desert', 'armadillo', 4); mob_on('desert', 'rabbit', 4)
mob_on('volcan', 'strider', 7, dmin=9, water='lava'); mob_on('volcan', 'magma_cube', 5, extra='Size:0')
mob_on('centre', 'cow', 6); mob_on('centre', 'sheep', 6); mob_on('centre', 'horse', 4); mob_on('centre', 'fox', 3); mob_on('centre', 'goat', 3)
for f in (0.2, 0.5, 0.8):
    i = (CA + int(((CB - CA) % NP) * f)) % NP
    for s_ in (-1, 1):
        x, y, z = road_pt(i, 9 * s_, 5)
        mob('blaze', x, y, z)

# ------------------------------------------------------------------ tables de jeu
K = int(LENGTH / 10)
CPS = []
for k in range(K):
    i = int(k * NP / K)
    for g in (GAPL, GAPW):
        if abs(sdist(g, i)) <= GAPH + 2: i = (g + int((GAPH + 4) * 2)) % NP
    x, z = pts[i]; tx, tz = tangent(i)
    CPS.append((round(x, 1), RY(i) + 1, round(z, 1), yaw_of(tx, tz)))

def write(name, lines):
    with open(os.path.join(OUT, name + '.mcfunction'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')

write('cp_check', [f'# Royaume Koopa : point de passage attendu (mg.kcp) atteint ? ({K} points par tour)'] +
      [f'execute if score @s mg.kcp matches {k} positioned {x} {y} {W(0) + z} if entity @e[type=minecraft:block_display,tag=mg.kk,distance=..9] run return run function mg:kart/cp_pass'
       for k, (x, y, z, yw) in enumerate(CPS)])
write('cp_tp', ['# Royaume Koopa : remise en piste (@s = kart) au point de passage $ki'] +
      [f'execute if score $ki mg.st matches {k} run return run tp @s {x} {y} {W(0) + z} {yw} 0' for k, (x, y, z, yw) in enumerate(CPS)])
write('bill_step', ['# Royaume Koopa : Bill Balle (@s = kart) file vers le point de passage $ki (suit les montées)'] +
      [f'execute if score $ki mg.st matches {k} facing {x} {y} {W(0) + z} run return run tp @s ^ ^ ^1.6 ~ 0' for k, (x, y, z, yw) in enumerate(CPS)])
sx, sz, tx, tz, nx, nz, ry = frame(START)
yaw0 = yaw_of(tx, tz)
grid = ['# Royaume Koopa : place le kart @s sur la grille (n° $gi, 1..16)']
for g in range(16):
    row, colm = g // 2, g % 2
    back = 4 + row * 4
    side = -2.5 if colm == 0 else 2.5
    x, z = sx - tx * back + nx * side, sz - tz * back + nz * side
    grid.append(f'execute if score $gi mg.st matches {g + 1} run return run tp @s {round(x, 1)} {ry + 1} {round(W(0) + z, 1)} {yaw0} 0')
write('grid_tp', grid)
gate_on, gate_off = ['# Portillon de départ fermé'], ['# Portillon ouvert']
for b in range(-6, 7):
    x, z = round(sx - tx * 1.5 + nx * b), round(sz - tz * 1.5 + nz * b)
    gate_on.append(f'fill {x} {ry + 1} {W(z)} {x} {ry + 2} {W(z)} minecraft:barrier')
    gate_off.append(f'fill {x} {ry + 1} {W(z)} {x} {ry + 2} {W(z)} minecraft:air')
write('gate_on', gate_on); write('gate_off', gate_off)
boxes = ['# Royaume Koopa : boîtes à objets (6 rangées de 5)', 'kill @e[type=minecraft:item_display,tag=mg.kbox]', 'kill @e[type=minecraft:text_display,tag=mg.kboxq]']
for i in ITEMROWS:
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    for b in (-3.6, -1.8, 0, 1.8, 3.6):
        x, z = cx + nx2 * b, cz + nz2 * b
        boxes.append(f'summon minecraft:item_display {round(x, 1)} {ry2 + 2} {round(W(0) + z, 1)} {{Tags:["mg.kbox","mg.kspin","mg.fx"],item:{{id:"minecraft:yellow_stained_glass"}},'
                     f'transformation:{{translation:[0f,0f,0f],{T0},scale:[1.1f,1.1f,1.1f]}},interpolation_duration:10}}')
        boxes.append(f'summon minecraft:text_display {round(x, 1)} {ry2 + 1.7} {round(W(0) + z, 1)} {{Tags:["mg.kboxq","mg.fx"],billboard:"center",text:[{{"text":"?","color":"gold","bold":true}}],background:0,'
                     f'transformation:{{translation:[0f,0f,0f],{T0},scale:[1.5f,1.5f,1.5f]}}}}')
write('boxes', boxes)
write('hazards', spawn)
write('track_tick', tick)
write('hz_hit', ['# @s = kart touché par un danger : son pilote part en tête-à-queue (sauf s\'il tourne déjà)',
                 'scoreboard players operation $ko mg.st = @s mg.ri',
                 'execute as @a[tag=mg.play] if score @s mg.ri = $ko mg.st unless score @s mg.khi matches 1.. run function mg:kart/hit'])
write('hz_big', ['# @s = kart écrasé (Thwomp, Chomp) : grand tête-à-queue',
                 'scoreboard players operation $ko mg.st = @s mg.ri',
                 'execute as @a[tag=mg.play] if score @s mg.ri = $ko mg.st unless score @s mg.khi matches 1.. run function mg:kart/hit_big'])
write('goo_squash', ['# Goomba (@s) percuté : le kart part en tête-à-queue, le Goomba est aplati 5 s',
                     f'execute as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.4] run function {PF}hz_hit',
                     'tag @s add mg.kdead', 'scoreboard players set @s mg.t 100',
                     'data merge entity @s {start_interpolation:0,interpolation_duration:3,transformation:{scale:[1.4f,0.25f,1.4f]}}',
                     'playsound minecraft:entity.slime.squish master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 1.4'])
write('goo_wait', ['scoreboard players remove @s mg.t 1', 'execute if score @s mg.t matches 1.. run return 0', 'tag @s remove mg.kdead',
                   'data merge entity @s {start_interpolation:0,interpolation_duration:6,transformation:{scale:[1.2f,1.2f,1.2f]}}'])

HXF = [(-HX, -126), (-125, -1), (0, 124), (125, HX)]
write('fl_add', ['# Royaume Koopa : zone chargée (4 bandes, forceload limité à 256 chunks par commande)'] +
      [f'forceload add {a} {W(-HZ)} {b} {W(HZ)}' for a, b in HXF])
write('fl_remove', ['# Royaume Koopa : zone libérée, puis zones permanentes rétablies'] +
      [f'forceload remove {a} {W(-HZ)} {b} {W(HZ)}' for a, b in HXF] + ['function mg:core/forceloads'])

clear = ['# Royaume Koopa : nettoyage de la zone']
for x in range(-HX, HX + 1, 16):
    for z in range(-HZ, HZ + 1, 16):
        clear.append(f'fill {x} {YB} {W(z)} {min(x + 15, HX)} {ROAD + 56} {W(min(z + 15, HZ))} minecraft:air')
q4 = (len(clear) + 3) // 4
parts = [clear[k:k + q4] for k in range(0, len(clear), q4)]
CH = 3000
for i in range(0, len(terrain), CH):
    parts.append(['# Royaume Koopa : terrain'] + terrain[i:i + CH])
allb = struct_ + TUNNEL + walls + castle + deco
for i in range(0, len(allb), CH):
    parts.append(['# Royaume Koopa : décor'] + allb[i:i + CH])
parts.append(['# Royaume Koopa : fin', f'function {PF}fl_remove', 'data modify storage mg:kart built2 set value 1b',
              'execute unless data storage mg:kart built3 run schedule function mg:kart/t3/build 3s',
              'tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Circuit Royaume Koopa construit.","color":"green"}]'])
write('build', ['# (OP) Construit le Royaume Koopa : zone chargée, puis construction dès que tous ses chunks sont prêts',
                f'function {PF}fl_add', 'scoreboard players set $kbw2 mg.st 0', f'schedule function {PF}build_wait 20t'])
write('build_wait', ['# Attend que toute la zone soit chargée et générée (5 min au plus), puis construit',
                     f'execute if function {PF}loaded_all run return run function {PF}build_1',
                     'scoreboard players add $kbw2 mg.st 1',
                     'execute if score $kbw2 mg.st matches 300.. run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Royaume Koopa : zone toujours pas chargée, construction annulée.","color":"red"}]',
                     f'schedule function {PF}build_wait 20t'])
lo = ['# Vrai si toute la zone du Royaume Koopa est chargée']
for x in list(range(-HX, HX + 1, 32)) + [HX]:
    for z in list(range(-HZ, HZ + 1, 32)) + [HZ]:
        lo.append(f'execute store success score $kld mg.st unless block {x} {ROAD} {W(z)} minecraft:bedrock')
        lo.append('execute if score $kld mg.st matches 0 run return fail')
lo.append('return 1')
write('loaded_all', lo)
for k, p in enumerate(parts, 1):
    if k < len(parts): p = p + [f'schedule function {PF}build_{k + 1} 2t']
    write(f'build_{k}', p)
for f in os.listdir(OUT):
    if f.startswith('build_') and f[6:-11].isdigit() and int(f[6:-11]) > len(parts): os.remove(os.path.join(OUT, f))

# minimap
MMC, MMR = 24, 15
cells = []
for r in range(MMR):
    row = []
    for c_ in range(MMC):
        x1 = -HX + c_ * (2 * HX + 1) // MMC; x2 = -HX + (c_ + 1) * (2 * HX + 1) // MMC
        z1 = -HZ + r * (2 * HZ + 1) // MMR; z2 = -HZ + (r + 1) * (2 * HZ + 1) // MMR
        kinds = set()
        for x in range(x1, x2):
            for z in range(z1, z2):
                cc = col.get((x, z))
                if cc is None: continue
                if (x, z) in ROADSET: kinds.add('road')
                elif cc['liq'] == 'lava': kinds.add('lava')
                elif cc['liq']: kinds.add('water')
                elif cc['reg'] in ('desert', 'plage') or cc['top'] == 'sand': kinds.add('sand')
                elif cc['reg'] == 'volcan': kinds.add('rock')
                else: kinds.add('grass')
        sx_, sz_ = pts[START]
        if x1 <= sx_ < x2 and z1 <= sz_ < z2: color = 'white'
        elif 'road' in kinds: color = 'gray'
        elif 'lava' in kinds: color = 'gold'
        elif 'water' in kinds: color = 'dark_aqua'
        elif 'sand' in kinds: color = 'yellow'
        elif 'rock' in kinds: color = 'dark_gray'
        elif 'grass' in kinds: color = 'dark_green'
        else: color = 'black'
        row.append('{text:"█",color:"%s"}' % color)
    cells.append('l%d:[%s]' % (r, ','.join(row)))
write('mm_base', ['# Minimap du Royaume Koopa (générée)', 'data modify storage mg:kart base set value {' + ','.join(cells) + '}'])
write('mm_show', ['# Minimap : affiche les 15 lignes dans le tableau de droite (macro, storage mg:kart mm)'] +
      [f'$scoreboard players display name m{r:02d} mg.kmap $(l{r})' for r in range(MMR)])
write('mm_init', ['# Minimap : lignes du tableau (ordre de haut en bas)'] + [f'scoreboard players set m{r:02d} mg.kmap {MMR - r}' for r in range(MMR)])
write('const', ['# Constantes du Royaume Koopa (générées)', f'scoreboard players set $kK mg.st {K}', 'scoreboard players set $kLaps mg.st 3',
                f'scoreboard players set #kmx0 mg.st {HX}', f'scoreboard players set #kmz0 mg.st {ZC - HZ}', f'scoreboard players set #kmc mg.st {MMC}',
                f'scoreboard players set #kmw mg.st {2 * HX + 1}', f'scoreboard players set #kmr mg.st {MMR}', f'scoreboard players set #kmh mg.st {2 * HZ + 1}',
                'scoreboard players set $px mg.st 0', f'scoreboard players set $py mg.st {ROAD + 50}', f'scoreboard players set $pz mg.st {ZC}'] +
      [f'scoreboard players set #h{T} mg.st {T}' for T in sorted(consts)])
print('points de passage', K, '| terrain', len(terrain), '| décor', len(allb), '| étapes', len(parts), '| dangers', HID[0], '| lignes tick', len(tick), '| entités', len(spawn))

# ------------------------------------------------------------------ aperçu PNG
if len(sys.argv) > 2:
    w, hgt, sc = (2 * HX + 1), (2 * HZ + 1), 3
    px = bytearray(w * sc * hgt * sc * 3)
    def rect(x1, y1, x2, y2, rgb):
        for yy in range(max(0, y1), min(hgt * sc, y2 + 1)):
            for xx in range(max(0, x1), min(w * sc, x2 + 1)):
                k = (yy * w * sc + xx) * 3; px[k:k + 3] = bytes(rgb)
    COL = {'grass_block': (95, 160, 60), 'moss_block': (80, 140, 50), 'podzol': (110, 80, 40), 'sand': (225, 210, 150), 'red_sand': (200, 110, 50),
           'stone': (125, 125, 125), 'snow_block': (245, 250, 255), 'blackstone': (45, 40, 50), 'basalt': (70, 70, 75), 'magma_block': (160, 70, 20),
           'black_concrete': (20, 20, 20), 'white_concrete': (235, 235, 235), 'orange_glazed_terracotta': (240, 140, 20), 'lime_concrete': (120, 220, 40),
           'soul_sand': (90, 70, 50), 'spruce_planks': (120, 85, 50), 'nether_bricks': (60, 30, 35)}
    for (x, z), c in col.items():
        if c['liq'] == 'water': rgb = (40, 110, 200)
        elif c['liq'] == 'lava': rgb = (230, 90, 10)
        elif (x, z) in ROADSET: rgb = COL.get(c['top'], (90, 90, 95))
        else: rgb = COL.get(c['top'], (150, 150, 150))
        if c['wall']: rgb = (120, 60, 30)
        if c.get('roof') and (x, z) not in ROADSET: rgb = (60, 30, 35)
        f = 1 + (c['h'] - ROAD) * 0.02
        rgb = tuple(max(0, min(255, int(v * f))) for v in rgb)
        X, Z = (x + HX) * sc, (z + HZ) * sc
        rect(X, Z, X + sc - 1, Z + sc - 1, rgb)
    for (x, z) in occ:
        if (x, z) in col and col[(x, z)]['d'] > WALLD + 1 and not col[(x, z)]['liq']:
            X, Z = (x + HX) * sc, (z + HZ) * sc; rect(X, Z, X + 1, Z + 1, (30, 70, 30))
    for (x, y, z, yw) in CPS:
        X, Z = int((x + HX) * sc), int((z + HZ) * sc); rect(X - 1, Z - 1, X + 1, Z + 1, (255, 255, 0))
    for i in ITEMROWS:
        X, Z = int((pts[i][0] + HX) * sc), int((pts[i][1] + HZ) * sc); rect(X - 3, Z - 3, X + 3, Z + 3, (255, 220, 0))
    raw = b''.join(bytes([0]) + bytes(px[y * w * sc * 3:(y + 1) * w * sc * 3]) for y in range(hgt * sc))
    def chunk(t, d): return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    with open(sys.argv[2], 'wb') as f:
        f.write(bytes([137, 80, 78, 71, 13, 10, 26, 10]) + chunk(b'IHDR', struct.pack('>IIBBBBB', w * sc, hgt * sc, 8, 2, 0, 0, 0))
                + chunk(b'IDAT', zlib.compress(raw, 6)) + chunk(b'IEND', b''))
    print('aperçu', sys.argv[2])
