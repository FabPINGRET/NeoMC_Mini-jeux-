"""⛳ Golf façon Wii Sports — id 215, parcours de 6 trous (par 23) sur une île flottante 200×200 (centre X, Z ci-dessous).

    cd /home/claude/dp && flock /home/claude/gen.lock python3 tools/arcade/gen_golf.py .
    python3 tools/arcade/gen_golf.py . --map      # aperçu ASCII du parcours (n'écrit rien)

Tout le monde joue en même temps, chacun sa balle (item_display), même parcours. Le joueur tient un club
(warped_fungus_on_a_stick : lu par mg.qs comme gun/ et bomber/, détecté par custom_data {golf:1|2}), vise avec le regard,
une jauge de puissance oscille dans la barre d'action, clic droit = frapper. Bois/Fer = vol en cloche, Putter = roule.

Physique en scores (positions ×1000, vitesses en millièmes de bloc par tick, 4 sous-pas par tick) : gravité, traînée,
rebond selon la surface, roulement avec frottement (green faible, fairway moyen, rough fort, sable très fort), collisions
avec les blocs pleins (rebond, ou marche d'un bloc franchie en roulant), trou = cuve (balle lente qui passe dessus, ou qui
tombe dedans). Eau / vide / arbre = +1 coup, balle replacée au dernier point sec où elle a touché le sol.

Tableau de droite : mg.gfd = −total (le plus petit total est donc en haut, le tri du jeu étant décroissant) et chaque ligne
affiche le vrai total et l'écart au par grâce à « scoreboard players display numberformat … fixed ».
"""
import math
import os
import random
import sys

import common as C

ARGS = [a for a in sys.argv[1:] if not a.startswith('--')]
C.init(ARGS[0] if ARGS else '.')
w, js = C.w, C.js
GID = 215
X0, Z0 = C.param('X', 300), C.param('Z', 34600)   # centre de l'île (zone libre : x 200..400, z 34500..34700)
R = 100                                           # demi-côté de l'emprise (201×201)
VERSION = 2                                       # changer → le parcours est reconstruit à la prochaine partie
SENT = (X0, 55, Z0 + VERSION)                     # bloc témoin (lodestone) : parcours déjà construit
BASE = 64                                         # niveau du sol (bloc du dessus en y 64, balle posée en y 65)
WATER_TOP = 64
G, DRAG, SUB = 40, 990, 4                         # gravité (mb/t²), traînée en l'air (‰ / tick), sous-pas par tick
WOOD_H, PUTT_H = 22, 8                            # vitesse horizontale max : bois 2,2 b/t (× √puissance), putter 0,8 b/t
HOLE_V = 420                                      # vitesse max (|vx|+|vz|) pour tomber dans le trou en roulant
MAXS = 8                                          # coups max par trou
FX, FZ = X0 - R - 4, Z0 - R - 4                   # forceload (temporaire, pendant la partie)
FX2, FZ2 = X0 + R + 4, Z0 + R + 4

# ---------------------------------------------------------------------------------------------------------------- tracé
# pts : départ → (coude) → trou ; fw : demi-largeur du fairway (0 = pas de fairway) ; lim : temps limite (ticks)
HOLES = [
    dict(par=4, pts=[(-76, 80), (-80, -6)], fw=8, name='Le Grand Chêne'),
    dict(par=3, pts=[(-62, -24), (-57, -72)], fw=6, fw_from=0.45, name='La Descente'),
    dict(par=5, pts=[(-44, -88), (84, -80)], fw=8, name='La Rivière'),
    dict(par=3, pts=[(86, -62), (84, -18)], fw=0, island=True, name="L'Île"),
    dict(par=4, pts=[(80, 14), (80, 70), (32, 82)], fw=8, name='Le Coude'),
    dict(par=4, pts=[(12, 60), (-14, -36)], fw=8, name='Le Retour'),
]
LIM = {3: 1200, 4: 1500, 5: 1800}
GREEN_R = 7
LAKES = [(-45, 25, 13, 17), (25, -86, 7, 17), (84, -20, 16, 14), (-29, -22, 7, 6), (58, 50, 8, 8)]
ISLAND = (84, -18, 8)              # île du trou 4 (green r 6 + collier)
BUNKERS = [(-88, 18, 3, 5), (-70, -3, 2.5, 3.5), (-87, -13, 3, 2.5),
           (-49, -67, 2.5, 4), (-65, -70, 2.5, 3.5),
           (-2, -80, 5, 2.5), (62, -93, 4, 2.5), (92, -76, 2.5, 3.2), (78, -90, 3, 2.5),
           (90, 77, 3, 4), (34, 91, 4, 2.5), (23, 77, 2.5, 3),
           (2, 18, 3, 6), (-5, -44, 3, 2.5)]
HILLS = [(4.7, -62, -24, 11), (2.6, -96, 50, 15), (2.2, -58, 72, 13), (2.6, 42, -55, 15), (2.2, 34, 22, 17),
         (2.0, 66, -2, 9), (2.4, -14, -38, 11), (1.7, -22, 86, 13), (1.4, 0, -96, 11), (1.6, 66, 36, 10)]
DOGLEG_TREES = [(66, 34), (70, 44), (64, 58), (48, 64), (68, 26), (52, 40), (44, 56), (60, 68)]
rnd = random.Random(215)


def seg_dist(px, pz, a, b):
    (ax, az), (bx, bz) = a, b
    dx, dz = bx - ax, bz - az
    L2 = dx * dx + dz * dz
    t = max(0.0, min(1.0, ((px - ax) * dx + (pz - az) * dz) / L2))
    return math.hypot(px - ax - t * dx, pz - az - t * dz), t


def path_dist(px, pz, pts):
    """Distance au tracé + abscisse curviligne relative (0 départ, 1 trou)."""
    lens = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    tot, acc, best = sum(lens), 0.0, (1e9, 0)
    for i in range(len(pts) - 1):
        d, t = seg_dist(px, pz, pts[i], pts[i + 1])
        if d < best[0]:
            best = (d, (acc + t * lens[i]) / tot)
        acc += lens[i]
    return best


def noise(x, z):
    return math.sin(x * 0.21 + z * 0.13) + math.sin(x * 0.07 - z * 0.27 + 1.3) * 0.8 + math.sin(x * 0.33 + z * 0.29 + 2.1) * 0.5


def in_ell(x, z, e, m=0.0):
    cx, cz, rx, rz = e
    return ((x - cx) / (rx + m)) ** 2 + ((z - cz) / (rz + m)) ** 2 <= 1


def hill_h(x, z):
    return sum(a * math.exp(-((x - cx) ** 2 + (z - cz) ** 2) / (r * r)) for a, cx, cz, r in HILLS)


for h in HOLES:
    h['tee'], h['cup'] = h['pts'][0], h['pts'][-1]
    h['len'] = round(sum(math.dist(h['pts'][i], h['pts'][i + 1]) for i in range(len(h['pts']) - 1)))
    (ax, az), (bx, bz) = h['pts'][0], h['pts'][1]
    n = math.hypot(bx - ax, bz - az)
    h['dir'] = ((bx - ax) / n, (bz - az) / n)

# ---------------------------------------------------------------------------------------------------------------- carte
# kind : V vide, R rough, F fairway, G green, T départ, B bunker, W eau, I collier de l'île
KIND, HGT = {}, {}
for x in range(-R, R + 1):
    for z in range(-R, R + 1):
        e = (abs(x) / 98) ** 6 + (abs(z) / 98) ** 6
        if e > 1 + 0.06 * noise(x, z):
            KIND[x, z] = 'V'
            continue
        k, hh = 'R', BASE + hill_h(x, z)
        for i, h in enumerate(HOLES):
            if h['fw']:
                d, t = path_dist(x, z, h['pts'])
                if d <= h['fw'] + 0.9 * math.sin(t * 9 + i) + 0.5 * noise(x * 2, z * 2) and t >= h.get('fw_from', 0.08):
                    k = 'F'
        if any(in_ell(x, z, b) for b in BUNKERS):
            k = 'B'
        lake = any(in_ell(x, z, l) for l in LAKES)
        if lake:
            k = 'W'
        if any(in_ell(x, z, l, 4) for l in LAKES):
            hh = BASE                      # rives plates
        KIND[x, z], HGT[x, z] = k, int(math.floor(hh))
# greens (plateau) et départs (5×5, +1)
for i, h in enumerate(HOLES):
    cx, cz = h['cup']
    if h.get('island'):
        ix, iz, ir = ISLAND
        h['gy'] = BASE + 1
        for x in range(ix - ir, ix + ir + 1):
            for z in range(iz - ir, iz + ir + 1):
                d = math.hypot(x - ix, z - iz)
                if d <= ir - 1.5:
                    KIND[x, z], HGT[x, z] = 'G', BASE + 1
                elif d <= ir:
                    KIND[x, z], HGT[x, z] = 'I', BASE + 1
    else:
        gy = HGT[cx, cz]
        h['gy'] = gy
        for x in range(cx - GREEN_R - 3, cx + GREEN_R + 4):
            for z in range(cz - GREEN_R - 3, cz + GREEN_R + 4):
                d = math.hypot((x - cx) * 0.95, (z - cz) * 1.08)
                if d <= GREEN_R + 0.5 * math.sin(math.atan2(z - cz, x - cx) * 3 + i):
                    KIND[x, z], HGT[x, z] = 'G', gy
                elif d <= GREEN_R + 2.5 and KIND.get((x, z), 'V') not in ('W', 'B', 'V'):
                    KIND[x, z], HGT[x, z] = 'F', gy          # collier autour du green
                elif d <= GREEN_R + 3.5 and KIND.get((x, z), 'V') != 'V':
                    HGT[x, z] = max(gy - 1, min(gy + 1, HGT[x, z]))
    tx, tz = h['tee']
    ty = max(HGT[x, z] for x in range(tx - 2, tx + 3) for z in range(tz - 2, tz + 3)) + 1
    h['ty'] = ty
    for x in range(tx - 2, tx + 3):
        for z in range(tz - 2, tz + 3):
            KIND[x, z], HGT[x, z] = 'T', ty
    for x in range(tx - 4, tx + 5):
        for z in range(tz - 4, tz + 5):
            if KIND[x, z] in ('R', 'F'):
                HGT[x, z] = max(ty - 1, min(ty + 1, HGT[x, z]))

