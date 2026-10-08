"""Decors et objets du Canyon du Couchant : anneaux, portiques de reprise, cheminees de fee, arches, viaduc, crete,
depart. (La ville fantome est dans town_canyon.py.) Tout ce qui est solide est enregistre dans le World pour que le
pilote automatique le voie.
Python stdlib uniquement (compatible 3.8).
"""
import math
import random

import course_canyon as C

RING_COLORS = {'ring': ('sea_lantern', 'light_blue_concrete', 'blue_concrete'),
               'finish': ('sea_lantern', 'lime_concrete', 'white_concrete')}


# ---------------------------------------------------------------- anneaux
def ring_frame(w, x, cy, cz, kind='ring'):
    """Cadre carre de 17 x 17 (trou de 9 x 9) dans le plan x..x+1, centre (cy, cz) : couches colorees, rebord lumineux."""
    a, b, c = RING_COLORS[kind]
    for r, blk in ((8, c), (7, b), (5, a), (4, 'air')):
        w.box(x, cy - r, cz - r, x + 1, cy + r, cz + r, blk)


def gold_frame(w, x, cy, cz):
    """Anneau d'or : cadre d'or de 9 x 9 (1 bloc d'epaisseur), trou de 7 x 7."""
    for r, blk in ((4, 'gold_block'), (3, 'air')):
        w.box(x, cy - r, cz - r, x + 1, cy + r, cz + r, blk)


def cp_gate(w, x, cy, cz):
    """Portique de point de reprise : deux colonnes lumineuses de part et d'autre de la trajectoire, linteau tres haut."""
    for dz in (-12, 11):
        w.box(x + 4, cy - 16, cz + dz, x + 5, cy + 34, cz + dz + 1, 'sea_lantern')
    w.box(x + 4, cy + 34, cz - 12, x + 5, cy + 35, cz + 12, 'lime_concrete')


# ---------------------------------------------------------------- strates en blocs
def col(w, strata, x1, z1, x2, z2, y0, y1):
    """Colonne pleine rayee comme le relief (une boite par bande de materiau)."""
    for s0, s1, blk in strata:
        if s1 < y0:
            continue
        if s0 > y1:
            break
        w.box(x1, max(y0, s0), z1, x2, min(y1, s1), z2, blk)


# ---------------------------------------------------------------- cheminees de fee
def hoodoo(w, strata, x, z, base, top, rs, rc):
    """Cheminee de fee : pied evase, fut carre de demi-cote rs, cou plus fin, chapeau de demi-cote rc (3 + 1 blocs)."""
    flare = base + 8
    col(w, strata, x - rs - 2, z - rs - 2, x + rs + 2, z + rs + 2, base, flare)
    col(w, strata, x - rs, z - rs, x + rs, z + rs, flare + 1, top - 7)
    rn = max(rs - 1, 1)
    col(w, strata, x - rn, z - rn, x + rn, z + rn, top - 6, top - 4)
    col(w, strata, x - rc, z - rc, x + rc, z + rc, top - 3, top - 1)
    col(w, strata, x - rc + 1, z - rc + 1, x + rc - 1, z + rc - 1, top, top)


def near_path(x, z, r, y_top, path, margin=10):
    """Vrai si une cheminee de demi-cote r en (x, z) coiffee a y_top gene la trajectoire (cadres des anneaux compris)."""
    if y_top < path.y(x) - 12:
        return False
    for xx in range(int(x - r - 4), int(x + r + 5), 2):
        if abs(z - C.CZ - C.lat(xx)) < r + margin:
            return True
    return False


def hoodoos(w, strata, path, rings, golds):
    """Slalom : une paire de cheminees autour de chacun des anneaux 2 a 4, puis des cheminees decoratives dans le canyon."""
    rnd = random.Random(1860)
    placed = [(gx, gz, 5) for gx, gy, gz in golds]       # (x, z, r) : les anneaux d'or comptent comme des obstacles

    def ok(x, z, r):
        return all(math.hypot(x - a, z - b) > r + q + 9 for a, b, q in placed)

    def put(x, z, rs, rc, top):
        base = int(C.floor_y(path, x)) - 3
        hoodoo(w, strata, x, z, base, top, rs, rc)
        placed.append((x, z, rc))

    for rx, ry, rz, zone in rings[1:4]:
        for side in (-1, 1):
            x, z = rx + 6, rz + side * 19
            put(x, z, 2, 4, int(path.y(x)) + rnd.randint(2, 9))
    tries = 0
    while len(placed) < 44 + len(golds) and tries < 4000:
        tries += 1
        x = rnd.randint(90, 640) if rnd.random() < 0.8 else rnd.randint(640, 900)
        if any(abs(x - r[0]) < 10 for r in rings if r[3] in ('arch', 'viaduct')) or 540 < x < 580 or 880 < x < 904:
            continue
        hw = C.T.lerp_pts(C.HALFW, x)
        z = C.CZ + int(C.lat(x)) + rnd.randint(int(-hw + 10), int(hw - 10))
        rs = rnd.choice([1, 2, 2, 3])
        rc = rs + rnd.choice([2, 3])
        fl = int(C.floor_y(path, x))
        if 130 < x < 335 and rnd.random() < 0.6:        # zone du slalom : sommets proches de la trajectoire
            top = int(path.y(x)) + rnd.randint(-6, 12)
        else:
            top = min(fl + rnd.randint(22, 55), int(path.y(x)) - 16)
        if top - fl < 14 or not ok(x, z, rc) or near_path(x, z, rc, top, path):
            continue
        put(x, z, rs, rc, top)
    return placed


