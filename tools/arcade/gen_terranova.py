"""🦖 Terra Nova : colonie préhistorique, monde libre (dimension mg:terranova) relié au lobby par un portail (en face de Neo GTA).

    python tools/arcade/gen_terranova.py .      (avant tools/duel/gen_duel.py : il ajoute une garde à terra/menu_go, réécrit ici)

Monde
- Dimension mg:terranova (data/mg/dimension/terranova.json) : vide, biome the_void (aucune apparition naturelle). Carte bornée
  192 × 192 construite une fois par mg:terra/world_build (~2 min) : jungle (relief, rivière, falaises au bord, arbres et
  bambous posés par « place feature »), colonie fortifiée au centre, 3 outposts. Ajouter la dimension demande un
  redémarrage du serveur (pas un simple /reload).
- Session : démarre au premier joueur (chargement forcé + entités), s'arrête au dernier (entités retirées, outposts réparés).
- Joueurs : tags mg.tvw + mg.surv (comme Neo GTA : exclus des mini-jeux, menu « retour au lobby »). Crédits (mg.tvc) gardés
  d'une visite à l'autre, équipement de base à chaque arrivée.

Jeu
- Colonie (sûre, défenses du périmètre) : dépôt d'équipement (7 présentoirs), infirmerie (soins), tableau des missions,
  portes nord et sud, portail du temps (retour au spawn).
- Armes : bâton électrique (étourdit), fusil à impulsions (surchauffe), canon sonique (onde en cône qui repousse),
  lance-filets et pièges au sol (immobilisent).
- Dinosaures (mobs vanilla invisibles + modèle en block_display) : slashers (vindicateurs, en meute, traquent),
  carnotaure (hoglin, mini-boss, casse les structures légères des outposts), brachiosaures (dromadaires) et
  pachycéphalosaures (chèvres) neutres.
- Missions : récupération de matériel (caisse à ramener), défense d'outpost (90 s), chasse aux slashers, chasse au carnotaure.
"""
import json
import math
import os
import random
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
import shutil
for _d in ('b', 'r', 'bio', 'an', 'dino', 'rpg'):                  # dossiers entièrement générés : repartis de zéro
    shutil.rmtree(os.path.join(C.F, 'terra', _d), ignore_errors=True)
w, js = C.w, C.js
DIM = 'mg:terranova'
HX = 96                                  # carte : x, z de -96 à 95
FL = '-112 -112 111 111'                 # chargement forcé (marge d'un chunk pour les arbres)
WALL = 28                                # enceinte de la colonie
G = 64                                   # sol de la colonie (on marche à y 65)
PX, PZ = -9, -19                         # portail du lobby (en face de celui de Neo GTA, x 9 z -19)
SPAWN = (0.5, 65, 4.5)                   # arrivée : place centrale, regard vers le nord
MED = (16.5, 65, 17.5)                   # réapparition : infirmerie
EXITA = (-12, 16)                        # portail du temps (sortie), ouverture z 15..17
COLONY_BOX = f'x={-WALL},y=58,z={-WALL},dx={2 * WALL},dy=30,dz={2 * WALL}'
TR = 'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[%sf,%sf,%sf],scale:[%sf,%sf,%sf]}'
rnd = random.Random(2042)

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

# ---------------------------------------------------------------- colonie
S = []


def fill(x1, y1, z1, x2, y2, z2, b, mode=''):
    S.append(f'fill {x1} {y1} {z1} {x2} {y2} {z2} minecraft:{b}{" " + mode if mode else ""}')


def setb(x, y, z, b):
    S.append(f'setblock {x} {y} {z} minecraft:{b}')


def building(x1, z1, x2, z2, hgt, wall, floor, roof, pillar, door, windows='glass_pane'):
    """door = (côté 'n'|'s'|'e'|'w', centre, largeur)"""
    top_y = G + hgt
    fill(x1, G, z1, x2, G, z2, floor)
    fill(x1, G + 1, z1, x2, top_y, z2, wall, 'hollow')
    fill(x1 + 1, G + 1, z1 + 1, x2 - 1, top_y, z2 - 1, 'air')
    for (x, z) in [(x1, z1), (x1, z2), (x2, z1), (x2, z2)]:
        fill(x, G + 1, z, x, top_y, z, pillar)
    fill(x1 - 1, top_y + 1, z1 - 1, x2 + 1, top_y + 1, z2 + 1, roof)
    for x in range(x1 + 2, x2 - 1, 3):
        fill(x, G + 2, z1, x, G + 3, z1, windows)
        fill(x, G + 2, z2, x, G + 3, z2, windows)
    for z in range(z1 + 2, z2 - 1, 3):
        fill(x1, G + 2, z, x1, G + 3, z, windows)
        fill(x2, G + 2, z, x2, G + 3, z, windows)
    side, c, wd = door
    a, b = c - wd // 2, c + wd // 2
    if side in 'ew':
        x = x2 if side == 'e' else x1
        fill(x, G + 1, a, x, G + 3, b, 'air')
        fill(x, G + 4, a - 1, x, G + 4, b + 1, pillar)
    else:
        z = z2 if side == 's' else z1
        fill(a, G + 1, z, b, G + 3, z, 'air')
        fill(a - 1, G + 4, z, b + 1, G + 4, z, pillar)
    for x in range(x1 + 3, x2 - 1, 5):
        for z in range(z1 + 3, z2 - 1, 5):
            setb(x, top_y, z, 'lantern[hanging=true]')


# sol : herbe, routes, place
fill(-WALL + 1, G, -WALL + 1, WALL - 1, G, WALL - 1, 'grass_block')
fill(-2, G, -WALL, 2, G, WALL, 'packed_mud')
fill(-WALL + 1, G, -2, WALL - 1, G, 2, 'packed_mud')
for x in range(-8, 9):
    for z in range(-8, 9):
        if x * x + z * z <= 56:
            setb(x, G, z, 'polished_andesite' if (x + z) % 2 else 'andesite')
fill(-1, G, -1, 1, G, 1, 'chiseled_stone_bricks')
for _y in range(G + 1, G + 13):
    fill(-WALL + 1, _y, -WALL + 1, WALL - 1, _y, WALL - 1, 'air')
# palissade
for (a, b, c, d) in [(-WALL, -WALL, WALL, -WALL), (-WALL, WALL, WALL, WALL), (-WALL, -WALL, -WALL, WALL), (WALL, -WALL, WALL, WALL)]:
    fill(a, G - 2, b, c, G + 6, d, 'spruce_log')
    fill(a, G + 7, b, c, G + 7, d, 'spruce_fence')
for zg, lab in [(-WALL, 'n'), (WALL, 's')]:
    fill(-3, G + 1, zg, 3, G + 5, zg, 'air')
    fill(-3, G + 7, zg, 3, G + 7, zg, 'air')
    fill(-4, G + 1, zg, -4, G + 9, zg, 'dark_oak_log')
    fill(4, G + 1, zg, 4, G + 9, zg, 'dark_oak_log')
    fill(-4, G + 6, zg, 4, G + 7, zg, 'stripped_dark_oak_log[axis=x]')
    fill(-3, G + 5, zg, 3, G + 5, zg, 'iron_bars')
    setb(-4, G + 10, zg, 'lantern')
    setb(4, G + 10, zg, 'lantern')
    fill(-3, G, zg - 1, 3, G, zg + 1, 'packed_mud')
# tours de guet (coins)
for cx in (-WALL, WALL):
    for cz in (-WALL, WALL):
        fill(cx - 2, G - 2, cz - 2, cx + 2, G + 11, cz + 2, 'spruce_planks', 'hollow')
        fill(cx - 2, G + 12, cz - 2, cx + 2, G + 12, cz + 2, 'dark_oak_slab')
        for (x, z) in [(cx - 2, cz - 2), (cx - 2, cz + 2), (cx + 2, cz - 2), (cx + 2, cz + 2)]:
            fill(x, G - 2, z, x, G + 13, z, 'stripped_spruce_log')
        fill(cx - 2, G + 9, cz, cx + 2, G + 10, cz, 'light_gray_stained_glass_pane')
        fill(cx, G + 9, cz - 2, cx, G + 10, cz + 2, 'light_gray_stained_glass_pane')
        setb(cx, G + 13, cz, 'lightning_rod')
        setb(cx, G + 14, cz, 'end_rod')
        setb(cx - 1, G + 13, cz - 1, 'lantern')
        setb(cx + 1, G + 13, cz + 1, 'lantern')
# dépôt d'équipement (nord-ouest)
building(-24, -25, -8, -11, 6, 'spruce_planks', 'smooth_stone', 'dark_oak_slab', 'stripped_dark_oak_log', ('e', -18, 3))
fill(-23, G + 1, -24, -9, G + 1, -24, 'barrel[facing=up]')
PADS = [(-23, 'sonic'), (-21, 'mk2'), (-19, 'net'), (-17, 'netx'), (-15, 'trap'), (-13, 'med'), (-11, 'armor'), (-9, 'saddle')]
SHOP_FIX = ['# Socles des présentoirs du dépôt (corrige un monde construit avant le 8e présentoir)',
            f'fill -23 {G + 1} -22 -9 {G + 1} -22 minecraft:air'] + [f'setblock {x} {G + 1} -22 minecraft:polished_andesite' for (x, _) in PADS]
w('terra/shop_fix', SHOP_FIX)
for (x, _) in PADS:
    setb(x, G + 1, -22, 'polished_andesite')
for x in range(-22, -9, 4):
    setb(x, G + 7, -18, 'daylight_detector')
# QG (nord-est) + tableau des missions
building(10, -25, 24, -11, 7, 'light_gray_concrete', 'spruce_planks', 'smooth_stone_slab', 'stripped_spruce_log', ('w', -18, 3))
setb(17, G + 1, -18, 'cartography_table')
setb(18, G + 1, -18, 'lectern[facing=west]')
fill(22, G + 1, -24, 23, G + 2, -24, 'bookshelf')
fill(17, G + 9, -18, 17, G + 12, -18, 'iron_bars')
setb(17, G + 13, -18, 'lightning_rod')
for x in range(12, 24, 3):
    setb(x, G + 9, -13, 'daylight_detector')
    setb(x, G + 9, -23, 'daylight_detector')
fill(9, G + 1, -24, 9, G + 3, -21, 'spruce_planks')
fill(9, G + 4, -25, 9, G + 4, -20, 'spruce_slab')
fill(9, G + 1, -25, 9, G + 4, -25, 'stripped_spruce_log')
fill(9, G + 1, -20, 9, G + 4, -20, 'stripped_spruce_log')
fill(3, G, -24, 8, G, -21, 'packed_mud')
# infirmerie (sud-est)
building(8, 10, 24, 24, 5, 'white_concrete', 'white_terracotta', 'smooth_stone_slab', 'light_gray_concrete', ('w', 17, 3))
fill(8, G + 4, 13, 8, G + 4, 21, 'white_concrete')
fill(7, G + 7, 16, 7, G + 7, 18, 'red_concrete')
fill(7, G + 6, 17, 7, G + 8, 17, 'red_concrete')
for z in (12, 15, 20, 23):
    setb(23, G + 1, z, 'red_bed[facing=west,part=head]')
    setb(22, G + 1, z, 'red_bed[facing=west,part=foot]')
setb(12, G + 1, 11, 'brewing_stand')
setb(13, G + 1, 11, 'cauldron')
# maisons des colons (sud-ouest) + portail du temps
for (x1, z1) in [(-25, 20), (-25, 7)]:
    building(x1, z1, x1 + 8, z1 + 5, 4, 'birch_planks', 'spruce_planks', 'dark_oak_slab', 'stripped_birch_log', ('e', z1 + 2, 1))
    setb(x1 + 6, G + 1, z1 + 1, 'barrel[facing=up]')
    setb(x1 + 1, G + 1, z1 + 4, 'crafting_table')
ex, ez = EXITA
fill(ex, G, ez - 3, ex, G, ez + 3, 'polished_blackstone_bricks')
fill(ex, G + 1, ez - 2, ex, G + 6, ez - 2, 'polished_blackstone')
fill(ex, G + 1, ez + 2, ex, G + 6, ez + 2, 'polished_blackstone')
fill(ex, G + 7, ez - 2, ex, G + 7, ez + 2, 'polished_blackstone_brick_slab')
fill(ex, G + 1, ez - 3, ex, G + 5, ez - 3, 'crying_obsidian')
fill(ex, G + 1, ez + 3, ex, G + 5, ez + 3, 'crying_obsidian')
setb(ex, G + 6, ez - 3, 'amethyst_cluster')
setb(ex, G + 6, ez + 3, 'amethyst_cluster')
fill(ex + 1, G, ez - 1, -3, G, ez + 1, 'packed_mud')
# éclairage des routes, réserves
for z in range(-24, 25, 8):
    for x in (-3, 3):
        if abs(z) > 9:
            setb(x, G + 1, z, 'spruce_fence')
            setb(x, G + 2, z, 'spruce_fence')
            setb(x, G + 3, z, 'lantern')
for (x, z) in [(-6, 10), (-7, 10), (-6, 11), (6, -6), (7, -6), (-24, -4), (-23, -4), (-24, -5), (24, 6), (24, 7)]:
    setb(x, G + 1, z, rnd.choice(['barrel[facing=up]', 'hay_block', 'composter', 'spruce_trapdoor[half=top]']))

# ---------------------------------------------------------------- outposts (blocs « légers » : le carnotaure les casse)
LIGHT = ['oak_planks', 'oak_fence', 'oak_slab', 'white_wool', 'glass_pane', 'scaffolding', 'oak_trapdoor', 'lantern']
OUT_B = {}
for k, (name, ox, oz) in enumerate(OUTPOSTS, 1):
    h = OUT_H[name]
    L = [f'# Outpost {name} : (re)construction',
         f'fill {ox - 6} {h + 1} {oz - 6} {ox + 6} {h + 7} {oz + 6} minecraft:air',
         f'fill {ox - 5} {h} {oz - 5} {ox + 5} {h} {oz + 5} minecraft:oak_planks',
         f'fill {ox - 5} {h + 1} {oz - 5} {ox + 5} {h + 1} {oz + 5} minecraft:oak_fence outline',
         f'fill {ox - 1} {h + 1} {oz - 5} {ox + 1} {h + 1} {oz - 5} minecraft:air', f'fill {ox - 1} {h + 1} {oz + 5} {ox + 1} {h + 1} {oz + 5} minecraft:air',
         f'fill {ox - 5} {h + 1} {oz - 1} {ox - 5} {h + 1} {oz + 1} minecraft:air', f'fill {ox + 5} {h + 1} {oz - 1} {ox + 5} {h + 1} {oz + 1} minecraft:air',
         f'setblock {ox} {h + 1} {oz} minecraft:iron_block', f'setblock {ox} {h + 2} {oz} minecraft:lodestone',
         f'setblock {ox} {h + 3} {oz} minecraft:lightning_rod',
         f'fill {ox - 1} {h + 1} {oz - 1} {ox + 1} {h + 1} {oz + 1} minecraft:oak_slab replace minecraft:air',
         f'fill {ox + 2} {h + 1} {oz + 2} {ox + 4} {h + 1} {oz + 4} minecraft:oak_fence outline',
         f'fill {ox + 2} {h + 2} {oz + 2} {ox + 4} {h + 2} {oz + 4} minecraft:white_wool',
         f'fill {ox - 4} {h + 1} {oz + 2} {ox - 2} {h + 1} {oz + 4} minecraft:oak_fence outline',
         f'fill {ox - 4} {h + 2} {oz + 2} {ox - 2} {h + 2} {oz + 4} minecraft:white_wool',
         f'fill {ox - 4} {h + 1} {oz - 4} {ox - 4} {h + 3} {oz - 4} minecraft:oak_fence',
         f'setblock {ox - 4} {h + 4} {oz - 4} minecraft:lantern',
         f'fill {ox + 3} {h + 1} {oz - 4} {ox + 4} {h + 2} {oz - 3} minecraft:scaffolding',
         f'fill {ox - 1} {h + 2} {oz - 1} {ox + 1} {h + 2} {oz - 1} minecraft:glass_pane',
         f'fill {ox - 1} {h + 2} {oz + 1} {ox + 1} {h + 2} {oz + 1} minecraft:glass_pane']
    OUT_B[k] = L
    w(f'terra/out_build_{k}', L)
    S.append(f'function mg:terra/out_build_{k}')

# ---------------------------------------------------------------- régions du RPG (tv_world.py)
TVW = dict(globals())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tv_world.py'), encoding='utf-8').read(), TVW)
R_TERRAIN, RS_CMD, R_VEG, R_BIOME, V_PATCH, V_BIOME, VSTRUCT, FL_REGIONS = (TVW[k] for k in (
    'R_TERRAIN', 'RS_CMD', 'R_VEG', 'R_BIOME', 'V_PATCH', 'V_BIOME', 'VSTRUCT', 'FL_REGIONS'))
VCARVE = []                                         # mondes construits avant les cols : falaises creusées
for (x, z), h0 in sorted(H_OLD.items()):
    h = H[(x, z)]
    if h != h0:
        VCARVE += [f'fill {x} 56 {z} {x} {h - 1} {z} minecraft:{under(x, z)}', f'setblock {x} {h} {z} minecraft:{surface(x, z)}',
                   f'fill {x} {h + 1} {z} {x} {max(h, h0) + 12} {z} minecraft:air']

# ---------------------------------------------------------------- étapes de construction
STEPS = []
for i in range(0, len(TERRAIN), 450):
    STEPS.append(TERRAIN[i:i + 450])
for i in range(0, len(S), 300):
    STEPS.append(S[i:i + 300])
for i in range(0, len(VEG), 40):
    STEPS.append(VEG[i:i + 40])
for i, L in enumerate(STEPS, 1):
    w(f'terra/b/s{i}', [f'# Construction de Terra Nova, étape {i}/{len(STEPS)} (dimension {DIM}, générée)'] + L)
