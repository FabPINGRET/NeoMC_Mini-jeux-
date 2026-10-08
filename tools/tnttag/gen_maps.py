"""TNT Tag — 3 cartes à relief : python3 tools/tnttag/gen_maps.py (depuis la racine du dépôt)

Carte 1 « Collines »       centre (0, 26500) : prairie vallonnée, rivière peu profonde, ponts, moulin, kiosque.
Carte 2 « Canyon »         centre (0, 26800) : mesa en terracotta, plateaux, rampes, arche, tunnel, pont suspendu.
Carte 3 « Village perché » centre (0, 27400) : place en contrebas, terrasses, maisons à toits accessibles, passerelles.

Chaque carte est un nuage de voxels (x et z relatifs au centre, y absolu) dans l'emprise 51 x 51
(intérieur -24..24, anneau de barrières à ±25). Les blocs sont regroupés en pavés (`fill` <= 32768 blocs),
posés par phases (blocs pleins, puis escaliers/barrières, puis décor, puis eau) et par y croissant
(le sable ne tombe pas). Tout est déterministe (graines fixes).

Vérification intégrée (le script échoue sinon) : simulation de marche (pas de 1 bloc, saut <= 1,25,
hauteur libre 1,8, chutes) : toute position atteignable doit pouvoir revenir au point de départ,
les points de départ doivent être au sol et atteignables ; sol entre y 80 et 96, eau d'un bloc au plus.

Sorties : data/mg/function/tnttag/map/{build_k,setup_k,info_k}.mcfunction (k = 1..3), sp.mcfunction, fl.mcfunction
"""
import math, os, random, sys
from collections import deque

OUT = os.path.join('data', 'mg', 'function', 'tnttag', 'map')
IN = 24                       # demi-intérieur (jouable : -24..24)
RING = 25                     # anneau de barrières
Y0, YCLR = 76, 120            # nettoyage de y 76 à y 120
IR = range(-IN, IN + 1)

PASS = {'air', 'water', 'short_grass', 'tall_grass', 'fern', 'dead_bush', 'poppy', 'dandelion', 'cornflower',
        'oxeye_daisy', 'azure_bluet', 'allium', 'blue_orchid', 'lily_of_the_valley', 'short_dry_grass',
        'tall_dry_grass', 'pink_petals', 'wildflowers', 'leaf_litter', 'light', 'torch', 'red_tulip',
        'orange_tulip', 'white_tulip', 'pink_tulip', 'firefly_bush', 'bush'}
DECOR = PASS | {'lantern', 'flower_pot', 'potted_red_tulip', 'potted_cornflower', 'potted_poppy', 'bell'}


def base(b):
    return b.split('[')[0]


def phase(b):
    n = base(b)
    if n == 'water':
        return 3
    if n in DECOR:
        return 2
    if n.endswith(('_stairs', '_slab', '_fence', '_wall', '_pane', '_fence_gate', '_trapdoor')) or n == 'iron_chain':
        return 1
    return 0


def occ(b):
    """occupation verticale (bas, haut, on peut se tenir dessus) d'un bloc, ou None s'il est traversable"""
    n = base(b)
    if n in PASS:
        return None
    if n.endswith('_slab'):
        if 'type=top' in b:
            return (0.5, 1.0, True)
        if 'type=double' in b:
            return (0.0, 1.0, True)
        return (0.0, 0.5, True)
    if n.endswith(('_fence', '_wall', '_fence_gate')):
        return (0.0, 1.5, True)
    if n in ('lantern', 'iron_chain', 'bell', 'flower_pot') or n.startswith('potted_'):
        return (0.0, 1.0, False)
    if n == 'dirt_path':
        return (0.0, 0.9375, True)
    return (0.0, 1.0, True)


def hsh(*a):
    """hachage déterministe -> [0, 1["""
    v = 2166136261
    for x in a:
        v = ((v ^ (int(x) & 0xffffffff)) * 16777619) & 0xffffffff
    v ^= v >> 13
    v = (v * 1274126177) & 0xffffffff
    return (v >> 8) / float(1 << 24)


