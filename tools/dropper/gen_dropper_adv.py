"""The Dropper : Aventure (id 64) — 10 niveaux à thème enchaînés : python gen_dropper_adv.py <racine du dépôt>

Inspiré des maps de dropper classiques (puits à thème, une idée par niveau), constructions originales.
Chaque niveau est un puits de 23 x 23 (intérieur) sur 260 blocs, en trois « actes » (trois idées d'obstacles du même thème,
séparés par une bande lumineuse) : on part du rebord en haut (y 301), on saute dans l'ouverture et on doit finir dans l'eau
du fond. Toucher quoi que ce soit d'autre = retour en haut du niveau ; réussir = niveau suivant.
Chaque niveau est vérifié par une chute simulée (voir plus bas) : s'il n'y a pas de passage, un trou est percé.
Le premier à finir les 10 niveaux gagne ; sinon, au bout de 10 minutes, le plus avancé (puis le moins d'échecs).
Sortie : data/mg/function/dropadv/*.mcfunction
"""
import math, os, random, sys

R = sys.argv[1]
OUT = os.path.join(R, 'data', 'mg', 'function', 'dropadv')
os.makedirs(OUT, exist_ok=True)
for f in os.listdir(OUT):
    os.remove(os.path.join(OUT, f))
CZ = 24000
TOP, FLOOR = 300, 40          # rebord de départ, sol du fond (l'eau est juste au-dessus)
IN, WALL = 11, 14             # demi-intérieur, demi-extérieur (murs de 3)
SPACING = 40
A1, A2 = 222, 142             # limites des trois actes (haut : TOP..A1, milieu : A1..A2, bas : A2..FLOOR)
RAIN = ['red', 'orange', 'yellow', 'lime', 'light_blue', 'blue', 'purple', 'magenta']

