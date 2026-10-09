"""💣 Bombardier (id 99) : une grande ville façon Manhattan vue du ciel, on largue des bombes, le plus de dégâts gagne.

    python tools/arcade/gen_bomber.py .

- La ville (177 × 177, centre 0 64 32400) : avenues nord-sud, rues est-ouest, gratte-ciel de verre, immeubles de brique
  avec châteaux d'eau, tours art déco à gradins, deux géants (Empire et Chrysler), un carrefour à écrans, Central Park
  avec son lac, l'East River avec un pont suspendu et une statue verte sur son île. Taxis jaunes, réverbères.
- Les joueurs marchent sur un plancher invisible (barrières) à y 170 et lâchent les bombes sous leurs pieds,
  lancées dans la direction du regard : bombe (rayon 3), méga-bombe (6), bombe à fragmentation (7 sous-munitions
  de rayon 2) et, pour la dernière minute, une bombe atomique (rayon 11) par joueur.
- Dégâts = blocs détruits (bloc doré ou statue : 10 points). Une explosion = fills « replace #mg:bomb_city »
  empilés en sphère (le nombre de blocs remplacés est le score), sans vraie explosion ni objets au sol.
- 2 min 30, le plus gros score gagne. Barre de boss : part de la ville détruite. Reconstruite à chaque partie
  (en 80 étapes pendant le compte à rebours), sol et plancher posés une fois (storage mg:bomber v1).
"""
import math
import os
import random
import sys
import json
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
GID = 99
Z = 32400
HX = 88                      # demi-côté de la ville
Y0, YT = 56, 170             # bas du sol, plancher de barrières
GY = 64                      # surface (routes, trottoirs) ; bâtiments à partir de 65
LIMIT = 3000                 # 2 min 30
NUKE_AT = 1800               # bombe atomique : dernière minute
random.seed(1999)

# ---------------------------------------------------------------- grille de blocs (comptage) + commandes
NX, NY, NZ = 2 * HX + 1, YT - Y0 + 1, 2 * HX + 1
PAL = ['air']
PIDX = {'air': 0}
CITY = set()                 # palette des blocs « destructibles » (posés par la ville, pas par le sol)
GSET = set()                 # blocs du sol : ne doivent jamais être destructibles
grid = bytearray(NX * NY * NZ)


def pid(b, city):
    n = b.split('[')[0].replace('minecraft:', '')
    if n not in PIDX:
        PIDX[n] = len(PAL)
        PAL.append(n)
        assert len(PAL) < 256
    if n != 'air':
        (CITY if city else GSET).add(n)
    return PIDX[n]


def mark(x1, y1, z1, x2, y2, z2, b, city, hollow=False):
    v = pid(b, city)
    for y in range(y1, y2 + 1):
        for z in range(z1, z2 + 1):
            base = ((y - Y0) * NZ + (z + HX)) * NX + HX
            if hollow and y1 < y < y2 and z1 < z < z2:
                grid[base + x1:base + x1 + 1] = bytes([v])
                grid[base + x2:base + x2 + 1] = bytes([v])
                grid[base + x1 + 1:base + x2] = bytes(x2 - x1 - 1)
            else:
                grid[base + x1:base + x2 + 1] = bytes([v]) * (x2 - x1 + 1)


CMDS = []                    # commandes de la ville (reconstruites à chaque partie)
GROUND = []                  # sol, fleuve, plancher (une fois)