if '--map' in sys.argv:
    ch = {'V': ' ', 'R': '.', 'F': '=', 'G': 'o', 'T': 'T', 'B': ':', 'W': '~', 'I': '='}
    for z in range(-R, R + 1, 2):
        print(''.join(ch[KIND[x, z]] if (x, z) not in [h['cup'] for h in HOLES] else '@' for x in range(-R, R + 1)))
    for i, h in enumerate(HOLES):
        print(f'trou {i + 1} par {h["par"]} {h["len"]} m  départ y{h["ty"]}  green y{h["gy"]}')
    sys.exit()

if '--dump' in sys.argv:          # pour les tests : surface attendue colonne par colonne
    import json
    print(json.dumps({f'{x},{z}': [k, HGT.get((x, z), 0)] for (x, z), k in KIND.items()}))
    sys.exit()

# ---------------------------------------------------------------------------------------------------------------- construction
TOP = {'R': 'grass_block', 'F': 'moss_block', 'G': 'lime_concrete', 'T': 'moss_block', 'B': 'sand', 'I': 'moss_block'}


def rects(cells):
    """cells : {(x, z): clé} → rectangles fusionnés [(x1, z1, x2, z2, clé)] (lignes puis fusion verticale)."""
    out, open_ = [], {}
    for z in range(-R, R + 2):
        segs, x = [], -R
        while z <= R and x <= R:
            k = cells.get((x, z))
            if k is None:
                x += 1
                continue
            x1 = x
            while x + 1 <= R and cells.get((x + 1, z)) == k:
                x += 1
            segs.append((x1, x, k))
            x += 1
        nxt = {}
        for s in segs:
            if s in open_:
                nxt[s] = open_.pop(s)
            else:
                nxt[s] = z
        for (x1, x2, k), z1 in open_.items():
            out.append((x1, z1, x2, z - 1, k))
        open_ = nxt
    return out


