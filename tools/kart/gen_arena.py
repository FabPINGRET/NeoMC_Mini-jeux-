"""Génère l'arène du mode bataille du kart, la Forteresse Bob-omb : python gen_arena.py ../../data/mg [apercu.png]

Cour carrée de 140 x 140 entourée de remparts (tours d'angle, créneaux, villageois spectateurs sur le chemin de ronde).
Au centre, un donjon surélevé (+4) entouré de douves, accessible par 4 rampes-ponts ; le long de chaque rempart, une
terrasse (+3) avec rampes aux deux bouts ; piliers, canons, massifs fleuris, plaques de boost, 2 Chomps, 40 boîtes.
Sortie : data/mg/function/kart/t3/*.mcfunction
"""
import math, os, random, sys, zlib, struct

OUT = os.path.join(sys.argv[1], 'function', 'kart', 't3')
os.makedirs(OUT, exist_ok=True)
PF = 'mg:kart/t3/'
ZC = 22000
HX = HZ = 100
YB, ROAD = 48, 64
WALL_IN, WALL_OUT = 70, 74
random.seed(63)

def W(z): return ZC + z
def yaw_of(dx, dz): return round(math.degrees(math.atan2(-dx, dz)), 1)

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

def sides(x, z):
    """(le long du rempart, profondeur depuis le rempart) pour chacun des 4 côtés."""
    return ((x, 69 + z), (x, 69 - z), (z, 69 + x), (z, 69 - x))

BEDS = [(sx * 32, sz * 32) for sx in (-1, 1) for sz in (-1, 1)]
PILLARS = [(sx * 46, sz * 16) for sx in (-1, 1) for sz in (-1, 1)] + [(sx * 16, sz * 46) for sx in (-1, 1) for sz in (-1, 1)]
CANNONS = [(sx * 55, sz * 55) for sx in (-1, 1) for sz in (-1, 1)]

