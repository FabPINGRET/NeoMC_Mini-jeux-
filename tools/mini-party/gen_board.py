"""Génère la grande carte de la Mini Party (île à thèmes, chemins avec embranchements) et les tables du plateau."""
import os, sys, math, random

OUT = os.path.join(sys.argv[1], 'function', 'party')
os.makedirs(OUT, exist_ok=True)
ZC = 15000          # centre de l'île (x 0, z 15000)
HALF = 90           # île + océan : x et z relatifs de -90 à 90
YB = 44             # dessous de l'île
SEA = 62            # niveau de l'eau
VOL, VR = (38, 40), 24
MNT, MR = (-46, -4), 24
LAKE, LR = (-60, 22), 7
random.seed(26)

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

def sq(x, z):
    return ((abs(x) / 76) ** 4 + (abs(z) / 76) ** 4) ** 0.25

def zone(x, z):
    if math.hypot(x - VOL[0], z - VOL[1]) < 26: return 'volcano'
    if math.hypot(x - MNT[0], z - MNT[1]) < 25: return 'mountain'
    if math.hypot(x, z) < 18: return 'castle'
    ox, oz = x, z
    x = x + (vn(ox, oz, 17, 21) - 0.5) * 18
    z = z + (vn(ox, oz, 17, 22) - 0.5) * 18
    if ox > 40 and x > 46 and z < 60: return 'beach'
    if ox > 20 and oz > 20 and sq(ox, oz) > 0.9: return 'beach'
    if z > 38 and -42 < x < 26: return 'desert'
    if x < -38 and z > -30: return 'frost'
    if z < -28 and x < -24: return 'forest'
    if z < -34: return 'village'
    return 'meadow'

def H0(x, z):
    zn = zone(x, z)
    h = 64 + (vn(x, z, 9, 1) - 0.5) * 1.6
    if zn == 'desert':
        h = 64.6 + 1.8 * math.sin(x / 6.5 + vn(x, z, 15, 2) * 3) + 1.2 * math.cos(z / 4.7)
    if zn == 'forest':
        h = 64 + vn(x, z, 7, 3) * 1.8
    if zn == 'beach':
        e = sq(x, z)
        h = 64.2 if e < 0.9 else 64.2 - (e - 0.9) / 0.1 * 4.8
    rc = math.hypot(x, z)
    if rc < 17:
        h = max(h, 72 if rc < 9 else 72 - (rc - 9))
    rv = math.hypot(x - VOL[0], z - VOL[1])
    if rv < VR:
        h = max(h, 64 + 44 * (1 - rv / VR) ** 1.4 + (vn(x, z, 4, 5) - 0.5) * 2 * (rv / VR))
    rm = math.hypot(x - MNT[0], z - MNT[1])
    if rm < MR:
        h = max(h, 64 + 44 * (1 - rm / MR) ** 1.15 + (vn(x, z, 5, 6) - 0.5) * 4 * (1 - rm / MR))
    return h

# ------------------------------------------------------------------ chemins
SEG = {
    'A':  [(0, -52), (26, -54), (44, -42), (54, -24), (56, -4)],
    'O1': [(56, -4), (62, 10), (68, 30), (70, 48), (62, 62), (46, 70), (28, 68)],
    'I1': [(56, -4), (46, 18), (26, 30), (22, 48), (28, 68)],
    'B':  [(28, 68), (8, 66), (-14, 62), (-30, 50)],
    'O2': [(-30, 50), (-56, 54), (-70, 30), (-72, 2), (-68, -26), (-56, -44), (-40, -44)],
    'I2': [(-30, 50), (-46, 32), (-46, -26), (-40, -44)],
    'C':  [(-40, -44), (-22, -54), (0, -52)],
}

def poly_len(p):
    return sum(math.dist(p[i], p[i + 1]) for i in range(len(p) - 1))

def poly_at(p, t):
    """Point à la distance t le long de la polyligne."""
    for i in range(len(p) - 1):
        L = math.dist(p[i], p[i + 1])
        if t <= L or i == len(p) - 2:
            f = min(1.0, t / L) if L else 0
            return (p[i][0] + (p[i + 1][0] - p[i][0]) * f, p[i][1] + (p[i + 1][1] - p[i][1]) * f)
        t -= L

samples = []   # (x, z, seg)
for name, p in SEG.items():
    L = poly_len(p)
    n = int(L / 0.5)
    for k in range(n + 1):
        x, z = poly_at(p, L * k / n)
        samples.append((x, z, name))

_ph_cache = {}
def ph_at(x, z, seg):
    if seg == 'I2':
        return 64
    key = (round(x * 2), round(z * 2))
    if key not in _ph_cache:
        acc, cnt = 0.0, 0
        for dx in range(-4, 5):
            for dz in range(-4, 5):
                if dx * dx + dz * dz <= 16:
                    acc += H0(x + dx, z + dz); cnt += 1
        _ph_cache[key] = max(64, round(acc / cnt))
    return _ph_cache[key]

samples = [(x, z, s, ph_at(x, z, s)) for (x, z, s) in samples]

# grille de recherche des échantillons
buck = {}
for i, (x, z, s, p) in enumerate(samples):
    buck.setdefault((math.floor(x / 4), math.floor(z / 4)), []).append(i)

def nearest(x, z):
    best, bi = 1e9, -1
    cx, cz = math.floor(x / 4), math.floor(z / 4)
    for gx in range(cx - 2, cx + 3):
        for gz in range(cz - 2, cz + 3):
            for i in buck.get((gx, gz), ()):
                d = (samples[i][0] - x) ** 2 + (samples[i][1] - z) ** 2
                if d < best:
                    best, bi = d, i
    return (math.sqrt(best), bi) if bi >= 0 else (99, -1)

# ------------------------------------------------------------------ cases (graphe)
S_START, S_BLUE, S_RED, S_EVENT, S_TRAP, S_FORK = 0, 1, 2, 3, 4, 5
WEIGHTS = {  # bleue, rouge, événement, piège
    'A': (60, 15, 20, 5), 'B': (60, 15, 20, 5), 'C': (60, 15, 20, 5),
    'O1': (65, 10, 25, 0), 'I1': (35, 30, 15, 20),
    'O2': (60, 15, 25, 0), 'I2': (40, 20, 25, 15),
}
SPACING = 7

def seg_points(name, include_start, include_end):
    p = SEG[name]
    L = poly_len(p)
    n = max(2, round(L / SPACING))
    ks = range(0 if include_start else 1, (n + 1) if include_end else n)
    out = []
    for k in ks:
        x, z = poly_at(p, L * k / n)
        out.append((round(x), round(z)))
    return out

nodes = []   # dict(x, z, y, seg, type)
def add_nodes(name, pts):
    ids = []
    for (x, z) in pts:
        nodes.append({'x': x, 'z': z, 'seg': name, 'y': ph_at(x, z, name)})
        ids.append(len(nodes) - 1)
    return ids

A = add_nodes('A', seg_points('A', True, True))           # départ ... embranchement 1
O1 = add_nodes('O1', seg_points('O1', False, False))
I1 = add_nodes('I1', seg_points('I1', False, False))
B = add_nodes('B', seg_points('B', True, True))           # jonction 1 ... embranchement 2
O2 = add_nodes('O2', seg_points('O2', False, False))
I2 = add_nodes('I2', seg_points('I2', False, False))
C = add_nodes('C', seg_points('C', True, False))          # jonction 2 ... (retour au départ)
N = len(nodes)
FORK1, JOIN1, FORK2, JOIN2 = A[-1], B[0], B[-1], C[0]

nxt, alt, prv = [None] * N, [None] * N, [None] * N
def chain(ids, after):
    for a, b in zip(ids, ids[1:]):
        nxt[a] = b
    nxt[ids[-1]] = after
chain(A, O1[0]); alt[FORK1] = I1[0]
chain(O1, JOIN1); chain(I1, JOIN1)
chain(B, O2[0]); alt[FORK2] = I2[0]
chain(O2, JOIN2); chain(I2, JOIN2)
chain(C, A[0])
for i in range(N):
    for j in (nxt[i], alt[i]):
        if j is not None and prv[j] is None:
            prv[j] = i
