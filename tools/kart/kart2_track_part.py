# Tracé 3D du circuit (catmull, frame, nearest, hash/bruit, île, région) et palette PAL : exécuté par gen_kart2.py (exec) dans l'ordre des parts.
# Utilise : HX, HZ, ROAD, SEA, math
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
