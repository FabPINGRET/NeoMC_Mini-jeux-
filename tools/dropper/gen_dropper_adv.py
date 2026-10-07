"""The Dropper : Aventure (id 64) — 10 niveaux à thème enchaînés : python gen_dropper_adv.py <racine du dépôt>

Inspiré des maps de dropper classiques (puits à thème, une idée par niveau), constructions originales.
Chaque niveau est un puits de 21 x 21 (intérieur) sur ~105 blocs : on part du rebord en haut (y 201), on saute dans l'ouverture
et on doit finir dans l'eau du fond. Toucher quoi que ce soit d'autre = retour en haut du niveau ; réussir = niveau suivant.
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
TOP, FLOOR = 200, 95          # rebord de départ, sol du fond (l'eau est juste au-dessus)
IN, WALL = 10, 13             # demi-intérieur, demi-extérieur (murs de 3)
SPACING = 40
LEVELS = []

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
    def inside(self, x, z): return abs(x) <= IN and abs(z) <= IN
    def shell(self, round_=False, mats=None):
        """murs, intérieur vidé, rebord de départ, éclairage invisible, sol du fond."""
        for y in range(FLOOR - 3, TOP, 40):
            self.fill(-WALL, y, -WALL, WALL, min(y + 39, TOP - 1), WALL, self.wall)
        if round_:
            for y in range(FLOOR + 1, TOP + 1, 16):
                self.disc_range(y, min(y + 15, TOP), IN)
        else:
            for y in range(FLOOR + 1, TOP + 1, 60):
                self.fill(-IN, y, -IN, IN, min(y + 59, TOP), IN, 'air')
        if mats:
            for _ in range(400):
                x, z = self.rnd.randint(-IN - 1, IN + 1), self.rnd.randint(-IN - 1, IN + 1)
                if abs(x) == IN + 1 or abs(z) == IN + 1:
                    self.set(x, self.rnd.randint(FLOOR, TOP), z, self.rnd.choice(mats))
        # rebord : plancher à y TOP autour d'une ouverture 15 x 15, garde-corps
        self.fill(-WALL - 4, TOP + 1, -WALL - 4, WALL + 4, TOP + 6, WALL + 4, 'air')
        self.fill(-WALL - 4, TOP, -WALL - 4, WALL + 4, TOP, WALL + 4, 'polished_andesite')
        self.fill(-7, TOP, -7, 7, TOP, 7, 'air')
        self.fill(-8, TOP, -8, 8, TOP, -8, 'yellow_concrete'); self.fill(-8, TOP, 8, 8, TOP, 8, 'yellow_concrete')
        self.fill(-8, TOP, -8, -8, TOP, 8, 'yellow_concrete'); self.fill(8, TOP, -8, 8, TOP, 8, 'yellow_concrete')
        self.fill(-WALL - 4, TOP + 1, -WALL - 4, WALL + 4, TOP + 4, -WALL - 4, 'glass')
        self.fill(-WALL - 4, TOP + 1, WALL + 4, WALL + 4, TOP + 4, WALL + 4, 'glass')
        self.fill(-WALL - 4, TOP + 1, -WALL - 4, -WALL - 4, TOP + 4, WALL + 4, 'glass')
        self.fill(WALL + 4, TOP + 1, -WALL - 4, WALL + 4, TOP + 4, WALL + 4, 'glass')
        self.fill(-WALL - 4, TOP + 6, -WALL - 4, WALL + 4, TOP + 6, WALL + 4, 'barrier')
        for y in range(FLOOR + 4, TOP, 9):
            for (x, z) in ((-6, -6), (6, -6), (-6, 6), (6, 6), (0, 0)):
                self.set(x, y, z, 'light[level=15]')
    def disc_range(self, y1, y2, r):
        for a in range(-r, r + 1):
            w = int(math.sqrt(max(0, r * r + r - a * a)))
            self.fill(a, y1, -w, a, y2, w, 'air')

LV = []
# ------------------------------------------------------------------ 1. Arc-en-ciel : entonnoir
L = Lv(0, 'Arc-en-ciel', 'light_purple', 'white_concrete', 'Des anneaux colorés qui se resserrent : reste au milieu !')
L.shell()
RAIN = ['red', 'orange', 'yellow', 'lime', 'light_blue', 'blue', 'purple', 'magenta']
n = 0
for y in range(TOP - 8, FLOOR + 6, -6):
    t = (TOP - 8 - y) / (TOP - 8 - FLOOR - 6)
    r_open = max(1, round(8 - 7 * t))
    ox, oz = (L.rnd.randint(-1, 1), L.rnd.randint(-1, 1)) if r_open < 7 else (0, 0)
    L.fill(-IN, y, -IN, IN, y, IN, f'{RAIN[n % 8]}_concrete')
    L.fill(ox - r_open, y, oz - r_open, ox + r_open, y, oz + r_open, 'air')
    n += 1
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'white_concrete')
L.fill(-2, FLOOR, -2, 2, FLOOR, 2, 'light_blue_concrete'); L.fill(-1, FLOOR, -1, 1, FLOOR, 1, 'water')
LV.append(L)

# ------------------------------------------------------------------ 2. Spirale : boules lumineuses qui tournent
L = Lv(1, 'Spirale', 'yellow', 'black_concrete', 'Des boules de lumière tournent en descendant : glisse entre elles.')
L.shell(round_=True)
a = 0.0
for y in range(TOP - 10, FLOOR + 8, -5):
    for ph in (0, math.pi):
        x, z = round(5.5 * math.cos(a + ph)), round(5.5 * math.sin(a + ph))
        L.ball(x, y, z, 2, 'glowstone' if ph == 0 else 'sea_lantern')
    a += math.radians(38)
L.disc(FLOOR, IN, 'black_concrete')
L.disc(FLOOR, 4, 'light_blue_concrete'); L.disc(FLOOR, 3, 'water')
LV.append(L)

# ------------------------------------------------------------------ 3. La mine : grotte, poutres, rails, toiles
L = Lv(2, 'La mine', 'gray', 'stone', 'Une vieille mine : évite les poutres, les toiles ralentissent.')
L.shell(mats=['coal_ore', 'iron_ore', 'andesite', 'gravel', 'cobblestone', 'copper_ore'])
for y in range(FLOOR + 1, TOP, 2):                                  # parois irrégulières
    for _ in range(10):
        x, z = L.rnd.randint(-IN, IN), L.rnd.choice([-IN, IN])
        if L.rnd.random() < 0.5: x, z = z, x
        L.ball(x, y, z, L.rnd.randint(1, 2), L.rnd.choice(['stone', 'cobblestone', 'andesite', 'tuff']))
L.fill(-7, TOP - 3, -7, 7, TOP - 1, 7, 'air')
for y in range(TOP - 12, FLOOR + 8, -8):
    o = L.rnd.randint(-6, 6)
    if L.rnd.random() < 0.5:
        L.fill(-IN, y, o, IN, y, o + 1, 'oak_log[axis=x]'); L.fill(-IN, y + 1, o, IN, y + 1, o, 'rail[shape=east_west]')
        L.fill(o, y - 3, -IN, o, y - 1, -IN, 'oak_fence')
    else:
        L.fill(o, y, -IN, o + 1, y, IN, 'oak_log[axis=z]'); L.fill(o, y + 1, -IN, o, y + 1, IN, 'rail')
    L.set(L.rnd.randint(-8, 8), y - 1, L.rnd.randint(-8, 8), 'cobweb')
    L.set(o, y - 1, o, 'lantern[hanging=true]')
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'gravel')
L.disc(FLOOR, 3, 'water')
LV.append(L)

# ------------------------------------------------------------------ 4. Rideaux : nappes de laine percées
L = Lv(3, 'Rideaux', 'white', 'quartz_block', 'Des rideaux de laine percés de quelques trous : trouve le passage.')
L.shell()
cols = ['white', 'pink', 'light_blue', 'lime', 'yellow', 'orange']
for n, y in enumerate(range(TOP - 9, FLOOR + 6, -8)):
    L.fill(-IN, y, -IN, IN, y, IN, f'{cols[n % len(cols)]}_wool')
    for _ in range(L.rnd.randint(2, 3)):
        x, z = L.rnd.randint(-IN, IN - 2), L.rnd.randint(-IN, IN - 2)
        L.fill(x, y, z, x + 2, y, z + 2, 'air')
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'quartz_block')
x, z = L.rnd.randint(-6, 5), L.rnd.randint(-6, 5)
L.fill(x, FLOOR, z, x + 1, FLOOR, z + 1, 'water')
LV.append(L)

# ------------------------------------------------------------------ 5. Trous piégés : certains trous sont fermés (verre)
L = Lv(4, 'Trous piégés', 'dark_purple', 'obsidian', 'Des planchers à 9 trous... mais certains sont fermés par du verre !')
L.shell()
HOLES = [(-7, -7), (-1, -7), (5, -7), (-7, -1), (-1, -1), (5, -1), (-7, 5), (-1, 5), (5, 5)]
for y in range(TOP - 10, FLOOR + 8, -10):
    L.fill(-IN, y, -IN, IN, y, IN, 'obsidian')
    closed = set(L.rnd.sample(range(9), L.rnd.randint(3, 6)))
    for h, (x, z) in enumerate(HOLES):
        L.fill(x, y, z, x + 2, y, z + 2, 'glass' if h in closed else 'air')
    L.set(-IN, y + 2, 0, 'soul_lantern'); L.set(IN, y + 2, 0, 'soul_lantern')
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'obsidian')
x, z = L.rnd.choice(HOLES)
L.fill(x, FLOOR, z, x + 2, FLOOR, z + 2, 'water')
LV.append(L)

# ------------------------------------------------------------------ 6. L'Enfer : basalte, champignons géants, magma
L = Lv(5, 'L\'Enfer', 'red', 'netherrack', 'Le Nether : piliers de basalte et champignons géants, ne touche à rien !')
L.shell(mats=['magma_block', 'nether_quartz_ore', 'nether_gold_ore', 'blackstone', 'crimson_nylium'])
for y in range(TOP - 10, FLOOR + 8, -7):
    kind = L.rnd.random()
    if kind < 0.4:                                     # pilier de basalte qui sort d'un mur
        side = L.rnd.randint(0, 3); o = L.rnd.randint(-7, 7); ln = L.rnd.randint(7, 13)
        a1, a2 = -IN, -IN + ln
        if side == 0: L.fill(a1, y, o, a2, y + 1, o + 1, 'basalt[axis=x]')
        elif side == 1: L.fill(-a2, y, o, -a1, y + 1, o + 1, 'basalt[axis=x]')
        elif side == 2: L.fill(o, y, a1, o + 1, y + 1, a2, 'basalt[axis=z]')
        else: L.fill(o, y, -a2, o + 1, y + 1, -a1, 'basalt[axis=z]')
    else:                                              # champignon géant suspendu (chapeau + pied)
        x, z = L.rnd.randint(-5, 5), L.rnd.randint(-5, 5)
        cap = L.rnd.choice(['nether_wart_block', 'warped_wart_block'])
        L.disc(y, 3, cap, x, z); L.disc(y + 1, 2, cap, x, z)
        L.fill(x, y + 2, z, x, y + 6, z, 'crimson_stem' if cap == 'nether_wart_block' else 'warped_stem')
        L.set(x + 1, y - 1, z, 'shroomlight')
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'blackstone')
L.disc(FLOOR, 4, 'magma_block')
L.disc(FLOOR, 2, 'water')
LV.append(L)

# ------------------------------------------------------------------ 7. Le salon géant : tu es minuscule
L = Lv(6, 'Le salon géant', 'gold', 'yellow_terracotta', 'Tu es minuscule dans un salon : vise le bocal à poisson !')
L.shell()
for y in range(FLOOR + 1, TOP, 4):                          # papier peint rayé
    for a in range(-IN - 1, IN + 2, 3):
        for (x, z) in ((a, -IN - 1), (a, IN + 1), (-IN - 1, a), (IN + 1, a)):
            L.set(x, y, z, 'white_terracotta')
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'spruce_planks')
L.fill(-6, FLOOR + 1, -6, 6, FLOOR + 1, 6, 'red_carpet')
# lustre près du haut
L.disc(TOP - 8, 3, 'gold_block'); L.fill(0, TOP - 7, 0, 0, TOP - 1, 0, 'iron_bars')
for (x, z) in ((-3, 0), (3, 0), (0, -3), (0, 3)): L.set(x, TOP - 9, z, 'end_rod')
# étagère le long d'un mur avec des livres géants
L.fill(-IN, 172, -IN, IN, 173, -4, 'dark_oak_planks')
for x in range(-9, 10, 3): L.fill(x, 174, -IN, x + 1, 179, -6, L.rnd.choice(['red_wool', 'blue_wool', 'green_wool', 'brown_wool']))
# abat-jour de la lampe sur pied
L.disc(155, 5, 'white_wool', -3, 4); L.disc(154, 6, 'white_wool', -3, 4); L.disc(154, 4, 'air', -3, 4)
L.fill(-3, FLOOR + 1, 4, -3, 153, 4, 'gray_concrete')
# table : plateau sur les 2/3, pieds
L.fill(-IN, 130, -2, IN, 131, IN, 'oak_planks')
L.fill(-2, 130, 2, 2, 131, 6, 'air')                                   # trou dans la nappe (fleur posée à côté)
for (x, z) in ((-9, -1), (9, -1), (-9, 9), (9, 9)): L.fill(x, FLOOR + 1, z, x, 129, z, 'oak_log')
L.set(4, 132, 6, 'flower_pot')
# chaise
L.fill(4, 112, -9, IN, 113, -3, 'birch_planks'); L.fill(IN, 114, -9, IN, 124, -3, 'birch_planks')
# bocal à poisson : verre autour, eau dedans, ouverture 3 x 3
L.fill(-3, FLOOR + 1, -3, 3, FLOOR + 4, 3, 'glass')
L.fill(-2, FLOOR + 1, -2, 2, FLOOR + 3, 2, 'water')
L.fill(-1, FLOOR + 4, -1, 1, FLOOR + 4, 1, 'water')
LV.append(L)

# ------------------------------------------------------------------ 8. La bibliothèque : étagères géantes, livres volants
L = Lv(7, 'La bibliothèque', 'dark_red', 'bookshelf', 'Étagères géantes et livres volants : vise l\'encrier.')
L.shell()
for y in range(TOP - 10, FLOOR + 8, -9):
    side = L.rnd.randint(0, 3); depth = L.rnd.randint(6, 11)
    if side == 0: L.fill(-IN, y, -IN, IN, y + 2, -IN + depth, 'bookshelf')
    elif side == 1: L.fill(-IN, y, IN - depth, IN, y + 2, IN, 'bookshelf')
    elif side == 2: L.fill(-IN, y, -IN, -IN + depth, y + 2, IN, 'bookshelf')
    else: L.fill(IN - depth, y, -IN, IN, y + 2, IN, 'bookshelf')
    x, z = L.rnd.randint(-6, 4), L.rnd.randint(-6, 4)            # livre ouvert volant
    L.fill(x, y - 4, z, x + 2, y - 4, z + 4, 'white_wool'); L.fill(x - 1, y - 5, z, x + 3, y - 5, z + 4, L.rnd.choice(['red_wool', 'brown_wool', 'blue_wool']))
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'dark_oak_planks')
L.fill(2, FLOOR + 1, 2, 6, FLOOR + 3, 6, 'black_concrete'); L.fill(3, FLOOR + 1, 3, 5, FLOOR + 3, 5, 'water')
L.fill(4, FLOOR + 4, 4, 4, FLOOR + 9, 4, 'white_wool')       # plume
LV.append(L)

# ------------------------------------------------------------------ 9. La forêt : branches, feuillages, toiles, nénuphars pièges
L = Lv(8, 'La forêt', 'green', 'oak_log', 'Branches et feuillages, toiles d\'araignée... et les nénuphars ne sont PAS de l\'eau !')
L.shell(mats=['moss_block', 'oak_leaves[persistent=true]'])
for y in range(TOP - 8, FLOOR + 8, -6):
    side = L.rnd.randint(0, 3); o = L.rnd.randint(-6, 6); ln = L.rnd.randint(6, 12)
    for s in range(ln):
        yy = y - s // 3
        x, z = [(-IN + s, o), (IN - s, o), (o, -IN + s), (o, IN - s)][side]
        L.set(x, yy, z, 'oak_log')
    x, z = [(-IN + ln, o), (IN - ln, o), (o, -IN + ln), (o, IN - ln)][side]
    L.ball(x, y - ln // 3, z, 2, 'oak_leaves[persistent=true]')
    if L.rnd.random() < 0.6: L.set(L.rnd.randint(-8, 8), y - 3, L.rnd.randint(-8, 8), 'cobweb')
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'grass_block')
L.disc(FLOOR, 6, 'water')
for _ in range(14):
    x, z = L.rnd.randint(-5, 5), L.rnd.randint(-5, 5)
    if x * x + z * z <= 30: L.set(x, FLOOR + 1, z, 'lily_pad')
LV.append(L)

# ------------------------------------------------------------------ 10. Les nuages : final sur un seul bloc d'eau
L = Lv(9, 'Les nuages', 'aqua', 'light_blue_concrete', 'Le grand final dans le ciel : un seul bloc d\'eau au fond !')
L.shell()
for y in range(TOP - 8, FLOOR + 10, -5):
    for _ in range(2):
        x, z = L.rnd.randint(-7, 7), L.rnd.randint(-7, 7)
        L.ball(x, y, z, L.rnd.randint(1, 3), 'white_wool')
for b, c in enumerate(['red', 'orange', 'yellow', 'lime', 'light_blue', 'purple']):     # arc-en-ciel en travers
    for a in range(0, 181, 4):
        th = math.radians(a)
        x, y = round((8 - b) * math.cos(th)), round(150 + (8 - b) * math.sin(th))
        L.set(x, y, 0, f'{c}_concrete')
L.fill(-IN, FLOOR, -IN, IN, FLOOR, IN, 'white_wool')
for _ in range(6): L.ball(L.rnd.randint(-8, 8), FLOOR + 1, L.rnd.randint(-8, 8), 2, 'white_wool')
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
parts.append(['function mg:dropadv/fl_remove', 'data modify storage mg:dropadv built set value 1b',
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