class Carte:
    def __init__(self, k, nom, cz, couleur, desc):
        self.k, self.nom, self.cz, self.couleur, self.desc = k, nom, cz, couleur, desc
        self.v = {}
        self.H = {}               # (x, z) -> y du bloc de surface du terrain
        self.spawns = []          # (x, y des pieds, z)
        self.home = None          # point de réapparition (x, y, z)
        self.filler = 'stone'     # bloc de remplissage des parties invisibles

    # --- écriture des voxels ---
    def set(self, x, y, z, b):
        if abs(x) > IN or abs(z) > IN:
            return
        assert Y0 <= y < YCLR, (x, y, z, b)
        if b == 'air':
            self.v.pop((x, y, z), None)
        else:
            self.v[(x, y, z)] = b

    def get(self, x, y, z):
        return self.v.get((x, y, z), 'air')

    def box(self, x1, y1, z1, x2, y2, z2, b):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                for z in range(min(z1, z2), max(z1, z2) + 1):
                    self.set(x, y, z, b)

    def top(self, x, z):
        """y du plus haut bloc non traversable de la colonne"""
        for y in range(YCLR - 1, Y0 - 1, -1):
            b = self.v.get((x, y, z))
            if b and occ(b):
                return y
        return Y0 - 1

    # --- terrain : colonne pleine de y 76 à H ---
    def terrain(self, mat):
        """mat(x, y, z, h) -> bloc pour chaque y de 76 à h"""
        for (x, z), h in self.H.items():
            assert 80 <= h <= 96, ('sol hors limites', x, z, h)
            for y in range(Y0, h + 1):
                self.set(x, y, z, mat(x, y, z, h))

    # --- éléments génériques ---
    def lamp_post(self, x, z, wood='spruce_fence', hgt=2):
        h = self.top(x, z)
        for i in range(1, hgt + 1):
            self.set(x, h + i, z, f'{wood}')
        self.set(x, h + hgt + 1, z, 'lantern')

    def roof(self, cx, cz, y, s, stair, fill_b, hx=None):
        """toit pyramidal : demi-côté s au niveau y, puis s-1 au-dessus..."""
        i = 0
        while s - i >= 0:
            r = s - i
            yy = y + i
            for dx in range(-r, r + 1):
                for dz in range(-r, r + 1):
                    if r == 0:
                        self.set(cx, yy, cz, fill_b)
                    elif dz == -r:
                        self.set(cx + dx, yy, cz + dz, f'{stair}[facing=south]')
                    elif dz == r:
                        self.set(cx + dx, yy, cz + dz, f'{stair}[facing=north]')
                    elif dx == -r:
                        self.set(cx + dx, yy, cz + dz, f'{stair}[facing=east]')
                    elif dx == r:
                        self.set(cx + dx, yy, cz + dz, f'{stair}[facing=west]')
                    else:
                        self.set(cx + dx, yy, cz + dz, fill_b)
            i += 1
        return y + s

    # --- sortie ---
    def cache_invisible(self):
        """les blocs pleins entièrement entourés de blocs pleins (invisibles) deviennent du remplissage uniforme,
        ce qui réduit fortement le nombre de commandes"""
        def opaque(b):
            n = base(b)
            return phase(b) == 0 and not n.endswith(('_leaves', 'glass')) and n not in ('glowstone', 'water', 'barrel', 'dirt_path', 'barrier')
        v = dict(self.v)
        for (x, y, z), b in self.v.items():
            if not opaque(b) or base(b) == self.filler:
                continue
            hidden = True
            for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                q = (x + dx, y + dy, z + dz)
                if q[1] < Y0:
                    continue
                if abs(q[0]) > IN or abs(q[2]) > IN or q not in self.v or not opaque(self.v[q]):
                    hidden = False
                    break
            if hidden:
                v[(x, y, z)] = self.filler
        return v

    def ymax(self):
        return max(y for (x, y, z) in self.v)

    def commands(self):
        cz = self.cz
        top = self.ymax()
        btop = top + 12
        assert btop < YCLR, ('trop haut', top)
        cmds = [f'# TNT Tag — carte {self.k} « {self.nom.capitalize()} » (centre 0 ~ {cz}), générée par tools/tnttag/gen_maps.py',
                '# Nettoyage de l\'emprise (sans mise à jour de blocs : rien ne tombe)']
        y = Y0
        while y <= YCLR:
            y2 = min(YCLR, y + 11)
            cmds.append(f'fill -{RING} {y} {cz - RING} {RING} {y2} {cz + RING} minecraft:air strict')
            y = y2 + 1
        boxes = []
        groups = {}
        for p, b in self.cache_invisible().items():
            groups.setdefault(b, set()).add(p)
        for b, cells in groups.items():
            for bx in merge(cells):
                boxes.append((phase(b), bx[1], b, bx))
        boxes.sort(key=lambda t: (t[0], t[1], t[2], t[3]))
        cmds.append('# Construction (terrain, puis escaliers et barrières, puis décor, puis eau)')
        for ph, _, b, (x1, y1, z1, x2, y2, z2) in boxes:
            if (x1, y1, z1) == (x2, y2, z2):
                cmds.append(f'setblock {x1} {y1} {z1 + cz} minecraft:{b}')
            else:
                cmds.append(f'fill {x1} {y1} {z1 + cz} {x2} {y2} {z2 + cz} minecraft:{b}')
        cmds.append(f'# Murs invisibles jusqu\'à y {btop}')
        cmds.append(f'fill -{RING} {Y0} {cz - RING} {RING} {btop} {cz - RING} minecraft:barrier')
        cmds.append(f'fill -{RING} {Y0} {cz + RING} {RING} {btop} {cz + RING} minecraft:barrier')
        cmds.append(f'fill -{RING} {Y0} {cz - IN} -{RING} {btop} {cz + IN} minecraft:barrier')
        cmds.append(f'fill {RING} {Y0} {cz - IN} {RING} {btop} {cz + IN} minecraft:barrier')
        return cmds, btop


def merge(cells):
    """regroupe un ensemble de positions identiques en pavés (x, puis z, puis y), <= 32768 blocs"""
    left = set(cells)
    out = []
    for p in sorted(cells, key=lambda q: (q[1], q[2], q[0])):
        if p not in left:
            continue
        x, y, z = p
        x2 = x
        while (x2 + 1, y, z) in left:
            x2 += 1
        z2 = z
        while all((i, y, z2 + 1) in left for i in range(x, x2 + 1)):
            z2 += 1
        y2 = y
        area = (x2 - x + 1) * (z2 - z + 1)
        while area * (y2 - y + 2) <= 32768 and all((i, y2 + 1, j) in left for i in range(x, x2 + 1) for j in range(z, z2 + 1)):
            y2 += 1
        for i in range(x, x2 + 1):
            for j in range(z, z2 + 1):
                for yy in range(y, y2 + 1):
                    left.discard((i, yy, j))
        out.append((x, y, z, x2, y2, z2))
    return out


# =====================================================================================
# Vérification : simulation de déplacement à pied
# =====================================================================================
JUMP, BODY = 1.25, 1.8


def verifier(c):
    cols = {}
    for (x, y, z), b in c.v.items():
        o = occ(b)
        if o:
            cols.setdefault((x, z), []).append((y + o[0], y + o[1], o[2]))
    for x in range(-RING, RING + 1):              # anneau de barrières
        for z in range(-RING, RING + 1):
            if max(abs(x), abs(z)) == RING:
                cols[(x, z)] = [(Y0, c.ymax() + 13, True)]

    def free(col, a, b):
        for lo, hi, _ in cols.get(col, ()):
            if lo < b - 1e-6 and hi > a + 1e-6:
                return False
        return True

    spots = {}
    for col, lst in cols.items():
        s = []
        for lo, hi, st in lst:
            if st and free(col, hi, hi + BODY):
                s.append(hi)
        spots[col] = s
    allspots = [(col, t) for col, s in spots.items() for t in s]

    def nbrs(node):
        (x, z), t = node
        for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n = (x + dx, z + dz)
            for t2 in spots.get(n, ()):
                if t2 - t > JUMP + 1e-6:
                    continue
                hh = max(t, t2) + BODY
                if free((x, z), t, hh) and free(n, t2, hh):
                    yield (n, t2)

    fwd_adj = {}
    rev_adj = {}
    for node in allspots:
        for m in nbrs(node):
            fwd_adj.setdefault(node, []).append(m)
            rev_adj.setdefault(m, []).append(node)

    def bfs(start, adj):
        seen = {start}
        dq = deque([start])
        while dq:
            u = dq.popleft()
            for w in adj.get(u, ()):
                if w not in seen:
                    seen.add(w)
                    dq.append(w)
        return seen

    def spot_at(x, y, z):
        for t in spots.get((x, z), ()):
            if abs(t - y) < 0.1:
                return ((x, z), t)
        return None
    start = spot_at(*c.home)
    assert start, ('départ invalide', c.home)
    fwd = bfs(start, fwd_adj)
    rev = bfs(start, rev_adj)
    pieges = [n for n in fwd if n not in rev]
    inter = [n for n in allspots if max(abs(n[0][0]), abs(n[0][1])) <= IN]
    sans_retour = [n for n in inter if n not in rev]
    err = []
    if pieges:
        err.append(f'{len(pieges)} positions atteignables sans retour : {sorted(pieges)[:12]}')
    if sans_retour:
        err.append(f'{len(sans_retour)} positions (même inaccessibles) sans retour : {sorted(sans_retour)[:12]}')
    for (x, y, z) in c.spawns + [c.home]:
        n = spot_at(x, y, z)
        if n is None or n not in fwd or n not in rev:
            err.append(f'départ {(x, y, z)} non atteignable')
        if not free((x, z), y, YCLR + 20):
            err.append(f'départ {(x, y, z)} pas à ciel ouvert')
    # eau : jamais plus d'un bloc de profondeur
    for (x, y, z), b in c.v.items():
        if b == 'water' and c.get(x, y - 1, z) == 'water':
            err.append(f'eau profonde en {(x, y, z)}')
            break
    # rien qui fasse mal
    for b in set(c.v.values()):
        assert base(b) not in ('magma_block', 'cactus', 'lava', 'fire', 'campfire', 'soul_campfire', 'sweet_berry_bush',
                               'wither_rose', 'pointed_dripstone', 'powder_snow'), b
    reach = [t for (_, t) in fwd]
    ground = min(c.H.values())
    stats = dict(spots=len(allspots), atteignables=len(fwd), tmin=min(reach), tmax=max(reach),
                 sol_min=ground, sol_max=max(c.H.values()))
    return err, stats, fwd