assert all(v is not None for v in nxt) and all(v is not None for v in prv)

for i, nd in enumerate(nodes):
    if i == 0: nd['type'] = S_START; continue
    if i in (FORK1, FORK2): nd['type'] = S_FORK; continue
    w = WEIGHTS[nd['seg']]
    t = random.choices([S_BLUE, S_RED, S_EVENT, S_TRAP], weights=w)[0]
    if t == S_TRAP and nodes[prv[i]].get('type') == S_TRAP:
        t = S_BLUE
    nd['type'] = t

# ------------------------------------------------------------------ colonnes de terrain
R = range(-HALF, HALF + 1)
col = {}          # (x,z) -> dict(h, top, sub, core, water, zone, d)
carve = []        # échantillons du tunnel
CASE_CELLS = set()
for nd in nodes:
    for dx in (-1, 0, 1):
        for dz in (-1, 0, 1):
            CASE_CELLS.add((nd['x'] + dx, nd['z'] + dz))

PATH_MAT = {'village': 'stone_bricks', 'meadow': 'dirt_path', 'forest': 'dirt_path', 'castle': 'stone_bricks',
            'beach': 'smooth_sandstone', 'desert': 'cut_sandstone', 'volcano': 'polished_blackstone_bricks',
            'mountain': 'packed_ice', 'frost': 'spruce_planks'}

def pick(n, opts):
    return opts[min(len(opts) - 1, int(n * len(opts)))]

for x in R:
    for z in R:
        zn = zone(x, z)
        m = max(abs(x), abs(z))
        e = sq(x, z)
        c = {'zone': zn, 'water': None, 'core': 'stone', 'sub': 'dirt', 'top': 'grass_block', 'd': 99, 'land': True}
        if m >= 88:
            c.update(h=63 + int(vn(x, z, 3, 9) * 3.99), top=pick(vn(x, z, 2, 10), ['stone', 'andesite', 'mossy_cobblestone', 'cobblestone']),
                     sub='stone', zone='rim')
            col[(x, z)] = c; continue
        if e >= 1.0 or (zn != 'beach' and e >= 0.985):
            sb = int(58 - min(6, max(0, (e - 1)) * 40)) if e >= 1 else 57
            c.update(h=sb, top='sand' if (x > 30 or vn(x, z, 6, 11) > 0.5) else 'gravel', sub='sand', water=SEA, zone='ocean', land=False)
            col[(x, z)] = c; continue
        h0 = H0(x, z)
        d, si = nearest(x, z)
        h = round(h0)
        tunnel = False
        if si >= 0:
            sx, sz, sseg, sph = samples[si]
            c['d'] = d
            tunnel = sseg == 'I2' and h0 > sph + 5
            if d <= 2.0:
                if tunnel:
                    carve.append((x, z, sph, d))
                else:
                    h = sph
            elif d <= 5.5 and not tunnel:
                t = (d - 2.0) / 3.5
                h = round(sph * (1 - t) + h0 * t)
        rv = math.hypot(x - VOL[0], z - VOL[1])
        rm = math.hypot(x - MNT[0], z - MNT[1])
        rc = math.hypot(x, z)
        n1 = vn(x, z, 3, 8)
        if zn == 'forest':
            c['top'] = 'podzol' if vn(x, z, 6, 7) > 0.66 else ('moss_block' if vn(x, z, 6, 7) < 0.18 else 'grass_block')
        elif zn == 'village':
            if math.hypot(x, z + 52) < 8.5:
                c['top'] = 'stone_bricks' if (x + z) % 3 else 'cobblestone'
        elif zn == 'castle':
            if rc < 9: c['top'] = 'stone_bricks'
        elif zn == 'beach':
            c.update(top='sand', sub='sandstone')
        elif zn == 'desert':
            c.update(top='red_sand' if vn(x, z, 8, 12) > 0.78 else 'sand', sub='sandstone')
        elif zn == 'volcano':
            c.update(sub='blackstone', core='basalt')
            ang = math.atan2(z - VOL[1], x - VOL[0])
            streak = abs(((ang * 7 / math.pi) % 2) - 1) < 0.07 and 6 < rv < 21
            if rv > 21:
                c['top'] = pick(n1, ['coarse_dirt', 'gravel', 'coarse_dirt', 'tuff'])
            elif streak:
                c['top'] = 'magma_block'
            else:
                c['top'] = pick(n1, ['blackstone', 'basalt', 'tuff', 'blackstone', 'smooth_basalt'])
            if rv < 4.6:
                h = 92; c.update(top='lava', sub='blackstone')
        elif zn == 'mountain':
            if h >= 88: c['top'] = 'snow_block'
            elif h >= 78: c['top'] = 'snow_block' if n1 > 0.45 else 'stone'
            elif rm > 20: c['top'] = 'grass_block'
            else: c['top'] = pick(n1, ['stone', 'andesite', 'gravel', 'stone', 'cobblestone'])
            if c['top'] != 'grass_block': c['sub'] = 'stone'
        elif zn == 'frost':
            c['top'] = 'snow_block'
            if math.hypot(x - LAKE[0], z - LAKE[1]) < LR and c['d'] > 4:
                h = 63; c['top'] = 'packed_ice'
        if c['d'] <= 1.5 and not tunnel:
            c['top'] = PATH_MAT.get(zn, 'dirt_path')
        if h < 63:
            c.update(water=SEA, land=False, top='sand' if zn in ('beach', 'desert') else 'gravel', sub='sand')
        c['h'] = h
        col[(x, z)] = c

# ------------------------------------------------------------------ émission du terrain (rectangles fusionnés)
def sig(c):
    return (c['h'], c['top'], c['sub'], c['core'], c['water'])

terrain = []
seen = set()
xs = list(R)
for x in xs:
    for z in xs:
        if (x, z) in seen: continue
        s = sig(col[(x, z)])
        w = 1
        while w < 16 and (x, z + w) in col and (x, z + w) not in seen and sig(col[(x, z + w)]) == s:
            w += 1
        hgt = 1
        while hgt < 16 and all((x + hgt, z + k) in col and (x + hgt, z + k) not in seen and sig(col[(x + hgt, z + k)]) == s for k in range(w)):
            hgt += 1
        for a in range(hgt):
            for k in range(w):
                seen.add((x + a, z + k))
        h, top, sub, core, water = s
        x1, x2, z1, z2 = x, x + hgt - 1, ZC + z, ZC + z + w - 1
        if h - 4 >= YB:
            terrain.append(f'fill {x1} {YB} {z1} {x2} {h - 4} {z2} minecraft:{core}')
        terrain.append(f'fill {x1} {max(YB, h - 3)} {z1} {x2} {h - 1} {z2} minecraft:{sub}')
        terrain.append(f'fill {x1} {h} {z1} {x2} {h} {z2} minecraft:{top}')
        if water and h + 1 <= water:
            terrain.append(f'fill {x1} {h + 1} {z1} {x2} {water} {z2} minecraft:water')

# ------------------------------------------------------------------ tunnel de la grotte de glace
tunnel_cmds = []
done = set()
tun =[s for s in samples if s[2] == 'I2']
for i, (x, z, s, p) in enumerate(tun):
    cx, cz = round(x), round(z)
    if (cx, cz) in done: continue
    if H0(cx, cz) <= p + 5: continue
    done.add((cx, cz))
    tunnel_cmds.append(f'fill {cx - 2} {p + 1} {ZC + cz - 2} {cx + 2} {p + 5} {ZC + cz + 2} minecraft:air')
    tunnel_cmds.append(f'fill {cx - 1} {p} {ZC + cz - 1} {cx + 1} {p} {ZC + cz + 1} minecraft:packed_ice')
for i, (x, z, s, p) in enumerate(tun[::12]):
    cx, cz = round(x), round(z)
    if H0(cx, cz) > p + 6:
        tunnel_cmds.append(f'setblock {cx} {p + 6} {ZC + cz} minecraft:sea_lantern')
        tunnel_cmds.append(f'fill {cx - 3} {p + 1} {ZC + cz} {cx - 3} {p + 4} {ZC + cz} minecraft:blue_ice')
        tunnel_cmds.append(f'fill {cx + 3} {p + 1} {ZC + cz} {cx + 3} {p + 4} {ZC + cz} minecraft:blue_ice')