NS = len(STEPS)
w('terra/wb_step', ['# Une étape de construction de Terra Nova par tick ($tvb), dans la dimension. Planifiée.',
                    'scoreboard players add $tvb mg.st 1'] +
  [f'execute if score $tvb mg.st matches {i} in {DIM} run function mg:terra/b/s{i}' for i in range(1, NS + 1)] +
  [f'execute if score $tvb mg.st matches {NS + 1} run function mg:terra/wb_done',
   f'execute if score $tvb mg.st matches ..{NS} run schedule function mg:terra/wb_step 1t'])
w('terra/wb_done', ['# Vallée de Terra Nova prête : drapeau, puis construction des régions du RPG',
                    f'execute in {DIM} run kill @e[type=minecraft:item,x=-100,y=40,z=-100,dx=200,dy=80,dz=200]',
                    f'execute in {DIM} if block 0 {G} 0 minecraft:chiseled_stone_bricks run data modify storage mg:terra built set value 1b',
                    'function mg:terra/world_build2'])
# régions : chargement forcé de toute la carte, une étape par tick
RSTEPS = []
for k in ('n', 'e', 'w', 's'):
    for L, n in ((R_TERRAIN[k], 450), (RS_CMD[k], 200), (R_VEG[k], 40)):
        for i in range(0, len(L), n):
            RSTEPS.append(L[i:i + n])
for L in (VCARVE + V_PATCH + VSTRUCT,):
    for i in range(0, len(L), 300):
        RSTEPS.append(L[i:i + 300])
for i, L in enumerate(RSTEPS, 1):
    w(f'terra/r/s{i}', [f'# Construction des régions de Terra Nova, étape {i}/{len(RSTEPS)} (dimension {DIM}, générée)'] + L)
NR = len(RSTEPS)
FL_ALL = [FL] + list(FL_REGIONS.values())
w('terra/rb_step', ['# Une étape de construction des régions par tick ($tvrb), dans la dimension. Planifiée.',
                    'scoreboard players add $tvrb mg.st 1'] +
  [f'execute if score $tvrb mg.st matches {i} in {DIM} run function mg:terra/r/s{i}' for i in range(1, NR + 1)] +
  [f'execute if score $tvrb mg.st matches {NR + 1} run function mg:terra/rb_done',
   f'execute if score $tvrb mg.st matches ..{NR} run schedule function mg:terra/rb_step 1t'])
w('terra/world_build2', ['# Construction des régions du RPG (marais, plaines, canyon, volcan) + cols de la vallée (~3 min)',
                         'scoreboard players set $tvrb mg.st 0'] + [f'execute in {DIM} run forceload add {f}' for f in FL_ALL] +
  ['schedule function mg:terra/rb_step 100t'])
# biomes du datapack : connus seulement après un redémarrage du serveur. Les fonctions bio/* ne se chargent pas avant :
# mg:terra/bio_try (session, fin de construction) teste mg:terra/bio/ok et lance le remplissage une fois.
BIO = [l for k in ('n', 'e', 'w', 's') for l in R_BIOME[k]] + V_BIOME
for i in range(0, len(BIO), 150):
    w(f'terra/bio/s{i // 150 + 1}', [f'# Biomes de Terra Nova, étape {i // 150 + 1} (dimension {DIM})'] + BIO[i:i + 150])
NB = (len(BIO) + 149) // 150
w('terra/bio/ok', ['# Se charge seulement si les biomes du datapack existent (sinon l’appel échoue)', 'execute if biome 0 0 0 mg:tv_jungle run return 1', 'return 1'])
w('terra/bio_try', ['# Biomes des régions posés une seule fois, dès que le serveur les connaît (après un redémarrage)',
                    'execute if data storage mg:terra bio run return 0', 'execute unless data storage mg:terra v2 run return 0',
                    'scoreboard players set $tvbo mg.st 0', 'execute store result score $tvbo mg.st run function mg:terra/bio/ok',
                    'execute unless score $tvbo mg.st matches 1 run return 0',
                    'data modify storage mg:terra bio set value 1b', 'scoreboard players set $tvbs mg.st 0'] +
  [f'execute in {DIM} run forceload add {f}' for f in FL_ALL] + ['schedule function mg:terra/bio_step 60t'])
w('terra/bio_step', ['# Une étape de biomes par tick (zone chargée : session ou fin de construction)', 'scoreboard players add $tvbs mg.st 1'] +
  [f'execute if score $tvbs mg.st matches {i} in {DIM} run function mg:terra/bio/s{i}' for i in range(1, NB + 1)] +
  [f'execute if score $tvbs mg.st matches ..{NB - 1} run return run schedule function mg:terra/bio_step 1t'] +
  [f'execute unless score $tvw mg.st matches 1 in {DIM} run forceload remove {f}' for f in FL_ALL])
w('terra/rb_done', ['# Régions prêtes : bords de la carte, drapeau, plus de chargement forcé si personne ne joue',
                    f'execute in {DIM} run kill @e[type=minecraft:item,x=-260,y=40,z=-260,dx=520,dy=140,dz=520]',
                    f'execute in {DIM} run function mg:terra/walls_old', f'execute in {DIM} run function mg:terra/walls',
                    'data modify storage mg:terra v2 set value 1b'] +
  [f'execute unless score $tvw mg.st matches 1 in {DIM} run forceload remove {f}' for f in FL_ALL] +
  ['function mg:terra/bio_try', 'tellraw @a[tag=mg.admin] {"text":"🦖 Terra Nova est construite (vallée et régions du RPG).","color":"green"}'])
w('terra/world_build', ['# Première construction de Terra Nova (ou reconstruction complète, ~2 min)',
                        f'execute in {DIM} run forceload add {FL}', 'scoreboard players set $tvb mg.st 0',
                        'schedule function mg:terra/wb_step 40t'])
os.makedirs(os.path.join(C.D, 'dimension'), exist_ok=True)
with open(os.path.join(C.D, 'dimension', 'terranova.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'type': 'minecraft:overworld', 'generator': {'type': 'minecraft:flat', 'settings': {
        'biome': 'minecraft:the_void', 'layers': [], 'lakes': False, 'features': False, 'structure_overrides': []}}}, f, indent=2)
    f.write('\n')