# =====================================================================================
# Carte 1 — Collines
# =====================================================================================
def carte1():
    c = Carte(1, 'COLLINES', 26500, 'green', 'prairie vallonnée, rivière, ponts, moulin et kiosque')
    W = 82                                            # niveau de l'eau (bloc d'eau)

    def zr(x):
        return 2 + 4.5 * math.sin(x / 7.0 + 0.6)       # axe de la rivière (ouest -> est)
    hills = [(-14, -14, 8.5, 6.5), (14, -13, 5.5, 5.5), (15, 15, 6.5, 6.0), (-15, 15, 4.5, 5.5),
             (-1, 18, 3.0, 4.0), (3, -21, 3.0, 4.0), (22, 0, 2.5, 3.5), (-22, 1, 2.5, 3.5)]
    river = set()
    H = {}
    for x in IR:
        for z in IR:
            h = 84 + 0.7 * math.sin(x / 5.3 + 1) * math.cos(z / 6.1)
            for hx, hz, a, s in hills:
                h += a * math.exp(-((x - hx) ** 2 + (z - hz) ** 2) / (2 * s * s))
            d = abs(z - zr(x))
            if d <= 1.5:
                river.add((x, z))
                H[(x, z)] = W - 1
            else:
                H[(x, z)] = max(W, min(int(round(h)), W + int(d - 1.0)))
    pads = {'kiosque': (0, -9, 5), 'moulin': (-14, -14, 4)}

    def pad_cells(px, pz, r):
        return [(x, z) for x in range(px - r, px + r + 1) for z in range(pz - r, pz + r + 1) if (x, z) in H]
    for _ in range(50):
        changed = False
        for px, pz, r in pads.values():
            cells = pad_cells(px, pz, r)
            m = min(H[q] for q in cells)
            for q in cells:
                if H[q] != m:
                    H[q] = m
                    changed = True
        for (x, z) in H:
            if (x, z) in river:
                continue
            m = min([H[(x + dx, z + dz)] + 1 for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (x + dx, z + dz) in H])
            if H[(x, z)] > m:
                H[(x, z)] = m
                changed = True
        if not changed:
            break
    c.H = H

    # chemins (polylignes)
    paths = [[(-14, -10), (-11, -7), (-9, -4), (-9, 2), (-11, 9), (-15, 14)],
             [(-9, -5), (-5, -8), (0, -9), (5, -7), (9, -3), (11, 2), (12, 9), (14, 14)],
             [(0, -9), (1, -15), (3, -20)], [(5, -7), (10, -10), (14, -12)],
             [(-9, 2), (-3, 9), (-1, 16)]]
    pathc = set()
    for pl in paths:
        for (ax, az), (bx, bz) in zip(pl, pl[1:]):
            n = int(max(abs(bx - ax), abs(bz - az)) * 3) + 1
            for i in range(n + 1):
                t = i / n
                px, pz = ax + (bx - ax) * t, az + (bz - az) * t
                for x in (math.floor(px), math.floor(px + 0.6)):
                    for z in (math.floor(pz), math.floor(pz + 0.6)):
                        if (x, z) in H and (x, z) not in river:
                            pathc.add((x, z))

    def mat(x, y, z, h):
        if (x, z) in river:
            if y == h:
                r = hsh(x, z, 11)
                return 'gravel' if r < 0.45 else ('sand' if r < 0.85 else 'clay')
            return 'dirt' if y >= h - 2 else 'stone'
        if y == h:
            if (x, z) in pathc:
                return 'dirt_path'
            if abs(z - zr(x)) < 2.6:
                return 'sand' if hsh(x, z, 3) < 0.6 else 'grass_block'
            return 'grass_block'
        if y >= h - 3:
            return 'sandstone' if abs(z - zr(x)) < 2.6 and y == h - 1 else 'dirt'
        return 'stone' if hsh(x, y, z) < 0.8 else ('andesite' if hsh(x, y, z, 2) < 0.5 else 'cobblestone')
    c.terrain(mat)
    for (x, z) in river:
        c.set(x, W, z, 'water')

    # ponts (largeur 4 : rambardes + 2 de passage), tablier au niveau W+1
    for x0 in (-10, 10):
        for x in range(x0, x0 + 4):
            for z in IR:
                if H[(x, z)] <= W and abs(z - zr(x)) < 3:
                    c.set(x, W + 1, z, 'spruce_planks')
                    if x in (x0, x0 + 3):
                        c.set(x, W + 2, z, 'spruce_fence')
        zs = [z for z in IR if H[(x0, z)] <= W and abs(z - zr(x0)) < 3]
        for x in (x0, x0 + 3):
            zz = [z for z in IR if H[(x, z)] <= W and abs(z - zr(x)) < 3]
            c.set(x, W + 3, min(zz), 'lantern')
            c.set(x, W + 3, max(zz), 'lantern')

    # kiosque (centre 0, -9) : estrade 7 x 7 surélevée d'un bloc, poteaux, toit pyramidal
    kx, kz = 0, -9
    hp = H[(kx, kz)]
    for dx in range(-3, 4):
        for dz in range(-3, 4):
            edge = max(abs(dx), abs(dz)) == 3
            c.set(kx + dx, hp + 1, kz + dz, 'stone_bricks' if edge else ('glowstone' if dx == dz == 0 else 'polished_andesite'))
    for dx in (-3, 3):
        for dz in (-3, 3):
            c.box(kx + dx, hp + 2, kz + dz, kx + dx, hp + 4, kz + dz, 'stripped_spruce_log')
    c.roof(kx, kz, hp + 5, 4, 'dark_oak_stairs', 'dark_oak_planks')
    c.set(kx, hp + 4, kz, 'lantern[hanging=true]')

    # moulin (-14, -14) : tour 5 x 5 creuse avec deux portes (est/ouest), ailes au sud
    mx, mz = -14, -14
    hp = H[(mx, mz)]
    c.box(mx - 2, hp + 1, mz - 2, mx + 2, hp + 3, mz + 2, 'stone_bricks')
    c.box(mx - 2, hp + 4, mz - 2, mx + 2, hp + 8, mz + 2, 'oak_planks')
    for dx in (-2, 2):
        for dz in (-2, 2):
            c.box(mx + dx, hp + 1, mz + dz, mx + dx, hp + 1, mz + dz, 'mossy_stone_bricks')
            c.box(mx + dx, hp + 4, mz + dz, mx + dx, hp + 8, mz + dz, 'spruce_log')
    c.box(mx - 1, hp + 1, mz - 1, mx + 1, hp + 3, mz + 1, 'air')
    c.set(mx, hp, mz, 'glowstone')
    c.set(mx, hp + 3, mz, 'lantern[hanging=true]')
    for dx in (-2, 2):
        c.box(mx + dx, hp + 1, mz, mx + dx, hp + 2, mz, 'air')
    c.box(mx - 1, hp + 6, mz - 2, mx + 1, hp + 6, mz - 2, 'glass_pane')
    c.roof(mx, mz, hp + 9, 3, 'spruce_stairs', 'spruce_planks')
    hub = hp + 7
    c.set(mx, hub, mz + 3, 'spruce_log[axis=z]')
    for sx in (-1, 1):
        for sy in (-1, 1):
            for d in range(1, 5):
                c.set(mx + sx * d, hub + sy * d, mz + 3, 'stripped_spruce_log')
                if d >= 2:
                    c.set(mx + sx * (d - 1), hub + sy * d, mz + 3, 'white_wool')
    # bottes de foin et tonneaux près du moulin
    for (x, z) in ((-9, -17), (-9, -16), (-10, -17)):
        c.set(x, c.top(x, z) + 1, z, 'hay_block')
    c.set(-9, c.top(-9, -17) + 1, -17, 'hay_block')
    for (x, z) in ((-18, -10), (-19, -10)):
        c.set(x, c.top(x, z) + 1, z, 'barrel[facing=up]')

    # rochers
    rocks = [(-4, 11, 2.2, 1.6, 2), (6, 13, 1.8, 2.4, 3), (-20, 4, 2.0, 1.5, 2), (19, -4, 1.6, 2.2, 2),
             (8, -16, 2.0, 1.7, 3), (-6, -19, 2.4, 1.6, 2), (19, 21, 2.0, 2.0, 2), (-21, -21, 2.0, 2.0, 3),
             (-4, -3, 1.4, 1.2, 1), (17, 6, 1.5, 1.3, 2), (-17, 21, 1.6, 1.6, 2), (6, 21, 1.3, 1.6, 1),
             (21, -18, 1.8, 1.5, 2)]
    for rx, rz, ax, az, hmax in rocks:
        for x in range(int(rx - ax - 1), int(rx + ax + 2)):
            for z in range(int(rz - az - 1), int(rz + az + 2)):
                q = ((x - rx) / ax) ** 2 + ((z - rz) / az) ** 2
                if q > 1 or (x, z) not in H or (x, z) in river or (x, z) in pathc:
                    continue
                hr = max(1, int(round(hmax * (1 - q) + 0.4)))
                h = H[(x, z)]
                for y in range(h + 1, h + hr + 1):
                    r = hsh(x, y, z, 5)
                    c.set(x, y, z, 'mossy_cobblestone' if r < 0.4 else 'cobblestone' if r < 0.65 else 'andesite' if r < 0.85 else 'stone')

    # arbres (tronc + feuillage persistant)
    trees = [(-20, -4, 'oak', 5), (-19, 9, 'birch', 6), (-7, 15, 'oak', 5), (3, 20, 'birch', 5), (9, -12, 'oak', 5),
             (20, 3, 'oak', 6), (21, 10, 'birch', 5), (9, 19, 'oak', 5), (-22, 19, 'oak', 5), (-2, -21, 'birch', 6),
             (19, -21, 'oak', 5), (-13, 5, 'birch', 5), (14, -4, 'oak', 5), (-23, -14, 'birch', 5), (2, 9, 'oak', 5)]
    for tx, tz, wood, th in trees:
        g = H[(tx, tz)]
        for dy in range(-2, 3):
            ly = g + th - 1 + dy
            r = 2 if dy <= 0 else (1 if dy == 1 else 0)
            for dx in range(-r, r + 1):
                for dz in range(-r, r + 1):
                    if r == 2 and abs(dx) == 2 and abs(dz) == 2 and hsh(tx + dx, ly, tz + dz) < 0.7:
                        continue
                    if dy == 2 and (dx or dz):
                        continue
                    if (tx + dx, tz + dz) in H and ly > H[(tx + dx, tz + dz)] + 2:
                        if c.get(tx + dx, ly, tz + dz) == 'air':
                            c.set(tx + dx, ly, tz + dz, f'{wood}_leaves[persistent=true]')
            if dy == 1:
                for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    c.set(tx + dx, ly + 1, tz + dz, f'{wood}_leaves[persistent=true]')
        c.box(tx, g + 1, tz, tx, g + th, tz, f'{wood}_log')

    # lampadaires le long des chemins
    for (x, z) in ((-11, -4), (-7, 3), (-6, -10), (6, -10), (13, 1), (9, 9), (-2, -16), (-13, 11), (-1, 12), (11, -12)):
        if (x, z) in pathc or (x, z) in river:
            continue
        c.lamp_post(x, z)

    # fleurs et herbes
    flowers = ['poppy', 'dandelion', 'cornflower', 'oxeye_daisy', 'azure_bluet', 'allium']
    for (x, z), h in H.items():
        if (x, z) in river or (x, z) in pathc or c.get(x, h, z) != 'grass_block' or c.get(x, h + 1, z) != 'air':
            continue
        r = hsh(x, z, 21)
        if r < 0.07:
            c.set(x, h + 1, z, flowers[int(hsh(x, z, 22) * len(flowers))])
        elif r < 0.25:
            c.set(x, h + 1, z, 'short_grass')

    c.home = (-3, H[(-3, -16)] + 1, -16)
    degager_feuilles(c)
    pts = [(-3, -16), (5, -14), (-18, -6), (-23, 12), (-10, 20), (2, 15), (13, 18), (21, 15), (17, -1), (21, -10),
           (13, -20), (-11, -22), (-15, -4), (6, 4), (-4, 4), (20, 23)]
    c.spawns = [(x, c.top(x, z) + 1, z) for x, z in pts]
    return c


