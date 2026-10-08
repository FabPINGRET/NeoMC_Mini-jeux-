"""Decors du Pic Blanc : gare du sommet, telepherique (pylones, cable, cabines, gare intermediaire), seracs, village
et gare d'arrivee. (Les cadres des anneaux et des portiques sont dans frames.py, la grotte dans cave_blanc.py.)
Tout ce qui est solide est enregistre dans le World pour que le pilote automatique le voie. Le cable court a
CABLE_DZ blocs de l'axe et a CABLE_UP blocs au-dessus de la trajectoire : jamais dans la colonne de reapparition.
Python stdlib uniquement (compatible 3.8).
"""
import random

import course_blanc as C

CABLE_DZ = 22                                # decalage lateral du cable par rapport a l'axe (z)
CABLE_UP = 14                                # hauteur du cable au-dessus de la trajectoire (>= 12)
PYLONS = [60, 120, 180, 240, 300]            # abscisses des pylones
MID_X = 330                                  # gare intermediaire (fin du cable)
BAR = 'iron_bars'                            # cable et suspentes (barres : lisibles de loin, enregistrees pleines)


def ground_at(w, x, z):
    i, j = w.ij(x, z)
    return w.top(i, j)


def hollow(w, x1, y1, z1, x2, y2, z2, wall, roof=None):
    """Salle : coque pleine `wall`, interieur vide, toit `roof` (ou `wall`)."""
    w.box(x1, y1, z1, x2, y2, z2, wall)
    w.box(x1 + 1, y1 + 1, z1 + 1, x2 - 1, y2 - 1, z2 - 1, 'air')
    w.box(x1, y2, z1, x2, y2, z2, roof or wall)


# ---------------------------------------------------------------- sommet
def start_area(w):
    """Plateforme de depart au sommet : dalle, garde-corps de verre sur trois cotes, poteaux du portillon."""
    z1, z2 = C.CZ - 13, C.CZ + 13
    s = C.SUMMIT
    w.box(8, s, z1, C.EDGE_X - 1, s, z2, 'smooth_stone')
    w.box(10, s + 1, z1, C.GATE_X, s + 3, z1, 'white_stained_glass')
    w.box(10, s + 1, z2, C.GATE_X, s + 3, z2, 'white_stained_glass')
    w.box(10, s + 1, z1, 10, s + 3, z2, 'white_stained_glass')
    for dz in (-13, 13):
        w.box(C.GATE_X, s + 1, C.CZ + dz, C.GATE_X, s + 6, C.CZ + dz, 'oak_log')


def summit_station(w, path):
    """Gare du telepherique derriere la plateforme : salle ouverte du cote du depart, tour d'ancrage du cable."""
    s, z = C.SUMMIT, C.CZ
    hollow(w, -12, s, z - 12, 4, s + 8, z + 12, 'stone_bricks', 'spruce_planks')
    w.box(3, s + 1, z - 6, 4, s + 5, z + 6, 'air')                         # grande porte vers la plateforme
    for dz in (-12, 12):
        w.box(-8, s + 3, z + dz, 0, s + 5, z + dz, 'light_blue_stained_glass')
    top = cable_y(path, -8) - 1
    w.box(-8, s + 1, z + CABLE_DZ - 1, -7, top, z + CABLE_DZ, 'gray_concrete')            # tour d'ancrage
    w.box(-8, top, z + CABLE_DZ - 2, -7, top, z + CABLE_DZ + 2, 'gray_concrete')


# ---------------------------------------------------------------- telepherique
def cable_y(path, x):
    return int(round(path.y(x))) + CABLE_UP


def cable(w, path, x0, x1):
    """Cable en barres de fer le long de la pente : une boite par palier de hauteur."""
    z = C.CZ + CABLE_DZ
    a = x0
    for x in range(x0 + 1, x1 + 2):
        if x > x1 or cable_y(path, x) != cable_y(path, a):
            w.box(a, cable_y(path, a), z, x - 1, cable_y(path, a), z, BAR)
            a = x


def pylon(w, path, x):
    """Pylone : fut de 2 x 2 depuis le sol jusqu'au cable, traverse et suspente."""
    z = C.CZ + CABLE_DZ
    y = cable_y(path, x)
    g = ground_at(w, x, z)
    w.box(x, g, z - 1, x + 1, y, z, 'gray_concrete')
    w.box(x - 1, y - 2, z - 3, x + 2, y - 2, z + 2, 'gray_concrete')
    w.box(x, y + 1, z - 1, x + 1, y + 1, z, 'gray_concrete')