os.makedirs(os.path.join(C.D, 'tags', 'block'), exist_ok=True)
with open(os.path.join(C.D, 'tags', 'block', 'tv_light.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'values': [f'minecraft:{b}' for b in LIGHT]}, f, indent=2)
    f.write('\n')
with open(os.path.join(C.D, 'tags', 'block', 'tv_pass.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'values': ['#mg:ray_pass', '#minecraft:leaves', 'minecraft:bamboo', 'minecraft:firefly_bush',
                          {'id': 'minecraft:bush', 'required': False}, 'minecraft:cocoa', 'minecraft:melon_stem']}, f, indent=2)
    f.write('\n')

# ================================================================ objets
WF = 'minecraft:warped_fungus_on_a_stick'


def nm(t, c):
    return js({'text': t, 'color': c, 'italic': False, 'bold': True})


def lo(*ls):
    return '[' + ','.join(js({'text': l, 'color': 'gray', 'italic': False}) for l in ls) + ']'


PROD = (f'minecraft:stick[custom_data={{tv:1}},item_model="minecraft:blaze_rod",custom_name={nm("⚡ Bâton électrique", "yellow")},'
        f'lore={lo("Mêlée : étourdit le dinosaure touché", "(lenteur V + faiblesse, 3 s)")},'
        'attribute_modifiers=[{type:"minecraft:attack_damage",id:"mg:tvprod",amount:5.0,operation:"add_value",slot:"mainhand"}]]')
RIFLE1 = (f'{WF}[custom_data={{tv:2}},item_model="minecraft:crossbow",unbreakable={{}},custom_name={nm("🔫 Fusil à impulsions", "aqua")},'
          f'lore={lo("Clic droit : tir (maintenir = rafale)", "Attention à la surchauffe !")}]')
RIFLE2 = (f'{WF}[custom_data={{tv:3}},item_model="minecraft:crossbow",unbreakable={{}},enchantment_glint_override=true,'
          f'custom_name={nm("🔫 Fusil à impulsions Mk2", "gold")},lore={lo("Plus puissant, chauffe moins vite", "Clic droit : tir")}]')
SONIC = (f'{WF}[custom_data={{tv:4}},item_model="minecraft:goat_horn",unbreakable={{}},custom_name={nm("📢 Canon sonique", "aqua")},'
         f'lore={lo("Clic droit : onde de choc en cône (8 blocs)", "Repousse et ralentit, recharge 4 s")}]')
NETL = (f'{WF}[custom_data={{tv:5}},item_model="minecraft:fishing_rod",unbreakable={{}},custom_name={nm("🕸 Lance-filets", "white")},'
        f'lore={lo("Clic droit : immobilise un dinosaure 5 s", "Filets en vente au dépôt")}]')
TRAP = (f'{WF}[custom_data={{tv:6}},item_model="minecraft:tripwire_hook",unbreakable={{}},custom_name={nm("⚙ Pièges au sol", "gray")},'
        f'lore={lo("Clic droit : pose un piège à tes pieds", "Le premier prédateur qui marche dessus est bloqué 6 s")}]')
HOME = (f'{WF}[custom_data={{tv:9}},item_model="minecraft:bell",unbreakable={{}},custom_name={nm("📡 Rappel à la colonie", "green")},'
        f'lore={lo("Clic droit : retour à la colonie en 5 s", "Annulé si tu prends un coup")}]')
SADDLE = (f'minecraft:saddle[custom_name={nm("🐴 Selle de brachiosaure", "yellow")},'
          f'lore={lo("Clic droit sur un brachiosaure pour la poser,", "puis clic droit pour monter (Z/Q/S/D, espace = élan)")}]')
MEDK = f'minecraft:golden_apple[custom_name={nm("✚ Trousse de soins", "red")}]'
UNIF_C = f'minecraft:leather_chestplate[dyed_color=9140827,unbreakable={{}},custom_name={nm("Uniforme de colon", "gold")}]'
UNIF_B = f'minecraft:leather_boots[dyed_color=5915971,unbreakable={{}},custom_name={nm("Bottes de colon", "gold")}]'
ARM = {s: f'minecraft:chainmail_{p}[unbreakable={{}},custom_data={{tvarm:1b}},custom_name={nm("🛡 Armure de patrouille", "dark_aqua")}]'
       for s, p in [('head', 'helmet'), ('chest', 'chestplate'), ('legs', 'leggings')]}

w('terra/loc', ['# @s : 📡 localisateur (boussole) vers $(x) $(y) $(z) (macro), en case 9 de la barre',
                'clear @s minecraft:compass[minecraft:custom_data~{tvloc:1b}]',
                f'$item replace entity @s hotbar.8 with minecraft:compass[custom_data={{tvloc:1b}},lodestone_tracker={{target:{{pos:[I;$(x),$(y),$(z)],dimension:"{DIM}"}},tracked:false}},'
                f'custom_name={nm("📡 Localisateur", "aqua")},lore={lo("Indique la colonie ou l’objectif de ta mission")}]',
                '$scoreboard players set @s mg.trox $(x)', '$scoreboard players set @s mg.troy $(y)', '$scoreboard players set @s mg.troz $(z)',
                'scoreboard players set @s mg.tron 1'])
LOC_HOME = 'function mg:terra/loc {x:0,y:65,z:0}'
w('terra/kit', ['# @s : équipement (paliers du RPG gardés : mêlée, fusil, armure, scanner, sifflet)', 'clear @s',
                'function mg:terra/rpg/kit', f'item replace entity @s hotbar.7 with {HOME}', 'function mg:terra/rpg/qloc',
                'scoreboard players set @s mg.tvnet 0', 'scoreboard players set @s mg.tvtr 0',
                'effect give @s minecraft:saturation infinite 0 true'])

# ================================================================ portail du lobby (monde des mini-jeux)
def part(tags, blk, tx, ty, tz, sx, sy, sz, at='~ ~ ~', extra=''):
    if '"mg.tvp"' in tags:
        tags += ',"mg.tvok"'
    return (f'summon minecraft:block_display {at} {{Tags:[{tags}],block_state:{{Name:"minecraft:{blk}"}},teleport_duration:2,'
            f'{TR % (tx, ty, tz, sx, sy, sz)}{extra}}}')


RAPTOR = [('green_terracotta', -0.28, 0.75, -0.55, 0.56, 0.5, 1.05), ('green_terracotta', -0.14, 1.05, 0.35, 0.28, 0.45, 0.3),
          ('green_terracotta', -0.2, 1.38, 0.4, 0.4, 0.32, 0.6), ('lime_terracotta', -0.15, 1.3, 0.98, 0.3, 0.16, 0.2),
          ('yellow_concrete', -0.21, 1.55, 0.74, 0.42, 0.06, 0.08), ('white_concrete', -0.13, 1.28, 1.0, 0.26, 0.04, 0.16),
          ('green_terracotta', -0.12, 0.88, -1.45, 0.24, 0.24, 0.92), ('black_terracotta', -0.07, 0.92, -1.85, 0.14, 0.14, 0.42),
          ('black_terracotta', -0.29, 1.0, -0.3, 0.58, 0.1, 0.12), ('black_terracotta', -0.29, 1.0, 0.1, 0.58, 0.1, 0.12),
          ('brown_terracotta', -0.26, 0.0, -0.15, 0.13, 0.78, 0.2), ('brown_terracotta', 0.13, 0.0, -0.15, 0.13, 0.78, 0.2),
          ('brown_terracotta', -0.24, 0.85, 0.42, 0.08, 0.25, 0.08), ('brown_terracotta', 0.16, 0.85, 0.42, 0.08, 0.25, 0.08)]
CARNO = [('red_terracotta', -0.8, 1.4, -1.3, 1.6, 1.3, 2.5), ('orange_terracotta', -0.7, 1.3, -1.0, 1.4, 0.15, 1.9),
         ('red_terracotta', -0.45, 2.2, 1.0, 0.9, 0.8, 0.6), ('red_terracotta', -0.6, 2.45, 1.4, 1.2, 0.95, 1.4),
         ('brown_terracotta', -0.5, 2.15, 1.5, 1.0, 0.3, 1.2), ('white_concrete', -0.48, 2.42, 2.78, 0.96, 0.08, 0.06),
         ('black_terracotta', -0.6, 3.38, 1.6, 0.25, 0.35, 0.25), ('black_terracotta', 0.35, 3.38, 1.6, 0.25, 0.35, 0.25),
         ('yellow_concrete', -0.62, 2.95, 2.2, 1.24, 0.12, 0.12), ('red_terracotta', -0.4, 1.8, -3.3, 0.8, 0.7, 2.0),
         ('red_terracotta', -0.2, 1.9, -4.4, 0.4, 0.4, 1.1), ('brown_terracotta', -0.8, 0.0, -0.6, 0.5, 1.5, 0.7),
         ('brown_terracotta', 0.3, 0.0, -0.6, 0.5, 1.5, 0.7), ('red_terracotta', -0.75, 1.7, 1.0, 0.15, 0.4, 0.15),
         ('red_terracotta', 0.6, 1.7, 1.0, 0.15, 0.4, 0.15), ('black_terracotta', -0.1, 2.7, -1.1, 0.2, 0.15, 2.0)]
BRACH = [('light_gray_terracotta', -1.3, 2.4, -2.0, 2.6, 2.0, 4.0), ('white_terracotta', -1.2, 2.3, -1.6, 2.4, 0.15, 3.2),
         ('light_gray_terracotta', -0.45, 3.8, 1.7, 0.9, 2.4, 0.9), ('light_gray_terracotta', -0.4, 6.0, 2.2, 0.8, 2.2, 0.8),
         ('light_gray_terracotta', -0.5, 8.0, 2.0, 1.0, 0.7, 1.6), ('black_concrete', -0.52, 8.4, 3.0, 1.04, 0.1, 0.1),
         ('light_gray_terracotta', -0.35, 2.9, -4.6, 0.7, 0.7, 2.7), ('light_gray_terracotta', -0.2, 2.9, -6.6, 0.4, 0.4, 2.1),
         ('gray_terracotta', -1.25, 0.0, -1.8, 0.75, 2.5, 0.75), ('gray_terracotta', 0.5, 0.0, -1.8, 0.75, 2.5, 0.75),
         ('gray_terracotta', -1.25, 0.0, 0.9, 0.75, 2.5, 0.75), ('gray_terracotta', 0.5, 0.0, 0.9, 0.75, 2.5, 0.75),
         ('gray_terracotta', -1.31, 3.3, -0.5, 2.62, 0.4, 0.6)]
PACHY = [('brown_terracotta', -0.38, 0.65, -0.65, 0.76, 0.6, 1.25), ('brown_terracotta', -0.2, 0.95, 0.5, 0.4, 0.4, 0.3),
         ('orange_terracotta', -0.28, 1.05, 0.65, 0.56, 0.45, 0.5), ('white_terracotta', -0.24, 1.48, 0.68, 0.48, 0.22, 0.42),
         ('black_terracotta', -0.3, 1.4, 0.62, 0.6, 0.06, 0.06), ('black_concrete', -0.29, 1.25, 1.1, 0.58, 0.06, 0.06),
         ('brown_terracotta', -0.13, 0.85, -1.55, 0.26, 0.26, 0.95), ('brown_terracotta', -0.3, 0.0, -0.1, 0.16, 0.7, 0.22),
         ('brown_terracotta', 0.14, 0.0, -0.1, 0.16, 0.7, 0.22)]

PB = ['# Portail de Terra Nova au lobby (avenue nord, côté ouest, en face de Neo GTA), reconstruit par mg:terra/lobby_tick s\'il disparaît',
      'kill @e[tag=mg.tvport]',
      f'fill {PX - 4} 64 {PZ - 4} {PX + 4} 73 {PZ + 4} minecraft:air',
      f'fill {PX - 4} 63 {PZ - 4} {PX + 4} 63 {PZ + 4} minecraft:mossy_stone_bricks',
      f'fill {PX - 3} 63 {PZ - 3} {PX + 3} 63 {PZ + 3} minecraft:moss_block',
      f'fill {PX + 1} 63 {PZ} {PX + 4} 63 {PZ} minecraft:coarse_dirt',
      f'fill {PX} 64 {PZ - 2} {PX} 69 {PZ - 2} minecraft:jungle_log', f'fill {PX} 64 {PZ + 2} {PX} 69 {PZ + 2} minecraft:jungle_log',
      f'fill {PX} 70 {PZ - 2} {PX} 70 {PZ + 2} minecraft:stripped_jungle_log[axis=z]',
      f'fill {PX} 64 {PZ - 3} {PX} 70 {PZ - 3} minecraft:mossy_cobblestone', f'fill {PX} 64 {PZ + 3} {PX} 70 {PZ + 3} minecraft:mossy_cobblestone',
      f'fill {PX} 71 {PZ - 3} {PX} 71 {PZ + 3} minecraft:moss_block',
      f'fill {PX - 1} 72 {PZ - 3} {PX + 1} 72 {PZ + 3} minecraft:jungle_leaves[persistent=true]',
      f'setblock {PX} 73 {PZ} minecraft:jungle_leaves[persistent=true]',
      f'setblock {PX} 63 {PZ} minecraft:chiseled_tuff_bricks',
      # haie de l'avenue ouverte devant le portail, passage jusqu'à l'avenue (x -8 à -4)
      f'fill -4 64 {PZ - 1} {PX + 1} 66 {PZ + 1} minecraft:air', f'fill -4 63 {PZ - 1} {PX + 5} 63 {PZ + 1} minecraft:stone_bricks',
      f'setblock {PX + 3} 64 {PZ - 4} minecraft:bamboo_fence', f'setblock {PX + 3} 65 {PZ - 4} minecraft:bamboo_fence', f'setblock {PX + 3} 66 {PZ - 4} minecraft:lantern',
      f'setblock {PX + 3} 64 {PZ + 4} minecraft:bamboo_fence', f'setblock {PX + 3} 65 {PZ + 4} minecraft:bamboo_fence', f'setblock {PX + 3} 66 {PZ + 4} minecraft:lantern',
      f'setblock {PX - 2} 64 {PZ - 3} minecraft:large_fern[half=lower]', f'setblock {PX - 2} 65 {PZ - 3} minecraft:large_fern[half=upper]',
      f'setblock {PX - 2} 64 {PZ + 3} minecraft:large_fern[half=lower]', f'setblock {PX - 2} 65 {PZ + 3} minecraft:large_fern[half=upper]']
for y in range(65, 71):
    PB += [f'setblock {PX + 1} {y} {PZ - 3} minecraft:vine[west=true]', f'setblock {PX + 1} {y} {PZ + 3} minecraft:vine[west=true]']
PB += [f'summon minecraft:text_display {PX + 0.6} 72.6 {PZ + 0.5} {{Tags:["mg.tvport"],Rotation:[-90f,0f],text:{js({"text": "🦖 TERRA NOVA", "color": "green", "bold": True})},'
       f'background:-1442840576,{TR % (0, 0, 0, 2.6, 2.6, 2.6)}}}',
       f'summon minecraft:text_display {PX + 0.6} 72.15 {PZ + 0.5} {{Tags:["mg.tvport"],Rotation:[-90f,0f],text:{js({"text": "Colonie préhistorique : missions, jungle, dinosaures", "color": "gray"})},'
       f'background:0,{TR % (0, 0, 0, 0.9, 0.9, 0.9)}}}',
       f'summon minecraft:text_display {PX + 0.6} 64.4 {PZ + 0.5} {{Tags:["mg.tvport"],Rotation:[-90f,0f],text:{js({"text": "▶ entre dans le portail", "color": "yellow"})},'
       f'background:0,{TR % (0, 0, 0, 0.8, 0.8, 0.8)}}}']
PB += [part('"mg.tvport"', *p, at=f'{PX - 2.3} 64 {PZ + 0.5}', extra=',Rotation:[-60f,0f]') for p in RAPTOR]
PB.append('function mg:terra/spawn_clean')
w('terra/portal_build', PB)
w('terra/spawn_clean', ['# Abords du portail de Terra Nova au spawn : arbre sous le portail coupé, bordure ouest de l\'avenue (x -4) dégagée',
                        f'fill {PX - 7} 64 {PZ - 4} {PX + 4} 78 {PZ + 4} minecraft:air replace #minecraft:leaves',
                        f'fill {PX - 7} 64 {PZ - 4} {PX + 4} 78 {PZ + 4} minecraft:air replace #minecraft:logs',
                        f'fill -4 64 {PZ - 7} -4 72 {PZ + 4} minecraft:air',
                        f'fill -4 63 {PZ - 4} -4 63 {PZ + 4} minecraft:stone_bricks',
                        f'fill -4 63 {PZ - 1} {PX + 5} 63 {PZ + 1} minecraft:stone_bricks',
                        'data modify storage mg:lobby tvclean set value 1b'])
ENTER_SEL = (f'tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,'
             f'gamemode=adventure,x={PX},y=64,z={PZ - 1},dx=0,dy=2,dz=2')
w('terra/lobby_tick', ['# Chaque tick (core/tick, monde des mini-jeux) : portail de Terra Nova, session du monde',
                       f'execute if score $setup mg.st matches 1 as @a[{ENTER_SEL}] run function mg:terra/enter',
                       f'particle minecraft:dust{{color:[0.3,0.85,0.25],scale:1.1}} {PX + 0.5} 66.5 {PZ + 0.5} 0.05 1.3 1.1 0 3',
                       f'particle minecraft:spore_blossom_air {PX + 0.5} 66.5 {PZ + 0.5} 0.05 1.3 1.1 0 2',
                       f'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block {PX} 63 {PZ} minecraft:chiseled_tuff_bricks run function mg:terra/portal_build',
                       'execute unless score $tvw mg.st matches 1 if entity @a[tag=mg.tvw] run function mg:terra/session_start',
                       'execute if score $tvw mg.st matches 1 unless entity @a[tag=mg.tvw] run function mg:terra/session_end',
                       f'execute if score $tvw mg.st matches 1 in {DIM} run function mg:terra/tick'])
w('terra/pre_tick', ['# Avant la survie (core/tick) : un joueur de Terra Nova sorti de la dimension sans passer par la sortie perd ses tags',
                     f'execute as @a[tag=mg.tvw] at @s unless dimension {DIM} run function mg:terra/strayed'])
w('terra/strayed', ['# @s a quitté Terra Nova autrement (téléportation…)', 'tag @s remove mg.tvw', 'tag @s remove mg.surv', 'function mg:terra/mis_clear', 'function mg:terra/traps_clear', 'function mg:terra/untag',
                     'function mg:terra/rpg/leave'])
w('terra/traps_clear', ['# @s part : ses pièges disparaissent', 'scoreboard players operation $own mg.st = @s mg.tvpid',
                        'execute as @e[tag=mg.tvtrap] if score @s mg.tvo = $own mg.st run kill @s', 'execute as @e[tag=mg.tvtrapd] if score @s mg.tvo = $own mg.st run kill @s'])

# ================================================================ entrée, sortie, session
w('terra/enter', ['# @s entre dans le portail de Terra Nova (contexte : monde des mini-jeux)',
                  'execute unless data storage mg:terra built run return run function mg:terra/not_ready',
                  'execute if entity @s[tag=mg.mpp] run return run tellraw @s {"text":"⚠ Tu participes à la Mini Party : Terra Nova sera accessible après.","color":"red"}',
                  'function mg:lobkart/leave', 'function mg:parkour/quit',
                  'tag @s remove mg.inplot', 'tag @s remove mg.plabel', 'tag @s remove mg.visit',
                  'tag @s add mg.surv', 'tag @s add mg.tvw',
                  'execute if score $state mg.st matches 0 run scoreboard players reset @s mg.vc',
                  'execute if score $state mg.st matches 0 run function mg:vote/refresh',
                  'team leave @s', 'effect clear @s', 'clear @s', 'gamemode adventure @s', 'function mg:core/attr_reset',
                  'attribute @s minecraft:fall_damage_multiplier base set 1',
                  'function mg:terra/join', 'function mg:core/heal',
                  f'execute in {DIM} run spawnpoint @s {int(MED[0])} {MED[1]} {int(MED[2])}',
                  f'execute in {DIM} run tp @s {SPAWN[0]} {SPAWN[1]} {SPAWN[2]} 180 0',
                  'function mg:terra/kit',
                  'title @s times 10 60 20', 'title @s title {"text":"TERRA NOVA","color":"green","bold":true}', 'function mg:terra/rpg/enter',
                  'title @s subtitle {"text":"Il y a 85 millions d\'années…","color":"gray"}',
                  'tellraw @s ' + js([{'text': '🦖 TERRA NOVA', 'color': 'green', 'bold': True}, {'text': ' : bienvenue dans la colonie, colon !', 'color': 'yellow'}]),
                  'tellraw @s ' + js([{'text': ' 📋 Missions : ', 'color': 'gold'}, {'text': 'tableau sur le mur du QG (nord-est de la place), récompenses en crédits ₵', 'color': 'gray'}]),
                  'tellraw @s ' + js([{'text': ' 🛒 Équipement : ', 'color': 'aqua'}, {'text': 'dépôt au nord-ouest (canon sonique, filets, pièges, armure…)', 'color': 'gray'}]),
                  'tellraw @s ' + js([{'text': ' 🔫 Armes : ', 'color': 'yellow'}, {'text': 'bâton électrique (étourdit), fusil à impulsions (clic droit, gare à la surchauffe)', 'color': 'gray'}]),
                  'tellraw @s ' + js([{'text': ' ✚ Infirmerie : ', 'color': 'red'}, {'text': 'au sud-est, soigne. Mort = -10 % de tes crédits', 'color': 'gray'}]),
                  'tellraw @s ' + js([{'text': ' 🚪 Sortir : ', 'color': 'light_purple'}, {'text': 'portail du temps (sud-ouest) ou Échap → ≡ Menu', 'color': 'gray'}]),
                  'execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.3 1.8'])
w('terra/not_ready', ['# Terra Nova pas encore construite : on recule le joueur', f'tp @s {PX + 3}.5 64 {PZ}.5 90 0',
                      'tellraw @s {"text":"🚧 Terra Nova est en construction (quelques minutes après le démarrage du serveur). Réessaie bientôt !","color":"yellow"}'])
w('terra/menu_go', ['# @s : « Aller à Terra Nova » du menu Échap (trigger mg.sv 7), d\'où qu\'on soit hors partie',
                    'execute unless score $setup mg.st matches 1 run return run tellraw @s {"text":"⚠ Installation manquante : un OP doit d\'abord lancer /function mg:setup","color":"red"}',
                    'execute if entity @s[tag=mg.tvw] run return run tellraw @s {"text":"Tu es déjà à Terra Nova.","color":"gray"}',
                    'execute if entity @s[tag=mg.play] run return run tellraw @s {"text":"⚠ Tu participes à la partie en cours : Terra Nova sera accessible après.","color":"red"}',
                    'execute if entity @s[tag=mg.out] run return run tellraw @s {"text":"⚠ Partie en cours : Terra Nova sera accessible après.","color":"red"}',
                    'execute if entity @s[tag=mg.surv] run function mg:survie/leave',
                    'execute in minecraft:overworld run function mg:terra/enter'])
w('terra/join', ['# @s : réglages d\'arrivée (les crédits sont gardés d\'une visite à l\'autre)',
                 'execute unless score @s mg.tvpid matches 1.. run scoreboard players add $tvpn mg.st 1',
                 'execute unless score @s mg.tvpid matches 1.. run scoreboard players operation @s mg.tvpid = $tvpn mg.st',
                 'execute unless score @s mg.tvc matches -2147483648.. run scoreboard players set @s mg.tvc 0',
                 'function mg:terra/mis_clear',
                 'scoreboard players set @s mg.tvh 0', 'scoreboard players set @s mg.tvcd 0', 'scoreboard players set @s mg.tvsc 0',
                 'scoreboard players set @s mg.tvhm 0', 'scoreboard players set @s mg.tval 0', 'scoreboard players set @s mg.deaths 0',
                 'scoreboard players set @s mg.tvkr 0', 'scoreboard players set @s mg.tvkc 0', 'scoreboard players set @s mg.tvkb 0',
                 'scoreboard players set @s mg.tvkg 0', 'scoreboard players set @s mg.tvdd 0', 'scoreboard players reset @s mg.tvq',
                 'scoreboard players enable @s mg.tvms', 'tag @s remove mg.tvoh', 'tag @s remove mg.tvout',
                 'team add mg_tv', 'team modify mg_tv friendlyFire false', 'team modify mg_tv color dark_green', 'team join mg_tv @s',
                 'function mg:terra/rpg/join'])
w('terra/untag', ['# @s : plus joueur de Terra Nova (tags, titres, recharges)', 'tag @s remove mg.tvout', 'tag @s remove mg.tvoh', 'tag @s remove mg.tvin2',
                  'title @s clear', 'title @s reset', 'scoreboard players set @s mg.tvhm 0', 'scoreboard players set @s mg.tvh 0',
                  'effect clear @s minecraft:slowness', 'team leave @s'])
w('terra/leave', ['# @s retourne au lobby (appelé dans le monde des mini-jeux : execute in minecraft:overworld)',
                  'execute unless entity @s[tag=mg.tvw] run return 0',
                  'tag @s remove mg.tvw', 'tag @s remove mg.surv', 'function mg:terra/mis_clear', 'function mg:terra/traps_clear', 'function mg:terra/untag',
                  'function mg:terra/rpg/leave', 'function mg:core/reset_player', 'attribute @s minecraft:fall_damage_multiplier base set 0',
                  'tellraw @s [{"text":"⌂ Retour au lobby. Tes crédits restent à Terra Nova : ","color":"gold"},'
                  '{"score":{"name":"@s","objective":"mg.tvc"},"color":"green","bold":true},{"text":" ₵","color":"green"}]'])
w('terra/session_start', ['# Premier joueur à Terra Nova : chargement de la carte, entités dans 1,5 s',
                          'scoreboard players set $tvw mg.st 1', 'scoreboard players add $tvses mg.st 1', 'scoreboard players set $tvt mg.st 0', 'scoreboard players set $tvsu mg.st 0',
                          f'execute in {DIM} run forceload add {FL}'] + [f'execute in {DIM} run forceload add {f}' for f in FL_REGIONS.values()] +
  ['schedule function mg:terra/session_setup 30t', 'schedule function mg:terra/rpg/setup_s 100t'])
w('terra/rpg/setup_s', ['# Session : entités du RPG (régions chargées)', 'execute unless score $tvw mg.st matches 1 run return 0',
                        f'execute in {DIM} run function mg:terra/rpg/setup'])
w('terra/session_setup', ['# Session : entités de Terra Nova (dans la dimension)',
                          'execute unless score $tvw mg.st matches 1 run return 0', f'execute in {DIM} run function mg:terra/setup_in'])
w('terra/session_end', ['# Plus personne à Terra Nova : entités retirées, outposts réparés, plus de chargement forcé',
                        'scoreboard players set $tvw mg.st 0', 'scoreboard players set $tvsu mg.st 0', 'schedule clear mg:terra/session_setup',
                        'function mg:terra/clear', 'team remove mg_tv'] +
  [f'execute in {DIM} run function mg:terra/out_build_{k}' for k in range(1, 4)] +
  [f'execute in {DIM} run forceload remove {FL}'] + [f'execute in {DIM} run forceload remove {f}' for f in FL_REGIONS.values()] +
  ['schedule clear mg:terra/rpg/setup_s'])
w('terra/clear', ['# Retire tout ce que Terra Nova a posé (entités, objets au sol, barres)', 'kill @e[tag=mg.tv]', 'function mg:terra/rpg/clear',
                  f'execute in {DIM} run kill @e[type=minecraft:item,x=-100,y=40,z=-100,dx=200,dy=80,dz=200]',
                  f'execute in {DIM} run kill @e[type=minecraft:experience_orb,x=-100,y=40,z=-100,dx=200,dy=80,dz=200]',
                  'bossbar remove mg:tvcarno'] + [f'bossbar remove mg:tvo{k}' for k in range(1, 4)] +
  [f'scoreboard players set $tvo{k} mg.st 0' for k in range(1, 4)])
RULES = [f'execute in {DIM} run difficulty normal', f'execute in {DIM} run gamerule spawn_mobs false',
         f'execute in {DIM} run gamerule mob_griefing false', f'execute in {DIM} run gamerule keep_inventory true',
         f'execute in {DIM} run gamerule immediate_respawn true', f'execute in {DIM} run gamerule advance_time false',
         f'execute in {DIM} run gamerule advance_weather false', f'execute in {DIM} run time set 2000', f'execute in {DIM} run weather clear']
w('terra/rules', ['# Règles du monde de Terra Nova (propres à la dimension sur Paper) : jour fixe, pas d\'apparitions naturelles, inventaire gardé'] + RULES)

# ---------------------------------------------------------------- entités de la session
def tdisp(x, y, z, text, scale=1.0, bg=1140850688, extra=''):
    return (f'summon minecraft:text_display {x} {y} {z} {{Tags:["mg.tv"],billboard:"vertical",text:{js(text)},background:{bg},'
            f'{TR % (0, 0, 0, scale, scale, scale)}{extra}}}')


PAD = {'sonic': (1, '📢 Canon sonique', 'aqua', 150, 'minecraft:goat_horn'), 'mk2': (2, '🔫 Fusil à impulsions Mk2', 'gold', 220, 'minecraft:crossbow'),
       'net': (3, '🕸 Lance-filets (+3 filets)', 'white', 80, 'minecraft:fishing_rod'), 'netx': (4, '🕸 Filets ×3', 'white', 25, 'minecraft:cobweb'),
       'trap': (5, '⚙ Pièges au sol ×3', 'gray', 45, 'minecraft:tripwire_hook'), 'med': (6, '✚ Trousses de soins ×2', 'red', 15, 'minecraft:golden_apple'),
       'armor': (7, '🛡 Armure de patrouille', 'dark_aqua', 100, 'minecraft:chainmail_chestplate'),
       'saddle': (8, '🐴 Selle de brachiosaure', 'yellow', 40, 'minecraft:saddle')}
SU = ['# Session (dans la dimension) : panneaux, présentoirs, tableau, marqueurs, herbivores, barres',
      '# reste d\'une session interrompue (/reload, arrêt du serveur) : tout est retiré avant', 'function mg:terra/clear', 'function mg:terra/shop_fix',
      'execute as @a[tag=mg.tvw] run function mg:terra/mis_clear', 'function mg:terra/rules',
      f'summon minecraft:marker {EXITA[0] + 0.5} 65 {EXITA[1] + 0.5} {{Tags:["mg.tv","mg.tvexit"]}}',
      tdisp(0.5, 73, 0.5, [{'text': 'TERRA NOVA\n', 'color': 'green', 'bold': True}, {'text': 'Colonie humaine · il y a 85 millions d\'années', 'color': 'gray', 'bold': False}], 3.0),
      tdisp(-7.4, 70.4, -17.5, {'text': '🛒 DÉPÔT D\'ÉQUIPEMENT', 'color': 'aqua', 'bold': True}, 1.3),
      tdisp(9.4, 71.4, -17.5, {'text': '🏛 QG DE COMMANDEMENT', 'color': 'gold', 'bold': True}, 1.3),
      tdisp(7.4, 70.6, 17.5, [{'text': '✚ INFIRMERIE\n', 'color': 'red', 'bold': True}, {'text': 'reste à l\'intérieur pour te soigner', 'color': 'gray', 'bold': False}], 1.3),
      tdisp(EXITA[0] + 0.5, 72.6, EXITA[1] + 0.5, [{'text': '🌀 Portail du temps\n', 'color': 'light_purple', 'bold': True}, {'text': 'retour au spawn', 'color': 'gray', 'bold': False}], 1.2),
      tdisp(0.5, 75.6, -WALL + 0.5, {'text': '🚪 PORTE NORD', 'color': 'yellow', 'bold': True}, 1.5),
      tdisp(0.5, 75.6, WALL + 0.5, {'text': '🚪 PORTE SUD', 'color': 'yellow', 'bold': True}, 1.5),
      f'summon minecraft:text_display 8.4 67.4 -22.5 {{Tags:["mg.tv"],Rotation:[90f,0f],text:{js([{"text": "📋 MISSIONS\n", "color": "gold", "bold": True}, {"text": "clic droit sur le tableau", "color": "gray", "bold": False}])},background:-1442840576,{TR % (0, 0, 0, 1.2, 1.2, 1.2)}}}',
      'summon minecraft:interaction 8.8 65 -22.5 {Tags:["mg.tv","mg.tvboard"],width:2.6f,height:3.2f,response:1b}',
      'summon minecraft:villager -15.5 65 -23.5 {Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[0f,0f],'
      'VillagerData:{profession:"minecraft:weaponsmith",level:5,type:"minecraft:jungle"},Offers:{Recipes:[]},'
      f'CustomName:{js({"text": "🛒 Intendant", "color": "gold"})},CustomNameVisible:1b}}',
      'summon minecraft:villager 20.5 65 17.5 {Tags:["mg.tv"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,Rotation:[90f,0f],'
      'VillagerData:{profession:"minecraft:cleric",level:5,type:"minecraft:jungle"},Offers:{Recipes:[]},'
      f'CustomName:{js({"text": "✚ Médecin", "color": "red"})},CustomNameVisible:1b}}']
for (x, key) in PADS:
    code, lab, col, price, it = PAD[key]
    SU += [f'summon minecraft:item_display {x + 0.5} 66.7 -21.5 {{Tags:["mg.tv","mg.tvpdi"],item:{{id:"{it}",count:1}},billboard:"fixed",{TR % (0, 0, 0, 0.7, 0.7, 0.7)}}}',
           tdisp(x + 0.5, 67.55, -21.5, [{'text': lab + '\n', 'color': col, 'bold': True}, {'text': f'{price} ₵', 'color': 'green', 'bold': False}], 0.45),
           f'summon minecraft:interaction {x + 0.5} 65 -21.5 {{Tags:["mg.tv","mg.tvbuy","mg.tvn"],width:1.2f,height:2.4f,response:1b}}',
           f'scoreboard players set @e[tag=mg.tvn,limit=1] mg.tvk {code}', 'tag @e[tag=mg.tvn] remove mg.tvn']
for k, (name, ox, oz) in enumerate(OUTPOSTS, 1):
    SU.append(tdisp(ox + 0.5, OUT_H[name] + 5, oz + 0.5, [{'text': f'📡 Outpost {name}\n', 'color': 'aqua', 'bold': True}, {'text': 'générateur de la colonie', 'color': 'gray', 'bold': False}], 1.2))
for (x, z) in SPAWNS:
    SU.append(f'summon minecraft:marker {x + 0.5} {top(x, z)} {z + 0.5} {{Tags:["mg.tv","mg.tvsp"{",\"mg.tvfar\"" if (x, z) in FAR else ""}]}}')
for (x, z) in HERBS:
    SU.append(f'summon minecraft:marker {x + 0.5} {top(x, z)} {z + 0.5} {{Tags:["mg.tv","mg.tvhp"]}}')
for i, (x, z) in enumerate(HERBS):
    SU.append(f'execute positioned {x + 0.5} {top(x, z)} {z + 0.5} run function mg:terra/dino/{"brachio" if i < 3 else "pachy"}')
SU += ['bossbar add mg:tvcarno {"text":"🦖 Carnotaure","color":"red"}', 'bossbar set mg:tvcarno color red', 'bossbar set mg:tvcarno style notched_10',
       'bossbar set mg:tvcarno max 160', 'bossbar set mg:tvcarno players']
for k, (name, _, _) in enumerate(OUTPOSTS, 1):
    SU += [f'bossbar add mg:tvo{k} {js({"text": f"🛡 Outpost {name}", "color": "aqua"})}', f'bossbar set mg:tvo{k} color blue',
           f'bossbar set mg:tvo{k} style notched_10', f'bossbar set mg:tvo{k} max 100', f'bossbar set mg:tvo{k} players',
           f'scoreboard players set $tvo{k} mg.st 0']
SU += ['scoreboard players set $tvcc mg.st 90', 'scoreboard players set $tvpk mg.st 3', 'scoreboard players set $tvsu mg.st 1']
w('terra/setup_in', SU)

# ================================================================ dinosaures
INVIS = 'active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}]'


def attrs(**a):
    names = {'hp': 'max_health', 'spd': 'movement_speed', 'fol': 'follow_range', 'dmg': 'attack_damage', 'scale': 'scale',
             'step': 'step_height', 'kb': 'knockback_resistance', 'akb': 'attack_knockback', 'jump': 'jump_strength', 'armor': 'armor'}
    return 'attributes:[' + ','.join(f'{{id:"minecraft:{names[k]}",base:{v}}}' for k, v in a.items()) + ']'


TVD = dict(globals())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tv_dino_fn.py'), encoding='utf-8').read(), TVD)
w('terra/pack', ['# Meute de 2 ou 3 slashers ici, lancée sur le colon le plus proche hors de la colonie',
                 'tag @e[tag=mg.tvpk] remove mg.tvpk', 'execute store result score $tvn mg.st run random value 2..4', 'function mg:terra/pack_one',
                 'execute as @e[tag=mg.tvpk] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvout,gamemode=adventure,distance=..70]',
                 'tag @e[tag=mg.tvpk] remove mg.tvpk'])
w('terra/pack_one', ['function mg:terra/dino/raptor', 'tag @e[tag=mg.tvlast] add mg.tvpk', 'scoreboard players remove $tvn mg.st 1',
                     'execute if score $tvn mg.st matches 1.. run function mg:terra/pack_one'])
w('terra/pack_try', ['# Une meute sur un point d\'apparition entre 24 et 64 blocs d\'un colon (aucun à moins de 22)',
                     'scoreboard players set $tvpk mg.st 5', 'tag @e[tag=mg.trok] remove mg.trok',
                     'execute as @e[type=minecraft:marker,tag=mg.tvsp] at @s if entity @a[tag=mg.tvout,gamemode=adventure,distance=24..64] unless entity @a[tag=mg.tvw,distance=..22] run tag @s add mg.trok',
                     '# un seul point tiré parmi les points possibles (une condition « if score » serait évaluée pour tous avant la première apparition)',
                     'execute as @e[tag=mg.trok,sort=random,limit=1] at @s run function mg:terra/pack_at', 'tag @e[tag=mg.trok] remove mg.trok'])
w('terra/pack_at', ['scoreboard players set $tvf mg.st 1', 'function mg:terra/pack'])
w('terra/carno_try', ['# Une chance sur 90 par seconde : un carnotaure sauvage apparaît loin des colons',
                      'execute store result score $tvr mg.st run random value 0..89', 'execute unless score $tvr mg.st matches 0 run return 0',
                      'tag @e[tag=mg.trok] remove mg.trok',
                      'execute as @e[type=minecraft:marker,tag=mg.tvsp] at @s if entity @a[tag=mg.tvout,gamemode=adventure,distance=36..80] unless entity @a[tag=mg.tvw,distance=..30] run tag @s add mg.trok',
                      'execute as @e[tag=mg.trok,sort=random,limit=1] at @s run function mg:terra/carno_at', 'tag @e[tag=mg.trok] remove mg.trok'])
w('terra/carno_at', ['scoreboard players set $tvf mg.st 1', 'scoreboard players set $tvcc mg.st 240', 'function mg:terra/dino/carno',
                     'tellraw @a[tag=mg.tvw] {"text":"🦖 Un rugissement résonne dans la jungle… un carnotaure rôde.","color":"red"}',
                     'execute as @a[tag=mg.tvw] at @s run playsound minecraft:entity.ravager.roar hostile @s ~ ~ ~ 0.6 0.55'])
w('terra/brach_saddle', ['# @s : brachiosaure monté sans selle → sellé (sinon on ne peut pas le diriger)',
                         'item replace entity @s saddle with minecraft:saddle',
                         'execute on passengers run title @s actionbar ' + js({'text': '🦕 Brachiosaure sellé : Z/Q/S/D pour le diriger, espace = élan', 'color': 'yellow'})])
w('terra/herb_fill', ['# Toutes les 20 s : 3 brachiosaures et 4 pachycéphalosaures dans la jungle',
                      'execute store result score $tvn mg.st if entity @e[tag=mg.tvbrach]',
                      'execute if score $tvn mg.st matches ..2 as @e[type=minecraft:marker,tag=mg.tvhp,sort=random,limit=1] at @s unless entity @a[tag=mg.tvw,distance=..30] run function mg:terra/dino/brachio',
                      'execute store result score $tvn mg.st if entity @e[tag=mg.tvpachy]',
                      'execute if score $tvn mg.st matches ..3 as @e[type=minecraft:marker,tag=mg.tvhp,sort=random,limit=1] at @s unless entity @a[tag=mg.tvw,distance=..30] run function mg:terra/dino/pachy'])
w('terra/zap', ['# @s (prédateur entré dans la colonie) : les tourelles du périmètre le frappent et le repoussent',
                'damage @s 10 minecraft:lightning_bolt', 'particle minecraft:electric_spark ~ ~1 ~ 0.4 0.8 0.4 0.3 30',
                'playsound minecraft:entity.lightning_bolt.impact hostile @a ~ ~ ~ 0.5 1.6',
                'execute facing 0 65 0 rotated ~180 -20 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:terra/vec {d:1.2}',
                'function mg:terra/push'])
w('terra/vec', ['# Marqueur placé au bout du vecteur (contexte : origine, orientation voulue)', '$tp @s ^ ^ ^$(d)', 'tag @s add mg.tvv'])
w('terra/push', ['# @s : élan = vecteur du marqueur mg.tvv', 'data modify entity @s Motion set from entity @e[type=minecraft:marker,tag=mg.tvv,limit=1] Pos',
                 'kill @e[type=minecraft:marker,tag=mg.tvv]'])
w('terra/carno_smash', ['# @s (carnotaure) : casse les structures légères autour de lui (outposts)',
                        'execute store result score $tvb2 mg.st run fill ~-2 ~ ~-2 ~2 ~3 ~2 minecraft:air replace #mg:tv_light',
                        'execute if score $tvb2 mg.st matches 1.. run playsound minecraft:entity.zombie.break_wooden_door hostile @a ~ ~ ~ 1 0.7',
                        'execute if score $tvb2 mg.st matches 1.. run particle minecraft:block{block_state:"minecraft:oak_planks"} ~ ~1 ~ 1 1 1 0 30'])
w('terra/carno_bar', ['# @s (carnotaure) : barre de vie pour les colons proches',
                      'execute store result bossbar mg:tvcarno value run data get entity @s Health',
                      'bossbar set mg:tvcarno players @a[tag=mg.tvw,distance=..48]'])
w('terra/unnet', ['# @s : fin d\'immobilisation (filet, piège)', 'data merge entity @s {NoAI:0b}', 'tag @s remove mg.tvnetted',
                  'scoreboard players operation $tvi mg.st = @s mg.tvid',
                  'execute as @e[type=minecraft:block_display,tag=mg.tvnetd] if score @s mg.tvid = $tvi mg.st run kill @s'])
w('terra/net_on', ['# @s (dinosaure) : pris dans un filet (5 s, carnotaure 2,5 s, brachiosaure 3 s)',
                   'scoreboard players set @s mg.tvst 100', 'execute if entity @s[tag=mg.tvcarno] run scoreboard players set @s mg.tvst 50',
                   'execute if entity @s[tag=mg.tvbig] run scoreboard players set @s mg.tvst 60',
                   'data merge entity @s {NoAI:1b}', 'tag @s add mg.tvnetted', 'scoreboard players operation $tvi mg.st = @s mg.tvid',
                   'execute as @e[type=minecraft:block_display,tag=mg.tvnetd] if score @s mg.tvid = $tvi mg.st run kill @s',
                   'execute unless entity @s[tag=mg.tvcarno] unless entity @s[tag=mg.tvbig] run ' + part('"mg.tv","mg.tvp","mg.tvnetd","mg.tvn"', 'cobweb', -0.8, 0, -0.8, 1.6, 1.8, 1.6),
                   'execute if entity @s[tag=mg.tvcarno] run ' + part('"mg.tv","mg.tvp","mg.tvnetd","mg.tvn"', 'cobweb', -1.4, 0, -1.4, 2.8, 3.4, 2.8),
                   'execute if entity @s[tag=mg.tvbig] run ' + part('"mg.tv","mg.tvp","mg.tvnetd","mg.tvn"', 'cobweb', -2.0, 0, -2.0, 4.0, 5.0, 4.0),
                   'scoreboard players operation @e[tag=mg.tvn] mg.tvid = $tvi mg.st', 'tag @e[tag=mg.tvn] remove mg.tvn',
                   'playsound minecraft:block.wool.place hostile @a ~ ~ ~ 1 0.6', 'particle minecraft:block{block_state:"minecraft:cobweb"} ~ ~1 ~ 0.5 0.6 0.5 0 25'])

# ================================================================ armes
def gain(n, why, col='green'):
    return [f'scoreboard players add @s mg.tvc {n}', f'function mg:terra/rpg/xp {{n:{max(5, n // 2)}}}', 'scoreboard players set @s mg.tval 40',
            f'title @s actionbar [{{"text":"+{n} ₵ ","color":"{col}","bold":true}},{{"text":"{why}","color":"gray"}}]',
            'execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.6 1.2']


def say(msg, col='gray'):
    return ['scoreboard players set @s mg.tval 40', f'title @s actionbar {js({"text": msg, "color": col})}']


w('terra/use', ['# @s : clic droit avec un objet de Terra Nova',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:2}] run return run function mg:terra/fire2',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:3}] run return run function mg:terra/fire3',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:4}] run return run function mg:terra/sonic',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:5}] run return run function mg:terra/net_fire',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:6}] run return run function mg:terra/trap_use',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:9}] run return run function mg:terra/home',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:7}] run return run function mg:terra/fire7',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:8}] run return run function mg:terra/fire8',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:10}] run return run function mg:terra/rpg/scan',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:11}] run return run function mg:terra/rpg/whistle',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:14}] run return run function mg:terra/rpg/cl/use',
                'execute if items entity @s weapon.mainhand *[custom_data~{tv:15}] run return run function mg:terra/rpg/sheet'])