def degager_feuilles(c, tours=6):
    """retire les feuilles qui ferment une poche sous un arbre (position sans retour)"""
    for _ in range(tours):
        err, st, fwd = verifier(c)
        bad = [e for e in err if 'sans retour' in e]
        if not bad:
            return
        cols = {}
        for (x, y, z), b in c.v.items():
            o = occ(b)
            if o:
                cols.setdefault((x, z), []).append((y + o[0], y + o[1], o[2]))
        # recalcul local : toutes les positions dont la colonne a des feuilles juste au-dessus
        changed = False
        for (x, y, z), b in list(c.v.items()):
            if not base(b).endswith('_leaves'):
                continue
            g = c.H.get((x, z))
            if g is not None and y - g <= 4:
                # feuille basse : on la garde seulement si une colonne voisine plus haute ne la colle pas
                if any(c.H.get((x + dx, z + dz), 0) >= y - 2 for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    c.set(x, y, z, 'air')
                    changed = True
        if not changed:
            return


def ell(x, z, cx, cz, rx, rz):
    return ((x - cx) / rx) ** 2 + ((z - cz) / rz) ** 2 <= 1.0


FACE = {(1, 0): 'east', (-1, 0): 'west', (0, 1): 'south', (0, -1): 'north'}


def rampe(H, starts, d, L, steps=None):
    """escalier de 1 bloc par marche construit vers l'extérieur d'un plateau de niveau L.
    starts : cases du plateau (au niveau L) ; d : direction de descente. Renvoie {case: direction de montée}"""
    out = {}
    dx, dz = d
    for (x, z) in starts:
        while H.get((x + dx, z + dz)) == L:
            x, z = x + dx, z + dz
        v = L - 1
        n = 0
        while (x + dx, z + dz) in H and H[(x + dx, z + dz)] < v and (steps is None or n < steps):
            x, z = x + dx, z + dz
            H[(x, z)] = v
            out[(x, z)] = (-dx, -dz)
            v -= 1
            n += 1
    return out


# =====================================================================================
# Carte 2 — Canyon
# =====================================================================================
STRATA = ['terracotta', 'orange_terracotta', 'orange_terracotta', 'terracotta', 'yellow_terracotta', 'terracotta',
          'white_terracotta', 'orange_terracotta', 'red_terracotta', 'terracotta', 'brown_terracotta',
          'orange_terracotta', 'light_gray_terracotta', 'terracotta', 'yellow_terracotta', 'orange_terracotta',
          'red_terracotta', 'terracotta', 'white_terracotta', 'orange_terracotta', 'terracotta', 'brown_terracotta']


def carte2():
    c = Carte(2, 'CANYON', 26800, 'gold', 'mesa en terracotta : plateaux, arche, tunnel et pont suspendu')
    F, L1, L2, L3 = 82, 86, 90, 94
    H = {}
    for x in IR:
        for z in IR:
            h = F
            we = -9 + 1.5 * math.sin(z / 4.0) + 1.0 * math.sin(z / 2.3 + 1)
            ee = 9 + 1.5 * math.sin(z / 3.7 + 2) + 1.0 * math.cos(z / 2.1)
            if x < we or x > ee:
                h = L1
            if ell(x, z, -16, -12, 7, 6.5) or ell(x, z, 16, -12, 7, 6.5):
                h = L2
            if ell(x, z, -18, -18, 3.5, 3.5) or ell(x, z, 18, -18, 3.5, 3.5):
                h = L3
            if ell(x, z, 18, 18, 5, 4.5):                 # cirque au sud-est (sol du canyon)
                h = F
            if ell(x, z, 1, 14, 3.6, 2.6):               # butte basse au milieu du canyon
                h = F + 2
            elif ell(x, z, 1, 14, 4.8, 3.8):
                h = max(h, F + 1)
            H[(x, z)] = h
    stairs = {}
    # plateaux ouest/est <-> fond du canyon
    stairs.update(rampe(H, [(-20, z) for z in (-3, -2, -1)], (1, 0), L1))
    stairs.update(rampe(H, [(20, z) for z in (-3, -2, -1)], (-1, 0), L1))
    stairs.update(rampe(H, [(-20, z) for z in (18, 19, 20)], (1, 0), L1))
    stairs.update(rampe(H, [(x, 12) for x in (17, 18, 19)], (0, 1), L1))          # descente dans le cirque
    stairs.update(rampe(H, [(20, z) for z in (8, 9)], (-1, 0), L1))
    # plateaux -> buttes
    stairs.update(rampe(H, [(x, -12) for x in (-17, -16, -15)], (0, 1), L2))
    stairs.update(rampe(H, [(x, -12) for x in (15, 16, 17)], (0, 1), L2))
    # buttes -> sommets
    stairs.update(rampe(H, [(-18, z) for z in (-19, -18, -17)], (1, 0), L3))
    stairs.update(rampe(H, [(18, z) for z in (-19, -18, -17)], (-1, 0), L3))
    c.H = H

    def mat(x, y, z, h):
        if y == h:
            if (x, z) in stairs:
                return f'smooth_red_sandstone'
            r = hsh(x, z, 31)
            if h == F:
                return 'red_sand' if r < 0.75 else ('coarse_dirt' if r < 0.9 else 'packed_mud')
            return 'red_sand' if r < 0.6 else ('coarse_dirt' if r < 0.78 else 'terracotta')
        if y == h - 1 and h > F:
            return 'red_sandstone' if (x, z) not in stairs else 'smooth_red_sandstone'
        return STRATA[(y - Y0 + (1 if hsh(x // 4, z // 4, 33) < 0.25 else 0)) % len(STRATA)]
    c.terrain(mat)
    # marches en escaliers
    for (x, z), d in stairs.items():
        c.set(x, H[(x, z)], z, f'red_sandstone_stairs[facing={FACE[d]}]')

    # arche naturelle au sud, entre les plateaux ouest et est (z 4..6)
    for x in range(-10, 11):
        if H[(x, 5)] >= L1:
            continue
        top = 86 + int(2.5 * (1 - (x / 8.5) ** 2) + 0.5)
        under = 83 + int(4.0 * (1 - (x / 9.0) ** 2) + 0.5)
        for z in (4, 5, 6):
            if H[(x, z)] >= L1:
                continue
            u = under + (1 if z != 5 and hsh(x, z, 41) < 0.4 else 0)
            for y in range(u, top + 1):
                c.set(x, y, z, 'red_sand' if y == top else STRATA[(y - Y0) % len(STRATA)])
    # pont suspendu entre les deux buttes (z -14..-10, rambardes en z -14 et -10)
    for x in range(-11, 12):
        if H[(x, -12)] >= L2:
            continue
        y = 90 - int(2 * (1 - (x / 9.5) ** 2) + 0.5)
        for z in range(-14, -9):
            c.set(x, y, z, 'spruce_planks' if z in (-14, -10) or (x % 3) else 'stripped_spruce_log[axis=z]')
        for z in (-14, -10):
            c.set(x, y + 1, z, 'spruce_fence')
            if x % 3 == 0:
                c.box(x, y - 2, z, x, y - 1, z, 'iron_chain')
    for x in (-10, 10):
        for z in (-14, -10):
            g = c.top(x, z)
            c.box(x, g + 1, z, x, g + 2, z, 'spruce_log')
            c.set(x, g + 3, z, 'lantern')
    # tunnel ouest -> cirque (z 16..18), plafond = plateau
    for x in range(6, 15):
        for z in (16, 17, 18):
            if H[(x, z)] == L1:
                c.box(x, F + 1, z, x, F + 3, z, 'air')
                c.set(x, F, z, 'smooth_red_sandstone')
                if x % 3 == 0 and z != 17:
                    c.set(x, F + 3, z, 'lantern[hanging=true]')
    for x in range(6, 15):
        for z in (15, 19):
            if H[(x, z)] == L1 and c.get(x, F + 2, z) != 'air':
                c.set(x, F + 2, z, 'cut_red_sandstone')
    # cheminées de fée (hoodoos) dans le canyon
    hoodoos = [(-1, -4, 4, 2), (-4, 10, 3, 1), (5, 10, 2, 1), (3, 20, 5, 2), (-5, -18, 3, 1), (6, -19, 2, 1),
               (-4, -9, 1, 1), (-3, -9, 2, 1), (-2, -9, 3, 1), (5, 0, 3, 1), (-6, 20, 2, 1), (19, 21, 3, 1)]
    for hx, hz, hh, w in hoodoos:
        for x in range(hx, hx + w):
            for z in range(hz, hz + w):
                g = H[(x, z)]
                for y in range(g + 1, g + hh + 1):
                    c.set(x, y, z, 'red_sandstone' if y == g + hh else STRATA[(y - Y0 + 3) % len(STRATA)])
    # éclats de glowstone dans les falaises
    n = 0
    for (x, z), h in sorted(H.items(), key=lambda t: hsh(t[0][0], t[0][1], 51)):
        if n >= 14 or h < L1:
            continue
        low = min(H.get((x + dx, z + dz), 999) for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        if h - low >= 3 and (x, z) not in stairs:
            c.set(x, low + 2, z, 'glowstone')
            n += 1
    # lanternes sur poteaux
    for (x, z) in ((-14, -2), (14, 2), (-20, 15), (21, 6), (-13, -9), (13, -9), (-20, -18), (21, -19), (0, -21),
                   (-6, 2), (7, 7), (16, 22), (-12, 22)):
        c.lamp_post(x, z, 'dark_oak_fence', 1)
    # buissons morts et herbes sèches (pas de cactus)
    for (x, z), h in H.items():
        if c.get(x, h + 1, z) != 'air' or base(c.get(x, h, z)) not in ('red_sand', 'coarse_dirt', 'terracotta'):
            continue
        r = hsh(x, z, 61)
        if r < 0.05:
            c.set(x, h + 1, z, 'dead_bush')
        elif r < 0.11:
            c.set(x, h + 1, z, 'short_dry_grass')
        elif r < 0.13:
            c.set(x, h + 1, z, 'tall_dry_grass')
    c.home = (0, F + 1, -1)
    pts = [(0, -1), (-3, 14), (3, -15), (-5, 4), (6, 16), (18, 18), (-18, 5), (18, -2), (-17, -11), (17, -14),
           (-20, 22), (13, 10), (-14, 12), (-18, -21), (19, -21), (-5, -22)]
    c.spawns = [(x, c.top(x, z) + 1, z) for x, z in pts]
    return c


# =====================================================================================
# Carte 3 — Village perché
# =====================================================================================
def carte3():
    c = Carte(3, 'VILLAGE PERCHÉ', 27400, 'aqua', 'place en contrebas, terrasses, toits et passerelles')
    P, T1, T2, T3 = 82, 85, 88, 91
    H = {}
    for x in IR:
        for z in IR:
            d = max(abs(x), abs(z - 1))
            h = P if d <= 7 else (T1 if d <= 13 else T2)
            if h == T2 and (z <= -19 or x <= -19):
                h = T3
            H[(x, z)] = h
    stairs = {}
    # place <-> terrasse 1 (4 escaliers)
    stairs.update(rampe(H, [(x, -8) for x in (-1, 0, 1)], (0, 1), T1))
    stairs.update(rampe(H, [(x, 10) for x in (-1, 0, 1)], (0, -1), T1))
    stairs.update(rampe(H, [(9, z) for z in (0, 1, 2)], (-1, 0), T1))
    stairs.update(rampe(H, [(-9, z) for z in (0, 1, 2)], (1, 0), T1))
    # terrasse 1 <-> terrasse 2
    stairs.update(rampe(H, [(x, -14) for x in (6, 7, 8)], (0, 1), T2))
    stairs.update(rampe(H, [(x, 16) for x in (-8, -7, -6)], (0, -1), T2))
    stairs.update(rampe(H, [(15, z) for z in (3, 4, 5)], (-1, 0), T2))
    stairs.update(rampe(H, [(-15, z) for z in (-4, -3, -2)], (1, 0), T2))
    # terrasse 2 <-> terrasse 3
    stairs.update(rampe(H, [(x, -20) for x in (4, 5, 6)], (0, 1), T3))
    stairs.update(rampe(H, [(-20, z) for z in (8, 9, 10)], (1, 0), T3))
    c.H = H
    plaza_pat = {}

    def mat(x, y, z, h):
        if y == h:
            if (x, z) in stairs:
                return 'stone_bricks'
            if h == P:
                r = max(abs(x), abs(z - 1))
                if r in (2, 5):
                    return 'polished_andesite'
                if (x + z) % 7 == 0 and r == 6:
                    return 'glowstone'
                return 'cobblestone' if hsh(x, z, 71) < 0.15 else 'stone_bricks'
            r = hsh(x, z, 72)
            return 'grass_block' if r < 0.7 else ('dirt_path' if r < 0.85 else 'coarse_dirt')
        if y >= h - 1 and h > P:
            r = hsh(x, y, z, 73)
            return 'stone_bricks' if r < 0.6 else ('mossy_stone_bricks' if r < 0.85 else 'cracked_stone_bricks')
        return 'stone' if y < h - 3 else 'stone_bricks'
    c.terrain(mat)
    for (x, z), d in stairs.items():
        c.set(x, H[(x, z)], z, f'stone_brick_stairs[facing={FACE[d]}]')

    def house(x1, z1, x2, z2, doors, windows, roof='flat', wall='oak_planks', corner='spruce_log', roofb='spruce_planks',
              hgt=3, chimney=None):
        fy = H[(x1, z1)]
        c.box(x1, fy + 1, z1, x2, fy + hgt, z2, wall)
        for x in (x1, x2):
            for z in (z1, z2):
                c.box(x, fy + 1, z, x, fy + hgt, z, corner)
        c.box(x1 + 1, fy + 1, z1 + 1, x2 - 1, fy + hgt, z2 - 1, 'air')
        c.box(x1 + 1, fy, z1 + 1, x2 - 1, fy, z2 - 1, 'spruce_planks')
        for (x, z) in doors:
            c.box(x, fy + 1, z, x, fy + 2, z, 'air')
        for (x, z) in windows:
            c.set(x, fy + 2, z, 'glass_pane')
        ry = fy + hgt + 1
        if roof == 'flat':
            c.box(x1, ry, z1, x2, ry, z2, roofb)
            c.set((x1 + x2) // 2, ry - 1, (z1 + z2) // 2, 'lantern[hanging=true]')
            if chimney:
                cx_, cz_ = chimney
                c.box(cx_, ry + 1, cz_, cx_, ry + 2, cz_, 'bricks')
        else:
            c.box(x1, ry, z1, x2, ry, z2, roofb)
            c.set((x1 + x2) // 2, ry - 1, (z1 + z2) // 2, 'lantern[hanging=true]')
            i = 0
            while z1 - 1 + i <= z2 + 1 - i:
                y = ry + i
                za, zb = z1 - 1 + i, z2 + 1 - i
                for x in range(x1 - 1, x2 + 2):
                    if za == zb:
                        c.set(x, y, za, 'dark_oak_planks')
                    else:
                        c.set(x, y, za, 'dark_oak_stairs[facing=south]')
                        c.set(x, y, zb, 'dark_oak_stairs[facing=north]')
                for x in (x1, x2):
                    for z in range(za + 1, zb):
                        c.set(x, y, z, wall)
                i += 1

    def passerelle(x1, z1, x2, z2, y, rails):
        c.box(x1, y, z1, x2, y, z2, 'spruce_planks')
        for (a, b, e, f) in rails:
            c.box(a, y + 1, b, e, y + 1, f, 'spruce_fence')

    # terrasse 1 : maisons adossées au mur de la terrasse 2 (toit = terrasse 2 + 1)
    house(-12, -12, -7, -9, [(-9, -9), (-7, -10)], [(-11, -9)], chimney=(-11, -12))
    house(-4, -12, 1, -9, [(-2, -9), (-4, -11)], [(0, -9)])
    passerelle(-6, -12, -5, -9, T1 + 4, [])
    house(-4, 11, 1, 14, [(-2, 11), (1, 13)], [(0, 11)], wall='spruce_planks', corner='stripped_oak_log', roofb='oak_planks')
    house(4, 11, 8, 14, [(6, 11), (4, 12)], [(7, 11)], wall='white_terracotta', corner='oak_log', chimney=(7, 14))
    passerelle(2, 11, 3, 14, T1 + 4, [])
    house(10, -6, 13, -1, [(10, -3), (12, -1)], [(10, -5)], wall='spruce_planks', corner='stripped_oak_log', roofb='oak_planks')
    house(10, 7, 13, 12, [(10, 9), (11, 7)], [(10, 11)])
    house(-13, 3, -10, 8, [(-10, 5), (-12, 3)], [(-10, 7)], wall='white_terracotta', corner='oak_log')
    house(-13, 10, -10, 14, [(-10, 12)], [(-11, 10)], wall='spruce_planks', corner='stripped_oak_log', roofb='oak_planks')
    # terrasse 2 nord / ouest : maisons adossées à la terrasse 3
    house(-10, -18, -5, -15, [(-7, -15), (-5, -17)], [(-9, -15)], wall='white_terracotta', corner='oak_log')
    house(-2, -18, 2, -15, [(0, -15), (-2, -16)], [(2, -16)], chimney=(1, -18))
    passerelle(-4, -18, -3, -15, T2 + 4, [])
    house(8, -18, 13, -15, [(10, -15), (13, -16)], [(8, -16)], wall='spruce_planks', corner='stripped_oak_log', roofb='oak_planks')
    house(-18, -8, -16, -3, [(-16, -6), (-17, -3)], [(-16, -4)], hgt=3)
    house(-18, 1, -16, 6, [(-16, 3), (-17, 1)], [(-16, 5)], wall='white_terracotta', corner='oak_log')
    # terrasse 2 sud / est : maisons à toit en pente (cachettes)
    house(-3, 18, 3, 21, [(0, 18), (3, 19), (-3, 20)], [(-2, 18), (2, 18)], roof='pitch', wall='white_terracotta', corner='dark_oak_log')
    house(17, -4, 21, -1, [(17, -2), (19, -1), (19, -4)], [(21, -3)], roof='pitch', wall='oak_planks', corner='dark_oak_log')
    house(15, 15, 19, 18, [(17, 15), (15, 17)], [(19, 16)], roof='pitch', wall='spruce_planks', corner='dark_oak_log')
    # clocher sur la terrasse 3 (coin nord-ouest), traversant (portes est et sud)
    tx, tz = -21, -21
    fy = H[(tx, tz)]
    c.box(tx - 2, fy + 1, tz - 2, tx + 2, fy + 7, tz + 2, 'stone_bricks')
    c.box(tx - 1, fy + 1, tz - 1, tx + 1, fy + 3, tz + 1, 'air')
    c.box(tx + 2, fy + 1, tz, tx + 2, fy + 2, tz, 'air')
    c.box(tx, fy + 1, tz + 2, tx, fy + 2, tz + 2, 'air')
    c.set(tx, fy + 3, tz, 'lantern[hanging=true]')
    c.box(tx - 1, fy + 5, tz - 2, tx + 1, fy + 6, tz + 2, 'air')
    c.box(tx - 2, fy + 5, tz - 1, tx + 2, fy + 6, tz + 1, 'air')
    c.box(tx - 1, fy + 4, tz - 1, tx + 1, fy + 4, tz + 1, 'stone_bricks')
    c.set(tx, fy + 6, tz, 'bell[attachment=ceiling]')
    c.roof(tx, tz, fy + 8, 3, 'deepslate_tile_stairs', 'deepslate_tiles')
    # puits fermé au centre de la place
    wx, wz = 0, 1
    c.box(wx - 1, P + 1, wz - 1, wx + 1, P + 1, wz + 1, 'mossy_cobblestone')
    c.set(wx, P + 1, wz, 'water')
    for dx in (-1, 1):
        for dz in (-1, 1):
            c.box(wx + dx, P + 2, wz + dz, wx + dx, P + 3, wz + dz, 'oak_fence')
    c.box(wx - 1, P + 4, wz - 1, wx + 1, P + 4, wz + 1, 'spruce_slab[type=bottom]')
    c.set(wx, P + 4, wz, 'spruce_planks')
    c.set(wx, P + 3, wz, 'iron_chain')
    c.set(wx, P + 2, wz, 'lantern[hanging=true]')
    # étals de marché (auvents de laine) sur la place
    for (sx, sz, wool) in ((-5, -3, 'red_wool'), (4, 5, 'yellow_wool')):
        for dx in (0, 2):
            for dz in (0, 1):
                c.box(sx + dx, P + 1, sz + dz, sx + dx, P + 2, sz + dz, 'oak_fence')
        c.box(sx, P + 3, sz, sx + 2, P + 3, sz + 1, wool)
        c.set(sx + 1, P + 1, sz, 'barrel[facing=up]')
    # bancs et pots de fleurs
    for (x, z, f) in ((-6, 6, 'east'), (6, -4, 'west'), (-3, 7, 'north'), (3, -5, 'south')):
        c.set(x, P + 1, z, f'oak_stairs[facing={f}]')
    # arbres (sur les terrasses larges)
    for tx_, tz_, wood in ((10, 20, 'oak'), (20, 12, 'birch'), (21, 21, 'oak'), (-12, 20, 'oak'), (14, -21, 'birch'), (-22, -6, 'birch')):
        g = H[(tx_, tz_)]
        th = 5
        for dy in range(-1, 3):
            ly = g + th - 1 + dy
            r = 2 if dy <= 0 else (1 if dy == 1 else 0)
            for dx in range(-r, r + 1):
                for dz in range(-r, r + 1):
                    if r == 2 and abs(dx) == 2 and abs(dz) == 2:
                        continue
                    q = (tx_ + dx, tz_ + dz)
                    if q in H and ly > H[q] + 2 and c.get(q[0], ly, q[1]) == 'air':
                        c.set(q[0], ly, q[1], f'{wood}_leaves[persistent=true]')
        c.box(tx_, g + 1, tz_, tx_, g + th, tz_, f'{wood}_log')
    # lanternes sur poteaux et bacs à fleurs
    for (x, z) in ((-7, -6), (7, -6), (-7, 8), (7, 8), (-3, -8), (3, 10), (11, 1), (-11, 1), (5, -13), (-9, 15), (14, 6),
                   (-14, -1), (2, -20), (-20, 6), (20, 20), (0, 23), (23, 5), (-23, -16), (-14, -22)):
        if c.get(x, H[(x, z)] + 1, z) == 'air' and (x, z) not in stairs:
            c.lamp_post(x, z, 'oak_fence', 1)
    flowers = ['poppy', 'dandelion', 'cornflower', 'oxeye_daisy', 'allium', 'red_tulip', 'white_tulip']
    for (x, z), h in H.items():
        if c.get(x, h, z) != 'grass_block' or c.get(x, h + 1, z) != 'air':
            continue
        r = hsh(x, z, 81)
        if r < 0.08:
            c.set(x, h + 1, z, flowers[int(hsh(x, z, 82) * len(flowers))])
        elif r < 0.2:
            c.set(x, h + 1, z, 'short_grass')
    c.home = (0, P + 1, -4)
    pts = [(0, -4), (-4, 4), (5, 2), (-2, 6), (-11, -7), (6, 9), (11, -9), (-10, 0), (0, -14),
           (12, 14), (-17, 17), (20, 7), (20, -12), (-16, 12), (-12, -21), (6, 22)]
    c.spawns = [(x, c.top(x, z) + 1, z) for x, z in pts]
    return c


# =====================================================================================
# Sorties
# =====================================================================================
def write(name, lines):
    with open(os.path.join(OUT, name + '.mcfunction'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


def main():
    os.makedirs(OUT, exist_ok=True)
    cartes = [carte1(), carte2(), carte3()]
    ok = True
    fl = ['# TNT Tag — chargement permanent des emprises des 3 cartes à relief (généré par tools/tnttag/gen_maps.py)']
    for c in cartes:
        err, st, fwd = verifier(c)
        cmds, btop = c.commands()
        top = c.ymax()
        py = top + 15
        tty = int(math.floor(st['tmin'])) - 3
        cz = c.cz
        print(f'carte {c.k} {c.nom}: {len(cmds)} commandes, blocs y {Y0}..{top}, barrières jusqu\'à {btop}, '
              f'$py {py}, $tty {tty}, {st}')
        for e in err:
            print('  ERREUR', e)
            ok = False
        write(f'build_{c.k}', cmds)
        hx, hy, hz = c.home
        L = [f'# TNT Tag — préparation de la carte {c.k} « {c.nom.capitalize()} » (centre 0 ~ {cz}), générée par tools/tnttag/gen_maps.py',
             f'function mg:tnttag/map/build_{c.k}',
             '# Perchoir des éliminés (~15 blocs au-dessus du point le plus haut) et hauteur d\'élimination',
             'scoreboard players set $px mg.st 0', f'scoreboard players set $py mg.st {py}',
             f'scoreboard players set $pz mg.st {cz}', f'scoreboard players set $tty mg.st {tty}',
             f'kill @e[type=minecraft:item,x=-{RING},y={Y0},z={cz - RING},dx={2 * RING},dy={YCLR - Y0},dz={2 * RING}]',
             'gamemode adventure @a[tag=mg.play]',
             f'execute as @a[tag=mg.play] run spawnpoint @s {hx} {hy} {hz + cz}',
             f'# Placement sur {len(c.spawns)} points de départ fixes au sol (tirés au hasard, deux passes si beaucoup de joueurs)',
             'tag @a remove mg.tts']
        for _ in range(2):
            for (x, y, z) in c.spawns:
                L.append(f'execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {{x:{x}.5,y:{y},z:{z + cz}.5,fx:0.5,fz:{cz}.5}}')
        L.append(f'tp @a[tag=mg.play,tag=!mg.tts] {hx}.5 {hy} {hz + cz}.5')
        L.append('tag @a remove mg.tts')
        write(f'setup_{c.k}', L)
        write(f'info_{c.k}', [f'# TNT Tag — annonce de la carte {c.k}',
                              f'tellraw @a [{{"text":"Carte : ","color":"gray"}},{{"text":"{c.nom}","color":"{c.couleur}","bold":true}},{{"text":" ({c.desc})","color":"gray"}}]'])
        fl.append(f'forceload add -{RING} {cz - RING} {RING} {cz + RING}')
    write('fl', fl)
    write('sp', ['# @s = joueur placé sur un point de départ (macro : x y z, regard vers fx fz)',
                 '$tp @s $(x) $(y) $(z) facing $(fx) $(y) $(fz)',
                 'tag @s add mg.tts'])
    if not ok:
        sys.exit(1)


if __name__ == '__main__':
    main()