def wr(name, lines):
    with open(os.path.join(OUT, name + '.mcfunction'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')

class Lv:
    def __init__(self, k, name, colr, wall, desc):
        self.k, self.name, self.colr, self.wall, self.desc = k, name, colr, wall, desc
        self.cx = k * SPACING
        self.cmd = []
        self.rnd = random.Random(640 + k)
    def fill(self, x1, y1, z1, x2, y2, z2, blk, mode=''):
        self.cmd.append(f'fill {self.cx + min(x1, x2)} {min(y1, y2)} {CZ + min(z1, z2)} {self.cx + max(x1, x2)} {max(y1, y2)} {CZ + max(z1, z2)} minecraft:{blk}{(" " + mode) if mode else ""}')
    def set(self, x, y, z, blk):
        self.cmd.append(f'setblock {self.cx + x} {y} {CZ + z} minecraft:{blk}')
    def disc(self, y, r, blk, ox=0, oz=0, mode=''):
        for a in range(-r, r + 1):
            w = int(math.sqrt(max(0, r * r + r - a * a)))
            self.fill(ox + a, y, oz - w, ox + a, y, oz + w, blk, mode)
    def ball(self, x, y, z, r, blk):
        for dy in range(-r, r + 1):
            rr = int(math.sqrt(max(0, r * r - dy * dy) + 0.5))
            self.disc(y + dy, rr, blk, x, z)
    def layer(self, y, fn, lo=-IN, hi=IN):
        """une couche : fn(x, z) -> bloc ou None, regroupé en bandes le long de z."""
        for x in range(lo, hi + 1):
            run = None
            for z in list(range(lo, hi + 1)) + [None]:
                b = fn(x, z) if z is not None else None
                if run and (b != run[2] or z is None):
                    self.fill(x, y, run[0], x, y, run[1], run[2]); run = None
                if b and z is not None:
                    run = [run[0], z, b] if run and run[2] == b else [z, z, b]
    def band(self, y1, y2, blk):
        """bande décorative sur la face intérieure des murs."""
        e = IN + 1
        self.fill(-e, y1, -e, e, y2, -e, blk); self.fill(-e, y1, e, e, y2, e, blk)
        self.fill(-e, y1, -e, -e, y2, e, blk); self.fill(e, y1, -e, e, y2, e, blk)
    def wall_spots(self, y1, y2, n, mats):
        for _ in range(n):
            x, z = self.rnd.randint(-IN - 1, IN + 1), self.rnd.randint(-IN - 1, IN + 1)
            if abs(x) == IN + 1 or abs(z) == IN + 1:
                self.set(x, self.rnd.randint(y2, y1), z, self.rnd.choice(mats))
    def shell(self, round_=False, mats=None, acts=('sea_lantern', 'sea_lantern')):
        """murs, intérieur vidé, rebord de départ, bandes des actes, éclairage invisible."""
        for y in range(FLOOR - 8, TOP + 8, 23):                           # nettoyage (anciennes versions du puits comprises)
            self.fill(-WALL - 4, y, -WALL - 4, WALL + 4, min(y + 22, TOP + 7), WALL + 4, 'air')
        for y in range(FLOOR - 3, TOP, 35):
            self.fill(-WALL, y, -WALL, WALL, min(y + 34, TOP - 1), WALL, self.wall)
        if round_:
            for y in range(FLOOR + 1, TOP + 1, 16):
                self.disc_range(y, min(y + 15, TOP), IN)
        else:
            for y in range(FLOOR + 1, TOP + 1, 55):
                self.fill(-IN, y, -IN, IN, min(y + 54, TOP), IN, 'air')
        if mats: self.wall_spots(TOP, FLOOR, 900, mats)
        for yb, blk in ((A1, acts[0]), (A2, acts[1])):
            self.band(yb, yb, blk)
        # rebord : plancher à y TOP autour d'une ouverture 17 x 17, garde-corps
        self.fill(-WALL - 4, TOP + 1, -WALL - 4, WALL + 4, TOP + 6, WALL + 4, 'air')
        self.fill(-WALL - 4, TOP, -WALL - 4, WALL + 4, TOP, WALL + 4, 'polished_andesite')
        self.fill(-8, TOP, -8, 8, TOP, 8, 'air')
        for (a, b, c, d) in ((-9, -9, 9, -9), (-9, 9, 9, 9), (-9, -9, -9, 9), (9, -9, 9, 9)):
            self.fill(a, TOP, b, c, TOP, d, 'yellow_concrete')
        self.fill(-WALL - 4, TOP + 1, -WALL - 4, WALL + 4, TOP + 4, -WALL - 4, 'glass')
        self.fill(-WALL - 4, TOP + 1, WALL + 4, WALL + 4, TOP + 4, WALL + 4, 'glass')
        self.fill(-WALL - 4, TOP + 1, -WALL - 4, -WALL - 4, TOP + 4, WALL + 4, 'glass')
        self.fill(WALL + 4, TOP + 1, -WALL - 4, WALL + 4, TOP + 4, WALL + 4, 'glass')
        self.fill(-WALL - 4, TOP + 6, -WALL - 4, WALL + 4, TOP + 6, WALL + 4, 'barrier')
        for y in range(FLOOR + 4, TOP, 9):
            for (x, z) in ((-7, -7), (7, -7), (-7, 7), (7, 7), (0, 0)):
                self.set(x, y, z, 'light[level=15]')
    def disc_range(self, y1, y2, r):
        for a in range(-r, r + 1):
            w = int(math.sqrt(max(0, r * r + r - a * a)))
            self.fill(a, y1, -w, a, y2, w, 'air')
    def make_path(self, lim=8):
        """« vrai chemin » : position (x, z) à chaque hauteur, qui ne dérive pas plus vite qu'un joueur ne peut se déplacer en tombant."""
        self.path = {}
        px, pz, tx, tz = 0.0, 0.0, 0.0, 0.0
        v, feet = 0.0, TOP + 1.0
        for y in range(TOP, FLOOR - 1, -1):
            while feet > y:
                v = (v + 0.08) * 0.98; feet -= v
            step = min(0.5, 0.55 * 0.15 / max(v, 0.08))
            if (TOP - y) % 25 == 0: tx, tz = self.rnd.uniform(-lim, lim), self.rnd.uniform(-lim, lim)
            dx, dz = tx - px, tz - pz; d = math.hypot(dx, dz)
            if d > 1e-6:
                k = min(step, d) / d; px += dx * k; pz += dz * k
            self.path[y] = (round(px), round(pz))
        return self.path
    def keep_path(self, y1, y2):
        """garantit le passage (3 x 3) le long du vrai chemin entre y1 (haut) et y2 (bas)."""
        for y in range(y2, y1 + 1):
            x, z = self.path[y]
            self.fill(x - 1, y, z - 1, x + 1, y, z + 1, 'air')

def spread(y1, y2, step, jitter=0, rnd=None):
    """hauteurs d'obstacles de y1 (haut) à y2 (bas)."""
    ys, y = [], y1
    while y > y2:
        ys.append(y); y -= step + (rnd.randint(0, jitter) if rnd and jitter else 0)
    return ys

LV = []
# ------------------------------------------------------------------ 1. Arc-en-ciel
L = Lv(0, 'Arc-en-ciel', 'light_purple', 'white_concrete', 'Entonnoirs, rayons et nuages pastel : suis les couleurs !')
L.shell(acts=('magenta_stained_glass', 'light_blue_stained_glass'))
for i in range(0, 8): L.band(TOP - 1 - i * 8, TOP - 1 - i * 8, f'{RAIN[i % 8]}_concrete')
for n, y in enumerate(spread(TOP - 8, A1 + 2, 6)):                      # acte 1 : entonnoirs
    r_open = [8, 7, 6, 5, 4, 5, 6, 7][n % 8]
    ox, oz = (L.rnd.randint(-2, 2), L.rnd.randint(-2, 2)) if r_open < 7 else (0, 0)
    L.layer(y, lambda x, z: None if max(abs(x - ox), abs(z - oz)) <= r_open else f'{RAIN[n % 8]}_concrete')
for n, y in enumerate(spread(A1 - 6, A2 + 2, 8)):                       # acte 2 : rayons qui tournent
    a0 = n * 17
    def spoke(x, z, a0=a0, n=n):
        r = math.hypot(x, z)
        if r < 2.5: return None
        a = (math.degrees(math.atan2(z, x)) - a0) % 45
        return f'{RAIN[(n + int(((math.degrees(math.atan2(z, x)) - a0) % 360) // 45)) % 8]}_terracotta' if a < 9 else None
    L.layer(y, spoke)
for y in spread(A2 - 6, FLOOR + 10, 7):                                  # acte 3 : nuages pastel
    for _ in range(2):
        L.ball(L.rnd.randint(-7, 7), y, L.rnd.randint(-7, 7), L.rnd.randint(2, 3), L.rnd.choice(['white_wool', 'pink_wool', 'light_blue_wool', 'yellow_wool']))
L.make_path(4); L.keep_path(TOP - 2, A1)
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'white_concrete')
for i, c in enumerate(RAIN[:5]): L.disc(FLOOR, 7 - i, f'{c}_concrete')
L.disc(FLOOR, 2, 'water')
LV.append(L)

# ------------------------------------------------------------------ 2. Spirale
L = Lv(1, 'Spirale', 'yellow', 'black_concrete', 'Boules qui tournent, barres pivotantes, spirale qui se resserre.')
L.shell(round_=True, acts=('glowstone', 'shroomlight'))
a = 0.0
for y in spread(TOP - 10, A1 + 3, 5):                                    # acte 1 : deux boules en spirale
    for ph in (0, math.pi):
        L.ball(round(6 * math.cos(a + ph)), y, round(6 * math.sin(a + ph)), 2, 'glowstone' if ph == 0 else 'sea_lantern')
    a += math.radians(38)
for n, y in enumerate(spread(A1 - 6, A2 + 2, 7)):                        # acte 2 : barre pivotante avec un trou décalé
    ang = math.radians(n * 30); ux, uz = math.cos(ang), math.sin(ang); gap = [-6, 0, 6][n % 3]
    def bar(x, z, ux=ux, uz=uz, gap=gap):
        along, side = x * ux + z * uz, -x * uz + z * ux
        return 'yellow_concrete' if abs(side) <= 1.2 and abs(along - gap) > 2 else None
    L.layer(y, bar); L.layer(y + 1, lambda x, z, b=bar: 'black_concrete' if b(x, z) else None)
a = 0.0
for n, y in enumerate(spread(A2 - 6, FLOOR + 10, 6)):                    # acte 3 : trois boules, spirale qui se resserre
    rad = 8 - 5 * n / 14
    for k in range(3):
        L.ball(round(rad * math.cos(a + k * 2.094)), y, round(rad * math.sin(a + k * 2.094)), 2, ['glowstone', 'sea_lantern', 'shroomlight'][k])
    a += math.radians(33)
L.disc(FLOOR, IN, 'black_concrete'); L.disc(FLOOR, 5, 'yellow_concrete'); L.disc(FLOOR, 3, 'water')
LV.append(L)

# ------------------------------------------------------------------ 3. La mine
L = Lv(2, 'La mine', 'gray', 'stone', 'Poutres et toiles, galeries et filons, puis le lac souterrain.')
L.shell(mats=['coal_ore', 'iron_ore', 'andesite', 'gravel', 'cobblestone', 'copper_ore', 'gold_ore', 'tuff'], acts=('lantern', 'redstone_ore'))
for y in range(FLOOR + 1, TOP, 3):                                       # parois irrégulières
    for _ in range(8):
        x, z = L.rnd.randint(-IN, IN), L.rnd.choice([-IN, IN])
        if L.rnd.random() < 0.5: x, z = z, x
        L.ball(x, y, z, L.rnd.randint(1, 2), L.rnd.choice(['stone', 'cobblestone', 'andesite', 'tuff']))
L.fill(-8, TOP - 3, -8, 8, TOP - 1, 8, 'air')
for y in spread(TOP - 12, A1 + 3, 8):                                    # acte 1 : poutres, rails, toiles
    o = L.rnd.randint(-6, 6)
    if L.rnd.random() < 0.5:
        L.fill(-IN, y, o, IN, y, o + 1, 'oak_log[axis=x]'); L.fill(-IN, y + 1, o, IN, y + 1, o, 'rail[shape=east_west]')
        L.fill(o, y - 3, -IN, o, y - 1, -IN, 'oak_fence')
    else:
        L.fill(o, y, -IN, o + 1, y, IN, 'oak_log[axis=z]'); L.fill(o, y + 1, -IN, o, y + 1, IN, 'rail')
    L.set(L.rnd.randint(-8, 8), y - 1, L.rnd.randint(-8, 8), 'cobweb')
    L.set(o, y - 1, o, 'lantern[hanging=true]')
for y in spread(A1 - 6, A2 + 2, 7):                                      # acte 2 : filons qui sortent des murs
    for _ in range(2):
        side = L.rnd.randint(0, 3); o = L.rnd.randint(-7, 7)
        x, z = [(-IN + 2, o), (IN - 2, o), (o, -IN + 2), (o, IN - 2)][side]
        L.ball(x, y, z, L.rnd.randint(3, 4), L.rnd.choice(['deepslate_iron_ore', 'deepslate_gold_ore', 'deepslate_diamond_ore', 'deepslate_redstone_ore', 'amethyst_block']))
    if L.rnd.random() < 0.5: L.set(L.rnd.randint(-6, 6), y - 3, L.rnd.randint(-6, 6), 'cobweb')
for n, y in enumerate(spread(A2 - 6, FLOOR + 12, 9)):                    # acte 3 : corniches et stalactites
    side = n % 4; d = L.rnd.randint(6, 10)
    box = [(-IN, -IN, -IN + d, IN), (IN - d, -IN, IN, IN), (-IN, -IN, IN, -IN + d), (-IN, IN - d, IN, IN)][side]
    L.fill(box[0], y, box[1], box[2], y, box[3], 'dripstone_block')
    for _ in range(6):
        x, z = L.rnd.randint(box[0], box[2]), L.rnd.randint(box[1], box[3])
        L.set(x, y - 1, z, 'pointed_dripstone[vertical_direction=down,thickness=tip]')
    L.set(L.rnd.randint(box[0], box[2]), y + 1, L.rnd.randint(box[1], box[3]), 'glow_lichen[down=true]')
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'gravel')
L.disc(FLOOR, 4, 'water')
LV.append(L)