RCOL = {2: '0.35,0.75,1.0', 3: '1.0,0.7,0.2', 7: '0.8,0.3,1.0', 8: '1.0,1.0,0.4'}
for n, heat, cd, dmg in [(2, 140, 4, 5), (3, 90, 3, 7), (7, 60, 3, 11), (8, 45, 3, 16)]:
    w(f'terra/fire{n}', [f'# @s tire ({ {2: "fusil à impulsions", 3: "fusil Mk2", 7: "fusil à plasma Mk3", 8: "lance-foudre"}[n]}) : +{heat} de chaleur, surchauffe à 1000',
                         'execute if entity @s[tag=mg.tvoh] run return run playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.5 1.6',
                         'execute if score @s mg.tvcd matches 1.. run return 0',
                         f'scoreboard players set @s mg.tvcd {cd}', f'scoreboard players add @s mg.tvh {heat}',
                         f'execute if score @s mg.trcl matches 1 run scoreboard players remove @s mg.tvh {heat * 3 // 10}',
                         'execute if score @s mg.tvh matches 1000.. run function mg:terra/overheat',
                         f'playsound minecraft:entity.breeze.shoot player @a ~ ~ ~ 0.7 {1.9 if n == 2 else 1.6}' if n < 8 else
                         'playsound minecraft:item.trident.thunder player @a ~ ~ ~ 0.5 1.8',
                         'scoreboard players set $tvr mg.st 0', 'tag @s add mg.tvsh',
                         f'execute anchored eyes positioned ^ ^ ^0.6 run function mg:terra/ray{n}', 'tag @s remove mg.tvsh', 'tag @e[tag=mg.tvhitn] remove mg.tvhitn'])
    w(f'terra/ray{n}', ['# Un pas (0,5 bloc) du tir à impulsions',
                        f'particle minecraft:dust{{color:[{RCOL[n]}],scale:{0.7 if n < 7 else 1.0}}} ~ ~ ~ 0 0 0 0 1 force',
                        'scoreboard players add $tvr mg.st 1',
                        f'execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[tag=mg.tvtg,tag=!mg.tvhitn,dx=0,dy=0,dz=0,limit=1] positioned ~0.5 ~0.5 ~0.5 run {"" if n == 7 else "return run "}function mg:terra/hit{n}',
                        'execute unless block ~ ~ ~ #mg:tv_pass run return run particle minecraft:electric_spark ~ ~ ~ 0.1 0.1 0.1 0.2 6',
                        f'execute if score $tvr mg.st matches ..80 positioned ^ ^ ^0.5 run function mg:terra/ray{n}'])
    w(f'terra/hit{n}', ['# @s (dinosaure) touché par une impulsion' + (' (plasma : traverse)' if n == 7 else ''),
                        '# précision du tireur : +1 dégât tous les 2 points (chiffre affiché au-dessus de la cible)',
                        f'execute if entity @a[tag=mg.tvsh,scores={{mg.trs4=8..}}] run function mg:terra/hitd {{d:{dmg + 4}}}',
                        f'execute if entity @a[tag=mg.tvsh,scores={{mg.trs4=6..7}}] run function mg:terra/hitd {{d:{dmg + 3}}}',
                        f'execute if entity @a[tag=mg.tvsh,scores={{mg.trs4=4..5}}] run function mg:terra/hitd {{d:{dmg + 2}}}',
                        f'execute if entity @a[tag=mg.tvsh,scores={{mg.trs4=2..3}}] run function mg:terra/hitd {{d:{dmg + 1}}}',
                        f'execute unless entity @a[tag=mg.tvsh,scores={{mg.trs4=2..}}] run function mg:terra/hitd {{d:{dmg}}}', 'tag @s add mg.tvhitn',
                        'particle minecraft:electric_spark ~ ~1 ~ 0.3 0.6 0.3 0.5 30' if n == 8 else 'particle minecraft:crit ~ ~ ~ 0 0 0 0 1',
                        'particle minecraft:electric_spark ~ ~ ~ 0.2 0.2 0.2 0.3 10',
                        'execute as @a[tag=mg.tvsh] at @s run playsound minecraft:entity.arrow.hit_player player @s ~ ~ ~ 0.4 1.5'])
