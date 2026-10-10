"""Génère le spawn (grande île flottante détaillée) : python tools/lobby/gen_lobby.py <racine du dépôt> [aperçu.png]

Île de ~70 blocs de rayon centrée sur 0 64 0 (sol en y = 63), entourée par les 15 plots (jamais touchés : chaque bloc posé est vérifié).
  - centre : rose des vents dorée (point d'apparition), douves avec jets d'eau, grande place pavée ;
  - ouest : l'Armurerie (château à toit de chêne noir, 4 socles d'armes) et le Stand de tir (cibles : le laser y marque les points) ;
  - est : porte du Parkour, puis le parcours au-dessus du vide jusqu'à la Tour céleste (spirale, 3 checkpoints, balise au sommet) ;
  - nord : le Portail des plots (on le traverse pour aller sur son plot) ;
  - sud : le Garage Kart (piste, podium, tuyaux) ;
  - quatre jardins (cerisiers et étang, champignons géants, parc et fontaine, bambous et lanternes), promenade circulaire,
    ponts vers chaque plot, cascades, petites îles volantes ; dessous de l'île en roche avec racines, lichen lumineux et lianes.
Les modèles du resource pack (logo, panneaux, armes, karts, boîtes ?, trophée, cristaux, ballons) sont posés si $rp = 1, sinon des
équivalents vanilla.
Sorties : data/mg/function/lobby/ (build*, deco*, anim, fx, armory_*, pads, laser_hit, portal) et parkour/ (build, fall_check, fall, board_refresh).
"""
import math, os, random, re, sys

R = sys.argv[1]
F = os.path.join(R, 'data', 'mg', 'function')
G = 63
rnd = random.Random(20261007)

# ------------------------------------------------------------------ plots (lus dans plot/build_all : murs = zone interdite)
PLOTS = []
for l in open(os.path.join(F, 'plot', 'build_all.mcfunction'), encoding='utf-8'):
    m = re.search(r'\{n:(\d+),lx:([-\d.]+),lz:([-\d.]+),wx1:(-?\d+),wx2:(-?\d+),wz1:(-?\d+),wz2:(-?\d+)', l)
    if m: PLOTS.append((int(m[1]), float(m[2]), float(m[3])) + tuple(int(v) for v in m.groups()[3:]))
assert len(PLOTS) == 15
def inplot(x, z, mg=0): return any(a - mg <= x <= b + mg and c - mg <= z <= d + mg for _, _, _, a, b, c, d in PLOTS)

W = {}
def put(x, y, z, b):
    assert not inplot(x, z), ('plot !', x, y, z, b)
    W[(x, y, z)] = b
def setif(x, y, z, b):
    if (x, y, z) not in W and not inplot(x, z): W[(x, y, z)] = b
def box(x1, y1, z1, x2, y2, z2, b):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            for z in range(min(z1, z2), max(z1, z2) + 1): put(x, y, z, b)
def get(x, y, z): return W.get((x, y, z))

def h2(i, j, s):
    n = (i * 374761393 + j * 668265263 + s * 2246822519) & 0xffffffff
    n = ((n ^ (n >> 13)) * 1274126177) & 0xffffffff
    return ((n ^ (n >> 16)) & 0xffff) / 65535
def vn(x, z, sc, s):
    fx, fz = x / sc, z / sc
    i, j = math.floor(fx), math.floor(fz)
    tx, tz = fx - i, fz - j
    tx, tz = tx * tx * (3 - 2 * tx), tz * tz * (3 - 2 * tz)
    a, b, c, d = h2(i, j, s), h2(i + 1, j, s), h2(i, j + 1, s), h2(i + 1, j + 1, s)
    return a + (b - a) * tx + (c - a) * tz + (a - b - c + d) * tx * tz

LEAF = lambda t: f'{t}_leaves[persistent=true]'
FLOWERS = ['poppy', 'dandelion', 'cornflower', 'allium', 'azure_bluet', 'oxeye_daisy', 'red_tulip', 'orange_tulip', 'white_tulip', 'pink_tulip',
           'lily_of_the_valley', 'blue_orchid']

# ------------------------------------------------------------------ île : contour, dessus, dessous
def edge(x, z):
    t = math.atan2(z, x)
    return 71 + 1.6 * math.sin(5 * t + 0.7) + 1.2 * math.sin(11 * t + 2.1) + 0.6 * math.sin(23 * t)
ISL = [(x, z) for x in range(-77, 78) for z in range(-77, 78) if math.hypot(x, z) <= edge(x, z)]
ISET = set(ISL)
for (x, z) in ISL: assert not inplot(x, z, 2), ('île trop près d\'un plot', x, z)

TOP = {p: 'grass_block' for p in ISL}
MASK = {p: 'g' for p in ISL}
def paint(x, z, b, m='p'):
    if (x, z) in TOP: TOP[(x, z)] = b; MASK[(x, z)] = m

BOT = {}
for (x, z) in ISL:
    r = math.hypot(x, z); t = min(1.0, r / edge(x, z))
    depth = 6 + 34 * (1 - t * t) ** 0.75 * (0.65 + 0.7 * vn(x, z, 9, 1)) + 4 * vn(x, z, 3.5, 2)
    BOT[(x, z)] = int(G - 1 - depth)
# pointes rocheuses sous l'île
for k in range(9):
    a = rnd.uniform(0, 2 * math.pi); rr = rnd.uniform(0, 34); sx, sz = int(rr * math.cos(a)), int(rr * math.sin(a))
    L, rad = rnd.randint(8, 16), rnd.uniform(2.5, 4.5)
    for (x, z) in ISL:
        d = math.hypot(x - sx, z - sz)
        if d < rad: BOT[(x, z)] = min(BOT[(x, z)], int(BOT[(sx, sz)] - L * (1 - d / rad)))

def shell(x, y, z):
    n = vn(x + y * 3, z - y * 2, 6, 3)
    if y >= 59: return 'dirt' if n < 0.55 else ('coarse_dirt' if n < 0.8 else 'rooted_dirt')
    if y >= 50: return 'stone' if n < 0.45 else ('andesite' if n < 0.7 else ('mossy_cobblestone' if n < 0.85 else 'cobblestone'))
    if y >= 38: return 'stone' if n < 0.4 else ('tuff' if n < 0.65 else ('andesite' if n < 0.85 else 'calcite'))
    return 'deepslate' if n < 0.5 else ('tuff' if n < 0.75 else 'cobbled_deepslate')
ORES = {True: ['coal_ore', 'iron_ore', 'copper_ore', 'gold_ore', 'lapis_ore'], False: ['deepslate_coal_ore', 'deepslate_iron_ore', 'deepslate_diamond_ore',
                                                                                        'deepslate_redstone_ore', 'deepslate_emerald_ore']}
for (x, z) in ISL:
    b0 = BOT[(x, z)]
    nb = [BOT.get((x + dx, z + dz), 999) for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1))]
    for y in range(b0, G):
        exposed = y == b0 or any(v > y for v in nb)
        if not exposed: put(x, y, z, 'dirt' if y >= 59 else 'stone')
        elif y == b0 and y < 57 and rnd.random() < 0.05: put(x, y, z, rnd.choice(ORES[y >= 38]))
        else: put(x, y, z, shell(x, y, z))
    # sous la roche : racines, lichen lumineux, pointes, fleurs suspendues
    u = rnd.random()
    if b0 >= 55 and u < 0.12: put(x, b0 - 1, z, 'hanging_roots')
    elif u < 0.07: put(x, b0 - 1, z, 'glow_lichen[up=true]')
    elif u < 0.10: put(x, b0 - 1, z, 'pointed_dripstone[vertical_direction=down,thickness=tip]')
    elif u < 0.108: put(x, b0 - 1, z, 'spore_blossom')
# lianes sur le pourtour
for (x, z) in ISL:
    for dx, dz, face in ((1, 0, 'west'), (-1, 0, 'east'), (0, 1, 'north'), (0, -1, 'south')):
        nx, nz = x + dx, z + dz
        if (nx, nz) in ISET or rnd.random() > 0.22 or inplot(nx, nz): continue
        for y in range(G - 1, G - 1 - rnd.randint(2, 9), -1):
            if y < BOT[(x, z)]: break
            setif(nx, y, nz, f'vine[{face}=true]')

# ------------------------------------------------------------------ helpers de déco
def lamp(x, z, kind='blackstone', top='lantern'):
    wall = {'blackstone': 'polished_blackstone_wall', 'stone': 'stone_brick_wall', 'andesite': 'andesite_wall'}[kind]
    base = {'blackstone': 'chiseled_polished_blackstone', 'stone': 'chiseled_stone_bricks', 'andesite': 'polished_andesite'}[kind]
    put(x, 64, z, base); put(x, 65, z, wall); put(x, 66, z, wall); put(x, 67, z, wall); put(x, 68, z, top)
def bench(cells, facing):
    for (x, z) in cells: put(x, 64, z, f'spruce_stairs[facing={facing}]')
def hedge(x, z):
    if get(x, 64, z) is None: put(x, 64, z, 'flowering_azalea_leaves[persistent=true]' if rnd.random() < 0.3 else 'azalea_leaves[persistent=true]')
def disc(cx, cz, r):
    return [(x, z) for x in range(int(cx - r) - 1, int(cx + r) + 2) for z in range(int(cz - r) - 1, int(cz + r) + 2) if math.hypot(x - cx, z - cz) <= r]
def facing_of(dx, dz):
    if abs(dx) >= abs(dz): return 'east' if dx > 0 else 'west'
    return 'south' if dz > 0 else 'north'

PETALS = True
JETS = []   # sources d'eau posées sans « strict » à la fin (elles coulent)

# ------------------------------------------------------------------ promenade circulaire + chemins vers les ponts
for (x, z) in ISL:
    r = math.hypot(x, z)
    if 60 <= r < 63.5:
        u = vn(x, z, 2.5, 7)
        paint(x, z, 'dirt_path' if u < 0.72 else ('coarse_dirt' if u < 0.9 else 'packed_mud'))

# ------------------------------------------------------------------ place centrale
for (x, z) in ISL:
    r = math.hypot(x, z)
    if r > 15.5: continue
    a = math.degrees(math.atan2(z, x)) % 360
    if r < 1.6: b = 'gold_block'
    elif r < 4.6:
        da = min(a % 45, 45 - a % 45)
        ray = r * math.sin(math.radians(da)) < 0.55
        b = ('gold_block' if round(a / 45) % 2 == 0 else 'waxed_cut_copper') if ray else 'smooth_quartz'
    elif r < 5.6: b = 'polished_blackstone_bricks'
    elif r < 9.0:
        if abs(x) <= 1 or abs(z) <= 1: b = 'smooth_quartz'
        else: b = 'water'; MASK[(x, z)] = 'w'
    elif r < 10.0: b = 'chiseled_stone_bricks' if int(a / 15) % 2 == 0 and a % 15 < 4 else 'stone_bricks'
    elif r < 14.5: b = ['polished_andesite', 'polished_diorite'][(int(r) + int(a / 11.25)) % 2]
    else: b = 'gilded_blackstone' if a % 45 < 3 else 'polished_blackstone_bricks'
    if b == 'water': TOP[(x, z)] = 'water'
    else: paint(x, z, b)
for (x, z) in ISL:          # fond des douves
    r = math.hypot(x, z)
    if 5.6 <= r < 9.0 and TOP[(x, z)] == 'water':
        a = math.degrees(math.atan2(z, x)) % 360
        put(x, 62, z, 'sea_lantern' if a % 30 < 4 and 7 <= r < 8 else ('dark_prismarine' if (x + z) % 3 == 0 else 'prismarine'))
for sx in (-5, 5):          # jets d'eau sur les diagonales
    for sz in (-5, 5):
        TOP[(sx, sz)] = 'prismarine_bricks'
        put(sx, 64, sz, 'prismarine_bricks'); put(sx, 65, sz, 'prismarine_bricks'); put(sx, 66, sz, 'sea_lantern')
        JETS.append((sx, 67, sz))
for k in range(8):          # lampadaires et massifs de fleurs autour de la place
    a = math.radians(22.5 + 45 * k)
    lamp(round(14 * math.cos(a)), round(14 * math.sin(a)))
for k in range(4):
    a = math.radians(45 + 90 * k); cx, cz = 11.6 * math.cos(a), 11.6 * math.sin(a)
    for (x, z) in disc(cx, cz, 1.9):
        paint(x, z, 'grass_block', 'f')
    put(round(cx), 64, round(cz), 'flowering_azalea')

# ------------------------------------------------------------------ avenues
def av(d, u, v):
    return {'E': (u, v), 'W': (-u, v), 'S': (v, u), 'N': (v, -u)}[d]
