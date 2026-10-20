# Spawn : décor secret, sommet, arbres, îlots, parkour et éclairage des chemins ; exécuté par gen_lobby.py (exec) après le circuit du spawn.
# Utilise : FLOWERS, G, ISET, ISL, JETS, LEAF, MASK, PETALS, TOP, W, box, disc, edge, get, hedge, lamp, math, put, rnd, setif, shell, vn

# ------------------------------------------------------------------ SECRETS : éléments cachés dans le décor (voir la section « secrets » plus bas)
SEC_ROOM = (-29, 55, -32, -21, 59, -26)          # x1 y1 z1 x2 y2 z2 (y1 = sol)
SEC_SHAFT = (-25, -25)
for x in range(SEC_ROOM[0] - 1, SEC_ROOM[3] + 2):
    for z in range(SEC_ROOM[2] - 1, SEC_ROOM[5] + 2):
        for y in range(SEC_ROOM[1] - 1, SEC_ROOM[4] + 2):
            edge_ = x in (SEC_ROOM[0] - 1, SEC_ROOM[3] + 1) or z in (SEC_ROOM[2] - 1, SEC_ROOM[5] + 1) or y in (SEC_ROOM[1] - 1, SEC_ROOM[4] + 1)
            if edge_: put(x, y, z, 'mossy_stone_bricks' if (x + y + z) % 3 else 'cracked_stone_bricks')
            elif y == SEC_ROOM[1]: put(x, y, z, 'polished_deepslate' if (x + z) % 2 else 'deepslate_tiles')
            else: put(x, y, z, 'air')
sx0, sz0 = SEC_SHAFT
for y in range(SEC_ROOM[1] + 1, G):
    put(sx0, y, sz0, 'ladder[facing=north]'); put(sx0, y, sz0 + 1, 'stone')
    for dx in (-1, 1): put(sx0 + dx, y, sz0, 'stone')
    put(sx0, y, sz0 - 1, 'air' if y <= SEC_ROOM[4] else 'stone')
TOP[SEC_SHAFT] = 'spruce_trapdoor[facing=north,half=top,open=false]'
for (x, z) in disc(sx0, sz0, 2.5):
    if (x, z) in MASK: MASK[(x, z)] = 'b'
for (dx, dz) in ((-2, 0), (2, 1), (0, 2), (-1, -2), (2, -1)):
    put(sx0 + dx, 64, sz0 + dz, 'azalea_leaves[persistent=true]' if (dx + dz) % 2 else 'flowering_azalea_leaves[persistent=true]')
