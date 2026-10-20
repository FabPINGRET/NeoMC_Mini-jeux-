# Terra Nova : relief, bruit, hauteurs, surface, chemins, points d'apparition, TERRAIN et VEG ; exécuté par gen_terranova.py (exec), à la place exacte de ce bloc.
# Tranche contiguë de l'ancien gen_terranova.py : mêmes globals que la façade, aucun import, aucune copie de w/js/patch.
# Utilise : G, HX, WALL, math, random, rnd

# ================================================================ relief
def _hash(seed, i, j):
    return random.Random(seed * 1000003 + i * 7919 + j * 104729).uniform(-1, 1)


def noise(seed, cell, x, z):
    fx, fz = x / cell, z / cell
    i, j = math.floor(fx), math.floor(fz)
    tx, tz = fx - i, fz - j
    sx, sz = tx * tx * (3 - 2 * tx), tz * tz * (3 - 2 * tz)
    a, b = _hash(seed, i, j), _hash(seed, i + 1, j)
    c, d = _hash(seed, i, j + 1), _hash(seed, i + 1, j + 1)
    return (a + (b - a) * sx) * (1 - sz) + (c + (d - c) * sx) * sz


def river_z(x):
    return -52 + 7 * math.sin(x / 15) + 3 * math.sin(x / 7.3)


OUTPOSTS = [('Alpha', 62, -74), ('Bravo', -72, 6), ('Charlie', 30, 72)]


def raw_h(x, z):
    return 65 + 4.5 * noise(11, 22, x, z) + 2.0 * noise(12, 9, x, z) + 0.8 * noise(13, 4, x, z)


OUT_H = {k: max(63, round(raw_h(ox, oz))) for k, ox, oz in OUTPOSTS}


def edge(x, z):
    return min(x + HX, HX - 1 - x, z + HX, HX - 1 - z)


# cols vers les régions (tv_world.py) : (axe du bord, coordonnée du couloir)
PASSES = {'n': ('z', -30), 's': ('z', -24), 'e': ('x', 30), 'w': ('x', 6)}
PASS_Y = 66


def valley_pass(x, z):
    """(distance au bord du côté le plus proche, distance au couloir du col de ce côté)."""
    d = {'w': x + HX, 'e': HX - 1 - x, 'n': z + HX, 's': HX - 1 - z}
    side = min(d, key=d.get)
    ax, c = PASSES[side]
    return d[side], (abs(x - c) if ax == 'z' else abs(z - c))


def lerp_(a, b, t):
    return a + (b - a) * t