w('terra/hitd', ['# @s (cible) : dégâts du tir ($(d)) et chiffre flottant', '$damage @s $(d) minecraft:player_attack by @a[tag=mg.tvsh,limit=1]',
                 '$execute at @s run function mg:terra/rpg/dmgnum {d:$(d)}'])
w('terra/overheat', ['# @s : surchauffe, plus de tir avant refroidissement complet', 'tag @s add mg.tvoh', 'scoreboard players set @s mg.tvh 1000',
                     'playsound minecraft:block.fire.extinguish player @s ~ ~ ~ 0.8 1.2', 'scoreboard players set @s mg.tval 0'])
w('terra/cooled', ['# @s : fusil refroidi', 'tag @s remove mg.tvoh', 'playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 0.4 1.8'])
w('terra/sonic', ['# @s : canon sonique, onde en cône (sphère de 4,5 blocs centrée 4 blocs devant)',
                  'execute if score @s mg.tvsc matches 1.. run return run playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.5 1.4',
                  'scoreboard players set @s mg.tvsc 80', 'playsound minecraft:entity.warden.sonic_boom player @a ~ ~ ~ 1 1.3',
                  'execute anchored eyes positioned ^ ^ ^1.5 run particle minecraft:sonic_boom ~ ~ ~ 0 0 0 0 1 force',
                  'execute anchored eyes positioned ^ ^ ^3.5 run particle minecraft:sonic_boom ~ ~ ~ 0.4 0.3 0.4 0 2 force',
                  'execute anchored eyes positioned ^ ^ ^6 run particle minecraft:sonic_boom ~ ~ ~ 0.9 0.5 0.9 0 3 force',
                  'tag @s add mg.tvsrc',
                  'execute anchored eyes positioned ^ ^ ^4 as @e[tag=mg.tvtg,distance=..4.5] at @s run function mg:terra/sonic_hit',
                  'tag @s remove mg.tvsrc'])
w('terra/sonic_hit', ['# @s (dinosaure) pris dans l\'onde : dégâts, ralenti, repoussé (sauf les géants)',
                      'damage @s 3 minecraft:sonic_boom by @a[tag=mg.tvsrc,limit=1]', 'effect give @s minecraft:slowness 4 2 true',
                      'execute if entity @s[tag=mg.tvbig] run return 0',
                      'execute if entity @s[tag=mg.tvcarno] facing entity @a[tag=mg.tvsrc,limit=1] feet rotated ~180 -20 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:terra/vec {d:0.9}',
                      'execute unless entity @s[tag=mg.tvcarno] facing entity @a[tag=mg.tvsrc,limit=1] feet rotated ~180 -25 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:terra/vec {d:1.8}',
                      'function mg:terra/push'])
w('terra/prod_hit', ['# @s a frappé avec le bâton électrique : le dinosaure visé est étourdi',
                     'execute anchored eyes positioned ^ ^ ^1.8 as @e[tag=mg.tvtg,distance=..2.4,sort=nearest,limit=1] at @s run function mg:terra/stun'])
w('terra/stun', ['# @s (dinosaure) : étourdi 3 s', 'effect give @s minecraft:slowness 3 4 true', 'effect give @s minecraft:weakness 3 1 true',
                 'particle minecraft:electric_spark ~ ~1 ~ 0.3 0.6 0.3 0.25 25', 'playsound minecraft:item.trident.thunder player @a ~ ~ ~ 0.25 2'])
w('terra/net_fire', ['# @s : lance-filets (un filet par tir)',
                     'execute if score @s mg.tvnet matches ..0 run return run function mg:terra/no_net',
                     'scoreboard players remove @s mg.tvnet 1', 'playsound minecraft:entity.fishing_bobber.throw player @a ~ ~ ~ 1 0.6',
                     'scoreboard players set $tvr mg.st 0', 'execute anchored eyes positioned ^ ^ ^0.6 run function mg:terra/net_ray'])
w('terra/no_net', say('🕸 Plus de filets : achète-en au dépôt de la colonie', 'red') + ['playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.5 1.2'])
w('terra/net_ray', ['# Un pas (0,5 bloc) du filet', 'particle minecraft:block{block_state:"minecraft:cobweb"} ~ ~ ~ 0.05 0.05 0.05 0 2',
                    'scoreboard players add $tvr mg.st 1',
                    'execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[tag=mg.tvtg,tag=!mg.tvnetted,dx=0,dy=0,dz=0,limit=1] at @s run return run function mg:terra/net_on',
                    'execute unless block ~ ~ ~ #mg:tv_pass run return 0',
                    'execute if score $tvr mg.st matches ..48 positioned ^ ^ ^0.5 run function mg:terra/net_ray'])
w('terra/trap_use', ['# @s : pose un piège à ses pieds (hors de la colonie, 4 actifs au plus)',
                     'execute if score @s mg.tvtr matches ..0 run return run function mg:terra/no_trap',
                     'execute unless entity @s[tag=mg.tvout] run return run function mg:terra/trap_here',
                     'execute if block ~ ~-0.3 ~ #mg:tv_pass run return run function mg:terra/trap_air',
                     'scoreboard players operation $own mg.st = @s mg.tvpid', 'scoreboard players set $tvn mg.st 0',
                     'execute as @e[type=minecraft:marker,tag=mg.tvtrap] if score @s mg.tvo = $own mg.st run scoreboard players add $tvn mg.st 1',
                     'execute if score $tvn mg.st matches 4.. unless score @s mg.trcl matches 4 run return run function mg:terra/trap_max',
                     'execute if score $tvn mg.st matches 8.. run return run function mg:terra/trap_max',
                     'scoreboard players remove @s mg.tvtr 1', 'execute align xyz positioned ~0.5 ~ ~0.5 run function mg:terra/trap_new'])
w('terra/no_trap', say('⚙ Plus de pièges : achète-en au dépôt de la colonie', 'red'))
w('terra/trap_here', say('⚙ Pas de pièges dans la colonie : pose-les dans la jungle', 'yellow'))
w('terra/trap_air', say('⚙ Pose le piège au sol', 'yellow'))
w('terra/trap_max', say('⚙ 4 pièges posés au plus : attends qu\'ils servent', 'yellow'))
w('terra/trap_new', ['# Piège ici (propriétaire $own)', 'scoreboard players add $tvid mg.st 1',
                     'summon minecraft:marker ~ ~ ~ {Tags:["mg.tv","mg.tvtrap","mg.tvn"]}',
                     part('"mg.tv","mg.tvtrapd","mg.tvn"', 'heavy_weighted_pressure_plate', -0.45, 0, -0.45, 0.9, 1.0, 0.9),
                     part('"mg.tv","mg.tvtrapd","mg.tvn"', 'iron_bars', -0.4, 0.02, -0.38, 0.8, 0.22, 0.1),
                     part('"mg.tv","mg.tvtrapd","mg.tvn"', 'iron_bars', -0.4, 0.02, 0.28, 0.8, 0.22, 0.1),
                     'scoreboard players operation @e[tag=mg.tvn] mg.tvid = $tvid mg.st', 'scoreboard players operation @e[tag=mg.tvn] mg.tvo = $own mg.st',
                     'tag @e[tag=mg.tvn] remove mg.tvn', 'playsound minecraft:block.chain.place player @a ~ ~ ~ 0.8 0.8'])
w('terra/trap_fire', ['# @s (piège) : un prédateur marche dessus : bloqué 6 s (carnotaure 2,5 s), 4 dégâts',
                      'scoreboard players operation $tvti mg.st = @s mg.tvid',
                      'execute as @e[tag=mg.tvhos,tag=!mg.tvnetted,distance=..1.4,sort=nearest,limit=1] at @s run function mg:terra/trap_hit',
                      'execute as @e[type=minecraft:block_display,tag=mg.tvtrapd] if score @s mg.tvid = $tvti mg.st run kill @s',
                      'playsound minecraft:block.chain.break hostile @a ~ ~ ~ 1 0.6', 'particle minecraft:crit ~ ~0.5 ~ 0.4 0.3 0.4 0.2 15', 'kill @s'])
w('terra/trap_hit', ['damage @s 4 minecraft:generic', 'function mg:terra/net_on', 'execute unless entity @s[tag=mg.tvcarno] run scoreboard players set @s mg.tvst 120'])
w('terra/home', ['# @s : rappel à la colonie (5 s, annulé par un coup)',
                 'execute if entity @s[tag=mg.tvcar] run return run function mg:terra/home_no_crate',
                 'execute unless entity @s[tag=mg.tvout] run return run function mg:terra/home_here',
                 'execute if score @s mg.tvhm matches 1.. run return 0',
                 'scoreboard players set @s mg.tvhm 100', 'scoreboard players set @s mg.tvdt 0',
                 'tellraw @s {"text":"📡 Rappel à la colonie dans 5 s… ne prends pas de coup !","color":"green"}',
                 'playsound minecraft:block.beacon.activate player @s ~ ~ ~ 0.6 1.6'])
w('terra/home_no_crate', say('📦 Impossible avec la caisse : rapporte-la à pied !', 'red'))
w('terra/home_here', say('Tu es déjà dans la colonie.', 'gray'))
w('terra/home_tick', ['# @s attend son rappel (5 s) : un coup reçu annule',
                      'execute if score @s mg.tvdt matches 1.. run scoreboard players set @s mg.tvhm 0',
                      'execute if score @s mg.tvdt matches 1.. run return run title @s actionbar {"text":"✖ Rappel annulé : tu as pris un coup !","color":"red","bold":true}',
                      'scoreboard players remove @s mg.tvhm 1',
                      'scoreboard players operation $tvs mg.st = @s mg.tvhm', 'scoreboard players add $tvs mg.st 19', 'scoreboard players set #20 mg.st 20',
                      'scoreboard players operation $tvs mg.st /= #20 mg.st',
                      'title @s actionbar [{"text":"📡 Rappel à la colonie dans ","color":"green"},{"score":{"name":"$tvs","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"green"}]',
                      'execute if score @s mg.tvhm matches 0 run function mg:terra/home_go'])
w('terra/home_go', ['# @s : de retour sur la place de la colonie', f'tp @s {SPAWN[0]} {SPAWN[1]} {SPAWN[2]}',
                    'execute at @s run playsound minecraft:entity.enderman.teleport player @a ~ ~ ~ 0.6 1.2',
                    'execute at @s run particle minecraft:reverse_portal ~ ~1 ~ 0.4 0.8 0.4 0.05 40'])

# ================================================================ boutique, tableau des missions
BUY = ['# @s (joueur) achète au présentoir $tvk : prix, conditions, objet',
       'scoreboard players set $tvp mg.st 0'] + [f'execute if score $tvk mg.st matches {c} run scoreboard players set $tvp mg.st {p}' for (c, _, _, p, _) in PAD.values()] + [
       'execute if score $tvk mg.st matches 1 if items entity @s container.* *[custom_data~{tv:4}] run return run function mg:terra/buy_has',
       'execute if score $tvk mg.st matches 2 if score @s mg.trwp matches 2.. run return run function mg:terra/buy_has',
       'execute if score $tvk mg.st matches 3 if items entity @s container.* *[custom_data~{tv:5}] run return run function mg:terra/buy_has_net',
       'execute if score $tvk mg.st matches 4 unless items entity @s container.* *[custom_data~{tv:5}] run return run function mg:terra/buy_need_net',
       'execute if score $tvk mg.st matches 7 if score @s mg.trar matches 1.. run return run function mg:terra/buy_has',
       'execute if score @s mg.tvc < $tvp mg.st run return run function mg:terra/buy_poor',
       'scoreboard players operation @s mg.tvc -= $tvp mg.st',
       'execute if score $tvk mg.st matches 1 run give @s ' + SONIC,
       'execute if score $tvk mg.st matches 2 run clear @s ' + WF + '[minecraft:custom_data~{tv:2}]',
       'execute if score $tvk mg.st matches 2 run give @s ' + RIFLE2, 'execute if score $tvk mg.st matches 2 run scoreboard players set @s mg.trwp 2',
       'execute if score $tvk mg.st matches 3 run give @s ' + NETL,
       'execute if score $tvk mg.st matches 3..4 run scoreboard players add @s mg.tvnet 3',
       'execute if score $tvk mg.st matches 5 unless items entity @s container.* *[custom_data~{tv:6}] run give @s ' + TRAP,
       'execute if score $tvk mg.st matches 5 run scoreboard players add @s mg.tvtr 3',
       'execute if score $tvk mg.st matches 6 run give @s ' + MEDK + ' 2',
       f'execute if score $tvk mg.st matches 7 run item replace entity @s armor.head with {ARM["head"]}',
       f'execute if score $tvk mg.st matches 7 run item replace entity @s armor.chest with {ARM["chest"]}',
       f'execute if score $tvk mg.st matches 7 run item replace entity @s armor.legs with {ARM["legs"]}',
       'execute if score $tvk mg.st matches 7 run scoreboard players set @s mg.trar 1',
       f'execute if score $tvk mg.st matches 8 run give @s {SADDLE}',
       'scoreboard players set @s mg.tval 50',
       'title @s actionbar [{"text":"✔ Acheté ! ","color":"green","bold":true},{"text":"reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.tvc"},"color":"yellow"},{"text":" ₵","color":"yellow"}]',
       'execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1']
w('terra/buy', BUY)
w('terra/buy_int', ['# @s (présentoir) : le colon qui a cliqué achète', 'scoreboard players operation $tvk mg.st = @s mg.tvk',
                    'execute on target if entity @s[tag=mg.tvw] run function mg:terra/buy', 'data remove entity @s interaction'])
w('terra/buy_has', say('Tu l\'as déjà !', 'yellow'))
w('terra/buy_has_net', say('Tu as déjà un lance-filets : prends les filets ×3 à côté', 'yellow'))
w('terra/buy_need_net', say('Il te faut d\'abord un lance-filets', 'yellow'))
w('terra/buy_poor', say('Pas assez de crédits ₵ : fais des missions !', 'red') + ['execute at @s run playsound minecraft:entity.villager.no player @s ~ ~ ~ 0.8 1'])


def mbtn(label, col, tip, n):
    return {'label': [{'text': label, 'color': col, 'bold': True}], 'tooltip': [{'text': tip, 'color': 'gray'}],
            'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.tvms set {n}'}}


BOARD = {'type': 'minecraft:multi_action', 'title': {'text': '📋 Missions de la colonie', 'color': 'gold', 'bold': True},
         'external_title': {'text': '📋 Missions', 'color': 'gold'}, 'pause': False, 'can_close_with_escape': True, 'columns': 1,
         'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': 'Une mission à la fois. Le 📡 localisateur (case 9) indique l\'objectif.\n'
                                                                                'Les autres colons peuvent t\'aider.', 'color': 'gray'}]}],
         'actions': [mbtn('📦 Récupération de matériel — 150 ₵', 'yellow', 'Une caisse larguée dans la jungle : trouve-la, ramasse-la (accroupi 3 s) et rapporte-la à la colonie', 1),
                     mbtn('🛡 Défense d\'outpost — 250 ₵', 'aqua', 'Rejoins l\'outpost attaqué et protège son générateur pendant 90 s', 2),
                     mbtn('🦖 Chasse : 5 slashers — 200 ₵', 'green', 'Abats 5 slashers dans la jungle', 3),
                     mbtn('🦖 Chasse : le carnotaure — 400 ₵', 'red', 'Un carnotaure rôde : suis le localisateur et abats-le', 4),
                     mbtn('✖ Abandonner ma mission', 'gray', 'Annule la mission en cours', 9)]}
w('terra/board_int', ['# @s (tableau) : le colon qui a cliqué voit les missions',
                      'execute on target if entity @s[tag=mg.tvw] run function mg:terra/board', 'data remove entity @s interaction'])
MLINKS = [{'text': '📋 Missions : ', 'color': 'gold', 'bold': True}] + [
    {'text': f'[{a["label"][0]["text"]}] ', 'color': a['label'][0]['color'], 'bold': False,
     'click_event': {'action': 'run_command', 'command': a['action']['command'].replace('trigger', '/trigger')},
     'hover_event': {'action': 'show_text', 'value': a['tooltip'][0]['text']}} for a in BOARD['actions']]
