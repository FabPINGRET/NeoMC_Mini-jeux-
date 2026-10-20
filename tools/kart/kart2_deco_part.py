# Décor : outils de décor et modèles (arbres, palmiers, cactus, champignons, tuyaux, maisons Toad...) : exécuté par gen_kart2.py (exec) dans l'ordre des parts.
# Utilise : HX, HZ, W, WALLD, col, math, random
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