# ------------------------------------------------------------------ cases
CASE_BLOCK = {S_START: 'gold_block', S_BLUE: 'blue_concrete', S_RED: 'red_concrete', S_EVENT: 'lime_concrete',
              S_TRAP: 'black_concrete', S_FORK: 'quartz_block'}
case_cmds = []
for nd in nodes:
    x, z, y = nd['x'], ZC + nd['z'], nd['y']
    case_cmds.append(f'fill {x - 1} {y} {z - 1} {x + 1} {y} {z + 1} minecraft:{CASE_BLOCK[nd["type"]]}')
    case_cmds.append(f'fill {x - 1} {y + 1} {z - 1} {x + 1} {y + 3} {z + 1} minecraft:air')
    if nd['type'] == S_FORK:
        case_cmds.append(f'setblock {x} {y} {z} minecraft:chiseled_quartz_block')

# ------------------------------------------------------------------ décor
occ = set()
def free(x, z, r):
    for dx in range(-r, r + 1):
        for dz in range(-r, r + 1):
            if (x + dx, z + dz) in occ: return False
    return True
def take(x, z, r):
    for dx in range(-r, r + 1):
        for dz in range(-r, r + 1):
            occ.add((x + dx, z + dz))
def ok_ground(x, z, r=0, dmin=3.5):
    for dx in range(-r, r + 1):
        for dz in range(-r, r + 1):
            c = col.get((x + dx, z + dz))
            if c is None or not c['land'] or c['d'] < dmin or (x + dx, z + dz) in CASE_CELLS: return False
    return True
def H(x, z): return col[(x, z)]['h']
def W(z): return ZC + z

deco = []
def B(cmd): deco.append(cmd)

def tree(x, z, kind='oak'):
    y = H(x, z) + 1; t = random.randint(4, 6)
    log, lv = f'{kind}_log', f'{kind}_leaves[persistent=true]'
    B(f'fill {x} {y} {W(z)} {x} {y + t - 1} {W(z)} minecraft:{log}')
    B(f'fill {x - 2} {y + t - 2} {W(z - 2)} {x + 2} {y + t - 1} {W(z + 2)} minecraft:{lv} replace air')
    B(f'fill {x - 1} {y + t} {W(z - 1)} {x + 1} {y + t + 1} {W(z + 1)} minecraft:{lv} replace air')

def dark_oak(x, z):
    y = H(x, z) + 1; t = random.randint(5, 7)
    B(f'fill {x} {y} {W(z)} {x + 1} {y + t - 1} {W(z + 1)} minecraft:dark_oak_log')
    B(f'fill {x - 3} {y + t - 2} {W(z - 3)} {x + 4} {y + t} {W(z + 4)} minecraft:dark_oak_leaves[persistent=true] replace air')
    B(f'fill {x - 1} {y + t + 1} {W(z - 1)} {x + 2} {y + t + 1} {W(z + 2)} minecraft:dark_oak_leaves[persistent=true] replace air')

def spruce(x, z, snowy=True):
    y = H(x, z) + 1; t = random.randint(6, 9)
    lv = 'spruce_leaves[persistent=true]'
    B(f'fill {x} {y} {W(z)} {x} {y + t - 1} {W(z)} minecraft:spruce_log')
    for k, r in ((2, 2), (4, 2), (5, 1), (t - 1, 1)):
        if k < t:
            B(f'fill {x - r} {y + k} {W(z - r)} {x + r} {y + k} {W(z + r)} minecraft:{lv} replace air')
    B(f'setblock {x} {y + t} {W(z)} minecraft:{lv}')
    if snowy:
        B(f'setblock {x} {y + t + 1} {W(z)} minecraft:snow')

def palm(x, z):
    y = H(x, z) + 1; t = random.randint(6, 8)
    dx, dz = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
    B(f'fill {x} {y} {W(z)} {x} {y + 3} {W(z)} minecraft:jungle_log')
    tx, tz = x + dx, z + dz
    B(f'fill {tx} {y + 4} {W(tz)} {tx} {y + t - 1} {W(tz)} minecraft:jungle_log')
    top = y + t
    lv = 'jungle_leaves[persistent=true]'
    B(f'setblock {tx} {top} {W(tz)} minecraft:{lv}')
    for ax, az in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        B(f'fill {tx + ax} {top} {W(tz + az)} {tx + ax * 2} {top} {W(tz + az * 2)} minecraft:{lv} replace air')
        B(f'setblock {tx + ax * 3} {top - 1} {W(tz + az * 3)} minecraft:{lv}')
    for ax, az in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        B(f'setblock {tx + ax} {top} {W(tz + az)} minecraft:{lv}')
        B(f'setblock {tx + ax * 2} {top - 1} {W(tz + az * 2)} minecraft:{lv}')

def mushroom(x, z):
    y = H(x, z) + 1; t = random.randint(4, 6)
    B(f'fill {x} {y} {W(z)} {x} {y + t - 1} {W(z)} minecraft:mushroom_stem')
    if random.random() < 0.5:
        B(f'fill {x - 2} {y + t} {W(z - 2)} {x + 2} {y + t} {W(z + 2)} minecraft:red_mushroom_block')
        B(f'fill {x - 1} {y + t + 1} {W(z - 1)} {x + 1} {y + t + 1} {W(z + 1)} minecraft:red_mushroom_block')
        for k in (-2, 2):
            B(f'fill {x - 1} {y + t - 1} {W(z + k)} {x + 1} {y + t - 1} {W(z + k)} minecraft:red_mushroom_block')
            B(f'fill {x + k} {y + t - 1} {W(z - 1)} {x + k} {y + t - 1} {W(z + 1)} minecraft:red_mushroom_block')
    else:
        B(f'fill {x - 3} {y + t} {W(z - 3)} {x + 3} {y + t} {W(z + 3)} minecraft:brown_mushroom_block')
        B(f'fill {x - 3} {y + t} {W(z - 3)} {x - 3} {y + t} {W(z - 3)} minecraft:air')
        B(f'fill {x + 3} {y + t} {W(z + 3)} {x + 3} {y + t} {W(z + 3)} minecraft:air')
        B(f'fill {x - 3} {y + t} {W(z + 3)} {x - 3} {y + t} {W(z + 3)} minecraft:air')
        B(f'fill {x + 3} {y + t} {W(z - 3)} {x + 3} {y + t} {W(z - 3)} minecraft:air')

def boulder(x, z, mats=('mossy_cobblestone', 'andesite', 'cobblestone')):
    y = H(x, z) + 1
    B(f'fill {x} {y} {W(z)} {x + 1} {y} {W(z + 1)} minecraft:{random.choice(mats)}')
    B(f'setblock {x} {y + 1} {W(z)} minecraft:{random.choice(mats)}')

def plant(x, z, block):
    B(f'setblock {x} {H(x, z) + 1} {W(z)} minecraft:{block}')

def lamp(x, z):
    y = H(x, z) + 1
    B(f'fill {x} {y} {W(z)} {x} {y + 1} {W(z)} minecraft:oak_fence')
    B(f'setblock {x} {y + 2} {W(z)} minecraft:lantern')

def cactus(x, z):
    y = H(x, z) + 1
    B(f'fill {x} {y} {W(z)} {x} {y + random.randint(0, 2)} {W(z)} minecraft:cactus')

def ice_spike(x, z):
    y = H(x, z) + 1; t = random.randint(5, 11)
    B(f'fill {x} {y} {W(z)} {x} {y + t} {W(z)} minecraft:packed_ice')
    B(f'fill {x - 1} {y} {W(z)} {x + 1} {y + t // 3} {W(z)} minecraft:packed_ice')
    B(f'fill {x} {y} {W(z - 1)} {x} {y + t // 3} {W(z + 1)} minecraft:packed_ice')

def basalt_pillar(x, z):
    y = H(x, z) + 1
    B(f'fill {x} {y} {W(z)} {x} {y + random.randint(2, 6)} {W(z)} minecraft:basalt')

