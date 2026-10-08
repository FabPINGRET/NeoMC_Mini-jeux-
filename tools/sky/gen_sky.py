"""Mini-jeu « Élytra » (id de base 74, mode dans $elm mg.st) : génère data/mg/function/sky/*.mcfunction.

  Mode 1 — Course d'anneaux : 20 anneaux lumineux dans un décor aérien (îles suspendues, falaises
           flottantes, arches, tours, nuages), x -200..200 / z 27600..28400 / y 90..250.
  Mode 2 — Course + combat : même parcours, arc + charges de vent, les touchés sont « sonnés ».
  Mode 3 — Survie en vol : arène séparée centrée (0, 29000), rayon <= 100, y 90..220
           (anneau de pics flottants, obstacles, colonnes de vent), zone qui rétrécit.

Construction asynchrone : le décor est découpé en sections (forceload temporaire, attente du
chargement, construction en plusieurs morceaux, forceload retiré). Tout est déterministe (graine fixe).
Lancer depuis la racine du dépôt : python3 tools/sky/gen_sky.py
"""
import math
import os
import random

OUT = os.path.join('data', 'mg', 'function', 'sky')
SUB = os.path.join(OUT, 'b')
ADV = os.path.join('data', 'mg', 'advancement', 'sky')
NS = 'mg:sky'

files = {}


def W(name, lines):
    files[name] = '\n'.join(lines) + '\n'


# =====================================================================================
# Géométrie : parcours (modes 1-2)
# =====================================================================================
PAD1 = (0, 235, 27640)      # plateforme de départ (dessus du plancher à y 235)
PAD3 = (0, 195, 29000)      # plateforme de décollage de l'arène (mode 3)
PADR = 6                    # rayon des plateformes
# (x, y, z, taille du cadre, type)  type : n normal, b boost (fusée), f arrivée
RINGS = [
    (0, 226, 27700, 9, 'n'),
    (35, 219, 27745, 7, 'n'),
    (85, 213, 27775, 7, 'n'),
    (135, 205, 27815, 9, 'b'),
    (150, 198, 27880, 7, 'n'),
    (110, 193, 27930, 7, 'n'),
    (55, 188, 27955, 9, 'n'),
    (-5, 182, 27975, 7, 'n'),
    (-70, 176, 27990, 9, 'b'),
    (-130, 169, 28030, 7, 'n'),
    (-155, 163, 28090, 7, 'n'),
    (-120, 157, 28140, 9, 'n'),
    (-60, 151, 28160, 7, 'n'),
    (0, 145, 28175, 9, 'b'),
    (60, 139, 28190, 7, 'n'),
    (120, 132, 28220, 7, 'n'),
    (150, 126, 28280, 9, 'n'),
    (115, 120, 28335, 9, 'b'),
    (55, 114, 28360, 7, 'n'),
    (-10, 108, 28350, 9, 'f'),
]
N = len(RINGS)
ZONE = (-205, 88, 27590, 410, 190, 820)          # sortie de zone (x, y, z, dx, dy, dz)
PERCH1 = (0, 250, 27700)
PERCH3 = (0, 222, 28940)
ARENA = (0, 29000)
FLOOR3 = 96                                       # mode 3 : sous ce y = éliminé
RING_COLS = ['pearlescent_froglight', 'verdant_froglight', 'sea_lantern']

PATH = [(PAD1[0], PAD1[1] + 1, PAD1[2])] + [(x, y, z) for x, y, z, _, _ in RINGS]


def axis_of(i):
    """Axe de traversée de l'anneau i (0-based) : 'x' (cadre dans le plan YZ) ou 'z'."""
    a = PATH[i]
    b = PATH[i + 2] if i + 2 < len(PATH) else PATH[i + 1]
    dx, dz = b[0] - a[0], b[2] - a[2]
    return 'x' if abs(dx) >= abs(dz) else 'z'


AXES = [axis_of(i) for i in range(N)]

# =====================================================================================
# Voxels → commandes fill/setblock fusionnées
# =====================================================================================


class Vox:
    def __init__(self):
        self.v = {}

    def put(self, x, y, z, b):
        self.v[(x, y, z)] = b

    def bbox(self):
        xs = [p[0] for p in self.v]; ys = [p[1] for p in self.v]; zs = [p[2] for p in self.v]
        return min(xs), min(ys), min(zs), max(xs), max(ys), max(zs)


def to_cmds(v):
    """Fusion : segments en x → rectangles en z → pavés en y."""
    layers = {}
    for (x, y, z), b in v.items():
        layers.setdefault((y, b), {}).setdefault(z, []).append(x)
    rects = {}
    for (y, b), rows in layers.items():
        runs = {}
        for z, xs in rows.items():
            xs.sort()
            s = p = xs[0]
            for x in xs[1:] + [None]:
                if x is not None and x == p + 1:
                    p = x
                    continue
                runs.setdefault((s, p), []).append(z)
                if x is not None:
                    s = p = x
        for (x0, x1), zs in runs.items():
            zs.sort()
            s = p = zs[0]
            for z in zs[1:] + [None]:
                if z is not None and z == p + 1:
                    p = z
                    continue
                rects.setdefault((x0, x1, s, p, b), []).append(y)
                if z is not None:
                    s = p = z
    out = []
    for (x0, x1, z0, z1, b), ys in rects.items():
        ys.sort()
        s = p = ys[0]
        for y in ys[1:] + [None]:
            if y is not None and y == p + 1 and (x1 - x0 + 1) * (z1 - z0 + 1) * (y - s + 1) <= 32768:
                p = y
                continue
            vol = (x1 - x0 + 1) * (z1 - z0 + 1) * (p - s + 1)
            if vol == 1:
                out.append((vol, s, f'setblock {x0} {s} {z0} minecraft:{b}'))
            else:
                out.append((vol, s, f'fill {x0} {s} {z0} {x1} {p} {z1} minecraft:{b}'))
            if y is not None:
                s = p = y
    # du bas vers le haut (les fleurs/herbes posées après leur support)
    out.sort(key=lambda t: t[1])
    return out


# =====================================================================================
# Formes
# =====================================================================================
STONE_BANDS = ['stone', 'stone', 'andesite', 'stone', 'tuff', 'stone', 'cobblestone', 'andesite']
ORES = ['coal_ore', 'iron_ore', 'copper_ore', 'gold_ore', 'emerald_ore', 'amethyst_block']


def edge(rng):
    p1, p2, p3 = rng.random() * 6.3, rng.random() * 6.3, rng.random() * 6.3
    return lambda t: 1 + 0.14 * math.sin(3 * t + p1) + 0.09 * math.sin(5 * t + p2) + 0.05 * math.sin(9 * t + p3)


def tree(V, x, y, z, rng):
    log, leaf = rng.choice([('oak_log', 'oak_leaves'), ('birch_log', 'birch_leaves'),
                            ('cherry_log', 'cherry_leaves'), ('spruce_log', 'spruce_leaves')])
    h = rng.randint(4, 6)
    for k in range(h):
        V.put(x, y + k, z, log)
    cy = y + h - 1
    for dx in range(-2, 3):
        for dy in range(-1, 3):
            for dz in range(-2, 3):
                if dx * dx + dz * dz + (dy * 1.3) ** 2 <= 6.2 and (dx, dz) != (0, 0) or (dx == 0 and dz == 0 and dy > 0):
                    if (x + dx, cy + dy, z + dz) not in V.v:
                        V.put(x + dx, cy + dy, z + dz, f'{leaf}[persistent=true]')