def smooth_(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def height(x, z, passes=True):
    h = raw_h(x, z)
    d = max(abs(x), abs(z))
    if d <= 31:
        h = G
    elif d < 42:
        t = (d - 31) / 11
        t = t * t * (3 - 2 * t)
        h = G + (h - G) * t
    for k, ox, oz in OUTPOSTS:
        do = math.hypot(x - ox, z - oz)
        if do < 11:
            t = 0 if do < 7 else (do - 7) / 4
            h = OUT_H[k] + (h - OUT_H[k]) * t
    dr = abs(z - river_z(x))
    if dr < 7 and d > 31:
        h = min(h, 59 if dr < 4 else 62 + (dr - 4) * 0.7)
    e = edge(x, z)
    db, dc = valley_pass(x, z)
    if passes and db < 16 and dc <= 3:
        h = lerp_(PASS_Y, h, smooth_(db / 16))
    if e < 12:
        f = 1.0
        if passes and dc <= 7:
            f = 0.0 if dc <= 3 else (dc - 3) / 4
        h += ((12 - e) / 12) ** 2 * 26 * f
    return max(59, min(95, round(h)))


H = {(x, z): height(x, z) for x in range(-HX, HX) for z in range(-HX, HX)}
H_OLD = {c: height(*c, passes=False) for c in H if valley_pass(*c)[0] < 16 and valley_pass(*c)[1] <= 7}


def surface(x, z):
    h = H[(x, z)]
    e = edge(x, z)
    if e < 6 and h > 70:
        return 'mossy_cobblestone' if (x * 7 + z * 3) % 5 == 0 else 'stone'
    dr = abs(z - river_z(x))
    if max(abs(x), abs(z)) > 31 and dr < 4:
        return 'gravel' if (x + z) % 3 else 'sand'
    if h <= 62:
        return 'mud'
    return 'grass_block'


def under(x, z):
    return 'stone' if surface(x, z) in ('stone', 'mossy_cobblestone') else 'dirt'


# ---------------------------------------------------------------- chemins (porte → outpost)
PATHS = [[(0, -30), (8, -45), (30, -58), (60, -67)],
         [(0, 30), (10, 48), (28, 65)],
         [(0, 30), (-20, 38), (-45, 30), (-65, 8)]]
PATH = set()
for pts in PATHS:
    for (x1, z1), (x2, z2) in zip(pts, pts[1:]):
        n = max(abs(x2 - x1), abs(z2 - z1))
        for s in range(n + 1):
            x, z = round(x1 + (x2 - x1) * s / n), round(z1 + (z2 - z1) * s / n)
            for dx in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    if max(abs(x + dx), abs(z + dz)) > WALL and (x + dx, z + dz) in H:
                        PATH.add((x + dx, z + dz))


def near_path(x, z, r):
    return any((x + dx, z + dz) in PATH for dx in range(-r, r + 1) for dz in range(-r, r + 1))


def jungle_ok(x, z, colony=38, river=5, out=11, edge_min=4):
    if (x, z) not in H or max(abs(x), abs(z)) < colony or edge(x, z) < edge_min:
        return False
    if abs(z - river_z(x)) < river or surface(x, z) != 'grass_block':
        return False
    return all(math.hypot(x - ox, z - oz) >= out for _, ox, oz in OUTPOSTS)


def sample(n, min_d, ok, tries=6000, others=()):
    pts = []
    for _ in range(tries):
        if len(pts) >= n:
            break
        x, z = rnd.randrange(-HX, HX), rnd.randrange(-HX, HX)
        if not ok(x, z):
            continue
        if all(math.hypot(x - a, z - b) >= min_d for a, b in pts) and all(math.hypot(x - a, z - b) >= min_d for a, b in others):
            pts.append((x, z))
    return pts


CRATES = sample(14, 18, lambda x, z: jungle_ok(x, z, colony=45, river=6, out=14, edge_min=12) and not near_path(x, z, 2))
SPAWNS = sample(36, 13, lambda x, z: jungle_ok(x, z, colony=42, river=4, out=10, edge_min=8))
HERBS = sample(8, 24, lambda x, z: jungle_ok(x, z, colony=48, river=6, out=12, edge_min=10) and not near_path(x, z, 3))
FAR = [(x, z) for (x, z) in SPAWNS if math.hypot(x, z) >= 62]


def top(x, z):
    return H[(x, z)] + 1


# ================================================================ construction du monde (étapes)
TERRAIN = []
for x in range(-HX, HX):
    z = -HX
    while z < HX:
        key = (H[(x, z)], surface(x, z), under(x, z), (x, z) in PATH)
        z2 = z
        while z2 + 1 < HX and (H[(x, z2 + 1)], surface(x, z2 + 1), under(x, z2 + 1), (x, z2 + 1) in PATH) == key:
            z2 += 1
        h, s, u, p = key
        if h - 1 >= 56:
            TERRAIN.append(f'fill {x} 56 {z} {x} {h - 1} {z2} minecraft:{u}')
        top_blk = 'dirt_path' if p and s == 'grass_block' else s
        TERRAIN.append(f'fill {x} {h} {z} {x} {h} {z2} minecraft:{top_blk}')
        if h < 62:
            TERRAIN.append(f'fill {x} {h + 1} {z} {x} 62 {z2} minecraft:water')
        z = z2 + 1
# taches de podzol, terre grossière, mousse (sans toucher aux chemins)
for _ in range(260):
    x, z = rnd.randrange(-HX + 6, HX - 6), rnd.randrange(-HX + 6, HX - 6)
    if not jungle_ok(x, z, colony=33, river=6, out=9) or near_path(x, z, 3):
        continue
    b = rnd.choice(['podzol', 'podzol', 'coarse_dirt', 'moss_block', 'rooted_dirt'])
    r = rnd.randint(1, 3)
    h = H[(x, z)]
    TERRAIN.append(f'fill {x - r} {h - 1} {z - r} {x + r} {h + 1} {z + r} minecraft:{b} replace minecraft:grass_block')

VEG = []
used = []


def veg(feature, n, min_d, colony, path_r, out):
    pts = sample(n, min_d, lambda x, z: jungle_ok(x, z, colony=colony, out=out) and not near_path(x, z, path_r)
                 and all(math.hypot(x - a, z - b) >= 4 for a, b in CRATES), tries=n * 40, others=used)
    for (x, z) in pts:
        VEG.append(f'place feature minecraft:{feature} {x} {top(x, z)} {z}')
    used.extend(pts)


veg('mega_jungle_tree', 80, 9, 44, 4, 15)
veg('jungle_tree', 280, 4, 38, 2, 11)
veg('fallen_jungle_tree', 22, 6, 38, 2, 11)
veg('bamboo_some_podzol', 36, 6, 38, 2, 11)
veg('jungle_bush', 480, 2, 36, 1, 9)
veg('melon', 12, 6, 36, 1, 9)
veg('firefly_bush', 60, 3, 36, 1, 9)
for (x, z) in sample(700, 3, lambda x, z: jungle_ok(x, z, colony=33, out=8) and not near_path(x, z, 0), tries=20000):
    VEG.append(f'place feature minecraft:{rnd.choice(["grass_jungle", "grass_jungle", "large_fern"])} {x} {top(x, z)} {z}')
# quelques arbres dans la colonie (ombre), loin des bâtiments
for (x, z) in [(-20, -6), (21, -6), (-4, 21), (24, 4)]:
    VEG.append(f'place feature minecraft:jungle_tree_no_vine {x} {G + 1} {z}')