AVLEN = {'E': 63, 'W': 35, 'S': 36, 'N': 44}
for d, L in AVLEN.items():
    for u in range(15, L + 1):
        for v in range(-6, 7):
            x, z = av(d, u, v)
            if (x, z) not in ISET: continue
            av_ = abs(v)
            if av_ <= 2:
                q = rnd.random()
                paint(x, z, 'mossy_stone_bricks' if q < 0.06 else ('cracked_stone_bricks' if q < 0.1 else 'stone_bricks'))
            elif av_ == 3: paint(x, z, 'polished_andesite')
            elif av_ == 4: paint(x, z, 'grass_block', 'h')
            else: paint(x, z, 'grass_block', 'f')
    for u in range(17, L - 1):
        for side in (-1, 1):
            x, z = av(d, u, 4 * side)
            if (u - 17) % 10 == 0 and (u // 10 + side) % 2 == 0: lamp(x, z)
            elif (u - 22) % 10 in (0, 1, 2) and u + 2 < L - 1:
                ox, oz = av(d, u, 5 * side); bx, bz = av(d, u, 4 * side)
                bench([(x, z)], facing_of(ox - bx, oz - bz))
            elif (u - 22) % 10 in (9, 3): pass
            else: hedge(x, z)

# ------------------------------------------------------------------ ARMURERIE (ouest) + STAND DE TIR
X1, X2, Z1, Z2 = -57, -35, -11, 11
for x in range(X1 - 2, X2 + 3):
    for z in range(Z1 - 2, Z2 + 3):
        if X1 <= x <= X2 and Z1 <= z <= Z2: paint(x, z, 'polished_deepslate' if (x + z) % 2 else 'deepslate_tiles', 'b')
        else: paint(x, z, 'cobblestone' if rnd.random() < 0.3 else 'stone_bricks', 'b')
def wallb(x, y, z, along):
    if y == 64: return 'deepslate_bricks'
    if y == 71: return f'stripped_dark_oak_log[axis={along}]'
    c = x if along == 'x' else z
    if c % 4 == 0: return 'dark_oak_log'
    q = rnd.random()
    return 'mossy_stone_bricks' if q < 0.14 else ('cracked_stone_bricks' if q < 0.22 else 'stone_bricks')
for y in range(64, 72):
    for x in range(X1, X2 + 1):
        for z in (Z1, Z2):
            win = (x - X1) % 6 in (2, 3) and 66 <= y <= 68 and X1 + 1 < x < X2 - 1
            put(x, y, z, 'iron_bars' if win else wallb(x, y, z, 'x'))
    for z in range(Z1 + 1, Z2):
        for x in (X1, X2):
            if x == X2 and abs(z) <= 2 and y <= 67: continue
            put(x, y, z, wallb(x, y, z, 'z'))
put(X2, 68, 0, 'chiseled_stone_bricks')
for z in (-2, 2): put(X2, 68, z, 'stone_brick_stairs[facing=' + ('north' if z < 0 else 'south') + ',half=top]')
for z in (-4, 4):
    put(X2 + 1, 68, z, 'red_wall_banner[facing=east]'); put(X2 + 1, 66, z, 'wall_torch[facing=east]')
# panneau d'armes (mur ouest)
for z in range(-7, 8):
    for y in range(65, 70): put(X1, y, z, 'stripped_dark_oak_log[axis=z]' if y in (65, 69) or abs(z) == 7 else 'dark_oak_planks')
# toit à deux pans (faîte selon x)
for k in range(12):
    for x in range(X1 - 1, X2 + 2):
        put(x, 72 + k, -12 + k, 'dark_oak_stairs[facing=south]')
        put(x, 72 + k, 12 - k, 'dark_oak_stairs[facing=north]')
for x in range(X1 - 1, X2 + 2): put(x, 83, 0, 'dark_oak_planks'); put(x, 84, 0, 'dark_oak_slab')
for gx in (X1, X2):
    for y in range(72, 84):
        for z in range(-(11 - (y - 72)), 12 - (y - 72)):
            win = math.hypot(z, (y - 77) * 1.0) < 2.4
            put(gx, y, z, 'orange_stained_glass' if win else ('stripped_dark_oak_log[axis=y]' if z == 0 else 'dark_oak_planks'))
# tours d'angle
for (tx, tz) in ((X1, Z1), (X1, Z2), (X2, Z1), (X2, Z2)):
    for y in range(63, 82):
        for x in range(tx - 2, tx + 3):
            for z in range(tz - 2, tz + 3):
                edge_ = abs(x - tx) == 2 or abs(z - tz) == 2
                if not edge_ and y > 63: continue
                corner = abs(x - tx) == 2 and abs(z - tz) == 2
                if y == 81:
                    if (x + z) % 2 == 0: put(x, y, z, 'stone_bricks')
                    continue
                slit = not corner and (x - tx == 0 or z - tz == 0) and y in (75, 76)
                if slit: continue
                q = rnd.random()
                put(x, y, z, 'polished_deepslate' if corner else ('mossy_stone_bricks' if q < 0.15 else 'stone_bricks'))
    box(tx - 1, 80, tz - 1, tx + 1, 80, tz + 1, 'spruce_planks')
    for k, rr in enumerate((1, 0)):
        box(tx - rr, 82 + k, tz - rr, tx + rr, 82 + k, tz + rr, 'deepslate_tiles')
    for y in range(84, 87): put(tx, y, tz, 'dark_oak_fence')
    put(tx, 87, tz, 'red_banner[rotation=4]')
    put(tx, 79, tz, 'lantern[hanging=true]')
# intérieur
for x in range(-48, X2):
    for z in (-1, 0, 1): put(x, 64, z, 'red_carpet')
PADS = [(-53, -9, 'red_concrete'), (-53, -5, 'yellow_concrete'), (-53, 3, 'cyan_concrete'), (-53, 7, 'white_concrete')]
for (px, pz, c) in PADS:
    for x in range(px, px + 3):
        for z in range(pz, pz + 3):
            corner = x in (px, px + 2) and z in (pz, pz + 2)
            put(x, 63, z, c if (x, z) == (px + 1, pz + 1) else ('sea_lantern' if corner else 'polished_blackstone'))
north = ['barrel[facing=up]', 'smithing_table', 'anvil[facing=east]', 'blast_furnace[facing=south,lit=true]', 'grindstone[face=floor,facing=east]',
         'lava_cauldron', 'crafting_table', 'barrel[facing=up]', 'fletching_table', 'barrel[facing=up]']
for i, b in enumerate(north): put(-47 + i, 64, Z1 + 1, b)
put(-47, 65, Z1 + 1, 'barrel[facing=up]'); put(-38, 65, Z1 + 1, 'lantern')
south = ['hay_block', 'barrel[facing=up]', 'target', 'barrel[facing=up]', 'hay_block', 'chiseled_bookshelf[facing=north]', 'loom[facing=north]',
         'cartography_table', 'barrel[facing=up]', 'hay_block']
for i, b in enumerate(south): put(-47 + i, 64, Z2 - 1, b)
put(-47, 65, Z2 - 1, 'lantern'); put(-38, 65, Z2 - 1, 'lantern')
for cx in (-50, -42):          # lustres
    for y in range(74, 83): put(cx, y, 0, 'iron_chain')
    put(cx, 73, 0, 'lantern[hanging=true]')
    for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        put(cx + dx, 74, dz, 'iron_chain'); put(cx + dx, 73, dz, 'lantern[hanging=true]')
for x in (-55, -45, -38):
    for z in (-8, 8): put(x, 67, z, 'light[level=14]')
# stand de tir (nord de l'armurerie)
RX1, RX2, RZ1, RZ2 = -57, -37, -34, -16
for x in range(RX1, RX2 + 1):
    for z in range(RZ1, RZ2 + 1):
        lane = x in (-50, -44)
        paint(x, z, 'mud_bricks' if lane else ('packed_mud' if rnd.random() < 0.8 else 'coarse_dirt'), 'b')
for x in range(RX1, RX2 + 1):
    for y in range(64, 72): put(x, y, RZ1, 'stone_bricks' if y < 71 else 'stone_brick_slab')
for z in range(RZ1 + 1, RZ2 + 1):
    put(RX1, 64, z, 'mossy_stone_bricks'); put(RX1, 65, z, 'stone_brick_wall')
for bx in (-52, -47, -42):
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            dd = max(abs(dx), abs(dy))
            put(bx + dx, 67 + dy, RZ1, 'target' if dd == 0 else ('white_wool' if dd == 1 else 'red_wool'))
    put(bx, 64, RZ1 + 1, 'hay_block'); put(bx - 2, 64, RZ1 + 1, 'hay_block[axis=x]'); put(bx + 2, 64, RZ1 + 1, 'hay_block[axis=x]')
for tx in (-54, -48, -41):
    put(tx, 64, -25, 'oak_fence'); put(tx, 65, -25, 'hay_block'); put(tx, 66, -25, 'target')
for x in range(RX1 + 2, RX2 - 1): put(x, 64, -18, 'spruce_slab[type=top]')
for x in range(RX1 + 1, RX2): put(x, 68, -17, 'spruce_slab'); put(x, 68, -16, 'spruce_slab'); put(x, 68, -18, 'spruce_slab')
for px in (RX1 + 1, -47, RX2 - 1):
    for y in range(64, 68): put(px, y, -16, 'dark_oak_log')
for lx in (-52, -42): put(lx, 67, -17, 'lantern[hanging=true]')

# ------------------------------------------------------------------ PORTE DU PARKOUR (est)
for x in range(64, 71):
    for z in range(-4, 5):
        if (x, z) in ISET: paint(x, z, 'smooth_quartz' if (x + z) % 2 else 'quartz_bricks')
for x in range(66, 69):
    for z in range(-1, 2): paint(x, z, 'emerald_block')
for pz in (-4, 4):
    for x in (64, 65):
        for y in range(64, 72): put(x, y, pz, 'sea_lantern' if y == 67 else ('lime_stained_glass' if y in (66, 68) else 'quartz_pillar'))
for x in (64, 65):
    for z in range(-4, 5):
        put(x, 72, z, 'emerald_block' if z == 0 else 'smooth_quartz'); put(x, 73, z, 'quartz_slab' if abs(z) < 4 else 'quartz_bricks')

# ------------------------------------------------------------------ PORTAIL DES PLOTS (nord)
PC = (0, -47)
for (x, z) in disc(0, -47, 8.4):
    if (x, z) not in ISET: continue
    r = math.hypot(x, z + 47); a = math.degrees(math.atan2(z + 47, x))
    b = 'purpur_block' if r > 7.2 else ('crying_obsidian' if (a + r * 22) % 90 < 20 else 'obsidian')
    paint(x, z, b)
for z in (-48, -47):
    for x in range(-7, 8):
        for y in range(64, 79):
            d = math.hypot(x, y - 71)
            if y < 71 and abs(x) < 5: continue
            if not (5 <= d <= 6.7 or (y < 71 and 5 <= abs(x) <= 6)): continue
            if y < 71 and abs(x) > 6: continue
            put(x, y, z, 'amethyst_block' if d < 5.6 or (y < 71 and abs(x) == 5) else ('crying_obsidian' if y < 66 else 'purpur_block'))
    put(0, 78, z, 'amethyst_cluster[facing=up]')
for y in (65, 69, 73): put(0, y, -47, 'light[level=15]')
for sx in (-8, 8):
    put(sx, 64, -47, 'purpur_pillar'); put(sx, 65, -47, 'purpur_pillar'); put(sx, 66, -47, 'end_rod[facing=up]')

# ------------------------------------------------------------------ GARAGE KART (sud)
GC = (0, 48)
for (x, z) in disc(0, 48, 13.4):
    if (x, z) not in ISET: continue
    r = math.hypot(x, z - 48); a = math.degrees(math.atan2(z - 48, x)) % 360
    if r < 6: b = 'black_concrete' if ((x // 2) + (z // 2)) % 2 else 'white_concrete'
    elif r < 7: b = 'red_concrete' if int(a / 10) % 2 else 'white_concrete'
    elif r < 10: b = 'light_gray_concrete' if 8.3 <= r < 8.8 and int(a / 8) % 2 else 'gray_concrete'
    elif r < 11: b = 'red_concrete' if int(a / 10) % 2 else 'white_concrete'
    else: b = None
    if b: paint(x, z, b, 'b')
for (x0, h, b) in ((-4, 2, 'iron_block'), (-1, 3, 'gold_block'), (2, 1, 'waxed_copper_block')):
    box(x0, 64, 47, x0 + 2, 63 + h, 49, b)
for px in (-6, 6):
    for y in range(64, 71): put(px, y, 36, 'red_concrete' if y % 2 else 'white_concrete'); put(px, y, 37, 'red_concrete' if y % 2 == 0 else 'white_concrete')
for x in range(-6, 7):
    for y in (71, 72):
        for z in (36, 37): put(x, y, z, 'black_concrete' if (x + y + z) % 2 else 'white_concrete')
PIPES = [(-12, 39), (12, 39), (-12, 57), (12, 57)]
for (cx, cz) in PIPES:
    for (x, z) in disc(cx, cz, 1.6):
        for y in range(64, 67): put(x, y, z, 'green_concrete')
    for (x, z) in disc(cx, cz, 2.3): put(x, 67, z, 'lime_concrete')
    for (x, z) in disc(cx, cz, 0.8): put(x, 67, z, 'black_concrete')
for (cx, cz) in ((-9, 60), (9, 60), (-13, 48), (13, 48)):     # piles de pneus
    for y in range(64, 64 + rnd.randint(2, 3)): put(cx, y, cz, 'black_wool' if y % 2 else 'coal_block')

# ------------------------------------------------------------------ jardins
POND = (30, -30, 6.6)
for (x, z) in disc(POND[0], POND[1], POND[2] + 1.2):
    if (x, z) not in ISET: continue
    r = math.hypot(x - POND[0], z - POND[1])
    if r <= POND[2]:
        TOP[(x, z)] = 'water'; MASK[(x, z)] = 'w'
        put(x, 62, z, 'water' if r < 3.5 else ('clay' if rnd.random() < 0.4 else 'sand'))
        if r < 3.5: put(x, 61, z, 'clay')
        if rnd.random() < 0.12 and r > 1.5: put(x, 64, z, 'lily_pad')
    else: paint(x, z, rnd.choice(['mossy_cobblestone', 'stone', 'moss_block', 'grass_block']), 'r')
FOUNT = (-30, 30)
for (x, z) in disc(FOUNT[0], FOUNT[1], 5.5):
    r = math.hypot(x - FOUNT[0], z - FOUNT[1])
    if r > 4.5: paint(x, z, 'polished_andesite')
    elif r > 3.5: paint(x, z, 'stone_bricks'); put(x, 64, z, 'stone_brick_slab')
    else: paint(x, z, 'stone_bricks', 'w'); put(x, 64, z, 'water')
for y in range(64, 67): put(FOUNT[0], y, FOUNT[1], 'chiseled_stone_bricks' if y == 66 else 'stone_brick_wall')
put(FOUNT[0], 66, FOUNT[1], 'chiseled_stone_bricks'); JETS.append((FOUNT[0], 67, FOUNT[1]))
for (x, z) in disc(FOUNT[0], FOUNT[1], 1.5):
    if (x, z) != FOUNT: put(x, 64, z, 'water')

# ponts vers chaque plot
def bridge(n, lx, lz, a, b_, c, d):
    ang = math.atan2(lz, lx); ux, uz = math.cos(ang), math.sin(ang); px_, pz_ = -uz, ux
    t = 58.0
    k = 0
    while t < 100:
        cx, cz = ux * t, uz * t
        if inplot(round(cx), round(cz)): break
        for o in (-1.5, -1, -0.5, 0, 0.5, 1, 1.5):
            x, z = round(cx + px_ * o), round(cz + pz_ * o)
            if inplot(x, z): continue
            if (x, z) in ISET:
                if math.hypot(x, z) >= 63.5: paint(x, z, 'dirt_path')
            else: put(x, G, z, 'spruce_planks'); setif(x, G - 1, z, 'spruce_slab[type=top]')
        for o in (-2.3, 2.3):
            x, z = round(cx + px_ * o), round(cz + pz_ * o)
            if (x, z) in ISET or inplot(x, z): continue
            put(x, G, z, 'spruce_planks'); put(x, G + 1, z, 'spruce_fence')
            if k % 10 == 0: put(x, G + 2, z, 'lantern')
        t += 0.5; k += 1
for p in PLOTS: bridge(*p)
# cascades au bord de l'île (petit ruisseau puis chute dans le vide)
for deg in (33.75, 123.75, 213.75, 303.75):
    a = math.radians(deg); ux, uz = math.cos(a), math.sin(a)
    t = 63.6
    while True:
        x, z = round(ux * t), round(uz * t)
        if (x, z) not in ISET: break
        TOP[(x, z)] = 'water'; MASK[(x, z)] = 'w'; put(x, 62, z, 'stone')
        t += 0.5
    JETS.append((x, G, z))

# ------------------------------------------------------------------ CIRCUIT DU SPAWN (kart libre) : départ derrière le garage, sort de l'île
# entre les plots 3 et 4, grande boucle au sud au-dessus du vide (saut, boosts), revient entre les plots 4 et 5.
KWP = [(0, 66), (9, 66.5), (15, 69), (18.5, 76), (18.5, 84), (18.5, 96), (18.5, 108), (19, 115), (28, 124), (48, 131), (72, 136), (92, 150),
       (100, 172), (92, 196), (70, 208), (50, 203), (40, 188), (28, 172), (10, 166), (-8, 174), (-24, 192), (-46, 208), (-72, 210), (-94, 196),
       (-102, 170), (-92, 146), (-70, 132), (-48, 126), (-28, 124), (-19, 115), (-18.5, 108), (-18.5, 96), (-18.5, 84), (-18.5, 76), (-15, 69), (-9, 66.5)]
def catmull(p0, p1, p2, p3, t):
    t2, t3 = t * t, t * t * t
    return tuple(0.5 * ((2 * p1[i]) + (-p0[i] + p2[i]) * t + (2 * p0[i] - 5 * p1[i] + 4 * p2[i] - p3[i]) * t2 + (-p0[i] + 3 * p1[i] - 3 * p2[i] + p3[i]) * t3) for i in (0, 1))
kraw = []
for i in range(len(KWP)):
    p0, p1, p2, p3 = KWP[i - 1], KWP[i], KWP[(i + 1) % len(KWP)], KWP[(i + 2) % len(KWP)]
    for k in range(40): kraw.append(catmull(p0, p1, p2, p3, k / 40))
KP = [kraw[0]]; acc = 0.0
for a, b in zip(kraw, kraw[1:] + kraw[:1]):
    d = math.dist(a, b)
    while acc + d >= 0.5:
        t = (0.5 - acc) / d; a = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t); d = math.dist(a, b); KP.append(a); acc = 0.0
    acc += d
KN = len(KP)
def ktan(i):
    a, b = KP[(i - 2) % KN], KP[(i + 2) % KN]; L = math.dist(a, b) or 1
    return ((b[0] - a[0]) / L, (b[1] - a[1]) / L)
def kyaw(dx, dz): return round(math.degrees(math.atan2(-dx, dz)), 1)
kworst = min(math.dist(KP[i], KP[j]) for i in range(0, KN, 4) for j in range(i + 80, KN - (80 if i < 80 else 0), 4))
assert kworst > 16, ('le circuit se croise', kworst)
kbuck = {}
for i, (x, z) in enumerate(KP): kbuck.setdefault((math.floor(x / 4), math.floor(z / 4)), []).append(i)
def knear(x, z):
    best, bi = 1e9, -1
    for gx in range(math.floor(x / 4) - 2, math.floor(x / 4) + 3):
        for gz in range(math.floor(z / 4) - 2, math.floor(z / 4) + 3):
            for i in kbuck.get((gx, gz), ()):
                d = (KP[i][0] - x) ** 2 + (KP[i][1] - z) ** 2
                if d < best: best, bi = d, i
    return (math.sqrt(best), bi) if bi >= 0 else (99, -1)
KJ = min(range(KN), key=lambda i: math.dist(KP[i], (-59, 209)))
KBOOST = [int(f * KN) for f in (0.12, 0.36, 0.62, 0.86)]
KSTAMP = {}
def kstamp(i, w1, w2, l1, l2, fn):
    cx, cz = KP[i]; tx, tz = ktan(i); nx, nz = -tz, tx
    for a in [l1 + k * 0.5 for k in range(int((l2 - l1) * 2) + 1)]:
        for b in [w1 + k * 0.5 for k in range(int((w2 - w1) * 2) + 1)]:
            KSTAMP[(round(cx + tx * a + nx * b), round(cz + tz * a + nz * b))] = fn(round(a), round(b))
kstamp(0, -4.5, 4.5, -1, 1, lambda a, b: 'black_concrete' if (a + b) % 2 else 'white_concrete')
for bi in KBOOST: kstamp(bi, -2, 2, 0, 3, lambda a, b: 'orange_glazed_terracotta')
kstamp((KJ - 14) % KN, -4.5, 4.5, 0, 1.5, lambda a, b: 'lime_concrete')
def kgap(x, z):
    jx, jz = KP[KJ]; tx, tz = ktan(KJ)
    return abs((x - jx) * tx + (z - jz) * tz) <= 2.5 and abs((x - jx) * -tz + (z - jz) * tx) < 9
KROADC = set()
for x in range(-115, 116):
    for z in range(55, 225):
        d, si = knear(x, z)
        if d > 5.5 or kgap(x, z): continue
        onisl = (x, z) in ISET
        if d <= 4.5:
            b = KSTAMP.get((x, z)) or ('gray_concrete' if d <= 3.5 else ('white_concrete' if d <= 4 else ('red_concrete' if (si // 6) % 2 else 'white_concrete')))
            KROADC.add((x, z))
            if onisl:
                paint(x, z, b, 'b')
                for y in range(64, 70): W.pop((x, y, z), None)
            else:
                put(x, G, z, b); put(x, G - 1, z, 'stone_bricks')
                if si % 16 == 0 and d < 1: put(x, G + 2, z, 'light[level=13]')
        elif not onisl:
            put(x, G, z, 'stone_bricks'); put(x, G - 1, z, 'stone_brick_slab[type=top]')
            put(x, G + 1, z, 'red_concrete' if (si // 8) % 2 else 'white_concrete'); put(x, G + 2, z, 'barrier')
            if si % 24 == 0: put(x, G + 3, z, 'lantern')
# portique de départ en damier et tapis d'embarquement (garage)
sx_, sz_ = KP[0]; tx_, tz_ = ktan(0); nx_, nz_ = -tz_, tx_
for o in (-6.5, 6.5):
    px, pz = round(sx_ + nx_ * o), round(sz_ + nz_ * o)
    for y in range(G, 71): put(px, y, pz, 'black_concrete' if y % 2 else 'white_concrete')
for o in [k * 0.5 for k in range(-13, 14)]:
    px, pz = round(sx_ + nx_ * o), round(sz_ + nz_ * o)
    for y in (71, 72): put(px, y, pz, 'black_concrete' if (px + pz + y) % 2 else 'white_concrete')
KPAD = (-1, 54)
for x in range(KPAD[0], KPAD[0] + 3):
    for z in range(KPAD[1], KPAD[1] + 3): paint(x, z, 'yellow_glazed_terracotta' if (x, z) != (KPAD[0] + 1, KPAD[1] + 1) else 'gold_block', 'b')
KK = int(KN * 0.5 / 10)
KCPS = []
for k in range(KK):
    i = int(k * KN / KK)
    if (i - KJ) % KN < 12 or (KJ - i) % KN < 8: i = (KJ + 16) % KN            # jamais dans le trou du saut : après la réception
    x, z = KP[i]; tx, tz = ktan(i)
    KCPS.append((round(x, 1), round(z, 1), kyaw(tx, tz)))
print('circuit du spawn : longueur', round(KN * 0.5), '| points de passage', KK, '| écart mini', round(kworst, 1))

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

# ------------------------------------------------------------------ émission des commandes
def is_conn(b):
    n = b.split('[')[0]
    return n.endswith('_fence') or n.endswith('_wall') or n.endswith('_pane') or n == 'iron_bars'
def rects(cells):
    rows = {}
    for (x, z), b in cells.items(): rows.setdefault(x, []).append((z, b))
    out, active = [], {}
    for x in sorted(rows):
        lst = sorted(rows[x]); runs = []
        for z, b in lst:
            if runs and runs[-1][2] == b and runs[-1][1] == z - 1: runs[-1][1] = z
            else: runs.append([z, z, b])
        new = {}
        for z1, z2, b in runs:
            k = (z1, z2, b)
            if k in active and active[k][1] == x - 1: v = active.pop(k); v[1] = x; new[k] = v
            else: new[k] = [x, x]
        for k, v in active.items(): out.append((v[0], v[1], k[0], k[1], k[2]))
        active = new
    for k, v in active.items(): out.append((v[0], v[1], k[0], k[1], k[2]))
    return out
def merge(cells, suffix):
    layers = {}
    for (x, y, z), b in cells.items(): layers.setdefault(y, {})[(x, z)] = b
    boxes, active = [], {}
    for y in sorted(layers):
        new = {}
        for r in rects(layers[y]):
            if r in active and active[r][1] == y - 1: v = active.pop(r); v[1] = y; new[r] = v
            else: new[r] = [y, y]
        for r, v in active.items(): boxes.append((r, v[0], v[1]))
        active = new
    for r, v in active.items(): boxes.append((r, v[0], v[1]))
    boxes.sort(key=lambda t: (t[1], t[0][0], t[0][2]))
    cmds = []
    for (x1, x2, z1, z2, b), y1, y2 in boxes:
        ys = y1
        step = max(1, 32768 // ((x2 - x1 + 1) * (z2 - z1 + 1)))
        while ys <= y2:
            ye = min(y2, ys + step - 1)
            if x1 == x2 and z1 == z2 and ys == ye: cmds.append(f'setblock {x1} {ys} {z1} minecraft:{b}{suffix}')
            else: cmds.append(f'fill {x1} {ys} {z1} {x2} {ye} {z2} minecraft:{b}{suffix}')
            ys = ye + 1
    return cmds

clear = []
xs = {}
for x in range(-77, 78):
    zz = [z for z in range(-77, 78) if math.hypot(x, z) <= 76.5]
    if zz: clear.append(f'fill {x} 64 {min(zz)} {x} 122 {max(zz)} minecraft:air strict')
clear.append('fill 18 63 -8 125 80 6 minecraft:air strict')        # ancien parkour
for (x, z) in ISL: assert not inplot(x, z)
strict = {k: v for k, v in W.items() if not is_conn(v)}
conn = {k: v for k, v in W.items() if is_conn(v)}
CMDS = clear + merge(strict, ' strict') + merge(conn, '')
print('blocs', len(W), '| commandes', len(CMDS), '| arbres', len(TREES))

def wr(rel, lines):
    p = os.path.join(F, rel + '.mcfunction')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f: f.write('\n'.join(lines) + '\n')

old = [f for f in os.listdir(os.path.join(F, 'lobby')) if re.match(r'build_\d+\.mcfunction$', f)]
for f in old: os.remove(os.path.join(F, 'lobby', f))
PART = 3000
parts = [CMDS[i:i + PART] for i in range(0, len(CMDS), PART)]
for i, p in enumerate(parts, 1):
    nxt = f'mg:lobby/build_{i + 1}' if i < len(parts) else 'mg:lobby/build_end'
    wr(f'lobby/build_{i}', [f'# Spawn, partie {i}/{len(parts)} (généré par tools/lobby/gen_lobby.py)'] + p + [f'schedule function {nxt} 1t'])
wr('lobby/build', ['# Spawn : grande île flottante (générée par tools/lobby/gen_lobby.py), construite en plusieurs ticks',
                   'kill @e[type=minecraft:text_display,tag=mg.deco]',
                   'forceload add -80 -80 80 80', 'forceload add 81 -32 144 32', 'forceload add -115 81 115 225',
                   'tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Construction du spawn (quelques secondes)...","color":"gray"}]',
                   'schedule function mg:lobby/build_1 5s'])
wr('lobby/build_end', ['# Fin de la construction du spawn : eau qui coule, décor, chargement des zones'] +
   [f'setblock {x} {y} {z} minecraft:water' for (x, y, z) in JETS] +
   ['function mg:lobby/deco', 'function mg:lobby/armory_build', 'function mg:parkour/build',
    'forceload remove -80 -80 80 80', 'forceload remove 81 -32 144 32', 'forceload remove -115 81 115 225', 'function mg:core/forceloads', 'data modify storage mg:lobby v6 set value 1b',
    'tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Spawn construit.","color":"green"}]'])

# ------------------------------------------------------------------ entités de décor
TF = 'transformation:{{translation:[0f,{ty}f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[{s}f,{s}f,{s}f]}}'
def face_spawn(x, z):
    # orientation fixe du panneau, face lisible tournée vers le centre de la place (opposé du regard d'un joueur au centre)
    return round((math.degrees(math.atan2(-(x - 0.5), z - 0.5)) + 360) % 360 - 180, 1)
def tdisp(x, y, z, text, s, tags='', bill='vertical', yaw=None):
    rot = '' if yaw is None else f'Rotation:[{yaw}f,0f],'
    if yaw is not None: bill = 'fixed'
    return (f'summon minecraft:text_display {x} {y} {z} {{Tags:["mg.lby"{tags}],billboard:"{bill}",{rot}background:0,text:{text},'
            + TF.format(ty=0, s=s) + '}')
def idisp(x, y, z, item, s, tags='', bill='fixed', yaw=0, extra=''):
    return (f'summon minecraft:item_display {x} {y} {z} {{Tags:["mg.lby"{tags}],billboard:"{bill}",Rotation:[{yaw}f,0f],item:{item},'
            + TF.format(ty=0, s=s) + extra + '}')
def rp(model, base='minecraft:paper', color=None):
    comp = f'"minecraft:item_model":"mg:{model}"' + (f',"minecraft:dyed_color":{color}' if color is not None else '')
    return f'{{id:"{base}",components:{{{comp}}}}}'
def vi(i): return f'{{id:"minecraft:{i}"}}'
SPIN, BOB, BOTH = ',"mg.lspin"', ',"mg.lbob"', ',"mg.lspin","mg.lbob"'
G_ = lambda c: '{"text":"' + c + '","font":"mg:lobby"}'
SIGNS = [  # glyphe, texte vanilla, position, échelle rp, échelle vanilla
    ('', '[{"text":"✦ NEOMC ✦","color":"gold","bold":true},{"text":"\\nMINI-JEUX","color":"aqua","bold":true}]', (0.5, 72.5, 17.5), 4, 5),
    ('', '[{"text":"⚔ ARMURERIE ⚔","color":"gold","bold":true}]', (-33.3, 74, 0.5), 3.4, 3),
    ('', '[{"text":"◎ STAND DE TIR ◎","color":"red","bold":true}]', (-46.5, 72.5, -33.2), 2.6, 2.4),
    ('', '[{"text":"⚑ PARKOUR ⚑","color":"green","bold":true}]', (64.5, 75, 0.5), 3.2, 3),
    ('', '[{"text":"⌂ PLOTS ⌂","color":"light_purple","bold":true}]', (0.5, 80.5, -47), 3.4, 3.4),
    ('', '[{"text":"🏁 GARAGE KART 🏁","color":"red","bold":true}]', (0.5, 75, 36.5), 3.2, 3),
    ('', '[{"text":"★ ARRIVÉE ★","color":"aqua","bold":true}]', (FIN[0], FIN[1] + 5, FIN[2]), 3.4, 3),
]
HINTS = [
    ('[{"text":"Marche sur un socle pour t\'équiper !","color":"gray"}]', (-33.3, 69.4, 0.5), 1.3),
    ('[{"text":"Le railgun marque les points : vise le cœur des cibles !","color":"gray"}]', (-46.5, 71.6, -33.2), 1.1),
    ('[{"text":"Traverse le portail pour aller sur ","color":"gray"},{"text":"ton plot","color":"light_purple","bold":true}]', (0.5, 79.4, -47), 1.3),
    ('[{"text":"Bienvenue ! ","color":"yellow","bold":true},{"text":"⚔ Armurerie à l\'ouest, ⚑ Parkour à l\'est, ⌂ Plots au nord, 🏁 Kart au sud","color":"gray"}]', (0.5, 70.2, 17.5), 1.2),
]
common = ['# Décor commun (rp ou vanilla)']
for (t, pos, s) in HINTS: common.append(tdisp(*pos, t, s, yaw=face_spawn(pos[0], pos[2])))
for (z, it) in ((-5, 'iron_sword'), (-3, 'bow'), (-1, 'trident'), (1, 'crossbow'), (3, 'mace'), (5, 'diamond_sword')):
    common.append(idisp(-56.4, 67.2, z + 0.5, vi(it), 1.3, yaw=90).replace('left_rotation:[0f,0f,0f,1f]', 'left_rotation:[0f,0f,0.3827f,0.9239f]'))
for (x, z, yaw, set_) in ((-55.5, -3.5, -90, 'iron'), (-55.5, 4.5, -90, 'diamond'), (-37.5, 9.5, 180, 'golden'), (-37.5, -8.5, 0, 'netherite')):
    common.append(f'summon minecraft:armor_stand {x} 64 {z} {{Tags:["mg.lby"],Invulnerable:1b,NoGravity:1b,ShowArms:1b,DisabledSlots:4144959,Rotation:[{yaw}f,0f],'
                  f'equipment:{{head:{{id:"minecraft:{set_}_helmet"}},chest:{{id:"minecraft:{set_}_chestplate"}},legs:{{id:"minecraft:{set_}_leggings"}},'
                  f'feet:{{id:"minecraft:{set_}_boots"}},mainhand:{{id:"minecraft:{set_}_sword"}}}}}}')
rpl, vnl = ['# Décor du resource pack (modèles mg:*)'], ['# Décor vanilla (sans resource pack)']
for (g, txt, pos, s1, s2) in SIGNS:
    yaw = None if pos == (FIN[0], FIN[1] + 5, FIN[2]) else face_spawn(pos[0], pos[2])   # ARRIVÉE (haut du parkour) : reste tournante
    rpl.append(tdisp(*pos, G_(g), s1, yaw=yaw)); vnl.append(tdisp(*pos, txt, s2, yaw=yaw))
# boîtes ? en couronne au-dessus du point d'apparition + étoile
for k in range(8):
    a = math.radians(45 * k)
    rpl.append(idisp(round(0.5 + 3.6 * math.cos(a), 2), 69.5, round(0.5 + 3.6 * math.sin(a), 2), rp('item_box'), 0.9, BOTH))
rpl.append(idisp(0.5, 70.6, 0.5, rp('star'), 2.6, BOB, bill='vertical'))
vnl.append(idisp(0.5, 70.6, 0.5, vi('nether_star'), 2.2, BOB, bill='vertical'))
# ballons autour de la place
COLS = [16711680, 3368703, 16766720, 6750054, 16738740, 10053375]
for k in range(4):
    a = math.radians(45 + 90 * k); cx, cz = 11.6 * math.cos(a) + 0.5, 11.6 * math.sin(a) + 0.5
    for j in range(3):
        rpl.append(idisp(round(cx + (j - 1) * 0.7, 2), 66.6 + (j % 2) * 0.8, round(cz + (1 - j) * 0.5, 2),
                         rp('balloon', 'minecraft:leather_horse_armor', COLS[(k + j) % 6]), 1.3, BOB))
# garage : karts sur le podium et sur la piste, boîtes ?, tuyaux, Thwomp, Goombas
KC = [15022389, 2712319, 6610199, 16766720, 9315498, 16739584]
for (x, y, m, c) in ((0.5, 67, 'kart_bolide', KC[0]), (-2.5, 66, 'kart', KC[1]), (3.5, 65, 'kart_costaud', KC[2])):
    # le modèle est centré sur l'entité : on le remonte de la moitié de sa taille pour qu'il soit posé sur le podium
    rpl.append(idisp(x, round(y + 0.5 * 1.4 + 0.02, 2), 48.5, rp(m, 'minecraft:leather_horse_armor', c), 1.4, SPIN))
    vnl.append(idisp(x, round(y + 0.5 * 1.2 + 0.02, 2), 48.5, vi('minecart'), 1.2, SPIN))
for k, ang in enumerate((40, 160, 280)):
    a = math.radians(ang); x, z = 8.5 * math.cos(a) + 0.5, 48.5 + 8.5 * math.sin(a)
    yaw = (math.degrees(math.atan2(-math.cos(a + math.pi / 2), math.sin(a + math.pi / 2)))) % 360
    rpl.append(idisp(round(x, 2), round(64 + 0.5 * 1.1 + 0.02, 2), round(z, 2), rp(['kart_mini', 'kart', 'kart_bolide'][k], 'minecraft:leather_horse_armor', KC[3 + k]), 1.1, yaw=round(yaw, 1)))
for x in (-4.5, -1.5, 1.5, 4.5):
    rpl.append(idisp(x + 0.5, 74, 36.5, rp('item_box'), 1.0, BOTH))
for (cx, cz) in PIPES: rpl.append(idisp(cx + 0.5, 68.2, cz + 0.5, rp('piranha'), 1.3, BOB, yaw=rnd.choice((0, 90, 180, 270))))
rpl.append(idisp(0.5, 75.5, 48.5, rp('thwomp'), 3.0, BOB))
for (x, z, yaw) in ((-11.5, 47.5, 90), (10.5, 52.5, -90), (-4.5, 59.5, 180)):
    rpl.append(idisp(x, 64.55, z, rp('goomba'), 1.1, yaw=yaw))
# parkour : trophée et cristaux au sommet de la tour, cristaux du portail
rpl.append(idisp(FIN[0], FIN[1] + 1.6, FIN[2], rp('trophy'), 2.4, BOTH))
vnl.append(idisp(FIN[0], FIN[1] + 1.6, FIN[2], vi('gold_block'), 1.0, BOTH))
for k, c in enumerate((6740479, 16738740, 8453888, 16766720)):
    a = math.radians(45 + 90 * k)
    rpl.append(idisp(round(FIN[0] + 7 * math.cos(a), 2), FIN[1] + 3, round(FIN[2] + 7 * math.sin(a), 2), rp('crystal', 'minecraft:leather_horse_armor', c), 2.2, BOTH))
for sx in (-7.5, 8.5):
    rpl.append(idisp(sx, 68.5, -46.5, rp('crystal', 'minecraft:leather_horse_armor', 11751679), 1.6, BOTH))
    vnl.append(idisp(sx, 68.5, -46.5, vi('amethyst_cluster'), 1.4, BOTH))
# boîtes ? au-dessus des jardins aux champignons
for (x, y, z) in ((24.5, 72, 22.5), (30.5, 74, 30.5), (20.5, 73, 36.5), (38.5, 71, 20.5)):
    rpl.append(idisp(x, y, z, rp('item_box'), 1.2, BOTH))
wr('lobby/deco', ['# Décor du spawn (entités mg.lby) : modèles du resource pack si $rp = 1, sinon vanilla (généré)',
                  'kill @e[tag=mg.lby]', 'kill @e[type=minecraft:text_display,tag=mg.deco]', 'function mg:lobby/deco_common',
                  'execute if score $rp mg.st matches 1 run function mg:lobby/deco_rp',
                  'execute unless score $rp mg.st matches 1 run function mg:lobby/deco_vn',
                  'data modify storage mg:lobby deco3 set value 1b'])
wr('lobby/deco_common', common)
wr('lobby/deco_rp', rpl)
wr('lobby/deco_vn', vnl)

# animation (toutes les 2 s) et ambiance (toutes les 0,5 s)
Q = ['[0f,0f,0f,1f]', '[0f,0.7071f,0f,0.7071f]', '[0f,1f,0f,0f]', '[0f,0.7071f,0f,-0.7071f]']
anim = ['# Décor du spawn : rotation (mg.lspin) et flottement (mg.lbob), interpolés sur 2 s',
        'scoreboard players add $lph mg.st 1', 'execute if score $lph mg.st matches 4.. run scoreboard players set $lph mg.st 0',
        'execute as @e[type=minecraft:item_display,tag=mg.lby] run data merge entity @s {start_interpolation:0,interpolation_duration:40}']
for i in range(4):
    anim.append(f'execute if score $lph mg.st matches {i} as @e[type=minecraft:item_display,tag=mg.lspin] run data modify entity @s transformation.left_rotation set value {Q[(i + 1) % 4]}')
anim.append('execute if score $lph mg.st matches 0..3 as @e[type=minecraft:item_display,tag=mg.lbob] run data modify entity @s transformation.translation set value [0f,0f,0f]')
anim.append('execute if score $lph mg.st matches 0 as @e[type=minecraft:item_display,tag=mg.lbob] run data modify entity @s transformation.translation set value [0f,0.35f,0f]')
anim.append('execute if score $lph mg.st matches 2 as @e[type=minecraft:item_display,tag=mg.lbob] run data modify entity @s transformation.translation set value [0f,0.35f,0f]')
wr('lobby/anim', anim)
fx = ['# Ambiance du spawn (particules)',
      'particle minecraft:portal 0.5 68.5 -46.5 2.6 2.8 0.2 0.6 40',
      'particle minecraft:reverse_portal 0.5 68.5 -46.5 2.4 2.6 0.1 0.01 6',
      'particle minecraft:dust{color:[0.75,0.4,1.0],scale:1.2} 0.5 68.5 -46.5 2.6 2.8 0.15 0 8',
      'particle minecraft:end_rod 67.5 64.3 0.5 1.2 0.2 1.2 0.01 2',
      f'particle minecraft:end_rod {FIN[0]} {FIN[1] + 2} {FIN[2]} 3 1.5 3 0.01 3',
      'particle minecraft:cherry_leaves 30 72 -30 12 5 12 0 4',
      'particle minecraft:cherry_leaves 31 88 -31 4 1 4 0 2',
      'particle minecraft:glow 0.5 66 0.5 6 0.6 6 0 3',
      'particle minecraft:falling_water 0.5 67 0.5 7 0.5 7 0 4',
      'particle minecraft:wax_on 0.5 70 0.5 3.5 0.6 3.5 0 2']
for (x, y, z) in JETS[:4]: fx.append(f'particle minecraft:splash {x + 0.5} 64 {z + 0.5} 0.8 0.1 0.8 0 6')
wr('lobby/fx', fx)

# ------------------------------------------------------------------ armurerie : socles, tick, armes avec le resource pack
PADM = [('warped_fungus_on_a_stick', 'laser_gun', '⚡ Railgun', 'red'), ('blaze_rod', 'magic_wand', '✦ Baguette feu d\'artifice', 'gold'),
        ('wind_charge', 'wind_orb', '☁ Lance-vent', 'aqua'), ('snowball', 'snow_orb', '❄ Lance-neige', 'white')]
ab = ['# Armurerie du spawn : armes au-dessus des socles (généré par tools/lobby/gen_lobby.py)', 'kill @e[tag=mg.arm]']
for (px, pz, c), (it, mdl, name, col) in zip(PADS, PADM):
    cx, cz = px + 1.5, pz + 1.5
    item = f'{{id:"minecraft:{it}"}}'
    for tag, itm in (('rp', rp(mdl, f'minecraft:{it}')), ('vn', item)):
        cond = 'execute if score $rp mg.st matches 1 run ' if tag == 'rp' else 'execute unless score $rp mg.st matches 1 run '
        ab.append(cond + f'summon minecraft:item_display {cx} 65.6 {cz} {{Tags:["mg.arm","mg.lspin","mg.lbob"],billboard:"fixed",item:{itm},' + TF.format(ty=0, s=1.4) + '}')
    ab.append(f'summon minecraft:text_display {cx} 67.2 {cz} {{Tags:["mg.arm"],billboard:"center",background:0,text:[{{"text":"{name}","color":"{col}","bold":true}}],'
              + TF.format(ty=0, s=1.0) + '}')
wr('lobby/armory_build', ab)
at = ['# Spawn (chaque tick après le setup) : socles de l\'armurerie, armes, portail des plots, animation du décor']
for i, (px, pz, c) in enumerate(PADS, 1):
    at.append(f'execute as @a[tag=!mg.play,x={px},y=63,z={pz},dx=2.99,dy=2.5,dz=2.99] run function mg:lobby/pad_{i}')
at += ['', '# Recharge de la baguette et du railgun', 'scoreboard players remove @a[scores={mg.wd=1..}] mg.wd 1', 'scoreboard players remove @a[scores={mg.lcd=1..}] mg.lcd 1', '',
       '# Utilisation (seulement dans le lobby, hors partie)',
       'execute if score $state mg.st matches 0 as @a[scores={mg.qs=1..},tag=!mg.surv] at @s run function mg:lobby/laser',
       'execute if score $state mg.st matches 0 as @a[scores={mg.fw=1..},tag=!mg.surv] at @s run function mg:lobby/wand',
       'execute as @a[scores={mg.wc=1..},tag=!mg.surv] run function mg:lobby/wind_used',
       'execute if score $state mg.st matches 0 as @e[type=minecraft:snowball,tag=mg.sn] at @s run function mg:lobby/snow_tick',
       'execute if score $state mg.st matches 0 as @a[scores={mg.us=1..},tag=!mg.surv] at @s run function mg:lobby/snow_thrown',
       'execute unless score $state mg.st matches 0 run scoreboard players reset @a mg.fw', '',
       '# Portail des plots : le traverser envoie sur son plot (une fois par passage)',
       'execute as @a[tag=mg.lpz] unless entity @s[x=-4,y=64,z=-48,dx=8,dy=3,dz=1] run tag @s remove mg.lpz',
       'execute as @a[tag=!mg.lpz,tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,gamemode=adventure,x=-4,y=64,z=-48,dx=8,dy=3,dz=1] run function mg:lobby/portal',
       '', '# Décor : animation toutes les 2 s, particules toutes les 0,5 s',
       'scoreboard players add $lan mg.t 1',
       'execute if score $lan mg.t matches 40.. run function mg:lobby/anim',
       'execute if score $lan mg.t matches 40.. run scoreboard players set $lan mg.t 0',
       'scoreboard players operation $lfx mg.t = $lan mg.t', 'scoreboard players set $l10 mg.t 10', 'scoreboard players operation $lfx mg.t %= $l10 mg.t',
       'execute if score $lfx mg.t matches 0 if entity @a[x=0,y=64,z=0,distance=..160] run function mg:lobby/fx']
wr('lobby/armory_tick', at)
wr('lobby/portal', ['# @s traverse le portail des plots : direction son plot',
                    'tag @s add mg.lpz',
                    'execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.2 1.8',
                    'execute at @s run particle minecraft:reverse_portal ~ ~1 ~ 0.4 0.8 0.4 0.05 40',
                    'function mg:plot/enter'])
GIVE_SLOT = {1: 'hotbar.0', 3: 'hotbar.2', 4: 'hotbar.3'}
for i, slot in GIVE_SLOT.items():
    p = os.path.join(F, 'lobby', f'pad_{i}_give.mcfunction')
    s = open(p, encoding='utf-8').read().rstrip('\n').split('\n')
    s = [l for l in s if 'item_model' not in l]
    s.append(f'execute if score $rp mg.st matches 1 run item modify entity @s {slot} {{"function":"minecraft:set_components","components":{{"minecraft:item_model":"mg:{PADM[i - 1][1]}"}}}}')
    wr(f'lobby/pad_{i}_give', s)
p = os.path.join(F, 'lobby', 'give_wand.mcfunction')
s = [l for l in open(p, encoding='utf-8').read().rstrip('\n').split('\n') if 'item_model' not in l]
s.insert(2, 'execute if score $rp mg.st matches 1 run item modify entity @s hotbar.1 {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:magic_wand"}}')
wr('lobby/give_wand', s)
wr('lobby/laser_hit', ['# Impact du laser sur un bloc (@s = tireur) : cibles du stand de tir',
                       'execute if block ~ ~ ~ minecraft:target run return run function mg:lobby/laser_bull',
                       'execute if block ~ ~ ~ #minecraft:wool run function mg:lobby/laser_ring',
                       'particle minecraft:electric_spark ~ ~ ~ 0.2 0.2 0.2 0.4 18',
                       'particle minecraft:end_rod ~ ~ ~ 0.15 0.15 0.15 0.08 10',
                       'particle minecraft:dust{color:[1.0,0.2,0.2],scale:1.5} ~ ~ ~ 0.15 0.15 0.15 0 10',
                       'particle minecraft:smoke ~ ~ ~ 0.1 0.1 0.1 0.02 6',
                       'playsound minecraft:block.amethyst_block.chime master @a ~ ~ ~ 0.8 1.6'])
wr('lobby/laser_bull', ['# Laser dans le mille (cœur d\'une cible)',
                        'particle minecraft:firework ~ ~ ~ 0.2 0.2 0.2 0.15 30',
                        'particle minecraft:dust{color:[1.0,0.85,0.1],scale:1.4} ~ ~ ~ 0.3 0.3 0.3 0 20',
                        'playsound minecraft:block.note_block.bell master @a ~ ~ ~ 1 1.5',
                        'playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.8 1.2',
                        'title @s actionbar [{"text":"★ DANS LE MILLE ! ★","color":"gold","bold":true}]'])
wr('lobby/laser_ring', ['# Laser sur les anneaux d\'une cible',
                        'particle minecraft:crit ~ ~ ~ 0.2 0.2 0.2 0.1 12',
                        'playsound minecraft:block.note_block.pling master @a ~ ~ ~ 0.8 1.1',
                        'title @s actionbar [{"text":"◎ Cible touchée, vise le centre !","color":"yellow"}]'])

# ------------------------------------------------------------------ parkour : blocs, marqueurs, chutes
def yaw_to(a, b): return round(math.degrees(math.atan2(-(b[0] - a[0]), b[2] - a[2])), 1)
seq = [(67.5, 63, 0.5)] + [(x + 0.5, y, z + 0.5) for (x, z, y, b) in S1]
pb = ['# Parkour du spawn (généré par tools/lobby/gen_lobby.py) : jardin suspendu puis la Tour céleste en spirale',
      'kill @e[type=minecraft:marker,tag=mg.pkm]', 'kill @e[type=minecraft:text_display,tag=mg.pkd]']
pkc = {}
for (x, y, z, b) in PK: pkc[(x, y, z)] = b
pb += merge({k: v for k, v in pkc.items() if not is_conn(v)}, ' strict') + merge({k: v for k, v in pkc.items() if is_conn(v)}, '')
for (x, y, z, b) in [(x, y, z, b) for (x, y, z), b in W.items() if x >= 112 and b in ('beacon', 'lime_stained_glass', 'iron_block')]:
    pb.append(f'setblock {x} {y} {z} minecraft:{b}')
nexts = {0: (71.5, 0.5), 1: (106.5, 1.5)}
for (sx, sy, sz, i) in spiral:
    if i in (14, 28):
        nx = spiral[i + 1]; nexts[2 if i == 14 else 3] = (nx[0] + 0.5, nx[2] + 0.5)
for (pos, n, by) in CPS:
    tags = '"mg.pkc","mg.pks","mg.pkm","mg.pkn"' if n == 0 else '"mg.pkc","mg.pkm","mg.pkn"'
    nx = nexts[n]
    pb.append(f'summon minecraft:marker {pos[0]} {pos[1]} {pos[2]} {{Tags:[{tags}],Rotation:[{yaw_to((pos[0], 0, pos[2]), (nx[0], 0, nx[1]))}f,0f]}}')
    pb.append(f'scoreboard players set @e[type=minecraft:marker,tag=mg.pkn,limit=1] mg.t {n}')
    pb.append('tag @e[type=minecraft:marker,tag=mg.pkn] remove mg.pkn')
pb.append(f'summon minecraft:marker {FIN[0]} {FIN[1]} {FIN[2]} {{Tags:["mg.pkf","mg.pkm","mg.pkn"]}}')
pb.append('scoreboard players set @e[type=minecraft:marker,tag=mg.pkn,limit=1] mg.t 4')
pb.append('tag @e[type=minecraft:marker,tag=mg.pkn] remove mg.pkn')
pb.append('summon minecraft:text_display 67.5 66.9 0.5 {Tags:["mg.pkd","mg.pkboard"],billboard:"center",text:[{"text":"3 checkpoints : grimpe au sommet de la Tour céleste !","color":"gray"}],'
          + TF.format(ty=0, s=1) + '}')
pb.append('summon minecraft:text_display 67.5 67.4 0.5 {Tags:["mg.pkd"],billboard:"center",text:[{"text":"Pose-toi sur l\'émeraude pour démarrer le chrono","color":"green"}],'
          + TF.format(ty=0, s=0.9) + '}')
for (pos, n, by) in CPS[1:]:
    pb.append(f'summon minecraft:text_display {pos[0]} {pos[1] + 1.6} {pos[2]} {{Tags:["mg.pkd"],billboard:"center",text:[{{"text":"✔ Checkpoint {n}/3","color":"aqua","bold":true}}],'
              + TF.format(ty=0, s=1.2) + '}')
pb.append('execute if score $pkrec mg.st matches 1.. run function mg:parkour/board_refresh')
wr('parkour/build', pb)
wr('parkour/board_refresh', ['# Réaffiche le record du parkour sur le panneau (après reconstruction)',
                             'scoreboard players set $pk20 mg.st 20', 'scoreboard players set $pk2 mg.st 2',
                             'scoreboard players operation $s mg.st = $pkrec mg.st', 'scoreboard players operation $s mg.st /= $pk20 mg.st',
                             'scoreboard players operation $d mg.st = $pkrec mg.st', 'scoreboard players operation $d mg.st %= $pk20 mg.st',
                             'scoreboard players operation $d mg.st /= $pk2 mg.st',
                             'execute store result storage mg:pk s int 1 run scoreboard players get $s mg.st',
                             'execute store result storage mg:pk d int 1 run scoreboard players get $d mg.st',
                             'function mg:parkour/board with storage mg:pk'])
segmin = {}
allpts = [(63, 0)] + [(y, 0) for (x, z, y, b) in S1] + [(67, 1), (67, 1), (68, 1)]
for (x, y, z, i) in spiral: allpts.append((y, 1 if i < 14 else (2 if i < 28 else 3)))
allpts.append((FINY, 3))
for (y, sgm) in allpts: segmin[sgm] = min(segmin.get(sgm, 999), y)
fc = ['# Chute : en dessous du point le plus bas du tronçon → retour au dernier checkpoint (@s = coureur) (généré)']
for sgm in range(4):
    fc.append(f'execute if score @s mg.ppc matches {sgm} at @s if entity @s[y={segmin[sgm] - 3 - 2048},dy=2048] run return run function mg:parkour/fall')
wr('parkour/fall_check', fc)
wr('parkour/fall', ['# Chute (@s = coureur) : retour au dernier checkpoint, tourné vers le saut suivant',
                    'scoreboard players add @s mg.ppf 1', 'scoreboard players operation $ck mg.st = @s mg.ppc', 'tag @s add mg.pkx',
                    'execute as @e[type=minecraft:marker,tag=mg.pkc] if score @s mg.t = $ck mg.st at @s run tp @a[tag=mg.pkx,limit=1] ~ ~ ~ ~ 0',
                    'tag @s remove mg.pkx',
                    'title @s actionbar [{"text":"↺ Retour au checkpoint","color":"yellow"}]',
                    'execute at @s run playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 0.6 1.2',
                    'function mg:core/fall_heal'])
print('parkour : fin y', FINY, '| seuils', {k: v - 3 for k, v in segmin.items()}, '| sauts', len(path))

# ------------------------------------------------------------------ CIRCUIT DU SPAWN : tables du moteur (kart/t4) et mode kart libre (lobkart/)
KY = G + 1
wr('kart/t4/cp_check', [f'# Circuit du spawn : point de passage attendu (mg.kcp) atteint ? ({KK} points par tour) (généré par tools/lobby/gen_lobby.py)'] +
   [f'execute if score @s mg.kcp matches {k} positioned {x} {KY} {z} if entity @e[type=minecraft:block_display,tag=mg.kk,distance=..9] run return run function mg:kart/cp_pass'
    for k, (x, z, yw) in enumerate(KCPS)])
wr('kart/t4/cp_tp', ['# Circuit du spawn : remise en piste (@s = kart) au point de passage $ki'] +
   [f'execute if score $ki mg.st matches {k} run return run tp @s {x} {KY} {z} {yw} 0' for k, (x, z, yw) in enumerate(KCPS)])
wr('kart/t4/bill_step', ['# Circuit du spawn : Bill Balle (@s = kart) vers le point de passage $ki'] +
   [f'execute if score $ki mg.st matches {k} facing {x} {KY} {z} rotated ~ 0 run return run tp @s ^ ^ ^1.6 ~ ~' for k, (x, z, yw) in enumerate(KCPS)])
wr('kart/t4/const', ['# Circuit du spawn : constantes', f'scoreboard players set $kK mg.st {KK}', 'scoreboard players set $kLaps mg.st 999'])
grid = ['# Place @s (le pilote) sur une des 6 places de départ ($lgi 0..5), tourné vers la piste']
for g in range(6):
    back, side = 3 + (g // 2) * 4, (-2 if g % 2 == 0 else 2)
    i = (-back * 2) % KN; tx, tz = ktan(i)
    x, z = KP[i][0] + -tz * side, KP[i][1] + tx * side
    grid.append(f'execute if score $lgi mg.st matches {g} run return run tp @s {round(x, 1)} {KY} {round(z, 1)} {kyaw(tx, tz)} 0')
wr('lobkart/grid_tp', grid)
LKC = ['scoreboard players set #km1 mg.st -1'] + [f'scoreboard players set #k{v} mg.st {v}' for v in (2, 3, 4, 5, 8, 10, 12, 20, 60, 65, 100, 120, 1000)] + \
      ['scoreboard players set #kt85 mg.st 85', 'scoreboard players set #kt120 mg.st 120', 'scoreboard players set #kt90 mg.st 90', 'scoreboard players set #kkmh mg.st 108']
wr('lobkart/consts', ['# Constantes du moteur du kart (les mêmes qu\'en course)'] + LKC)
RESET = ['ksp', 'kdr', 'krc', 'kbo', 'khi', 'kst', 'kit', 'kic', 'kgd', 'kbill', 'kboo', 'kmg', 'kcp', 'klp', 'kvy', 'kfp', 'kps', 'kbl', 'krl', 'klt']
BTN = ('tellraw @s [{"text":"🏎 ","color":"gold"},{"text":"Circuit du spawn : ","color":"gray"},'
       '{"text":"[Descendre]","color":"red","bold":true,"click_event":{"action":"run_command","command":"trigger mg.opt set 27"},"hover_event":{"action":"show_text","value":"Ranger le kart et revenir au garage (/trigger mg.opt set 27)"}},'
       '{"text":" ","color":"gray"},{"text":"[Vue assise]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.kv set 2"}},'
       '{"text":" ","color":"gray"},{"text":"[Caméra de poursuite]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.kv set 1"}},'
       '{"text":" ","color":"gray"},{"text":"[⛑ Je suis coincé]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.opt set 26"},"hover_event":{"action":"show_text","value":"Te remet sur la piste au dernier point de passage (ou /trigger mg.opt set 26)"}},'
       '{"text":"  (Shift = descendre ; on peut rouler sur tout le spawn)","color":"dark_gray"}]')
wr('lobkart/enter', ['# @s marche sur le tapis du garage : il monte dans un kart sur la ligne de départ du circuit du spawn',
                     'tag @s add mg.lkz',
                     'execute unless score $state mg.st matches 0 run return run tellraw @s [{"text":"⚠ Le kart libre n\'est pas disponible pendant une partie.","color":"red"}]',
                     'execute store result score $lkn mg.st if entity @a[tag=mg.lk]',
                     'execute if score $lkn mg.st matches 12.. run return run tellraw @s [{"text":"⚠ Trop de karts sur le circuit, réessaie dans un instant.","color":"red"}]',
                     'function mg:parkour/quit', 'clear @s', 'effect clear @s', 'function mg:lobkart/consts',
                     'tag @s remove mg.kfin', 'tag @s remove mg.kout', 'tag @s remove mg.kok',
                     'scoreboard players add $lri mg.st 1', 'execute unless score $lri mg.st matches 100..999 run scoreboard players set $lri mg.st 100',
                     'scoreboard players operation @s mg.ri = $lri mg.st'] +
   [f'scoreboard players set @s mg.{k} 0' for k in RESET] +
   ['execute unless score @s mg.kvm matches 0..1 run scoreboard players set @s mg.kvm 1', 'scoreboard players reset @s mg.qs', 'scoreboard players enable @s mg.kv',
    'scoreboard players add $lgi mg.st 1', 'execute unless score $lgi mg.st matches 0..5 run scoreboard players set $lgi mg.st 0',
    'function mg:lobkart/grid_tp', 'tag @s add mg.lk',
    'execute at @s run function mg:kart/kart_new', 'function mg:kart/kk', 'tag @e[tag=mg.kk] add mg.lkart', 'function mg:kart/seat',
    'tag @e[tag=mg.kk] remove mg.kk', 'tag @e[tag=mg.kcamc] remove mg.kcamc',
    'title @s title [{"text":"🏁 CIRCUIT DU SPAWN","color":"gold","bold":true}]',
    'title @s subtitle [{"text":"Z avancer, Q / D tourner, Espace = dérapage, Shift = descendre","color":"yellow"}]',
    'execute at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 1 1.4', BTN])
wr('lobkart/remove', ['# Range le kart de @s (et sa caméra, sa tête) sans le déplacer',
                      'function mg:kart/kk', 'ride @s dismount',
                      'execute as @e[type=minecraft:block_display,tag=mg.kk] on passengers unless entity @s[type=minecraft:player] run kill @s',
                      'kill @e[tag=mg.kk]', 'kill @e[tag=mg.kcamc]',
                      'execute as @e[type=minecraft:item_display,tag=mg.khead] if score @s mg.ri = $me mg.st run kill @s',
                      'tag @s remove mg.lk', 'tag @s remove mg.kfin', 'tag @s remove mg.kout', 'scoreboard players set @s mg.ri 0',
                      'execute if entity @s[gamemode=spectator] run gamemode adventure @s'])
wr('lobkart/leave', ['# @s quitte le circuit du spawn sans être ramené au garage (plot, survie, reconnexion)', 'execute if entity @s[tag=mg.lk] run function mg:lobkart/remove'])
wr('lobkart/exit', ['# @s descend du kart : retour au garage',
                    'execute unless entity @s[tag=mg.lk] run return 0',
                    'function mg:lobkart/remove', 'tag @s add mg.lkz',
                    f'tp @s 0.5 64 {KPAD[1] - 2.5} 180 0', 'function mg:core/give_menu',
                    'title @s actionbar [{"text":"🏎 Kart rangé. À bientôt sur le circuit !","color":"gold"}]'])
wr('lobkart/stop_all', ['# Une partie commence : karts du spawn rangés (participant déjà sorti par core/request, filet de sécurité : sur place ; les autres : au garage)',
                        'execute as @a[tag=mg.lk,tag=mg.play] run function mg:lobkart/leave', 'execute as @a[tag=mg.lk] run function mg:lobkart/exit'])
wr('lobkart/claim', ['# @s (pilote du spawn) garde son kart et sa caméra (pas orphelins)', 'function mg:kart/kk', 'tag @e[tag=mg.kk] remove mg.lko', 'tag @e[tag=mg.kcamc] remove mg.lko',
                     'tag @e[tag=mg.kk] remove mg.kk', 'tag @e[tag=mg.kcamc] remove mg.kcamc'])
wr('lobkart/orphans', ['# Karts du spawn dont le pilote est parti (déconnexion) : rangés',
                       'tag @e[type=minecraft:block_display,tag=mg.lkart] add mg.lko',
                       'execute as @e[type=minecraft:item_display,tag=mg.kcam] if score @s mg.ri matches 100.. run tag @s add mg.lko',
                       'execute as @a[tag=mg.lk] run function mg:lobkart/claim',
                       'execute as @e[type=minecraft:block_display,tag=mg.lko] on passengers run kill @s',
                       'kill @e[tag=mg.lko]'])
wr('lobkart/tick', ['# Kart libre au spawn (chaque tick) : moteur du kart pour les pilotes mg.lk, sur le circuit du spawn',
                    f'execute as @a[tag=mg.lkz] unless entity @s[x={KPAD[0]},y=63,z={KPAD[1]},dx=2.99,dy=2.5,dz=2.99] run tag @s remove mg.lkz',
                    f'execute if score $state mg.st matches 0 as @a[tag=!mg.lk,tag=!mg.lkz,tag=!mg.play,tag=!mg.surv,tag=!mg.inplot,gamemode=adventure,x={KPAD[0]},y=63,z={KPAD[1]},dx=2.99,dy=2.5,dz=2.99] run function mg:lobkart/enter',
                    'scoreboard players add $lko mg.st 1',
                    'execute if score $lko mg.st matches 100.. run function mg:lobkart/orphans',
                    'execute if score $lko mg.st matches 100.. run scoreboard players set $lko mg.st 0',
                    'execute unless entity @a[tag=mg.lk] run return 0',
                    'execute unless score $state mg.st matches 0 run return run function mg:lobkart/stop_all',
                    'execute as @a[tag=mg.lk,gamemode=creative] run function mg:lobkart/leave',
                    'execute as @a[tag=mg.lk] if predicate mg:sneak run function mg:lobkart/exit',
                    'execute as @a[tag=mg.lk,tag=mg.surv] run function mg:lobkart/leave',
                    'scoreboard players operation $lkb mg.st = $kbat mg.st', 'scoreboard players set $kbat mg.st 0',
                    'scoreboard players set $klob mg.st 1', 'function mg:kart/t4/const',
                    'execute if score $rp mg.st matches 1 as @e[type=minecraft:block_display,tag=mg.lkart,tag=!mg.rps] at @s run function mg:kart/rp_skin',
                    'execute if score $rp mg.st matches 1 as @e[tag=mg.fx,tag=!mg.rps] at @s run function mg:kart/rp_skin',
                    'scoreboard players add @a[tag=mg.lk,scores={mg.klp=1..}] mg.klt 1',
                    'execute as @a[tag=mg.lk] run function mg:kart/drive',
                    'tag @e[tag=mg.kk] remove mg.kk', 'tag @e[tag=mg.kcamc] remove mg.kcamc',
                    'execute as @e[type=minecraft:block_display,tag=mg.kart,tag=!mg.lkart] if score @s mg.ri matches 100.. run tag @s add mg.lkart',
                    'scoreboard players add $kph mg.st 1', 'execute if score $kph mg.st matches 4.. run scoreboard players set $kph mg.st 0',
                    'execute if score $kph mg.st matches 0 as @a[tag=mg.lk] run function mg:lobkart/hud',
                    'scoreboard players set $klob mg.st 0', 'scoreboard players operation $kbat mg.st = $lkb mg.st', 'function mg:kart/const'])
def tsd(score):   # secondes.dixièmes d'un score en ticks → $s, $d
    return [f'scoreboard players operation $s mg.st = {score}', 'scoreboard players operation $s mg.st /= #k20 mg.st',
            f'scoreboard players operation $d mg.st = {score}', 'scoreboard players operation $d mg.st %= #k20 mg.st', 'scoreboard players operation $d mg.st /= #k2 mg.st']
wr('lobkart/hud', ['# Barre du bas du pilote du spawn (@s) : tour, chrono, meilleur tour, vitesse',
                   'scoreboard players operation $kmh mg.st = @s mg.ksp', 'scoreboard players operation $kmh mg.st *= #kkmh mg.st', 'scoreboard players operation $kmh mg.st /= #k100 mg.st',
                   'execute if score $kmh mg.st matches ..-1 run scoreboard players operation $kmh mg.st *= #km1 mg.st',
                   'execute if score @s mg.klp matches 0 run return run title @s actionbar [{"text":"🏁 Passe la ligne de départ pour lancer le chrono  ","color":"gold"},{"score":{"name":"$kmh","objective":"mg.st"},"color":"aqua"},{"text":" km/h","color":"dark_aqua"}]']
   + tsd('@s mg.klt') + ['scoreboard players operation $bs mg.st = @s mg.klb', 'scoreboard players operation $bs mg.st /= #k20 mg.st',
                         'scoreboard players operation $bd mg.st = @s mg.klb', 'scoreboard players operation $bd mg.st %= #k20 mg.st', 'scoreboard players operation $bd mg.st /= #k2 mg.st',
                         'execute unless score @s mg.klb matches 1.. run title @s actionbar [{"text":"🏁 Tour ","color":"gold"},{"score":{"name":"@s","objective":"mg.klp"},"color":"yellow","bold":true},{"text":"   ⏱ ","color":"gold"},{"score":{"name":"$s","objective":"mg.st"},"color":"white","bold":true},{"text":".","color":"white"},{"score":{"name":"$d","objective":"mg.st"},"color":"white"},{"text":" s   ","color":"gray"},{"score":{"name":"$kmh","objective":"mg.st"},"color":"aqua"},{"text":" km/h","color":"dark_aqua"}]',
                         'execute if score @s mg.klb matches 1.. run title @s actionbar [{"text":"🏁 Tour ","color":"gold"},{"score":{"name":"@s","objective":"mg.klp"},"color":"yellow","bold":true},{"text":"   ⏱ ","color":"gold"},{"score":{"name":"$s","objective":"mg.st"},"color":"white","bold":true},{"text":".","color":"white"},{"score":{"name":"$d","objective":"mg.st"},"color":"white"},{"text":" s   ★ ","color":"gold"},{"score":{"name":"$bs","objective":"mg.st"},"color":"yellow"},{"text":".","color":"yellow"},{"score":{"name":"$bd","objective":"mg.st"},"color":"yellow"},{"text":" s   ","color":"gray"},{"score":{"name":"$kmh","objective":"mg.st"},"color":"aqua"},{"text":" km/h","color":"dark_aqua"}]'])
wr('lobkart/lap', ['# Ligne d\'arrivée franchie par un pilote du spawn (@s) : tour chronométré, record perso et record du circuit',
                   'scoreboard players add @s mg.klp 1',
                   'execute if score @s mg.klp matches 1 run scoreboard players set @s mg.klt 0',
                   'execute if score @s mg.klp matches 1 run return run title @s actionbar [{"text":"🏁 C\'est parti, le chrono tourne !","color":"green","bold":true}]']
   + tsd('@s mg.klt') +
   ['tellraw @s [{"text":"🏁 Tour en ","color":"gold"},{"score":{"name":"$s","objective":"mg.st"},"color":"white","bold":true},{"text":".","color":"white"},{"score":{"name":"$d","objective":"mg.st"},"color":"white"},{"text":" s","color":"gold"}]',
    'execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.2',
    'execute if score @s mg.klb matches 1.. if score @s mg.klt < @s mg.klb run tellraw @s [{"text":"★ Nouveau record perso !","color":"aqua","bold":true}]',
    'execute unless score @s mg.klb matches 1.. run scoreboard players operation @s mg.klb = @s mg.klt',
    'execute if score @s mg.klt < @s mg.klb run scoreboard players operation @s mg.klb = @s mg.klt',
    'execute unless score $klrec mg.st matches 1.. run function mg:lobkart/record',
    'execute if score $klrec mg.st matches 1.. if score @s mg.klt < $klrec mg.st run function mg:lobkart/record',
    'scoreboard players set @s mg.klt 0'])
wr('lobkart/record', ['# Nouveau record du circuit du spawn (@s ; $s / $d déjà calculés)',
                      'scoreboard players operation $klrec mg.st = @s mg.klt',
                      'tellraw @a[tag=!mg.surv] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" bat le record du circuit du spawn : ","color":"gray"},{"score":{"name":"$s","objective":"mg.st"},"color":"gold","bold":true},{"text":".","color":"gold"},{"score":{"name":"$d","objective":"mg.st"},"color":"gold"},{"text":" s !","color":"gold"}]',
                      'execute store result storage mg:lk s int 1 run scoreboard players get $s mg.st', 'execute store result storage mg:lk d int 1 run scoreboard players get $d mg.st',
                      'function mg:lobkart/board with storage mg:lk'])
wr('lobkart/board', ['# Panneau du record (macro $(s), $(d))', '$data modify entity @e[type=minecraft:text_display,tag=mg.lkboard,limit=1] text set value {text:"🏆 Record du tour : $(s).$(d) s",color:"gold"}'])
wr('lobkart/board_refresh', ['# Réaffiche le record sur le panneau (après reconstruction du décor)', 'function mg:lobkart/consts'] + tsd('$klrec mg.st') +
   ['execute store result storage mg:lk s int 1 run scoreboard players get $s mg.st', 'execute store result storage mg:lk d int 1 run scoreboard players get $d mg.st',
    'function mg:lobkart/board with storage mg:lk'])
KDECO = [tdisp(KPAD[0] + 1.5, 66.6, KPAD[1] + 1.5, '[{"text":"🏎 KART LIBRE","color":"gold","bold":true}]', 1.6),
         tdisp(KPAD[0] + 1.5, 66.1, KPAD[1] + 1.5, '[{"text":"Marche sur le tapis pour monter dans un kart","color":"gray"}]', 0.9),
         tdisp(round(sx_, 1) + 0.5, 74.5, round(sz_, 1) + 0.5, '[{"text":"🏁 CIRCUIT DU SPAWN","color":"gold","bold":true}]', 2.4),
         tdisp(round(sx_, 1) + 0.5, 73.8, round(sz_, 1) + 0.5, '[{"text":"🏆 Record du tour : aucun","color":"gold"}]', 1.4).replace('Tags:["mg.lby"', 'Tags:["mg.lby","mg.lkboard"')]
with open(os.path.join(F, 'lobby', 'deco_common.mcfunction'), 'a', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(['# Circuit du spawn : panneaux'] + KDECO + ['execute if score $klrec mg.st matches 1.. run function mg:lobkart/board_refresh']) + '\n')

# ------------------------------------------------------------------ SECRETS : succès cachés (onglet « Secrets du spawn ») et leur détection
import json
ADV = os.path.join(R, 'data', 'mg', 'advancement', 'secrets')
os.makedirs(ADV, exist_ok=True)
for f in os.listdir(ADV): os.remove(os.path.join(ADV, f))
SECRETS = [  # id, titre, indice, icône, cadre
    ('terrier', 'Le terrier', 'Certaines trappes mènent plus loin qu\'on ne croit', 'spruce_trapdoor', 'task'),
    ('tuyau', 'Tuyau de distorsion', 'Accroupi, on voyage plus vite', 'green_concrete', 'task'),
    ('couronne', 'Roi du château', 'Personne ne regarde jamais les toits', 'golden_helmet', 'task'),
    ('etoiles', 'La tête dans les étoiles', 'Au cœur doré, lève les yeux', 'nether_star', 'task'),
    ('ile', 'Île céleste', 'Le ciel n\'est pas réservé aux oiseaux', 'grass_block', 'challenge'),
    ('plongeon', 'Petit plongeon', 'Les poissons aussi aiment la visite', 'tropical_fish_bucket', 'task'),
    ('vide', 'Ouf !', 'Le vide ne veut pas de toi', 'feather', 'task'),
    ('arsenal', 'Arsenal complet', 'Un de chaque, pas moins', 'blaze_rod', 'task'),
    ('mille', 'Dans le mille', 'Vise le cœur', 'target', 'task'),
    ('lynx', 'Œil de lynx', 'Vingt fois en plein cœur', 'spyglass', 'challenge'),
    ('sommet', 'Au sommet', 'Tout en haut, la lumière verte', 'diamond', 'task'),
    ('ecureuil', 'Écureuil volant', 'Tout en haut en moins d\'une minute', 'elytra', 'challenge'),
    ('pilote', 'Pilote du dimanche', 'Un tour, rien qu\'un', 'minecart', 'task'),
    ('volant', 'Fou du volant', 'Un tour en moins de 40 secondes', 'blaze_powder', 'challenge'),
    ('danse', 'Danse de la victoire', 'Sur la place, montre tes plus beaux pas', 'jukebox', 'task'),
    ('bouton', 'Appuie, pour voir', 'Un bouton discret, près des champions', 'polished_blackstone_button', 'task'),
    ('visite', 'Visite guidée', 'Cinq lieux à voir absolument', 'filled_map', 'task'),
]
def adv(name, d):
    with open(os.path.join(ADV, name + '.json'), 'w', encoding='utf-8', newline='\n') as f: json.dump(d, f, indent=2, ensure_ascii=False); f.write('\n')
adv('root', {'criteria': {'tick': {'trigger': 'minecraft:tick'}},
             'display': {'icon': {'id': 'minecraft:ender_eye'}, 'title': {'text': 'Secrets du spawn', 'color': 'gold'},
                         'description': {'text': f'Le spawn cache {len(SECRETS)} secrets... ouvre l\'œil !', 'color': 'gray'},
                         'background': 'minecraft:block/amethyst_block', 'show_toast': False, 'announce_to_chat': False}})
for sid, title, hint, icon, frame in SECRETS:
    adv(sid, {'parent': 'mg:secrets/root', 'criteria': {'found': {'trigger': 'minecraft:impossible'}},
              'display': {'icon': {'id': f'minecraft:{icon}'}, 'title': {'text': title}, 'description': {'text': hint, 'color': 'gray'}, 'frame': frame,
                          'show_toast': True, 'announce_to_chat': False, 'hidden': True},
              'rewards': {'function': f'mg:secrets/found/{sid}'}})
adv('maitre', {'parent': 'mg:secrets/visite', 'criteria': {'found': {'trigger': 'minecraft:impossible'}},
               'display': {'icon': {'id': 'minecraft:dragon_egg'}, 'title': {'text': 'Maître des secrets', 'color': 'light_purple'},
                           'description': {'text': 'Tous les secrets du spawn', 'color': 'gray'}, 'frame': 'challenge',
                           'show_toast': True, 'announce_to_chat': False, 'hidden': True},
               'rewards': {'function': 'mg:secrets/found/maitre'}})
def G_(sid): return f'advancement grant @s only mg:secrets/{sid}'
def NOT(sid): return f'unless entity @s[advancements={{mg:secrets/{sid}=true}}]'
ALL = ','.join(f'mg:secrets/{s[0]}=true' for s in SECRETS)
import shutil
shutil.rmtree(os.path.join(F, 'secrets', 'found'), ignore_errors=True)
for sid, title, hint, icon, frame in SECRETS + [('maitre', 'Maître des secrets', '', '', 'challenge')]:
    col = 'light_purple' if frame == 'challenge' else 'green'
    wr(f'secrets/found/{sid}', [f'# Secret « {title} » trouvé par @s : annonce à tout le monde',
                               'function mg:secrets/count',
                               'tellraw @a [{"text":"🕵 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" a trouvé un secret du spawn : ","color":"gray"},'
                               f'{{"text":"[{title}]","color":"{col}","bold":true}},{{"text":" (","color":"gray"}},{{"score":{{"name":"$secn","objective":"mg.st"}},"color":"gold"}},'
                               f'{{"text":"/{len(SECRETS) + 1})","color":"gray"}}]',
                               'execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 0.6 1.6',
                               'function mg:secrets/reward'])
wr('secrets/count', ['# Nombre de secrets trouvés par @s → $secn'] + ['scoreboard players set $secn mg.st 0'] +
   [f'execute if entity @s[advancements={{mg:secrets/{x[0]}=true}}] run scoreboard players add $secn mg.st 1' for x in SECRETS + [('maitre',)]])
wr('secrets/reward', ['# Un secret trouvé (@s) : petite fête, et le grand final quand tout est trouvé',
                      'execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.3',
                      'execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.5 0.8 0.5 0.4 40',
                      f'execute if entity @s[advancements={{{ALL}}}] unless entity @s[advancements={{mg:secrets/maitre=true}}] run advancement grant @s only mg:secrets/maitre'])
ISL_SPOTS = [(31, 90, -31, 5), (-34, 94, 31, 5), (-31, 98, -35, 4), (37, 96, 31, 4), (-6, 104, 30, 3)]
chk = ['# Secrets du spawn : vérifications (toutes les 0,5 s, @s = joueur du spawn, à sa position)',
       f'execute {NOT("terrier")} if entity @s[x={rx1},y={ry1},z={rz1},dx={rx2 - rx1},dy={ry2 - ry1},dz={rz2 - rz1}] run {G_("terrier")}',
       f'execute {NOT("couronne")} if entity @s[x={X1 - 1},y=84,z=-0.3,dx={X2 - X1 + 2},dy=2,dz=0.6] run {G_("couronne")}',
       f'execute {NOT("plongeon")} if entity @s[x={POND[0] - 3},y=61.5,z={POND[1] - 3},dx=6,dy=1,dz=6] if block ~ ~ ~ minecraft:water run {G_("plongeon")}',
       f'execute {NOT("arsenal")} if items entity @s container.* minecraft:warped_fungus_on_a_stick if items entity @s container.* minecraft:blaze_rod '
       f'if items entity @s container.* minecraft:wind_charge if items entity @s container.* minecraft:snowball run {G_("arsenal")}']
for (cx, cy, cz, r) in ISL_SPOTS:
    chk.append(f'execute {NOT("ile")} if entity @s[x={cx - r},y={cy + 0.5},z={cz - r},dx={2 * r},dy=3,dz={2 * r}] run {G_("ile")}')
chk += [f'execute if entity @s[x=-1,y=64,z=-1,dx=2,dy=1,dz=2,x_rotation=-90..-75] run scoreboard players add @s mg.eup 10',
        f'execute unless entity @s[x=-1,y=64,z=-1,dx=2,dy=1,dz=2,x_rotation=-90..-75] run scoreboard players set @s mg.eup 0',
        f'execute {NOT("etoiles")} if score @s mg.eup matches 60.. run {G_("etoiles")}',
        'tag @s[x=-56,y=64,z=-10,dx=20,dy=6,dz=20] add mg.ev1', 'tag @s[x=64,y=63,z=-4,dx=6,dy=4,dz=8] add mg.ev2', 'tag @s[x=-6,y=63,z=-53,dx=12,dy=6,dz=12] add mg.ev3',
        'tag @s[x=-5,y=63,z=43,dx=10,dy=4,dz=10] add mg.ev4', f'tag @s[x=-4,y=63,z={round(sz_) - 4},dx=8,dy=5,dz=8] add mg.ev5',
        f'execute {NOT("visite")} if entity @s[tag=mg.ev1,tag=mg.ev2,tag=mg.ev3,tag=mg.ev4,tag=mg.ev5] run {G_("visite")}',
        'scoreboard players remove @s[scores={mg.ept=1..}] mg.ept 10']
for (a, b) in ((PIPES[0], PIPES[3]), (PIPES[1], PIPES[2])):
    for (p, q) in ((a, b), (b, a)):
        chk.append(f'execute unless score @s mg.ept matches 1.. if predicate mg:sneak positioned {p[0] + 0.5} 68 {p[1] + 0.5} if entity @s[distance=..0.9] run function mg:secrets/pipe {{x:{q[0] + 0.5},z:{q[1] + 0.5}}}')
wr('secrets/check', chk)
wr('secrets/pipe', ['# Tuyau de distorsion : @s file vers l\'autre tuyau (macro x, z)',
                    'execute at @s run particle minecraft:portal ~ ~0.5 ~ 0.3 0.6 0.3 0.6 40',
                    '$tp @s $(x) 68.2 $(z)', 'scoreboard players set @s mg.ept 40',
                    'execute at @s run playsound minecraft:entity.enderman.teleport master @a ~ ~ ~ 0.8 1.6',
                    'execute at @s run playsound minecraft:block.note_block.bit master @s ~ ~ ~ 1 0.6',
                    'execute at @s run particle minecraft:happy_villager ~ ~1 ~ 0.4 0.6 0.4 0 20', G_('tuyau')])
bx, by, bz = SEC_BTN
wr('secrets/tick', ['# Secrets du spawn (toutes les 0,5 s depuis lobby/armory_tick)',
                    'execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.lk,gamemode=!spectator,x=0,y=64,z=0,distance=..140] at @s run function mg:secrets/check',
                    'scoreboard players remove $ebt mg.st 10',
                    f'execute unless score $ebt mg.st matches 1.. if block {bx} {by} {bz} minecraft:polished_blackstone_button[powered=true] run function mg:secrets/button'])
wr('secrets/button', ['# Le bouton secret du garage : feu d\'artifice au-dessus du podium',
                      'scoreboard players set $ebt mg.st 100',
                      f'execute as @a[x={bx + 0.5},y={by},z={bz + 0.5},distance=..5] run {G_("bouton")}',
                      'execute positioned 0.5 80 48.5 run function mg:lobby/boom',
                      'execute positioned -6.5 76 48.5 run function mg:lobby/boom',
                      'execute positioned 7.5 77 48.5 run function mg:lobby/boom'])
wr('secrets/dance', ['# Danse de la victoire (@s sur la place) : 10 accroupissements en 3 s',
                     'execute store result score $sn mg.t if predicate mg:sneak',
                     'execute if score $sn mg.t matches 1 unless score @s mg.esn matches 1 run scoreboard players add @s mg.esc 1',
                     'scoreboard players operation @s mg.esn = $sn mg.t',
                     'scoreboard players add @s mg.est 1',
                     'execute if score @s mg.est matches 60.. run scoreboard players set @s mg.esc 0',
                     'execute if score @s mg.est matches 60.. run scoreboard players set @s mg.est 0',
                     f'execute if score @s mg.esc matches 10.. {NOT("danse")} run {G_("danse")}'])
# crochets dans les fonctions générées ici
for rel, anchor, add in (('lobby/laser_bull', 'title @s actionbar [{"text":"★ DANS LE MILLE ! ★"',
                          ['scoreboard players add @s mg.ebl 1', G_('mille'), 'execute if score @s mg.ebl matches 20.. run ' + G_('lynx')]),
                         ('lobkart/lap', 'execute unless score $klrec mg.st matches 1.. run function mg:lobkart/record',
                          [G_('pilote'), 'execute if score @s mg.klt matches ..799 run ' + G_('volant')])):
    p = os.path.join(F, rel + '.mcfunction')
    s = open(p, encoding='utf-8').read().rstrip('\n').split('\n')
    i = next(k for k, l in enumerate(s) if l.startswith(anchor))
    wr(rel, s[:i] + add + s[i:])
with open(os.path.join(F, 'lobby', 'armory_tick.mcfunction'), 'a', encoding='utf-8', newline='\n') as f:
    f.write('\n# Secrets du spawn\n'
            'execute if score $lfx mg.t matches 0 run function mg:secrets/tick\n'
            'execute as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.lk,x=0,y=64,z=0,distance=..15] run function mg:secrets/dance\n')
with open(os.path.join(F, 'lobby', 'deco_common.mcfunction'), 'a', encoding='utf-8', newline='\n') as f:
    f.write(tdisp((rx1 + rx2) / 2 + 0.5, ry1 + 3.2, rz1 + 1.5, '[{"text":"🕳 Le terrier secret","color":"light_purple","bold":true},{"text":"\\nBravo, peu de gens trouvent cet endroit...","color":"gray"}]', 1.0) + '\n')
print('secrets :', len(SECRETS) + 1)

# ------------------------------------------------------------------ aperçu (vue de dessus)
if len(sys.argv) > 2:
    import struct, zlib
    COL = {'grass': (92, 160, 60), 'water': (50, 110, 220), 'leaves': (60, 130, 50), 'cherry_leaves': (240, 170, 200), 'stone_brick': (130, 130, 130),
           'andesite': (150, 150, 150), 'diorite': (215, 215, 215), 'quartz': (235, 230, 225), 'gold': (250, 210, 60), 'blackstone': (50, 45, 50),
           'deepslate': (80, 80, 88), 'dark_oak': (70, 50, 30), 'spruce': (110, 80, 50), 'concrete': None, 'purpur': (170, 120, 170), 'obsidian': (30, 20, 50),
           'amethyst': (150, 100, 210), 'dirt_path': (160, 130, 80), 'mud': (140, 110, 90), 'mushroom': (200, 40, 40), 'bamboo': (120, 170, 60),
           'birch': (215, 210, 190), 'log': (100, 75, 45), 'lapis': (40, 70, 180), 'emerald': (40, 200, 90), 'ice': (160, 200, 250), 'snow': (245, 250, 255),
           'nether': (130, 40, 40), 'end_stone': (225, 225, 170), 'calcite': (225, 225, 225), 'diamond': (100, 230, 230)}
    CC = {'red': (190, 40, 40), 'white': (235, 235, 235), 'black': (25, 25, 30), 'gray': (80, 80, 85), 'light_gray': (150, 150, 150), 'green': (70, 110, 30),
          'lime': (110, 190, 30), 'yellow': (240, 200, 40), 'cyan': (30, 140, 150)}
    def col(b):
        n = b.split('[')[0]
        if n.endswith('_concrete') or n.endswith('_wool'):
            return CC.get(n.rsplit('_', 1)[0], (150, 150, 150))
        for k, v in COL.items():
            if k in n and v: return v
        h = sum(ord(c) * (i + 1) for i, c in enumerate(n))
        return (90 + h % 120, 90 + (h // 7) % 120, 90 + (h // 49) % 120)
    X0, X1_, Z0, Z1_ = -115, 140, -80, 225
    S = 3
    hm = {}
    for (x, y, z), b in W.items():
        if b.startswith('light') or b == 'air': continue
        if (x, z) not in hm or y > hm[(x, z)][0]: hm[(x, z)] = (y, b)
    w, h = (X1_ - X0 + 1) * S, (Z1_ - Z0 + 1) * S
    img = [[(18, 22, 40)] * w for _ in range(h)]
    for (x, z), (y, b) in hm.items():
        if not (X0 <= x <= X1_ and Z0 <= z <= Z1_): continue
        c = col(b); f = max(0.55, min(1.35, 0.8 + (y - 63) * 0.025))
        c = tuple(min(255, int(v * f)) for v in c)
        for dy in range(S):
            for dx in range(S): img[(z - Z0) * S + dy][(x - X0) * S + dx] = c
    for (_, _, _, a, b, c2, d) in PLOTS:
        for x in range(a, b + 1):
            for z in range(c2, d + 1):
                if X0 <= x <= X1_ and Z0 <= z <= Z1_ and (x in (a, b) or z in (c2, d)):
                    for dy in range(S):
                        for dx in range(S): img[(z - Z0) * S + dy][(x - X0) * S + dx] = (255, 60, 60)
    raw = b''.join(b'\0' + b''.join(bytes(p) for p in r) for r in img)
    def ch(t, dd): return struct.pack('>I', len(dd)) + t + dd + struct.pack('>I', zlib.crc32(t + dd) & 0xffffffff)
    open(sys.argv[2], 'wb').write(b'\x89PNG\r\n\x1a\n' + ch(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0)) + ch(b'IDAT', zlib.compress(raw)) + ch(b'IEND', b''))
    print('aperçu :', sys.argv[2])

# panneaux du spawn à orientation fixe : décor recréé une fois sur les mondes existants (témoin mg:lobby deco3)
def _patch(rel, anchor, line):
    pth = os.path.join(R, 'data/mg/function', rel + '.mcfunction'); t = open(pth, encoding='utf-8').read()
    if line in t: return
    assert anchor in t, (rel, anchor)
    open(pth, 'w', encoding='utf-8', newline='\n').write(t.replace(anchor, anchor + '\n' + line, 1))
_patch('core/load', 'execute unless score $rp mg.st matches 0.. run function mg:core/rp_default',
       'execute if score $setup mg.st matches 1 unless data storage mg:lobby deco3 run schedule function mg:lobby/deco 6s')
_patch('desinstaller', 'data remove storage mg:lobby beacon1', 'data remove storage mg:lobby deco3\ndata remove storage mg:lobby deco2')