def fill(x1, y1, z1, x2, y2, z2, b, city=True, out=None):
    x1, x2 = sorted((x1, x2)); y1, y2 = sorted((y1, y2)); z1, z2 = sorted((z1, z2))
    x1, z1, x2, z2 = max(x1, -HX), max(z1, -HX), min(x2, HX), min(z2, HX)
    if x1 > x2 or z1 > z2:
        return
    out = CMDS if out is None else out
    area = (x2 - x1 + 1) * (z2 - z1 + 1)
    step = max(1, 32768 // area)
    for ya in range(y1, y2 + 1, step):
        yb = min(y2, ya + step - 1)
        out.append(f'fill {x1} {ya} {Z + z1} {x2} {yb} {Z + z2} minecraft:{b}' if (x1, ya, z1) != (x2, yb, z2)
                   else f'setblock {x1} {ya} {Z + z1} minecraft:{b}')
    if Y0 <= y1 and y2 <= YT:
        mark(x1, y1, z1, x2, y2, z2, b if b != 'barrier' else 'air', city)


def put(x, y, z, b, city=True):
    fill(x, y, z, x, y, z, b, city)


# ---------------------------------------------------------------- plan
AV = [-76, -44, -12, 20, 52]                     # avenues (nord-sud), largeur 7
ST = [-78, -54, -30, -6, 18, 42, 66]             # rues (est-ouest), largeur 5
LAND = 64                                        # x > 64 : East River
PARK = (-40, 21, 16, 63)                         # Central Park (x1, z1, x2, z2)
BRIDGE_Z = -30


def spans(centers, half, lo, hi):
    s, prev = [], lo
    for c in centers:
        if c - half - 1 >= prev:
            s.append((prev, c - half - 1))
        prev = c + half + 1
    if prev <= hi:
        s.append((prev, hi))
    return s


LOTX = spans(AV, 3, -HX, LAND)
LOTZ = spans(ST, 2, -HX, HX)


def in_park(x, z):
    return PARK[0] <= x <= PARK[2] and PARK[1] <= z <= PARK[3]


# ---------------------------------------------------------------- sol (une fois)
G = GROUND
for y in range(Y0, YT + 7):
    fill(-HX, y, -HX, HX, y, HX, 'air', False, G)
fill(-HX, Y0, -HX, HX, 60, HX, 'stone', False, G)
fill(-HX, 61, -HX, HX, 63, HX, 'dirt', False, G)
fill(-HX, GY, -HX, LAND, GY, HX, 'smooth_stone', False, G)                   # trottoirs partout, puis chaussées
for c in AV:
    fill(c - 3, GY, -HX, c + 3, GY, HX, 'polished_blackstone', False, G)
    for z in range(-HX, HX + 1, 6):
        fill(c, GY, z, c, GY, z + 2, 'white_concrete_powder', False, G)
for c in ST:
    fill(-HX, GY, c - 2, LAND, GY, c + 2, 'polished_blackstone', False, G)
    for x in range(-HX, LAND + 1, 6):
        fill(x, GY, c, x + 2, GY, c, 'white_concrete_powder', False, G)
for c in AV:                                                                  # passages piétons
    for s in ST:
        for k in range(-2, 3, 2):
            fill(c - 3, GY, s + k, c + 3, GY, s + k, 'white_concrete_powder', False, G)
# East River : quai en pierre taillée, eau, île de la statue
fill(LAND + 1, 57, -HX, HX, 57, HX, 'sand', False, G)
fill(LAND + 1, 58, -HX, HX, 63, HX, 'water', False, G)
fill(LAND + 1, GY, -HX, HX, GY, HX, 'air', False, G)
fill(LAND, 58, -HX, LAND, GY - 1, HX, 'stone', False, G)
G += [f'fill {HX + 1} 57 {Z - HX - 1} {HX + 1} {GY} {Z + HX + 1} minecraft:stone',          # le fleuve ne coule pas hors de la carte
      f'fill {LAND} 57 {Z - HX - 1} {HX} {GY} {Z - HX - 1} minecraft:stone', f'fill {LAND} 57 {Z + HX + 1} {HX} {GY} {Z + HX + 1} minecraft:stone']
for x in range(LAND + 1, HX + 1):
    for z in range(-HX, -58):
        d = math.hypot(x - 78, z + 72)
        if d <= 7.5:
            fill(x, 58, z, x, 63, z, 'sand', False, G)
            put(x, GY, z, 'grass_block' if d <= 6 else 'sand', False)
            G.append(CMDS.pop())
# Central Park : pelouse, allées, lac
px1, pz1, px2, pz2 = PARK
fill(px1, GY, pz1, px2, GY, pz2, 'grass_block', False, G)
fill(px1, 63, pz1, px2, 63, pz2, 'dirt', False, G)
fill(-14, GY, pz1, -10, GY, pz2, 'dirt_path', False, G)
fill(px1, GY, 40, px2, GY, 43, 'dirt_path', False, G)
for z in range(pz1, pz2 + 1):
    for x in range(px1, px2 + 1):
        if math.hypot((x + 26) / 9, (z - 52) / 6) <= 1:
            fill(x, 61, z, x, GY, z, 'water', False, G)
# plancher invisible et murs
fill(-HX, YT, -HX, HX, YT, HX, 'barrier', False, G)
for (a, b, c, d) in [(-HX, -HX, HX, -HX), (-HX, HX, HX, HX), (-HX, -HX, -HX, HX), (HX, -HX, HX, HX)]:
    fill(a, YT + 1, b, c, YT + 6, d, 'barrier', False, G)
GROUND.append('data modify storage mg:bomber v1 set value 1b')

# ---------------------------------------------------------------- bâtiments
STYLES = {
    'glass':  dict(wall=['light_blue_stained_glass', 'cyan_stained_glass', 'gray_stained_glass', 'blue_stained_glass'],
                   frame=['white_concrete', 'light_gray_concrete', 'gray_concrete', 'iron_block'], step=4),
    'brick':  dict(wall=['bricks', 'red_terracotta', 'brown_terracotta', 'terracotta', 'granite'],
                   frame=['black_stained_glass', 'gray_stained_glass'], step=2),
    'deco':   dict(wall=['white_terracotta', 'light_gray_terracotta', 'polished_diorite', 'calcite', 'smooth_sandstone'],
                   frame=['gray_stained_glass', 'black_stained_glass', 'light_gray_stained_glass'], step=3),
    'dark':   dict(wall=['black_concrete', 'gray_concrete', 'polished_deepslate'],
                   frame=['light_blue_stained_glass', 'cyan_stained_glass', 'orange_stained_glass'], step=2),
}
ROOFTOP = []                                       # (x1, z1, x2, z2, top, style) pour les décors de toit


def tower(x1, z1, x2, z2, yb, h, style, wall=None, frame=None, slab=None, roof=True):
    """Bâtiment creux : 4 façades, intérieur vidé, fenêtres en colonnes, planchers tous les 4 blocs."""
    s = STYLES[style]
    wall = wall or random.choice(s['wall'])
    frame = frame or random.choice(s['frame'])
    yt = yb + h - 1
    if style == 'glass':
        glass, solid = wall, frame
    else:
        glass, solid = frame, wall
    fill(x1, yb, z1, x2, yt, z1, solid); fill(x1, yb, z2, x2, yt, z2, solid)
    fill(x1, yb, z1, x1, yt, z2, solid); fill(x2, yb, z1, x2, yt, z2, solid)
    if x2 - x1 >= 2 and z2 - z1 >= 2:
        fill(x1 + 1, yb, z1 + 1, x2 - 1, yt, z2 - 1, 'air')
    # fenêtres (colonnes) : verre continu pour les tours vitrées (montants tous les 4), alternance sinon
    st = s['step']
    w0, w1 = yb + 1, yt - 1
    if w1 > w0:
        for x in range(x1 + 1, x2):
            on = ((x - x1) % st != 0) if style == 'glass' else ((x - x1) % st == 1 or (st == 3 and (x - x1) % 3 == 2))
            if on:
                fill(x, w0, z1, x, w1, z1, glass); fill(x, w0, z2, x, w1, z2, glass)
        for z in range(z1 + 1, z2):
            on = ((z - z1) % st != 0) if style == 'glass' else ((z - z1) % st == 1 or (st == 3 and (z - z1) % 3 == 2))
            if on:
                fill(x1, w0, z, x1, w1, z, glass); fill(x2, w0, z, x2, w1, z, glass)
    # planchers (bandeaux en façade)
    sl = slab or solid
    for y in range(yb + 4, yt, 4):
        fill(x1, y, z1, x2, y, z2, sl)
    fill(x1, yb, z1, x2, yb, z2, sl)
    fill(x1, yt, z1, x2, yt, z2, solid if style != 'glass' else frame)
    if style != 'glass':                          # rez-de-chaussée : vitrines
        for x in range(x1 + 2, x2 - 1, 3):
            fill(x, yb + 1, z1, x + 1, yb + 2, z1, 'glass'); fill(x, yb + 1, z2, x + 1, yb + 2, z2, 'glass')
    if roof:
        ROOFTOP.append((x1, z1, x2, z2, yt, style))
    return yt


def setbacks(x1, z1, x2, z2, yb, h, style, tiers=3):
    """Tour à gradins (art déco) : chaque étage en retrait de 2 blocs."""
    wall = random.choice(STYLES[style]['wall']); frame = random.choice(STYLES[style]['frame'])
    y = yb
    parts = [0.55, 0.3, 0.15][:tiers]
    for i, f in enumerate(parts):
        hh = max(4, int(h * f) // 4 * 4 + 1)
        last = i == len(parts) - 1 or (x2 - x1) < 8 or (z2 - z1) < 8
        top = tower(x1, z1, x2, z2, y, hh, style, wall, frame, roof=last)
        if last:
            return top
        y = top
        x1, z1, x2, z2 = x1 + 2, z1 + 2, x2 - 2, z2 - 2
    return y


def height_for(cx, cz):
    if cx >= 56 or cx <= -80:
        return random.randint(10, 26), 'brick'
    if cz >= 21:                                   # Upper : brownstones et immeubles moyens
        return random.choice([(random.randint(10, 22), 'brick'), (random.randint(18, 34), 'deco')])
    if cz <= -57:                                  # Downtown : grandes tours de verre
        return random.choice([(random.randint(40, 84), 'glass'), (random.randint(30, 60), 'dark'), (random.randint(20, 40), 'deco')])
    return random.choice([(random.randint(28, 72), 'glass'), (random.randint(24, 56), 'deco'),
                          (random.randint(14, 30), 'brick'), (random.randint(26, 52), 'dark')])


LANDMARK_LOTS = {}


def split(a, b, minw):
    n = b - a + 1
    if n < 2 * minw + 1 or random.random() < 0.3:
        return [(a, b)]
    k = random.randint(minw, n - minw - 1)
    return [(a, a + k - 1)] + split(a + k + 1, b, minw)


def empire(x1, z1, x2, z2):
    cx, cz = (x1 + x2) // 2, (z1 + z2) // 2
    W, F = 'smooth_sandstone', 'gray_stained_glass'
    t = tower(x1, z1, x2, z2, 65, 13, 'deco', W, F, roof=False)
    t = tower(cx - 7, cz - 5, cx + 7, cz + 5, t, 49, 'deco', W, F, roof=False)
    t = tower(cx - 5, cz - 4, cx + 5, cz + 4, t, 17, 'deco', W, F, roof=False)
    t = tower(cx - 3, cz - 3, cx + 3, cz + 3, t, 9, 'deco', W, F, roof=False)
    fill(cx - 3, t, cz - 3, cx + 3, t, cz + 3, 'gold_block')
    t = tower(cx - 2, cz - 2, cx + 2, cz + 2, t + 1, 6, 'deco', W, 'light_blue_stained_glass', roof=False)
    fill(cx - 1, t + 1, cz - 1, cx + 1, t + 4, cz + 1, 'gold_block')
    fill(cx, t + 5, cz, cx, t + 14, cz, 'lightning_rod')


def chrysler(x1, z1, x2, z2):
    cx, cz = (x1 + x2) // 2, (z1 + z2) // 2
    W, F = 'white_terracotta', 'black_stained_glass'
    t = tower(x1, z1, x2, z2, 65, 17, 'deco', W, F, roof=False)
    t = tower(cx - 5, cz - 5, cx + 5, cz + 5, t, 45, 'deco', W, F, roof=False)
    for i, r in enumerate([4, 3, 2, 1]):           # couronne en écailles d'acier
        fill(cx - r, t + 1, cz - r, cx + r, t + 4, cz + r, 'iron_block')
        for d in range(-r + 1, r, 2):
            fill(cx + d, t + 2, cz - r, cx + d, t + 3, cz - r, 'black_stained_glass')
            fill(cx + d, t + 2, cz + r, cx + d, t + 3, cz + r, 'black_stained_glass')
            fill(cx - r, t + 2, cz + d, cx - r, t + 3, cz + d, 'black_stained_glass')
            fill(cx + r, t + 2, cz + d, cx + r, t + 3, cz + d, 'black_stained_glass')
        t += 4
    fill(cx, t + 1, cz, cx, t + 2, cz, 'gold_block')
    fill(cx, t + 3, cz, cx, t + 13, cz, 'lightning_rod')


def needle(x1, z1, x2, z2):
    t = tower(x1, z1, x2, z2, 65, 85, 'glass', 'cyan_stained_glass', 'light_gray_concrete', roof=False)
    cx, cz = (x1 + x2) // 2, (z1 + z2) // 2
    t = tower(cx - 2, cz - 2, cx + 2, cz + 2, t, 5, 'glass', 'light_blue_stained_glass', 'iron_block', roof=False)
    fill(cx, t + 1, cz, cx, t + 9, cz, 'lightning_rod')


LANDMARKS = {(-40, -51): empire, (-8, -51): chrysler, (24, -75): needle}
TIMES = (-12, -6)                                  # carrefour à écrans
BILLBOARD = ['red_concrete', 'yellow_concrete', 'lime_concrete', 'magenta_concrete', 'cyan_concrete', 'orange_concrete', 'blue_concrete']

for (lx1, lx2) in LOTX:
    for (lz1, lz2) in LOTZ:
        if in_park(lx1, lz1):
            continue
        bx1, bx2, bz1, bz2 = lx1 + 2, lx2 - 2, lz1 + 2, lz2 - 2
        if bx2 - bx1 < 3 or bz2 - bz1 < 3:
            continue
        if (lx1, lz1) in LANDMARKS:
            LANDMARKS[(lx1, lz1)](bx1, bz1, bx2, bz2)
            continue
        for (ax, bx) in split(bx1, bx2, 6):
            for (az, bz) in split(bz1, bz2, 6):
                h, style = height_for((ax + bx) // 2, (az + bz) // 2)
                if style == 'deco' and h > 30 and bx - ax >= 10 and bz - az >= 10:
                    top = setbacks(ax, az, bx, bz, 65, h, 'deco')
                else:
                    top = tower(ax, az, bx, bz, 65, h, style)
                # carrefour à écrans : panneaux colorés sur les façades qui donnent sur le carrefour
                near = abs((ax + bx) / 2 - TIMES[0]) < 30 and abs((az + bz) / 2 - TIMES[1]) < 24
                if near:
                    fx = bx if (ax + bx) / 2 < TIMES[0] else ax
                    fz = bz if (az + bz) / 2 < TIMES[1] else az
                    for k in range(2):
                        c = random.choice(BILLBOARD)
                        y0 = 68 + k * 8
                        if y0 + 6 < top:
                            fill(fx, y0, az + 1, fx, y0 + 5, bz - 1, c)
                            fill(fx, y0 - 1, az + 1, fx, y0 - 1, bz - 1, 'sea_lantern')
                            fill(ax + 1, y0, fz, bx - 1, y0 + 5, fz, random.choice(BILLBOARD))
                            fill(ax + 1, y0 + 6, fz, bx - 1, y0 + 6, fz, 'glowstone')

# toits : châteaux d'eau, climatiseurs, antennes
for (x1, z1, x2, z2, yt, style) in ROOFTOP:
    w_, d_ = x2 - x1, z2 - z1
    if style in ('brick', 'deco') and w_ >= 6 and d_ >= 6 and random.random() < 0.75:
        tx, tz = random.randint(x1 + 1, x2 - 4), random.randint(z1 + 1, z2 - 4)
        for (lx, lz) in [(tx, tz), (tx + 2, tz), (tx, tz + 2), (tx + 2, tz + 2)]:
            fill(lx, yt + 1, lz, lx, yt + 2, lz, 'stripped_spruce_log')
        fill(tx, yt + 3, tz, tx + 2, yt + 5, tz + 2, 'spruce_planks')
        fill(tx + 1, yt + 3, tz, tx + 1, yt + 5, tz, 'stripped_spruce_wood')
        put(tx + 1, yt + 6, tz + 1, 'spruce_slab')
        fill(tx, yt + 6, tz, tx + 2, yt + 6, tz, 'spruce_slab'); fill(tx, yt + 6, tz + 2, tx + 2, yt + 6, tz + 2, 'spruce_slab')
    elif style in ('glass', 'dark'):
        cx, cz = (x1 + x2) // 2, (z1 + z2) // 2
        if w_ >= 6 and d_ >= 6:
            fill(cx - 2, yt + 1, cz - 2, cx + 1, yt + 3, cz + 1, 'light_gray_concrete')
        put(cx, yt + 4 if w_ >= 6 and d_ >= 6 else yt + 1, cz, 'lightning_rod')
        if yt > 110:
            fill(cx, yt + 5, cz, cx, yt + 8, cz, 'lightning_rod')
    if w_ >= 4 and d_ >= 4 and random.random() < 0.6:
        ax, az = random.randint(x1 + 1, x2 - 2), random.randint(z1 + 1, z2 - 1)
        fill(ax, yt + 1, az, ax + 1, yt + 1, az, 'iron_block')

# ---------------------------------------------------------------- Central Park : arbres, rochers
for _ in range(70):
    x, z = random.randint(px1 + 2, px2 - 2), random.randint(pz1 + 2, pz2 - 2)
    if math.hypot((x + 26) / 10, (z - 52) / 7) <= 1 or -15 <= x <= -9 or 39 <= z <= 44:
        continue
    kind = random.choice(['oak', 'oak', 'birch', 'dark_oak'])
    th = random.randint(4, 6)
    fill(x - 2, 65 + th - 2, z - 2, x + 2, 65 + th - 1, z + 2, f'{kind}_leaves[persistent=true]')
    fill(x - 1, 65 + th, z - 1, x + 1, 65 + th + 1, z + 1, f'{kind}_leaves[persistent=true]')
    fill(x, 65, z, x, 65 + th - 1, z, f'{kind}_log')
for _ in range(8):
    x, z = random.randint(px1 + 3, px2 - 3), random.randint(pz1 + 3, pz2 - 3)
    if not (-15 <= x <= -9 or 39 <= z <= 44) and math.hypot((x + 26) / 10, (z - 52) / 7) > 1:
        fill(x, 65, z, x + 1, 65, z + 1, 'mossy_cobblestone'); put(x, 66, z, 'mossy_cobblestone')
fill(-27, 65, 42, -25, 65, 44, 'chiseled_stone_bricks'); put(-26, 66, 43, 'sea_lantern')

# ---------------------------------------------------------------- rues : taxis, voitures, réverbères
CARS = ['yellow_concrete'] * 5 + ['red_concrete', 'blue_concrete', 'white_concrete', 'black_concrete']
for c in AV:
    for z in range(-HX + 4, HX - 4, 9):
        if in_park(c, z) or any(abs(z - s) <= 4 for s in ST) or random.random() < 0.45:
            continue
        lane = c + random.choice([-2, 2])
        col = random.choice(CARS)
        fill(lane, 65, z, lane, 65, z + 2, col); put(lane, 66, z + 1, 'black_stained_glass')
for s in ST:
    for x in range(-HX + 4, LAND - 4, 9):
        if in_park(x, s) or any(abs(x - c) <= 5 for c in AV) or random.random() < 0.45:
            continue
        lane = s + random.choice([-1, 1])
        col = random.choice(CARS)
        fill(x, 65, lane, x + 2, 65, lane, col); put(x + 1, 66, lane, 'black_stained_glass')
for (lx1, lx2) in LOTX:
    for (lz1, lz2) in LOTZ:
        if in_park(lx1, lz1) or lx2 - lx1 < 6 or lz2 - lz1 < 6:
            continue
        for (x, z) in [(lx1, lz1), (lx2, lz1), (lx1, lz2), (lx2, lz2)]:
            fill(x, 65, z, x, 67, z, 'iron_bars'); put(x, 68, z, 'lantern')

# ---------------------------------------------------------------- pont suspendu (rue BRIDGE_Z) et statue
bz = BRIDGE_Z
fill(LAND - 3, 65, bz - 2, LAND, 68, bz + 2, 'stone_bricks')
fill(LAND - 6, 65, bz - 2, LAND - 4, 65, bz + 2, 'stone_brick_slab')
fill(LAND - 3, 69, bz - 2, HX, 69, bz + 2, 'dark_oak_planks')
fill(LAND - 3, 70, bz - 2, HX, 70, bz - 2, 'dark_oak_fence'); fill(LAND - 3, 70, bz + 2, HX, 70, bz + 2, 'dark_oak_fence')
for tx in (71, 83):
    for zz in (bz - 3, bz + 3):
        fill(tx - 1, 58, zz - 1 if zz < bz else zz, tx + 1, 92, zz if zz < bz else zz + 1, 'stone_bricks')
    fill(tx - 1, 88, bz - 2, tx + 1, 92, bz + 2, 'stone_bricks')
    fill(tx - 1, 88, bz - 1, tx + 1, 90, bz + 1, 'air')
    fill(tx - 1, 58, bz - 2, tx + 1, 68, bz + 2, 'stone_bricks')
for zz in (bz - 3, bz + 3):
    for x in range(LAND - 3, HX + 1):
        if x in (70, 71, 72, 82, 83, 84):
            continue
        y = round(71 + 21 * ((x - 77) / 6) ** 2) if 71 <= x <= 83 else round(92 - 2.2 * (71 - x if x < 71 else x - 83))
        y = max(71, min(y, 92))
        put(x, y, zz, 'iron_chain')
        if x % 2 == 0 and y > 71:
            fill(x, 71, zz, x, y - 1, zz, 'iron_chain')
# statue (bonus : cuivre oxydé et flamme dorée)
sx, sz = 78, -72
fill(sx - 3, 65, sz - 3, sx + 3, 70, sz + 3, 'stone_bricks')
fill(sx - 2, 71, sz - 2, sx + 2, 72, sz + 2, 'chiseled_stone_bricks')
fill(sx - 1, 73, sz - 1, sx + 1, 82, sz + 1, 'oxidized_copper')
fill(sx - 2, 73, sz - 1, sx + 2, 76, sz + 1, 'oxidized_cut_copper')
fill(sx, 83, sz, sx, 85, sz, 'oxidized_copper')
fill(sx - 1, 84, sz, sx + 1, 84, sz, 'oxidized_copper')
for (dx, dz) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    put(sx + dx, 86, sz + dz, 'oxidized_cut_copper')
fill(sx + 2, 80, sz, sx + 2, 88, sz, 'oxidized_copper')
fill(sx + 2, 89, sz, sx + 2, 90, sz, 'gold_block')
fill(sx - 2, 79, sz, sx - 2, 81, sz, 'oxidized_cut_copper')

# ---------------------------------------------------------------- comptage, tags
BONUS = {'gold_block', 'oxidized_copper', 'oxidized_cut_copper'}
CITY -= {'air'}
GSET.discard('barrier')
assert not (CITY & (GSET | {'barrier', 'water'})), CITY & GSET
cnt = {n: grid.count(bytes([PIDX[n]])) for n in CITY}
TOTAL = sum(cnt.values())
TB = sum(cnt[n] for n in BONUS if n in cnt)
os.makedirs(os.path.join(C.D, 'tags/block'), exist_ok=True)
for name, vals in [('bomb_city', sorted(CITY - BONUS)), ('bomb_bonus', sorted(BONUS)),
                   ('bomb_pass', ['air', 'cave_air', 'void_air', 'light'])]:
    with open(os.path.join(C.D, 'tags/block', name + '.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'values': ['minecraft:' + v for v in vals]}, f, indent=2)
        f.write('\n')

# ---------------------------------------------------------------- construction par étapes
NPART = 80
per = math.ceil(len(CMDS) / NPART)
parts = [CMDS[i:i + per] for i in range(0, len(CMDS), per)]
NPART = len(parts)
for i, p in enumerate(parts, 1):
    w(f'bomber/b/p{i}', [f'# Ville du Bombardier, étape {i}/{NPART} (généré par tools/arcade/gen_bomber.py)'] + p)
gper = math.ceil(len(GROUND) / 40)
gparts = [GROUND[i:i + gper] for i in range(0, len(GROUND), gper)]
for i, p in enumerate(gparts, 1):
    w(f'bomber/b/g{i}', [f'# Sol, fleuve et plancher du Bombardier, étape {i}/{len(gparts)}'] + p)
NG = len(gparts)
step = ['# Une étape de construction par tick ($bbs : 1..40 sol si absent, puis la ville). Planifiée par bomber/prepare.',
        'scoreboard players add $bbs mg.st 1']
step += [f'execute if score $bbs mg.st matches {i} run function mg:bomber/b/g{i}' for i in range(1, NG + 1)]
step += [f'execute if score $bbs mg.st matches {NG + i} run function mg:bomber/b/p{i}' for i in range(1, NPART + 1)]
step += [f'execute if score $bbs mg.st matches ..{NG + NPART - 1} run schedule function mg:bomber/build_step 1t']
w('bomber/build_step', step)

# ---------------------------------------------------------------- explosions : sphère de fills
def boom(r):
    L = [f'# Explosion de rayon {r} à la position courante : $bk blocs, $bb blocs bonus détruits',
         'scoreboard players set $bk mg.st 0', 'scoreboard players set $bb mg.st 0']
    for dy in range(-r, r + 1):
        h = int(math.sqrt(r * r - dy * dy) + 0.35)
        k = max(0, round(h * 0.5))
        boxes = [(h, k), (k, h)] if h != k else [(h, h)]
        for (a, b) in boxes:
            for tag, var in (('bomb_bonus', '$bb'), ('bomb_city', '$bk')):
                L.append(f'execute store result score $bt mg.st run fill ~-{a} ~{dy} ~-{b} ~{a} ~{dy} ~{b} minecraft:air replace #mg:{tag}')
                L.append(f'scoreboard players operation {var} mg.st += $bt mg.st')
    return L


for r in (2, 3, 6, 11):
    w(f'bomber/boom/r{r}', boom(r))

# ---------------------------------------------------------------- jeu
BOMBS = [  # type, item_model, nom, couleur, cooldown (ticks), vitesse de lancer (‰), description
    (1, 'tnt', 'Bombe', 'red', 12, 900, 'Rayon 3, recharge 0,6 s'),
    (2, 'tnt_minecart', 'Méga-bombe', 'dark_red', 140, 600, 'Rayon 6, recharge 7 s'),
    (3, 'fire_charge', 'Bombe à fragmentation', 'gold', 100, 900, '7 sous-munitions, recharge 5 s'),
]


def item(t, model, name, col, cd, desc, slot):
    cdc = f',use_cooldown={{seconds:{cd / 20}f,cooldown_group:"mg:bomb{t}"}}' if cd else ''
    comp = (f'custom_data={{bomb:{t}}},item_model="minecraft:{model}",unbreakable={{}},'
            f'custom_name={js({"text": name, "color": col, "bold": True, "italic": False})},'
            f'lore=[{js({"text": desc, "color": "gray", "italic": False})},{js({"text": "Clic droit : larguer (dans la direction du regard)", "color": "dark_gray", "italic": False})}]'
            + cdc)
    return f'item replace entity @s hotbar.{slot} with minecraft:warped_fungus_on_a_stick[{comp}]'


w('bomber/prepare', ['# 💣 Bombardier : préparation (construction en étapes pendant le compte à rebours)',
                     f'fill -{HX} {YT} {Z - HX} {HX} {YT} {Z + HX} minecraft:barrier',
                     'scoreboard players set $bbs mg.st 0',
                     f'execute if data storage mg:bomber v1 run scoreboard players set $bbs mg.st {NG}',
                     'function mg:bomber/build_step',
                     'kill @e[tag=mg.bomb]', 'kill @e[tag=mg.bsm]',
                     'scoreboard players set $bdes mg.st 0', 'scoreboard players set $bpct mg.st 0',
                     'scoreboard players set $bidn mg.st 0',
                     'scoreboard players reset * mg.bmb',
                     'execute as @a[tag=mg.play] run function mg:bomber/join',
                     'gamemode adventure @a[tag=mg.play]', 'clear @a[tag=mg.play]',
                     f'spreadplayers 0 {Z} 6 50 under {YT + 3} false @a[tag=mg.play]',
                     f'execute as @a[tag=mg.play] at @s run tp @s ~ {YT + 1} ~ ~ 60',
                     f'bossbar add mg:bomber {js({"text": "🏙 Ville détruite : 0 %", "color": "red"})}',
                     f'bossbar set mg:bomber max {TOTAL}', 'bossbar set mg:bomber value 0', 'bossbar set mg:bomber color red',
                     'bossbar set mg:bomber style notched_10', 'bossbar set mg:bomber players @a[tag=mg.play]'])
w('bomber/join', ['# @s : numéro de bombardier (attribution des dégâts)', 'scoreboard players add $bidn mg.st 1',
                  'scoreboard players operation @s mg.bid = $bidn mg.st', 'scoreboard players set @s mg.bmb 0',
                  'scoreboard players set @s mg.bc1 0', 'scoreboard players set @s mg.bc2 0', 'scoreboard players set @s mg.bc3 0',
                  'scoreboard players set @s mg.bc4 0'])
w('bomber/kit', ['# @s : les bombes'] + [item(t, m, n, c, cd, d, i) for i, (t, m, n, c, cd, _, d) in enumerate(BOMBS)] +
  ['effect give @s minecraft:speed infinite 1 true', 'effect give @s minecraft:saturation infinite 0 true',
   'effect give @s minecraft:resistance infinite 4 true', 'effect give @s minecraft:night_vision infinite 0 true'])
w('bomber/go', ['# Départ', 'scoreboard players set $btt mg.st 0',
                f'execute unless score $bbs mg.st matches {NG + NPART}.. run function mg:bomber/build_rest',
                'execute as @a[tag=mg.play] run function mg:bomber/kit',
                'scoreboard players reset @a mg.qs',
                'scoreboard objectives setdisplay sidebar mg.bmb',
                'tellraw @a[tag=mg.play] ' + js([{'text': '💣 BOMBARDIER : ', 'color': 'red', 'bold': True},
                                                 {'text': 'vise un immeuble et clic droit pour larguer. Chaque bloc détruit = 1 point, '
                                                          'or et statue = 10. Bombe atomique pour la dernière minute. 2 min 30.', 'color': 'gray'}])])
w('bomber/build_rest', ['# Filet de sécurité : termine la construction d\'un coup si le départ arrive avant la fin',
                        f'execute if score $bbs mg.st matches ..{NG + NPART - 1} run function mg:bomber/build_step',
                        f'execute if score $bbs mg.st matches ..{NG + NPART - 1} run function mg:bomber/build_rest'])

nuke = item(4, 'nether_star', '☢ Bombe atomique', 'green', 0, 'Rayon 11, une seule !', 3)
w('bomber/tick', ['# 💣 Bombardier : tick', 'scoreboard players add $btt mg.st 1',
                  'execute as @a[tag=mg.play,scores={mg.qs=1..}] at @s run function mg:bomber/use',
                  'scoreboard players reset @a[scores={mg.qs=1..}] mg.qs',
                  'scoreboard players remove @a[scores={mg.bc1=1..}] mg.bc1 1', 'scoreboard players remove @a[scores={mg.bc2=1..}] mg.bc2 1',
                  'scoreboard players remove @a[scores={mg.bc3=1..}] mg.bc3 1',
                  'execute as @e[type=minecraft:tnt,tag=mg.bomb] at @s run function mg:bomber/bomb_tick',
                  'scoreboard players add @e[type=minecraft:marker,tag=mg.bsm] mg.bc4 1',
                  'execute as @e[type=minecraft:marker,tag=mg.bsm,scores={mg.bc4=400..}] run kill @s',
                  'scoreboard players operation $bq mg.st = $btt mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $bq mg.st %= #20 mg.st',
                  'execute if score $bq mg.st matches 0 run function mg:bomber/second',
                  'execute if score $bq mg.st matches 0 run execute at @e[type=minecraft:marker,tag=mg.bsm] run particle minecraft:campfire_cosy_smoke ~ ~ ~ 0.8 0.3 0.8 0.02 3 force',
                  'execute if score $bq mg.st matches 10 run execute at @e[type=minecraft:marker,tag=mg.bsm] run particle minecraft:flame ~ ~0.5 ~ 0.8 0.3 0.8 0.01 4',
                  f'execute if score $btt mg.st matches {NUKE_AT} run function mg:bomber/nuke_give',
                  f'execute if score $btt mg.st matches {LIMIT - 600} run tellraw @a[tag=mg.play] {{"text":"💣 Plus que 30 secondes !","color":"gold"}}',
                  f'execute if score $state mg.st matches 2 if score $btt mg.st matches {LIMIT}.. run function mg:bomber/timeout',
                  'execute store result score $alive mg.st if entity @a[tag=mg.play]',
                  'execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw'])
w('bomber/second', ['# Une seconde : barre de destruction, joueurs retenus au-dessus de la ville',
                    'scoreboard players operation $bpct mg.st = $bdes mg.st', 'scoreboard players set #100 mg.st 100',
                    'scoreboard players operation $bpct mg.st *= #100 mg.st', f'scoreboard players set #btot mg.st {TOTAL}',
                    'scoreboard players operation $bpct mg.st /= #btot mg.st',
                    'execute store result bossbar mg:bomber value run scoreboard players get $bdes mg.st',
                    'bossbar set mg:bomber name [{"text":"🏙 Ville détruite : ","color":"red"},{"score":{"name":"$bpct","objective":"mg.st"},"color":"yellow","bold":true},{"text":" %","color":"red"}]',
                    f'execute as @a[tag=mg.play] at @s if entity @s[y=0,dy={YT - 1}] run tp @s 0 {YT + 1} {Z}',
                    'execute if score $state mg.st matches 2 if score $bpct mg.st matches 85.. run function mg:bomber/timeout'])
w('bomber/nuke_give', ['# Dernière minute : une bombe atomique par joueur',
                       'execute as @a[tag=mg.play] run ' + nuke,
                       'title @a[tag=mg.play] title {"text":"☢","color":"green","bold":true}',
                       'title @a[tag=mg.play] subtitle {"text":"Bombe atomique disponible (case 4) !","color":"green"}',
                       'execute as @a[tag=mg.play] at @s run playsound minecraft:block.beacon.activate master @s ~ ~ ~ 1 0.6'])

# lancer : direction du regard ×1000 dans $fx $fy $fz
w('bomber/use', ['# Clic droit (@s, à sa position) : la bombe en main',
                 'execute if items entity @s weapon.mainhand *[custom_data~{bomb:1}] if score @s mg.bc1 matches ..0 run return run function mg:bomber/drop {t:1,cd:"bc1",cdv:%d,sp:0.0009}' % BOMBS[0][4],
                 'execute if items entity @s weapon.mainhand *[custom_data~{bomb:2}] if score @s mg.bc2 matches ..0 run return run function mg:bomber/drop {t:2,cd:"bc2",cdv:%d,sp:0.0006}' % BOMBS[1][4],
                 'execute if items entity @s weapon.mainhand *[custom_data~{bomb:3}] if score @s mg.bc3 matches ..0 run return run function mg:bomber/drop {t:3,cd:"bc3",cdv:%d,sp:0.0009}' % BOMBS[2][4],
                 'execute if items entity @s weapon.mainhand *[custom_data~{bomb:4}] run return run function mg:bomber/drop_nuke',
                 'playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.4 1.6'])
w('bomber/drop_nuke', ['# Bombe atomique : une seule, l\'objet disparaît', 'item replace entity @s weapon.mainhand with minecraft:air',
                       'function mg:bomber/drop {t:5,cd:"bc4",cdv:0,sp:0.0004}',
                       'tellraw @a[tag=mg.play] [{"text":"☢ ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" a largué la bombe atomique !","color":"green"}]',
                       'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.6 1.4'])
w('bomber/drop', ['# @s : largue une bombe de type $(t) sous ses pieds, lancée dans la direction du regard',
                  '$scoreboard players set @s mg.$(cd) $(cdv)',
                  'execute anchored eyes positioned ^ ^ ^1 run summon minecraft:marker ~ ~ ~ {Tags:["mg.bdm"]}',
                  'execute store result score $fx mg.st run data get entity @e[type=minecraft:marker,tag=mg.bdm,limit=1] Pos[0] 1000',
                  'execute store result score $fy mg.st run data get entity @e[type=minecraft:marker,tag=mg.bdm,limit=1] Pos[1] 1000',
                  'execute store result score $fz mg.st run data get entity @e[type=minecraft:marker,tag=mg.bdm,limit=1] Pos[2] 1000',
                  'kill @e[type=minecraft:marker,tag=mg.bdm]',
                  'execute store result score $px0 mg.st run data get entity @s Pos[0] 1000',
                  'execute store result score $py0 mg.st run data get entity @s Pos[1] 1000',
                  'execute store result score $pz0 mg.st run data get entity @s Pos[2] 1000',
                  'scoreboard players operation $fx mg.st -= $px0 mg.st', 'scoreboard players operation $fy mg.st -= $py0 mg.st',
                  'scoreboard players remove $fy mg.st 1620', 'scoreboard players operation $fz mg.st -= $pz0 mg.st',
                  f'execute positioned ~ {YT - 1.3} ~ run summon minecraft:tnt ~ ~ ~ {{Tags:["mg.bomb","mg.bnew"],fuse:400s,explosion_power:0.0f}}',
                  '$execute store result entity @e[type=minecraft:tnt,tag=mg.bnew,limit=1] Motion[0] double $(sp) run scoreboard players get $fx mg.st',
                  '$execute store result entity @e[type=minecraft:tnt,tag=mg.bnew,limit=1] Motion[1] double $(sp) run scoreboard players get $fy mg.st',
                  '$execute store result entity @e[type=minecraft:tnt,tag=mg.bnew,limit=1] Motion[2] double $(sp) run scoreboard players get $fz mg.st',
                  'scoreboard players operation @e[type=minecraft:tnt,tag=mg.bnew] mg.bid = @s mg.bid',
                  '$scoreboard players set @e[type=minecraft:tnt,tag=mg.bnew] mg.bty $(t)',
                  'scoreboard players set @e[type=minecraft:tnt,tag=mg.bnew] mg.bc4 0',
                  '$function mg:bomber/look_$(t)',
                  'tag @e[tag=mg.bnew] remove mg.bnew',
                  'playsound minecraft:entity.tnt.primed player @a ~ ~ ~ 0.8 1.2'])
for t, blk in [(1, 'tnt'), (2, 'coal_block'), (3, 'redstone_block'), (4, 'tnt'), (5, 'lodestone')]:
    w(f'bomber/look_{t}', [f'# Aspect de la bombe de type {t}',
                           f'data merge entity @e[type=minecraft:tnt,tag=mg.bnew,limit=1] {{block_state:{{Name:"minecraft:{blk}"}}}}'])

w('bomber/bomb_tick', ['# @s : bombe en vol (âge mg.bc4, type mg.bty, lanceur mg.bid)',
                       'scoreboard players add @s mg.bc4 1',
                       'execute if score @s mg.bc4 matches 300.. run return run kill @s',
                       'execute if entity @s[y=-64,dy=103] run return run kill @s',
                       'execute if score @s mg.bty matches 3 if score @s mg.bc4 matches 14 run return run function mg:bomber/split',
                       'particle minecraft:smoke ~ ~0.5 ~ 0.1 0.1 0.1 0 2',
                       'execute if score @s mg.bty matches 5 run particle minecraft:end_rod ~ ~0.5 ~ 0.2 0.2 0.2 0 2 force',
                       'execute unless block ~ ~-0.2 ~ #mg:bomb_pass run return run function mg:bomber/impact',
                       'execute unless block ~0.6 ~0.4 ~ #mg:bomb_pass run return run function mg:bomber/impact',
                       'execute unless block ~-0.6 ~0.4 ~ #mg:bomb_pass run return run function mg:bomber/impact',
                       'execute unless block ~ ~0.4 ~0.6 #mg:bomb_pass run return run function mg:bomber/impact',
                       'execute unless block ~ ~0.4 ~-0.6 #mg:bomb_pass run return run function mg:bomber/impact'])
w('bomber/split', ['# @s : la bombe à fragmentation s\'ouvre en 7 sous-munitions',
                   'execute store result score $mx mg.st run data get entity @s Motion[0] 1000',
                   'execute store result score $my mg.st run data get entity @s Motion[1] 1000',
                   'execute store result score $mz mg.st run data get entity @s Motion[2] 1000',
                   'scoreboard players operation $bid mg.st = @s mg.bid'] +
  ['execute summon minecraft:tnt run function mg:bomber/bomblet'] * 7 +
  ['particle minecraft:firework ~ ~0.5 ~ 0.3 0.3 0.3 0.15 25 force', 'playsound minecraft:entity.firework_rocket.blast master @a ~ ~ ~ 3 0.8', 'kill @s'])
w('bomber/bomblet', ['# @s : sous-munition (même lanceur, direction écartée au hasard)',
                     'tag @s add mg.bomb', 'data merge entity @s {fuse:400s,explosion_power:0.0f}',
                     'scoreboard players operation @s mg.bid = $bid mg.st', 'scoreboard players set @s mg.bty 4', 'scoreboard players set @s mg.bc4 20',
                     'execute store result score $br mg.st run random value -280..280', 'scoreboard players operation $br mg.st += $mx mg.st',
                     'execute store result entity @s Motion[0] double 0.001 run scoreboard players get $br mg.st',
                     'execute store result score $br mg.st run random value -150..80', 'scoreboard players operation $br mg.st += $my mg.st',
                     'execute store result entity @s Motion[1] double 0.001 run scoreboard players get $br mg.st',
                     'execute store result score $br mg.st run random value -280..280', 'scoreboard players operation $br mg.st += $mz mg.st',
                     'execute store result entity @s Motion[2] double 0.001 run scoreboard players get $br mg.st'])
w('bomber/impact', ['# @s : la bombe touche (explosion selon le type, points au lanceur)',
                    'scoreboard players operation $bid mg.st = @s mg.bid',
                    'execute if score @s mg.bty matches 1 run function mg:bomber/boom/r3',
                    'execute if score @s mg.bty matches 2 run function mg:bomber/boom/r6',
                    'execute if score @s mg.bty matches 3 run function mg:bomber/boom/r3',
                    'execute if score @s mg.bty matches 4 run function mg:bomber/boom/r2',
                    'execute if score @s mg.bty matches 5 run function mg:bomber/boom/r11',
                    'execute if score @s mg.bty matches 1 run function mg:bomber/fx_small',
                    'execute if score @s mg.bty matches 3..4 run function mg:bomber/fx_small',
                    'execute if score @s mg.bty matches 2 run function mg:bomber/fx_big',
                    'execute if score @s mg.bty matches 5 run function mg:bomber/fx_nuke',
                    'execute if score $bk mg.st matches 1.. run summon minecraft:marker ~ ~ ~ {Tags:["mg.bsm"]}',
                    'scoreboard players operation $bpts mg.st = $bb mg.st', 'scoreboard players set #10 mg.st 10',
                    'scoreboard players operation $bpts mg.st *= #10 mg.st', 'scoreboard players operation $bpts mg.st += $bk mg.st',
                    'scoreboard players operation $bdes mg.st += $bk mg.st', 'scoreboard players operation $bdes mg.st += $bb mg.st',
                    'execute as @a[tag=mg.play] if score @s mg.bid = $bid mg.st run function mg:bomber/credit',
                    'kill @s'])
w('bomber/credit', ['# @s : lanceur de la bombe qui vient d\'exploser ($bpts points)',
                    'scoreboard players operation @s mg.bmb += $bpts mg.st',
                    'execute if score $bpts mg.st matches 1.. run title @s actionbar [{"text":"💥 +","color":"gold"},{"score":{"name":"$bpts","objective":"mg.st"},"color":"yellow","bold":true},{"text":" dégâts","color":"gold"}]',
                    'execute if score $bpts mg.st matches 0 run title @s actionbar {"text":"💨 Raté !","color":"gray"}',
                    'execute if score $bpts mg.st matches 400.. run tellraw @a[tag=mg.play] [{"text":"💥 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" : coup dévastateur, ","color":"red"},{"score":{"name":"$bpts","objective":"mg.st"},"color":"gold","bold":true},{"text":" points !","color":"red"}]',
                    'execute if score $bpts mg.st matches 1.. at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.6 0.8'])
w('bomber/fx_small', ['particle minecraft:explosion ~ ~ ~ 1.5 1.5 1.5 0 6 force', 'particle minecraft:large_smoke ~ ~ ~ 1.5 1 1.5 0.05 20 force',
                      'particle minecraft:flame ~ ~ ~ 1.2 1 1.2 0.08 25 force',
                      'playsound minecraft:entity.generic.explode master @a ~ ~ ~ 6 1'])
w('bomber/fx_big', ['particle minecraft:explosion_emitter ~ ~ ~ 1.5 1.5 1.5 0 3 force', 'particle minecraft:large_smoke ~ ~ ~ 3 2 3 0.08 60 force',
                    'particle minecraft:lava ~ ~ ~ 3 2 3 0 30 force', 'particle minecraft:flame ~ ~ ~ 3 2 3 0.15 60 force',
                    'playsound minecraft:entity.generic.explode master @a ~ ~ ~ 12 0.6',
                    'playsound minecraft:entity.lightning_bolt.thunder master @a ~ ~ ~ 6 1.4'])
w('bomber/fx_nuke', ['particle minecraft:explosion_emitter ~ ~ ~ 6 4 6 0 25 force', 'particle minecraft:campfire_signal_smoke ~ ~8 ~ 4 12 4 0.05 200 force',
                     'particle minecraft:large_smoke ~ ~4 ~ 8 6 8 0.2 300 force', 'particle minecraft:lava ~ ~ ~ 6 4 6 0 120 force',
                     'particle minecraft:flame ~ ~2 ~ 8 4 8 0.3 300 force',
                     'playsound minecraft:entity.generic.explode master @a ~ ~ ~ 40 0.4',
                     'playsound minecraft:entity.lightning_bolt.thunder master @a ~ ~ ~ 40 0.5',
                     'playsound minecraft:entity.wither.death master @a ~ ~ ~ 20 0.6'])
w('bomber/timeout', ['# Fin : le plus de dégâts gagne (égalité = match nul)',
                     'scoreboard players set $bx mg.st 0', 'scoreboard players operation $bx mg.st > @a[tag=mg.play] mg.bmb',
                     'scoreboard players set $bc mg.st 0', 'execute as @a[tag=mg.play] if score @s mg.bmb = $bx mg.st run scoreboard players add $bc mg.st 1',
                     'tellraw @a[tag=mg.play] [{"text":"🏙 La ville est détruite à ","color":"gray"},{"score":{"name":"$bpct","objective":"mg.st"},"color":"red","bold":true},{"text":" %","color":"gray"}]',
                     'execute if score $bx mg.st matches 0 run return run function mg:core/draw',
                     'execute if score $bc mg.st matches 2.. run return run function mg:core/draw',
                     'execute as @a[tag=mg.play] if score @s mg.bmb = $bx mg.st run function mg:core/win_player'])
w('bomber/cleanup', ['schedule clear mg:bomber/build_step', 'kill @e[tag=mg.bomb]', 'kill @e[tag=mg.bsm]', 'bossbar remove mg:bomber',
                     'scoreboard players reset * mg.bmb', 'scoreboard players reset * mg.bid', 'effect clear @a[tag=mg.play]'])

C.register([GID], 'bomber', [C.announce(GID, '', '💣 BOMBARDIER', 'red', 'largue des bombes sur la ville, le plus de dégâts gagne !')])
C.objectives([('mg.bmb', 'dummy {"text":"💣 Dégâts","color":"red","bold":true}'), ('mg.bid', 'dummy'), ('mg.bty', 'dummy'),
              ('mg.bc1', 'dummy'), ('mg.bc2', 'dummy'), ('mg.bc3', 'dummy'), ('mg.bc4', 'dummy')])
C.forceload([f'# Bombardier (z {Z})', f'forceload add -{HX} {Z - HX} {HX} {Z + HX}'])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['bossbar remove mg:bomber', 'schedule clear mg:bomber/build_step',
                                                              'data remove storage mg:bomber v1'])
print(f'Bombardier OK : {len(CMDS)} commandes en {NPART} étapes, sol {len(GROUND)} en {NG}, {TOTAL} blocs destructibles ({TB} bonus), '
      f'{len(CITY)} matériaux')