def flat_pad(x1, z1, x2, z2, y, block):
    B(f'fill {x1} {y} {W(z1)} {x2} {y} {W(z2)} minecraft:{block}')
    B(f'fill {x1} {y - 4} {W(z1)} {x2} {y - 1} {W(z2)} minecraft:dirt replace air')
    B(f'fill {x1} {y + 1} {W(z1)} {x2} {y + 12} {W(z2)} minecraft:air')

def house(x, z, wall='oak_planks', roof='dark_oak_planks', frame='oak_log', door='s'):
    y = max(H(x + dx, z + dz) for dx in (-3, 3) for dz in (-3, 3))
    flat_pad(x - 4, z - 4, x + 4, z + 4, y, 'cobblestone')
    B(f'fill {x - 3} {y + 1} {W(z - 3)} {x + 3} {y + 4} {W(z + 3)} minecraft:{wall} hollow')
    for cx in (x - 3, x + 3):
        for cz in (z - 3, z + 3):
            B(f'fill {cx} {y + 1} {W(cz)} {cx} {y + 4} {W(cz)} minecraft:{frame}')
    B(f'fill {x - 1} {y + 2} {W(z - 3)} {x + 1} {y + 3} {W(z - 3)} minecraft:glass')
    B(f'fill {x - 1} {y + 2} {W(z + 3)} {x + 1} {y + 3} {W(z + 3)} minecraft:glass')
    B(f'fill {x - 3} {y + 2} {W(z)} {x - 3} {y + 3} {W(z)} minecraft:glass')
    B(f'fill {x + 3} {y + 2} {W(z)} {x + 3} {y + 3} {W(z)} minecraft:glass')
    dz = 3 if door == 's' else -3
    B(f'fill {x} {y + 2} {W(z + dz)} {x} {y + 3} {W(z + dz)} minecraft:air')
    B(f'setblock {x + 1} {y + 4} {W(z + dz + (1 if dz > 0 else -1))} minecraft:lantern')
    for k in range(5):
        r = 4 - k
        B(f'fill {x - r} {y + 5 + k} {W(z - r)} {x + r} {y + 5 + k} {W(z + r)} minecraft:{roof}')
    B(f'fill {x + 2} {y + 6} {W(z - 1)} {x + 2} {y + 9} {W(z - 1)} minecraft:bricks')

def stall(x, z, wool):
    y = H(x, z) + 1
    for cx in (x - 1, x + 1):
        for cz in (z - 1, z + 1):
            B(f'fill {cx} {y} {W(cz)} {cx} {y + 2} {W(cz)} minecraft:oak_fence')
    B(f'fill {x - 2} {y + 3} {W(z - 2)} {x + 2} {y + 3} {W(z + 2)} minecraft:{wool}')
    B(f'fill {x - 1} {y} {W(z)} {x + 1} {y} {W(z)} minecraft:barrel')
    B(f'setblock {x} {y + 1} {W(z)} minecraft:pumpkin')

def umbrella(x, z, wool):
    y = H(x, z) + 1
    B(f'fill {x} {y} {W(z)} {x} {y + 2} {W(z)} minecraft:birch_fence')
    B(f'fill {x - 1} {y + 3} {W(z - 1)} {x + 1} {y + 3} {W(z + 1)} minecraft:{wool}')
    B(f'setblock {x} {y + 4} {W(z)} minecraft:{wool}')
    B(f'setblock {x + 1} {y} {W(z + 1)} minecraft:yellow_carpet')
    B(f'setblock {x + 1} {y} {W(z + 2)} minecraft:yellow_carpet')

# --- structures fixes (enregistrées avant le semis aléatoire)
# Château de l'Étoile (centre)
CASTLE = [
    'fill -8 60 14992 8 72 15008 minecraft:stone_bricks',
    'fill -6 73 14994 6 81 15006 minecraft:stone_bricks hollow',
    'fill -5 74 14995 5 80 15005 minecraft:air',
    'fill -1 73 14994 1 76 14994 minecraft:air',
    'fill -2 77 14994 2 77 14994 minecraft:chiseled_stone_bricks',
    'fill -6 82 14994 6 82 15006 minecraft:stone_brick_wall hollow',
    'fill -5 82 14995 5 82 15005 minecraft:air',
]
for wx in (-3, 3):
    CASTLE.append(f'fill {wx} 77 14994 {wx} 78 14994 minecraft:glass')
    CASTLE.append(f'fill {wx} 77 15006 {wx} 78 15006 minecraft:glass')
    CASTLE.append(f'fill -6 77 {15000 + wx} -6 78 {15000 + wx} minecraft:glass')
    CASTLE.append(f'fill 6 77 {15000 + wx} 6 78 {15000 + wx} minecraft:glass')
for tx in (-6, 6):
    for tz in (-6, 6):
        z = 15000 + tz
        CASTLE += [f'fill {tx - 2} 73 {z - 1} {tx + 2} 88 {z + 1} minecraft:stone_bricks',
                   f'fill {tx - 1} 73 {z - 2} {tx + 1} 88 {z + 2} minecraft:stone_bricks',
                   f'fill {tx - 2} 89 {z - 1} {tx + 2} 89 {z + 1} minecraft:red_terracotta',
                   f'fill {tx - 1} 89 {z - 2} {tx + 1} 89 {z + 2} minecraft:red_terracotta',
                   f'fill {tx - 1} 90 {z - 1} {tx + 1} 90 {z + 1} minecraft:red_terracotta',
                   f'setblock {tx} 91 {z} minecraft:red_terracotta',
                   f'setblock {tx} 92 {z} minecraft:gold_block',
                   f'setblock {tx} 84 {z - 2 if tz < 0 else z + 2} minecraft:glass']
CASTLE += ['fill -2 82 14998 2 95 15002 minecraft:quartz_block hollow',
           'fill -3 96 14997 3 96 15003 minecraft:gold_block',
           'fill -2 97 14998 2 97 15002 minecraft:gold_block',
           'setblock 0 98 15000 minecraft:beacon',
           'fill -1 88 14998 1 90 14998 minecraft:glass',
           'setblock 0 99 15000 minecraft:yellow_stained_glass']
for k in range(-6, 7, 2):
    CASTLE.append(f'setblock {k} 82 14994 minecraft:lantern')
for cell in [(x, z) for x in range(-9, 10) for z in range(-9, 10)]:
    occ.add(cell)

# Village : place, fontaine, maisons, étals
F_X, F_Z = 0, -61
village = []
yv = H(F_X, F_Z)
village += [f'fill {F_X - 3} {yv} {W(F_Z - 3)} {F_X + 3} {yv} {W(F_Z + 3)} minecraft:stone_bricks',
            f'fill {F_X - 3} {yv + 1} {W(F_Z - 3)} {F_X + 3} {yv + 1} {W(F_Z + 3)} minecraft:stone_brick_wall hollow',
            f'fill {F_X - 2} {yv + 1} {W(F_Z - 2)} {F_X + 2} {yv + 1} {W(F_Z + 2)} minecraft:water',
            f'fill {F_X} {yv + 1} {W(F_Z)} {F_X} {yv + 3} {W(F_Z)} minecraft:chiseled_stone_bricks',
            f'setblock {F_X} {yv + 4} {W(F_Z)} minecraft:sea_lantern']
take(F_X, F_Z, 4)
deco += village
for (hx, hz, wall, roof, door) in [(-22, -66, 'oak_planks', 'dark_oak_planks', 's'), (-11, -69, 'spruce_planks', 'red_terracotta', 's'),
                                   (11, -69, 'birch_planks', 'blue_terracotta', 's'), (22, -66, 'oak_planks', 'spruce_planks', 's'),
                                   (35, -64, 'bricks', 'dark_oak_planks', 's'), (-16, -41, 'spruce_planks', 'dark_oak_planks', 'n'),
                                   (16, -41, 'oak_planks', 'red_terracotta', 'n')]:
    if ok_ground(hx, hz, 4, 3.0) and free(hx, hz, 4):
        house(hx, hz, wall, roof, 'oak_log', door); take(hx, hz, 5)