def island(V, cx, cy, cz, r, rng, depth=None, trees=True, top='grass_block'):
    """Île suspendue : dessus herbeux à cy, cône rocheux irrégulier en dessous."""
    depth = depth or int(r * 1.3) + 3
    f = edge(rng)
    band0 = rng.randint(0, 7)
    tops = []
    for k in range(depth + 1):
        y = cy - k
        t = k / depth
        rad = r * (1 - t) ** 0.75 + 0.6
        if k <= 2:
            rad = r * (1 - 0.04 * k)
        R = int(rad * 1.25) + 2
        for dx in range(-R, R + 1):
            for dz in range(-R, R + 1):
                d = math.hypot(dx, dz)
                if d > rad * f(math.atan2(dz, dx) + k * 0.05):
                    continue
                if k == 0:
                    b = top
                    tops.append((cx + dx, cz + dz, d))
                elif k <= 2:
                    b = 'dirt' if top == 'grass_block' else top
                else:
                    b = STONE_BANDS[(band0 + k // 3) % len(STONE_BANDS)]
                    if rng.random() < 0.012:
                        b = rng.choice(ORES)
                V.put(cx + dx, y, cz + dz, b)
    if top != 'grass_block':
        return
    inner = [t for t in tops if t[2] < r * 0.6]
    rng.shuffle(inner)
    if trees:
        for (x, z, _) in inner[:max(1, r // 6)]:
            tree(V, x, cy + 1, z, rng)
    for (x, z, _) in inner[:int(r * 1.6)]:
        if (x, cy + 1, z) not in V.v:
            V.put(x, cy + 1, z, rng.choice(['short_grass', 'short_grass', 'poppy', 'dandelion', 'cornflower', 'oxeye_daisy']))


def cliff(V, cx, cy0, cz, a, b, H, ang, rng):
    """Falaise flottante : haute lame de roche (ellipse a×b orientée ang), base en pointe."""
    f = edge(rng)
    ca, sa = math.cos(ang), math.sin(ang)
    bands = rng.choice([['stone', 'andesite', 'tuff', 'calcite', 'stone', 'deepslate'],
                        ['terracotta', 'orange_terracotta', 'white_terracotta', 'red_terracotta', 'yellow_terracotta', 'light_gray_terracotta'],
                        ['stone', 'diorite', 'calcite', 'stone', 'andesite', 'dripstone_block']])
    R = int(max(a, b) * 1.3) + 2
    for k in range(H + 1):
        y = cy0 + k
        t = k / H
        s = min(1.0, (t / 0.35) ** 0.7) if t < 0.35 else (1 - 0.15 * (t - 0.35))
        s = max(s, 0.12)
        for dx in range(-R, R + 1):
            for dz in range(-R, R + 1):
                u = (dx * ca + dz * sa) / (a * s)
                w = (-dx * sa + dz * ca) / (b * s)
                if u * u + w * w > f(math.atan2(w, u) + k * 0.08) ** 2:
                    continue
                if k == H:
                    blk = 'grass_block'
                elif k >= H - 2:
                    blk = 'dirt'
                else:
                    blk = bands[(k // 4) % len(bands)]
                V.put(cx + dx, y, cz + dz, blk)
    for _ in range(2):
        tree(V, cx + rng.randint(-2, 2), cy0 + H + 1, cz + rng.randint(-1, 1), rng)


def tower(V, cx, cy0, cz, r, H, rng):
    """Tour flottante en pierre, base rocheuse en pointe, toit conique."""
    island(V, cx, cy0 - 1, cz, r + 3, rng, depth=r + 9, trees=False, top='stone')
    for k in range(H):
        y = cy0 + k
        for dx in range(-r, r + 1):
            for dz in range(-r, r + 1):
                d = math.hypot(dx, dz)
                if d > r + 0.4:
                    continue
                blk = 'stone_bricks'
                if d > r - 0.7:
                    if k % 9 == 4 and (dx == 0 or dz == 0):
                        blk = 'sea_lantern'
                    elif rng.random() < 0.18:
                        blk = rng.choice(['mossy_stone_bricks', 'cracked_stone_bricks'])
                V.put(cx + dx, y, cz + dz, blk)
    top = cy0 + H
    for dx in range(-r - 1, r + 2):
        for dz in range(-r - 1, r + 2):
            d = math.hypot(dx, dz)
            if d <= r + 1.4:
                V.put(cx + dx, top, cz + dz, 'polished_andesite')
                if d > r + 0.4 and (dx + dz) % 2 == 0:
                    V.put(cx + dx, top + 1, cz + dz, 'stone_brick_wall')
    for k in range(r + 4):
        rad = (r + 1) * (1 - k / (r + 4))
        for dx in range(-r - 1, r + 2):
            for dz in range(-r - 1, r + 2):
                if math.hypot(dx, dz) <= rad + 0.3:
                    V.put(cx + dx, top + 2 + k, cz + dz, 'deepslate_tiles')
    V.put(cx, top + r + 6, cz, 'glowstone')
    V.put(cx, top + r + 7, cz, 'lightning_rod')


def arch(V, cx, cy, cz, ax, R, rng):
    """Arche (demi-cercle de rayon R) dans le plan de l'anneau, pieds en rochers flottants."""
    mats = ['smooth_sandstone', 'cut_sandstone', 'smooth_sandstone', 'chiseled_sandstone']
    pts = set()
    for i in range(0, 181):
        t = math.radians(i)
        u, h = R * math.cos(t), R * math.sin(t)
        for du in range(-2, 3):
            for dh in range(-2, 3):
                for dw in range(-1, 2):
                    if du * du + dh * dh + dw * dw * 2 <= 5:
                        pts.add((round(u + du), round(h + dh), dw))
    for leg in (-R, R):
        for k in range(1, 9):
            for du in range(-2, 3):
                for dw in range(-1, 2):
                    if du * du + dw * dw * 2 <= 5:
                        pts.add((leg + du, -k, dw))
    for (u, h, w) in pts:
        blk = mats[(abs(h) // 3) % len(mats)]
        if h == R + 2 and abs(u) <= 1:
            blk = 'glowstone'
        if ax == 'x':
            V.put(cx + w, cy + h, cz + u, blk)
        else:
            V.put(cx + u, cy + h, cz + w, blk)
    for leg in (-R, R):
        if ax == 'x':
            island(V, cx, cy - 9, cz + leg, 4, rng, depth=7, trees=False, top='smooth_sandstone')
        else:
            island(V, cx + leg, cy - 9, cz, 4, rng, depth=7, trees=False, top='smooth_sandstone')


def cloud(V, cx, cy, cz, rng):
    for _ in range(rng.randint(4, 7)):
        ox, oz, oy = rng.randint(-9, 9), rng.randint(-6, 6), rng.randint(-1, 1)
        rx, rz, ry = rng.randint(4, 7), rng.randint(3, 5), rng.randint(1, 2)
        for dx in range(-rx, rx + 1):
            for dy in range(-ry, ry + 1):
                for dz in range(-rz, rz + 1):
                    if (dx / rx) ** 2 + (dy / (ry + .5)) ** 2 + (dz / rz) ** 2 <= 1:
                        V.put(cx + ox + dx, cy + oy + dy, cz + oz + dz, 'white_wool')


def ring(V, i):
    x, y, z, size, kind = RINGS[i]
    h = size // 2
    ax = AXES[i]
    for a in range(-h, h + 1):
        for b in range(-h, h + 1):
            if max(abs(a), abs(b)) != h:
                continue
            corner = abs(a) == h and abs(b) == h
            mid = a == 0 or b == 0
            if kind == 'b':
                blk = 'ochre_froglight' if (corner or mid) else 'gold_block'
            elif kind == 'f':
                blk = 'sea_lantern' if (a + b) % 2 == 0 else 'black_concrete'
            else:
                blk = RING_COLS[i % 3] if not corner else 'crying_obsidian'
            if ax == 'x':
                V.put(x, y + a, z + b, blk)
            else:
                V.put(x + b, y + a, z, blk)


def spike(V, cx, cy, cz, r, H, up, rng):
    """Pic de glace flottant (up : pointe vers le haut, sinon suspendu pointe en bas)."""
    for k in range(H + 1):
        t = k / H
        rad = r * (1 - t) ** 1.1 + 0.3
        y = cy + k if up else cy - k
        blk = 'packed_ice' if t < 0.45 else ('blue_ice' if t < 0.85 else 'snow_block')
        R = int(rad) + 1
        for dx in range(-R, R + 1):
            for dz in range(-R, R + 1):
                if math.hypot(dx, dz) <= rad:
                    V.put(cx + dx, y, cz + dz, blk)
    if up:
        island(V, cx, cy - 1, cz, r + 2, rng, depth=r + 5, trees=False, top='stone')
    else:
        for dx in range(-r - 1, r + 2):
            for dz in range(-r - 1, r + 2):
                if math.hypot(dx, dz) <= r + 1.2:
                    V.put(cx + dx, cy + 1, cz + dz, 'snow_block')


def pillar(V, cx, cy0, cz, H, rng):
    for k in range(H):
        for dx in range(-2, 3):
            for dz in range(-2, 3):
                if dx * dx + dz * dz <= 5:
                    blk = 'prismarine_bricks' if (k // 5) % 2 == 0 else 'dark_prismarine'
                    if k % 10 == 7 and dx * dx + dz * dz >= 4:
                        blk = 'sea_lantern'
                    V.put(cx + dx, cy0 + k, cz + dz, blk)
    for dx in range(-3, 4):
        for dz in range(-3, 4):
            if dx * dx + dz * dz <= 10:
                V.put(cx + dx, cy0 - 1, cz + dz, 'dark_prismarine')
                V.put(cx + dx, cy0 + H, cz + dz, 'dark_prismarine')
    V.put(cx, cy0 + H + 1, cz, 'sea_lantern')


# Colonnes de vent (mode 3) : (x, z) ; base y 98, sommet y 205
COLS = [(round(ARENA[0] + 46 * math.cos(math.radians(a))), round(ARENA[1] + 46 * math.sin(math.radians(a))))
        for a in (18, 90, 162, 234, 306)]
COL_Y0, COL_Y1, COL_R = 98, 205, 3


def wind_column(V, cx, cz):
    for dx in range(-5, 6):
        for dz in range(-5, 6):
            d = math.hypot(dx, dz)
            if d <= 5.3:
                blk = 'waxed_oxidized_cut_copper'
                if 3.5 < d <= 4.6:
                    blk = 'waxed_copper_grate'
                if d <= 1.2:
                    blk = 'sea_lantern'
                V.put(cx + dx, COL_Y0 - 1, cz + dz, blk)
            if d <= 4.3:
                V.put(cx + dx, COL_Y0 - 2, cz + dz, 'waxed_oxidized_copper')
            if 4.4 < d <= 5.4 and (dx + dz) % 3 == 0:
                V.put(cx + dx, COL_Y0, cz + dz, 'waxed_oxidized_copper_bulb[lit=true]')
            if 4.4 < d <= 5.4:
                V.put(cx + dx, COL_Y1, cz + dz, 'white_stained_glass')
    for k in range(1, 6):
        for dx, dz in ((5, 0), (-5, 0), (0, 5), (0, -5)):
            V.put(cx + dx, COL_Y1 + k - 6, cz + dz, 'iron_chain')


# =====================================================================================
# Placement du décor (graine fixe), avec dégagement autour de la trajectoire
# =====================================================================================
rng = random.Random(7431)


def seg_dist(p, a, b):
    ax_, ay, az = a; bx, by, bz = b; px, py, pz = p
    vx, vy, vz = bx - ax_, by - ay, bz - az
    L = vx * vx + vy * vy + vz * vz
    t = max(0, min(1, ((px - ax_) * vx + (py - ay) * vy + (pz - az) * vz) / L)) if L else 0
    return math.dist(p, (ax_ + vx * t, ay + vy * t, az + vz * t))


def path_dist(p):
    return min(seg_dist(p, PATH[i], PATH[i + 1]) for i in range(len(PATH) - 1))


def box_path_clear(bb, margin):
    """Aucun voxel de la boîte englobante (échantillonnée) à moins de margin de la trajectoire."""
    x0, y0, z0, x1, y1, z1 = bb
    for x in range(x0, x1 + 1, 3):
        for y in range(y0, y1 + 1, 3):
            for z in range(z0, z1 + 1, 3):
                if path_dist((x, y, z)) < margin:
                    return False
    return True


features = []   # (nom, Vox, zone 'c' parcours / 'a' arène)


def add_feature(name, fn, zone, check=True, margin=9, tries=1):
    V = Vox()
    fn(V)
    bb = V.bbox()
    if zone == 'c':
        if bb[0] < -200 or bb[3] > 200 or bb[2] < 27600 or bb[5] > 28400 or bb[1] < 90 or bb[4] > 250:
            return False
    else:
        if bb[1] < 90 or bb[4] > 220 or math.hypot(max(abs(bb[0]), abs(bb[3])), max(abs(bb[2] - ARENA[1]), abs(bb[5] - ARENA[1]))) > 101 * 1.42:
            return False
        if max(abs(bb[0]), abs(bb[3])) > 100 or max(abs(bb[2] - ARENA[1]), abs(bb[5] - ARENA[1])) > 100:
            return False
    for (_, W2, _) in features:
        b2 = W2.bbox()
        if not (bb[3] + 3 < b2[0] or b2[3] + 3 < bb[0] or bb[4] + 3 < b2[1] or b2[4] + 3 < bb[1] or bb[5] + 3 < b2[2] or b2[5] + 3 < bb[2]):
            if check:
                return False
    if zone == 'c' and check and not box_path_clear(bb, margin):
        return False
    features.append((name, V, zone))
    return True


# Anneaux (toujours)
for i in range(N):
    add_feature(f'anneau {i+1}', lambda V, i=i: ring(V, i), 'c', check=False)
# Île sous la plateforme de départ (plus petite que la plateforme : on tombe dans le vide en sautant)
add_feature('socle départ', lambda V: island(V, PAD1[0], PAD1[1] - 1, PAD1[2], 5, rng, depth=14, trees=False, top='stone'), 'c', check=False)
# Arches autour de quelques anneaux (plan de l'anneau)
for i in (2, 7, 12, 18):
    x, y, z, size, _ = RINGS[i]
    add_feature(f'arche {i+1}', lambda V, x=x, y=y, z=z, i=i: arch(V, x, y - 2, z, AXES[i], 13, rng), 'c', check=False)

# Îles suspendues bien visibles sous/à côté de la trajectoire
placed = 0
for _ in range(4000):
    if placed >= 14:
        break
    i = rng.randrange(N)
    x, y, z, _, _ = RINGS[i]
    r = rng.randint(8, 15)
    px, pz = x + rng.randint(-40, 40), z + rng.randint(-40, 40)
    py = y + rng.randint(-34, -14)
    if add_feature('île', lambda V: island(V, px, py, pz, r, rng), 'c', margin=r * 0.4 + 8):
        placed += 1
placed = 0
for _ in range(4000):
    if placed >= 6:
        break
    x, z = rng.randint(-185, 185), rng.randint(27630, 28380)
    a, b, H = rng.randint(10, 16), rng.randint(4, 7), rng.randint(45, 75)
    y0 = rng.randint(95, 150)
    if add_feature('falaise', lambda V: cliff(V, x, y0, z, a, b, H, rng.random() * 3.14, rng), 'c', margin=10):
        placed += 1
placed = 0
for _ in range(4000):
    if placed >= 4:
        break
    x, z = rng.randint(-180, 180), rng.randint(27640, 28370)
    r, H = rng.randint(3, 5), rng.randint(30, 55)
    y0 = rng.randint(110, 160)
    if add_feature('tour', lambda V: tower(V, x, y0, z, r, H, rng), 'c', margin=10):
        placed += 1
placed = 0
for _ in range(4000):
    if placed >= 9:
        break
    x, z, y = rng.randint(-185, 185), rng.randint(27620, 28385), rng.randint(140, 240)
    if add_feature('nuage', lambda V: cloud(V, x, y, z, rng), 'c', margin=9):
        placed += 1

# ---- Arène (mode 3)
for (cx, cz) in COLS:
    add_feature('colonne de vent', lambda V, cx=cx, cz=cz: wind_column(V, cx, cz), 'a', check=False)
for k in range(16):
    ang = math.radians(k * 22.5 + rng.uniform(-6, 6))
    rad = rng.uniform(80, 90)
    x, z = round(ARENA[0] + rad * math.cos(ang)), round(ARENA[1] + rad * math.sin(ang))
    if k % 2 == 0:
        add_feature('pic', lambda V, x=x, z=z: spike(V, x, rng.randint(105, 140), z, rng.randint(4, 6), rng.randint(32, 55), True, rng), 'a', check=False)
    else:
        add_feature('pic suspendu', lambda V, x=x, z=z: spike(V, x, rng.randint(195, 212), z, rng.randint(4, 6), rng.randint(30, 50), False, rng), 'a', check=False)
placed = 0
for _ in range(4000):
    if placed >= 8:
        break
    ang, rad = rng.random() * 6.283, rng.uniform(24, 64)
    x, z = round(ARENA[0] + rad * math.cos(ang)), round(ARENA[1] + rad * math.sin(ang))
    if min(math.hypot(x - cx, z - cz) for cx, cz in COLS) < 16:
        continue
    r, y = rng.randint(5, 9), rng.randint(115, 180)
    if add_feature('rocher', lambda V: island(V, x, y, z, r, rng), 'a'):
        placed += 1
placed = 0
for _ in range(4000):
    if placed >= 4:
        break
    ang, rad = rng.random() * 6.283, rng.uniform(26, 70)
    x, z = round(ARENA[0] + rad * math.cos(ang)), round(ARENA[1] + rad * math.sin(ang))
    if min(math.hypot(x - cx, z - cz) for cx, cz in COLS) < 12:
        continue
    if add_feature('pilier', lambda V: pillar(V, x, rng.randint(110, 140), z, rng.randint(28, 45), rng), 'a'):
        placed += 1

# =====================================================================================
# Sections de construction
# =====================================================================================
CELL = 96
sections = {}
for (name, V, zone) in features:
    bb = V.bbox()
    key = (zone, (bb[0] + bb[3]) // 2 // CELL, (bb[2] + bb[5]) // 2 // CELL)
    sections.setdefault(key, []).append((name, V))


def sec_order(k):
    zone, gx, gz = k
    return (0 if zone == 'c' else 1, gz, gx)


sec_keys = sorted(sections, key=sec_order)
steps_b, steps_w = [], []
stats = []
PART_VOL = 14000
os.makedirs(SUB, exist_ok=True)
for si, key in enumerate(sec_keys):
    feats = sections[key]
    merged = Vox()
    for (_, V) in feats:
        merged.v.update(V.v)
    bbs = [V.bbox() for (_, V) in feats]
    x0, z0 = min(b[0] for b in bbs), min(b[2] for b in bbs)
    x1, z1 = max(b[3] for b in bbs), max(b[5] for b in bbs)
    nch = ((x1 >> 4) - (x0 >> 4) + 1) * ((z1 >> 4) - (z0 >> 4) + 1)
    assert nch <= 256, (key, nch)
    W(f'b/fl{si}', [f'# Section {si} : chargement temporaire ({", ".join(sorted(set(n for n, _ in feats)))})',
                   f'forceload add {x0} {z0} {x1} {z1}', 'return 1'])
    ld = [f'# Section {si} : 1 quand tous les tronçons sont chargés']
    for cx in range(x0 >> 4, (x1 >> 4) + 1):
        for cz in range(z0 >> 4, (z1 >> 4) + 1):
            ld.append(f'execute unless loaded {cx * 16 + 8} 100 {cz * 16 + 8} run return 0')
    ld.append('return 1')
    W(f'b/ld{si}', ld)
    W(f'b/rm{si}', [f'forceload remove {x0} {z0} {x1} {z1}', 'return 1'])
    cmds = to_cmds(merged.v)
    parts, cur, vol = [], [], 0
    for (v, _, c) in cmds:
        if cur and (vol + v > PART_VOL or len(cur) >= 250):
            parts.append(cur)
            cur, vol = [], 0
        cur.append(c)
        vol += v
    if cur:
        parts.append(cur)
    steps_b += [f'b/fl{si}', f'b/ld{si}']
    for pi, p in enumerate(parts):
        W(f'b/s{si}_{pi}', [f'# Section {si}, morceau {pi + 1}/{len(parts)} (généré)'] + p + ['return 1'])
        steps_b.append(f'b/s{si}_{pi}')
    steps_b.append(f'b/rm{si}')
    wipe = [f'# Section {si} : effacement du décor (boîtes englobantes)']
    for (_, V) in feats:
        a0, b0, c0, a1, b1, c1 = V.bbox()
        h = max(1, 32768 // ((a1 - a0 + 1) * (c1 - c0 + 1)))
        y = b0
        while y <= b1:
            wipe.append(f'fill {a0} {y} {c0} {a1} {min(b1, y + h - 1)} {c1} minecraft:air')
            y += h
    W(f'b/w{si}', wipe + ['return 1'])
    steps_w += [f'b/fl{si}', f'b/ld{si}', f'b/w{si}', f'b/rm{si}']
    stats.append((si, key, len(cmds), len(parts), nch, len(merged.v)))

W('b_step', ['# Étape courante de la construction ($skbs) — renvoie 1 si terminée, 0 s\'il faut attendre (généré)']
  + [f'execute if score $skbs mg.st matches {i} run return run function {NS}/{s}' for i, s in enumerate(steps_b)] + ['return 1'])
W('w_step', ['# Étape courante de l\'effacement ($skbs) — renvoie 1 si terminée, 0 s\'il faut attendre (généré)']
  + [f'execute if score $skbs mg.st matches {i} run return run function {NS}/{s}' for i, s in enumerate(steps_w)] + ['return 1'])
W('fl_secs_off', ['# Retire tous les chargements temporaires des sections (construction interrompue)']
  + [f'function {NS}/b/rm{si}' for si in range(len(sec_keys))])

# =====================================================================================
# Fonctions de jeu
# =====================================================================================
ELY = 'minecraft:elytra[minecraft:custom_data={mg_sky:1b},minecraft:unbreakable={},minecraft:enchantments={"minecraft:binding_curse":1},minecraft:custom_name={"text":"Élytres du ciel","color":"aqua","italic":false}]'
ROCK = 'minecraft:firework_rocket[minecraft:custom_data={mg_sky:1b},minecraft:fireworks={flight_duration:1},minecraft:custom_name={"text":"Fusée du ciel","color":"gold","italic":false}]'
BOW = 'minecraft:bow[minecraft:custom_data={mg_sky:1b},minecraft:unbreakable={},minecraft:enchantments={"minecraft:infinity":1},minecraft:custom_name={"text":"Arc du ciel","color":"red","italic":false}]'
ARROW = 'minecraft:arrow[minecraft:custom_data={mg_sky:1b}]'
WIND = 'minecraft:wind_charge[minecraft:custom_data={mg_sky:1b},minecraft:custom_name={"text":"Charge de vent","color":"aqua","italic":false}]'
SKYITEM = '*[minecraft:custom_data~{mg_sky:1b}]'
ADM = '[{"text":"[Mini-Jeux] ","color":"gold"},{"text":"%s","color":"%s"}]'

W('load', ['# Élytra : objectifs (à appeler depuis core/load)',
           'scoreboard objectives add mg.skr dummy [{"text":"🪽 Anneaux","color":"aqua","bold":true}]',
           'scoreboard objectives add mg.sks dummy [{"text":"🪽 Survivants","color":"aqua","bold":true}]',
           'scoreboard objectives add mg.skg dummy',
           'scoreboard objectives add mg.skst dummy',
           'scoreboard objectives add mg.skl dummy',
           'scoreboard objectives add mg.sko dummy'])
W('remove', ['# Élytra : désinstallation (à appeler depuis mg:desinstaller)',
             'scoreboard objectives remove mg.skr',
             'scoreboard objectives remove mg.sks',
             'scoreboard objectives remove mg.skg',
             'scoreboard objectives remove mg.skst',
             'scoreboard objectives remove mg.skl',
             'scoreboard objectives remove mg.sko',
             f'schedule clear {NS}/b_next',
             f'schedule clear {NS}/pad_wait',
             f'function {NS}/fl_secs_off',
             f'function {NS}/pad_fl_off',
             'data remove storage mg:sky built',
             'data remove storage mg:sky z',
             'advancement revoke @a only mg:sky/hurt'])

# ---- construction asynchrone
W('build', ['# (OP) Construit le parcours Élytra (modes 1-2) et l\'arène de survie (mode 3), section par section (asynchrone)',
            f'execute if score $skbm mg.st matches 1.. run return run tellraw @a[tag=mg.admin] {ADM % ("Élytra : construction déjà en cours.", "yellow")}',
            'scoreboard players set $skbm mg.st 1',
            'scoreboard players set $skbs mg.st 0',
            'scoreboard players set $skw mg.st 0',
            f'scoreboard players set $skbn mg.st {len(steps_b)}',
            f'tellraw @a[tag=mg.admin] {ADM % ("Élytra : construction du décor (" + str(len(sec_keys)) + " sections)...", "gray")}',
            f'schedule function {NS}/b_next 1t'])
W('wipe', ['# (OP) Efface tout le décor Élytra (pour reconstruire après une modification du générateur)',
           f'execute if score $skbm mg.st matches 1.. run return run tellraw @a[tag=mg.admin] {ADM % ("Élytra : construction en cours, réessaie plus tard.", "yellow")}',
           'data remove storage mg:sky built',
           'scoreboard players set $skbm mg.st 2',
           'scoreboard players set $skbs mg.st 0',
           'scoreboard players set $skw mg.st 0',
           f'scoreboard players set $skbn mg.st {len(steps_w)}',
           f'schedule function {NS}/b_next 1t'])
W('b_next', ['# Construction / effacement : une étape par tick (attente du chargement des tronçons)',
             'scoreboard players set $skok mg.st 0',
             f'execute if score $skbm mg.st matches 1 store result score $skok mg.st run function {NS}/b_step',
             f'execute if score $skbm mg.st matches 2 store result score $skok mg.st run function {NS}/w_step',
             'execute if score $skok mg.st matches 1 run scoreboard players set $skw mg.st 0',
             'execute if score $skok mg.st matches 1 run scoreboard players add $skbs mg.st 1',
             'execute if score $skok mg.st matches 0 run scoreboard players add $skw mg.st 1',
             f'execute if score $skw mg.st matches 400.. run return run function {NS}/b_fail',
             f'execute if score $skbs mg.st >= $skbn mg.st run return run function {NS}/b_done',
             f'schedule function {NS}/b_next 1t'])
W('b_done', ['# Fin de la construction (ou de l\'effacement)',
             f'function {NS}/fl_secs_off',
             'execute if score $skbm mg.st matches 1 run data modify storage mg:sky built set value 1b',
             f'execute if score $skbm mg.st matches 1 run tellraw @a[tag=mg.admin] {ADM % ("Élytra : parcours d\'anneaux et arène de survie construits.", "green")}',
             f'execute if score $skbm mg.st matches 2 run tellraw @a[tag=mg.admin] {ADM % ("Élytra : décor effacé.", "gray")}',
             'scoreboard players set $skbm mg.st 0'])
W('b_fail', ['# Zone jamais chargée : abandon propre',
             f'function {NS}/fl_secs_off',
             'scoreboard players set $skbm mg.st 0',
             f'tellraw @a[tag=mg.admin] {ADM % ("Élytra : zone pas chargée, construction interrompue (relance mg:sky/build).", "red")}'])

# ---- plateformes de départ
def disc(cx, cy, cz, r, blk_fn):
    V = Vox()
    for dx in range(-r - 2, r + 3):
        for dz in range(-r - 2, r + 3):
            d = math.hypot(dx, dz)
            b = blk_fn(d, dx, dz)
            if b:
                V.put(cx + dx, cy, cz + dz, b)
    return V


def pad_lines(c, floor_fn, title):
    cx, cy, cz = c
    V = disc(cx, cy, cz, PADR, floor_fn)
    for y in range(cy + 1, cy + 4):
        for dx in range(-PADR - 2, PADR + 3):
            for dz in range(-PADR - 2, PADR + 3):
                if PADR + 0.5 < math.hypot(dx, dz) <= PADR + 1.5:
                    V.put(cx + dx, y, cz + dz, 'barrier')
    return [f'# {title} (généré)', f'fill {cx-PADR-2} {cy} {cz-PADR-2} {cx+PADR+2} {cy+5} {cz+PADR+2} minecraft:air'] + [c for _, _, c in to_cmds(V.v)]


def pad1_floor(d, dx, dz):
    if d > PADR + 0.5:
        return None
    if d <= 1.2:
        return 'sea_lantern'
    if 3.5 < d <= 4.5:
        return 'light_blue_concrete'
    if d > PADR - 0.5:
        return 'quartz_bricks'
    return 'smooth_quartz'


def pad3_floor(d, dx, dz):
    if d > PADR + 0.5:
        return None
    if d <= 1.2:
        return 'sea_lantern'
    if 3.5 < d <= 4.5:
        return 'cyan_stained_glass'
    if d > PADR - 0.5:
        return 'waxed_oxidized_cut_copper'
    return 'light_blue_stained_glass'


W('pad1', pad_lines(PAD1, pad1_floor, 'Plateforme de départ de la course (sol + barrière)'))
W('pad3', pad_lines(PAD3, pad3_floor, 'Plateforme de décollage de l\'arène (sol + barrière)'))
for nm, (cx, cy, cz) in (('pad1', PAD1), ('pad3', PAD3)):
    W(f'{nm}_open', [f'# Barrière retirée (GO)', f'fill {cx-PADR-2} {cy+1} {cz-PADR-2} {cx+PADR+2} {cy+3} {cz+PADR+2} minecraft:air replace minecraft:barrier'])
    W(f'{nm}_ld', ['# 1 si la plateforme est chargée'] +
      [f'execute unless loaded {cx+a} {cy} {cz+b} run return fail' for a in (-8, 8) for b in (-8, 8)] + ['return 1'])
cx, cy, cz = PAD3
W('pad3_off', ['# Mode 3 : la plateforme de décollage s\'effondre',
               f'fill {cx-PADR-2} {cy} {cz-PADR-2} {cx+PADR+2} {cy+3} {cz+PADR+2} minecraft:air',
               f'particle minecraft:cloud {cx} {cy} {cz} 4 0.5 4 0.05 120 force @a',
               f'execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.glass.break master @s ~ ~ ~ 1 0.7',
               'scoreboard players set $skpo mg.st 0',
               'title @a[tag=mg.play] actionbar [{"text":"La plateforme s\'est effondrée : reste en l\'air !","color":"red"}]'])
FL1 = f'{PAD1[0]-16} {PAD1[2]-16} {PAD1[0]+16} {PAD1[2]+16}'
FL3 = f'{PAD3[0]-16} {PAD3[2]-16} {PAD3[0]+16} {PAD3[2]+16}'
W('pad_fl_off', ['# Chargements temporaires des plateformes retirés', f'forceload remove {FL1}', f'forceload remove {FL3}'])

r1 = RINGS[0]
W('pad_wait', ['# Attend le chargement de la plateforme du mode puis y place les joueurs',
               'execute unless score $game mg.st matches 74 run return 0',
               'execute unless score $state mg.st matches 1..2 run return 0',
               f'execute if score $elm mg.st matches 1..2 if function {NS}/pad1_ld run return run function {NS}/pad_place',
               f'execute if score $elm mg.st matches 3 if function {NS}/pad3_ld run return run function {NS}/pad_place',
               'scoreboard players add $skpw mg.st 1',
               f'execute if score $skpw mg.st matches 60.. run return run function {NS}/pad_place',
               f'schedule function {NS}/pad_wait 2t'])
DISPT = 'transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[%sf,%sf,%sf]}'
W('pad_place', ['# Plateforme posée, joueurs répartis dessus (gelés par le compte à rebours)',
                'scoreboard players set $skpd mg.st 1',
                'kill @e[tag=mg.sky]',
                f'execute if score $elm mg.st matches 1..2 run function {NS}/pad1',
                f'execute if score $elm mg.st matches 3 run function {NS}/pad3',
                'scoreboard players set $skok mg.st 0',
                f'execute if score $elm mg.st matches 1..2 store success score $skok mg.st run spreadplayers {PAD1[0]} {PAD1[2]} 1 4 under {PAD1[1]+2} false @a[tag=mg.play]',
                f'execute if score $elm mg.st matches 3 store success score $skok mg.st run spreadplayers {PAD3[0]} {PAD3[2]} 1 4 under {PAD3[1]+2} false @a[tag=mg.play]',
                f'execute if score $skok mg.st matches 0 if score $elm mg.st matches 1..2 run tp @a[tag=mg.play] {PAD1[0]+.5} {PAD1[1]+1} {PAD1[2]+.5}',
                f'execute if score $skok mg.st matches 0 if score $elm mg.st matches 3 run tp @a[tag=mg.play] {PAD3[0]+.5} {PAD3[1]+1} {PAD3[2]+.5}',
                f'execute if score $elm mg.st matches 1..2 as @a[tag=mg.play] at @s run tp @s ~ ~ ~ facing {r1[0]+.5} {r1[1]+.5} {r1[2]+.5}',
                f'execute if score $elm mg.st matches 3 as @a[tag=mg.play] at @s run tp @s ~ ~ ~ facing {PAD3[0]+.5} {PAD3[1]-10} {PAD3[2]+60}',
                f'execute if score $elm mg.st matches 1..2 run spawnpoint @a[tag=mg.play] {PAD1[0]} {PAD1[1]+1} {PAD1[2]}',
                f'execute if score $elm mg.st matches 3 run spawnpoint @a[tag=mg.play] {PAD3[0]} {PAD3[1]+1} {PAD3[2]}',
                f'execute if score $elm mg.st matches 1 run summon minecraft:text_display {PAD1[0]+.5} {PAD1[1]+5} {PAD1[2]+.5} {{Tags:["mg.fx","mg.sky"],billboard:"center",background:0,text:[{{"text":"🪽 COURSE D\'ANNEAUX","color":"aqua","bold":true}},{{"text":"\\n{N} anneaux dans l\'ordre — suis la traînée lumineuse","color":"gray","bold":false}}],{DISPT % (1.3, 1.3, 1.3)}}}',
                f'execute if score $elm mg.st matches 2 run summon minecraft:text_display {PAD1[0]+.5} {PAD1[1]+5} {PAD1[2]+.5} {{Tags:["mg.fx","mg.sky"],billboard:"center",background:0,text:[{{"text":"🏹 COURSE + COMBAT","color":"red","bold":true}},{{"text":"\\n{N} anneaux — abats tes rivaux à l\'arc et à la charge de vent","color":"gray","bold":false}}],{DISPT % (1.3, 1.3, 1.3)}}}',
                f'execute if score $elm mg.st matches 3 run summon minecraft:text_display {PAD3[0]+.5} {PAD3[1]+5} {PAD3[2]+.5} {{Tags:["mg.fx","mg.sky"],billboard:"center",background:0,text:[{{"text":"🌪 SURVIE EN VOL","color":"light_purple","bold":true}},{{"text":"\\nNe te pose jamais — reste dans la zone","color":"gray","bold":false}}],{DISPT % (1.3, 1.3, 1.3)}}}'])

# ---- préparation / départ
W('prepare', ['# Élytra — préparation ($elm : 1 course d\'anneaux, 2 course + combat, 3 survie en vol)',
              'execute unless score $elm mg.st matches 1..3 run scoreboard players set $elm mg.st 1',
              f'execute unless data storage mg:sky {{built:1b}} run tellraw @a [{{"text":"🪽 Le décor Élytra n\'est pas encore construit : il apparaît pendant la partie (les anneaux comptent déjà).","color":"yellow"}}]',
              f'execute unless data storage mg:sky {{built:1b}} run function {NS}/build',
              'scoreboard players set #-1 mg.st -1',
              'scoreboard players set #2 mg.st 2',
              'scoreboard players set #5 mg.st 5',
              'scoreboard players set #10 mg.st 10',
              'scoreboard players set #11 mg.st 11',
              'scoreboard players set #20 mg.st 20',
              'scoreboard players set #72 mg.st 72',
              'scoreboard players set #160 mg.st 160',
              'scoreboard players reset * mg.skr',
              'scoreboard players reset * mg.sks',
              'scoreboard players reset * mg.skst',
              'scoreboard players reset * mg.skl',
              'scoreboard players reset * mg.sko',
              'tag @a remove mg.skf',
              'tag @a remove mg.skstun',
              'tag @a remove mg.skak',
              'tag @a remove mg.skv',
              'tag @a remove mg.skw',
              'execute if score $elm mg.st matches 1..2 run scoreboard players set @a[tag=mg.play] mg.skr 0',
              'execute if score $elm mg.st matches 3 run scoreboard players set @a[tag=mg.play] mg.sks 0',
              'scoreboard players set @a[tag=mg.play] mg.skg -40',
              'scoreboard players set @a[tag=mg.play] mg.skst 0',
              'scoreboard players set @a[tag=mg.play] mg.skl 0',
              'scoreboard players set @a[tag=mg.play] mg.sko 0',
              'scoreboard players set $skt mg.st 0',
              'scoreboard players set $skpd mg.st 0',
              'scoreboard players set $skpw mg.st 0',
              'scoreboard players set $skpo mg.st 1',
              'advancement revoke @a only mg:sky/hurt',
              f'execute if score $elm mg.st matches 1..2 run scoreboard players set $px mg.st {PERCH1[0]}',
              f'execute if score $elm mg.st matches 1..2 run scoreboard players set $py mg.st {PERCH1[1]}',
              f'execute if score $elm mg.st matches 1..2 run scoreboard players set $pz mg.st {PERCH1[2]}',
              f'execute if score $elm mg.st matches 3 run scoreboard players set $px mg.st {PERCH3[0]}',
              f'execute if score $elm mg.st matches 3 run scoreboard players set $py mg.st {PERCH3[1]}',
              f'execute if score $elm mg.st matches 3 run scoreboard players set $pz mg.st {PERCH3[2]}',
              'gamemode adventure @a[tag=mg.play]',
              'clear @a[tag=mg.play]',
              'effect clear @a[tag=mg.play] minecraft:levitation',
              f'item replace entity @a[tag=mg.play] armor.chest with {ELY}',
              f'execute if score $elm mg.st matches 1..2 run forceload add {FL1}',
              f'execute if score $elm mg.st matches 3 run forceload add {FL3}',
              f'schedule function {NS}/pad_wait 2t'])

RULES = {
    1: f'[{{"text":"🪽 COURSE D\'ANNEAUX : ","color":"aqua","bold":true}},{{"text":"saute, ouvre tes élytres (Espace en l\'air) et traverse les {N} anneaux DANS L\'ORDRE — la traînée lumineuse montre le suivant. Anneaux dorés = +1 fusée. Le premier arrivé gagne (4 min max).","color":"gray","bold":false}}]',
    2: f'[{{"text":"🏹 COURSE + COMBAT : ","color":"red","bold":true}},{{"text":"même course de {N} anneaux, mais arc et charges de vent (rechargées toutes les 15 s) ! Un rival touché est sonné : ses élytres disparaissent 1,5 s. Personne ne meurt. Le premier arrivé gagne.","color":"gray","bold":false}}]',
    3: '[{"text":"🌪 SURVIE EN VOL : ","color":"light_purple","bold":true},{"text":"reste en l\'air ! Te poser, tomber sous l\'arène ou rester 3 s hors de la zone (cercle rouge qui rétrécit) = éliminé. Une fusée toutes les 8 s, colonnes de vent = élan vers le haut. La plateforme s\'effondre au bout de 10 s. Dernier en vol gagne.","color":"gray","bold":false}]',
}
W('go', ['# Élytra — départ',
         f'execute if score $skpd mg.st matches 0 run function {NS}/pad_place',
         'scoreboard players set $skt mg.st 0',
         'effect give @a[tag=mg.play] minecraft:resistance infinite 4 true',
         'effect give @a[tag=mg.play] minecraft:saturation infinite 0 true',
         'scoreboard players set @a[tag=mg.play] mg.skg -40',
         f'execute if score $elm mg.st matches 1..2 run function {NS}/go_race',
         f'execute if score $elm mg.st matches 3 run function {NS}/go_surv',
         'execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.ender_dragon.flap master @s ~ ~ ~ 1 1.2'])
W('go_race', ['# Modes 1-2 : barrière ouverte, fusées (+ arc et charges de vent en mode 2)',
              f'function {NS}/pad1_open',
              f'give @a[tag=mg.play] {ROCK} 3',
              f'execute if score $elm mg.st matches 2 run give @a[tag=mg.play] {BOW}',
              f'execute if score $elm mg.st matches 2 run give @a[tag=mg.play] {ARROW}',
              f'execute if score $elm mg.st matches 2 run give @a[tag=mg.play] {WIND} 3',
              'scoreboard players set $skwt mg.st 0',
              'scoreboard objectives setdisplay sidebar mg.skr',
              f'execute if score $elm mg.st matches 1 run tellraw @a[tag=mg.play] {RULES[1]}',
              f'execute if score $elm mg.st matches 2 run tellraw @a[tag=mg.play] {RULES[2]}'])
W('go_surv', ['# Mode 3 : barrière ouverte, fusées, zone de 70 blocs',
              f'function {NS}/pad3_open',
              f'give @a[tag=mg.play] {ROCK} 2',
              'scoreboard players set $skz mg.st 700',
              'data modify storage mg:sky z.r set value 70.0d',
              'scoreboard players set $skpo mg.st 1',
              'scoreboard objectives setdisplay sidebar mg.sks',
              f'tellraw @a[tag=mg.play] {RULES[3]}'])

W('tick', ['# Élytra — tick de partie (état 2)',
           'scoreboard players add $skt mg.st 1',
           'scoreboard players operation $skp mg.st = $skt mg.st',
           'scoreboard players operation $skp mg.st %= #2 mg.st',
           f'execute if score $elm mg.st matches 1..2 run function {NS}/t_race',
           f'execute if score $elm mg.st matches 3 run function {NS}/t_surv'])

# ---- course (modes 1-2)
SPLIT = ['scoreboard players operation $es mg.st = $skt mg.st', 'scoreboard players operation $es mg.st /= #20 mg.st',
         'scoreboard players operation $ecs mg.st = $skt mg.st', 'scoreboard players operation $ecs mg.st %= #20 mg.st',
         'scoreboard players operation $ecs mg.st *= #5 mg.st']


def tparts(col):
    T = '{"score":{"name":"$es","objective":"mg.st"},"color":"%s"},{"text":",","color":"%s"}' % (col, col)
    return (f'{T},{{"text":"0","color":"{col}"}},{{"score":{{"name":"$ecs","objective":"mg.st"}},"color":"{col}"}}',
            f'{T},{{"score":{{"name":"$ecs","objective":"mg.st"}},"color":"{col}"}}')


W('t_race', ['# Modes 1-2 : chrono, joueurs, combat, limite de 4 minutes'] + SPLIT + [
    f'execute as @a[tag=mg.play] at @s run function {NS}/r_player',
    f'execute if score $elm mg.st matches 2 run function {NS}/t_combat',
    'execute if score $skt mg.st matches 3600 run tellraw @a[tag=mg.play] [{"text":"🪽 Plus qu\'une minute !","color":"gold"}]',
    f'execute if score $state mg.st matches 2 if score $skt mg.st matches 4800.. run function {NS}/r_timeout',
    'execute if score $state mg.st matches 2 unless entity @a[tag=mg.play] run function mg:core/draw'])

zx, zy, zz, zdx, zdy, zdz = ZONE
W('r_player', ['# Course, chaque tick (@s = participant, positionné)',
               'execute if entity @s[tag=mg.skf] run return 0',
               '# Compteur « pas en vol plané » (négatif = délai de grâce)',
               'scoreboard players add @s mg.skg 1',
               'execute if score @s mg.skg matches 1.. if predicate mg:gliding run scoreboard players set @s mg.skg 0',
               f'execute if entity @s[x={PAD1[0]-8},y={PAD1[1]},z={PAD1[2]-8},dx=16,dy=6,dz=16] run scoreboard players set @s mg.skg -40',
               'execute if entity @s[tag=mg.skstun] run scoreboard players set @s mg.skg -30',
               f'execute if score @s mg.skg matches 20.. run return run function {NS}/rescue',
               f'execute unless entity @s[x={zx},y={zy},z={zz},dx={zdx},dy={zdy},dz={zdz}] run return run function {NS}/rescue',
               f'function {NS}/r_hud']
  + [f'execute if score @s mg.skr matches {k} run return run function {NS}/rk/r{k}' for k in range(N)])

a, b2 = tparts('white')
W('r_hud', ['# Chrono et progression (@s)',
            f'execute if score $ecs mg.st matches ..9 if score $elm mg.st matches 1 run title @s actionbar [{{"text":"⏱ ","color":"aqua"}},{a},{{"text":" s   ◎ ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.skr"}},"color":"aqua"}},{{"text":"/{N}","color":"gray"}}]',
            f'execute if score $ecs mg.st matches 10.. if score $elm mg.st matches 1 run title @s actionbar [{{"text":"⏱ ","color":"aqua"}},{b2},{{"text":" s   ◎ ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.skr"}},"color":"aqua"}},{{"text":"/{N}","color":"gray"}}]',
            f'execute if score $ecs mg.st matches ..9 if score $elm mg.st matches 2 unless entity @s[tag=mg.skstun] run title @s actionbar [{{"text":"⏱ ","color":"aqua"}},{a},{{"text":" s   ◎ ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.skr"}},"color":"aqua"}},{{"text":"/{N}   💨 recharge dans ","color":"gray"}},{{"score":{{"name":"$skws","objective":"mg.st"}},"color":"aqua"}},{{"text":" s","color":"gray"}}]',
            f'execute if score $ecs mg.st matches 10.. if score $elm mg.st matches 2 unless entity @s[tag=mg.skstun] run title @s actionbar [{{"text":"⏱ ","color":"aqua"}},{b2},{{"text":" s   ◎ ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.skr"}},"color":"aqua"}},{{"text":"/{N}   💨 recharge dans ","color":"gray"}},{{"score":{{"name":"$skws","objective":"mg.st"}},"color":"aqua"}},{{"text":" s","color":"gray"}}]',
            'execute if entity @s[tag=mg.skstun] run title @s actionbar [{"text":"💫 Sonné ! Élytres de retour dans un instant...","color":"red"}]'])

os.makedirs(os.path.join(OUT, 'rk'), exist_ok=True)
for k in range(N):
    x, y, z, size, kind = RINGS[k]
    h = size // 2 - 1
    if AXES[k] == 'x':
        box = f'x={x-2},y={y-h},z={z-h},dx=4,dy={2*h},dz={2*h}'
    else:
        box = f'x={x-h},y={y-h},z={z-2},dx={2*h},dy={2*h},dz=4'
    prev = PATH[k]
    floor = max(ZONE[1], min(prev[1], y) - 32)
    col = 'wax_on' if kind == 'b' else 'end_rod'
    W(f'rk/r{k}', [f'# Vers l\'anneau {k+1}/{N} (@s, {RINGS[k][4]}) : passage, plancher, traînée (généré)',
                   f'execute if entity @s[{box}] run return run function {NS}/pass',
                   f'execute unless entity @s[y={floor},dy=400] run return run function {NS}/rescue',
                   f'execute if score $skp mg.st matches 0 anchored eyes facing {x+.5} {y+.5} {z+.5} run function {NS}/trail',
                   f'execute if score $skp mg.st matches 0 run particle minecraft:{col} {x+.5} {y+.5} {z+.5} {h*.5:.1f} {h*.5:.1f} {h*.5:.1f} 0.01 4 force @s'])
W('trail', ['# Traînée lumineuse vers l\'anneau suivant (@s, orienté vers l\'anneau, vue par @s seul)']
  + [f'particle minecraft:end_rod ^ ^-0.4 ^{d} 0 0 0 0 1 force @s' for d in range(3, 17, 2)])

boosts = [i + 1 for i, r in enumerate(RINGS) if r[4] == 'b']
W('pass', ['# Anneau franchi (@s)',
           'scoreboard players add @s mg.skr 1',
           'playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.5',
           'particle minecraft:totem_of_undying ~ ~ ~ 0.6 0.6 0.6 0.3 15 force @s']
  + [f'execute if score @s mg.skr matches {b} run function {NS}/boost' for b in boosts]
  + [f'execute if score @s mg.skr matches {N}.. run return run function {NS}/finish'])
W('boost', ['# Anneau doré (@s) : une fusée de plus',
            f'give @s {ROCK} 1',
            'playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.8 1.6',
            'title @s subtitle [{"text":"🚀 +1 fusée !","color":"gold","bold":true}]',
            'title @s title [{"text":" "}]'])

resc = ['# Remise en selle (@s) : au-dessus du dernier anneau franchi, orienté vers le suivant (généré)',
        f'execute if score @s mg.skr matches 0 run tp @s {PAD1[0]+.5} {PAD1[1]+1} {PAD1[2]+.5} facing {RINGS[0][0]+.5} {RINGS[0][1]+.5} {RINGS[0][2]+.5}']
for k in range(1, N):
    x, y, z, size, _ = RINGS[k - 1]
    nx, ny, nz = RINGS[k][:3]
    resc.append(f'execute if score @s mg.skr matches {k} run tp @s {x+.5} {y + size // 2 + 3} {z+.5} facing {nx+.5} {ny+.5} {nz+.5}')
resc += [f'execute if entity @s[tag=mg.skstun] run function {NS}/unstun',
         'effect give @s minecraft:slow_falling 2 0 true',
         'scoreboard players set @s mg.skg -40',
         'title @s subtitle [{"text":"Appuie sur Espace pour replaner !","color":"yellow"}]',
         'title @s title [{"text":"↺","color":"aqua","bold":true}]',
         'playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 0.7 1.3']
W('rescue', resc)

a, b2 = tparts('gold')
W('finish', ['# Arrivée (@s) : temps, record du serveur (mode 1), victoire'] + SPLIT + [
    'tag @s add mg.skf',
    'effect give @s minecraft:slow_falling 30 0 true',
    'title @s title [{"text":"🏁 Arrivée !","color":"gold","bold":true}]',
    f'execute if score $ecs mg.st matches ..9 run tellraw @a[tag=!mg.surv] [{{"text":"🏁 ","color":"gold"}},{{"selector":"@s","color":"yellow"}},{{"text":" boucle la course en ","color":"gray"}},{a},{{"text":" s","color":"gold"}}]',
    f'execute if score $ecs mg.st matches 10.. run tellraw @a[tag=!mg.surv] [{{"text":"🏁 ","color":"gold"}},{{"selector":"@s","color":"yellow"}},{{"text":" boucle la course en ","color":"gray"}},{b2},{{"text":" s","color":"gold"}}]',
    'execute unless score $skrec mg.st matches 1.. run scoreboard players set $skrec mg.st 999999',
    f'execute if score $elm mg.st matches 1 if score $skt mg.st < $skrec mg.st run function {NS}/record',
    'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. run effect give @a[tag=mg.play] minecraft:slow_falling 15 0 true',
    'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. run return run function mg:core/win_player',
    'tellraw @s [{"text":"(Mode test solo : menu → Arrêter pour finir)","color":"dark_gray","italic":true}]'])
W('record', ['# Nouveau record du serveur, course d\'anneaux (@s ; $es / $ecs déjà calculés)',
             'scoreboard players operation $skrec mg.st = $skt mg.st',
             f'execute if score $ecs mg.st matches ..9 run tellraw @a [{{"text":"🏆 ","color":"gold"}},{{"selector":"@s","color":"yellow","bold":true}},{{"text":" bat le record de la course Élytra : ","color":"gray"}},{a},{{"text":" s !","color":"gold"}}]',
             f'execute if score $ecs mg.st matches 10.. run tellraw @a [{{"text":"🏆 ","color":"gold"}},{{"selector":"@s","color":"yellow","bold":true}},{{"text":" bat le record de la course Élytra : ","color":"gray"}},{b2},{{"text":" s !","color":"gold"}}]',
             'function mg:hall/ely {key:"elyg",lbl:"🪽 Record Élytra : course"}'])
W('r_timeout', ['# 4 minutes écoulées : le plus avancé gagne',
                'tellraw @a[tag=mg.play] [{"text":"🪽 Temps écoulé : le plus avancé l\'emporte !","color":"gold"}]',
                'effect give @a[tag=mg.play] minecraft:slow_falling 15 0 true',
                'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                'scoreboard players set $skmx mg.st -1',
                'execute as @a[tag=mg.play] run scoreboard players operation $skmx mg.st > @s mg.skr',
                'execute if score $skmx mg.st matches ..0 run return run function mg:core/draw',
                'tag @a remove mg.skw',
                'execute as @a[tag=mg.play] if score @s mg.skr = $skmx mg.st run tag @s add mg.skw',
                'execute as @a[tag=mg.skw,sort=random,limit=1] run function mg:core/win_player',
                'tag @a remove mg.skw'])

# ---- combat (mode 2)
W('t_combat', ['# Mode 2 : sonnés, recharge des charges de vent, détonation de proximité des charges',
               'scoreboard players remove @a[scores={mg.skst=1..}] mg.skst 1',
               f'execute as @a[tag=mg.skstun,scores={{mg.skst=..0}}] run function {NS}/unstun',
               'scoreboard players add $skwt mg.st 1',
               f'execute if score $skwt mg.st matches 300.. run function {NS}/wc_refill',
               'scoreboard players set $skws mg.st 300',
               'scoreboard players operation $skws mg.st -= $skwt mg.st',
               'scoreboard players operation $skws mg.st /= #20 mg.st',
               f'execute as @e[type=minecraft:wind_charge,x={zx-20},y=60,z={zz-20},dx={zdx+40},dy=240,dz={zdz+40}] at @s run function {NS}/wc_check'])
W('wc_refill', ['# Toutes les 15 s : 3 charges de vent',
                'scoreboard players set $skwt mg.st 0',
                f'clear @a[tag=mg.play] minecraft:wind_charge[minecraft:custom_data~{{mg_sky:1b}}]',
                f'give @a[tag=mg.play] {WIND} 3',
                'execute as @a[tag=mg.play] at @s run playsound minecraft:item.armor.equip_elytra master @s ~ ~ ~ 0.6 1.6'])
W('wc_check', ['# Charge de vent (@s) : explose au contact d\'un rival (à 3,5 blocs)',
               'execute unless entity @a[tag=mg.play,distance=..3.5] run return 0',
               'tag @a remove mg.skak',
               'execute on origin run tag @s add mg.skak',
               'execute as @a[tag=mg.play,tag=!mg.skak,tag=!mg.skstun,distance=..3.5,sort=nearest,limit=1] run tag @s add mg.skv',
               'execute unless entity @a[tag=mg.skv] run return run tag @a remove mg.skak',
               'particle minecraft:gust_emitter_small ~ ~ ~ 0 0 0 0 1 force @a',
               'playsound minecraft:entity.wind_charge.wind_burst master @a ~ ~ ~ 1.5 1',
               f'execute as @a[tag=mg.skv] run function {NS}/stun',
               'tag @a remove mg.skv',
               'tag @a remove mg.skak',
               'kill @s'])
W('hurt_adv', ['# Touché par une flèche ou une charge de vent d\'un joueur (@s = victime) — avancement mg:sky/hurt',
               'advancement revoke @s only mg:sky/hurt',
               'execute unless score $game mg.st matches 74 run return 0',
               'execute unless score $state mg.st matches 2 run return 0',
               'execute unless score $elm mg.st matches 2 run return 0',
               'execute unless entity @s[tag=mg.play] run return 0',
               'tag @a remove mg.skak',
               'execute on attacker run tag @s[tag=mg.play] add mg.skak',
               'execute if entity @s[tag=mg.skak] run return run tag @a remove mg.skak',
               f'function {NS}/stun',
               'tag @a remove mg.skak'])
W('stun', ['# Rival touché (@s = victime ; tireur tagué mg.skak s\'il est connu) : élytres retirées 1,5 s',
           'execute if entity @s[tag=mg.skstun] run return 0',
           'execute if entity @s[tag=mg.skf] run return 0',
           'tag @s add mg.skstun',
           'scoreboard players set @s mg.skst 30',
           'item replace entity @s armor.chest with minecraft:air',
           'execute if entity @a[tag=mg.skak] run tellraw @a[tag=!mg.surv] [{"text":"🏹 ","color":"red"},{"selector":"@a[tag=mg.skak,limit=1]","color":"yellow"},{"text":" a abattu ","color":"gray"},{"selector":"@s","color":"yellow"},{"text":" !","color":"gray"}]',
           'execute unless entity @a[tag=mg.skak] run tellraw @a[tag=!mg.surv] [{"text":"🏹 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" est abattu !","color":"gray"}]',
           'title @s subtitle [{"text":"Tes élytres reviennent dans 1,5 s","color":"gray"}]',
           'title @s title [{"text":"💫 Sonné !","color":"red","bold":true}]',
           'playsound minecraft:entity.player.hurt master @s ~ ~ ~ 1 0.8',
           'execute at @s run particle minecraft:crit ~ ~1 ~ 0.4 0.6 0.4 0.3 25 force @a',
           'execute as @a[tag=mg.skak] at @s run playsound minecraft:entity.arrow.hit_player master @s ~ ~ ~ 1 1'])
W('unstun', ['# Fin de l\'étourdissement (@s) : élytres rendues',
             'tag @s remove mg.skstun',
             'scoreboard players set @s mg.skst 0',
             'execute unless entity @s[tag=mg.play] run return 0',
             f'item replace entity @s armor.chest with {ELY}',
             'scoreboard players set @s mg.skg -30',
             'title @s subtitle [{"text":"Élytres rendues : appuie sur Espace !","color":"yellow","bold":true}]',
             'title @s title [{"text":" "}]',
             'playsound minecraft:item.armor.equip_elytra master @s ~ ~ ~ 1 1.2'])

# ---- survie en vol (mode 3)
ax0, az0 = ARENA
W('t_surv', ['# Mode 3 : plateforme, zone, joueurs, colonnes de vent, fusées, fin',
             'execute if score $skt mg.st matches 140 run title @a[tag=mg.play] actionbar [{"text":"⚠ La plateforme s\'effondre dans 3 s !","color":"red","bold":true}]',
             f'execute if score $skt mg.st matches 200 run function {NS}/pad3_off',
             '# Rayon de la zone (dixièmes de bloc) : 700 → 150 en 3 minutes',
             f'execute if score $skt mg.st matches ..3600 run function {NS}/s_zone',
             'scoreboard players operation $skp5 mg.st = $skt mg.st',
             'scoreboard players operation $skp5 mg.st %= #5 mg.st',
             'scoreboard players operation $skfw mg.st = $skt mg.st',
             'scoreboard players operation $skfw mg.st %= #160 mg.st',
             'scoreboard players set $skfs mg.st 160',
             'scoreboard players operation $skfs mg.st -= $skfw mg.st',
             'scoreboard players operation $skfs mg.st /= #20 mg.st',
             'scoreboard players operation $skzr mg.st = $skz mg.st',
             'scoreboard players operation $skzr mg.st /= #10 mg.st',
             'execute store result score $skn mg.st if entity @a[tag=mg.play]',
             '# Colonnes de vent (actives pendant les 3 premières minutes)',
             'scoreboard players remove @a[scores={mg.skl=1..}] mg.skl 1',
             f'execute as @a[scores={{mg.skl=100}}] run function {NS}/lift_end',
             f'execute if score $skt mg.st matches ..3599 run function {NS}/s_cols',
             f'execute as @a[tag=mg.play] at @s run function {NS}/s_player',
             f'execute if score $skp5 mg.st matches 0 as @a[tag=mg.play] at @s positioned {ax0+.5} ~ {az0+.5} run function {NS}/zone_chk with storage mg:sky z',
             f'execute if score $skp5 mg.st matches 0 as @a[tag=mg.play] at @s positioned {ax0+.5} ~ {az0+.5} run function {NS}/zone_draw with storage mg:sky z',
             f'execute if score $skp5 mg.st matches 0 as @a[tag=mg.out] at @s positioned {ax0+.5} ~ {az0+.5} run function {NS}/zone_draw with storage mg:sky z',
             '# Une fusée toutes les 8 s (jusqu\'à la mort subite)',
             f'execute if score $skt mg.st matches ..3599 if score $skfw mg.st matches 0 run function {NS}/s_rocket',
             'execute if score $skt mg.st matches 3600 run tellraw @a[tag=!mg.surv] [{"text":"🌪 MORT SUBITE : ","color":"red","bold":true},{"text":"zone au minimum, plus de fusées ni de colonnes de vent !","color":"gray","bold":false}]',
             'execute if score $skt mg.st matches 3600 as @a[tag=!mg.surv] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.5 1.5',
             '# Survivants : une seconde de plus',
             'scoreboard players operation $skq mg.st = $skt mg.st',
             'scoreboard players operation $skq mg.st %= #20 mg.st',
             'execute if score $skq mg.st matches 0 run scoreboard players add @a[tag=mg.play] mg.sks 1',
             '# Fin',
             'execute store result score $skn mg.st if entity @a[tag=mg.play]',
             f'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $skn mg.st matches 1 as @a[tag=mg.play,limit=1] run function {NS}/s_win',
             f'execute if score $state mg.st matches 2 if score $skt mg.st matches 6000.. run function {NS}/s_timeout',
             'execute if score $state mg.st matches 2 unless entity @a[tag=mg.play] run function mg:core/draw'])
W('s_zone', ['# $skz = 700 - t × 11 / 72  (t ≤ 3600) → mg:sky z.r',
             'scoreboard players operation $skz mg.st = $skt mg.st',
             'scoreboard players operation $skz mg.st *= #11 mg.st',
             'scoreboard players operation $skz mg.st /= #72 mg.st',
             'scoreboard players operation $skz mg.st *= #-1 mg.st',
             'scoreboard players add $skz mg.st 700',
             'execute if score $skz mg.st matches ..150 run scoreboard players set $skz mg.st 150',
             'execute store result storage mg:sky z.r double 0.1 run scoreboard players get $skz mg.st'])
W('s_player', ['# Survie en vol, chaque tick (@s = participant, positionné)',
               'scoreboard players add @s mg.skg 1',
               'execute if score @s mg.skg matches 1.. if predicate mg:gliding run scoreboard players set @s mg.skg 0',
               f'execute if score $skpo mg.st matches 1 if entity @s[x={PAD3[0]-8},y={PAD3[1]},z={PAD3[2]-8},dx=16,dy=6,dz=16] run scoreboard players set @s mg.skg -40',
               'execute if score @s mg.skl matches 101.. run scoreboard players set @s mg.skg -20',
               f'execute unless entity @s[y={FLOOR3},dy=400] run return run function {NS}/s_elim {{why:"est tombé dans le vide"}}',
               f'execute if score @s mg.skg matches 20.. run return run function {NS}/s_elim {{why:"s\'est posé"}}',
               f'execute if score @s mg.sko matches 60.. run return run function {NS}/s_elim {{why:"est resté hors de la zone"}}',
               'execute if score @s mg.sko matches 1.. run return run title @s actionbar [{"text":"⚠ HORS DE LA ZONE — reviens vers le centre ! ","color":"red","bold":true},{"score":{"name":"@s","objective":"mg.sko"},"color":"yellow"},{"text":"/60","color":"gray"}]',
               'execute if score @s mg.skl matches 101.. run return run title @s actionbar [{"text":"💨 Colonne de vent !","color":"aqua","bold":true}]',
               'execute if score $skt mg.st matches ..3599 run title @s actionbar [{"text":"🪽 En vol : ","color":"aqua"},{"score":{"name":"$skn","objective":"mg.st"},"color":"white"},{"text":"   ◯ zone ","color":"gray"},{"score":{"name":"$skzr","objective":"mg.st"},"color":"red"},{"text":" blocs   🚀 dans ","color":"gray"},{"score":{"name":"$skfs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gray"}]',
               'execute if score $skt mg.st matches 3600.. run title @s actionbar [{"text":"🌪 MORT SUBITE","color":"red","bold":true},{"text":"   🪽 En vol : ","color":"aqua","bold":false},{"score":{"name":"$skn","objective":"mg.st"},"color":"white","bold":false}]'])
W('s_elim', ['# Éliminé (@s) — macro {why}',
             '$tellraw @a[tag=!mg.surv] [{"text":"🪽 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" $(why).","color":"gray"}]',
             'scoreboard players reset @s mg.sks',
             'scoreboard players set @s mg.skl 0',
             'scoreboard players set @s mg.sko 0',
             'effect clear @s minecraft:levitation',
             f'clear @s {SKYITEM}',
             'function mg:core/eliminate'])
W('zone_chk', ['# Dans la zone ? (@s, positionné au centre à sa hauteur) — macro {r}',
               '$execute if entity @s[distance=..$(r)] run return run scoreboard players set @s mg.sko 0',
               'execute if score @s mg.sko matches 0 run title @s subtitle [{"text":"Hors de la zone : 3 s pour revenir !","color":"red"}]',
               'execute if score @s mg.sko matches 0 run title @s title [{"text":"⚠","color":"red","bold":true}]',
               'execute if score @s mg.sko matches 0 run playsound minecraft:block.note_block.bass master @s ~ ~ ~ 1 0.6',
               'scoreboard players add @s mg.sko 5'])
W('zone_draw', ['# Cercle de la zone à la hauteur du joueur, vu par lui seul (@s, positionné au centre) — macro {r} (généré)']
  + [f'$execute rotated {a} 0 run particle minecraft:dust{{color:[1.0,0.2,0.15],scale:3.0}} ^ ^ ^$(r) 0.1 2.5 0.1 0 3 force @s' for a in range(0, 360, 8)])
W('s_cols', ['# Colonnes de vent : élan vers le haut (généré)']
  + [f'execute as @a[tag=mg.play,x={cx-COL_R},y={COL_Y0},z={cz-COL_R},dx={2*COL_R},dy={COL_Y1-COL_Y0},dz={2*COL_R},scores={{mg.skl=..0}}] run function {NS}/lift' for cx, cz in COLS]
  + ['execute if score $skp5 mg.st matches 0 run function mg:sky/s_colfx'])
W('s_colfx', ['# Colonnes de vent : particules ascendantes (généré)']
  + [l for cx, cz in COLS for l in (
      f'particle minecraft:cloud {cx+.5} {(COL_Y0+COL_Y1)//2} {cz+.5} 1.3 26 1.3 0.02 30 force @a',
      f'particle minecraft:small_gust {cx+.5} {(COL_Y0+COL_Y1)//2} {cz+.5} 1.5 26 1.5 0 12 force @a',
      f'particle minecraft:end_rod {cx+.5} {COL_Y0+3} {cz+.5} 1.5 1 1.5 0.15 6 force @a')])
W('lift', ['# Entrée dans une colonne de vent (@s) : 1,5 s de lévitation, puis 5 s avant la suivante',
           'scoreboard players set @s mg.skl 130',
           'effect give @s minecraft:levitation infinite 9 true',
           'playsound minecraft:entity.breeze.wind_burst master @s ~ ~ ~ 1 1'])
W('lift_end', ['# Fin de l\'élan (@s)',
               'effect clear @s minecraft:levitation',
               'execute if entity @s[tag=mg.play] run title @s subtitle [{"text":"Appuie sur Espace pour replaner !","color":"yellow","bold":true}]',
               'execute if entity @s[tag=mg.play] run title @s title [{"text":" "}]'])
W('s_rocket', ['# Une fusée pour chaque survivant',
               f'give @a[tag=mg.play] {ROCK} 1',
               'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 0.8 1.4'])
W('s_win', ['# Dernier en vol (@s)',
            'effect give @s minecraft:slow_falling 15 0 true',
            'function mg:core/win_player'])
W('s_timeout', ['# 5 minutes : le plus haut gagne',
                'tellraw @a[tag=mg.play] [{"text":"🌪 Temps écoulé : le plus haut l\'emporte !","color":"gold"}]',
                'effect give @a[tag=mg.play] minecraft:slow_falling 15 0 true',
                'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                'execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]',
                'scoreboard players set $skmx mg.st -9999',
                'execute as @a[tag=mg.play] run scoreboard players operation $skmx mg.st > @s mg.t',
                'tag @a remove mg.skw',
                'execute as @a[tag=mg.play] if score @s mg.t = $skmx mg.st run tag @s add mg.skw',
                'execute as @a[tag=mg.skw,sort=random,limit=1] run function mg:core/win_player',
                'tag @a remove mg.skw'])

W('cleanup', ['# Élytra — nettoyage (appelé par core/return_lobby)',
              f'clear @a {SKYITEM}',
              'effect clear @a[scores={mg.skl=1..}] minecraft:levitation',
              'kill @e[tag=mg.sky]',
              f'kill @e[type=minecraft:wind_charge,x={zx-20},y=0,z={zz-20},dx={zdx+40},dy=320,dz=1600]',
              'tag @a remove mg.skf',
              'tag @a remove mg.skstun',
              'tag @a remove mg.skak',
              'tag @a remove mg.skv',
              'tag @a remove mg.skw',
              'scoreboard players reset * mg.skr',
              'scoreboard players reset * mg.sks',
              'scoreboard players reset * mg.skg',
              'scoreboard players reset * mg.skst',
              'scoreboard players reset * mg.skl',
              'scoreboard players reset * mg.sko',
              'advancement revoke @a only mg:sky/hurt',
              f'schedule clear {NS}/pad_wait',
              f'function {NS}/pad_fl_off'])

# =====================================================================================
# Écriture
# =====================================================================================
for d in (OUT, SUB, os.path.join(OUT, 'rk')):
    os.makedirs(d, exist_ok=True)
    for f in os.listdir(d):
        if f.endswith('.mcfunction'):
            os.remove(os.path.join(d, f))
for name, txt in files.items():
    with open(os.path.join(OUT, name + '.mcfunction'), 'w', encoding='utf-8') as f:
        f.write(txt)
os.makedirs(ADV, exist_ok=True)
with open(os.path.join(ADV, 'hurt.json'), 'w', encoding='utf-8') as f:
    f.write('''{
  "criteria": {
    "hit": {
      "trigger": "minecraft:entity_hurt_player",
      "conditions": {
        "damage": {
          "type": {
            "source_entity": {
              "minecraft:entity_type": "minecraft:player"
            },
            "direct_entity": {
              "minecraft:entity_type": [
                "minecraft:arrow",
                "minecraft:wind_charge"
              ]
            }
          }
        }
      }
    }
  },
  "rewards": {
    "function": "mg:sky/hurt_adv"
  }
}
''')

if __name__ == '__main__':
    tot = sum(s[2] for s in stats)
    print(f'{len(files)} fonctions, {len(features)} éléments de décor, {len(sec_keys)} sections, '
          f'{tot} commandes de construction, {len(steps_b)} étapes')
    for s in stats:
        print('  section', s[0], s[1], 'cmds', s[2], 'morceaux', s[3], 'tronçons', s[4], 'voxels', s[5])
    from collections import Counter
    print(Counter(n for n, _, _ in features))