def fill(x1, y1, z1, x2, y2, z2, block, extra=''):
    """fill découpé (≤ 32768 blocs)."""
    res = []
    vol_row = (x2 - x1 + 1) * (y2 - y1 + 1)
    step = max(1, 32768 // vol_row)
    for zz in range(z1, z2 + 1, step):
        res.append(f'fill {X0 + x1} {y1} {Z0 + zz} {X0 + x2} {y2} {Z0 + min(z2, zz + step - 1)} minecraft:{block}{extra}')
    return res


BUILD = []
# 0. vide la zone (y 55..110)
for y1 in range(55, 111, 14):
    BUILD += fill(-R - 2, y1, -R - 2, R + 2, min(110, y1 + 13), R + 2, 'air')
# 1. socle : pierre 58..60, terre 61..63 (sous les lacs : lit de gravier/argile)
land = {(x, z): 1 for (x, z), k in KIND.items() if k != 'V'}
for x1, z1, x2, z2, _ in rects(land):
    BUILD += fill(x1, 58, z1, x2, 60, z2, 'stone') + fill(x1, 61, z1, x2, 63, z2, 'dirt')
# dessous de l'île un peu irrégulier
under = {(x, z): 1 for (x, z), k in KIND.items() if k != 'V' and all(KIND.get((x + dx, z + dz), 'V') != 'V' for dx in (-3, 3) for dz in (-3, 3))}
for x1, z1, x2, z2, _ in rects(under):
    BUILD += fill(x1, 56, z1, x2, 57, z2, 'stone')
# 2. terre au-dessus de 63 (collines, départs, green surélevé)
raised = {(x, z): HGT[x, z] for (x, z), k in KIND.items() if k not in ('V', 'W') and HGT[x, z] > BASE}
for x1, z1, x2, z2, hh in rects(raised):
    BUILD += fill(x1, BASE, z1, x2, hh - 1, z2, 'dirt')
# 3. surface
surf = {}
for (x, z), k in KIND.items():
    if k == 'V':
        continue
    if k == 'W':
        surf[x, z] = ('W', BASE)
    elif k == 'B':
        surf[x, z] = ('B', HGT[x, z] - 1)
    else:
        surf[x, z] = (TOP[k], HGT[x, z])
for x1, z1, x2, z2, (blk, hh) in rects(surf):
    if blk == 'W':
        BUILD += fill(x1, 60, z1, x2, 60, z2, 'clay') + fill(x1, 61, z1, x2, 61, z2, 'gravel') + fill(x1, 62, z1, x2, WATER_TOP, z2, 'water')
    elif blk == 'B':
        BUILD += fill(x1, hh - 1, z1, x2, hh, z2, 'sand')
    else:
        BUILD += fill(x1, hh, z1, x2, hh, z2, blk)
# fairway tondu en damier (carrés de 4 : moss_block / green_concrete)
fw = {(x // 4, z // 4) for (x, z), k in KIND.items() if k in ('F', 'T', 'I') and (x // 4 + z // 4) % 2}
for cx, cz in sorted(fw):
    BUILD.append(f'fill {X0 + cx * 4} 63 {Z0 + cz * 4} {X0 + cx * 4 + 3} 72 {Z0 + cz * 4 + 3} minecraft:green_concrete replace minecraft:moss_block')
# green : bandes plus claires (lime_concrete / lime_terracotta n'est pas assez clair → lime_wool en damier fin 2×2)
# (même frottement : tag golf_green)
gr = {(x // 2, z // 2) for (x, z), k in KIND.items() if k == 'G' and (x // 2 + z // 2) % 2}
for cx, cz in sorted(gr):
    BUILD.append(f'fill {X0 + cx * 2} 63 {Z0 + cz * 2} {X0 + cx * 2 + 1} 72 {Z0 + cz * 2 + 1} minecraft:lime_wool replace minecraft:lime_concrete')

# 4. décor : herbes, fleurs, nénuphars, arbres
FLOWERS = ['poppy', 'dandelion', 'cornflower', 'oxeye_daisy', 'azure_bluet', 'allium']
def far_from_play(x, z, m):
    for h in HOLES:
        if path_dist(x, z, h['pts'])[0] < (h['fw'] or 6) + m:
            return False
        if math.dist((x, z), h['cup']) < GREEN_R + m + 2 or math.dist((x, z), h['tee']) < 5 + m:
            return False
    return True


DECO = []
for (x, z), k in sorted(KIND.items()):
    if k != 'R':
        continue
    r_ = rnd.random()
    if r_ < 0.10:
        DECO.append(f'setblock {X0 + x} {HGT[x, z] + 1} {Z0 + z} minecraft:short_grass')
    elif r_ < 0.125 and far_from_play(x, z, 3):
        DECO.append(f'setblock {X0 + x} {HGT[x, z] + 1} {Z0 + z} minecraft:{rnd.choice(FLOWERS)}')
for (x, z), k in sorted(KIND.items()):
    if k == 'W' and rnd.random() < 0.03:
        DECO.append(f'setblock {X0 + x} {WATER_TOP + 1} {Z0 + z} minecraft:lily_pad')

TREES = []
def tree_ok(x, z):
    if not all(KIND.get((x + dx, z + dz)) == 'R' for dx in (-3, 0, 3) for dz in (-3, 0, 3)):
        return False
    return all(math.dist((x, z), t) >= 6 for t in TREES)


for _ in range(900):
    x, z = rnd.randint(-92, 92), rnd.randint(-92, 92)
    if tree_ok(x, z) and far_from_play(x, z, 4):
        TREES.append((x, z))
for t in DOGLEG_TREES:
    if KIND.get(t) not in ('V', 'W') and all(math.dist(t, u) >= 4 for u in TREES):
        TREES.append(t)


def tree(x, z, kind):
    y = HGT[x, z] + 1
    X, Z = X0 + x, Z0 + z
    if kind == 'spruce':
        L = [f'fill {X} {y} {Z} {X} {y + 6} {Z} minecraft:spruce_log']
        for i, r in enumerate((2, 2, 1, 1, 0)):
            yy = y + 3 + i
            L.append(f'fill {X - r} {yy} {Z - r} {X + r} {yy} {Z + r} minecraft:spruce_leaves[persistent=true] replace minecraft:air')
        L.append(f'setblock {X} {y + 7} {Z} minecraft:spruce_leaves[persistent=true]')
        return L
    log, leaves = ('birch_log', 'birch_leaves') if kind == 'birch' else ('oak_log', 'oak_leaves')
    hgt = 5 if kind == 'birch' else 4
    L = [f'fill {X} {y} {Z} {X} {y + hgt} {Z} minecraft:{log}',
         f'fill {X - 2} {y + hgt - 1} {Z - 2} {X + 2} {y + hgt} {Z + 2} minecraft:{leaves}[persistent=true] replace minecraft:air',
         f'fill {X - 1} {y + hgt + 1} {Z - 1} {X + 1} {y + hgt + 2} {Z + 1} minecraft:{leaves}[persistent=true] replace minecraft:air']
    for dx, dz in ((-2, -2), (2, -2), (-2, 2), (2, 2)):
        if rnd.random() < 0.7:
            L.append(f'setblock {X + dx} {y + hgt} {Z + dz} minecraft:air')
    return L


for x, z in TREES:
    DECO += tree(x, z, rnd.choice(['oak', 'oak', 'birch', 'spruce']))
# grand chêne du trou 1 (à gauche du départ)
DECO += [f'fill {X0 - 92} {HGT[-92, 70] + 1} {Z0 + 70} {X0 - 91} {HGT[-92, 70] + 7} {Z0 + 71} minecraft:oak_log',
         f'fill {X0 - 96} {HGT[-92, 70] + 6} {Z0 + 66} {X0 - 87} {HGT[-92, 70] + 8} {Z0 + 75} minecraft:oak_leaves[persistent=true] replace minecraft:air',
         f'fill {X0 - 94} {HGT[-92, 70] + 9} {Z0 + 68} {X0 - 89} {HGT[-92, 70] + 10} {Z0 + 73} minecraft:oak_leaves[persistent=true] replace minecraft:air']


def yaw_of(dx, dz):
    return math.degrees(math.atan2(-dx, dz))


# départs : repères, panneau ; trous : cuve
for i, h in enumerate(HOLES):
    tx, tz = h['tee']
    ux, uz = h['dir']
    px_, pz_ = -uz, ux                                   # perpendiculaire
    for s in (-1, 1):
        mx, mz = round(tx + ux * 3 + px_ * 3 * s), round(tz + uz * 3 + pz_ * 3 * s)
        DECO.append(f'setblock {X0 + mx} {HGT.get((mx, mz), h["ty"]) + 1} {Z0 + mz} minecraft:quartz_pillar')
    sx, sz = round(tx - ux * 1 - px_ * 4), round(tz - uz * 1 - pz_ * 4)
    rot = round(yaw_of(ux, uz) / 22.5) % 16                # le panneau regarde vers… l'arrière du départ (lu depuis le tee)
    rot = (rot + 8) % 16
    h['sign'] = (sx, sz)
    DECO.append(f'setblock {X0 + sx} {HGT[sx, sz] + 1} {Z0 + sz} minecraft:oak_sign[rotation={rot}]' + '{front_text:{messages:[' +
                f'{{text:"⛳ Trou {i + 1}",color:"dark_green",bold:true}},{{text:"Par {h["par"]}",color:"black"}},'
                f'{{text:"{h["len"]} m",color:"dark_gray"}},{{text:"{h["name"]}",color:"blue"}}' + ']}}')
    cx, cz = h['cup']
    DECO.append(f'setblock {X0 + cx} {h["gy"]} {Z0 + cz} minecraft:cauldron')
DECO.append(f'setblock {SENT[0]} {SENT[1]} {SENT[2]} minecraft:lodestone')

# découpe en étapes (une par tick)
PARTS, cur, vol = [], [], 0
for line in BUILD + DECO:
    cur.append(line)
    if len(cur) >= 700:
        PARTS.append(cur)
        cur = []
PARTS.append(cur)
NP = len(PARTS)
for k, p in enumerate(PARTS):
    nxt = [f'schedule function mg:golf/build_{k + 1} 1t'] if k + 1 < NP else ['function mg:golf/ready']
    w(f'golf/build_{k}', [f'# ⛳ Golf : construction du parcours, étape {k + 1}/{NP} (générée par tools/arcade/gen_golf.py)',
                          f'execute unless loaded {FX + 4} 64 {FZ + 4} run return run function mg:golf/build_fail',
                          f'execute unless loaded {FX2 - 4} 64 {FZ2 - 4} run return run function mg:golf/build_fail'] + p + nxt)
w('golf/build_fail', ['# Zone déchargée pendant la construction (partie annulée ?) : on reconstruira à la prochaine partie',
                      f'setblock {SENT[0]} {SENT[1]} {SENT[2]} minecraft:air',
                      'tellraw @a[tag=mg.admin] {"text":"[Mini-Jeux] Golf : construction interrompue (zone déchargée).","color":"red"}'])

# block tag : ce que la balle traverse
tag_dir = os.path.join(C.D, 'tags/block')
os.makedirs(tag_dir, exist_ok=True)
with open(os.path.join(tag_dir, 'golf_pass.json'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(js({'values': ['minecraft:air', 'minecraft:cave_air', 'minecraft:void_air', 'minecraft:water', 'minecraft:short_grass',
                           'minecraft:tall_grass', 'minecraft:fern', 'minecraft:lily_pad', 'minecraft:light', 'minecraft:structure_void']
                + [f'minecraft:{fl}' for fl in FLOWERS]}) + '\n')

# ---------------------------------------------------------------------------------------------------------------- entités du décor
COLORS = [(16777215, '1.0,1.0,1.0', 'white'), (16733525, '1.0,0.33,0.33', 'red'), (5592575, '0.33,0.33,1.0', 'blue'),
          (5635925, '0.33,1.0,0.33', 'green'), (16777045, '1.0,1.0,0.33', 'yellow'), (16733695, '1.0,0.33,1.0', 'light_purple'),
          (5636095, '0.33,1.0,1.0', 'aqua'), (16755200, '1.0,0.67,0.0', 'gold')]
T_ID = '{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]'
FLAGS = []
for i, h in enumerate(HOLES):
    cx, cz = h['cup']
    x, y, z = X0 + cx + 0.5, h['gy'] + 1, Z0 + cz + 0.5
    FLAGS += [f'summon minecraft:block_display {x} {y} {z} {{Tags:["mg.fx","mg.gff"],view_range:3f,block_state:{{Name:"minecraft:white_concrete"}},'
              f'transformation:{T_ID},translation:[-0.04f,-0.6f,-0.04f],scale:[0.08f,4.1f,0.08f]}}}}',
              f'summon minecraft:block_display {x} {y} {z} {{Tags:["mg.fx","mg.gff"],view_range:3f,block_state:{{Name:"minecraft:red_wool"}},'
              f'transformation:{T_ID},translation:[0.04f,2.85f,-0.02f],scale:[1.0f,0.6f,0.04f]}}}}',
              f'summon minecraft:text_display {x} {y + 4.0} {z} {{Tags:["mg.fx","mg.gff"],billboard:"center",view_range:3f,'
              f'text:{{"text":"{i + 1}","color":"yellow","bold":true}},background:0,transformation:{T_ID},translation:[0f,0f,0f],scale:[2f,2f,2f]}}}}']
    tx, tz = h['tee']
    ux, uz = h['dir']
    FLAGS.append(f'summon minecraft:text_display {X0 + tx + 0.5 - ux * 3.5} {h["ty"] + 3.2} {Z0 + tz + 0.5 - uz * 3.5} '
                 f'{{Tags:["mg.fx","mg.gff"],billboard:"center",view_range:2f,background:1342177280,transformation:{T_ID},translation:[0f,0f,0f],scale:[1.4f,1.4f,1.4f]}},'
                 f'text:[{{"text":"⛳ TROU {i + 1}","color":"yellow","bold":true}},{{"text":"\\nPar {h["par"]} · {h["len"]} m","color":"white"}},'
                 f'{{"text":"\\n{h["name"]}","color":"aqua","italic":true}}]}}')

# ---------------------------------------------------------------------------------------------------------------- jeu
PL = '@a[tag=mg.play]'
w('golf/prepare', ['# ⛳ Golf — préparation (pendant le compte à rebours) : zone chargée, parcours construit si besoin, joueurs au départ 1',
                   'scoreboard players set $gfok mg.st 0', 'scoreboard players set $gfh mg.st 0', 'scoreboard players set $gfw mg.st 0',
                   'scoreboard players set $gfn mg.st 0', 'scoreboard players set $gfwait mg.st 0', 'scoreboard players set $gfpc mg.st 0',
                   'scoreboard players set #gf2 mg.st 2', 'scoreboard players set #gf4 mg.st 4', 'scoreboard players set #gf10 mg.st 10',
                   'scoreboard players set #gf100 mg.st 100', 'scoreboard players set #gf1000 mg.st 1000', 'scoreboard players set #gf10000 mg.st 10000',
                   'scoreboard players set #gfm1 mg.st -1', f'scoreboard players set #gfdrag mg.st {DRAG}', 'scoreboard players set #gf5 mg.st 5',
                   'scoreboard players set #gf8 mg.st 8', 'scoreboard players set #gfest1 mg.st 93', 'scoreboard players set #gfest2 mg.st 16',
                   f'scoreboard players set $px mg.st {X0}', 'scoreboard players set $py mg.st 100', f'scoreboard players set $pz mg.st {Z0}',
                   f'gamemode adventure {PL}', f'clear {PL}', f'effect give {PL} minecraft:saturation infinite 0 true',
                   f'effect give {PL} minecraft:resistance infinite 4 true', f'team join mg_golf {PL}',
                   'scoreboard players reset * mg.gft', 'scoreboard players reset * mg.gfd', 'scoreboard players reset * mg.gfi',
                   f'scoreboard players set {PL} mg.gft 0', f'scoreboard players set {PL} mg.gfs 2', f'scoreboard players set {PL} mg.gfc 0',
                   f'execute as {PL} run function mg:golf/assign',
                   'kill @e[tag=mg.gfb]', 'kill @e[tag=mg.gff]', 'kill @e[tag=mg.gftg]',
                   f'forceload add {FX} {FZ} {FX2} {FZ2}',
                   'schedule function mg:golf/wait 10t'])
w('golf/assign', ['# @s : numéro de joueur (relie le joueur à sa balle), ligne du tableau', 'scoreboard players add $gfn mg.st 1',
                  'scoreboard players operation @s mg.gfi = $gfn mg.st', 'scoreboard players set @s mg.gfd 0',
                  'scoreboard players display numberformat @s mg.gfd fixed {"text":"0","color":"white"}'])
w('golf/wait', ['# Attend le chargement de la zone puis construit (si le bloc témoin manque) ou passe directement à golf/ready',
                f'execute unless score $game mg.st matches {GID} run return 0', 'execute unless score $state mg.st matches 1..2 run return 0',
                'scoreboard players add $gfwait mg.st 1',
                'execute if score $gfwait mg.st matches 60.. run return run tellraw @a[tag=mg.admin] {"text":"[Mini-Jeux] Golf : zone pas chargée.","color":"red"}'] +
  [f'execute unless loaded {x} 64 {z} run return run schedule function mg:golf/wait 10t'
   for x, z in ((FX + 4, FZ + 4), (FX2 - 4, FZ + 4), (FX + 4, FZ2 - 4), (FX2 - 4, FZ2 - 4), (X0, Z0))] +
  [f'execute unless block {SENT[0]} {SENT[1]} {SENT[2]} minecraft:lodestone run return run function mg:golf/build',
   'function mg:golf/ready'])
w('golf/build', ['# (aussi utilisable par un OP, zone chargée) : construit le parcours en plusieurs ticks puis golf/ready',
                 f'tellraw @a[tag=mg.play] {{"text":"⛳ Construction du parcours…","color":"green"}}', 'function mg:golf/build_0'])
w('golf/ready', ['# Parcours prêt : drapeaux, panneaux flottants, joueurs au départ du trou 1',
                 f'execute unless score $game mg.st matches {GID} run return 0', 'execute unless score $state mg.st matches 1..2 run return 0',
                 'scoreboard players set $gfok mg.st 1', 'kill @e[tag=mg.gff]', 'kill @e[tag=mg.gftg]'] + FLAGS +
  [f'summon minecraft:marker {X0} 80 {Z0} {{Tags:["mg.fx","mg.gftg"]}}',
   f'execute if score $state mg.st matches 1 as {PL} run function mg:golf/tee_wait'])
tx, tz = HOLES[0]['tee']
w('golf/tee_wait', ['# @s : attend le départ sur le tee 1',
                    f'tp @s {X0 + tx + 0.5} {HOLES[0]["ty"] + 1} {Z0 + tz + 0.5} facing {X0 + HOLES[0]["cup"][0]} {HOLES[0]["gy"] + 1} {Z0 + HOLES[0]["cup"][1]}'])

CLUBS = ['item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[custom_data={golf:1},item_model="minecraft:iron_hoe",unbreakable={},'
         'custom_name={"text":"🏌 Bois / Fer","color":"gold","bold":true,"italic":false},lore=[{"text":"Coup long en cloche (jusqu\'à ~100 m)","color":"gray","italic":false},'
         '{"text":"Clic droit : frapper au bon moment de la jauge","color":"dark_gray","italic":false}],use_cooldown={seconds:0.5f,cooldown_group:"mg:golf"}]',
         'item replace entity @s hotbar.1 with minecraft:warped_fungus_on_a_stick[custom_data={golf:2},item_model="minecraft:golden_shovel",unbreakable={},'
         'custom_name={"text":"⛳ Putter","color":"green","bold":true,"italic":false},lore=[{"text":"La balle roule (jusqu\'à ~16 m sur le green)","color":"gray","italic":false},'
         '{"text":"Clic droit : frapper au bon moment de la jauge","color":"dark_gray","italic":false}],use_cooldown={seconds:0.5f,cooldown_group:"mg:golf"}]']
w('golf/kit', ['# @s : les deux clubs'] + CLUBS)
w('golf/go', ['# ⛳ Départ', f'execute as {PL} run function mg:golf/kit', f'scoreboard players reset {PL} mg.qs',
              'scoreboard objectives setdisplay sidebar mg.gfd',
              f'tellraw {PL} ' + js([{'text': '⛳ GOLF : ', 'color': 'green', 'bold': True},
                                    {'text': f'6 trous (par {sum(h["par"] for h in HOLES)}), tout le monde joue en même temps. Vise avec le regard, ',
                                     'color': 'gray'},
                                    {'text': 'clic droit', 'color': 'yellow'}, {'text': ' quand la jauge est au bon niveau. ', 'color': 'gray'},
                                    {'text': 'Bois/Fer', 'color': 'gold'}, {'text': ' = vol en cloche, ', 'color': 'gray'},
                                    {'text': 'Putter', 'color': 'green'},
                                    {'text': f' = roule (green). Eau / vide = +1 coup. {MAXS} coups max par trou. Le plus petit total gagne !',
                                     'color': 'gray'}])])

# --- tick global
w('golf/tick', ['# ⛳ Golf — tick',
                'execute unless score $gfok mg.st matches 1 run return run title @a[tag=mg.play] actionbar {"text":"⛳ Préparation du parcours…","color":"green"}',
                'execute if score $gfh mg.st matches 0 run function mg:golf/hole_next',
                f'execute as {PL} at @s run function mg:golf/ptick',
                f'scoreboard players reset {PL} mg.qs',
                'execute as @e[type=minecraft:item_display,tag=mg.gfmv] at @s run function mg:golf/ball',
                f'execute store result score $alive mg.st if entity {PL}',
                'execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run return run function mg:core/draw',
                'execute if score $gfw mg.st matches 1.. run return run function mg:golf/between',
                'scoreboard players add $gft mg.st 1',
                'scoreboard players operation $gfr mg.st = $gflim mg.st', 'scoreboard players operation $gfr mg.st -= $gft mg.st',
                f'execute if score $gfr mg.st matches 300 run tellraw {PL} {{"text":"⏱ Plus que 15 secondes pour finir le trou !","color":"gold"}}',
                f'execute if score $gfr mg.st matches ..0 as @a[tag=mg.play,scores={{mg.gfs=0..1}}] run function mg:golf/timeout',
                f'execute store result score $gfa mg.st if entity @a[tag=mg.play,scores={{mg.gfs=0..1}}]',
                'execute if score $gfa mg.st matches 0 run function mg:golf/hole_done'])
w('golf/hole_done', ['# Tout le monde a fini le trou : pause de 4 s', 'scoreboard players set $gfw mg.st 80',
                     f'tellraw {PL} ' + js([{'text': '⛳ Trou ', 'color': 'green'}, {'score': {'name': '$gfh', 'objective': 'mg.st'}, 'color': 'yellow'},
                                           {'text': ' terminé. ', 'color': 'green'}, {'text': 'Trou suivant dans 4 s…', 'color': 'gray'}])])
w('golf/between', ['# Pause entre deux trous', 'scoreboard players remove $gfw mg.st 1',
                   'execute if score $gfw mg.st matches 0 if score $gfh mg.st matches 6.. run return run function mg:golf/finish',
                   'execute if score $gfw mg.st matches 0 run function mg:golf/hole_next'])
w('golf/hole_next', ['# Trou suivant', 'scoreboard players add $gfh mg.st 1', 'scoreboard players set $gft mg.st 0',
                     'kill @e[type=minecraft:item_display,tag=mg.gfb]'] +
  [f'execute if score $gfh mg.st matches {i + 1} run function mg:golf/h{i + 1}' for i in range(len(HOLES))])

for i, h in enumerate(HOLES):
    n = i + 1
    cx, cz = h['cup']
    tx, tz = h['tee']
    ux, uz = h['dir']
    L = [f'# Trou {n} : par {h["par"]}, {h["len"]} m — {h["name"]}',
         f'scoreboard players set $gfpar mg.st {h["par"]}', f'scoreboard players add $gfpc mg.st {h["par"]}',
         f'scoreboard players set $gflim mg.st {LIM[h["par"]]}',
         f'scoreboard players set $gfcx mg.st {(X0 + cx) * 1000 + 500}', f'scoreboard players set $gfcz mg.st {(Z0 + cz) * 1000 + 500}',
         f'tp @e[tag=mg.gftg] {X0 + cx + 0.5} {h["gy"] + 1} {Z0 + cz + 0.5}',
         f'execute as {PL} run function mg:golf/h{n}_ball',
         f'title {PL} times 5 50 15',
         f'title {PL} subtitle ' + js([{'text': f'Par {h["par"]} · {h["len"]} m · {h["name"]}', 'color': 'white'}]),
         f'title {PL} title ' + js([{'text': f'⛳ Trou {n}', 'color': 'green', 'bold': True}]),
         f'tellraw {PL} ' + js([{'text': f'⛳ Trou {n}/6', 'color': 'green', 'bold': True},
                               {'text': f' — par {h["par"]}, {h["len"]} m, « {h["name"]} »', 'color': 'gray'}] +
                              ([{'text': ' (green en île : vise juste !)', 'color': 'aqua'}] if h.get('island') else []) +
                              ([{'text': ' (dogleg : le trou tourne à droite, les arbres bloquent le raccourci)', 'color': 'aqua'}] if len(h['pts']) > 2 else [])),
         f'execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 0.7 1.2']
    w(f'golf/h{n}', L)
    px_, pz_ = -uz, ux
    B = [f'# @s : sa balle au départ du trou {n} (5 emplacements côte à côte)',
         'scoreboard players operation $gfsl mg.st = @s mg.gfi', 'scoreboard players operation $gfsl mg.st %= #gf5 mg.st']
    for k, off in enumerate((0, -1, 1, -2, 2)):
        bx, bz = round(tx + px_ * off) + 0.5, round(tz + pz_ * off) + 0.5
        B.append(f'execute if score $gfsl mg.st matches {k} run summon minecraft:item_display {bx} {h["ty"] + 1} {bz} '
                 '{Tags:["mg.fx","mg.gfb","mg.gfnew"],item:{id:"minecraft:snowball",count:1},billboard:"center",view_range:4f,Glowing:1b,'
                 f'teleport_duration:1,transformation:{T_ID},translation:[0f,0.12f,0f],scale:[0.45f,0.45f,0.45f]}}}}')
    B += ['scoreboard players operation $cur mg.st = @s mg.gfi', 'execute as @e[tag=mg.gfnew] run function mg:golf/ball_init',
          'function mg:golf/stroke_start']
    w(f'golf/h{n}_ball', B)

w('golf/ball_init', ['# @s : balle neuve ($cur = numéro du joueur) : position en scores, couleur du joueur',
                     'tag @s remove mg.gfnew', 'scoreboard players operation @s mg.gfi = $cur mg.st',
                     'execute store result score @s mg.gfx run data get entity @s Pos[0] 1000',
                     'execute store result score @s mg.gfy run data get entity @s Pos[1] 1000',
                     'execute store result score @s mg.gfz run data get entity @s Pos[2] 1000',
                     'scoreboard players operation @s mg.gflx = @s mg.gfx', 'scoreboard players operation @s mg.gfly = @s mg.gfy',
                     'scoreboard players operation @s mg.gflz = @s mg.gfz',
                     'scoreboard players set @s mg.gfu 0', 'scoreboard players set @s mg.gfv 0', 'scoreboard players set @s mg.gfw 0',
                     'tag @s add mg.gfg', 'scoreboard players operation $gfcol mg.st = $cur mg.st', 'scoreboard players operation $gfcol mg.st %= #gf8 mg.st'] +
  [f'execute if score $gfcol mg.st matches {k} run data modify entity @s glow_color_override set value {c[0]}' for k, c in enumerate(COLORS)])

# --- joueur
w('golf/stroke_start', ['# @s : début d\'un coup (balle à l\'arrêt) : jauge à zéro, replacé à côté de sa balle, distance au trou',
                        'scoreboard players set @s mg.gfs 0', 'scoreboard players set @s mg.gfp 0', 'scoreboard players set @s mg.gfq 1',
                        'scoreboard players set @s mg.gfk 12', 'scoreboard players reset @s mg.qs',
                        'function mg:golf/own', 'function mg:golf/place', 'function mg:golf/dist', 'tag @e[tag=mg.gfmy] remove mg.gfmy'])
w('golf/own', ['# @s : marque sa balle (tag mg.gfmy)', 'tag @e[tag=mg.gfmy] remove mg.gfmy', 'scoreboard players operation $cur mg.st = @s mg.gfi',
               'execute as @e[type=minecraft:item_display,tag=mg.gfb] if score @s mg.gfi = $cur mg.st run tag @s add mg.gfmy'])
w('golf/place', ['# @s : placé 1,3 bloc derrière sa balle, face au trou, regard baissé vers la balle',
                 'tag @s add mg.gfme',
                 'execute as @e[tag=mg.gfmy,limit=1] at @s facing entity @e[tag=mg.gftg,limit=1] feet rotated ~ 0 run function mg:golf/place_b',
                 'tag @s remove mg.gfme'])
w('golf/place_b', ['# @s = balle (orientée vers le trou)',
                   'execute positioned ^ ^ ^-1.3 if block ~ ~0.1 ~ #mg:golf_pass if block ~ ~1.1 ~ #mg:golf_pass unless block ~ ~-0.1 ~ #mg:golf_pass run return run tp @a[tag=mg.gfme,limit=1] ~ ~ ~ ~ 30',
                   'tp @a[tag=mg.gfme,limit=1] ~ ~ ~ ~ 30'])
w('golf/dist', ['# @s : distance de sa balle (tag mg.gfmy) au trou → mg.gfm (blocs)',
                'scoreboard players operation $gfdx mg.st = $gfcx mg.st', 'scoreboard players operation $gfdx mg.st -= @e[tag=mg.gfmy,limit=1] mg.gfx',
                'scoreboard players operation $gfdz mg.st = $gfcz mg.st', 'scoreboard players operation $gfdz mg.st -= @e[tag=mg.gfmy,limit=1] mg.gfz',
                'scoreboard players operation $gfdx mg.st /= #gf100 mg.st', 'scoreboard players operation $gfdz mg.st /= #gf100 mg.st',
                'scoreboard players operation $gfdx mg.st *= $gfdx mg.st', 'scoreboard players operation $gfdz mg.st *= $gfdz mg.st',
                'scoreboard players operation $gfsq mg.st = $gfdx mg.st', 'scoreboard players operation $gfsq mg.st += $gfdz mg.st',
                'function mg:golf/isqrt', 'scoreboard players operation @s mg.gfm = $gfsr mg.st', 'scoreboard players operation @s mg.gfm /= #gf10 mg.st'])
w('golf/isqrt', ['# $gfsr = √$gfsq (Newton, 14 itérations ; $gfsq ≤ 2·10⁹)', 'scoreboard players set $gfsr mg.st 0',
                 'execute if score $gfsq mg.st matches ..0 run return 0', 'scoreboard players set $gfsr mg.st 1',
                 'execute if score $gfsq mg.st matches 100.. run scoreboard players set $gfsr mg.st 30',
                 'execute if score $gfsq mg.st matches 10000.. run scoreboard players set $gfsr mg.st 300',
                 'execute if score $gfsq mg.st matches 1000000.. run scoreboard players set $gfsr mg.st 3000',
                 'execute if score $gfsq mg.st matches 100000000.. run scoreboard players set $gfsr mg.st 30000'] +
  ['function mg:golf/isqrt_it'] * 14)
w('golf/isqrt_it', ['scoreboard players operation $gfst mg.st = $gfsq mg.st', 'scoreboard players operation $gfst mg.st /= $gfsr mg.st',
                    'scoreboard players operation $gfsr mg.st += $gfst mg.st', 'scoreboard players operation $gfsr mg.st /= #gf2 mg.st',
                    'execute if score $gfsr mg.st matches ..0 run scoreboard players set $gfsr mg.st 1'])

w('golf/ptick', ['# @s : joueur, chaque tick',
                 f'execute if entity @s[y=-64,dy=110] run function mg:golf/rescue',
                 'execute if score @s mg.gfs matches 0 run function mg:golf/aim'])
w('golf/rescue', ['# @s tombé dans le vide : remis à côté de sa balle (ou au trou s\'il a fini)', 'function mg:golf/own',
                  'execute if score @s mg.gfs matches 0..1 if entity @e[tag=mg.gfmy] run function mg:golf/place',
                  'execute if score @s mg.gfs matches 2 run tp @s @e[tag=mg.gftg,limit=1]',
                  'tag @e[tag=mg.gfmy] remove mg.gfmy'])
BAR = 20
def bar_line(lo, hi, k, club):
    col = 'green' if k <= 12 else ('yellow' if k <= 17 else 'red')
    comps = [{'text': '●', 'color': '$COL'}, {'text': ' Trou ', 'color': 'gray'}, {'score': {'name': '$gfh', 'objective': 'mg.st'}, 'color': 'white'},
             {'text': ' · coup ', 'color': 'gray'}, {'score': {'name': '$gfnc', 'objective': 'mg.st'}, 'color': 'white'},
             {'text': ' · trou à ', 'color': 'gray'}, {'score': {'name': '@s', 'objective': 'mg.gfm'}, 'color': 'white'}, {'text': ' m   ', 'color': 'gray'},
             {'text': '█' * k, 'color': col}, {'text': '█' * (BAR - k), 'color': 'dark_gray'},
             {'text': ' ', 'color': 'gray'}, {'score': {'name': '@s', 'objective': 'mg.gfp'}, 'color': col}, {'text': '% ≈ ', 'color': 'gray'},
             {'score': {'name': '$gfe', 'objective': 'mg.st'}, 'color': 'white'}, {'text': ' m', 'color': 'gray'},
             {'text': '  [Bois/Fer]' if club == 1 else '  [Putter]', 'color': 'gold' if club == 1 else 'green'}]
    return f'execute if score @s mg.gfp matches {lo}..{hi} run return run title @s actionbar {js(comps)}'


for club in (1, 2):
    lines = [f'# @s : barre d\'action (jauge) — {"bois/fer" if club == 1 else "putter"} ; $COL remplacé par couleur du joueur']
    for k in range(BAR + 1):
        lo, hi = (0, 2) if k == 0 else (k * 5 - 2, k * 5 + 2)
        if k == BAR:
            hi = 100
        lines.append(bar_line(lo, hi, k, club))
    w(f'golf/bar{club}', ['# @s : couleur du joueur → golf/bar' + str(club) + '_c'] +
      [f'execute if score $gfcol mg.st matches {k} run return run function mg:golf/bar{club}_{k}' for k in range(len(COLORS))])
    for k, c in enumerate(COLORS):
        w(f'golf/bar{club}_{k}', [l.replace('$COL', c[2]) for l in lines])

w('golf/aim', ['# @s : visée (balle à l\'arrêt) : jauge, barre d\'action, ligne de visée, tir au clic droit',
               'scoreboard players remove @s[scores={mg.gfk=1..}] mg.gfk 1', 'function mg:golf/own',
               'execute unless entity @e[tag=mg.gfmy] run return run tag @e[tag=mg.gfmy] remove mg.gfmy',
               'execute unless entity @e[tag=mg.gfmy,distance=..5] run function mg:golf/place',
               'scoreboard players set $gfclub mg.st 0',
               'execute if items entity @s weapon.mainhand minecraft:warped_fungus_on_a_stick[custom_data~{golf:1}] run scoreboard players set $gfclub mg.st 1',
               'execute if items entity @s weapon.mainhand minecraft:warped_fungus_on_a_stick[custom_data~{golf:2}] run scoreboard players set $gfclub mg.st 2',
               'scoreboard players operation $gfnc mg.st = @s mg.gfc', 'scoreboard players add $gfnc mg.st 1',
               'scoreboard players operation $gfcol mg.st = @s mg.gfi', 'scoreboard players operation $gfcol mg.st %= #gf8 mg.st',
               'execute if score $gfclub mg.st matches 0 run title @s actionbar [{"text":"⛳ Prends un club en main : ","color":"gray"},{"text":"Bois/Fer","color":"gold"},{"text":" (vol) ou ","color":"gray"},{"text":"Putter","color":"green"},{"text":" (roule)","color":"gray"}]',
               'execute if score $gfclub mg.st matches 1.. if score @s mg.gfk matches ..0 run function mg:golf/gauge',
               'execute if score $gfclub mg.st matches 1 run scoreboard players operation $gfe mg.st = @s mg.gfp',
               'execute if score $gfclub mg.st matches 1 run scoreboard players operation $gfe mg.st *= #gfest1 mg.st',
               'execute if score $gfclub mg.st matches 2 run scoreboard players operation $gfe mg.st = @s mg.gfp',
               'execute if score $gfclub mg.st matches 2 run scoreboard players operation $gfe mg.st *= #gfest2 mg.st',
               'scoreboard players operation $gfe mg.st /= #gf100 mg.st',
               'execute if score $gfclub mg.st matches 1 run scoreboard players add $gfe mg.st 6',
               'execute if score $gfclub mg.st matches 1 run function mg:golf/bar1',
               'execute if score $gfclub mg.st matches 2 run function mg:golf/bar2',
               # ligne de visée (pointillés devant la balle, visibles par lui seul)
               'scoreboard players operation $gfq mg.st = $gft mg.st', 'scoreboard players operation $gfq mg.st %= #gf4 mg.st',
               'tag @s add mg.gfme',
               'execute if score $gfq mg.st matches 0 if score $gfclub mg.st matches 1.. as @e[tag=mg.gfmy,limit=1] at @s rotated as @a[tag=mg.gfme,limit=1] rotated ~ 0 run function mg:golf/aimline',
               'execute if score @s mg.qs matches 1.. if score $gfclub mg.st matches 1.. if score @s mg.gfk matches ..0 run function mg:golf/shoot',
               'tag @s remove mg.gfme', 'tag @e[tag=mg.gfmy] remove mg.gfmy'])
w('golf/aimline', ['# @s = balle, orientée comme le regard du joueur (mg.gfme)'] +
  [f'particle minecraft:dust{{color:[1.0,1.0,1.0],scale:0.5}} ^ ^0.15 ^{d} 0 0 0 0 1 force @a[tag=mg.gfme]' for d in (1, 1.75, 2.5, 3.25, 4, 5, 6)])
w('golf/gauge', ['# @s : jauge qui oscille 0 → 100 → 0 (bois : 3 %/tick, putter : 2 %/tick)',
                 'scoreboard players set $gfgs mg.st 3', 'execute if score $gfclub mg.st matches 2 run scoreboard players set $gfgs mg.st 2',
                 'scoreboard players operation $gfgs mg.st *= @s mg.gfq', 'scoreboard players operation @s mg.gfp += $gfgs mg.st',
                 'execute if score @s mg.gfp matches 100.. run scoreboard players set @s mg.gfq -1',
                 'execute if score @s mg.gfp matches 100.. run scoreboard players set @s mg.gfp 100',
                 'execute if score @s mg.gfp matches ..0 run scoreboard players set @s mg.gfq 1',
                 'execute if score @s mg.gfp matches ..0 run scoreboard players set @s mg.gfp 0'])
w('golf/shoot', ['# @s : frappe ! (balle mg.gfmy, joueur mg.gfme, $gfclub = 1 bois/fer, 2 putter)',
                 'scoreboard players reset @s mg.qs', 'scoreboard players add @s mg.gfc 1', 'scoreboard players set @s mg.gfs 1',
                 'scoreboard players operation $gfpw mg.st = @s mg.gfp', 'execute if score $gfpw mg.st matches ..2 run scoreboard players set $gfpw mg.st 3',
                 # direction (vecteur unitaire ×1000) : marqueur 10 blocs devant la balle
                 'execute as @e[tag=mg.gfmy,limit=1] at @s rotated as @a[tag=mg.gfme,limit=1] rotated ~ 0 positioned ^ ^ ^10 summon minecraft:marker run function mg:golf/dir',
                 'execute if score $gfclub mg.st matches 1 run function mg:golf/v_wood',
                 'execute if score $gfclub mg.st matches 2 run function mg:golf/v_putt',
                 'execute as @e[tag=mg.gfmy,limit=1] run function mg:golf/launch',
                 'execute if score $gfclub mg.st matches 1 run playsound minecraft:entity.player.attack.strong master @a ~ ~ ~ 1 1.4',
                 'execute if score $gfclub mg.st matches 2 run playsound minecraft:block.note_block.hat master @a ~ ~ ~ 1 1.6',
                 'title @s actionbar ""'])
w('golf/dir', ['# @s = marqueur 10 blocs devant la balle → $gfux / $gfuz (×1000)',
               'execute store result score $gfux mg.st run data get entity @s Pos[0] 1000',
               'execute store result score $gfuz mg.st run data get entity @s Pos[2] 1000',
               'scoreboard players operation $gfux mg.st -= @e[tag=mg.gfmy,limit=1] mg.gfx', 'scoreboard players operation $gfuz mg.st -= @e[tag=mg.gfmy,limit=1] mg.gfz',
               'scoreboard players operation $gfux mg.st /= #gf10 mg.st', 'scoreboard players operation $gfuz mg.st /= #gf10 mg.st',
               'kill @s'])
w('golf/v_wood', ['# Bois/Fer : vitesse ∝ √puissance (distance ≈ proportionnelle à la jauge), élévation ~25°',
                  'scoreboard players operation $gfsq mg.st = $gfpw mg.st', 'scoreboard players operation $gfsq mg.st *= #gf10000 mg.st',
                  'function mg:golf/isqrt',
                  'scoreboard players operation $gfvx mg.st = $gfux mg.st', 'scoreboard players operation $gfvx mg.st *= $gfsr mg.st',
                  'scoreboard players operation $gfvz mg.st = $gfuz mg.st', 'scoreboard players operation $gfvz mg.st *= $gfsr mg.st',
                  f'scoreboard players set $gfk mg.st {WOOD_H}',
                  'scoreboard players operation $gfvx mg.st *= $gfk mg.st', 'scoreboard players operation $gfvz mg.st *= $gfk mg.st',
                  'scoreboard players operation $gfvx mg.st /= #gf10000 mg.st', 'scoreboard players operation $gfvz mg.st /= #gf10000 mg.st',
                  'scoreboard players operation $gfvy mg.st = $gfsr mg.st'])
w('golf/v_putt', ['# Putter : vitesse ∝ puissance, au ras du sol',
                  'scoreboard players operation $gfvx mg.st = $gfux mg.st', 'scoreboard players operation $gfvx mg.st *= $gfpw mg.st',
                  'scoreboard players operation $gfvz mg.st = $gfuz mg.st', 'scoreboard players operation $gfvz mg.st *= $gfpw mg.st',
                  f'scoreboard players set $gfk mg.st {PUTT_H}',
                  'scoreboard players operation $gfvx mg.st *= $gfk mg.st', 'scoreboard players operation $gfvz mg.st *= $gfk mg.st',
                  'scoreboard players operation $gfvx mg.st /= #gf1000 mg.st', 'scoreboard players operation $gfvz mg.st /= #gf1000 mg.st',
                  'scoreboard players set $gfvy mg.st 0'])
w('golf/launch', ['# @s = balle : reçoit la vitesse ($gfvx/$gfvy/$gfvz) et se met en mouvement',
                  'scoreboard players operation @s mg.gfu = $gfvx mg.st', 'scoreboard players operation @s mg.gfv = $gfvy mg.st',
                  'scoreboard players operation @s mg.gfw = $gfvz mg.st', 'tag @s add mg.gfmv',
                  'execute if score $gfvy mg.st matches 1.. run tag @s remove mg.gfg',
                  'execute at @s run particle minecraft:cloud ~ ~0.1 ~ 0.1 0.05 0.1 0.02 4'])

# --- physique de la balle
w('golf/ball', ['# @s = balle en mouvement, chaque tick : gravité, traînée, 4 sous-pas (collisions), sol, hors-jeu, trace',
                'function mg:golf/speed', 'scoreboard players operation $gfsp0 mg.st = $gfsp mg.st',
                f'scoreboard players remove @s mg.gfv {G}',
                'execute unless entity @s[tag=mg.gfg] run function mg:golf/drag'] +
  ['execute if entity @s[tag=mg.gfmv] run function mg:golf/sub'] * SUB +
  ['execute unless entity @s[tag=mg.gfmv] run return 0',
   'tag @s remove mg.gfg',
   'execute at @s unless block ~ ~-0.05 ~ #mg:golf_pass run function mg:golf/roll',
   'execute unless entity @s[tag=mg.gfmv] run return 0',
   'execute if score @s mg.gfy matches ..56000 run return run function mg:golf/penalty_void',
   f'execute unless score @s mg.gfx matches {(X0 - R - 2) * 1000}..{(X0 + R + 2) * 1000} run return run function mg:golf/penalty_void',
   f'execute unless score @s mg.gfz matches {(Z0 - R - 2) * 1000}..{(Z0 + R + 2) * 1000} run return run function mg:golf/penalty_void',
   'execute unless entity @s[tag=mg.gfg] run function mg:golf/trail'])
w('golf/speed', ['# $gfsp = |vx| + |vz| de @s', 'scoreboard players operation $gfsp mg.st = @s mg.gfu',
                 'execute if score $gfsp mg.st matches ..-1 run scoreboard players operation $gfsp mg.st *= #gfm1 mg.st',
                 'scoreboard players operation $gfs2 mg.st = @s mg.gfw',
                 'execute if score $gfs2 mg.st matches ..-1 run scoreboard players operation $gfs2 mg.st *= #gfm1 mg.st',
                 'scoreboard players operation $gfsp mg.st += $gfs2 mg.st'])
w('golf/drag', ['# Traînée de l\'air', 'scoreboard players operation @s mg.gfu *= #gfdrag mg.st', 'scoreboard players operation @s mg.gfu /= #gf1000 mg.st',
                'scoreboard players operation @s mg.gfv *= #gfdrag mg.st', 'scoreboard players operation @s mg.gfv /= #gf1000 mg.st',
                'scoreboard players operation @s mg.gfw *= #gfdrag mg.st', 'scoreboard players operation @s mg.gfw /= #gf1000 mg.st'])
w('golf/trail', ['# Trace de particules (couleur du joueur)', 'scoreboard players operation $gfcol mg.st = @s mg.gfi',
                 'scoreboard players operation $gfcol mg.st %= #gf8 mg.st'] +
  [f'execute if score $gfcol mg.st matches {k} run particle minecraft:dust{{color:[{c[1]}],scale:1.2}} ~ ~0.15 ~ 0 0 0 0 1 force @a[tag=!mg.surv]'
   for k, c in enumerate(COLORS)])
w('golf/sub', ['# Sous-pas : x, z puis y (chacun annulé / rebondi si la balle entre dans un bloc plein)',
               f'scoreboard players operation $gfd mg.st = @s mg.gfu', f'scoreboard players operation $gfd mg.st /= #gf{SUB} mg.st',
               'scoreboard players operation @s mg.gfx += $gfd mg.st',
               'execute store result entity @s Pos[0] double 0.001 run scoreboard players get @s mg.gfx',
               'execute at @s unless block ~ ~0.05 ~ #mg:golf_pass run function mg:golf/hit_x',
               f'scoreboard players operation $gfd mg.st = @s mg.gfw', f'scoreboard players operation $gfd mg.st /= #gf{SUB} mg.st',
               'scoreboard players operation @s mg.gfz += $gfd mg.st',
               'execute store result entity @s Pos[2] double 0.001 run scoreboard players get @s mg.gfz',
               'execute at @s unless block ~ ~0.05 ~ #mg:golf_pass run function mg:golf/hit_z',
               f'scoreboard players operation $gfd mg.st = @s mg.gfv', f'scoreboard players operation $gfd mg.st /= #gf{SUB} mg.st',
               'scoreboard players operation @s mg.gfy += $gfd mg.st',
               'execute store result entity @s Pos[1] double 0.001 run scoreboard players get @s mg.gfy',
               'execute if score $gfd mg.st matches ..-1 at @s unless block ~ ~ ~ #mg:golf_pass run function mg:golf/hit_down',
               'execute if score $gfd mg.st matches 1.. at @s unless block ~ ~ ~ #mg:golf_pass run function mg:golf/hit_up',
               'execute unless entity @s[tag=mg.gfmv] run return 0',
               'execute at @s if block ~ ~ ~ minecraft:water run return run function mg:golf/penalty_water',
               f'execute if score $gfsp0 mg.st matches ..{HOLE_V} at @s if block ~ ~-0.2 ~ minecraft:cauldron run function mg:golf/holed'])
for ax, sc, pos in (('x', 'mg.gfu', 0), ('z', 'mg.gfw', 2)):
    other = 'mg.gfw' if ax == 'x' else 'mg.gfu'
    w(f'golf/hit_{ax}', [f'# Collision en {ax} : marche d\'un bloc franchie en roulant, sinon retour et rebond (−40 %)',
                         f'execute if entity @s[tag=mg.gfg] if score $gfsp0 mg.st matches 60.. at @s if block ~ ~1.05 ~ #mg:golf_pass run return run function mg:golf/step_up',
                         f'scoreboard players operation @s mg.gf{ax} -= $gfd mg.st',
                         f'execute store result entity @s Pos[{pos}] double 0.001 run scoreboard players get @s mg.gf{ax}',
                         f'scoreboard players operation @s {sc} *= #gfm1 mg.st', f'scoreboard players set $gfk mg.st 4',
                         f'scoreboard players operation @s {sc} *= $gfk mg.st', f'scoreboard players operation @s {sc} /= #gf10 mg.st',
                         'execute if score $gfsp0 mg.st matches 200.. at @s run playsound minecraft:block.wood.hit master @a ~ ~ ~ 0.6 1.6'])
w('golf/step_up', ['# Monte une marche d\'un bloc (en roulant) : perd 40 % de sa vitesse',
                   'scoreboard players operation @s mg.gfy /= #gf1000 mg.st', 'scoreboard players add @s mg.gfy 1',
                   'scoreboard players operation @s mg.gfy *= #gf1000 mg.st',
                   'execute store result entity @s Pos[1] double 0.001 run scoreboard players get @s mg.gfy',
                   'scoreboard players set $gfk mg.st 6',
                   'scoreboard players operation @s mg.gfu *= $gfk mg.st', 'scoreboard players operation @s mg.gfu /= #gf10 mg.st',
                   'scoreboard players operation @s mg.gfw *= $gfk mg.st', 'scoreboard players operation @s mg.gfw /= #gf10 mg.st'])
w('golf/hit_down', ['# Touche le sol en descendant : dans la cuve = rentrée ; sinon posée sur le bloc, rebond si l\'impact est fort',
                    'execute if score @s mg.gfv matches ..-150 at @s if block ~ ~ ~ minecraft:cauldron run return run function mg:golf/holed',
                    f'execute if score $gfsp0 mg.st matches ..{HOLE_V} at @s if block ~ ~ ~ minecraft:cauldron run return run function mg:golf/holed',
                    'scoreboard players operation @s mg.gfy /= #gf1000 mg.st', 'scoreboard players add @s mg.gfy 1',
                    'scoreboard players operation @s mg.gfy *= #gf1000 mg.st',
                    'execute store result entity @s Pos[1] double 0.001 run scoreboard players get @s mg.gfy',
                    'execute if score @s mg.gfv matches ..-150 at @s run return run function mg:golf/bounce',
                    'scoreboard players set @s mg.gfv 0'])
w('golf/hit_up', ['# Touche un plafond en montant', 'scoreboard players operation @s mg.gfy -= $gfd mg.st',
                  'execute store result entity @s Pos[1] double 0.001 run scoreboard players get @s mg.gfy', 'scoreboard players set @s mg.gfv 0'])
w('golf/surf', ['# Surface sous la balle → $gff frottement en roulant (‰ gardés / tick), $gfr restitution, $gfh vitesse gardée à l\'impact',
                'scoreboard players set $gff mg.st 900', 'scoreboard players set $gfr mg.st 450', 'scoreboard players set $gfh mg.st 750',
                'execute if block ~ ~-0.05 ~ #mg:golf_green run return run function mg:golf/s_green',
                'execute if block ~ ~-0.05 ~ #mg:golf_fairway run return run function mg:golf/s_fair',
                'execute if block ~ ~-0.05 ~ #mg:golf_rough run return run function mg:golf/s_rough',
                'execute if block ~ ~-0.05 ~ minecraft:sand run return run function mg:golf/s_sand'])
for nm, (f_, r_, h_) in {'green': (955, 250, 800), 'fair': (925, 300, 720), 'rough': (840, 180, 500), 'sand': (560, 0, 150)}.items():
    w(f'golf/s_{nm}', [f'scoreboard players set $gff mg.st {f_}', f'scoreboard players set $gfr mg.st {r_}', f'scoreboard players set $gfh mg.st {h_}'])
for nm, vals in {'golf_green': ['lime_concrete', 'lime_wool', 'cauldron'], 'golf_fairway': ['moss_block', 'green_concrete'],
                 'golf_rough': ['grass_block', 'podzol', 'coarse_dirt', 'dirt']}.items():
    with open(os.path.join(tag_dir, nm + '.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(js({'values': ['minecraft:' + v for v in vals]}) + '\n')
w('golf/bounce', ['# Rebond (impact) selon la surface', 'function mg:golf/surf',
                  'scoreboard players operation @s mg.gfv *= #gfm1 mg.st', 'scoreboard players operation @s mg.gfv *= $gfr mg.st',
                  'scoreboard players operation @s mg.gfv /= #gf1000 mg.st',
                  'scoreboard players operation @s mg.gfu *= $gfh mg.st', 'scoreboard players operation @s mg.gfu /= #gf1000 mg.st',
                  'scoreboard players operation @s mg.gfw *= $gfh mg.st', 'scoreboard players operation @s mg.gfw /= #gf1000 mg.st',
                  'execute if score @s mg.gfv matches ..80 run scoreboard players set @s mg.gfv 0',
                  'playsound minecraft:block.wood.hit master @a ~ ~ ~ 0.5 1.8',
                  'execute if block ~ ~-0.05 ~ minecraft:sand run particle minecraft:block{block_state:"minecraft:sand"} ~ ~0.1 ~ 0.2 0.1 0.2 0 12 force',
                  'execute if block ~ ~-0.05 ~ minecraft:sand run playsound minecraft:block.sand.fall master @a ~ ~ ~ 1 0.8'])
w('golf/roll', ['# Au sol en fin de tick : frottement selon la surface, point sec mémorisé, arrêt sous le seuil',
                'tag @s add mg.gfg', 'function mg:golf/surf',
                'scoreboard players operation @s mg.gfu *= $gff mg.st', 'scoreboard players operation @s mg.gfu /= #gf1000 mg.st',
                'scoreboard players operation @s mg.gfw *= $gff mg.st', 'scoreboard players operation @s mg.gfw /= #gf1000 mg.st',
                'execute unless block ~ ~-0.05 ~ #minecraft:leaves unless block ~ ~-0.05 ~ #minecraft:logs run function mg:golf/dry',
                'function mg:golf/speed',
                'execute if score $gfsp mg.st matches ..24 if score @s mg.gfv matches -60..60 run function mg:golf/stop'])
w('golf/dry', ['# Dernier point sec (au sol, hors arbre) : la balle y revient après eau / vide / arbre',
               'scoreboard players operation @s mg.gflx = @s mg.gfx', 'scoreboard players operation @s mg.gfly = @s mg.gfy',
               'scoreboard players operation @s mg.gflz = @s mg.gfz'])
w('golf/stop', ['# @s = balle arrêtée', 'tag @s remove mg.gfmv', 'scoreboard players set @s mg.gfu 0', 'scoreboard players set @s mg.gfv 0',
                'scoreboard players set @s mg.gfw 0',
                'execute at @s if block ~ ~-0.05 ~ #minecraft:leaves run return run function mg:golf/penalty_tree',
                'execute at @s if block ~ ~-0.05 ~ #minecraft:logs run return run function mg:golf/penalty_tree',
                'execute at @s if block ~ ~-0.2 ~ minecraft:cauldron run return run function mg:golf/holed',
                'scoreboard players operation $cur mg.st = @s mg.gfi',
                f'execute as {PL} if score @s mg.gfi = $cur mg.st run function mg:golf/next'])
for kind, msg, snd in (('water', '💦 Plouf ! Balle à l\'eau', 'minecraft:entity.generic.splash'), ('void', '🌌 Balle hors limites', 'minecraft:entity.enderman.teleport'),
                       ('tree', '🌳 Balle injouable dans un arbre', 'minecraft:block.azalea_leaves.break')):
    w(f'golf/penalty_{kind}', [f'# @s = balle : {msg} → +1 coup, replacée au dernier point sec',
                               f'execute at @s run playsound {snd} master @a ~ ~ ~ 1 1',
                               'execute at @s run particle minecraft:splash ~ ~0.5 ~ 0.3 0.3 0.3 0 30 force' if kind == 'water' else
                               'execute at @s run particle minecraft:poof ~ ~0.3 ~ 0.2 0.2 0.2 0.02 10 force',
                               'scoreboard players operation $cur mg.st = @s mg.gfi',
                               f'execute as {PL} if score @s mg.gfi = $cur mg.st run tellraw @s ' +
                               js([{'text': msg, 'color': 'aqua'}, {'text': ' : +1 coup, balle replacée.', 'color': 'gray'}]),
                               f'execute as {PL} if score @s mg.gfi = $cur mg.st run scoreboard players add @s mg.gfc 1',
                               'scoreboard players operation @s mg.gfx = @s mg.gflx', 'scoreboard players operation @s mg.gfy = @s mg.gfly',
                               'scoreboard players operation @s mg.gfz = @s mg.gflz',
                               'execute store result entity @s Pos[0] double 0.001 run scoreboard players get @s mg.gfx',
                               'execute store result entity @s Pos[1] double 0.001 run scoreboard players get @s mg.gfy',
                               'execute store result entity @s Pos[2] double 0.001 run scoreboard players get @s mg.gfz',
                               'tag @s add mg.gfg',
                               'tag @s remove mg.gfmv', 'scoreboard players set @s mg.gfu 0', 'scoreboard players set @s mg.gfv 0',
                               'scoreboard players set @s mg.gfw 0',
                               f'execute as {PL} if score @s mg.gfi = $cur mg.st run function mg:golf/next'])
w('golf/next', ['# @s : sa balle vient de s\'arrêter (pas dans le trou)', 'execute unless score @s mg.gfs matches 1 run return 0',
                f'execute if score @s mg.gfc matches {MAXS}.. run return run function mg:golf/give_up',
                'function mg:golf/stroke_start',
                'function mg:golf/own',
                'execute at @e[tag=mg.gfmy,limit=1] if block ~ ~-0.05 ~ #mg:golf_green run title @s actionbar {"text":"Sur le green : prends le Putter !","color":"green"}',
                'tag @e[tag=mg.gfmy] remove mg.gfmy'])
w('golf/give_up', ['# @s : 8 coups sans rentrer la balle → trou abandonné (compte 8)', f'scoreboard players set @s mg.gfc {MAXS}',
                   f'tellraw {PL} ' + js([{'text': '⛳ ', 'color': 'green'}, {'selector': '@s', 'color': 'yellow'},
                                         {'text': f' abandonne le trou ({MAXS} coups).', 'color': 'gray'}]),
                   'function mg:golf/own', 'kill @e[tag=mg.gfmy]', 'function mg:golf/score'])
w('golf/timeout', ['# @s : temps écoulé sans finir le trou → compte 8', f'scoreboard players set @s mg.gfc {MAXS}',
                   f'tellraw {PL} ' + js([{'text': '⏱ ', 'color': 'gold'}, {'selector': '@s', 'color': 'yellow'},
                                         {'text': f' n\'a pas fini à temps ({MAXS} coups).', 'color': 'gray'}]),
                   'function mg:golf/own', 'kill @e[tag=mg.gfmy]', 'function mg:golf/score'])
w('golf/holed', ['# @s = balle dans le trou !', 'tag @s remove mg.gfmv', 'tag @s add mg.gfin',
                 'scoreboard players set @s mg.gfu 0', 'scoreboard players set @s mg.gfv 0', 'scoreboard players set @s mg.gfw 0',
                 'tp @s @e[tag=mg.gftg,limit=1]', 'execute at @s run tp @s ~ ~-0.55 ~',
                 'execute at @s run particle minecraft:firework ~ ~0.8 ~ 0.3 0.6 0.3 0.08 40 force',
                 'execute at @s run particle minecraft:happy_villager ~ ~0.5 ~ 0.6 0.3 0.6 0 15 force',
                 'execute at @s run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 1 0.8',
                 'scoreboard players operation $cur mg.st = @s mg.gfi',
                 f'execute as {PL} if score @s mg.gfi = $cur mg.st run function mg:golf/in'])
REL = [(-99, -4, '🦅 Condor', 'light_purple'), (-3, -3, '🦅 Albatros !', 'light_purple'), (-2, -2, '🦅 Eagle !', 'gold'),
       (-1, -1, '🐦 Birdie !', 'green'), (0, 0, 'Par', 'white'), (1, 1, 'Bogey', 'yellow'), (2, 2, 'Double bogey', 'red'),
       (3, 99, 'Triple bogey ou pire', 'dark_red')]
IN = ['# @s : a rentré sa balle', 'execute unless score @s mg.gfs matches 0..1 run return 0',
      'scoreboard players operation $gfrel mg.st = @s mg.gfc', 'scoreboard players operation $gfrel mg.st -= $gfpar mg.st',
      'execute if score @s mg.gfc matches 1 run return run function mg:golf/ace']
for lo, hi, txt, col in REL:
    IN.append(f'execute if score $gfrel mg.st matches {lo}..{hi} run tellraw {PL} ' +
              js([{'text': '⛳ ', 'color': 'green'}, {'selector': '@s', 'color': 'yellow'}, {'text': ' rentre en ', 'color': 'gray'},
                  {'score': {'name': '@s', 'objective': 'mg.gfc'}, 'color': 'white', 'bold': True}, {'text': ' coup(s) — ', 'color': 'gray'},
                  {'text': txt, 'color': col, 'bold': True}]))
    IN.append(f'execute if score $gfrel mg.st matches {lo}..{hi} run title @s title ' + js({'text': txt, 'color': col, 'bold': True}))
IN += ['execute if score $gfrel mg.st matches ..-1 at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.2',
       'function mg:golf/score']
w('golf/in', IN)
w('golf/ace', ['# @s : TROU EN UN !', f'tellraw @a[tag=!mg.surv] ' + js([{'text': '⛳ TROU EN UN ! ', 'color': 'gold', 'bold': True},
                                                                       {'selector': '@s', 'color': 'yellow'}, {'text': ' réussit le coup parfait !', 'color': 'gold'}]),
               f'title {PL} title ' + js({'text': 'TROU EN UN !', 'color': 'gold', 'bold': True}),
               f'title {PL} subtitle [{{"selector":"@s","color":"yellow"}}]',
               'execute at @s run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:20,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1,explosions:[{shape:"star",colors:[I;16766720,16777215],has_trail:true}]}}}}',
               'execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1',
               'function mg:golf/score'])
w('golf/score', ['# @s : trou fini (mg.gfc coups) → total, tableau (−total, affiché comme « total (écart au par) »)',
                 'scoreboard players set @s mg.gfs 2', 'scoreboard players operation @s mg.gft += @s mg.gfc',
                 'scoreboard players operation @s mg.gfd = @s mg.gft', 'scoreboard players operation @s mg.gfd *= #gfm1 mg.st',
                 'function mg:golf/sb_fmt'])
w('golf/sb_fmt', ['# @s : texte de sa ligne au tableau', 'execute store result storage mg:golf f.t int 1 run scoreboard players get @s mg.gft',
                  'scoreboard players operation $gfrel mg.st = @s mg.gft', 'scoreboard players operation $gfrel mg.st -= $gfpc mg.st',
                  'execute store result storage mg:golf f.n int 1 run scoreboard players get $gfrel mg.st',
                  'data modify storage mg:golf f.p set value ""', 'data modify storage mg:golf f.c set value "green"',
                  'execute if score $gfrel mg.st matches 0 run data modify storage mg:golf f.p set value "±"',
                  'execute if score $gfrel mg.st matches 0 run data modify storage mg:golf f.c set value "white"',
                  'execute if score $gfrel mg.st matches 1.. run data modify storage mg:golf f.p set value "+"',
                  'execute if score $gfrel mg.st matches 1.. run data modify storage mg:golf f.c set value "red"',
                  'function mg:golf/sb_set with storage mg:golf f'])
w('golf/sb_set', ['# (macro) t total, p signe, n écart au par, c couleur',
                  '$scoreboard players display numberformat @s mg.gfd fixed [{"text":"$(t)","color":"white","bold":true},{"text":" ($(p)$(n))","color":"$(c)"}]'])
w('golf/finish', ['# Fin des 6 trous : le plus petit total gagne (égalité = match nul)',
                  'execute unless score $state mg.st matches 2 run return 0',
                  f'tellraw {PL} ' + js([{'text': '⛳ Parcours terminé ! ', 'color': 'green', 'bold': True}, {'text': f'(par {sum(h["par"] for h in HOLES)})', 'color': 'gray'}]),
                  f'execute as {PL} run tellraw {PL} [{{"text":"  ","color":"gray"}},{{"selector":"@s","color":"yellow"}},{{"text":" : ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.gft"}},"color":"white","bold":true}},{{"text":" coups","color":"gray"}}]',
                  'scoreboard players set $gfmin mg.st 999', f'scoreboard players operation $gfmin mg.st < {PL} mg.gft',
                  'scoreboard players set $gfnb mg.st 0',
                  f'execute as {PL} if score @s mg.gft = $gfmin mg.st run scoreboard players add $gfnb mg.st 1',
                  'execute if score $gfnb mg.st matches 2.. run return run function mg:core/draw',
                  f'execute as {PL} if score @s mg.gft = $gfmin mg.st run function mg:core/win_player'])
w('golf/cleanup', ['# ⛳ Golf : nettoyage (entités, clubs, équipe, zone chargée)',
                   'kill @e[tag=mg.gfb]', 'kill @e[tag=mg.gff]', 'kill @e[tag=mg.gftg]',
                   'clear @a minecraft:warped_fungus_on_a_stick[custom_data~{golf:1}]', 'clear @a minecraft:warped_fungus_on_a_stick[custom_data~{golf:2}]',
                   'team leave @a[team=mg_golf]', 'effect clear @a[tag=mg.play] minecraft:resistance',
                   'scoreboard players reset * mg.gfs', 'scoreboard players reset * mg.gfd', 'scoreboard players reset * mg.gfi',
                   'tag @a remove mg.gfme', 'scoreboard players set $gfok mg.st 0',
                   'schedule clear mg:golf/wait'] + [f'schedule clear mg:golf/build_{k}' for k in range(1, NP)] +
  [f'forceload remove {FX} {FZ} {FX2} {FZ2}'])

# --- objectifs, équipe, constantes
OBJ = [('mg.gft', 'dummy'), ('mg.gfc', 'dummy'), ('mg.gfd', 'dummy {"text":"⛳ GOLF — coups","color":"green","bold":true}'),
       ('mg.gfi', 'dummy'), ('mg.gfs', 'dummy'), ('mg.gfp', 'dummy'), ('mg.gfq', 'dummy'), ('mg.gfm', 'dummy'), ('mg.gfk', 'dummy'),
       ('mg.gfx', 'dummy'), ('mg.gfy', 'dummy'), ('mg.gfz', 'dummy'), ('mg.gfu', 'dummy'), ('mg.gfv', 'dummy'), ('mg.gfw', 'dummy'),
       ('mg.gflx', 'dummy'), ('mg.gfly', 'dummy'), ('mg.gflz', 'dummy')]
w('golf/load', ['# ⛳ Golf : objectifs, équipe (sans collision entre joueurs), constantes (branché par le coordinateur ou via C.objectives)'] +
  [f'scoreboard objectives add {n} {c}' for n, c in OBJ] +
  ['team add mg_golf', 'team modify mg_golf collisionRule never', 'team modify mg_golf color green',
   'scoreboard players set #gfest1 mg.st 93', 'scoreboard players set #gfest2 mg.st 16'])
w('golf/remove', ['# ⛳ Golf : désinstallation'] + [f'scoreboard objectives remove {n}' for n, c in OBJ] +
  ['team remove mg_golf', 'schedule clear mg:golf/wait'] + [f'schedule clear mg:golf/build_{k}' for k in range(1, NP)] +
  [f'forceload remove {FX} {FZ} {FX2} {FZ2}'])

C.register([GID], 'golf', [C.announce(GID, '', '⛳ GOLF', 'green', '6 trous façon Wii Sports, le moins de coups gagne !')])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger', ['function mg:golf/load'])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['function mg:golf/remove'])
print(f'Golf OK : {len(BUILD) + len(DECO)} commandes de construction en {NP} étapes, {len(TREES)} arbres')