w('terra/board', ['# @s : fenêtre des missions (sinon liens cliquables dans le chat)', 'scoreboard players enable @s mg.tvms',
                  'scoreboard players set $dlg mg.st 0', f'execute store success score $dlg mg.st run dialog show @s {js(BOARD)}',
                  'execute unless score $dlg mg.st matches 1 run tellraw @s ' + js(MLINKS),
                  'execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1'])
w('terra/mission_cmd', ['# @s : choix au tableau (trigger mg.tvms)',
                        'execute if score @s mg.tvms matches 9 run function mg:terra/abandon',
                        'execute if score @s mg.tvms matches 1..4 unless score @s mg.tvm matches 1.. at @s run playsound minecraft:block.note_block.bell player @s ~ ~ ~ 0.8 1.2',
                        'execute if score @s mg.tvms matches 1..4 unless score @s mg.tvm matches 1.. run title @s title {"text":"📋 Mission acceptée","color":"gold","bold":true}',
                        'execute if score @s mg.tvms matches 1..4 if score @s mg.tvm matches 1.. run tellraw @s {"text":"Tu as déjà une mission : termine-la ou abandonne-la au tableau.","color":"yellow"}',
                        'execute if score @s mg.tvms matches 1 unless score @s mg.tvm matches 1.. run function mg:terra/m1',
                        'execute if score @s mg.tvms matches 2 unless score @s mg.tvm matches 1.. run function mg:terra/m2',
                        'execute if score @s mg.tvms matches 3 unless score @s mg.tvm matches 1.. run function mg:terra/m3',
                        'execute if score @s mg.tvms matches 4 unless score @s mg.tvm matches 1.. run function mg:terra/m4',
                        'scoreboard players reset @s mg.tvms', 'scoreboard players enable @s mg.tvms'])
w('terra/abandon', ['# @s abandonne sa mission', 'execute unless score @s mg.tvm matches 1.. run return run tellraw @s {"text":"Pas de mission en cours.","color":"gray"}',
                    'function mg:terra/mis_clear', 'tellraw @s {"text":"✖ Mission abandonnée.","color":"gray"}'])
w('terra/mis_clear', ['# @s : plus de mission (caisse posée ou portée retirée, localisateur vers la colonie)',
                      'scoreboard players operation $own mg.st = @s mg.tvpid',
                      'execute as @e[tag=mg.tvcrate] if score @s mg.tvo = $own mg.st run kill @s',
                      'execute as @e[tag=mg.tvcarry] if score @s mg.tvo = $own mg.st run kill @s',
                      'tag @s remove mg.tvcar', 'effect clear @s minecraft:slowness',
                      'scoreboard players set @s mg.tvm 0', 'scoreboard players set @s mg.tvmp 0', 'scoreboard players set @s mg.tvmo 0',
                      'execute if entity @s[tag=mg.tvw] run function mg:terra/rpg/qloc'])

# ---------------------------------------------------------------- mission 1 : récupération de matériel
M1 = ['# @s : mission « Récupération de matériel » : une caisse sur un point au hasard',
      f'execute store result score $tvr mg.st run random value 0..{len(CRATES) - 1}']
M1 += [f'execute if score $tvr mg.st matches {i} run return run function mg:terra/m1_at {{x:{x},y:{top(x, z)},z:{z}}}' for i, (x, z) in enumerate(CRATES)]
w('terra/m1', M1)
w('terra/m1_at', ['# @s : caisse larguée en $(x) $(y) $(z)', 'scoreboard players operation $own mg.st = @s mg.tvpid',
                  f'$execute in {DIM} positioned $(x) $(y) $(z) run function mg:terra/crate_new',
                  'scoreboard players set @s mg.tvm 1', 'scoreboard players set @s mg.tvmp 0',
                  '$function mg:terra/loc {x:$(x),y:$(y),z:$(z)}',
                  'tellraw @s ' + js([{'text': '📦 Mission : ', 'color': 'yellow', 'bold': True},
                                       {'text': 'une caisse de matériel a été larguée dans la jungle. Suis le 📡, ramasse-la (accroupi 3 s) et rapporte-la à la colonie. ', 'color': 'gray'},
                                       {'text': '+150 ₵', 'color': 'green'}]),
                  'playsound minecraft:block.note_block.bell player @s ~ ~ ~ 0.8 1.2'])
w('terra/crate_new', ['# Caisse de matériel ici (propriétaire $own) : tonneau lumineux, faisceau, étiquette, marqueur',
                      f'summon minecraft:block_display ~ ~ ~ {{Tags:["mg.tv","mg.tvcrate","mg.tvn"],block_state:{{Name:"minecraft:barrel",Properties:{{facing:"up"}}}},Glowing:1b,glow_color_override:16755200,{TR % (-0.45, 0, -0.45, 0.9, 0.9, 0.9)}}}',
                      f'summon minecraft:block_display ~ ~ ~ {{Tags:["mg.tv","mg.tvcrate","mg.tvn"],block_state:{{Name:"minecraft:yellow_stained_glass"}},brightness:{{sky:15,block:15}},view_range:4f,{TR % (-0.1, 0.9, -0.1, 0.2, 30, 0.2)}}}',
                      f'summon minecraft:text_display ~ ~1.6 ~ {{Tags:["mg.tv","mg.tvcrate","mg.tvn"],billboard:"center",text:{js({"text": "📦 Matériel", "color": "yellow", "bold": True})},background:1140850688}}',
                      'summon minecraft:marker ~ ~ ~ {Tags:["mg.tv","mg.tvcrate","mg.tvcrm","mg.tvn"]}',
                      'scoreboard players operation @e[tag=mg.tvn] mg.tvo = $own mg.st', 'tag @e[tag=mg.tvn] remove mg.tvn'])
PICK = ['# @s (accroupi, mission 1) : ramassage de sa caisse (3 s, 12 × 5 ticks)', 'scoreboard players operation $own mg.st = @s mg.tvpid',
        'scoreboard players set $tvf mg.st 0',
        'execute as @e[type=minecraft:marker,tag=mg.tvcrm,distance=..2.5] if score @s mg.tvo = $own mg.st run scoreboard players set $tvf mg.st 1',
        'execute if score $tvf mg.st matches 0 run return run scoreboard players set @s mg.tvmp 0',
        'scoreboard players add @s mg.tvmp 1', 'scoreboard players set @s mg.tval 10']
for i in range(1, 13):
    PICK.append(f'execute if score @s mg.tvmp matches {i} run title @s actionbar [{{"text":"📦 Ramassage ","color":"yellow"}},{{"text":"{"▮" * i}","color":"green"}},{{"text":"{"▮" * (12 - i)}","color":"dark_gray"}}]')
PICK.append('execute if score @s mg.tvmp matches 12.. run function mg:terra/crate_pick')
w('terra/crate_try', PICK)
w('terra/crate_pick', ['# @s ramasse sa caisse : il la porte (ralenti), une meute flaire l\'odeur',
                       'execute as @e[tag=mg.tvcrate] if score @s mg.tvo = $own mg.st run kill @s',
                       'tag @s add mg.tvcar', 'scoreboard players set @s mg.tvmp 0', 'effect give @s minecraft:slowness infinite 0 true',
                       f'summon minecraft:item_display ~ ~2.2 ~ {{Tags:["mg.tv","mg.tvcarry","mg.tvn"],teleport_duration:1,item:{{id:"minecraft:barrel",count:1}},{TR % (0, 0, 0, 0.7, 0.7, 0.7)}}}',
                       'scoreboard players operation @e[tag=mg.tvn] mg.tvo = $own mg.st',
                       'tag @e[tag=mg.tvn] remove mg.tvn', 'function mg:terra/save_pos', LOC_HOME,
                       'title @s title {"text":"📦 Caisse récupérée","color":"yellow","bold":true}',
                       'title @s subtitle {"text":"Rapporte-la à la colonie !","color":"gray"}',
                       'playsound minecraft:block.barrel.open player @s ~ ~ ~ 1 0.8',
                       'execute as @e[type=minecraft:marker,tag=mg.tvsp,distance=16..48,sort=nearest,limit=1] at @s run function mg:terra/pack',
                       'tellraw @s {"text":"⚠ Des slashers ont flairé la caisse !","color":"red"}'])
w('terra/carry_tick', ['# @s porte sa caisse : elle flotte au-dessus de sa tête', 'scoreboard players operation $own mg.st = @s mg.tvpid',
                         'execute as @e[type=minecraft:item_display,tag=mg.tvcarry] if score @s mg.tvo = $own mg.st run tp @s ~ ~2.2 ~ ~ 0'])
w('terra/m1_done', ['# @s rapporte la caisse à la colonie'] + gain(150, 'matériel livré à la colonie', 'gold') +
  ['function mg:terra/mis_clear', 'title @s title {"text":"✔ Mission accomplie","color":"green","bold":true}',
   'title @s subtitle {"text":"+150 ₵ : matériel livré","color":"gray"}', 'playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1'])
w('terra/save_pos', ['execute store result score @s mg.tvx run data get entity @s Pos[0]', 'execute store result score @s mg.tvy run data get entity @s Pos[1]',
                     'execute store result score @s mg.tvz run data get entity @s Pos[2]'])
w('terra/crate_drop', ['# @s est mort en portant la caisse : elle retombe là où il était (dernière position connue)',
                       'execute store result storage mg:terra d.x int 1 run scoreboard players get @s mg.tvx',
                       'execute store result storage mg:terra d.y int 1 run scoreboard players get @s mg.tvy',
                       'execute store result storage mg:terra d.z int 1 run scoreboard players get @s mg.tvz',
                       'scoreboard players operation $own mg.st = @s mg.tvpid',
                       'execute as @e[tag=mg.tvcarry] if score @s mg.tvo = $own mg.st run kill @s',
                       'function mg:terra/crate_drop_at with storage mg:terra d', 'tag @s remove mg.tvcar', 'effect clear @s minecraft:slowness',
                       'function mg:terra/loc with storage mg:terra d',
                       'tellraw @s {"text":"📦 Tu as lâché la caisse là où tu es tombé (📡).","color":"yellow"}'])
w('terra/crate_drop_at', [f'$execute in {DIM} positioned $(x) $(y) $(z) run function mg:terra/crate_new'])

# ---------------------------------------------------------------- mission 2 : défense d'outpost
GEN = {}
WAVE = {}
for k, (name, ox, oz) in enumerate(OUTPOSTS, 1):
    GEN[k] = (ox + 0.5, OUT_H[name] + 1, oz + 0.5)
    pts = []
    for dx, dz in [(0, -16), (16, 0), (0, 16), (-16, 0)]:
        x, z = max(-HX + 8, min(HX - 9, ox + dx)), max(-HX + 8, min(HX - 9, oz + dz))
        pts.append((x + 0.5, top(x, z), z + 0.5))
    WAVE[k] = pts
M2 = ['# @s : mission « Défense d\'outpost » : un outpost libre (tiré au sort)', 'execute store result score $tvr mg.st run random value 1..3']
for k in range(1, 4):
    gx, gy, gz = GEN[k]
    M2.append(f'execute if score $tvr mg.st matches {k} if score $tvo{k} mg.st matches 0 run return run function mg:terra/m2_set {{k:{k},x:{int(gx)},y:{gy},z:{int(gz)},n:"{OUTPOSTS[k - 1][0]}"}}')
for k in range(1, 4):
    gx, gy, gz = GEN[k]
    M2.append(f'execute if score $tvo{k} mg.st matches 0 run return run function mg:terra/m2_set {{k:{k},x:{int(gx)},y:{gy},z:{int(gz)},n:"{OUTPOSTS[k - 1][0]}"}}')
M2.append('tellraw @s {"text":"🛡 Tous les outposts sont déjà attaqués : rejoins une défense en cours (barre bleue) !","color":"aqua"}')
w('terra/m2', M2)
w('terra/m2_set', ['scoreboard players set @s mg.tvm 2', '$scoreboard players set @s mg.tvmo $(k)', 'scoreboard players set @s mg.tvmp 0',
                   '$function mg:terra/loc {x:$(x),y:$(y),z:$(z)}',
                   '$tellraw @s [{"text":"🛡 Mission : ","color":"aqua","bold":true},{"text":"l\'outpost $(n) va être attaqué. Rejoins-le (📡) : la défense commence à ton arrivée près du générateur. Tiens 90 s ! ","color":"gray"},{"text":"+250 ₵","color":"green"}]',
                   'playsound minecraft:block.note_block.bell player @s ~ ~ ~ 0.8 1.2'])
DEF_SECOND = []
for k, (name, ox, oz) in enumerate(OUTPOSTS, 1):
    gx, gy, gz = GEN[k]
    at = f'x={gx},y={gy},z={gz}'
    DEF_SECOND += [f'execute if score $tvo{k} mg.st matches 0 if entity @a[tag=mg.tvw,scores={{mg.tvm=2,mg.tvmo={k}}},{at},distance=..8] run function mg:terra/d_start_{k}',
                   f'execute if score $tvo{k} mg.st matches 1 run function mg:terra/d_tick_{k}']
    w(f'terra/d_start_{k}', [f'# Défense de l\'outpost {name} : 90 s, vagues toutes les 15 s, carnotaure à mi-parcours',
                             f'scoreboard players set $tvo{k} mg.st 1', f'scoreboard players set $tvot{k} mg.st 90', f'scoreboard players set $tvoi{k} mg.st 100',
                             f'scoreboard players set $tvow{k} mg.st 3', f'scoreboard players set $tvoa{k} mg.st 0',
                             f'tellraw @a[tag=mg.tvw,{at},distance=..64] ' + js([{'text': f'⚠ Les dinosaures attaquent l\'outpost {name} ! ', 'color': 'red', 'bold': True},
                                                                                  {'text': 'Protège le générateur pendant 90 s.', 'color': 'gray'}]),
                             f'execute positioned {gx} {gy} {gz} as @a[tag=mg.tvw,distance=..64] at @s run playsound minecraft:event.raid.horn hostile @s ~ ~ ~ 0.8 1.2'])
    TICK_D = [f'# Défense de l\'outpost {name} : chaque seconde', f'scoreboard players remove $tvot{k} mg.st 1', f'scoreboard players remove $tvow{k} mg.st 1',
              f'execute if score $tvow{k} mg.st matches ..0 run function mg:terra/d_wave_{k}',
              f'execute if score $tvot{k} mg.st matches 45 unless entity @e[tag=mg.tvcarno] positioned {WAVE[k][0][0]} {WAVE[k][0][1]} {WAVE[k][0][2]} run function mg:terra/d_boss',
              f'execute store result score $tvc2 mg.st if entity @e[tag=mg.tvhos,{at},distance=..3.5]',
              'scoreboard players operation $tvc2 mg.st *= #4 mg.st', f'scoreboard players operation $tvoi{k} mg.st -= $tvc2 mg.st',
              f'execute if score $tvc2 mg.st matches 1.. run particle minecraft:electric_spark {gx} {gy + 1.5} {gz} 0.3 0.6 0.3 0.4 25',
              f'execute if score $tvc2 mg.st matches 1.. run playsound minecraft:entity.iron_golem.damage hostile @a {gx} {gy} {gz} 0.8 1.4',
              f'execute store result bossbar mg:tvo{k} value run scoreboard players get $tvoi{k} mg.st',
              f'bossbar set mg:tvo{k} name [{{"text":"🛡 Outpost {name} : générateur ","color":"aqua"}},{{"score":{{"name":"$tvoi{k}","objective":"mg.st"}},"color":"white","bold":true}},{{"text":" %  ·  ","color":"gray"}},{{"score":{{"name":"$tvot{k}","objective":"mg.st"}},"color":"yellow","bold":true}},{{"text":" s","color":"yellow"}}]',
              f'bossbar set mg:tvo{k} players @a[tag=mg.tvw,{at},distance=..56]',
              f'execute unless entity @a[tag=mg.tvw,{at},distance=..56] run scoreboard players add $tvoa{k} mg.st 1',
              f'execute if entity @a[tag=mg.tvw,{at},distance=..56] run scoreboard players set $tvoa{k} mg.st 0',
              f'execute if score $tvoa{k} mg.st matches 15.. run return run function mg:terra/d_fail_{k}',
              f'execute if score $tvoi{k} mg.st matches ..0 run return run function mg:terra/d_fail_{k}',
              f'execute if score $tvot{k} mg.st matches ..0 run function mg:terra/d_win_{k}']
    w(f'terra/d_tick_{k}', TICK_D)
    WV = [f'# Vague sur l\'outpost {name} : 2 slashers + 1 par colon présent (5 au plus)', f'scoreboard players set $tvow{k} mg.st 15',
          f'execute store result score $tvn mg.st if entity @a[tag=mg.tvw,{at},distance=..40]', 'scoreboard players add $tvn mg.st 2',
          'execute if score $tvn mg.st matches 6.. run scoreboard players set $tvn mg.st 5', f'function mg:terra/d_wave_one_{k}']
    w(f'terra/d_wave_{k}', WV)
    W1 = ['execute store result score $tvr mg.st run random value 0..3']
    W1 += [f'execute if score $tvr mg.st matches {i} positioned {x} {y} {z} run function mg:terra/d_raptor' for i, (x, y, z) in enumerate(WAVE[k])]
    W1 += ['scoreboard players remove $tvn mg.st 1', f'execute if score $tvn mg.st matches 1.. run function mg:terra/d_wave_one_{k}']
    w(f'terra/d_wave_one_{k}', W1)
    win = [f'# Outpost {name} tenu : récompenses, outpost réparé', f'scoreboard players set $tvo{k} mg.st 0', f'bossbar set mg:tvo{k} players',
           f'execute as @a[tag=mg.tvw,{at},distance=..40] unless entity @s[scores={{mg.tvm=2,mg.tvmo={k}}}] run function mg:terra/m2_help',
           f'execute as @a[tag=mg.tvw,scores={{mg.tvm=2,mg.tvmo={k}}},{at},distance=..40] run function mg:terra/m2_done',
           f'execute as @a[tag=mg.tvw,scores={{mg.tvm=2,mg.tvmo={k}}}] run function mg:terra/m2_late',
           f'function mg:terra/out_build_{k}',
           f'execute positioned {gx} {gy} {gz} run playsound minecraft:ui.toast.challenge_complete player @a[tag=mg.tvw,distance=..48] ~ ~ ~ 0.6 1']
    w(f'terra/d_win_{k}', win)
    fail = [f'# Outpost {name} perdu', f'scoreboard players set $tvo{k} mg.st 0', f'bossbar set mg:tvo{k} players',
            f'particle minecraft:explosion_emitter {gx} {gy + 1} {gz} 0 0 0 0 1 force', f'playsound minecraft:entity.generic.explode hostile @a {gx} {gy} {gz} 2 0.8',
            f'tellraw @a[tag=mg.tvw,{at},distance=..64] {js({"text": f"💥 Le générateur de l’outpost {name} est détruit !", "color": "red", "bold": True})}',
            f'execute as @a[tag=mg.tvw,scores={{mg.tvm=2,mg.tvmo={k}}}] run function mg:terra/m2_fail',
            f'function mg:terra/out_build_{k}']
    w(f'terra/d_fail_{k}', fail)