# ------------------------------------------------------------------ 4. Rideaux
L = Lv(3, 'Rideaux', 'white', 'quartz_block', 'Rideaux percés, grilles croisées, puis le damier final.')
L.shell(acts=('pink_wool', 'light_blue_wool'))
cols = ['white', 'pink', 'light_blue', 'lime', 'yellow', 'orange']
prev = (0, 0)
for n, y in enumerate(spread(TOP - 9, A1 + 2, 8)):                       # acte 1 : rideaux percés (un trou près du précédent)
    holes = [(prev[0] + L.rnd.randint(-2, 2), prev[1] + L.rnd.randint(-2, 2))] + [(L.rnd.randint(-IN + 1, IN - 1), L.rnd.randint(-IN + 1, IN - 1)) for _ in range(2)]
    holes = [(max(-IN + 1, min(IN - 1, x)), max(-IN + 1, min(IN - 1, z))) for x, z in holes]
    prev = holes[0]
    L.layer(y, lambda x, z, h=holes, c=cols[n % 6]: None if any(abs(x - a) <= 1 and abs(z - b) <= 1 for a, b in h) else f'{c}_wool')
for n, y in enumerate(spread(A1 - 6, A2 + 2, 6)):                        # acte 2 : grilles croisées
    off = L.rnd.randint(0, 3)
    if n % 2: L.layer(y, lambda x, z, o=off: f'{cols[n % 6]}_wool' if (x + o) % 4 < 2 else None)
    else: L.layer(y, lambda x, z, o=off: f'{cols[n % 6]}_wool' if (z + o) % 4 < 2 else None)
prev = (0, 0)
for n, y in enumerate(spread(A2 - 6, FLOOR + 10, 10)):                   # acte 3 : damier, une case ouverte près de la précédente
    h = (max(-8, min(8, prev[0] + L.rnd.randint(-2, 2))), max(-8, min(8, prev[1] + L.rnd.randint(-2, 2)))); prev = h
    L.layer(y, lambda x, z, h=h: None if abs(x - h[0]) <= 1 and abs(z - h[1]) <= 1 else ('white_wool' if (x // 2 + z // 2) % 2 else 'black_wool'))
L.make_path(); L.keep_path(TOP - 2, FLOOR + 2)
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'quartz_block')
L.fill(L.path[FLOOR][0] - 1, FLOOR, L.path[FLOOR][1] - 1, L.path[FLOOR][0] + 1, FLOOR, L.path[FLOOR][1] + 1, 'water')
LV.append(L)

# ------------------------------------------------------------------ 5. Trous piégés
L = Lv(4, 'Trous piégés', 'dark_purple', 'obsidian', 'Des planchers troués... mais certains trous sont fermés par du verre !')
L.shell(acts=('crying_obsidian', 'crying_obsidian'))
L.wall_spots(TOP, FLOOR, 300, ['crying_obsidian', 'purple_stained_glass'])
H9 = [(-8, -8), (-1, -8), (6, -8), (-8, -1), (-1, -1), (6, -1), (-8, 6), (-1, 6), (6, 6)]
for y in spread(TOP - 10, A1 + 2, 10):                                   # acte 1 : 9 trous, 3 à 6 fermés
    L.fill(-IN, y, -IN, IN, y, IN, 'obsidian')
    closed = set(L.rnd.sample(range(9), L.rnd.randint(3, 6)))
    for h, (x, z) in enumerate(H9):
        L.fill(x, y, z, x + 2, y, z + 2, 'glass' if h in closed else 'air')
    L.set(-IN, y + 2, 0, 'soul_lantern'); L.set(IN, y + 2, 0, 'soul_lantern')
H4 = [(-8, -8), (4, -8), (-8, 4), (4, 4)]
for y in spread(A1 - 8, A2 + 2, 11):                                     # acte 2 : 4 grands trous, 2 fermés
    L.fill(-IN, y, -IN, IN, y, IN, 'purpur_block')
    closed = set(L.rnd.sample(range(4), 2))
    for h, (x, z) in enumerate(H4):
        L.fill(x, y, z, x + 4, y, z + 4, 'purple_stained_glass' if h in closed else 'air')
H2 = [(-6, -1), (4, -1), (-1, -6), (-1, 4)]
for y in spread(A2 - 8, FLOOR + 14, 13):                                 # acte 3 : un seul vrai passage sur quatre
    L.fill(-IN, y, -IN, IN, y, IN, 'crying_obsidian')
    ok = L.rnd.randrange(4)
    for h, (x, z) in enumerate(H2):
        L.fill(x, y, z, x + 2, y, z + 2, 'air' if h == ok else 'tinted_glass')
L.make_path(6); L.keep_path(TOP - 2, FLOOR + 2)
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'obsidian')
L.fill(L.path[FLOOR][0] - 1, FLOOR, L.path[FLOOR][1] - 1, L.path[FLOOR][0] + 1, FLOOR, L.path[FLOOR][1] + 1, 'water')
LV.append(L)

# ------------------------------------------------------------------ 6. L'Enfer
L = Lv(5, 'L\'Enfer', 'red', 'netherrack', 'Basalte et champignons, ponts de forteresse, puis le cœur du volcan.')
L.shell(mats=['magma_block', 'nether_quartz_ore', 'nether_gold_ore', 'blackstone', 'crimson_nylium', 'glowstone'], acts=('magma_block', 'shroomlight'))
for y in spread(TOP - 10, A1 + 3, 7):                                    # acte 1 : piliers de basalte et champignons
    if L.rnd.random() < 0.45:
        side = L.rnd.randint(0, 3); o = L.rnd.randint(-8, 8); ln = L.rnd.randint(8, 14)
        a1, a2 = -IN, -IN + ln
        if side == 0: L.fill(a1, y, o, a2, y + 1, o + 1, 'basalt[axis=x]')
        elif side == 1: L.fill(-a2, y, o, -a1, y + 1, o + 1, 'basalt[axis=x]')
        elif side == 2: L.fill(o, y, a1, o + 1, y + 1, a2, 'basalt[axis=z]')
        else: L.fill(o, y, -a2, o + 1, y + 1, -a1, 'basalt[axis=z]')
    else:
        x, z = L.rnd.randint(-6, 6), L.rnd.randint(-6, 6)
        cap = L.rnd.choice(['nether_wart_block', 'warped_wart_block'])
        L.disc(y, 3, cap, x, z); L.disc(y + 1, 2, cap, x, z)
        L.fill(x, y + 2, z, x, y + 6, z, 'crimson_stem' if cap == 'nether_wart_block' else 'warped_stem')
        L.set(x + 1, y - 1, z, 'shroomlight')
for n, y in enumerate(spread(A1 - 6, A2 + 2, 9)):                        # acte 2 : ponts de la forteresse
    o = L.rnd.randint(-7, 5)
    if n % 2:
        L.fill(-IN, y, o, IN, y, o + 2, 'nether_bricks'); L.fill(-IN, y + 1, o, IN, y + 1, o, 'nether_brick_fence'); L.fill(-IN, y + 1, o + 2, IN, y + 1, o + 2, 'nether_brick_fence')
    else:
        L.fill(o, y, -IN, o + 2, y, IN, 'nether_bricks'); L.fill(o, y + 1, -IN, o, y + 1, IN, 'nether_brick_fence'); L.fill(o + 2, y + 1, -IN, o + 2, y + 1, IN, 'nether_brick_fence')
    L.set(o + 1, y - 1, o + 1, 'soul_lantern[hanging=true]')
for y in spread(A2 - 6, FLOOR + 10, 8):                                  # acte 3 : rochers de magma et de basalte flottants
    for _ in range(2):
        L.ball(L.rnd.randint(-7, 7), y, L.rnd.randint(-7, 7), L.rnd.randint(1, 3), L.rnd.choice(['magma_block', 'blackstone', 'basalt', 'gilded_blackstone']))
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'blackstone')
L.disc(FLOOR, 5, 'magma_block')
L.disc(FLOOR, 3, 'water')
LV.append(L)

