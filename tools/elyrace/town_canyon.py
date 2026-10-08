"""Ville fantome du Canyon du Couchant (arrivee) : rue le long de x, facades a faux-front, eglise, chateau d'eau.
Les batiments sont pleins (pas d'interieur) : ils ne servent que de decor et de relief pour les derniers anneaux.
Python stdlib uniquement (compatible 3.8).
"""
import course_canyon as C


def house(w, x1, z1, x2, z2, h, wall, roof, front):
    """Batiment plein de h blocs : murs, toit plat debordant, faux-front de 3 blocs cote rue, porte et fenetres peintes.
    `front` = -1 si la rue est du cote z croissant, +1 si elle est du cote z decroissant."""
    y0 = C.TOWN_Y + 1
    w.box(x1, y0, z1, x2, y0 + h - 1, z2, wall)
    w.box(x1 - 1, y0 + h, z1 - 1, x2 + 1, y0 + h, z2 + 1, roof)
    zf = z2 if front < 0 else z1                       # facade cote rue
    w.box(x1, y0 + h + 1, zf, x2, y0 + h + 3, zf, wall)
    zr = zf + (1 if front < 0 else -1)                 # rangee juste devant la facade
    mid = (x1 + x2) // 2
    w.box(mid, y0, zr, mid + 1, y0 + 1, zr, 'dark_oak_planks')
    for wx in (x1 + 2, x2 - 3):
        if x2 - x1 > 6:
            w.box(wx, y0 + 2, zr, wx + 1, y0 + 3, zr, 'glass')
    w.box(x1, y0 + 4, zr, x2, y0 + 4, zr, 'dark_oak_slab', solid=False)   # auvent


def town(w):
    """Pose la ville : sol de la rue, batiments des deux cotes, eglise a clocher, chateau d'eau."""
    cz, y0 = C.CZ, C.TOWN_Y
    w.box(930, y0, cz - 9, 1039, y0, cz + 9, 'coarse_dirt')
    w.box(930, y0, cz - 1, 1039, y0, cz + 1, 'terracotta')
    # cote nord (z decroissant), facades tournees vers la rue
    house(w, 940, cz - 26, 958, cz - 12, 11, 'spruce_planks', 'dark_oak_planks', -1)
    house(w, 962, cz - 24, 974, cz - 12, 9, 'bricks', 'stone_brick_slab', -1)
    house(w, 980, cz - 22, 990, cz - 12, 8, 'oak_planks', 'dark_oak_planks', -1)
    # cote sud (z croissant)
    house(w, 946, cz + 12, 958, cz + 22, 8, 'oak_planks', 'dark_oak_planks', 1)
    house(w, 964, cz + 12, 980, cz + 28, 14, 'white_terracotta', 'dark_oak_planks', 1)
    house(w, 986, cz + 12, 996, cz + 20, 7, 'spruce_planks', 'dark_oak_planks', 1)
    # eglise : nef + clocher + fleche
    house(w, 1004, cz - 30, 1018, cz - 14, 12, 'white_concrete', 'dark_oak_planks', -1)
    w.box(1004, y0 + 13, cz - 30, 1008, y0 + 30, cz - 26, 'white_concrete')
    w.box(1005, y0 + 31, cz - 29, 1007, y0 + 33, cz - 27, 'dark_oak_planks')
    w.box(1006, y0 + 34, cz - 28, 1006, y0 + 38, cz - 28, 'dark_oak_fence', solid=False)
    # chateau d'eau sur pilotis
    for dx in (-2, 2):
        for dz in (-2, 2):
            w.box(1002 + dx, y0 + 1, cz + 30 + dz, 1002 + dx, y0 + 18, cz + 30 + dz, 'oak_log')
    w.box(999, y0 + 19, cz + 27, 1005, y0 + 24, cz + 33, 'spruce_planks')
    w.box(1000, y0 + 25, cz + 28, 1004, y0 + 25, cz + 32, 'dark_oak_planks')
    # barrieres de licol le long de la rue
    for x in range(942, 1000, 8):
        w.box(x, y0 + 1, cz - 8, x, y0 + 2, cz - 8, 'oak_fence', solid=False)
        w.box(x, y0 + 1, cz + 8, x, y0 + 2, cz + 8, 'oak_fence', solid=False)