w('terra/d_raptor', ['# Slasher de vague (ici) lancé sur le colon le plus proche', 'function mg:terra/dino/raptor', 'tag @e[tag=mg.tvlast] add mg.tvwave',
                     'execute as @e[tag=mg.tvlast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..60]'])
w('terra/d_boss', ['# Carnotaure de défense (ici)', 'function mg:terra/dino/carno', 'scoreboard players set $tvcc mg.st 240',
                   'execute as @e[tag=mg.tvlast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..60]',
                   'tellraw @a[tag=mg.tvw,distance=..80] {"text":"🦖 Un carnotaure fonce sur l\'outpost !","color":"red","bold":true}',
                   'execute as @a[tag=mg.tvw,distance=..80] at @s run playsound minecraft:entity.ravager.roar hostile @s ~ ~ ~ 1 0.55'])
w('terra/m2_done', ['# @s a tenu l\'outpost'] + gain(250, 'outpost défendu', 'aqua') +
  ['function mg:terra/mis_clear', 'title @s title {"text":"✔ Outpost défendu","color":"aqua","bold":true}', 'title @s subtitle {"text":"+250 ₵","color":"green"}'])
w('terra/m2_help', ['# @s a aidé à défendre un outpost'] + gain(60, 'renfort à l\'outpost', 'aqua'))
w('terra/m2_late', ['# @s avait la mission mais était trop loin à la fin', 'function mg:terra/mis_clear',
                    'tellraw @s {"text":"🛡 L\'outpost a tenu sans toi : mission terminée sans récompense.","color":"gray"}'])
w('terra/m2_fail', ['function mg:terra/mis_clear', 'title @s title {"text":"✖ Mission échouée","color":"red","bold":true}',
                    'title @s subtitle {"text":"Le générateur est détruit","color":"gray"}'])

# ---------------------------------------------------------------- missions 3 et 4 : chasse
w('terra/m3', ['# @s : mission « Chasse : 5 slashers »', 'scoreboard players set @s mg.tvm 3', 'scoreboard players set @s mg.tvmp 0',
               'execute as @e[type=minecraft:marker,tag=mg.tvfar,sort=random,limit=1] run function mg:terra/mark_loc',
               'function mg:terra/loc with storage mg:terra h',
               'tellraw @s ' + js([{'text': '🦖 Mission : ', 'color': 'green', 'bold': True}, {'text': 'abats 5 slashers dans la jungle (le 📡 indique une zone de chasse). ', 'color': 'gray'},
                                    {'text': '+200 ₵', 'color': 'green'}])])
w('terra/mark_loc', ['# @s (entité) : sa position dans storage mg:terra h', 'execute store result storage mg:terra h.x int 1 run data get entity @s Pos[0]',
                     'execute store result storage mg:terra h.y int 1 run data get entity @s Pos[1]', 'execute store result storage mg:terra h.z int 1 run data get entity @s Pos[2]'])
w('terra/m3_done', ['# @s a abattu ses 5 slashers'] + gain(200, 'chasse réussie', 'green') +
  ['function mg:terra/mis_clear', 'title @s title {"text":"✔ Chasse réussie","color":"green","bold":true}', 'title @s subtitle {"text":"+200 ₵","color":"green"}'])
w('terra/m4', ['# @s : mission « Chasse : le carnotaure » (un carnotaure traqué, apparu loin de la colonie si besoin)', 'scoreboard players set @s mg.tvm 4',
               'execute unless entity @e[tag=mg.tvhunt] as @e[type=minecraft:marker,tag=mg.tvfar,sort=random,limit=1] at @s run function mg:terra/hunt_spawn',
               'function mg:terra/hunt_loc',
               'tellraw @s ' + js([{'text': '🦖 Mission : ', 'color': 'red', 'bold': True}, {'text': 'un carnotaure rôde. Suis le 📡 et abats-le (prends du renfort !). ', 'color': 'gray'},
                                    {'text': '+400 ₵', 'color': 'green'}])])
w('terra/hunt_spawn', ['function mg:terra/dino/carno', 'tag @e[tag=mg.tvlast] add mg.tvhunt', 'scoreboard players set $tvcc mg.st 240'])
w('terra/hunt_loc', ['# Localisateurs des chasseurs de carnotaure : vers le carnotaure traqué',
                     'execute as @e[tag=mg.tvhunt,limit=1] run function mg:terra/mark_loc',
                     'execute if entity @e[tag=mg.tvhunt] as @a[tag=mg.tvw,scores={mg.tvm=4}] run function mg:terra/loc with storage mg:terra h'])
w('terra/k_raptor', ['# @s a abattu mg.tvkr slasher(s) : 12 ₵ chacun, progression de la chasse', 'function mg:terra/rpg/k_raptor',
                     'scoreboard players operation $tvk2 mg.st = @s mg.tvkr', 'scoreboard players operation $tvk2 mg.st *= #12 mg.st',
                     'scoreboard players operation @s mg.tvc += $tvk2 mg.st', 'scoreboard players set @s mg.tval 30',
                     'title @s actionbar [{"text":"+","color":"green","bold":true},{"score":{"name":"$tvk2","objective":"mg.st"},"color":"green","bold":true},{"text":" ₵ ","color":"green","bold":true},{"text":"slasher abattu","color":"gray"}]',
                     'execute if score @s mg.tvm matches 3 run scoreboard players operation @s mg.tvmp += @s mg.tvkr',
                     'execute if score @s mg.tvm matches 3 if score @s mg.tvmp matches ..4 run tellraw @s [{"text":"🦖 Chasse : ","color":"green"},{"score":{"name":"@s","objective":"mg.tvmp"},"color":"yellow","bold":true},{"text":" / 5","color":"yellow"}]',
                     'scoreboard players set @s mg.tvkr 0',
                     'execute if score @s mg.tvm matches 3 if score @s mg.tvmp matches 5.. run function mg:terra/m3_done'])
w('terra/k_carno', ['# @s a abattu un carnotaure : 120 ₵ (+ mission de chasse), les autres chasseurs ont une part',
                    'scoreboard players set @s mg.tvkc 0', 'function mg:terra/rpg/k_carno'] + gain(120, 'carnotaure abattu !', 'gold') +
  ['tellraw @a[tag=mg.tvw] [{"text":"🦖 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" a abattu le carnotaure !","color":"red","bold":true}]',
   'execute if entity @e[tag=mg.tvhunt] run return 0',
   'tag @s add mg.tvkill',
   'execute if score @s mg.tvm matches 4 run function mg:terra/m4_done',
   'execute as @a[tag=mg.tvw,tag=!mg.tvkill,scores={mg.tvm=4}] run function mg:terra/m4_share', 'tag @s remove mg.tvkill'])
w('terra/m4_done', ['# @s a abattu le carnotaure traqué'] + gain(400, 'chasse au carnotaure réussie', 'gold') +
  ['function mg:terra/mis_clear', 'title @s title {"text":"✔ Carnotaure abattu","color":"gold","bold":true}', 'title @s subtitle {"text":"+400 ₵","color":"green"}',
   'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.7 1'])
w('terra/m4_share', ['# @s chassait aussi le carnotaure : une part de la prime'] + gain(150, 'part de la chasse au carnotaure', 'gold') + ['function mg:terra/mis_clear'])
w('terra/k_herb', ['# @s a tué un herbivore : braconnage, -25 ₵', 'scoreboard players set @s mg.tvkb 0', 'scoreboard players set @s mg.tvkg 0',
                   'scoreboard players remove @s mg.tvc 25', 'execute if score @s mg.tvc matches ..-1 run scoreboard players set @s mg.tvc 0',
                   'scoreboard players set @s mg.tval 50',
                   'title @s actionbar [{"text":"-25 ₵ ","color":"red","bold":true},{"text":"braconnage : les herbivores sont protégés","color":"gray"}]'])

# ================================================================ mort, entrées et sorties de la colonie, interface
w('terra/died', ['# @s est mort à Terra Nova (inventaire gardé) : -10 % de crédits, caisse lâchée', 'scoreboard players set @s mg.deaths 0', 'scoreboard players set #10 mg.st 10',
                 'execute if entity @s[tag=mg.tvcar] run function mg:terra/crate_drop',
                 'scoreboard players operation $tvl mg.st = @s mg.tvc', 'scoreboard players operation $tvl mg.st /= #10 mg.st',
                 'scoreboard players operation @s mg.tvc -= $tvl mg.st', 'scoreboard players set @s mg.tvhm 0', 'scoreboard players set @s mg.tvh 0',
                 'tag @s remove mg.tvoh', 'title @s times 5 40 15', 'title @s title {"text":"☠ DÉVORÉ","color":"dark_red","bold":true}',
                 'title @s subtitle [{"text":"Frais d\'infirmerie : -","color":"gray"},{"score":{"name":"$tvl","objective":"mg.st"},"color":"red"},{"text":" ₵","color":"red"}]'])
w('terra/gate', ['# Chaque seconde : qui est dans la colonie (tag mg.tvout = dehors), messages aux portes',
                 'tag @a[tag=mg.tvin2] remove mg.tvin2', f'tag @a[tag=mg.tvw,{COLONY_BOX}] add mg.tvin2',
                 'execute as @a[tag=mg.tvw,tag=mg.tvin2,tag=mg.tvout] run function mg:terra/gate_in',
                 'execute as @a[tag=mg.tvw,tag=!mg.tvin2,tag=!mg.tvout] run function mg:terra/gate_out'])
w('terra/gate_in', ['tag @s remove mg.tvout'] + say('🏠 De retour dans la colonie : tu es en sécurité', 'green') +
  ['execute at @s run playsound minecraft:block.note_block.chime player @s ~ ~ ~ 0.5 1.4'])
w('terra/gate_out', ['tag @s add mg.tvout'] + say('🌿 Tu quittes le périmètre : prudence, colon !', 'gold') +
  ['execute at @s run playsound minecraft:block.bell.use player @s ~ ~ ~ 0.5 0.8'])
HM = ['# @s : barre d\'action (crédits + mission)']
CRED = ('{"text":"⭐","color":"gold"},{"score":{"name":"@s","objective":"mg.trlv"},"color":"gold","bold":true},{"text":"  ","color":"gray"},'
        '{"score":{"name":"@s","objective":"mg.tvc"},"color":"yellow","bold":true},{"text":" ₵","color":"yellow"},{"text":"   ","color":"gray"}')
HM.append('execute if entity @s[scores={mg.tvm=0}] run return run function mg:terra/rpg/hud')
for cond, txt, col in [('scores={mg.tvm=1},tag=!mg.tvcar', '📦 Trouve la caisse (📡)', 'yellow'),
                       ('scores={mg.tvm=1},tag=mg.tvcar', '📦 Rapporte la caisse à la colonie !', 'gold'), ('scores={mg.tvm=2}', '🛡 Rejoins l\'outpost et défends-le (📡)', 'aqua'),
                       ('scores={mg.tvm=4}', '🦖 Traque le carnotaure (📡)', 'red')]:
    DST = ',{"text":"  📍 ","color":"gold"},{"score":{"name":"@s","objective":"mg.trod"},"color":"yellow","bold":true},{"text":" m","color":"gold"}'
    HM.append(f'execute if entity @s[{cond}] run return run title @s actionbar [{CRED},{{"text":"{txt}","color":"{col}"}}{DST}]')
HM.append(f'execute if entity @s[scores={{mg.tvm=3}}] run return run title @s actionbar [{CRED},{{"text":"🦖 Slashers : ","color":"green"}},{{"score":{{"name":"@s","objective":"mg.tvmp"}},"color":"white","bold":true}},{{"text":" / 5","color":"white"}}]')
w('terra/hud_main', HM)
HH = ['# @s tient un fusil à impulsions : jauge de chaleur',
      'execute if entity @s[tag=mg.tvoh] run return run title @s actionbar [{"text":"⚠ SURCHAUFFE ","color":"red","bold":true},{"text":"refroidissement…","color":"gray"}]']
for i in range(11):
    lo_, hi_ = i * 100, i * 100 + 99
    col = 'green' if i < 6 else ('gold' if i < 9 else 'red')
    HH.append(f'execute if score @s mg.tvh matches {lo_}..{hi_} run title @s actionbar [{{"text":"🔫 Chaleur ","color":"aqua"}},{{"text":"{"▮" * i}","color":"{col}"}},{{"text":"{"▮" * (10 - i)}","color":"dark_gray"}}]')
w('terra/hud_heat', HH)
w('terra/hud_one', ['# @s : barre d\'action selon l\'objet en main',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:2}] run return run function mg:terra/hud_heat',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:3}] run return run function mg:terra/hud_heat',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:7}] run return run function mg:terra/hud_heat',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:14}] if score @s mg.trcd matches 1.. run return run title @s actionbar {"text":"🎖 Capacité : recharge…","color":"gray"}',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:14}] run return run title @s actionbar {"text":"🎖 Capacité PRÊTE (clic droit)","color":"gold","bold":true}',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:8}] run return run function mg:terra/hud_heat',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:4}] if score @s mg.tvsc matches 1.. run return run title @s actionbar {"text":"📢 Canon sonique : recharge…","color":"gray"}',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:4}] run return run title @s actionbar {"text":"📢 Canon sonique : PRÊT (clic droit)","color":"aqua","bold":true}',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:5}] run return run title @s actionbar [{"text":"🕸 Filets : ","color":"white"},{"score":{"name":"@s","objective":"mg.tvnet"},"color":"yellow","bold":true}]',
                    'execute if items entity @s weapon.mainhand *[custom_data~{tv:6}] run return run title @s actionbar [{"text":"⚙ Pièges : ","color":"gray"},{"score":{"name":"@s","objective":"mg.tvtr"},"color":"yellow","bold":true},{"text":"  (clic droit : poser à tes pieds)","color":"gray"}]',
                    'execute if score @s mg.tvhm matches 1.. run return 0',
                    'function mg:terra/hud_main'])

# ================================================================ tick de la session (dans la dimension)
w('terra/tick', ['# 🦖 Terra Nova : chaque tick tant qu\'un joueur y est (contexte : dimension mg:terranova)', 'scoreboard players add $tvt mg.st 1',
                 'scoreboard players operation $tvq mg.st = $tvt mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $tvq mg.st %= #20 mg.st',
                 # objets
                 'execute as @a[tag=mg.tvw,scores={mg.tvq=1..}] at @s run function mg:terra/use',
                 'scoreboard players reset @a[scores={mg.tvq=1..}] mg.tvq',
                 'execute as @a[tag=mg.tvw,scores={mg.tvdd=1..}] if items entity @s weapon.mainhand *[custom_data~{tv:1}] at @s run function mg:terra/prod_hit',
                 'execute as @a[tag=mg.tvw,scores={mg.tvdd=1..}] if items entity @s weapon.mainhand *[custom_data~{tv:12}] at @s run function mg:terra/prod_hit',
                 'execute as @a[tag=mg.tvw,scores={mg.tvdd=1..}] if items entity @s weapon.mainhand *[custom_data~{tv:13}] at @s run function mg:terra/prod_hit',
                 'scoreboard players reset @a[scores={mg.tvdd=1..}] mg.tvdd',
                 'scoreboard players remove @a[tag=mg.tvw,scores={mg.tvh=1..}] mg.tvh 15',
                 'scoreboard players set @a[tag=mg.tvw,scores={mg.tvh=..-1}] mg.tvh 0',
                 'execute as @a[tag=mg.tvoh,scores={mg.tvh=0}] run function mg:terra/cooled',
                 'scoreboard players remove @a[tag=mg.tvw,scores={mg.tvcd=1..}] mg.tvcd 1',
                 'scoreboard players remove @a[tag=mg.tvw,scores={mg.tvsc=1..}] mg.tvsc 1',
                 'scoreboard players remove @a[tag=mg.tvw,scores={mg.tval=1..}] mg.tval 1',
                 'execute as @a[tag=mg.tvw,scores={mg.tvhm=1..}] run function mg:terra/home_tick',
                 'execute as @a[tag=mg.tvw,scores={mg.tvms=1..}] run function mg:terra/mission_cmd',
                 'execute as @e[type=minecraft:interaction,tag=mg.tvbuy] if data entity @s interaction run function mg:terra/buy_int',
                 'execute as @e[type=minecraft:interaction,tag=mg.tvboard] if data entity @s interaction run function mg:terra/board_int',
                 'execute as @e[type=minecraft:item_display,tag=mg.tvpdi] at @s run tp @s ~ ~ ~ ~4 ~',
                 # dinosaures : modèles, filets, pièges
                 'scoreboard players operation $tvq3b mg.st = $tvt mg.st', 'scoreboard players set #3 mg.st 3', 'scoreboard players operation $tvq3b mg.st %= #3 mg.st',
                 'execute as @e[tag=mg.tvd] at @s if entity @a[tag=mg.tvw,distance=..32] run function mg:terra/dsync',
                 'execute as @e[tag=mg.tvd] if score @s mg.tvph = $tvq3b mg.st at @s unless entity @a[tag=mg.tvw,distance=..32] if entity @a[tag=mg.tvw,distance=..64] run function mg:terra/dsync',
                 'execute if score $tvq mg.st matches 0 as @e[tag=mg.tvd] at @s unless entity @a[tag=mg.tvw,distance=..64] run function mg:terra/dsync',
                 'execute if score $tvq mg.st matches 10 as @e[tag=mg.tvd] at @s unless entity @a[tag=mg.tvw,distance=..64] run function mg:terra/dsync',
                 'scoreboard players remove @e[tag=mg.tvd,scores={mg.tvst=1..}] mg.tvst 1',
                 'execute as @e[tag=mg.tvnetted,scores={mg.tvst=..0}] run function mg:terra/unnet',
                 'execute as @e[type=minecraft:marker,tag=mg.tvtrap] at @s if entity @e[tag=mg.tvhos,tag=!mg.tvnetted,distance=..1.4] run function mg:terra/trap_fire',
                 # caisse : ramassage (toutes les 5 ticks)
                 'scoreboard players operation $tvq5 mg.st = $tvt mg.st', 'scoreboard players set #5 mg.st 5', 'scoreboard players operation $tvq5 mg.st %= #5 mg.st',
                 'execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw,scores={mg.tvm=1},tag=!mg.tvcar] at @s if predicate mg:sneak run function mg:terra/crate_try',
                 'execute if score $tvq5 mg.st matches 0 as @a[tag=mg.tvw,scores={mg.tvm=1,mg.tvmp=1..},tag=!mg.tvcar] unless predicate mg:sneak run scoreboard players set @s mg.tvmp 0',
                 # morts, sortie
                 'execute as @a[tag=mg.tvcar] at @s run function mg:terra/carry_tick',
                 'execute as @a[tag=mg.tvw,scores={mg.deaths=1..}] run function mg:terra/died',
                 f'particle minecraft:reverse_portal {EXITA[0] + 0.5} 67 {EXITA[1] + 0.5} 0.05 1.3 1.0 0.02 4',
                 'execute as @a[tag=mg.tvw] at @s if entity @e[type=minecraft:marker,tag=mg.tvexit,distance=..1.4] in minecraft:overworld run function mg:terra/leave',
                 'execute if score $tvq mg.st matches 0 run function mg:terra/second',
                 'execute if score $tvq mg.st matches 5 as @a[tag=mg.tvw,scores={mg.tval=..0}] run function mg:terra/hud_one',
                 'execute if score $tvq mg.st matches 15 as @a[tag=mg.tvw,scores={mg.tval=..0}] run function mg:terra/hud_one',
                 'function mg:terra/rpg/tick'])