# ------------------------------------------------------------------ 7. Le salon géant
L = Lv(6, 'Le salon géant', 'gold', 'yellow_terracotta', 'Tu es minuscule dans un salon : lustre, étagères, table... vise le bocal !')
L.shell(acts=('white_terracotta', 'white_terracotta'))
for y in range(FLOOR + 1, TOP, 4):                                       # papier peint rayé
    for a in range(-IN - 1, IN + 2, 3):
        for (x, z) in ((a, -IN - 1), (a, IN + 1), (-IN - 1, a), (IN + 1, a)):
            L.set(x, y, z, 'white_terracotta')
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'spruce_planks')
L.fill(-7, FLOOR + 1, -7, 7, FLOOR + 1, 7, 'red_carpet')
# acte 1 : lustre géant, pendule au mur, étagère
L.disc(TOP - 10, 4, 'gold_block'); L.disc(TOP - 9, 2, 'gold_block'); L.fill(0, TOP - 8, 0, 0, TOP - 1, 0, 'iron_chain')
for (x, z) in ((-4, 0), (4, 0), (0, -4), (0, 4)): L.fill(x, TOP - 13, z, x, TOP - 11, z, 'end_rod')
L.disc(TOP - 30, 5, 'oak_planks'); L.fill(-1, TOP - 30, -1, 1, TOP - 30, 1, 'air')                    # plateau de l'abat-jour du plafonnier
for y in (TOP - 45, TOP - 58):                                           # étagères murales avec livres géants
    L.fill(-IN, y, -IN, IN, y + 1, -4, 'dark_oak_planks')
    for x in range(-10, 10, 3): L.fill(x, y + 2, -IN, x + 1, y + 7, -6, L.rnd.choice(['red_wool', 'blue_wool', 'green_wool', 'brown_wool']))
L.fill(IN, A1 + 4, -3, IN, A1 + 14, 3, 'white_concrete'); L.fill(IN - 1, A1 + 9, 0, IN - 1, A1 + 13, 0, 'black_concrete')    # pendule
# acte 2 : tableau, lampe sur pied, rideau
L.fill(-IN, A1 - 20, -5, -IN, A1 - 8, 5, 'orange_terracotta'); L.fill(-IN, A1 - 18, -3, -IN, A1 - 10, 3, 'light_blue_terracotta')
L.disc(A1 - 30, 6, 'white_wool', -3, 4); L.disc(A1 - 31, 7, 'white_wool', -3, 4); L.disc(A1 - 31, 5, 'air', -3, 4)
L.fill(-3, A2 - 40, 4, -3, A1 - 32, 4, 'gray_concrete')
for y in spread(A1 - 42, A2 + 4, 6): L.fill(IN - 3, y, -IN, IN, y, IN, 'red_wool') if L.rnd.random() < 0.5 else L.fill(-IN, y, IN - 3, IN, y, IN, 'red_wool')
# acte 3 : table (plateau percé), chaise, bocal
L.fill(-IN, A2 - 30, -2, IN, A2 - 29, IN, 'oak_planks'); L.fill(-2, A2 - 30, 2, 2, A2 - 29, 6, 'air')
for (x, z) in ((-9, -1), (9, -1), (-9, 9), (9, 9)): L.fill(x, FLOOR + 1, z, x, A2 - 31, z, 'oak_log')
L.set(4, A2 - 28, 7, 'flower_pot')
for n, y in enumerate(spread(A2 - 40, FLOOR + 40, 9)):                  # étagères murales et cadres entre la table et la chaise
    side = n % 4; d = L.rnd.randint(5, 9)
    box = [(-IN, -IN, -IN + d, IN), (IN - d, -IN, IN, IN), (-IN, -IN, IN, -IN + d), (-IN, IN - d, IN, IN)][side]
    L.fill(box[0], y, box[1], box[2], y, box[3], 'dark_oak_planks')
    for _ in range(3):
        x, z = L.rnd.randint(box[0], box[2]), L.rnd.randint(box[1], box[3])
        L.fill(x, y + 1, z, x, y + L.rnd.randint(2, 4), z, L.rnd.choice(['red_wool', 'blue_wool', 'green_wool', 'yellow_wool']))
for y in spread(TOP - 36, A1 + 18, 7):                                   # haut : guirlande et cadres
    L.ball(L.rnd.randint(-7, 7), y, L.rnd.randint(-7, 7), 1, L.rnd.choice(['yellow_stained_glass', 'orange_stained_glass', 'red_stained_glass']))
L.fill(4, FLOOR + 22, -9, IN, FLOOR + 23, -3, 'birch_planks'); L.fill(IN, FLOOR + 24, -9, IN, FLOOR + 36, -3, 'birch_planks')
L.fill(-3, FLOOR + 1, -3, 3, FLOOR + 4, 3, 'glass')
L.fill(-2, FLOOR + 1, -2, 2, FLOOR + 3, 2, 'water')
L.fill(-1, FLOOR + 4, -1, 1, FLOOR + 4, 1, 'water')
LV.append(L)