rx1, ry1, rz1, rx2, ry2, rz2 = SEC_ROOM
for x in range(rx1, rx2 + 1): put(x, ry1 + 1, rz1, 'bookshelf'); put(x, ry1 + 2, rz1, 'bookshelf')
put(rx1 + 1, ry1 + 1, rz1 + 1, 'chest[facing=south]'); put(rx2 - 1, ry1 + 1, rz1 + 1, 'chest[facing=south]')
put((rx1 + rx2) // 2, ry1 + 1, rz1 + 2, 'enchanting_table')
put(rx1, ry1 + 1, rz2, 'amethyst_block'); put(rx1, ry1 + 2, rz2, 'amethyst_cluster[facing=up]')
put(rx2, ry1 + 1, rz2, 'gold_block'); put(rx2, ry1 + 2, rz2, 'emerald_block'); put(rx2, ry1 + 3, rz2, 'diamond_block')
for x in (rx1 + 2, rx2 - 2): put(x, ry2, (rz1 + rz2) // 2, 'lantern[hanging=true]')
put(rx1, ry1 + 1, (rz1 + rz2) // 2, 'glow_lichen[west=true]'); put(rx2, ry1 + 2, (rz1 + rz2) // 2, 'glow_lichen[east=true]')
for x in range(rx1 + 1, rx2):
    for z in range(rz1 + 3, rz2 + 1): put(x, ry1 + 1, z, 'red_carpet' if (x + z) % 4 else 'orange_carpet') if (x, z) != (sx0, rz2) else None
SEC_BTN = (0, 65, 50)
put(*SEC_BTN, 'polished_blackstone_button[face=wall,facing=south]')

# ------------------------------------------------------------------ dessus de l'île
for (x, z), b in TOP.items():
    put(x, G, z, b)

# arbres et plantes
def tree(kind, x, z):
    if kind == 'oak' or kind == 'birch':
        h = rnd.randint(5, 6) if kind == 'oak' else rnd.randint(6, 7)
        lv = LEAF(kind)
        cy = 63 + h - 0.5
        rx = 2.7 if kind == 'oak' else 2.1
        for xx in range(x - 3, x + 4):
            for yy in range(int(cy - 2), int(cy + 3)):
                for zz in range(z - 3, z + 4):
                    dd = ((xx - x) / rx) ** 2 + ((yy - cy) / 2.0) ** 2 + ((zz - z) / rx) ** 2
                    if dd <= 1 and (dd < 0.65 or rnd.random() < 0.55): setif(xx, yy, zz, lv)
        for y in range(64, 64 + h): put(x, y, z, f'{kind}_log')
    elif kind == 'cherry':
        h = rnd.randint(4, 5)
        for y in range(64, 64 + h): put(x, y, z, 'cherry_log')
        dx, dz = rnd.choice(((1, 0), (-1, 0), (0, 1), (0, -1)))
        put(x + dx, 63 + h, z + dz, 'cherry_log[axis=' + ('x' if dx else 'z') + ']')
        cy = 64 + h + 0.5
        for xx in range(x - 4, x + 5):
            for yy in range(int(cy - 2), int(cy + 2)):
                for zz in range(z - 4, z + 5):
                    dd = ((xx - x) / 3.8) ** 2 + ((yy - cy) / 1.7) ** 2 + ((zz - z) / 3.8) ** 2
                    if dd <= 1 and (dd < 0.7 or rnd.random() < 0.5): setif(xx, yy, zz, LEAF('cherry'))
        for (xx, zz) in (disc(x, z, 3.5) if PETALS else []):
            if TOP.get((xx, zz)) == 'grass_block' and get(xx, 64, zz) is None and rnd.random() < 0.45:
                put(xx, 64, zz, f'pink_petals[flower_amount={rnd.randint(1, 4)},facing={rnd.choice(["north", "south", "east", "west"])}]')
    elif kind == 'spruce':
        h = rnd.randint(8, 10)
        for y in range(64, 64 + h): put(x, y, z, 'spruce_log')
        for y in range(66, 64 + h + 2):
            rr = max(0.0, (64 + h + 1 - y) * 0.42) * (1.0 if y % 2 else 0.7)
            for (xx, zz) in disc(x, z, rr + 0.3): setif(xx, y, zz, LEAF('spruce'))
        setif(x, 64 + h + 1, z, LEAF('spruce'))
    elif kind == 'mushroom':
        h = rnd.randint(5, 7)
        for y in range(64, 64 + h): put(x, y, z, 'mushroom_stem')
        if rnd.random() < 0.6:
            cy = 63 + h
            for xx in range(x - 4, x + 5):
                for yy in range(cy - 2, cy + 3):
                    for zz in range(z - 4, z + 5):
                        dd = ((xx - x) / 3.4) ** 2 + ((yy - cy + 0.5) / 2.4) ** 2 + ((zz - z) / 3.4) ** 2
                        if 0.55 <= dd <= 1 and yy >= cy - 1: setif(xx, yy, zz, 'red_mushroom_block')
        else:
            for (xx, zz) in disc(x, z, 3.6): setif(xx, 64 + h, zz, 'brown_mushroom_block')
    elif kind == 'bamboo':
        for (xx, zz) in disc(x, z, 1.8):
            if rnd.random() < 0.55 and TOP.get((xx, zz)) == 'grass_block' and get(xx, 64, zz) is None:
                hh = rnd.randint(6, 11)
                for y in range(64, 64 + hh):
                    lv = 'large' if y >= 64 + hh - 2 else ('small' if y == 64 + hh - 3 else 'none')
                    setif(xx, y, zz, f'bamboo[age=0,leaves={lv}]')
    elif kind == 'lantern':
        put(x, 64, z, 'polished_andesite'); put(x, 65, z, 'andesite_wall'); put(x, 66, z, 'andesite_wall'); put(x, 67, z, 'lantern')
    elif kind == 'bush':
        for xx in range(x - 2, x + 3):
            for yy in (64, 65):
                for zz in range(z - 2, z + 3):
                    dd = ((xx - x) / 1.7) ** 2 + ((yy - 64) / 1.3) ** 2 + ((zz - z) / 1.7) ** 2
                    if dd <= 1: setif(xx, yy, zz, 'flowering_azalea_leaves[persistent=true]' if rnd.random() < 0.4 else 'azalea_leaves[persistent=true]')

def free(x, z, rad):
    for (xx, zz) in disc(x, z, rad):
        if MASK.get((xx, zz)) != 'g': return False
        for y in range(64, 70):
            if get(xx, y, zz) is not None: return False
    return True
def species(x, z):
    if x > 0 and z < 0: return rnd.choice(['cherry', 'cherry', 'cherry', 'bush', 'birch'])
    if x > 0 and z > 0: return rnd.choice(['mushroom', 'mushroom', 'oak', 'bush', 'oak'])
    if x < 0 and z > 0: return rnd.choice(['oak', 'birch', 'oak', 'bush', 'birch'])
    return rnd.choice(['spruce', 'bamboo', 'spruce', 'lantern', 'bamboo', 'bush'])
TREES = []
cands = [p for p in ISL if MASK[p] == 'g' and 17 < math.hypot(*p) < 58]
rnd.shuffle(cands)
for (x, z) in cands:
    if any(math.hypot(x - a, z - b) < 7.5 for a, b in TREES): continue
    if not free(x, z, 2.2): continue
    TREES.append((x, z)); tree(species(x, z), x, z)
for (x, z) in cands[:0]: pass
# arbres autour de la promenade (côté extérieur)
for k in range(40):
    a = rnd.uniform(0, 2 * math.pi); r = rnd.uniform(64.5, 67.5); x, z = round(r * math.cos(a)), round(r * math.sin(a))
    if (x, z) in ISET and math.hypot(x, z) < edge(x, z) - 2.5 and free(x, z, 1.6) and not any(math.hypot(x - p, z - q) < 7 for p, q in TREES):
        TREES.append((x, z)); tree(rnd.choice(['oak', 'birch', 'bush', 'spruce']) if not (x > 0 and z < 0) else 'cherry', x, z)
# lampadaires de la promenade
for k in range(30):
    a = math.radians(6 + 12 * k); x, z = round(64.4 * math.cos(a)), round(64.4 * math.sin(a))
    if (x, z) in ISET and MASK[(x, z)] == 'g' and all(get(x, y, z) is None for y in range(64, 69)): lamp(x, z, 'stone')
# herbes et fleurs
for (x, z) in ISL:
    if TOP[(x, z)] != 'grass_block' or get(x, 64, z) is not None: continue
    m = MASK[(x, z)]; q = rnd.random()
    if m == 'f':
        if q < 0.75: put(x, 64, z, rnd.choice(FLOWERS))
        elif q < 0.9: put(x, 64, z, 'short_grass')
    elif m == 'h': hedge(x, z)
    elif m == 'g':
        if q < 0.20: put(x, 64, z, 'short_grass')
        elif q < 0.24: put(x, 64, z, 'fern')
        elif q < 0.29: put(x, 64, z, rnd.choice(FLOWERS))

# ------------------------------------------------------------------ petites îles volantes
def islet(cx, cy, cz, r, kind, fall_to=None):
    cells = [(x, z) for (x, z) in disc(cx, cz, r + 1) if math.hypot(x - cx, z - cz) <= r - 0.6 + 1.2 * vn(x, z, 2, 9)]
    for (x, z) in cells:
        t = math.hypot(x - cx, z - cz) / (r + 0.6)
        dep = int(2 + (r * 1.6) * (1 - t * t) * (0.7 + 0.6 * vn(x, z, 2.5, 11)))
        put(x, cy, z, 'grass_block')
        for y in range(cy - dep, cy):
            put(x, y, z, 'dirt' if y > cy - 3 else shell(x, y - 20, z))
        if rnd.random() < 0.15: setif(x, cy - dep - 1, z, 'hanging_roots')
    for (x, z) in cells:
        if get(x, cy + 1, z) is None and rnd.random() < 0.3: setif(x, cy + 1, z, rnd.choice(['short_grass', 'short_grass'] + FLOWERS))
    if kind:
        W.pop((cx, cy + 1, cz), None)
        tree_at(kind, cx, cy, cz)
    if fall_to:
        dx, dz = fall_to[0] - cx, fall_to[1] - cz; dl = math.hypot(dx, dz)
        for s in [x / 4 for x in range(int(r * 4), int(r * 4) + 16)]:
            x, z = round(cx + dx / dl * s), round(cz + dz / dl * s)
            if (x, z) not in cells: break
        JETS.append((x, cy, z))
def tree_at(kind, x, y0, z):
    # arbre posé sur une île volante : on décale tout de (y0 - 63)
    global W, PETALS
    before = dict(W); W = {}; PETALS = False
    tree(kind, x, z)
    PETALS = True
    moved = {(a, b + (y0 - G), c): v for (a, b, c), v in W.items()}
    W = before
    for k, v in moved.items():
        if k not in W: W[k] = v
islet(31, 90, -31, 5, 'cherry', fall_to=(29, -29))
islet(-34, 94, 31, 5, 'oak')
islet(-31, 98, -35, 4, 'spruce')
islet(37, 96, 31, 4, 'mushroom')
islet(-6, 104, 30, 3, 'bush')

# ------------------------------------------------------------------ PARKOUR (est) : jardin suspendu, puis la Tour céleste en spirale
PK = []
def pk(x, y, z, b): PK.append((x, y, z, b))
S1 = [(71, 0, 63, 'moss_block'), (74, 2, 63, LEAF('oak')), (77, 1, 64, 'moss_block'), (80, -1, 64, 'flowering_azalea_leaves[persistent=true]'),
      (83, -2, 65, 'mossy_cobblestone'), (86, -1, 65, 'oak_log[axis=x]'), (89, 1, 66, 'moss_block'), (92, 2, 66, 'mossy_stone_bricks'),
      (95, 1, 66, 'oak_fence'), (98, 0, 67, 'moss_block')]
for (x, z, y, b) in S1: pk(x, y, z, b)
CPS = [((67.5, 64, 0.5), 0, 63)]       # (position du marqueur, numéro, y du bloc)
def platform(cx, cy, cz, b='lapis_block'):
    for x in range(cx - 1, cx + 2):
        for z in range(cz - 1, cz + 2): pk(x, cy, z, b)
platform(102, 67, 0); CPS.append(((102.5, 68, 0.5), 1, 67))
pk(106, 67, 1, 'snow_block'); pk(109, 68, -1, 'packed_ice')
TC = (124, 0)
MATS = {0: ['packed_ice', 'snow_block', 'blue_ice', 'packed_ice', 'ice', 'snow_block', 'powder_snow_cauldron'],
        1: ['crimson_nylium', 'red_nether_bricks', 'warped_nylium', 'shroomlight', 'nether_brick_fence', 'blackstone', 'crying_obsidian', 'glowstone'],
        2: ['end_stone_bricks', 'purpur_block', 'white_stained_glass', 'quartz_block', 'purpur_pillar', 'light_blue_stained_glass', 'end_stone', 'amethyst_block']}
N = 42
ang = math.pi; y = 68; spiral = []
for i in range(N):
    r = 12.0 if i <= 30 else 12.0 - 3.5 * (i - 30) / (N - 1 - 30)
    if i > 0:
        rise = i % 3 != 2 and i not in (14, 28)
        if rise: y += 1
        px, _, pz, _ = spiral[-1]
        for st in [3.6 - 0.05 * k for k in range(30)]:
            a2 = ang - st / r
            x, z = round(TC[0] + r * math.cos(a2)), round(TC[1] + r * math.sin(a2))
            dh = math.hypot(x - px, z - pz)
            if 2.6 <= dh <= (3.5 if rise else 3.9): break
        ang = a2
    x, z = round(TC[0] + r * math.cos(ang)), round(TC[1] + r * math.sin(ang))
    spiral.append((x, y, z, i))
for (x, y, z, i) in spiral:
    if i in (14, 28):
        platform(x, y, z); CPS.append(((x + 0.5, y + 1, z + 0.5), 2 if i == 14 else 3, y))
    else:
        sec = 0 if i < 14 else (1 if i < 28 else 2)
        b = MATS[sec][i % len(MATS[sec])]
        if b == 'powder_snow_cauldron': b = 'snow_block'
        pk(x, y, z, b)
        if i % 4 == 1: pk(x, y - 1, z, 'soul_lantern[hanging=true]' if sec == 1 else 'lantern[hanging=true]')
# vérification des sauts
path = [(67, 63, 0)] + [(x, y, z) for (x, z, y, b) in S1] + [(102, 67, 0), (106, 67, 1), (109, 68, -1)] + [(x, y, z) for (x, y, z, i) in spiral]
for (a, b) in zip(path, path[1:]):
    dh = math.hypot(b[0] - a[0], b[2] - a[2]); dy = b[1] - a[1]
    lim = 4.3 if dy <= 0 else 3.7
    assert dy <= 1 and dh <= lim + (1.0 if a in ((102, 67, 0),) or b in ((102, 67, 0),) else 0), ('saut', a, b, dh, dy)
FINY = spiral[-1][1] + 1
# tour
for yy in range(40, FINY):
    rr = 3.6 if yy >= 52 else 0.6 + 3.0 * (yy - 40) / 12
    for (x, z) in disc(TC[0], TC[1], rr):
        outer = math.hypot(x - TC[0], z - TC[1]) > rr - 1.1
        if yy < 52: b = 'dripstone_block' if (x + z + yy) % 3 else 'calcite'
        elif not outer: b = 'smooth_quartz'
        elif yy % 8 == 0: b = 'sea_lantern'
        elif yy % 8 == 4: b = 'amethyst_block'
        else: b = 'smooth_quartz' if vn(x * 3 + yy, z * 3, 3, 5) < 0.6 else 'calcite'
        put(x, yy, z, b)
for (x, z) in disc(TC[0], TC[1], 5.4):
    r = math.hypot(x - TC[0], z - TC[1])
    put(x, FINY, z, 'diamond_block' if r < 2.2 else ('quartz_bricks' if r < 4.4 else 'gold_block'))
    if r < 4.6: put(x, FINY - 1, z, 'quartz_bricks')
box(TC[0] - 1, FINY - 2, TC[1] - 1, TC[0] + 1, FINY - 2, TC[1] + 1, 'iron_block')
put(TC[0], FINY - 1, TC[1], 'beacon'); put(TC[0], FINY, TC[1], 'lime_stained_glass')
assert math.hypot(spiral[-1][0] - TC[0], spiral[-1][2] - TC[1]) - 5.4 <= 3.3
FIN = (TC[0] + 0.5, FINY + 1, TC[1] + 0.5)
for (x, y, z, b) in PK: put(x, y, z, b)

# éclairage discret des chemins (blocs de lumière invisibles)
for (x, z) in ISL:
    if x % 6 == 0 and z % 6 == 0 and MASK[(x, z)] in ('p', 'b') and get(x, 64, z) is None and get(x, 65, z) is None:
        put(x, 65, z, 'light[level=12]')