for (sx, sz, w) in [(-9, -59, 'red_wool'), (9, -59, 'yellow_wool'), (-5, -44, 'lime_wool'), (5, -44, 'light_blue_wool')]:
    if ok_ground(sx, sz, 2, 2.6) and free(sx, sz, 2):
        stall(sx, sz, w); take(sx, sz, 2)

# Plage : ponton, poste de secours, parasols
yb = SEA + 1
deco += [f'fill 70 {yb} {W(-13)} 86 {yb} {W(-11)} minecraft:oak_planks',
         f'fill 86 {yb} {W(-15)} 88 {yb} {W(-9)} minecraft:oak_planks']
for px in range(72, 87, 4):
    deco += [f'fill {px} 52 {W(-14)} {px} {yb} {W(-14)} minecraft:oak_log', f'fill {px} 52 {W(-10)} {px} {yb} {W(-10)} minecraft:oak_log',
             f'setblock {px} {yb + 1} {W(-14)} minecraft:oak_fence', f'setblock {px} {yb + 2} {W(-14)} minecraft:lantern']
for (ux, uz, w) in [(64, -30, 'red_wool'), (66, -18, 'white_wool'), (64, 0, 'orange_wool'), (66, 20, 'cyan_wool'),
                    (64, 38, 'pink_wool'), (60, 52, 'yellow_wool')]:
    if ok_ground(ux, uz, 2, 2.6) and free(ux, uz, 2):
        umbrella(ux, uz, w); take(ux, uz, 2)
lx, lz = 67, 8
if ok_ground(lx, lz, 1, 2.6):
    y = H(lx, lz) + 1
    deco += [f'fill {lx - 1} {y} {W(lz - 1)} {lx - 1} {y + 3} {W(lz - 1)} minecraft:spruce_fence', f'fill {lx + 1} {y} {W(lz - 1)} {lx + 1} {y + 3} {W(lz - 1)} minecraft:spruce_fence',
             f'fill {lx - 1} {y} {W(lz + 1)} {lx - 1} {y + 3} {W(lz + 1)} minecraft:spruce_fence', f'fill {lx + 1} {y} {W(lz + 1)} {lx + 1} {y + 3} {W(lz + 1)} minecraft:spruce_fence',
             f'fill {lx - 1} {y + 4} {W(lz - 1)} {lx + 1} {y + 4} {W(lz + 1)} minecraft:spruce_planks',
             f'fill {lx - 1} {y + 5} {W(lz - 1)} {lx + 1} {y + 5} {W(lz + 1)} minecraft:red_wool',
             f'setblock {lx} {y + 6} {W(lz)} minecraft:white_wool']
    take(lx, lz, 2)

# Désert : pyramide et oasis
PX, PZ = -6, 44
yp = max(H(PX + dx, PZ + dz) for dx in (-7, 7) for dz in (-7, 7))
for k in range(8):
    r = 7 - k
    deco.append(f'fill {PX - r} {yp + k} {W(PZ - r)} {PX + r} {yp + k} {W(PZ + r)} minecraft:{"smooth_sandstone" if k % 2 else "sandstone"}')
deco += [f'fill {PX - 7} {yp - 5} {W(PZ - 7)} {PX + 7} {yp - 1} {W(PZ + 7)} minecraft:sandstone',
         f'setblock {PX} {yp + 8} {W(PZ)} minecraft:gold_block',
         f'fill {PX - 1} {yp} {W(PZ + 7)} {PX + 1} {yp + 2} {W(PZ + 7)} minecraft:chiseled_sandstone',
         f'fill {PX} {yp} {W(PZ + 7)} {PX} {yp + 1} {W(PZ + 7)} minecraft:air']
take(PX, PZ, 8)
OX, OZ = -28, 70
deco += [f'fill {OX - 5} 64 {W(OZ - 5)} {OX + 5} 64 {W(OZ + 5)} minecraft:sand',
         f'fill {OX - 5} 65 {W(OZ - 5)} {OX + 5} 70 {W(OZ + 5)} minecraft:air',
         f'fill {OX - 3} 64 {W(OZ - 3)} {OX + 3} 64 {W(OZ + 3)} minecraft:water',
         f'fill {OX - 3} 63 {W(OZ - 3)} {OX + 3} 63 {W(OZ + 3)} minecraft:sand',
         f'setblock {OX} 65 {W(OZ)} minecraft:lily_pad', f'setblock {OX + 1} 65 {W(OZ - 2)} minecraft:lily_pad']
for (ax, az) in ((OX - 5, OZ - 4), (OX + 5, OZ + 3), (OX - 4, OZ + 5)):
    col[(ax, az)]['h'] = 64
    palm(ax, az)
take(OX, OZ, 6)
for (rx, rz) in ((-24, 52), (10, 56), (-36, 64)):
    if ok_ground(rx, rz, 1, 3) and free(rx, rz, 1):
        y = H(rx, rz) + 1
        deco += [f'fill {rx} {y} {W(rz)} {rx} {y + random.randint(2, 4)} {W(rz)} minecraft:chiseled_sandstone',
                 f'setblock {rx + 1} {y} {W(rz)} minecraft:cut_sandstone_slab']
        take(rx, rz, 1)

# Volcan : feux de camp à fumée sur le bord du cratère
for k in range(8):
    a = k * math.pi / 4
    vx, vz = round(VOL[0] + 6.5 * math.cos(a)), round(VOL[1] + 6.5 * math.sin(a))
    y = H(vx, vz)
    deco += [f'setblock {vx} {y} {W(vz)} minecraft:hay_block', f'setblock {vx} {y + 1} {W(vz)} minecraft:campfire[lit=true,signal_fire=true]']
for cell in [(VOL[0] + dx, VOL[1] + dz) for dx in range(-8, 9) for dz in range(-8, 9)]:
    occ.add(cell)

# Igloo
IX, IZ = -54, 36
yi = H(IX, IZ)
for dx in range(-3, 4):
    for dz in range(-3, 4):
        for dy in range(0, 4):
            r = math.sqrt(dx * dx + dz * dz + (dy * 1.2) ** 2)
            if 2.4 < r <= 3.5:
                deco.append(f'setblock {IX + dx} {yi + 1 + dy} {W(IZ + dz)} minecraft:snow_block')
deco += [f'fill {IX} {yi + 1} {W(IZ + 3)} {IX} {yi + 2} {W(IZ + 3)} minecraft:air', f'setblock {IX} {yi + 1} {W(IZ)} minecraft:lantern']
take(IX, IZ, 4)

# Entrées de la grotte de glace (arches) et panneau
for ez in (18, -27):
    p = 64
    deco += [f'fill -49 {p + 1} {W(ez)} -49 {p + 6} {W(ez)} minecraft:packed_ice', f'fill -43 {p + 1} {W(ez)} -43 {p + 6} {W(ez)} minecraft:packed_ice',
             f'fill -49 {p + 7} {W(ez)} -43 {p + 7} {W(ez)} minecraft:blue_ice', f'setblock -46 {p + 6} {W(ez)} minecraft:sea_lantern']

