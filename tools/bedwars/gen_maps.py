"""Cartes alternatives du Bedwars : génère data/mg/function/bedwars/map/*.mcfunction.

Les 3 cartes sont construites au MÊME endroit que la classique (x -45..45, z 1155..1245)
et respectent exactement ses points d'ancrage (lits, générateurs, spawns, boutiques,
diamant, perchoir), que la logique du jeu utilise en dur.
  1. Caldeira  (volcan)            : cratère central + 4 îlots d'or bonus (gen_1) ;
  2. Hanami    (jardin des cerisiers) : terrasses surélevées, pagode, ponts inachevés ;
  3. Banquise  (glacier)           : igloos, pics de glace, banquise fragmentée.
Fichiers écrits : map/wipe, map/build_k, map/info_k, map/gen_1.
Le générateur vérifie lui-même ancrages, limites, perchoir et absence de chemin à pied
entre les îles (les joueurs doivent construire des ponts).
Lancer depuis la racine du dépôt : python3 tools/bedwars/gen_maps.py
"""
import math
import os
import random
from collections import deque

OUT = os.path.join('data', 'mg', 'function', 'bedwars', 'map')
X0, X1, Z0, Z1, YMIN, YMAX = -45, 45, 1155, 1245, 45, 100

# ---------------------------------------------------------------- ancrages
TEAMS = {  # centre du carré 11x11, direction « vers l'extérieur »
    'red':    dict(c=(-32, 1200), out=(-1, 0)),
    'blue':   dict(c=(32, 1200), out=(1, 0)),
    'green':  dict(c=(0, 1168), out=(0, -1)),
    'yellow': dict(c=(0, 1232), out=(0, 1)),
}
BEDS = {  # lignes copiées de bedwars/build.mcfunction
    'red':    [(-35, 1200, 'setblock -35 64 1200 minecraft:red_bed[facing=west,part=foot] strict'),
               (-36, 1200, 'setblock -36 64 1200 minecraft:red_bed[facing=west,part=head] strict')],
    'blue':   [(35, 1200, 'setblock 35 64 1200 minecraft:blue_bed[facing=east,part=foot] strict'),
               (36, 1200, 'setblock 36 64 1200 minecraft:blue_bed[facing=east,part=head] strict')],
    'green':  [(0, 1164, 'setblock 0 64 1164 minecraft:green_bed[facing=north,part=foot] strict'),
               (0, 1163, 'setblock 0 64 1163 minecraft:green_bed[facing=north,part=head] strict')],
    'yellow': [(0, 1236, 'setblock 0 64 1236 minecraft:yellow_bed[facing=south,part=foot] strict'),
               (0, 1237, 'setblock 0 64 1237 minecraft:yellow_bed[facing=south,part=head] strict')],
}
GOLD = {'red': (-28, 1200), 'blue': (28, 1200), 'green': (0, 1172), 'yellow': (0, 1228)}
SPAWN = {'red': (-32, 1200), 'blue': (31, 1200), 'green': (0, 1168), 'yellow': (0, 1232)}
SHOPS = {
    'red':    [(-34, 1196), (-32, 1196), (-34, 1204), (-32, 1204)],
    'blue':   [(33, 1196), (31, 1196), (33, 1204), (31, 1204)],
    'green':  [(-4, 1166), (-4, 1168), (4, 1166), (4, 1168)],
    'yellow': [(-4, 1233), (-4, 1231), (4, 1233), (4, 1231)],
}
DIAMOND = (0, 1200)
SQUARES = {t: (d['c'][0] - 5, d['c'][1] - 5, d['c'][0] + 5, d['c'][1] + 5) for t, d in TEAMS.items()}
CENTER_SQ = (-4, 1196, 4, 1204)
PERCH = (-2, 80, 1198, 2, 90, 1202)

# Colonnes qui doivent rester libres (air y 64..66 ; y 65..66 au-dessus des lits)
AIR_COLS = [DIAMOND] + list(GOLD.values()) + list(SPAWN.values()) + [c for v in SHOPS.values() for c in v]
BED_COLS = [(x, z) for v in BEDS.values() for x, z, _ in v]

# Blocs qui tiennent sur / sous un autre : posés après les blocs pleins
ATTACHED = ('lantern', 'torch', 'petals', 'short_grass', 'fern', 'carpet', 'roots', 'fungus', 'flower',
            'tulip', 'poppy', 'dandelion', 'allium', 'azure', 'oxeye', 'lily', 'cornflower', 'sprouts',
            'chain', 'candle', 'button', 'leaf_litter', 'bush', 'sapling', 'vine')
# Interdits : dangereux, instables (gravité, fonte) ou confondables avec les blocs achetés (laine, planches de chêne)
FORBIDDEN = ('lava', 'fire', 'magma', 'campfire', 'tnt', 'wool', 'powder_snow', 'cactus', 'obsidian', 'bedrock',
             'berry', 'dripstone', 'sand', 'gravel', 'concrete_powder', 'lightning_rod', 'water')
FORBIDDEN_EXACT = ('minecraft:oak_planks', 'minecraft:ice', 'minecraft:snow')
COLORS = ['red', 'blue', 'green', 'yellow']
FACE = {(1, 0): 'east', (-1, 0): 'west', (0, 1): 'south', (0, -1): 'north'}


