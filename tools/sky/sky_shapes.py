"""Élytra : formes du décor (îles, falaises, tours, arches, nuages, anneaux, pics, piliers, colonnes de vent).
Chaque forme remplit un Vox ; le générateur aléatoire (rng) est passé en paramètre par sky_layout.build.
"""
import math

from sky_track import ARENA, AXES, RING_COLS, RINGS


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