# Prairie : moulin, fermes, étang, champs de tulipes
def windmill(x, z):
    y = H(x, z)
    flat_pad(x - 3, z - 3, x + 3, z + 3, y, 'cobblestone')
    B(f'fill {x - 2} {y + 1} {W(z - 2)} {x + 2} {y + 9} {W(z + 2)} minecraft:stone_bricks hollow')
    B(f'fill {x - 2} {y + 1} {W(z - 2)} {x - 2} {y + 9} {W(z - 2)} minecraft:air')
    B(f'fill {x + 2} {y + 1} {W(z + 2)} {x + 2} {y + 9} {W(z + 2)} minecraft:air')
    B(f'fill {x - 2} {y + 1} {W(z + 2)} {x - 2} {y + 9} {W(z + 2)} minecraft:air')
    B(f'fill {x + 2} {y + 1} {W(z - 2)} {x + 2} {y + 9} {W(z - 2)} minecraft:air')
    B(f'fill {x - 2} {y + 10} {W(z - 2)} {x + 2} {y + 10} {W(z + 2)} minecraft:dark_oak_planks')
    B(f'fill {x - 1} {y + 11} {W(z - 1)} {x + 1} {y + 11} {W(z + 1)} minecraft:dark_oak_planks')
    B(f'fill {x} {y + 2} {W(z + 2)} {x} {y + 3} {W(z + 2)} minecraft:air')
    hz = W(z + 3); hy = y + 8
    B(f'setblock {x} {hy} {hz} minecraft:oak_log')
    B(f'fill {x} {hy + 1} {hz} {x} {hy + 6} {hz} minecraft:white_wool')
    B(f'fill {x} {hy - 6} {hz} {x} {hy - 1} {hz} minecraft:white_wool')
    B(f'fill {x + 1} {hy} {hz} {x + 6} {hy} {hz} minecraft:white_wool')
    B(f'fill {x - 6} {hy} {hz} {x - 1} {hy} {hz} minecraft:white_wool')
    B(f'fill {x + 1} {hy + 1} {hz} {x + 1} {hy + 6} {hz} minecraft:oak_planks')
    B(f'fill {x - 1} {hy - 6} {hz} {x - 1} {hy - 1} {hz} minecraft:oak_planks')
    B(f'fill {x + 1} {hy - 1} {hz} {x + 6} {hy - 1} {hz} minecraft:oak_planks')
    B(f'fill {x - 6} {hy + 1} {hz} {x - 1} {hy + 1} {hz} minecraft:oak_planks')

def farm(x, z):
    y = H(x, z)
    flat_pad(x - 5, z - 5, x + 5, z + 5, y, 'grass_block')
    B(f'fill {x - 4} {y} {W(z - 4)} {x + 4} {y} {W(z + 4)} minecraft:farmland[moisture=7]')
    B(f'fill {x - 4} {y + 1} {W(z - 4)} {x + 4} {y + 1} {W(z + 4)} minecraft:wheat[age=7]')
    B(f'fill {x - 4} {y} {W(z)} {x + 4} {y} {W(z)} minecraft:water')
    B(f'fill {x - 4} {y + 1} {W(z)} {x + 4} {y + 1} {W(z)} minecraft:air')
    B(f'fill {x - 1} {y + 1} {W(z - 2)} {x + 1} {y + 1} {W(z - 1)} minecraft:carrots[age=7]')
    B(f'fill {x - 1} {y + 1} {W(z + 1)} {x + 1} {y + 1} {W(z + 2)} minecraft:potatoes[age=7]')
    for k in range(-5, 6, 2):
        for (fx, fz) in ((x + k, z - 5), (x + k, z + 5), (x - 5, z + k), (x + 5, z + k)):
            B(f'setblock {fx} {y + 1} {W(fz)} minecraft:oak_fence')
    B(f'fill {x + 6} {y + 1} {W(z)} {x + 6} {y + 2} {W(z)} minecraft:oak_fence')
    B(f'setblock {x + 6} {y + 3} {W(z)} minecraft:hay_block')
    B(f'setblock {x + 6} {y + 4} {W(z)} minecraft:carved_pumpkin')

def pond(x, z, r=5):
    y = 64
    for dx in range(-r - 2, r + 3):
        for dz in range(-r - 2, r + 3):
            d = math.hypot(dx, dz * 1.4)
            if d <= r:
                B(f'setblock {x + dx} {y} {W(z + dz)} minecraft:water')
                B(f'setblock {x + dx} {y - 1} {W(z + dz)} minecraft:{"clay" if d < r - 2 else "sand"}')
                B(f'setblock {x + dx} {y + 1} {W(z + dz)} minecraft:air')
            elif d <= r + 1.5:
                B(f'setblock {x + dx} {y} {W(z + dz)} minecraft:grass_block')
    B(f'fill {x + r - 1} {y + 1} {W(z)} {x + r + 2} {y + 1} {W(z)} minecraft:spruce_slab')
    B(f'setblock {x + r - 1} {y + 2} {W(z - 1)} minecraft:lantern')
    for k in range(4):
        B(f'setblock {x + random.randint(-r + 1, r - 2)} {y + 1} {W(z + random.randint(-2, 2))} minecraft:lily_pad')

def tulips(x, z, w=10, d=6):
    y = H(x, z)
    colors = ['red_tulip', 'orange_tulip', 'white_tulip', 'pink_tulip', 'red_tulip', 'pink_tulip']
    flat_pad(x, z, x + w - 1, z + d - 1, y, 'grass_block')
    for k in range(d):
        B(f'fill {x} {y + 1} {W(z + k)} {x + w - 1} {y + 1} {W(z + k)} minecraft:{colors[k % len(colors)]}')

for (fn, x, z, r) in ((windmill, 26, -24, 7), (farm, -20, -20, 6), (farm, -22, 22, 6), (pond, 24, -2, 7), (tulips, -10, 24, 0), (tulips, 22, 12, 0)):
    cx, cz = (x + 5, z + 3) if fn is tulips else (x, z)
    rr = 6 if fn is tulips else r
    if ok_ground(cx, cz, rr, 2.6) and free(cx, cz, rr):
        fn(x, z); take(cx, cz, rr)
    else:
        print('structure ignorée', fn.__name__, x, z)

# --- semis aléatoire par zone
zcells = {}
for (x, z), c in col.items():
    zcells.setdefault(c['zone'], []).append((x, z))
for zn in zcells:
    random.shuffle(zcells[zn])

def scatter(zn, prob, fn, r, dmin=3.5, cond=None):
    for (x, z) in zcells.get(zn, []):
        if random.random() > prob: continue
        if cond and not cond(x, z): continue
        if not ok_ground(x, z, min(r, 1), dmin) or not free(x, z, r): continue
        fn(x, z); take(x, z, r)

def on_grass(x, z): return col[(x, z)]['top'] in ('grass_block', 'podzol', 'moss_block')
def on_sand(x, z): return col[(x, z)]['top'] in ('sand', 'red_sand')
def on_snow(x, z): return col[(x, z)]['top'] == 'snow_block'

scatter('castle', 0.002, tree, 3, cond=on_grass)
scatter('forest', 0.05, lambda x, z: dark_oak(x, z) if random.random() < 0.25 else tree(x, z, random.choice(['oak', 'birch', 'oak'])), 3, cond=on_grass)
scatter('forest', 0.01, mushroom, 3, cond=on_grass)
scatter('forest', 0.004, boulder, 1)
scatter('meadow', 0.012, lambda x, z: tree(x, z, random.choice(['oak', 'birch', 'oak'])), 3, cond=on_grass)
scatter('meadow', 0.003, boulder, 1)
scatter('meadow', 0.002, lambda x, z: plant(x, z, 'hay_block'), 1, cond=on_grass)
scatter('village', 0.004, tree, 3, cond=on_grass)
scatter('beach', 0.02, palm, 3, cond=lambda x, z: on_sand(x, z) and sq(x, z) < 0.95 and H(x, z) >= 63)
scatter('desert', 0.015, cactus, 1, cond=on_sand)
scatter('desert', 0.02, lambda x, z: plant(x, z, 'dead_bush'), 0, cond=on_sand)
scatter('volcano', 0.012, basalt_pillar, 1, cond=lambda x, z: math.hypot(x - VOL[0], z - VOL[1]) > 9)
scatter('volcano', 0.006, lambda x, z: boulder(x, z, ('obsidian', 'crying_obsidian', 'blackstone')), 1,
        cond=lambda x, z: math.hypot(x - VOL[0], z - VOL[1]) > 9)
scatter('mountain', 0.03, spruce, 2, cond=lambda x, z: H(x, z) < 80 and math.hypot(x - MNT[0], z - MNT[1]) > 12)
scatter('frost', 0.03, spruce, 2, cond=on_snow)
scatter('frost', 0.006, ice_spike, 1, cond=on_snow)
FLOWERS = ['poppy', 'dandelion', 'cornflower', 'oxeye_daisy', 'allium', 'azure_bluet', 'red_tulip', 'orange_tulip', 'lily_of_the_valley']
for zn, pf, pg in (('meadow', 0.07, 0.22), ('forest', 0.05, 0.25), ('village', 0.04, 0.1), ('castle', 0.08, 0.15)):
    for (x, z) in zcells.get(zn, []):
        if (x, z) in occ or not on_grass(x, z) or col[(x, z)]['d'] < 2.5 or (x, z) in CASE_CELLS: continue
        r = random.random()
        if r < pf: plant(x, z, random.choice(FLOWERS)); occ.add((x, z))
        elif r < pf + pg: plant(x, z, random.choice(['short_grass', 'short_grass', 'fern'])); occ.add((x, z))