# ------------------------------------------------------------------ 8. La bibliothèque
L = Lv(7, 'La bibliothèque', 'dark_red', 'bookshelf', 'Étagères géantes, livres volants, lustres... vise l\'encrier.')
L.shell(acts=('chiseled_bookshelf', 'chiseled_bookshelf'))
for y in spread(TOP - 10, A1 + 3, 9):                                    # acte 1 : étagères qui avancent, livres volants
    side = L.rnd.randint(0, 3); depth = L.rnd.randint(6, 12)
    if side == 0: L.fill(-IN, y, -IN, IN, y + 2, -IN + depth, 'bookshelf')
    elif side == 1: L.fill(-IN, y, IN - depth, IN, y + 2, IN, 'bookshelf')
    elif side == 2: L.fill(-IN, y, -IN, -IN + depth, y + 2, IN, 'bookshelf')
    else: L.fill(IN - depth, y, -IN, IN, y + 2, IN, 'bookshelf')
    x, z = L.rnd.randint(-7, 5), L.rnd.randint(-7, 5)
    L.fill(x, y - 4, z, x + 2, y - 4, z + 4, 'white_wool'); L.fill(x - 1, y - 5, z, x + 3, y - 5, z + 4, L.rnd.choice(['red_wool', 'brown_wool', 'blue_wool']))
for y in spread(A1 - 6, A2 + 3, 10):                                     # acte 2 : piles de livres et lustres
    for _ in range(2):
        x, z = L.rnd.randint(-8, 6), L.rnd.randint(-8, 6); h = L.rnd.randint(2, 4)
        for k in range(h): L.fill(x + (k % 2), y - k, z, x + 2 + (k % 2), y - k, z + 3, L.rnd.choice(['red_wool', 'green_wool', 'blue_wool', 'brown_wool', 'black_wool']))
    cx_, cz_ = L.rnd.randint(-5, 5), L.rnd.randint(-5, 5)
    L.disc(y + 3, 2, 'gold_block', cx_, cz_); L.set(cx_, y + 2, cz_, 'lantern[hanging=true]')
for y in spread(A2 - 6, FLOOR + 14, 9):                                  # acte 3 : rayonnages en croix
    o = L.rnd.randint(-6, 4)
    if L.rnd.random() < 0.5: L.fill(-IN, y, o, IN, y + 3, o + 1, 'bookshelf')
    else: L.fill(o, y, -IN, o + 1, y + 3, IN, 'bookshelf')
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'dark_oak_planks')
L.fill(2, FLOOR + 1, 2, 6, FLOOR + 3, 6, 'black_concrete'); L.fill(3, FLOOR + 1, 3, 5, FLOOR + 3, 5, 'water')
L.fill(4, FLOOR + 4, 4, 4, FLOOR + 10, 4, 'white_wool')       # plume
LV.append(L)

# ------------------------------------------------------------------ 9. La forêt
L = Lv(8, 'La forêt', 'green', 'oak_log', 'Canopée, branches et toiles, champignons... les nénuphars ne sont PAS de l\'eau !')
L.shell(mats=['moss_block', 'oak_leaves[persistent=true]', 'mossy_cobblestone'], acts=('glowstone', 'shroomlight'))
prev = (0, 0)
for y in spread(TOP - 8, A1 + 2, 7):                                     # acte 1 : canopée trouée
    h = (max(-8, min(8, prev[0] + L.rnd.randint(-3, 3))), max(-8, min(8, prev[1] + L.rnd.randint(-3, 3)))); prev = h
    h2 = (L.rnd.randint(-8, 8), L.rnd.randint(-8, 8))
    L.layer(y, lambda x, z, h=h, h2=h2: None if math.hypot(x - h[0], z - h[1]) < 2.6 or math.hypot(x - h2[0], z - h2[1]) < 2.6
            else ('flowering_azalea_leaves[persistent=true]' if (x * 7 + z * 3) % 5 == 0 else 'oak_leaves[persistent=true]'))
for y in spread(A1 - 6, A2 + 2, 6):                                      # acte 2 : branches, feuillages, toiles
    side = L.rnd.randint(0, 3); o = L.rnd.randint(-7, 7); ln = L.rnd.randint(7, 13)
    for s in range(ln):
        x, z = [(-IN + s, o), (IN - s, o), (o, -IN + s), (o, IN - s)][side]
        L.set(x, y - s // 3, z, 'oak_log')
    x, z = [(-IN + ln, o), (IN - ln, o), (o, -IN + ln), (o, IN - ln)][side]
    L.ball(x, y - ln // 3, z, 2, 'oak_leaves[persistent=true]')
    if L.rnd.random() < 0.6: L.set(L.rnd.randint(-8, 8), y - 3, L.rnd.randint(-8, 8), 'cobweb')
for y in spread(A2 - 8, FLOOR + 14, 12):                                 # acte 3 : champignons géants
    x, z = L.rnd.randint(-5, 5), L.rnd.randint(-5, 5)
    cap = L.rnd.choice(['red_mushroom_block', 'brown_mushroom_block'])
    L.disc(y, 4, cap, x, z); L.disc(y + 1, 3, cap, x, z); L.fill(x, y - 5, z, x, y - 1, z, 'mushroom_stem')
L.make_path(5); L.keep_path(TOP - 2, FLOOR + 8)
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'grass_block')
L.disc(FLOOR, 6, 'water')
for _ in range(16):
    x, z = L.rnd.randint(-5, 5), L.rnd.randint(-5, 5)
    if x * x + z * z <= 30: L.set(x, FLOOR + 1, z, 'lily_pad')
LV.append(L)

# ------------------------------------------------------------------ 10. Les nuages
L = Lv(9, 'Les nuages', 'aqua', 'light_blue_concrete', 'Nuages, arcs-en-ciel croisés, îles volantes : un seul bloc d\'eau au fond !')
L.shell(acts=('white_concrete', 'yellow_concrete'))
for y in spread(TOP - 8, A1 + 3, 5):                                     # acte 1 : nuages
    for _ in range(2): L.ball(L.rnd.randint(-8, 8), y, L.rnd.randint(-8, 8), L.rnd.randint(1, 3), 'white_wool')
for n, yc in enumerate(spread(A1 - 14, A2 + 14, 22)):                    # acte 2 : arcs-en-ciel croisés
    for b, c in enumerate(['red', 'orange', 'yellow', 'lime', 'light_blue', 'purple']):
        for a in range(0, 181, 3):
            th = math.radians(a)
            u, y = round((9 - b) * math.cos(th)), round(yc + (9 - b) * math.sin(th) * 0.8)
            L.set(u, y, 0, f'{c}_concrete') if n % 2 == 0 else L.set(0, y, u, f'{c}_concrete')
for y in spread(A1 - 6, A2 + 2, 6):                                      # nuages entre les arcs-en-ciel
    L.ball(L.rnd.randint(-8, 8), y, L.rnd.randint(-8, 8), L.rnd.randint(1, 2), 'white_wool')
for y in spread(A2 - 6, FLOOR + 12, 11):                                 # acte 3 : îles volantes
    x, z = L.rnd.randint(-6, 6), L.rnd.randint(-6, 6)
    L.disc(y, 3, 'grass_block', x, z); L.disc(y - 1, 2, 'dirt', x, z); L.set(x, y - 2, z, 'dirt')
    L.set(x, y + 1, z, L.rnd.choice(['poppy', 'dandelion', 'cornflower']))
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'white_wool')
for _ in range(7): L.ball(L.rnd.randint(-9, 9), FLOOR + 1, L.rnd.randint(-9, 9), 2, 'white_wool')
x, z = L.rnd.randint(-5, 5), L.rnd.randint(-5, 5)
L.fill(x - 1, FLOOR + 1, z - 1, x + 1, FLOOR + 3, z + 1, 'air'); L.set(x, FLOOR, z, 'water')
LV.append(L)