def W(name, lines):
    with open(os.path.join(OUT, name + '.mcfunction'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


def in_rect(x, z, r):
    return r[0] <= x <= r[2] and r[1] <= z <= r[3]


# ---------------------------------------------------------------- modèle de carte
class Map:
    def __init__(self, seed):
        self.b = {}
        self.r = random.Random(seed)
        self.land_cells = {}     # (x,z) -> hauteur du sol (pour le contrôle de connexité)

    # --- blocs
    def set(self, x, y, z, blk):
        if not (X0 <= x <= X1 and Z0 <= z <= Z1 and YMIN <= y <= YMAX):
            return
        if not blk.startswith('minecraft:'):
            blk = 'minecraft:' + blk
        self.b[(x, y, z)] = blk

    def clear(self, x, y, z):
        self.b.pop((x, y, z), None)

    def get(self, x, y, z):
        return self.b.get((x, y, z))

    def box(self, x1, y1, z1, x2, y2, z2, blk):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                for z in range(min(z1, z2), max(z1, z2) + 1):
                    self.set(x, y, z, blk)

    def pick(self, choices):
        """choices : [(bloc, poids), ...]"""
        t = self.r.random() * sum(w for _, w in choices)
        for b, w in choices:
            t -= w
            if t <= 0:
                return b
        return choices[-1][0]

    # --- formes
    def blob(self, cx, cz, rad, amp=1.2, rect=None):
        """Disque bruité (forme d'île) ; rect = carré à inclure en entier."""
        ph = [self.r.random() * 6.3 for _ in range(3)]
        cells = set()
        R = int(rad + amp + 2)
        for x in range(int(cx) - R, int(cx) + R + 1):
            for z in range(int(cz) - R, int(cz) + R + 1):
                dx, dz = x - cx, z - cz
                a = math.atan2(dz, dx)
                rr = rad + amp * (0.6 * math.sin(3 * a + ph[0]) + 0.4 * math.sin(5 * a + ph[1])
                                  + 0.3 * math.sin(2 * a + ph[2]))
                if dx * dx + dz * dz <= rr * rr and X0 <= x <= X1 and Z0 <= z <= Z1:
                    cells.add((x, z))
        if rect:
            for x in range(rect[0], rect[2] + 1):
                for z in range(rect[1], rect[3] + 1):
                    cells.add((x, z))
        return cells

    def land(self, cells, height, top, sub, core, under, depth_k=1.1, max_depth=16, extra_under=None):
        """Remplit une île : height(x,z) = y du bloc de surface ; matériaux = fonctions (x,y,z,depth)."""
        dist = {}
        q = deque()
        for (x, z) in cells:
            if any((x + dx, z + dz) not in cells for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                dist[(x, z)] = 0
                q.append((x, z))
        while q:
            x, z = q.popleft()
            for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                n = (x + dx, z + dz)
                if n in cells and n not in dist:
                    dist[n] = dist[(x, z)] + 1
                    q.append(n)
        for (x, z) in cells:
            d = dist[(x, z)]
            depth = min(max_depth, 2 + int(d * depth_k + self.r.random() * 2.2))
            bottom = max(YMIN + 1, 63 - depth)
            H = height(x, z)
            self.land_cells[(x, z)] = max(H, self.land_cells.get((x, z), -1))
            for y in range(bottom, H + 1):
                k = H - y
                if k == 0:
                    blk = top(x, y, z, d)
                elif k <= 2:
                    blk = sub(x, y, z, d)
                elif y == bottom:
                    blk = under(x, y, z, d)
                else:
                    blk = core(x, y, z, d)
                self.set(x, y, z, blk)
            if extra_under and self.r.random() < extra_under[1]:
                # stalactites sous l'île
                n = 1 + self.r.randrange(3 + d // 2)
                for y in range(bottom - n, bottom):
                    self.set(x, y, z, extra_under[0](x, y, z, d))
        return dist

    def frame(self, team):
        """(u, v) local -> (x, z) monde ; u vers l'extérieur, v latéral."""
        cx, cz = TEAMS[team]['c']
        ox, oz = TEAMS[team]['out']
        lx, lz = -oz, ox

        def f(u, v):
            return cx + u * ox + v * lx, cz + u * oz + v * lz
        return f

    def facing(self, team, du, dv):
        ox, oz = TEAMS[team]['out']
        lx, lz = -oz, ox
        return FACE[(du * ox + dv * lx, du * oz + dv * lz)]

    # --- éléments communs
    def team_square(self, team, color, floor_choices, border=True):
        x1, z1, x2, z2 = SQUARES[team]
        for x in range(x1, x2 + 1):
            for z in range(z1, z2 + 1):
                self.set(x, 63, z, self.pick(floor_choices))
                for y in range(64, 71):
                    self.clear(x, y, z)
        if border:
            for x in range(x1, x2 + 1):
                for z in range(z1, z2 + 1):
                    if x in (x1, x2) or z in (z1, z2):
                        self.set(x, 63, z, f'{color}_concrete' if (x + z) % 2 == 0 else f'{color}_glazed_terracotta')
        gx, gz = GOLD[team]
        self.set(gx, 63, gz, 'gold_block')

    def bed_guard(self, team, blk, top_blk=None, floor='stone'):
        """Petit muret cassable autour du lit (côtés + arrière, l'avant reste ouvert)."""
        (fx, fz, _), (hx, hz, _) = BEDS[team]
        ox, oz = TEAMS[team]['out']
        bed = {(fx, fz), (hx, hz)}
        front = (fx - ox, fz - oz)
        ring = set()
        for bx, bz in bed:
            for dx in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    ring.add((bx + dx, bz + dz))
        ring -= bed
        # retire la rangée de devant (3 cases)
        ring = {c for c in ring if (c[0] - front[0]) * ox + (c[1] - front[1]) * oz > 0}
        prot = set(AIR_COLS)
        back = [c for c in ring if (c[0] - hx) * ox + (c[1] - hz) * oz > 0]
        for (x, z) in ring:
            if (x, z) in prot:
                continue
            if self.get(x, 63, z) is None:
                self.set(x, 63, z, floor)
            self.set(x, 64, z, blk)
        if top_blk:
            for (x, z) in back:
                if (x, z) not in prot:
                    self.set(x, 65, z, top_blk)

    def center_square(self, choices):
        x1, z1, x2, z2 = CENTER_SQ
        for x in range(x1, x2 + 1):
            for z in range(z1, z2 + 1):
                self.set(x, 63, z, self.pick(choices))
        self.set(*DIAMOND[:1], 63, DIAMOND[1], 'diamond_block')

    def finalize(self):
        """Garantit les ancrages (air au-dessus, perchoir vide)."""
        for (x, z) in AIR_COLS:
            for y in range(64, 67):
                self.clear(x, y, z)
        for (x, z) in BED_COLS:
            for y in range(64, 67):
                self.clear(x, y, z)
        x1, y1, z1, x2, y2, z2 = PERCH
        for k in list(self.b):
            if x1 <= k[0] <= x2 and y1 <= k[1] <= y2 and z1 <= k[2] <= z2:
                del self.b[k]
        # blocs « attachés » sans support : supprimés
        for _ in range(3):
            for (x, y, z), blk in list(self.b.items()):
                if not is_attached(blk):
                    continue
                if 'hanging=true' in blk or 'hanging_roots' in blk or ('chain' in blk and 'lantern' not in blk):
                    sup = self.get(x, y + 1, z)
                else:
                    sup = self.get(x, y - 1, z)
                if sup is None or (is_attached(sup) and 'chain' not in sup):
                    del self.b[(x, y, z)]

    # --- émission
    def emit(self, k, title):
        solids = {p: b for p, b in self.b.items() if not is_attached(b)}
        att = {p: b for p, b in self.b.items() if is_attached(b)}
        lines = [f'# Bedwars — carte {k} : {title}',
                 '# Généré par tools/bedwars/gen_maps.py — ne pas éditer à la main.',
                 'function mg:bedwars/map/wipe']
        lines += merge(solids)
        lines.append('# Détails (lanternes, végétation…)')
        for (x, y, z), b in sorted(att.items(), key=lambda t: (t[0][1] if 'hanging' not in t[1] else 999, t[0])):
            lines.append(f'setblock {x} {y} {z} {b}')
        lines.append('# Lits (identiques à la carte classique)')
        for t in ['red', 'blue', 'green', 'yellow']:
            lines += [l for _, _, l in BEDS[t]]
        lines.append('kill @e[type=minecraft:item,x=-45,y=40,z=1155,dx=90,dy=70,dz=90]')
        return lines


def is_attached(b):
    return any(a in b for a in ATTACHED)


def merge(blocks):
    """Fusion gloutonne des blocs identiques en pavés (fill ≤ 32768)."""
    out = []
    done = set()
    keys = sorted(blocks, key=lambda p: (p[1], p[2], p[0]))
    for p in keys:
        if p in done:
            continue
        b = blocks[p]
        x, y, z = p

        def ok(xx, yy, zz):
            q = (xx, yy, zz)
            return q not in done and blocks.get(q) == b
        x2 = x
        while ok(x2 + 1, y, z):
            x2 += 1
        z2 = z
        while all(ok(i, y, z2 + 1) for i in range(x, x2 + 1)):
            z2 += 1
        y2 = y
        while (x2 - x + 1) * (z2 - z + 1) * (y2 - y + 2) <= 32768 and \
                all(ok(i, y2 + 1, j) for i in range(x, x2 + 1) for j in range(z, z2 + 1)):
            y2 += 1
        for i in range(x, x2 + 1):
            for j in range(z, z2 + 1):
                for h in range(y, y2 + 1):
                    done.add((i, h, j))
        if (x, y, z) == (x2, y2, z2):
            out.append(f'setblock {x} {y} {z} {b}')
        else:
            out.append(f'fill {x} {y} {z} {x2} {y2} {z2} {b}')
    return out


# ---------------------------------------------------------------- vérifications hors jeu
def verify(m, name):
    errs = []
    for (x, y, z), b in m.b.items():
        if not (X0 <= x <= X1 and Z0 <= z <= Z1 and YMIN <= y <= YMAX):
            errs.append(f'hors zone {x} {y} {z}')
        base = b.split('[')[0]
        if base in FORBIDDEN_EXACT or any(f in b and not (f == 'sand' and 'sandstone' in b) for f in FORBIDDEN):
            errs.append(f'bloc interdit {b} en {x} {y} {z}')
    solid = lambda x, y, z: m.get(x, y, z) is not None and not is_attached(m.get(x, y, z))
    for t, r in SQUARES.items():
        for x in range(r[0], r[2] + 1):
            for z in range(r[1], r[3] + 1):
                if not solid(x, 63, z):
                    errs.append(f'sol manquant {t} {x} 63 {z}')
    for x in range(CENTER_SQ[0], CENTER_SQ[2] + 1):
        for z in range(CENTER_SQ[1], CENTER_SQ[3] + 1):
            if not solid(x, 63, z):
                errs.append(f'sol central manquant {x} 63 {z}')
    for (x, z) in AIR_COLS:
        if not solid(x, 63, z):
            errs.append(f'pas de sol en {x} 63 {z}')
        for y in range(64, 67):
            if m.get(x, y, z):
                errs.append(f'pas d\'air en {x} {y} {z}')
    for t, (x, z) in GOLD.items():
        if m.get(x, 63, z) != 'minecraft:gold_block':
            errs.append(f'bloc d\'or {t}')
    if m.get(0, 63, 1200) != 'minecraft:diamond_block':
        errs.append('diamant')
    for (x, z) in BED_COLS:
        if not solid(x, 63, z):
            errs.append(f'sol sous lit {x} {z}')
    # connexité à pied : cases de surface reliées si écart ≤ 2 (saut) et dénivelé ≤ 1 par case
    top = {}
    for (x, y, z), b in m.b.items():
        if not is_attached(b) and (top.get((x, z), -1) < y):
            top[(x, z)] = y
    comp = {}
    cid = 0
    for c in top:
        if c in comp:
            continue
        cid += 1
        comp[c] = cid
        q = deque([c])
        while q:
            x, z = q.popleft()
            for dx in range(-3, 4):
                for dz in range(-3, 4):
                    n = (x + dx, z + dz)
                    if n in top and n not in comp and abs(top[n] - top[(x, z)]) <= 6 and \
                            max(abs(dx), abs(dz)) <= 3:
                        comp[n] = cid
                        q.append(n)
    keys = {t: comp[SPAWN[t]] for t in SPAWN}
    keys['centre'] = comp[DIAMOND]
    seen = {}
    for k, v in keys.items():
        if v in seen:
            errs.append(f'{k} relié à pied à {seen[v]} (pas besoin de pont)')
        seen[v] = k
    if errs:
        raise SystemExit(f'[{name}] ' + '\n'.join(errs[:40]))


# ================================================================ CARTE 1 : CALDEIRA (volcan)
BONUS1 = [(-19, 1181), (19, 1181), (-19, 1219), (19, 1219)]


def map_volcan():
    m = Map(101)
    rock_top = [('blackstone', 5), ('smooth_basalt', 3), ('tuff', 2), ('cracked_polished_blackstone_bricks', 1),
                ('basalt[axis=y]', 1)]
    top = lambda x, y, z, d: m.pick(rock_top)
    sub = lambda x, y, z, d: m.pick([('blackstone', 4), ('basalt[axis=y]', 2), ('tuff', 1)])
    core = lambda x, y, z, d: m.pick([('blackstone', 6), ('basalt[axis=y]', 3), ('gilded_blackstone', 0.15),
                                      ('nether_wart_block', 0.3), ('shroomlight', 0.12)])
    under = lambda x, y, z, d: m.pick([('basalt[axis=y]', 3), ('blackstone', 2), ('shroomlight', 0.4)])
    drip = (lambda x, y, z, d: m.pick([('basalt[axis=y]', 5), ('polished_basalt[axis=y]', 2)]), 0.35)

    for i, (t, color) in enumerate(zip(['red', 'blue', 'green', 'yellow'], COLORS)):
        f = m.frame(t)
        cx, cz = f(2, 0)
        cells = m.blob(cx, cz, 8.6, 1.3, rect=(SQUARES[t][0] - 1, SQUARES[t][1] - 1, SQUARES[t][2] + 1, SQUARES[t][3] + 1))
        m.land(cells, lambda x, z: 63, top, sub, core, under, extra_under=drip)
        # coulées refroidies et cheminées lumineuses (hors carré)
        for (x, z) in cells:
            if in_rect(x, z, SQUARES[t]):
                continue
            r = m.r.random()
            if r < 0.06:
                m.set(x, 63, z, 'shroomlight')
            elif r < 0.16:
                m.set(x, 63, z, 'crimson_nylium')
                if m.r.random() < 0.5:
                    m.set(x, 64, z, m.pick([('crimson_roots', 3), ('crimson_fungus', 1), ('nether_sprouts', 0)]))
        m.team_square(t, color, [('polished_blackstone_bricks', 6), ('cracked_polished_blackstone_bricks', 2),
                                 ('polished_blackstone', 2)])
        m.bed_guard(t, 'nether_wart_block', top_blk='red_nether_brick_slab')
        # orgues de basalte à l'arrière
        for _ in range(9):
            u = 7 + m.r.randrange(4)
            v = m.r.randrange(-8, 9)
            x, z = f(u, v)
            if (x, z) in cells and not in_rect(x, z, SQUARES[t]):
                h = 2 + m.r.randrange(6)
                for y in range(64, 64 + h):
                    m.set(x, y, z, 'basalt[axis=y]')
                if m.r.random() < 0.4:
                    m.set(x, 64 + h, z, 'polished_basalt[axis=y]')
        # poteaux de lanternes d'âme aux coins côté centre
        for v in (-6, 6):
            x, z = f(-6, v)
            m.set(x, 63, z, 'polished_blackstone')
            m.box(x, 64, z, x, 66, z, 'nether_brick_fence')
            m.set(x, 67, z, 'soul_lantern')
        # petite arche de nether bricks derrière le lit
        for v in (-3, 3):
            x, z = f(7, v)
            m.box(x, 64, z, x, 67, z, 'nether_bricks')
        for v in range(-3, 4):
            x, z = f(7, v)
            m.set(x, 68, z, 'nether_brick_slab' if v in (-3, 3) else 'nether_bricks')
        x, z = f(7, 0)
        m.set(x, 67, z, 'soul_lantern[hanging=true]')

    # --- cratère central
    cells = m.blob(0, 1200, 12.2, 1.0, rect=(-5, 1195, 5, 1205))
    gate = lambda x, z: abs(x) <= 1 or abs(z - 1200) <= 1

    def hc(x, z):
        r = math.hypot(x, z - 1200)
        if r < 6.8 or gate(x, z):
            return 63
        return 63 + max(1, int(round(8.5 - abs(r - 9.3) * 2.0 + m.r.random() * 1.2)))
    cmap = {c: hc(*c) for c in cells}
    rim_top = lambda x, y, z, d: m.pick([('smooth_basalt', 3), ('basalt[axis=y]', 3), ('blackstone', 2),
                                        ('polished_basalt[axis=y]', 0.5)]) if y > 63 else m.pick(
        [('polished_blackstone', 4), ('cracked_polished_blackstone_bricks', 1)])
    m.land(cells, lambda x, z: cmap[(x, z)], rim_top, sub, core, under, depth_k=1.3, extra_under=drip)
    for (x, z), h in cmap.items():
        r = math.hypot(x, z - 1200)
        if h == 63 and 4.6 < r < 6.4 and (x + z) % 2 == 0 and not gate(x, z):
            m.set(x, 63, z, 'shroomlight')          # anneau « lave figée » lumineux
        if h == 63 and gate(x, z) and r >= 6:
            m.set(x, 63, z, 'polished_blackstone_bricks')
        if h >= 69 and m.r.random() < 0.08:
            m.set(x, h + 1, z, 'soul_lantern')
    m.center_square([('polished_blackstone', 5), ('chiseled_polished_blackstone', 1), ('gilded_blackstone', 0.4)])
    # piliers qui encadrent les 4 passages
    for (a, b) in ((7, 2), (7, -2), (-7, 2), (-7, -2)):
        for (x, z) in ((a, 1200 + b), (b, 1200 + a)):
            m.box(x, 63, z, x, 67, z, 'nether_bricks')
            m.set(x, 68, z, 'nether_brick_fence')
            m.set(x, 69, z, 'soul_lantern')

    # --- 4 îlots d'or bonus
    for (bx, bz) in BONUS1:
        cells = m.blob(bx, bz, 3.3, 0.6)
        m.land(cells, lambda x, z: 63, lambda x, y, z, d: m.pick([('polished_blackstone', 3), ('blackstone', 2)]),
               sub, core, under, depth_k=1.6, extra_under=drip)
        m.set(bx, 63, bz, 'raw_gold_block')
        for (dx, dz) in ((-2, -2), (2, 2), (-2, 2), (2, -2)):
            if (bx + dx, bz + dz) in cells:
                m.box(bx + dx, 64, bz + dz, bx + dx, 64 + (2 if (dx + dz) == 0 else 1), bz + dz, 'basalt[axis=y]')
        m.set(bx + 2, 63, bz, 'shroomlight')
        m.set(bx - 2, 63, bz, 'shroomlight')
        AIR_COLS.append((bx, bz))
    m.finalize()
    for (bx, bz) in BONUS1:
        AIR_COLS.remove((bx, bz))
    return m


# ================================================================ CARTE 2 : HANAMI (cerisiers)
def cherry_tree(m, x, y, z, h=5):
    """Cerisier : tronc + houppier aplati de cherry_leaves persistantes."""
    for k in range(h):
        m.set(x, y + k, z, 'cherry_log[axis=y]')
    top = y + h
    for dx in range(-3, 4):
        for dy in range(-1, 3):
            for dz in range(-3, 4):
                d = dx * dx / 9.0 + (dy - 0.5) ** 2 / 2.4 + dz * dz / 9.0
                if d <= 1.0 and m.r.random() > 0.12 and m.get(x + dx, top + dy, z + dz) is None:
                    m.set(x + dx, top + dy, z + dz, 'cherry_leaves[persistent=true]')
    m.set(x, top, z, 'cherry_log[axis=y]')


def toro(m, x, y, z):
    """Lanterne de pierre japonaise."""
    m.set(x, y, z, 'polished_andesite')
    m.set(x, y + 1, z, 'stone_brick_wall')
    m.set(x, y + 2, z, 'lantern')
    m.set(x, y + 3, z, 'stone_brick_slab')


def map_hanami():
    m = Map(202)
    grass = lambda x, y, z, d: m.pick([('grass_block', 10), ('moss_block', 1)])
    sub = lambda x, y, z, d: 'dirt'
    core = lambda x, y, z, d: m.pick([('stone', 6), ('andesite', 2), ('dirt', 2), ('mossy_cobblestone', 1)])
    under = lambda x, y, z, d: m.pick([('rooted_dirt', 3), ('moss_block', 2)])
    roots = (lambda x, y, z, d: m.pick([('rooted_dirt', 3), ('moss_block', 1)]), 0.25)

    for t, color in zip(['red', 'blue', 'green', 'yellow'], COLORS):
        f = m.frame(t)
        cx, cz = f(1, 0)
        cells = m.blob(cx, cz, 8.5, 1.0, rect=(SQUARES[t][0] - 1, SQUARES[t][1] - 1, SQUARES[t][2] + 1, SQUARES[t][3] + 1))
        # terrasses latérales (|v| ≥ 9, y 66) avec escaliers 3 de large
        for u in range(-3, 9):
            for v in list(range(6, 13)) + list(range(-12, -5)):
                c = f(u, v)
                if X0 <= c[0] <= X1 and Z0 <= c[1] <= Z1:
                    cells.add(c)
        hmap = {}
        steps = {}
        for u in range(-3, 9):
            for s in (1, -1):
                for k, v in enumerate(range(6, 13)):
                    c = f(u, s * v)
                    if v >= 9:
                        hmap[c] = 66
                    elif -1 <= u <= 1:
                        hmap[c] = 64 + k
                        steps[c] = (64 + k, m.facing(t, 0, s))
        cmap = {c: hmap.get(c, 63) for c in cells}

        def wall_top(x, y, z, d, cmap=cmap):
            return 'grass_block' if y == cmap[(x, z)] else 'dirt'
        m.land(cells, lambda x, z: cmap[(x, z)], grass, sub, core, under, extra_under=roots)
        # murs de soutènement en pierre moussue autour des terrasses
        for c, h in cmap.items():
            if h == 66:
                for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    n = (c[0] + dx, c[1] + dz)
                    if cmap.get(n, 0) < 66 and n not in steps:
                        for y in range(63, 66):
                            m.set(c[0], y, c[1], m.pick([('stone_bricks', 3), ('mossy_stone_bricks', 3),
                                                         ('cracked_stone_bricks', 1)]))
                        break
        for c, (h, fc) in steps.items():
            m.set(c[0], h, c[1], f'stone_brick_stairs[facing={fc}]')
        m.team_square(t, color, [('grass_block', 6), ('moss_block', 1)], border=False)
        # allée de pierre + bordure en terracotta de l'équipe
        x1, z1, x2, z2 = SQUARES[t]
        for x in range(x1, x2 + 1):
            for z in range(z1, z2 + 1):
                if x in (x1, x2) or z in (z1, z2):
                    m.set(x, 63, z, f'{color}_terracotta')
        for u in range(-5, 6):
            x, z = f(u, 0)
            if m.get(x, 63, z) != 'minecraft:gold_block':
                m.set(x, 63, z, m.pick([('stone_bricks', 3), ('mossy_stone_bricks', 1)]))
        m.bed_guard(t, 'flowering_azalea_leaves[persistent=true]', floor='moss_block')
        # cerisiers + pétales, lanternes de pierre, torii sur une terrasse
        for s in (1, -1):
            x, z = f(4, s * 10)
            cherry_tree(m, x, 67, z, 4 + m.r.randrange(2))
            x, z = f(-2, s * 7)
            cherry_tree(m, x, 64, z, 4)
        x, z = f(1, -10)
        for dv in (-2, 2):
            px, pz = f(1, -10 + dv)
            m.box(px, 67, pz, px, 70, pz, 'stripped_mangrove_log[axis=y]')
        for dv in range(-3, 4):
            px, pz = f(1, -10 + dv)
            m.set(px, 71, pz, 'dark_oak_planks' if abs(dv) < 3 else 'dark_oak_slab')
            if abs(dv) < 2:
                m.set(px, 69, pz, 'mangrove_planks')
        for v in (-5, 5):
            x, z = f(-6, v)
            toro(m, x, 64, z)
        # pont de bois inachevé vers le centre (u -6 .. -13)
        for u in range(-6, -14, -1):
            broken = u <= -12
            for v in (-1, 0, 1):
                if broken and m.r.random() < 0.45:
                    continue
                x, z = f(u, v)
                m.set(x, 63, z, 'cherry_planks' if not (broken and v != 0) else 'cherry_slab[type=top]')
            for v in (-2, 2):
                x, z = f(u, v)
                if u > -11:
                    m.set(x, 63, z, 'stripped_cherry_log[axis=y]')
                    m.set(x, 64, z, 'cherry_fence')
                    if u in (-7, -10):
                        m.set(x, 65, z, 'lantern')
        # pétales roses au sol
        for (x, z), h in cmap.items():
            if m.get(x, h, z) == 'minecraft:grass_block' and m.get(x, h + 1, z) is None \
                    and m.r.random() < 0.3 and not in_rect(x, z, SQUARES[t]):
                m.set(x, h + 1, z, m.pick([(f'pink_petals[flower_amount={m.r.randrange(1, 5)},facing=north]', 4),
                                           ('short_grass', 1), ('allium', 0.2), ('lily_of_the_valley', 0.2)]))

    # --- île centrale + pagode
    cells = m.blob(0, 1200, 10.0, 0.9, rect=(-5, 1195, 5, 1205))
    m.land(cells, lambda x, z: 63, grass, sub, core, under, depth_k=1.3, extra_under=roots)
    for (x, z) in cells:
        if max(abs(x), abs(z - 1200)) <= 6:
            m.set(x, 63, z, m.pick([('stone_bricks', 4), ('polished_andesite', 2), ('mossy_stone_bricks', 1)]))
    m.center_square([('polished_andesite', 4), ('stone_bricks', 2), ('chiseled_stone_bricks', 0.5)])
    # amorces de pont du centre (r 9..11)
    for a in range(9, 12):
        for w in (-1, 0, 1):
            for (x, z) in ((a, 1200 + w), (-a, 1200 + w), (w, 1200 + a), (w, 1200 - a)):
                if a < 11 or w == 0:
                    m.set(x, 63, z, 'cherry_planks')
    # pagode : 3 niveaux, toits en tuiles d'ardoise
    def roof(y, r):
        for x in range(-r, r + 1):
            for z in range(-r, r + 1):
                e = max(abs(x), abs(z))
                if e == r:
                    if abs(x) == r and abs(z) == r:
                        m.set(x, y, 1200 + z, 'deepslate_tile_slab')
                    else:
                        fc = FACE[(0 if abs(x) != r else -int(math.copysign(1, x)),
                                   0 if abs(x) == r else -int(math.copysign(1, z)))]
                        m.set(x, y, 1200 + z, f'deepslate_tile_stairs[facing={fc}]')
                elif e == r - 1:
                    m.set(x, y, 1200 + z, 'deepslate_tiles')
                else:
                    m.set(x, y, 1200 + z, 'cherry_planks')
    for (px, pz) in ((-4, -4), (4, -4), (-4, 4), (4, 4)):
        m.box(px, 64, 1200 + pz, px, 67, 1200 + pz, 'stripped_cherry_log[axis=y]')
    roof(68, 6)
    for (px, pz) in ((-3, -3), (3, -3), (-3, 3), (3, 3)):
        m.box(px, 69, 1200 + pz, px, 71, 1200 + pz, 'stripped_cherry_log[axis=y]')
        m.set(px, 67, 1200 + pz + (1 if pz < 0 else -1), 'lantern[hanging=true]')
    for (px, pz) in ((-5, -5), (5, -5), (-5, 5), (5, 5)):
        m.set(px, 67, 1200 + pz, 'lantern[hanging=true]')
    roof(72, 4)
    for (px, pz) in ((-2, -2), (2, -2), (-2, 2), (2, 2)):
        m.box(px, 73, 1200 + pz, px, 74, 1200 + pz, 'stripped_cherry_log[axis=y]')
    roof(75, 3)
    m.box(0, 76, 1200, 0, 77, 1200, 'cherry_fence')
    m.set(0, 78, 1200, 'gold_block')
    m.set(0, 79, 1200, 'end_rod[facing=up]')
    for (px, pz) in ((-3, -3), (3, -3), (-3, 3), (3, 3)):
        m.set(px, 71, 1200 + pz + (1 if pz < 0 else -1), 'lantern[hanging=true]')
    # lanternes de pierre et cerisiers du centre
    for (x, z) in ((-8, 1192), (8, 1192), (-8, 1208), (8, 1208)):
        if (x, z) in cells:
            toro(m, x, 64, z)
    for (x, z) in ((-7, 1203), (7, 1197), (-3, 1193), (3, 1207)):
        if (x, z) in cells:
            m.set(x, 64, z, 'flowering_azalea')
    for (x, z) in cells:
        if m.get(x, 63, z) == 'minecraft:grass_block' and m.get(x, 64, z) is None and m.r.random() < 0.4:
            m.set(x, 64, z, f'pink_petals[flower_amount={m.r.randrange(1, 5)},facing=east]')
    m.finalize()
    return m


# ================================================================ CARTE 3 : BANQUISE (glacier)
def spike(m, x, z, y0, h, r0, blk='packed_ice'):
    for k in range(h):
        r = r0 * (1 - k / h) + 0.3
        for dx in range(-int(r) - 1, int(r) + 2):
            for dz in range(-int(r) - 1, int(r) + 2):
                if dx * dx + dz * dz <= r * r:
                    m.set(x + dx, y0 + k, z + dz, blk if m.r.random() > 0.12 else 'blue_ice')


def igloo(m, cx, y0, cz, door):
    """Dôme de neige r=3, porte vers `door` (dx, dz)."""
    for dx in range(-3, 4):
        for dy in range(0, 4):
            for dz in range(-3, 4):
                d = math.sqrt(dx * dx + dy * dy * 1.2 + dz * dz)
                p = (cx + dx, y0 + dy, cz + dz)
                if d <= 3.4:
                    if d >= 2.4:
                        m.set(*p, 'snow_block')
                    else:
                        m.clear(*p)
    for k in (2, 3):
        x, z = cx + door[0] * k, cz + door[1] * k
        m.clear(x, y0, z)
        m.clear(x, y0 + 1, z)
    m.set(cx + door[0] * 3 - door[1], y0, cz + door[1] * 3 + door[0], 'snow_block')
    m.set(cx + door[0] * 3 + door[1], y0, cz + door[1] * 3 - door[0], 'snow_block')
    m.set(cx + door[0] * 3 - door[1], y0 + 1, cz + door[1] * 3 + door[0], 'snow_block')
    m.set(cx + door[0] * 3 + door[1], y0 + 1, cz + door[1] * 3 - door[0], 'snow_block')
    m.set(cx + door[0] * 4 - door[1], y0, cz + door[1] * 4 + door[0], 'snow_block')
    m.set(cx + door[0] * 4 + door[1], y0, cz + door[1] * 4 - door[0], 'snow_block')
    for dx in (-1, 0, 1):
        for dz in (-1, 0, 1):
            m.set(cx + dx, y0, cz + dz, 'light_blue_carpet' if (dx + dz) % 2 else 'white_carpet')
    m.set(cx, y0 + 2, cz, 'lantern[hanging=true]')
    m.set(cx - door[0] * 2, y0, cz - door[1] * 2, 'blue_ice')
    m.set(cx - door[0] * 2, y0 + 1, cz - door[1] * 2, 'lantern')


def map_banquise():
    m = Map(303)
    snow_top = lambda x, y, z, d: m.pick([('snow_block', 8), ('packed_ice', 1.2)])
    sub = lambda x, y, z, d: m.pick([('snow_block', 3), ('packed_ice', 2)])
    core = lambda x, y, z, d: m.pick([('packed_ice', 5), ('blue_ice', 1), ('calcite', 1), ('diorite', 1)])
    under = lambda x, y, z, d: m.pick([('packed_ice', 3), ('blue_ice', 2)])
    icicle = (lambda x, y, z, d: m.pick([('packed_ice', 3), ('blue_ice', 1)]), 0.4)

    for t, color in zip(['red', 'blue', 'green', 'yellow'], COLORS):
        f = m.frame(t)
        cx, cz = f(3, 0)
        cells = m.blob(cx, cz, 10.0, 1.1, rect=(SQUARES[t][0] - 1, SQUARES[t][1] - 1, SQUARES[t][2] + 1, SQUARES[t][3] + 1))
        hx, hz = f(2, 9)         # colline de neige sur un flanc

        def hh(x, z, hx=hx, hz=hz, t=t):
            if in_rect(x, z, (SQUARES[t][0] - 1, SQUARES[t][1] - 1, SQUARES[t][2] + 1, SQUARES[t][3] + 1)):
                return 63
            return 63 + max(0, int(5 - math.hypot(x - hx, z - hz) * 1.1))
        cmap = {c: hh(*c) for c in cells}
        m.land(cells, lambda x, z: cmap[(x, z)], snow_top, sub, core, under, extra_under=icicle)
        m.team_square(t, color, [('snow_block', 6), ('polished_diorite', 1)])
        m.bed_guard(t, 'snow_block', top_blk='snow_block', floor='snow_block')
        # igloo dans un coin arrière, porte vers l'intérieur de l'île
        ix, iz = f(9, -6)
        dvx, dvz = f(9, -5)
        igloo(m, ix, 64, iz, (dvx - ix, dvz - iz))
        # pics de glace dans l'autre coin arrière + sur la colline
        for (u, v, h, r) in ((9, 6, 9, 1.6), (11, 3, 6, 1.1), (7, 8, 5, 1.0)):
            x, z = f(u, v)
            if (x, z) in cells:
                spike(m, x, z, cmap[(x, z)] + 1, h, r)
        x, z = f(2, 9)
        if (x, z) in cells:
            spike(m, x, z, cmap[(x, z)] + 1, 7, 1.3)
        # lampadaires en sapin
        for v in (-6, 6):
            x, z = f(-6, v)
            if (x, z) in cells:
                m.box(x, 64, z, x, 66, z, 'spruce_fence')
                m.set(x, 67, z, 'lantern')
        x, z = f(6, 3)
        m.box(x, 64, z, x, 65, z, 'spruce_fence')
        m.set(x, 66, z, 'lantern')

    # --- centre : glacier avec anneau de glace bleue et grands pics
    cells = m.blob(0, 1200, 9.5, 1.0, rect=(-5, 1195, 5, 1205))
    m.land(cells, lambda x, z: 63, snow_top, sub, core, under, depth_k=1.4, extra_under=icicle)
    for (x, z) in cells:
        r = math.hypot(x, z - 1200)
        if 5.5 <= r < 6.6:
            m.set(x, 63, z, 'blue_ice')
    m.center_square([('packed_ice', 3), ('snow_block', 2), ('polished_diorite', 1)])
    for (x, z, h) in ((-7, 1193, 16), (7, 1207, 14), (7, 1193, 11), (-7, 1207, 12)):
        spike(m, x, z, 64, h, 2.0)
    for (x, z) in ((-8, 1200), (8, 1200), (0, 1192), (0, 1208)):
        if (x, z) in cells:
            m.box(x, 64, z, x, 65, z, 'spruce_fence')
            m.set(x, 66, z, 'lantern')

    # --- banquise fragmentée : plaques de glace flottantes
    floes = [(-18, 1200, 1.6), (18, 1200, 1.6), (0, 1182, 1.6), (0, 1218, 1.6),     # axes
             (-17, 1183, 2.4), (17, 1183, 2.4), (-17, 1217, 2.4), (17, 1217, 2.4)]  # diagonales
    for (fx, fz, r) in floes:
        c = m.blob(fx, fz, r, 0.4)
        m.land(c, lambda x, z: 63, lambda x, y, z, d: m.pick([('snow_block', 2), ('packed_ice', 2)]),
               sub, core, under, depth_k=1.0, max_depth=5, extra_under=icicle)
        if r > 2:
            spike(m, fx, fz, 64, 4 + m.r.randrange(3), 0.9)
    for (fx, fz, y) in ((-24, 1180, 58), (24, 1222, 57), (-26, 1222, 59), (25, 1178, 56), (-12, 1186, 55),
                        (12, 1214, 56)):
        c = m.blob(fx, fz, 1.4, 0.3)
        for (x, z) in c:
            m.set(x, y, z, 'packed_ice')
            m.set(x, y - 1, z, 'blue_ice')
    m.finalize()
    return m


# ---------------------------------------------------------------- écriture
MAPS = [
    (1, 'Caldeira', map_volcan, 'gold',
     "Volcan : îles de basalte et de blackstone autour d'un cratère où dorment les diamants, avec 4 îlots d'or bonus"),
    (2, 'Hanami', map_hanami, 'light_purple',
     "Jardin des cerisiers : terrasses surélevées, pagode centrale et ponts de bois inachevés"),
    (3, 'Banquise', map_banquise, 'aqua',
     "Glacier : igloos, pics de glace et banquise fragmentée — gare à la glace bleue qui glisse"),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    wipe = ['# Bedwars — efface toute la zone des cartes (x -45..45, z 1155..1245, y 40..110)',
            '# Généré par tools/bedwars/gen_maps.py. « strict » : pas de mise à jour des voisins, rien ne tombe.']
    y = 40
    while y <= 110:
        y2 = min(110, y + 2)
        wipe.append(f'fill -45 {y} 1155 45 {y2} 1245 minecraft:air strict')
        y = y2 + 1
    wipe.append('kill @e[type=minecraft:item,x=-45,y=40,z=1155,dx=90,dy=70,dz=90]')
    W('wipe', wipe)
    for k, name, fn, col, desc in MAPS:
        m = fn()
        verify(m, name)
        lines = m.emit(k, name)
        W(f'build_{k}', lines)
        W(f'info_{k}', [f'# Bedwars — présentation de la carte {k}',
                        f'tellraw @a [{{"text":"Carte : ","color":"gray"}},{{"text":"{name}","color":"{col}","bold":true}},'
                        f'{{"text":" ({desc})","color":"gray"}}]'])
        print(f'build_{k} ({name}) : {len(m.b)} blocs, {len(lines)} lignes')
    W('gen_1', ['# Bedwars — Caldeira : générateurs d\'or bonus des 4 îlots (appelé à chaque cycle d\'or, 8 s)'] +
      [f'summon minecraft:item {x + 0.5} 64.5 {z + 0.5} {{Item:{{id:"minecraft:gold_ingot",count:1}},PickupDelay:10s}}'
       for x, z in BONUS1] +
      [f'particle minecraft:wax_on {x + 0.5} 64.8 {z + 0.5} 0.3 0.3 0.3 0 6' for x, z in BONUS1])


if __name__ == '__main__':
    main()