# fond marin
for (x, z) in zcells.get('ocean', []):
    c = col[(x, z)]
    r = random.random()
    if c['h'] >= 56 and x > 30 and r < 0.04:
        B(f'setblock {x} {c["h"] + 1} {W(z)} minecraft:{random.choice(["brain_coral_block", "tube_coral_block", "fire_coral_block", "horn_coral_block", "bubble_coral_block"])}')
    elif r < 0.10:
        B(f'setblock {x} {c["h"] + 1} {W(z)} minecraft:seagrass')
    elif r < 0.13 and c['h'] <= 57:
        t = random.randint(1, 3)
        B(f'fill {x} {c["h"] + 1} {W(z)} {x} {c["h"] + t} {W(z)} minecraft:kelp_plant')
        B(f'setblock {x} {c["h"] + t + 1} {W(z)} minecraft:kelp')

# lampadaires le long du chemin (toutes les 3 cases, sur le côté)
for i, nd in enumerate(nodes):
    if i % 3 or nd['seg'] in ('I2',): continue
    j = nxt[i]
    dx, dz = nodes[j]['x'] - nd['x'], nodes[j]['z'] - nd['z']
    L = math.hypot(dx, dz) or 1
    lx, lz = round(nd['x'] - dz / L * 3), round(nd['z'] + dx / L * 3)
    c = col.get((lx, lz))
    if c and c['land'] and (lx, lz) not in CASE_CELLS and (lx, lz) not in occ:
        lamp(lx, lz); occ.add((lx, lz))

# ------------------------------------------------------------------ panneaux (text_display)
def disp(tags, x, y, z, text, scale, extra=''):
    tg = ','.join(f'"{t}"' for t in tags)
    return (f'summon minecraft:text_display {x} {y} {z} {{Tags:[{tg}],billboard:"center",text:{text},{extra}'
            f'transformation:{{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[{scale}f,{scale}f,{scale}f]}}}}')

LABEL = {S_START: ('DÉPART', 'gold'), S_BLUE: ('+3', 'aqua'), S_RED: ('-3', 'red'), S_EVENT: ('?', 'green'),
         S_TRAP: ('☠', 'dark_gray'), S_FORK: ('⇆', 'white')}
labels = ['kill @e[type=minecraft:text_display,tag=mg.mpdeco]']
for nd in nodes:
    t, c = LABEL[nd['type']]
    labels.append(disp(['mg.mpdeco'], nd['x'] + 0.5, nd['y'] + 1.6, W(nd['z']) + 0.5, f'[{{"text":"{t}","color":"{c}","bold":true}}]', 1.5))
ZONES = [(0, 84, -66, '⌂ VILLAGE DU DÉPART', 'gold'), (68, 80, -22, '☀ PLAGE DORÉE', 'yellow'),
         (VOL[0], 116, VOL[1], '♨ VOLCAN ARDENT', 'red'), (-6, 82, 58, '☼ DÉSERT DES MIRAGES', 'gold'),
         (MNT[0], 116, MNT[1], '❄ PICS GELÉS', 'aqua'), (-64, 78, 12, '❄ LAC GELÉ', 'aqua'),
         (-56, 84, -58, '♣ FORÊT ENCHANTÉE', 'green')]
for (zx, zy, zz, t, c) in ZONES:
    labels.append(disp(['mg.mpdeco'], zx + 0.5, zy, W(zz) + 0.5, f'[{{"text":"{t}","color":"{c}","bold":true}}]', 5))
labels.append(disp(['mg.mpdeco'], 0.5, 108, W(0) + 0.5,
                   '[{"text":"★ MINI PARTY ★","color":"gold","bold":true},{"text":"\\nLe Château de l\'Étoile","color":"yellow","bold":false}]', 8))
st = nodes[0]
labels.append(disp(['mg.mpdeco'], -5.5, st['y'] + 4, W(st['z']) - 6.5,
                   '[{"text":"LÉGENDE","color":"gold","bold":true},{"text":"\\n■ bleue : +3 pièces","color":"aqua","bold":false},'
                   '{"text":"\\n■ rouge : -3 pièces","color":"red","bold":false},{"text":"\\n■ verte ? : surprise","color":"green","bold":false},'
                   '{"text":"\\n■ noire ☠ : piège","color":"gray","bold":false},{"text":"\\n■ blanche ⇆ : embranchement","color":"white","bold":false},'
                   '{"text":"\\n★ étoile : 20 pièces","color":"yellow","bold":false}]', 1.6, 'alignment:"left",'))
FORK_TXT = {FORK1: ('☀ Route de la plage', 'longue, tranquille', '♨ Raccourci du volcan', 'courte, dangereuse'),
            FORK2: ('❄ Tour du lac gelé', 'longue, tranquille', '❄ Grotte de glace', 'courte, piégeuse')}
for f, (n1, d1, n2, d2) in FORK_TXT.items():
    nd = nodes[f]
    labels.append(f'fill {nd["x"] + 2} {nd["y"] + 1} {W(nd["z"]) + 2} {nd["x"] + 2} {nd["y"] + 2} {W(nd["z"]) + 2} minecraft:oak_fence')
    labels.append(disp(['mg.mpdeco'], nd['x'] + 2.5, nd['y'] + 4.2, W(nd['z']) + 2.5,
                       f'[{{"text":"EMBRANCHEMENT","color":"white","bold":true}},{{"text":"\\n1 : {n1}","color":"yellow","bold":false}},'
                       f'{{"text":" ({d1})","color":"gray","bold":false}},{{"text":"\\n2 : {n2}","color":"red","bold":false}},{{"text":" ({d2})","color":"gray","bold":false}}]', 1.4))