# ------------------------------------------------------------------ vérification : chaque niveau doit être faisable
# Chute simulée tick par tick (gravité de Minecraft : v = (v + 0,08) x 0,98) avec un déplacement horizontal limité à HS bloc/tick
# (75 % de la vitesse maximale en l'air, pour laisser de la marge). Si aucun passage n'existe, on perce un trou de 3 x 3 dans
# l'obstacle, à l'endroit où le joueur peut encore être, puis on recommence.
HS = 0.15
PASS = {'air', 'light', 'water', 'cobweb', 'rail'}
def voxels(L):
    g = {}
    for c in L.cmd:
        p = c.split()
        if p[0] == 'fill':
            x1, y1, z1, x2, y2, z2 = map(int, p[1:7]); b = p[7].split('[')[0][10:]
            if x2 - L.cx < -WALL - 1 or x1 - L.cx > WALL + 1: continue
            for x in range(max(x1, L.cx - IN - 1), min(x2, L.cx + IN + 1) + 1):
                for z in range(max(z1, CZ - IN - 1), min(z2, CZ + IN + 1) + 1):
                    for y in range(max(y1, FLOOR - 2), min(y2, TOP + 2) + 1): g[(x - L.cx, y, z - CZ)] = b
        else:
            x, y, z = map(int, p[1:4]); g[(x - L.cx, y, z - CZ)] = p[4].split('[')[0][10:]
    return g
def simulate(L):
    g = voxels(L)
    def free(x, y, z): return g.get((x, y, z), 'air') in PASS
    reach = {(x, z) for x in range(-7, 8) for z in range(-7, 8)}
    feet, v, budget = TOP + 1.0, 0.0, 0.0
    while reach:
        budget += HS
        while budget >= 1:
            budget -= 1
            reach |= {(x + dx, z + dz) for (x, z) in reach for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1))
                      if abs(x + dx) <= IN and abs(z + dz) <= IN and all(free(x + dx, y, z + dz) for y in range(math.floor(feet), math.floor(feet + 1.79) + 1))}
        v = (v + 0.08) * 0.98
        nf = feet - v
        ys = range(math.floor(nf), math.floor(feet + 1.79) + 1)
        for (x, z) in reach:
            if any(g.get((x, y, z)) == 'water' for y in ys): return None
        nxt = {(x, z) for (x, z) in reach if all(free(x, y, z) for y in ys)}
        if not nxt: return (reach, list(ys))
        reach, feet = nxt, nf
        if feet < FLOOR - 3: return (reach, [FLOOR])
    return (set(), [])
for L in LV:
    fixes = 0
    while True:
        res = simulate(L)
        if res is None: break
        reach, ys = res
        g = voxels(L)
        x, z = sorted(reach)[L.rnd.randrange(len(reach))]
        bad = [y for y in ys if any(g.get((xx, y, zz), 'air') not in PASS for xx in range(x - 1, x + 2) for zz in range(z - 1, z + 2))]
        if not bad or min(bad) <= FLOOR:          # on touche le fond sans eau : on met l'eau sous le joueur
            L.fill(x - 1, FLOOR, z - 1, x + 1, FLOOR, z + 1, 'water'); L.fill(x - 1, FLOOR + 1, z - 1, x + 1, FLOOR + 3, z + 1, 'air')
        else:
            L.fill(max(-IN, x - 1), min(bad), max(-IN, z - 1), min(IN, x + 1), max(bad), min(IN, z + 1), 'air')
        fixes += 1
        assert fixes < 80, L.name
    print(f'niveau {L.k + 1} ({L.name}) : faisable' + (f' après {fixes} passage(s) percé(s)' if fixes else ''))

N = len(LV)
# ------------------------------------------------------------------ fonctions de jeu
X1, X2 = -WALL - 6, (N - 1) * SPACING + WALL + 6
wr('fl_add', [f'forceload add {X1} {CZ - WALL - 6} {X2} {CZ + WALL + 6}'])
wr('fl_remove', [f'forceload remove {X1} {CZ - WALL - 6} {X2} {CZ + WALL + 6}', 'function mg:core/forceloads'])
parts = []
for L in LV:
    for i in range(0, len(L.cmd), 2500):
        parts.append([f'# Dropper Aventure : niveau {L.k + 1} ({L.name})'] + L.cmd[i:i + 2500])
parts.append(['function mg:dropadv/fl_remove', 'data modify storage mg:dropadv v3 set value 1b',
              'tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"The Dropper : Aventure construit (10 niveaux).","color":"green"}]'])
for k, p in enumerate(parts, 1):
    if k < len(parts): p = p + [f'schedule function mg:dropadv/build_{k + 1} 3t']
    wr(f'build_{k}', p)
wr('build', ['# (OP) Construit les 10 niveaux du Dropper Aventure', 'function mg:dropadv/fl_add', 'scoreboard players set $daw mg.st 0',
             'schedule function mg:dropadv/build_wait 20t'])
lo = []
for L in LV:
    lo += [f'execute store success score $dld mg.st unless block {L.cx} {TOP} {CZ} minecraft:bedrock', 'execute if score $dld mg.st matches 0 run return fail']
wr('loaded_all', lo + ['return 1'])
wr('build_wait', ['execute if function mg:dropadv/loaded_all run return run function mg:dropadv/build_1', 'scoreboard players add $daw mg.st 1',
                  'execute if score $daw mg.st matches 120.. run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Dropper Aventure : zone pas chargée.","color":"red"}]',
                  'schedule function mg:dropadv/build_wait 20t'])

wr('spawn', ['# Place @s sur le rebord de départ de son niveau (mg.dlv)'] +
   [f'execute if score @s mg.dlv matches {L.k + 1} run tp @s {L.cx + 0.5} {TOP + 1} {CZ - 11 + 0.5} 0 25' for L in LV] +
   ['scoreboard players set @s mg.cd 10', 'effect give @s minecraft:resistance 2 255 true'])
wr('prepare', ['# The Dropper : Aventure — préparation',
               'function mg:dropadv/fl_add',
               'scoreboard objectives add mg.dlv dummy [{"text":"⬇ Dropper : niveau","color":"aqua","bold":true}]',
               'scoreboard objectives add mg.dfl dummy',
               'scoreboard players set @a[tag=mg.play] mg.dlv 1', 'scoreboard players set @a[tag=mg.play] mg.dfl 0',
               'scoreboard players set $dat mg.st 0', 'scoreboard players set #k10 mg.st 10', 'scoreboard players set #k20 mg.st 20', 'scoreboard players set #k1000 mg.st 1000',
               'gamemode adventure @a[tag=mg.play]', 'clear @a[tag=mg.play]',
               'execute as @a[tag=mg.play] run function mg:dropadv/spawn',
               'scoreboard objectives setdisplay sidebar mg.dlv',
               'scoreboard players set $px mg.st 0', f'scoreboard players set $py mg.st {TOP + 3}', f'scoreboard players set $pz mg.st {CZ - 11}',
               'function mg:dropadv/titles'])
tl = ['kill @e[type=minecraft:text_display,tag=mg.dat]']
for L in LV:
    tl.append(f'summon minecraft:text_display {L.cx + 0.5} {TOP + 4} {CZ - 3.5} {{Tags:["mg.dat","mg.fx"],billboard:"vertical",'
              f'text:[{{"text":"Niveau {L.k + 1}\\n","color":"white"}},{{"text":"{L.name}","color":"{L.colr}","bold":true}},{{"text":"\\n{L.desc}","color":"gray"}}],'
              f'background:1342177280,transformation:{{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.6f,1.6f,1.6f]}}}}')