def cabin(w, path, x):
    """Cabine suspendue au cable : 5 x 3 x 3, vitree sur les cotes, suspente en barres."""
    z = C.CZ + CABLE_DZ
    y = cable_y(path, x + 2) - 5
    w.box(x, y, z - 1, x + 4, y + 2, z + 1, 'red_concrete')
    w.box(x + 1, y + 1, z - 1, x + 3, y + 1, z - 1, 'light_blue_stained_glass')
    w.box(x + 1, y + 1, z + 1, x + 3, y + 1, z + 1, 'light_blue_stained_glass')
    w.box(x + 2, y + 3, z, x + 2, y + 4, z, BAR)


def mid_station(w, path):
    """Gare intermediaire : tour pleine depuis le sol, salle au niveau du cable."""
    z = C.CZ + CABLE_DZ
    y = cable_y(path, MID_X)
    g = ground_at(w, MID_X, z)
    w.box(MID_X - 1, g, z - 1, MID_X + 1, y - 4, z + 1, 'gray_concrete')
    hollow(w, MID_X - 3, y - 3, z - 3, MID_X + 3, y + 2, z + 3, 'spruce_planks', 'dark_oak_planks')


def telepherique(w, path):
    cable(w, path, -8, MID_X - 3)
    for x in PYLONS:
        pylon(w, path, x)
    for x in (150, 250):
        cabin(w, path, x)
    mid_station(w, path)


# ---------------------------------------------------------------- seracs
def seracs(w, path):
    """Tours de glace hors de la trajectoire (>= 18 blocs de l'axe) : glacier avant la crevasse et champ de glace."""
    rnd = random.Random(17)
    for lo, hi, n in ((440, 515, 7), (735, 800, 6)):
        for _ in range(n):
            x = rnd.randrange(lo, hi)
            dz = rnd.randrange(18, int(C.halfw(x)) - 6) * rnd.choice((-1, 1))
            z = C.CZ + int(round(C.lat(x))) + dz
            s, h = rnd.choice((2, 3, 4)), rnd.randrange(10, 28)
            g = min(ground_at(w, x + a, z + b) for a in (0, s) for b in (0, s))
            w.box(x, g - 1, z, x + s, g + h, z + s, 'packed_ice')
            w.box(x, g + h - 3, z, x + s, g + h, z + s, 'blue_ice')


# ---------------------------------------------------------------- village
def chalet(w, x, z):
    """Chalet de 7 x 7 : fondations jusqu'au sol, murs de sapin, fenetre, porte, toit en gradins sous la neige."""
    cells = [ground_at(w, x + a, z + b) for a in (-4, 0, 4) for b in (-4, 0, 4)]
    base = max(cells)
    w.box(x - 3, min(cells) - 2, z - 3, x + 3, base, z + 3, 'stone_bricks')
    hollow(w, x - 3, base, z - 3, x + 3, base + 4, z + 3, 'spruce_planks', 'dark_oak_planks')
    w.box(x - 1, base + 2, z - 3, x + 1, base + 3, z - 3, 'glass_pane')
    w.box(x, base + 1, z + 3, x, base + 2, z + 3, 'air')
    for k, r in enumerate((4, 3, 2, 1)):
        w.box(x - r, base + 4 + k, z - r, x + r, base + 4 + k, z + r, 'dark_oak_planks' if k < 3 else 'snow_block')


def village(w):
    for side in (-1, 1):
        for n, x in enumerate((1028, 1058, 1086, 1110)):
            chalet(w, x, C.CZ + side * (26 + 6 * (n % 2)))
    z = C.CZ
    g = max(ground_at(w, 1124, z + dz) for dz in (-9, 0, 9))
    hollow(w, 1119, g, z - 10, 1133, g + 7, z + 10, 'white_concrete', 'lime_concrete')
    w.box(1119, g + 1, z - 4, 1119, g + 4, z + 4, 'air')                    # arcade vers l'arrivee des joueurs


def gate_feet(w, x, cy, cz):
    """Pieds des colonnes d'un portique de reprise : descendent jusqu'au sol (sinon elles flotteraient)."""
    for dz in (-12, 11):
        g = ground_at(w, x + 4, cz + dz)
        if cy - 17 > g:
            w.box(x + 4, g + 1, cz + dz, x + 5, cy - 17, cz + dz + 1, 'packed_ice')


def props(c):
    w = c.world
    start_area(w)
    summit_station(w, c.path)
    telepherique(w, c.path)
    seracs(w, c.path)
    village(w)