# ------------------------------------------------------------------ écriture des fonctions
def write(name, lines):
    with open(os.path.join(OUT, name + '.mcfunction'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')

clear = ['# Mini Party, carte : 1/ nettoyage de la zone (y 44 à 140)']
for x in range(-HALF, HALF + 1, 16):
    for z in range(-HALF, HALF + 1, 16):
        clear.append(f'fill {x} {YB} {W(z)} {min(x + 15, HALF)} 140 {W(min(z + 15, HALF))} minecraft:air')

parts = [clear]
CH = 6000
for i in range(0, len(terrain), CH):
    parts.append([f'# Mini Party, carte : terrain ({i // CH + 1})'] + terrain[i:i + CH])
parts.append(['# Mini Party, carte : grotte de glace, cases, château'] + tunnel_cmds + case_cmds + CASTLE)
for i in range(0, len(deco), CH):
    parts.append([f'# Mini Party, carte : décor ({i // CH + 1})'] + deco[i:i + CH])
parts.append(['# Mini Party, carte : panneaux'] + labels + ['data modify storage mg:party built set value 2b',
             'tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Plateau de la Mini Party construit.","color":"green"}]'])

write('build', ['# (OP) Construit la carte de la Mini Party (île à z 15000, en plusieurs ticks pour éviter un pic de lag)',
                'tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Construction du plateau de la Mini Party (quelques secondes)...","color":"gray"}]',
                'function mg:party/build_1'])
for k, p in enumerate(parts, 1):
    if k < len(parts):
        p = p + [f'schedule function mg:party/build_{k + 1} 2t']
    write(f'build_{k}', p)

write('place_c', ['# Pion : téléporte @s au centre de sa case (mg.mpi = 0..%d), le décalage est fait par party/place' % (N - 1)] +
      [f'execute if score @s mg.mpi matches {i} run return run tp @s {nd["x"] + 0.5} {nd["y"] + 1} {W(nd["z"]) + 0.5}' for i, nd in enumerate(nodes)])
write('case_type', ['# Type de la case de @s -> $ct (0 départ, 1 bleue, 2 rouge, 3 événement, 4 piège, 5 embranchement)'] +
      [f'execute if score @s mg.mpi matches {i} run scoreboard players set $ct mg.st {nd["type"]}' for i, nd in enumerate(nodes)])
write('is_fork', ['# $fk = 1 si la case de @s est un embranchement', 'scoreboard players set $fk mg.st 0'] +
      [f'execute if score @s mg.mpi matches {f} run scoreboard players set $fk mg.st 1' for f in (FORK1, FORK2)])
write('next', ['# Case suivante de @s (hors embranchement)'] +
      [f'execute if score @s mg.mpi matches {i} run return run scoreboard players set @s mg.mpi {nxt[i]}' for i in range(N)])
write('next_fork', ['# Case suivante depuis un embranchement selon $mpch (1 = route 1, 2 = route 2)'] +
      sum([[f'execute if score @s mg.mpi matches {f} if score $mpch mg.st matches 1 run return run scoreboard players set @s mg.mpi {nxt[f]}',
            f'execute if score @s mg.mpi matches {f} if score $mpch mg.st matches 2 run return run scoreboard players set @s mg.mpi {alt[f]}'] for f in (FORK1, FORK2)], []))
write('prev', ['# Case précédente de @s'] +
      [f'execute if score @s mg.mpi matches {i} run return run scoreboard players set @s mg.mpi {prv[i]}' for i in range(N)])
star_txt = '[{"text":"★","color":"yellow","bold":true},{"text":"\\n20 pièces","color":"gold","bold":false}]'
write('star_place', ['# Panneau de l\'étoile sur la case $mps', 'kill @e[type=minecraft:text_display,tag=mg.mpstar]'] +
      [f'execute if score $mps mg.st matches {i} run ' + disp(['mg.mpstar'], nd['x'] + 0.5, nd['y'] + 5, W(nd['z']) + 0.5, star_txt, 3)
       for i, nd in enumerate(nodes) if nd['type'] in (S_BLUE, S_RED, S_EVENT)])
elig = [i for i, nd in enumerate(nodes) if nd['type'] in (S_BLUE, S_RED, S_EVENT)]
write('star_pick', ['# Tire une case possible pour l\'étoile -> $mpsn', f'execute store result score $tmp mg.st run random value 1..{len(elig)}'] +
      [f'execute if score $tmp mg.st matches {k} run return run scoreboard players set $mpsn mg.st {i}' for k, i in enumerate(elig, 1)])
fi = ['# Propose le choix de route à @s (embranchement de sa case)']
for f, (n1, d1, n2, d2) in FORK_TXT.items():
    fi.append(f'execute if score @s mg.mpi matches {f} run tellraw @s [{{"text":"⇆ EMBRANCHEMENT : ","color":"white","bold":true}},'
              f'{{"text":"[1 : {n1}]","color":"yellow","click_event":{{"action":"run_command","command":"trigger mg.dice set 11"}},"hover_event":{{"action":"show_text","value":"{d1}"}}}},'
              f'{{"text":"  "}},{{"text":"[2 : {n2}]","color":"red","click_event":{{"action":"run_command","command":"trigger mg.dice set 12"}},"hover_event":{{"action":"show_text","value":"{d2}"}}}},'
              f'{{"text":"  (choix au hasard dans 15 s)","color":"gray","bold":false}}]')
    fi.append(f'execute if score @s mg.mpi matches {f} run tellraw @a[tag=mg.mpp,tag=!mg.mpcur] [{{"selector":"@s","color":"yellow"}},'
              f'{{"text":" hésite à l\'embranchement : {n1} ou {n2} ?","color":"gray"}}]')
write('fork_info', fi)
write('dice_show', ['# Affiche $dv sur le grand dé'] +
      [f'execute if score $dv mg.st matches {v} run data modify entity @e[type=minecraft:text_display,tag=mg.mpdice,limit=1] text set value [{{"text":"{v}","color":"white","bold":true}}]' for v in range(1, 11)])

old = os.path.join(OUT, 'build.mcfunction')
print('cases', N, 'fork1', FORK1, 'fork2', FORK2, 'join', JOIN1, JOIN2,
      'segments', {g: sum(1 for n in nodes if n['seg'] == g) for g in SEG})
print('terrain', len(terrain), 'deco', len(deco), 'tunnel', len(tunnel_cmds), 'parts', len(parts))
print('types', {t: sum(1 for n in nodes if n['type'] == t) for t in range(6)})

# ------------------------------------------------------------------ aperçu PNG (optionnel)
if len(sys.argv) > 2:
    import zlib, struct

    class Img:
        def __init__(self, w, h):
            self.w, self.h, self.px = w, h, bytearray(w * h * 3)

        def rect(self, x1, y1, x2, y2, rgb):
            for y in range(max(0, y1), min(self.h, y2 + 1)):
                for x in range(max(0, x1), min(self.w, x2 + 1)):
                    k = (y * self.w + x) * 3
                    self.px[k:k + 3] = bytes(rgb)

        def save(self, path):
            raw = b''.join(bytes([0]) + bytes(self.px[y * self.w * 3:(y + 1) * self.w * 3]) for y in range(self.h))
            def chunk(t, d):
                return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
            sig = bytes([137, 80, 78, 71, 13, 10, 26, 10])
            ihdr = struct.pack('>IIBBBBB', self.w, self.h, 8, 2, 0, 0, 0)
            with open(path, 'wb') as f:
                f.write(sig + chunk(b'IHDR', ihdr) + chunk(b'IDAT', zlib.compress(raw, 6)) + chunk(b'IEND', b''))

    COL = {'grass_block': (95, 160, 60), 'podzol': (110, 80, 40), 'moss_block': (80, 130, 50), 'stone_bricks': (140, 140, 140),
           'cobblestone': (120, 120, 120), 'sand': (225, 210, 150), 'red_sand': (200, 110, 50), 'blackstone': (40, 35, 40),
           'basalt': (80, 80, 85), 'tuff': (100, 100, 90), 'smooth_basalt': (60, 60, 65), 'magma_block': (200, 70, 20),
           'lava': (255, 120, 0), 'coarse_dirt': (110, 80, 55), 'gravel': (130, 125, 120), 'snow_block': (245, 250, 255),
           'stone': (125, 125, 125), 'andesite': (135, 135, 135), 'packed_ice': (150, 190, 240), 'mossy_cobblestone': (100, 120, 90),
           'dirt_path': (150, 120, 70), 'smooth_sandstone': (215, 200, 140), 'cut_sandstone': (205, 185, 120),
           'polished_blackstone_bricks': (55, 50, 60), 'spruce_planks': (110, 80, 50)}
    sc = 4
    img = Img((2 * HALF + 1) * sc, (2 * HALF + 1) * sc)
    for (x, z), c in col.items():
        if c['water']:
            depth = SEA - c['h']
            rgb = (40, max(0, 110 - depth * 6), max(0, 200 - depth * 8))
        else:
            base = COL.get(c['top'], (255, 0, 255))
            f = 1 + (c['h'] - 64) * 0.012
            rgb = tuple(max(0, min(255, int(v * f))) for v in base)
        X, Z = (x + HALF) * sc, (z + HALF) * sc
        img.rect(X, Z, X + sc - 1, Z + sc - 1, rgb)
    for (x, z) in occ:
        if (x, z) in col and col[(x, z)]['land'] and (x, z) not in CASE_CELLS:
            X, Z = (x + HALF) * sc, (z + HALF) * sc
            img.rect(X + 1, Z + 1, X + 2, Z + 2, (20, 60, 20))
    CC = {0: (255, 215, 0), 1: (30, 60, 220), 2: (220, 30, 30), 3: (40, 220, 40), 4: (0, 0, 0), 5: (255, 255, 255)}
    for nd in nodes:
        X, Z = (nd['x'] + HALF) * sc, (nd['z'] + HALF) * sc
        img.rect(X - sc - 1, Z - sc - 1, X + 2 * sc, Z + 2 * sc, (255, 255, 255))
        img.rect(X - sc, Z - sc, X + 2 * sc - 1, Z + 2 * sc - 1, CC[nd['type']])
    img.save(sys.argv[2])
    print('apercu', sys.argv[2])