wr('titles', tl)
wr('go', ['# The Dropper : Aventure — départ',
          'effect give @a[tag=mg.play] minecraft:saturation infinite 0 true',
          'execute as @a[tag=mg.play] run function mg:dropper/attr_on',
          'tellraw @a[tag=mg.play] [{"text":"⬇ THE DROPPER : AVENTURE ! ","color":"aqua","bold":true},{"text":"10 niveaux à thème. Saute dans le puits et atterris dans l\'EAU du fond : tout le reste te renvoie en haut du niveau. Le premier à finir les 10 niveaux gagne (10 minutes au plus).","color":"gray"}]',
          'function mg:dropadv/show_level_all'])
wr('show_level_all', ['execute as @a[tag=mg.play] run function mg:dropadv/show_level'])
wr('show_level', [f'execute if score @s mg.dlv matches {L.k + 1} run title @s title [{{"text":"{L.name}","color":"{L.colr}","bold":true}}]' for L in LV] +
   [f'execute if score @s mg.dlv matches {L.k + 1} run title @s subtitle [{{"text":"Niveau {L.k + 1}/{N} : {L.desc}","color":"gray"}}]' for L in LV])
wr('tick', ['# The Dropper : Aventure — chaque tick',
            'scoreboard players add $dat mg.st 1',
            'scoreboard players remove @a[tag=mg.play,scores={mg.cd=1..}] mg.cd 1',
            'execute as @a[tag=mg.play] at @s if block ~ ~ ~ minecraft:water run function mg:dropadv/success',
            'execute as @a[tag=mg.play] at @s if block ~ ~ ~ minecraft:lava run function mg:dropadv/fail',
            'execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]',
            f'execute as @a[tag=mg.play,scores={{mg.cd=0,mg.t=..{TOP - 2}}}] at @s if data entity @s {{OnGround:1b}} unless block ~ ~ ~ minecraft:water run function mg:dropadv/fail',
            f'execute as @a[tag=mg.play,scores={{mg.t=..{FLOOR - 4}}}] run function mg:dropadv/fail',
            'scoreboard players operation $dam mg.st = $dat mg.st', 'scoreboard players operation $dam mg.st %= #k10 mg.st',
            'execute if score $dam mg.st matches 0 as @a[tag=mg.play] run function mg:dropadv/hud',
            'execute if score $dat mg.st matches 12000.. run return run function mg:dropadv/timeout',
            'execute unless entity @a[tag=mg.play] run function mg:core/draw'])
wr('hud', ['scoreboard players set $dsl mg.st 12000', 'scoreboard players operation $dsl mg.st -= $dat mg.st', 'scoreboard players operation $dsl mg.st /= #k20 mg.st'] +
   [f'execute if score @s mg.dlv matches {L.k + 1} run title @s actionbar [{{"text":"⬇ Niveau {L.k + 1}/{N} : ","color":"gray"}},{{"text":"{L.name}","color":"{L.colr}","bold":true}},'
    f'{{"text":"   ✖ ","color":"red"}},{{"score":{{"name":"@s","objective":"mg.dfl"}},"color":"white"}},{{"text":"   ⏱ ","color":"gold"}},{{"score":{{"name":"$dsl","objective":"mg.st"}},"color":"yellow"}},{{"text":" s","color":"gold"}}]'
    for L in LV])
wr('success', ['# @s atterrit dans l\'eau : niveau suivant (ou victoire)',
               'execute if score @s mg.cd matches 1.. run return 0',
               'execute at @s run particle minecraft:splash ~ ~ ~ 0.5 0.5 0.5 0.2 60',
               'execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.3',
               'scoreboard players add @s mg.dlv 1',
               f'execute if score @s mg.dlv matches {N + 1}.. run return run function mg:dropadv/finish',
               'tellraw @a[tag=mg.play] [{"text":"⬇ ","color":"aqua"},{"selector":"@s","color":"yellow"},{"text":" passe au niveau ","color":"gray"},{"score":{"name":"@s","objective":"mg.dlv"},"color":"aqua","bold":true}]',
               'function mg:dropadv/spawn', 'function mg:dropadv/show_level'])
wr('fail', ['# @s a touché autre chose que l\'eau : retour en haut du niveau',
            'execute if score @s mg.cd matches 1.. run return 0',
            'scoreboard players add @s mg.dfl 1',
            'execute at @s run particle minecraft:poof ~ ~0.2 ~ 0.3 0.2 0.3 0.05 15',
            'execute at @s run playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.8 1',
            'title @s actionbar [{"text":"✖ Raté ! Retour en haut du niveau...","color":"red"}]',
            'function mg:dropadv/spawn'])
wr('finish', [f'scoreboard players set @s mg.dlv {N}',
              f'tellraw @a[tag=!mg.surv] [{{"text":"🏆 ","color":"gold"}},{{"selector":"@s","color":"gold","bold":true}},{{"text":" termine les {N} niveaux du Dropper !","color":"yellow"}}]',
              'function mg:core/win_player'])
wr('timeout', ['# Temps écoulé : le plus avancé gagne (à égalité, le moins d\'échecs)',
               'execute as @a[tag=mg.play] run scoreboard players operation @s mg.t = @s mg.dlv',
               'execute as @a[tag=mg.play] run scoreboard players operation @s mg.t *= #k1000 mg.st',
               'execute as @a[tag=mg.play] run scoreboard players operation @s mg.t -= @s mg.dfl',
               'scoreboard players set $dbest mg.st -999999',
               'execute as @a[tag=mg.play] if score @s mg.t > $dbest mg.st run scoreboard players operation $dbest mg.st = @s mg.t',
               'tellraw @a[tag=!mg.surv] [{"text":"⏱ Temps écoulé !","color":"gold"}]',
               'execute as @a[tag=mg.play] if score @s mg.t = $dbest mg.st run tag @s add mg.dwin',
               'execute as @a[tag=mg.dwin,limit=1] run function mg:core/win_player',
               'tag @a remove mg.dwin'])
wr('cleanup', ['kill @e[type=minecraft:text_display,tag=mg.dat]', 'function mg:dropadv/fl_remove', 'scoreboard objectives setdisplay sidebar'])
print('niveaux', N, '| étapes de construction', len(parts), '| commandes', sum(len(L.cmd) for L in LV))

# ================================================================== DROPPER : DÉFI (id 65) — compétitif, niveau de l'Aventure tiré au hasard
# Tout le monde dans le même puits (réparti sur les 4 côtés du rebord) ; le premier dans l'eau gagne la manche ; premier à 3 manches.
WINS = 3
SIDES = [(0, -11, 0), (0, 11, 180), (-11, 0, -90), (11, 0, 90)]
wr('c_prepare', ['# Dropper : Défi — préparation',
                 'function mg:dropadv/fl_add',
                 'scoreboard objectives add mg.dpw dummy [{"text":"⬇ Dropper : Défi","color":"aqua","bold":true}]',
                 'scoreboard objectives add mg.dlv dummy', 'scoreboard objectives add mg.dfl dummy',
                 'scoreboard players set @a[tag=mg.play] mg.dpw 0',
                 'scoreboard players set #k10 mg.st 10', 'scoreboard players set #k20 mg.st 20', 'scoreboard players set #k4 mg.st 4',
                 'scoreboard players set $dcr mg.st 0', 'scoreboard players set $dcl mg.st 0', 'scoreboard players set $dcph mg.st 0',
                 'gamemode adventure @a[tag=mg.play]', 'clear @a[tag=mg.play]',
                 'scoreboard objectives setdisplay sidebar mg.dpw',
                 'function mg:dropadv/titles',
                 'function mg:dropadv/c_pick',
                 'scoreboard players set $dci mg.st 0',
                 'execute as @a[tag=mg.play] run function mg:dropadv/c_spawn'])