col = {}
for x in range(-HX, HX + 1):
    for z in range(-HZ, HZ + 1):
        e = ((abs(x) / (HX - 2)) ** 6 + (abs(z) / (HZ - 2)) ** 6) ** (1 / 6) + (vn(x, z, 14, 3) - 0.5) * 0.06
        if e > 1: continue
        R, mn = max(abs(x), abs(z)), min(abs(x), abs(z))
        c = {'h': ROAD, 'top': 'stone_bricks', 'sub': 'stone', 'liq': None, 'zone': 'cour', 'rail': None}
        if R > WALL_OUT:
            c['zone'] = 'dehors'
            c['h'] = ROAD + round(max(0, R - 78) * 0.45 + vn(x, z, 12, 1) * 3)
            c['top'] = 'grass_block'; c['sub'] = 'dirt'
            mr = math.hypot(x, z + 92)
            if mr < 24: c['h'] = max(c['h'], round(ROAD + 26 * (1 - mr / 24) ** 1.3)); c['top'] = 'grass_block' if c['h'] < ROAD + 18 else 'stone'
            if e > 0.97: c['top'] = 'stone'; c['h'] = min(c['h'], ROAD - 1 - int((e - 0.97) * 60))
        elif R >= WALL_IN:
            c['zone'] = 'mur'
        elif R <= 10:
            c['zone'] = 'donjon'; c['h'] = ROAD + 4
            c['top'] = 'chiseled_stone_bricks' if R == 10 else ('bricks' if (x + z) % 2 else 'polished_granite')
            if R <= 2: c['zone'] = 'statue'
        elif R <= 18 and mn <= 3:
            c['zone'] = 'rampe'; c['h'] = ROAD + max(0, min(4, math.ceil((18 - R) / 2)))
            c['top'] = 'polished_granite' if mn <= 2 else 'chiseled_stone_bricks'
        elif R <= 18 and mn == 4:
            c['zone'] = 'garde'; c['h'] = ROAD + max(0, min(4, math.ceil((18 - R) / 2))); c['top'] = 'stone_bricks'
            c['rail'] = 'stone_brick_wall'
        elif R <= 15:
            c['zone'] = 'douve'; c['h'] = ROAD - 4; c['top'] = 'gravel'; c['liq'] = 'water'; c['lvl'] = ROAD - 1
        elif R == 16:
            c['zone'] = 'barriere'; c['rail'] = 'oak_fence'
        else:
            # cour : allées en croix et en anneau, terrasses le long des remparts
            if abs(x) <= 2 or abs(z) <= 2 or abs(abs(x) - abs(z)) <= 1: c['top'] = 'polished_andesite'
            if 38 <= R <= 40: c['top'] = 'polished_andesite'
            if (abs(x) <= 2 or abs(z) <= 2) and 38 <= R <= 40: c['top'] = 'chiseled_stone_bricks'
            if c['top'] == 'stone_bricks':
                v = hsh(x, z, 9)
                c['top'] = 'mossy_stone_bricks' if v < 0.08 else ('cracked_stone_bricks' if v < 0.14 else 'stone_bricks')
            for along, depth in sides(x, z):
                if 0 <= depth <= 9:
                    if abs(along) <= 22: c['h'] = ROAD + 3; c['top'] = 'smooth_stone'; c['zone'] = 'terrasse'
                    elif abs(along) <= 28:
                        d = abs(along) - 22
                        c['h'] = max(c['h'], ROAD + 3 - (d + 1) // 2); c['top'] = 'smooth_stone'; c['zone'] = 'terrasse'
            for bx, bz in BEDS:
                if math.hypot(x - bx, z - bz) <= 6.5: c['top'] = 'grass_block'; c['sub'] = 'dirt'; c['zone'] = 'massif'
        col[(x, z)] = c

# plaques de boost sur les allées en croix (vers le centre)
for k in range(44, 49):
    for w in range(-1, 2):
        for (x, z) in ((k, w), (-k, w), (w, k), (w, -k)):
            col[(x, z)]['top'] = 'orange_glazed_terracotta'

# ------------------------------------------------------------------ terrain
def sig(c): return (c['h'], c['top'], c['sub'], c['liq'], c.get('lvl', 0))
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
        h, top, sub, liq, lvl = s
        x1, x2, z1, z2 = x, x + hh - 1, W(z), W(z + w - 1)
        if h - 4 >= YB: terrain.append(f'fill {x1} {YB} {z1} {x2} {h - 4} {z2} minecraft:stone')
        terrain.append(f'fill {x1} {max(YB, h - 3)} {z1} {x2} {h - 1} {z2} minecraft:{sub}')
        terrain.append(f'fill {x1} {h} {z1} {x2} {h} {z2} minecraft:{top}')
        if liq: terrain.append(f'fill {x1} {h + 1} {z1} {x2} {lvl} {z2} minecraft:{liq}')

B = []
def sb(x, y, z, blk): B.append(f'setblock {x} {y} {W(z)} minecraft:{blk}')
def fl(x1, y1, z1, x2, y2, z2, blk, mode=''):
    B.append(f'fill {min(x1, x2)} {min(y1, y2)} {W(min(z1, z2))} {max(x1, x2)} {max(y1, y2)} {W(max(z1, z2))} minecraft:{blk}{(" " + mode) if mode else ""}')
def disc(x, y, z, r, blk, mode=''):
    for a in range(-r, r + 1):
        w = int(math.sqrt(max(0, r * r + r - a * a)))
        fl(x + a, y, z - w, x + a, y, z + w, blk, mode)

# garde-corps des rampes et barrière des douves (infranchissables : mur ou clôture + barrières)
for (x, z), c in col.items():
    if c['rail']:
        sb(x, c['h'] + 1, z, c['rail'])
        fl(x, c['h'] + 2, z, x, c['h'] + 3, z, 'barrier')
        if c['rail'] == 'stone_brick_wall' and (x + z) % 4 == 0: sb(x, c['h'] + 2, z, 'lantern')

# remparts, créneaux, chemin de ronde, tentures
for s in range(4):
    def P(a, d):  # a = le long, d = distance au centre
        return [(a, -d), (a, d), (-d, a), (d, a)][s]
    (x1, z1), (x2, z2) = P(-WALL_OUT, WALL_IN), P(WALL_OUT, WALL_OUT)
    fl(x1, ROAD + 1, z1, x2, ROAD + 10, z2, 'stone_bricks')
    for a in range(-WALL_OUT, WALL_OUT + 1):
        if a % 2 == 0:
            xo, zo = P(a, WALL_OUT); sb(xo, ROAD + 11, zo, 'stone_bricks')
            xi, zi = P(a, WALL_IN); sb(xi, ROAD + 11, zi, 'stone_brick_wall')
        if a % 12 == 6 and abs(a) < 64:
            for k, colr in enumerate(('red', 'yellow', 'red')):
                xb, zb = P(a, WALL_IN - 1)
                sb(xb, ROAD + 7 - k, zb, f'{colr}_wool')
            xb, zb = P(a, WALL_IN - 1); sb(xb, ROAD + 8, zb, 'stone_brick_slab[type=top]')
        if a % 8 == 0:
            xl, zl = P(a, WALL_IN + 2); sb(xl, ROAD + 11, zl, 'lantern')
    for k in range(260):
        a, d, y = random.randint(-WALL_OUT, WALL_OUT), random.choice((WALL_IN, WALL_OUT)), random.randint(ROAD + 1, ROAD + 10)
        xr, zr = P(a, d); sb(xr, y, zr, random.choice(('mossy_stone_bricks', 'cracked_stone_bricks')))
# porte principale (sud), herse fermée
fl(-5, ROAD + 1, WALL_OUT, 5, ROAD + 13, WALL_OUT + 1, 'stone_bricks')
fl(-3, ROAD + 1, WALL_OUT + 1, 3, ROAD + 7, WALL_OUT + 1, 'iron_bars')
fl(-5, ROAD + 14, WALL_OUT, 5, ROAD + 14, WALL_OUT + 1, 'stone_brick_wall')
# tours d'angle
for sx in (-1, 1):
    for sz in (-1, 1):
        cx, cz = sx * 72, sz * 72
        for a in range(-7, 8):
            for b in range(-7, 8):
                if a * a + b * b <= 50: fl(cx + a, ROAD + 1, cz + b, cx + a, ROAD + 20, cz + b, 'stone_bricks')
        for a in range(-8, 9):
            for b in range(-8, 9):
                if 50 < a * a + b * b <= 68 and (a + b) % 2 == 0: sb(cx + a, ROAD + 21, cz + b, 'stone_brick_wall')
        for k, r in enumerate((7, 6, 5, 4, 3, 2, 1)):
            for a in range(-r, r + 1):
                for b in range(-r, r + 1):
                    if a * a + b * b <= r * r: sb(cx + a, ROAD + 22 + k, cz + b, 'red_concrete' if k % 2 == 0 else 'red_terracotta')
        fl(cx, ROAD + 29, cz, cx, ROAD + 34, cz, 'oak_fence')
        fl(cx + 1, ROAD + 32, cz, cx + 3, ROAD + 34, cz, 'yellow_wool' if sx * sz > 0 else 'red_wool')
        for k in range(4, 19, 5):
            sb(cx - sx * 7, ROAD + k, cz - sz * 2, 'iron_bars'); sb(cx - sx * 2, ROAD + k, cz - sz * 7, 'iron_bars')

# donjon : statue de Bob-omb sur un socle, lampadaires d'angle
y0 = ROAD + 4
fl(-2, y0 + 1, -2, 2, y0 + 2, 2, 'stone_bricks')
fl(-1, y0 + 3, -1, 1, y0 + 5, 1, 'black_wool')
for (a, b) in ((-2, 0), (2, 0), (0, -2), (0, 2)): fl(a, y0 + 4, b, a, y0 + 4, b, 'black_wool')
sb(0, y0 + 6, 0, 'black_wool'); sb(0, y0 + 7, 0, 'gray_wool'); sb(0, y0 + 8, 0, 'orange_wool')
sb(-1, y0 + 4, -2, 'white_wool'); sb(1, y0 + 4, -2, 'white_wool')                     # yeux
fl(-1, y0 + 4, 2, 1, y0 + 4, 2, 'gold_block'); sb(0, y0 + 5, 3, 'gold_block')         # clé
fl(-1, y0 + 2, -3, -1, y0 + 2, -3, 'yellow_wool'); sb(1, y0 + 2, -3, 'yellow_wool')   # pieds
for (a, b) in ((-9, -9), (9, -9), (-9, 9), (9, 9)):
    fl(a, y0 + 1, b, a, y0 + 3, b, 'dark_oak_fence'); sb(a, y0 + 4, b, 'lantern')

# piliers, canons, massifs fleuris, caisses
for (px, pz) in PILLARS:
    fl(px, ROAD + 1, pz, px + 1, ROAD + 5, pz + 1, 'stone_bricks')
    fl(px, ROAD + 6, pz, px + 1, ROAD + 6, pz + 1, 'chiseled_stone_bricks')
    sb(px, ROAD + 7, pz, 'lantern')
for (cx, cz) in CANNONS:
    fl(cx - 2, ROAD + 1, cz - 2, cx + 2, ROAD + 2, cz + 2, 'dark_oak_planks')
    dx, dz = -cx / abs(cx), -cz / abs(cz)
    for k in range(0, 6):
        x, z = round(cx + dx * k * 0.8), round(cz + dz * k * 0.8)
        fl(x - 1, ROAD + 3, z - 1, x + 1, ROAD + 4 + (1 if k > 2 else 0), z + 1, 'black_concrete')
    x, z = round(cx + dx * 4.8), round(cz + dz * 4.8)
    sb(x, ROAD + 4, z, 'coal_block')
    for a in (-2, 2): sb(cx + a, ROAD + 3, cz + a, 'black_concrete')
for (bx, bz) in BEDS:
    for a in range(-6, 7):
        for b in range(-6, 7):
            r = math.hypot(a, b)
            if r <= 6.5 and r > 2 and random.random() < 0.35:
                sb(bx + a, ROAD + 1, bz + b, random.choice(['poppy', 'dandelion', 'cornflower', 'allium', 'oxeye_daisy', 'short_grass']))
    fl(bx, ROAD + 1, bz, bx + 1, ROAD + 6, bz + 1, 'oak_log')
    disc(bx, ROAD + 7, bz, 4, 'oak_leaves[persistent=true]'); disc(bx, ROAD + 8, bz, 3, 'oak_leaves[persistent=true]')
    disc(bx, ROAD + 9, bz, 2, 'oak_leaves[persistent=true]')
# arches au-dessus des allées en croix (R = 24), haies en L dans les angles
for s in range(4):
    def Q(a, d): return [(a, -d), (a, d), (-d, a), (d, a)][s]
    for side in (-1, 1):
        (x1, z1), (x2, z2) = Q(side * 5, 24), Q(side * 6, 25)
        fl(x1, ROAD + 1, z1, x2, ROAD + 6, z2, 'stone_bricks')
    (x1, z1), (x2, z2) = Q(-6, 24), Q(6, 25)
    fl(x1, ROAD + 7, z1, x2, ROAD + 8, z2, 'stone_bricks')
    for a in range(-6, 7, 2):
        xc, zc = Q(a, 24); sb(xc, ROAD + 9, zc, 'stone_brick_wall')
    xb, zb = Q(0, 24); sb(xb, ROAD + 9, zb, 'gold_block')
    for a in (-3, 0, 3):
        xh, zh = Q(a, 24); sb(xh, ROAD + 6, zh, 'lantern[hanging=true]')
for sx in (-1, 1):
    for sz in (-1, 1):
        fl(sx * 60, ROAD + 1, sz * 44, sx * 66, ROAD + 2, sz * 44, 'oak_leaves[persistent=true]')
        fl(sx * 44, ROAD + 1, sz * 60, sx * 44, ROAD + 2, sz * 66, 'oak_leaves[persistent=true]')
        fl(sx * 50, ROAD + 1, sz * 50, sx * 50, ROAD + 2, sz * 47, 'oak_leaves[persistent=true]')
for (cx, cz) in ((-24, 52), (24, -52), (52, 24), (-52, -24), (-8, 56), (8, -56)):
    fl(cx, ROAD + 1, cz, cx + 1, ROAD + 2, cz + 1, 'barrel')
    sb(cx + 2, ROAD + 1, cz, 'hay_block'); sb(cx + 2, ROAD + 2, cz, 'hay_block')

# dehors : arbres, fleurs, statues de Bob-omb, nuages
def tree(x, z):
    y = col[(x, z)]['h'] + 1; t = random.randint(4, 6)
    fl(x, y, z, x, y + t - 1, z, 'oak_log')
    fl(x - 2, y + t - 2, z - 2, x + 2, y + t - 1, z + 2, 'oak_leaves[persistent=true]', 'replace air')
    fl(x - 1, y + t, z - 1, x + 1, y + t + 1, z + 1, 'oak_leaves[persistent=true]', 'replace air')
occ = set()
for _ in range(500):
    x, z = random.randint(-HX + 4, HX - 4), random.randint(-HZ + 4, HZ - 4)
    c = col.get((x, z))
    if c and c['zone'] == 'dehors' and c['top'] == 'grass_block' and max(abs(x), abs(z)) > 78 and all((x + a, z + b) not in occ for a in range(-3, 4) for b in range(-3, 4)):
        tree(x, z)
        for a in range(-3, 4):
            for b in range(-3, 4): occ.add((x + a, z + b))
for (x, z), c in col.items():
    if c['zone'] == 'dehors' and c['top'] == 'grass_block' and (x, z) not in occ and random.random() < 0.08:
        sb(x, c['h'] + 1, z, random.choice(['poppy', 'dandelion', 'short_grass', 'short_grass', 'cornflower']))
for (x, z) in ((-88, 20), (88, -20), (30, 88)):
    if (x, z) in col:
        y = col[(x, z)]['h'] + 1
        fl(x - 2, y + 1, z - 2, x + 2, y + 5, z + 2, 'black_concrete'); fl(x - 1, y + 6, z - 1, x + 1, y + 6, z + 1, 'black_concrete')
        sb(x, y + 7, z, 'gray_wool'); sb(x, y + 8, z, 'orange_wool'); fl(x - 1, y, z - 1, x + 1, y, z + 1, 'yellow_concrete')
        sb(x - 1, y + 4, z - 3, 'white_concrete'); sb(x + 1, y + 4, z - 3, 'white_concrete')
for _ in range(10):
    x, y, z = random.randint(-HX + 10, HX - 10), random.randint(96, 103), random.randint(-HZ + 10, HZ - 10)
    for a in range(-5, 6):
        for b in range(-2, 3):
            if a * a / 25 + b * b / 4 <= 1: sb(x + a, y, z + b, 'white_wool')
    fl(x - 2, y + 1, z - 1, x + 2, y + 1, z + 1, 'white_wool')

# ------------------------------------------------------------------ dangers, spectateurs, boîtes
T0 = 'left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]'
FLIP = 'left_rotation:[0f,1f,0f,0f],right_rotation:[0f,0f,0f,1f]'
def tf(s, flip=True): return 'transformation:{translation:[0f,0f,0f],%s,scale:[%sf,%sf,%sf]}' % (FLIP if flip else T0, s, s, s)
def Pt(x, y, z): return f'{round(x, 2)} {round(y, 2)} {round(W(0) + z, 2)}'
def lerp(a, b, t): return tuple(a[k] + (b[k] - a[k]) * t for k in range(3))
HZT = '"mg.khz","mg.fx"'
spawn = ['# Forteresse Bob-omb : Chomps et spectateurs (recréés à chaque bataille)', 'kill @e[tag=mg.khz]']
tick = ['# Forteresse Bob-omb : Chomps (chaque tick de bataille)']
MOB = 'NoAI:1b,Silent:1b,Invulnerable:1b,PersistenceRequired:1b'
for k in range(26):
    a = random.randint(-62, 62); s = random.randint(0, 3)
    x, z = [(a, -72), (a, 72), (-72, a), (72, a)][s]
    prof = random.choice(['farmer', 'librarian', 'cleric', 'fisherman', 'shepherd', 'armorer', 'cartographer', 'butcher'])
    spawn.append(f'summon minecraft:villager {Pt(x + 0.5, ROAD + 11, z + 0.5)} {{Tags:[{HZT},"mg.kmob"],{MOB},Rotation:[{yaw_of(-x, -z)}f,0f],'
                 f'VillagerData:{{profession:"minecraft:{prof}",type:"minecraft:plains",level:1}}}}')
for sx in (-1, 1):
    for sz in (-1, 1):
        spawn.append(f'summon minecraft:parrot {Pt(sx * 72 + 0.5, ROAD + 35, sz * 72 + 0.5)} {{Tags:[{HZT},"mg.kmob"],{MOB}}}')
for _ in range(10):
    for _t in range(200):
        x, z = random.randint(-HX + 6, HX - 6), random.randint(-HZ + 6, HZ - 6)
        c = col.get((x, z))
        if c and c['zone'] == 'dehors' and (x, z) not in occ and c['top'] == 'grass_block' and max(abs(x), abs(z)) > 78:
            spawn.append(f'summon minecraft:{random.choice(["sheep", "cow", "chicken", "pig"])} {Pt(x + 0.5, c["h"] + 1, z + 0.5)} '
                         f'{{Tags:[{HZT},"mg.kmob"],{MOB},Rotation:[{random.randint(0, 359)}f,0f]}}'); break
consts = {90}
for n, (px, pz) in enumerate(((0, -58), (0, 58))):
    t = f'mg.kh{n + 1}'
    dz = 1 if pz < 0 else -1
    post = (px + 0.5, ROAD + 1, pz + 0.5)
    rest = (px + 0.5, ROAD + 2.2, pz + 0.5 + dz * 2.5)
    far = (px + 0.5, ROAD + 2.2, pz + 0.5 + dz * 13)
    B.append(f'fill {px} {ROAD + 1} {W(pz)} {px} {ROAD + 2} {W(pz)} minecraft:oak_log')
    spawn.append(f'summon minecraft:item_display {Pt(*rest)} {{Tags:["mg.kchomp","{t}",{HZT}],teleport_duration:3,item:{{id:"minecraft:coal_block"}},'
                 f'Rotation:[{yaw_of(0, dz)}f,0f],{tf(2.4)}}}')
    links = []
    for k in range(1, 6):
        tl = f'{t}l{k}'; links.append(tl)
        spawn.append(f'summon minecraft:item_display {Pt(*lerp((post[0], post[1] + 1.2, post[2]), rest, k / 6))} {{Tags:["mg.kchain","{tl}",{HZT}],teleport_duration:3,item:{{id:"minecraft:iron_block"}},{tf(0.3, False)}}}')
    tick += ['scoreboard players operation $hp mg.st = $ktime mg.st', f'scoreboard players add $hp mg.st {n * 45}', 'scoreboard players operation $hp mg.st %= #h90 mg.st']
    def at(p, cmd): tick.append(f'execute if score $hp mg.st matches {p} run {cmd}')
    for p_, h_ in ((15, 0.6), (18, 0), (30, 0.6), (33, 0)):
        at(p_, f'tp @e[tag={t}] {Pt(rest[0], rest[1] + h_, rest[2])}')
    at(52, f'execute positioned {Pt(*rest)} run playsound minecraft:entity.wolf.growl master @a[tag=mg.play,distance=..30] ~ ~ ~ 1 0.5')
    at(60, f'data merge entity @e[tag={t},limit=1] {{teleport_duration:4}}')
    at(60, f'tp @e[tag={t}] {Pt(*far)}')
    for k, tl in enumerate(links, 1):
        at(60, f'data merge entity @e[tag={tl},limit=1] {{teleport_duration:4}}')
        at(60, f'tp @e[tag={tl}] {Pt(*lerp((post[0], post[1] + 1.2, post[2]), far, k / 6))}')
        at(72, f'data merge entity @e[tag={tl},limit=1] {{teleport_duration:15}}')
        at(72, f'tp @e[tag={tl}] {Pt(*lerp((post[0], post[1] + 1.2, post[2]), rest, k / 6))}')
    for k in range(6):
        q = lerp((rest[0], ROAD + 1, rest[2]), (far[0], ROAD + 1, far[2]), k / 5)
        tick.append(f'execute if score $hp mg.st matches 61..70 positioned {Pt(*q)} as @e[type=minecraft:block_display,tag=mg.kart,distance=..1.9] run function {PF}hz_big')
    at(72, f'data merge entity @e[tag={t},limit=1] {{teleport_duration:15}}')
    at(72, f'tp @e[tag={t}] {Pt(*rest)}')
tick.append('function mg:kart/bat_tick')
spawn.append(f'summon minecraft:text_display {Pt(0.5, ROAD + 20, 0.5)} {{Tags:[{HZT}],billboard:"vertical",text:[{{"text":"FORTERESSE ","color":"gold","bold":true}},{{"text":"BOB-OMB","color":"red","bold":true}}],'
             f'background:1342177280,{tf(5, False)}}}')

BOXES = [(6 * math.cos(math.radians(22.5 + 45 * k)), ROAD + 4, 6 * math.sin(math.radians(22.5 + 45 * k))) for k in range(8)]
for s in range(4):
    for a in (-14, -5, 5, 14):
        x, z = [(a, -64), (a, 64), (-64, a), (64, a)][s]
        BOXES.append((x + 0.5, ROAD + 3, z + 0.5))
for (cx, cz) in ((30, 0), (-30, 0), (0, 30), (0, -30)):
    for (a, b) in ((-2, -2), (2, -2), (-2, 2), (2, 2)):
        BOXES.append((cx + a + 0.5, ROAD, cz + b + 0.5))
boxes = ['# Forteresse Bob-omb : 40 boîtes à objets', 'kill @e[type=minecraft:item_display,tag=mg.kbox]', 'kill @e[type=minecraft:text_display,tag=mg.kboxq]']
for (x, y, z) in BOXES:
    boxes.append(f'summon minecraft:item_display {round(x, 1)} {y + 2} {round(W(0) + z, 1)} {{Tags:["mg.kbox","mg.kspin","mg.fx"],item:{{id:"minecraft:yellow_stained_glass"}},'
                 f'transformation:{{translation:[0f,0f,0f],{T0},scale:[1.1f,1.1f,1.1f]}},interpolation_duration:10}}')
    boxes.append(f'summon minecraft:text_display {round(x, 1)} {y + 1.7} {round(W(0) + z, 1)} {{Tags:["mg.kboxq","mg.fx"],billboard:"center",text:[{{"text":"?","color":"gold","bold":true}}],background:0,'
                 f'transformation:{{translation:[0f,0f,0f],{T0},scale:[1.5f,1.5f,1.5f]}}}}')

SPAWNS = []
for k in range(16):
    a = math.radians(11.25 + 22.5 * k)
    x, z = 52 * math.cos(a), 52 * math.sin(a)
    SPAWNS.append((round(x, 1), ROAD + 1, round(z, 1), yaw_of(-x, -z)))

def write(name, lines):
    with open(os.path.join(OUT, name + '.mcfunction'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')

write('grid_tp', ['# Forteresse Bob-omb : place le kart @s à son point de départ (n° $gi, 1..16), tourné vers le donjon'] +
      [f'execute if score $gi mg.st matches {k + 1} run return run tp @s {x} {y} {W(0) + z} {yw} 0' for k, (x, y, z, yw) in enumerate(SPAWNS)])
write('cp_tp', ['# Forteresse Bob-omb : retour en jeu (@s = kart) sur un point de départ au hasard',
                'execute store result score $kr2 mg.st run random value 1..16'] +
      [f'execute if score $kr2 mg.st matches {k + 1} run return run tp @s {x} {y} {W(0) + z} {yw} 0' for k, (x, y, z, yw) in enumerate(SPAWNS)])
write('cp_check', ['# Forteresse Bob-omb : pas de tours en bataille'])
write('bill_step', ['# Forteresse Bob-omb : pas de Bill Balle en bataille (remplacé par le champignon doré)'])
write('gate_on', ['# Forteresse Bob-omb : pas de portillon'])
write('gate_off', ['# Forteresse Bob-omb : pas de portillon'])
write('boxes', boxes)
write('hazards', spawn)
write('track_tick', tick)
write('spec_tp', ['# Pilote éliminé : vue d\'ensemble de l\'arène', f'tp @s 0.5 {ROAD + 36} {W(0) + 60.5} 180 50'])
write('hz_hit', ['scoreboard players operation $ko mg.st = @s mg.ri',
                 'execute as @a[tag=mg.play] if score @s mg.ri = $ko mg.st unless score @s mg.khi matches 1.. run function mg:kart/hit'])
write('hz_big', ['scoreboard players operation $ko mg.st = @s mg.ri',
                 'execute as @a[tag=mg.play] if score @s mg.ri = $ko mg.st unless score @s mg.khi matches 1.. run function mg:kart/hit_big'])
write('fl_add', ['# Forteresse Bob-omb : zone chargée', f'forceload add {-HX} {W(-HZ)} {HX} {W(HZ)}'])
write('fl_remove', ['# Forteresse Bob-omb : zone libérée', f'forceload remove {-HX} {W(-HZ)} {HX} {W(HZ)}', 'function mg:core/forceloads'])
clear = ['# Forteresse Bob-omb : nettoyage']
for x in range(-HX, HX + 1, 16):
    for z in range(-HZ, HZ + 1, 16):
        clear.append(f'fill {x} {YB} {W(z)} {min(x + 15, HX)} {ROAD + 42} {W(min(z + 15, HZ))} minecraft:air')
parts = [clear]
CH = 3000
for i in range(0, len(terrain), CH): parts.append(['# Forteresse Bob-omb : terrain'] + terrain[i:i + CH])
for i in range(0, len(B), CH): parts.append(['# Forteresse Bob-omb : décor'] + B[i:i + CH])
parts.append(['# Forteresse Bob-omb : fin', f'function {PF}fl_remove', 'data modify storage mg:kart built3 set value 1b',
              'tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Arène Forteresse Bob-omb construite.","color":"green"}]'])
write('build', ['# (OP) Construit la Forteresse Bob-omb', f'function {PF}fl_add', 'scoreboard players set $kbw3 mg.st 0', f'schedule function {PF}build_wait 20t'])
write('build_wait', [f'execute if function {PF}loaded_all run return run function {PF}build_1', 'scoreboard players add $kbw3 mg.st 1',
                     'execute if score $kbw3 mg.st matches 300.. run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Forteresse Bob-omb : zone pas chargée, construction annulée.","color":"red"}]',
                     f'schedule function {PF}build_wait 20t'])
lo = ['# Vrai si toute l\'arène est chargée']
for x in list(range(-HX, HX + 1, 32)) + [HX]:
    for z in list(range(-HZ, HZ + 1, 32)) + [HZ]:
        lo += [f'execute store success score $kld mg.st unless block {x} {ROAD} {W(z)} minecraft:bedrock', 'execute if score $kld mg.st matches 0 run return fail']
lo.append('return 1')
write('loaded_all', lo)
for k, p in enumerate(parts, 1):
    if k < len(parts): p = p + [f'schedule function {PF}build_{k + 1} 2t']
    write(f'build_{k}', p)
for f in os.listdir(OUT):
    if f.startswith('build_') and f[6:-11].isdigit() and int(f[6:-11]) > len(parts): os.remove(os.path.join(OUT, f))
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
                if cc: kinds.add(cc['zone'])
        if 'douve' in kinds: color = 'dark_aqua'
        elif kinds & {'donjon', 'statue', 'rampe'}: color = 'red'
        elif 'terrasse' in kinds: color = 'white'
        elif 'mur' in kinds: color = 'dark_gray'
        elif kinds & {'cour', 'massif', 'barriere', 'garde'}: color = 'gray'
        elif 'dehors' in kinds: color = 'dark_green'
        else: color = 'black'
        row.append('{text:"█",color:"%s"}' % color)
    cells.append('l%d:[%s]' % (r, ','.join(row)))
write('mm_base', ['# Minimap de la Forteresse Bob-omb', 'data modify storage mg:kart base set value {' + ','.join(cells) + '}'])
write('mm_show', [f'$scoreboard players display name m{r:02d} mg.kmap $(l{r})' for r in range(MMR)])
write('mm_init', [f'scoreboard players set m{r:02d} mg.kmap {MMR - r}' for r in range(MMR)])
write('const', ['# Constantes de la Forteresse Bob-omb', 'scoreboard players set $kK mg.st 1', 'scoreboard players set $kLaps mg.st 1',
                f'scoreboard players set #kmx0 mg.st {HX}', f'scoreboard players set #kmz0 mg.st {ZC - HZ}', f'scoreboard players set #kmc mg.st {MMC}',
                f'scoreboard players set #kmw mg.st {2 * HX + 1}', f'scoreboard players set #kmr mg.st {MMR}', f'scoreboard players set #kmh mg.st {2 * HZ + 1}',
                'scoreboard players set $px mg.st 0', f'scoreboard players set $py mg.st {ROAD + 36}', f'scoreboard players set $pz mg.st {ZC + 60}'] +
      [f'scoreboard players set #h{T} mg.st {T}' for T in sorted(consts)])
print('terrain', len(terrain), '| décor', len(B), '| étapes', len(parts), '| boîtes', len(BOXES), '| entités', len(spawn))

if len(sys.argv) > 2:
    w = h = 2 * HX + 1; sc = 4
    px = bytearray(w * sc * h * sc * 3)
    COL = {'cour': (150, 150, 150), 'mur': (70, 70, 75), 'donjon': (180, 80, 60), 'statue': (20, 20, 20), 'rampe': (200, 110, 90), 'garde': (100, 100, 100),
           'douve': (40, 110, 200), 'barriere': (120, 80, 40), 'terrasse': (220, 220, 210), 'massif': (90, 160, 60), 'dehors': (95, 160, 60)}
    for (x, z), c in col.items():
        rgb = COL[c['zone']]
        if c['top'] == 'polished_andesite': rgb = (175, 175, 180)
        if c['top'] == 'orange_glazed_terracotta': rgb = (240, 140, 20)
        f = 1 + (c['h'] - ROAD) * 0.04
        rgb = tuple(max(0, min(255, int(v * f))) for v in rgb)
        X, Z = (x + HX) * sc, (z + HZ) * sc
        for yy in range(Z, Z + sc):
            for xx in range(X, X + sc):
                k = (yy * w * sc + xx) * 3; px[k:k + 3] = bytes(rgb)
    for (x, y, z) in BOXES:
        X, Z = int((x + HX) * sc), int((z + HZ) * sc)
        for yy in range(Z - 2, Z + 3):
            for xx in range(X - 2, X + 3):
                k = (yy * w * sc + xx) * 3; px[k:k + 3] = bytes((255, 220, 0))
    raw = b''.join(bytes([0]) + bytes(px[y * w * sc * 3:(y + 1) * w * sc * 3]) for y in range(h * sc))
    def chunk(t, d): return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    with open(sys.argv[2], 'wb') as f:
        f.write(bytes([137, 80, 78, 71, 13, 10, 26, 10]) + chunk(b'IHDR', struct.pack('>IIBBBBB', w * sc, h * sc, 8, 2, 0, 0, 0))
                + chunk(b'IDAT', zlib.compress(raw, 6)) + chunk(b'IEND', b''))
    print('aperçu', sys.argv[2])