SEC = ['# Chaque seconde (dans la dimension) : colonie, soins, primes, missions, population de dinosaures, carnotaure',
       'execute unless score $tvsu mg.st matches 1.. run return 0',
       'execute if score $tvsu mg.st matches 2 run kill @e[tag=mg.tvp,tag=!mg.tvok]',
       'tag @e[tag=mg.tvok] remove mg.tvok', 'scoreboard players set $tvsu mg.st 2',
       'scoreboard players set #4 mg.st 4', 'scoreboard players set #10 mg.st 10', 'scoreboard players set #12 mg.st 12',
       'function mg:terra/gate',
       'scoreboard players enable @a[tag=mg.tvw] mg.tvms', 'effect give @a[tag=mg.tvw] minecraft:saturation infinite 0 true',
       'effect give @a[tag=mg.tvw,x=9,y=64,z=11,dx=14,dy=5,dz=12] minecraft:regeneration 3 2 true',
       # primes et missions
       'execute as @a[tag=mg.tvw,scores={mg.tvkr=1..}] run function mg:terra/k_raptor',
       'execute as @a[tag=mg.tvw,scores={mg.tvkc=1..}] run function mg:terra/k_carno',
       'execute as @a[tag=mg.tvw,scores={mg.tvkb=1..}] run function mg:terra/k_herb',
       'execute as @a[tag=mg.tvw,scores={mg.tvkg=1..}] run function mg:terra/k_herb',
       'execute as @a[tag=mg.tvcar] run function mg:terra/save_pos',
       'execute as @a[tag=mg.tvcar,tag=!mg.tvout] run function mg:terra/m1_done'] + DEF_SECOND + [
       'scoreboard players operation $tvq2 mg.st = $tvt mg.st', 'scoreboard players set #40 mg.st 40', 'scoreboard players operation $tvq2 mg.st %= #40 mg.st',
       'execute if score $tvq2 mg.st matches 0 if entity @a[tag=mg.tvw,scores={mg.tvm=4}] run function mg:terra/hunt_loc',
       'execute unless entity @a[tag=mg.tvw,scores={mg.tvm=4}] run tag @e[tag=mg.tvhunt] remove mg.tvhunt',
       'execute unless entity @e[tag=mg.tvhunt] if entity @a[tag=mg.tvw,scores={mg.tvm=4}] as @e[type=minecraft:marker,tag=mg.tvfar,sort=random,limit=1] at @s run function mg:terra/hunt_spawn',
       # population
       'execute store result score $tvno mg.st if entity @a[tag=mg.tvout,gamemode=adventure]',
       'execute store result score $tvnr mg.st if entity @e[tag=mg.tvraptor,tag=!mg.trr]',
       '# slashers de la vallée : 3 par colon dehors + 6 (20 au plus)',
       'scoreboard players operation $tvwr mg.st = $tvno mg.st', 'scoreboard players set #3 mg.st 3', 'scoreboard players operation $tvwr mg.st *= #3 mg.st',
       'scoreboard players add $tvwr mg.st 6', 'execute if score $tvwr mg.st matches 21.. run scoreboard players set $tvwr mg.st 20',
       'scoreboard players remove $tvpk mg.st 1', 'scoreboard players remove $tvcc mg.st 1',
       'execute if score $tvno mg.st matches 1.. if score $tvpk mg.st matches ..0 if score $tvnr mg.st < $tvwr mg.st run function mg:terra/pack_try',
       'execute if score $tvno mg.st matches 1.. if score $tvcc mg.st matches ..0 unless entity @e[tag=mg.tvcarno] run function mg:terra/carno_try',
       'scoreboard players operation $tvq3 mg.st = $tvt mg.st', 'scoreboard players set #60 mg.st 60', 'scoreboard players operation $tvq3 mg.st %= #60 mg.st',
       # traque : toutes les 3 s, un slasher sans proie proche « flaire » un colon dehors à moins de 56 blocs
       'execute if score $tvq3 mg.st matches 0 as @e[tag=mg.tvraptor,tag=!mg.tvnetted] at @s unless entity @a[tag=mg.tvout,distance=..14] if entity @a[tag=mg.tvout,gamemode=adventure,distance=..56] run damage @s 0.01 minecraft:generic by @p[tag=mg.tvout,gamemode=adventure,distance=..56]',
       'scoreboard players operation $tvq4 mg.st = $tvt mg.st', 'scoreboard players set #400 mg.st 400', 'scoreboard players operation $tvq4 mg.st %= #400 mg.st',
       'execute if score $tvq4 mg.st matches 0 run function mg:terra/herb_fill',
       'execute if score $tvq4 mg.st matches 200 as @e[tag=mg.tvhos,tag=!mg.tvhunt] at @s unless entity @a[tag=mg.tvw,distance=..80] run tp @s ~ -400 ~',
       # défenses du périmètre, herbivores égarés
       f'execute as @e[tag=mg.tvhos,{COLONY_BOX}] at @s run function mg:terra/zap',
       f'execute as @e[tag=mg.tvherb,{COLONY_BOX}] unless predicate mg:has_passenger run tp @s @e[type=minecraft:marker,tag=mg.tvhp,sort=random,limit=1]',
       # brachiosaure monté sans selle (impossible à diriger) : sellé d'office
       'execute as @e[tag=mg.tvbrach] if predicate mg:has_passenger unless items entity @s saddle minecraft:saddle run function mg:terra/brach_saddle',
       # carnotaure
       f'execute as @e[tag=mg.tvcarno,tag=!mg.tvnetted] at @s unless entity @s[{COLONY_BOX}] run function mg:terra/carno_smash',
       'execute unless entity @e[tag=mg.tvcarno] run bossbar set mg:tvcarno players',
       'execute as @e[tag=mg.tvhunt,limit=1] at @s run function mg:terra/carno_bar',
       'execute unless entity @e[tag=mg.tvhunt] as @e[tag=mg.tvcarno,limit=1] at @s run function mg:terra/carno_bar',
       # ambiance
       'execute store result score $tvr mg.st run random value 0..29',
       'execute if score $tvr mg.st matches 0..9 as @e[tag=mg.tvraptor,sort=random,limit=1] at @s run playsound minecraft:entity.fox.screech hostile @a ~ ~ ~ 1.2 0.75',
       'execute if score $tvr mg.st matches 10..12 as @e[tag=mg.tvcarno,sort=random,limit=1] at @s run playsound minecraft:entity.ravager.roar hostile @a ~ ~ ~ 2 0.6',
       'execute if score $tvr mg.st matches 13..15 as @e[tag=mg.tvbrach,sort=random,limit=1] at @s run playsound minecraft:entity.camel.ambient neutral @a ~ ~ ~ 2.5 0.45',
       'execute if score $tvr mg.st matches 16..17 as @e[tag=mg.tvpachy,sort=random,limit=1] at @s run playsound minecraft:entity.goat.ambient neutral @a ~ ~ ~ 1.2 0.6',
       'execute if score $tvr mg.st matches 18 as @a[tag=mg.tvout,sort=random,limit=1] at @s run playsound minecraft:entity.parrot.ambient ambient @s ~ ~8 ~ 0.6 0.8',
       '# RPG (régions, campagne, boss) ; dinosaures d\'une session précédente restés dans une zone non chargée : retirés',
       'function mg:terra/rpg/second',
       'execute as @e[tag=mg.tvd,tag=!mg.trmount] unless score @s mg.tvses = $tvses mg.st run tp @s ~ -400 ~']
w('terra/second', SEC)

# ================================================================ câblage
C.patch('core/tick', 'function mg:gta/lobby_tick', ['function mg:terra/lobby_tick'])
C.patch('core/tick', 'function mg:gta/pre_tick', ['function mg:terra/pre_tick'])
C.patch('survie/leave', 'execute if entity @s[tag=mg.gtw] run return run function mg:gta/leave',
        ['execute if entity @s[tag=mg.tvw] run return run function mg:terra/leave'])
C.patch('survie/cmd', 'execute if score @s mg.sv matches 4 run function mg:gta/menu_go', ['execute if score @s mg.sv matches 7 run function mg:terra/menu_go'])
_cmd = C.lines_of('survie/cmd')
if _cmd and '4 = Neo GTA,' in _cmd[0] and 'Terra Nova' not in _cmd[0]:
    _cmd[0] = _cmd[0].replace('4 = Neo GTA,', '4 = Neo GTA, 7 = Terra Nova,')
    C.w('survie/cmd', _cmd[:-1] if _cmd[-1] == '' else _cmd)
_pa = C.lines_of('core/pull_all')
_pa = [l.replace('tag @a[tag=mg.surv,tag=!mg.gtw] add mg.pulls', 'tag @a[tag=mg.surv,tag=!mg.gtw,tag=!mg.tvw] add mg.pulls') for l in _pa]
if 'tag @a[tag=mg.tvw] add mg.pullt' not in _pa:
    i = _pa.index('tag @a[tag=mg.gtw] add mg.pullg')
    _pa[i + 1:i + 1] = ['tag @a[tag=mg.tvw] add mg.pullt']
    j = _pa.index('execute as @a[tag=mg.pullg] in minecraft:overworld run function mg:gta/leave')
    _pa[j + 1:j + 1] = ['execute as @a[tag=mg.pullt] in minecraft:overworld run function mg:terra/leave']
C.w('core/pull_all', _pa[:-1] if _pa[-1] == '' else _pa)
C.patch('core/optout', 'execute if entity @s[tag=mg.pullg] in minecraft:overworld run function mg:gta/enter',
        ['execute if entity @s[tag=mg.pullt] in minecraft:overworld run function mg:terra/enter'])
C.patch('core/optout', 'tag @s remove mg.pullg', ['tag @s remove mg.pullt'])
C.patch('core/request', 'tag @a remove mg.pullg', ['tag @a remove mg.pullt'])
_st = C.lines_of('survie/tick')
_st = [l.replace('execute as @a[tag=mg.surv,tag=!mg.svg2,scores={mg.svid=1..}] run function mg:survie/regen_now',
                 'execute as @a[tag=mg.surv,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.svg2,scores={mg.svid=1..}] run function mg:survie/regen_now') for l in _st]
C.w('survie/tick', _st[:-1] if _st[-1] == '' else _st)
C.patch('desinstaller', 'execute if score $tmap mg.st matches 1 run function mg:lobby/theme/map/end',
        ['execute as @a[tag=mg.tvw] in minecraft:overworld run function mg:terra/leave'], where='before')
C.patch('core/load', 'execute unless score $rp mg.st matches 0..1 run scoreboard players set $rp mg.st 1',
        ['# Terra Nova : construite une fois (dimension mg:terranova, ~2 min, après Neo City), règles du monde',
         'execute if score $setup mg.st matches 1 unless data storage mg:terra built run schedule function mg:terra/world_build 200s',
         'execute if score $setup mg.st matches 1 unless data storage mg:lobby tvclean run schedule function mg:terra/spawn_clean 9s',
         'scoreboard players set $tvw mg.st 0', 'function mg:terra/rules'])
C.objectives([('mg.tvq', 'minecraft.used:minecraft.warped_fungus_on_a_stick'), ('mg.tvdd', 'minecraft.custom:minecraft.damage_dealt'),
              ('mg.tvdt', 'minecraft.custom:minecraft.damage_taken'), ('mg.tvkr', 'minecraft.killed:minecraft.vindicator'),
              ('mg.tvkc', 'minecraft.killed:minecraft.hoglin'), ('mg.tvkb', 'minecraft.killed:minecraft.camel'), ('mg.tvkg', 'minecraft.killed:minecraft.goat'),
              ('mg.tvms', 'trigger'), ('mg.tvpid', 'dummy'), ('mg.tvid', 'dummy'), ('mg.tvo', 'dummy'), ('mg.tvk', 'dummy'), ('mg.tvh', 'dummy'),
              ('mg.tvcd', 'dummy'), ('mg.tvsc', 'dummy'), ('mg.tvnet', 'dummy'), ('mg.tvtr', 'dummy'), ('mg.tvst', 'dummy'), ('mg.tvm', 'dummy'),
              ('mg.tvmo', 'dummy'), ('mg.tvmp', 'dummy'), ('mg.tvhm', 'dummy'), ('mg.tval', 'dummy'), ('mg.tvx', 'dummy'), ('mg.tvy', 'dummy'),
              ('mg.tvz', 'dummy')])
C.objectives([('mg.tvat', 'dummy'), ('mg.tvaf', 'dummy'), ('mg.tvas', 'dummy'), ('mg.tvses', 'dummy'), ('mg.tvak', 'dummy'), ('mg.tvab', 'dummy'), ('mg.tvph', 'dummy')])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger',
        ['scoreboard objectives add mg.tvc dummy {"text":"₵ Terra Nova","color":"green"}'])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw',
        ['scoreboard objectives remove mg.tvc', 'schedule clear mg:terra/wb_step', 'schedule clear mg:terra/world_build', 'schedule clear mg:terra/session_setup',
         'schedule clear mg:terra/spawn_clean', f'execute in {DIM} run forceload remove all', 'kill @e[tag=mg.tvport]', 'kill @e[tag=mg.tv]',
         'team remove mg_tv', 'bossbar remove mg:tvcarno', 'bossbar remove mg:tvo1', 'bossbar remove mg:tvo2', 'bossbar remove mg:tvo3',
         'data remove storage mg:terra built', 'data remove storage mg:terra d', 'data remove storage mg:terra h', 'data remove storage mg:lobby tvclean'])
# menu Échap : bouton « Aller à Terra Nova » (après Neo GTA)
_mp = os.path.join(C.D, 'dialog', 'main_menu.json')
_m = json.load(open(_mp, encoding='utf-8'))
if not any(a['action'].get('command') == 'trigger mg.sv set 7' for a in _m['actions']):
    i = next(i for i, a in enumerate(_m['actions']) if a['action'].get('command') == 'trigger mg.sv set 4')
    _m['actions'].insert(i + 1, {'label': [{'text': '🦖 Aller à Terra Nova', 'color': 'green', 'bold': True}],
                                 'tooltip': [{'text': 'Colonie préhistorique : missions, jungle, dinosaures (tes crédits y sont gardés)', 'color': 'gray'}],
                                 'action': {'type': 'minecraft:run_command', 'command': 'trigger mg.sv set 7'}})
    with open(_mp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(_m, f, ensure_ascii=False, indent=2)
        f.write('\n')
print(f'Terra Nova OK : {len(TERRAIN)} cmd de relief, {len(S)} de colonie, {len(VEG)} de végétation, {NS} étapes, '
      f'{len(CRATES)} caisses, {len(SPAWNS)} points d\'apparition ({len(FAR)} lointains), {len(HERBS)} herbivores')
# ================================================================ RPG (tv_rpg.py) : niveaux, campagne, PNJ, boss, forge, voyages
TVR = dict(globals())
TVR.update({k: TVW[k] for k in ('POIS', 'CAMPS', 'MARKERS', 'DATA_PTS', 'CELL', 'RIFT', 'VOLC', 'LAG', 'FORT', 'DELTA', 'CALD_Y', 'REGIONS',
                                'PASS_GATE', 'ECHO', 'LOOKOUT', 'REFUGE', 'BRIDGE', 'BR_Y', 'STATION', 'ground', 'EGGS', 'LAB_NPC', 'FORGE_NPC',
                                'COLONY_BEACON', 'DUNGEONS', 'CACHES')})
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tv_rpg.py'), encoding='utf-8').read(), TVR)
if os.environ.get('TV_DUMP'):                       # aperçu de la carte (outil de mise au point)
    import pickle
    pickle.dump({'H': H, 'surface': {c: surface(*c) for c in H}, 'COL': TVW['COL'], 'POIS': TVW['POIS'], 'MARKERS': TVW['MARKERS']},
                open(os.environ['TV_DUMP'], 'wb'))