wr('c_pick', ['# Nouveau niveau au hasard (jamais deux fois de suite le même)',
              'scoreboard players operation $dcp mg.st = $dcl mg.st',
              f'execute store result score $dcl mg.st run random value 1..{N}',
              f'execute if score $dcl mg.st = $dcp mg.st run scoreboard players add $dcl mg.st 1',
              f'execute if score $dcl mg.st matches {N + 1}.. run scoreboard players set $dcl mg.st 1',
              'scoreboard players add $dcr mg.st 1',
              'scoreboard players set $px mg.st 0', f'scoreboard players set $py mg.st {TOP + 3}', f'scoreboard players set $pz mg.st {CZ - 11}'])
sp = ['# Place @s sur un des 4 côtés du rebord du niveau de la manche ($dcl)',
      'scoreboard players operation @s mg.dlv = $dcl mg.st',
      'scoreboard players operation $dcs mg.st = $dci mg.st', 'scoreboard players operation $dcs mg.st %= #k4 mg.st', 'scoreboard players add $dci mg.st 1']
for L in LV:
    for s_, (dx, dz, yaw) in enumerate(SIDES):
        sp.append(f'execute if score $dcl mg.st matches {L.k + 1} if score $dcs mg.st matches {s_} run tp @s {L.cx + dx + 0.5} {TOP + 1} {CZ + dz + 0.5} {yaw} 25')
sp += ['scoreboard players set @s mg.cd 20', 'effect give @s minecraft:resistance 2 255 true']
wr('c_spawn', sp)
wr('c_go', ['# Dropper : Défi — départ de la première manche',
            'effect give @a[tag=mg.play] minecraft:saturation infinite 0 true',
            'execute as @a[tag=mg.play] run function mg:dropper/attr_on',
            '''tellraw @a[tag=mg.play] [{"text":"⬇ DROPPER : DÉFI ! ","color":"aqua","bold":true},{"text":"Tout le monde dans le même puits, tiré au hasard parmi les niveaux de l'Aventure. Le premier dans l'EAU gagne la manche ; premier à ''' + str(WINS) + ''' manches !","color":"gray"}]''',
            'function mg:dropadv/c_round'])
wr('c_round', ['# Nouvelle manche : tout le monde en haut du niveau tiré',
               'scoreboard players set $dcph mg.st 1', 'scoreboard players set $dct mg.st 0', 'scoreboard players set $dci mg.st 0',
               'execute as @a[tag=mg.play] run function mg:dropadv/c_spawn',
               'execute as @a[tag=mg.play] run function mg:dropadv/show_level',
               'execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.4'])
wr('c_tick', ['# Dropper : Défi — chaque tick',
              'scoreboard players remove @a[tag=mg.play,scores={mg.cd=1..}] mg.cd 1',
              'scoreboard players add $dct mg.st 1',
              'execute if score $dcph mg.st matches 2 run return run function mg:dropadv/c_inter',
              'execute as @a[tag=mg.play,scores={mg.cd=0}] at @s if block ~ ~ ~ minecraft:water run function mg:dropadv/c_win',
              'execute if score $dcph mg.st matches 2 run return 0',
              'execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]',
              'execute as @a[tag=mg.play,scores={mg.cd=0,mg.t=..' + str(TOP - 2) + '}] at @s if data entity @s {OnGround:1b} unless block ~ ~ ~ minecraft:water run function mg:dropadv/c_fail',
              'execute as @a[tag=mg.play,scores={mg.t=..' + str(FLOOR - 4) + '}] run function mg:dropadv/c_fail',
              'scoreboard players operation $dam mg.st = $dct mg.st', 'scoreboard players operation $dam mg.st %= #k10 mg.st',
              'execute if score $dam mg.st matches 0 as @a[tag=mg.play] run function mg:dropadv/c_hud',
              'execute if score $dct mg.st matches 1800.. run function mg:dropadv/c_timeout',
              'execute unless entity @a[tag=mg.play] run function mg:core/draw'])
wr('c_fail', ['execute if score @s mg.cd matches 1.. run return 0',
              'execute at @s run particle minecraft:poof ~ ~0.2 ~ 0.3 0.2 0.3 0.05 15',
              'execute at @s run playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.8 1',
              'title @s actionbar [{"text":"✖ Raté ! Retour en haut...","color":"red"}]',
              'function mg:dropadv/c_spawn'])
wr('c_win', ['# @s atterrit dans l\'eau en premier : il gagne la manche',
             'execute unless score $dcph mg.st matches 1 run return 0',
             'scoreboard players add @s mg.dpw 1',
             'scoreboard players set $dcph mg.st 2', 'scoreboard players set $dct mg.st 0',
             'execute at @s run particle minecraft:splash ~ ~ ~ 0.5 0.5 0.5 0.2 80',
             'title @a[tag=!mg.surv] title [{"selector":"@s","color":"gold","bold":true}]',
             'title @a[tag=!mg.surv] subtitle [{"text":"remporte la manche !","color":"yellow"}]',
             'tellraw @a[tag=!mg.surv] [{"text":"⬇ ","color":"aqua"},{"selector":"@s","color":"gold","bold":true},{"text":" gagne la manche (","color":"gray"},{"score":{"name":"@s","objective":"mg.dpw"},"color":"yellow"},{"text":"/' + str(WINS) + ')","color":"gray"}]',
             'execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.2',
             'execute if score @s mg.dpw matches ' + str(WINS) + '.. run function mg:core/win_player'])
wr('c_inter', ['# Pause de 3 s entre deux manches, puis nouveau niveau',
               'execute if score $dct mg.st matches 60.. run function mg:dropadv/c_pick',
               'execute if score $dct mg.st matches 60.. run function mg:dropadv/c_round'])
wr('c_timeout', ['# 90 s sans gagnant : manche annulée, nouveau niveau',
                 '''tellraw @a[tag=mg.play] [{"text":"⏱ Personne n'a réussi : on change de niveau !","color":"gold"}]''',
                 'scoreboard players set $dcph mg.st 2', 'scoreboard players set $dct mg.st 40'])
hud = ['scoreboard players set $dsl mg.st 1800', 'scoreboard players operation $dsl mg.st -= $dct mg.st', 'scoreboard players operation $dsl mg.st /= #k20 mg.st']
for L in LV:
    hud.append('execute if score $dcl mg.st matches ' + str(L.k + 1) + ' run title @s actionbar [{"text":"⬇ Manche ","color":"gray"},{"score":{"name":"$dcr","objective":"mg.st"},"color":"white"},'
               '{"text":" : ","color":"gray"},{"text":"' + L.name + '","color":"' + L.colr + '","bold":true},{"text":"   ★ ","color":"gold"},{"score":{"name":"@s","objective":"mg.dpw"},"color":"yellow"},'
               '{"text":"/' + str(WINS) + '   ⏱ ","color":"gold"},{"score":{"name":"$dsl","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gold"}]')
wr('c_hud', hud)