# ---------------------------------------------------------------- arches (portails de roche au-dessus du canyon)
def arch(w, path, x, cy, cz):
    """Aileron de roche en travers du canyon, epais de 12, perce d'un portail elliptique (largeur 34, couronne a cy+15)
    dans lequel s'inscrit l'anneau : piles de chaque cote, voute au-dessus."""
    a, b, y_top = 17.0, 14.0, cy + 27
    hw = C.T.lerp_pts(C.HALFW, x) + 8
    for i in range(w.nx):
        xc = w.cell_x(i) + 2
        if not x - 5 <= xc <= x + 6:
            continue
        for j in range(w.nz):
            zc = w.cell_z(j) + 2
            if abs(zc - C.CZ - C.lat(xc)) > hw:
                continue
            dz = zc - (cz + 0.5)
            if abs(dz) <= a:
                w.add(i, j, int(cy + 1 + b * math.sqrt(1 - (dz / a) ** 2)) + 2, y_top)
            elif w.top(i, j) < y_top:
                w.add(i, j, w.top(i, j), y_top)


def ridge(w, x, crest):
    """Crete triangulaire en travers du canyon (sommet plat de 8 blocs, flancs a 2,5 pour 1)."""
    for i in range(w.nx):
        xc = w.cell_x(i) + 2
        d = max(0, abs(xc - x) - 4)
        h = int(crest - 2.5 * d)
        for j in range(w.nz):
            if h > w.top(i, j):
                w.add(i, j, w.top(i, j), h)


# ---------------------------------------------------------------- viaduc ferroviaire
def viaduct(w, path, x, cy, cz):
    """Viaduc de pierre en travers du canyon (voie le long de z), l'anneau passe sous le tablier, entre deux piles."""
    yd = cy + 12
    hw = int(C.T.lerp_pts(C.HALFW, x)) + 6
    z1, z2 = C.CZ + int(C.lat(x)) - hw, C.CZ + int(C.lat(x)) + hw
    fl = int(C.floor_y(path, x)) - 3
    w.box(x - 3, yd, z1, x + 3, yd + 2, z2, 'stone_bricks')
    w.box(x - 3, yd - 2, z1, x + 3, yd - 1, z2, 'polished_andesite')
    w.box(x - 3, yd + 3, z1, x - 3, yd + 4, z2, 'stone_brick_wall', solid=False)
    w.box(x + 3, yd + 3, z1, x + 3, yd + 4, z2, 'stone_brick_wall', solid=False)
    w.box(x - 1, yd + 3, z1, x + 1, yd + 3, z2, 'gravel', solid=False)
    w.box(x, yd + 4, z1, x, yd + 4, z2, 'rail', solid=False)
    for n in range(4):
        for sgn in (-1, 1):
            pz = cz + sgn * (12 + 24 * n)
            if z1 <= pz <= z2:
                w.box(x - 2, fl, pz - 1, x + 2, yd - 3, pz + 1, 'stone_bricks')
    # train a l'arret : locomotive noire a cheminee, deux wagons
    w.box(x - 1, yd + 4, cz + 20, x + 1, yd + 7, cz + 29, 'black_concrete')
    w.box(x, yd + 8, cz + 27, x, yd + 10, cz + 27, 'black_concrete')
    w.box(x - 1, yd + 4, cz + 16, x + 1, yd + 8, cz + 19, 'brown_terracotta')
    w.box(x - 1, yd + 4, cz - 22, x + 1, yd + 7, cz - 12, 'red_terracotta')
    w.box(x - 1, yd + 4, cz - 36, x + 1, yd + 7, cz - 25, 'orange_terracotta')


# ---------------------------------------------------------------- depart
def start_area(w):
    """Plateforme de depart sur la mesa : dalle, garde-corps de verre sur trois cotes (le portillon est pose par le jeu)."""
    z1, z2 = C.CZ - 13, C.CZ + 13
    w.box(8, C.MESA, z1, C.EDGE_X - 1, C.MESA, z2, 'smooth_red_sandstone')
    w.box(10, C.MESA + 1, z1, C.GATE_X, C.MESA + 3, z1, 'white_stained_glass')
    w.box(10, C.MESA + 1, z2, C.GATE_X, C.MESA + 3, z2, 'white_stained_glass')
    w.box(10, C.MESA + 1, z1, 10, C.MESA + 3, z2, 'white_stained_glass')
    for dz in (-13, 13):
        w.box(C.GATE_X, C.MESA + 1, C.CZ + dz, C.GATE_X, C.MESA + 6, C.CZ + dz, 'oak_log')
