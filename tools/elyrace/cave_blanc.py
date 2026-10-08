"""Grotte de glace du Pic Blanc : voute au-dessus de la vallee, stalactites, lumieres et controle de l'eclairage.

La vallee (relief de course_blanc.py) est une gorge etroite aux parois verticales ; ici on lui pose un plafond (voute) :
4 blocs de large par cellule, plancher et plafond arrondis a 3 blocs de maniere a garder CLEAR blocs libres autour de la
trajectoire. Aucune source de lumiere naturelle sous la voute : des blocs `light` sont poses sur un reseau tous les
LIGHT_STEP blocs, puis completes jusqu'a ce que chaque bloc d'air sous la voute soit eclaire (niveau >= 1 : pas de monstre).
Python stdlib uniquement (compatible 3.8).
"""
import math
import random

import terrain as T

X_ROOF0, X_ROOF1 = 800, 1003     # emprise de la voute, bouche (descente du plafond) et sortie comprises
FULL0, FULL1 = 826, 975          # tunnel de pleine section
HW = 12                          # demi-largeur du tunnel (blocs)
CLEAR = 11                       # blocs libres au-dessus et au-dessous de la trajectoire
WALL_TOP = 35                    # hauteur des parois (et du dessus de la montagne) au-dessus de la trajectoire
LIGHT = 'light[level=11]'
LIGHT_LEVEL = 11
LIGHT_STEP = 8                   # espacement du reseau de lumieres le long du tunnel
STALA_MAX = 3                    # longueur maximale d'une stalactite ; sa pointe reste a >= STALA_CLEAR au-dessus de la trajectoire
STALA_CLEAR = 8
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def hill(x, dz):
    """Bosse de montagne au-dessus de la grotte (blocs ajoutes a la hauteur des parois)."""
    return 25 * T.smooth(1 - abs(dz) / 80.0) * T.smooth((x - 770) / 40.0) * T.smooth((1010 - x) / 40.0)


def roof_off(x):
    """Hauteur du plafond au-dessus de la trajectoire : descend a CLEAR dans la bouche, remonte a la sortie."""
    t = max(1 - T.smooth((x - X_ROOF0) / float(FULL0 - X_ROOF0)), T.smooth((x - FULL1) / float(X_ROOF1 - FULL1)))
    return CLEAR + (WALL_TOP - CLEAR) * t


def roof(w, path, spec):
    """Voute : pour chaque cellule de la vallee entre X_ROOF0 et X_ROOF1, plancher et plafond arrondis, dessus de montagne."""
    for i in range(w.nx):
        x0 = w.cell_x(i)
        if x0 + T.S <= X_ROOF0 or x0 > X_ROOF1:
            continue
        xs = range(x0, x0 + T.S)
        ceil = 3 * int(math.ceil(max(path.y(x) + roof_off(x) for x in xs) / 3.0))            # arrondis a 3 blocs, vers la marge
        floor = 3 * int(math.floor(min(path.y(x) - CLEAR for x in xs) / 3.0))
        for j in range(w.nz):
            xc, zc = x0 + 2, w.cell_z(j) + 2
            if abs(zc - spec.CZ - spec.lat(xc)) > spec.halfw(xc):
                continue
            top = max(spec.top_y(path, xc, zc), ceil + 4)
            if top - ceil < 3:
                continue
            w.cells[i][j] = [[-T.BIG, min(floor, w.top(i, j))], [ceil, top]]


def ceil_at(w, x, z):
    i, j = w.ij(x, z)
    iv = w.cells[i][j]
    return iv[1][0] if len(iv) == 2 else None


def stalactites(w, path, spec, avoid_x, seed=5):
    """Quelques stalactites de packed_ice (jamais de glace simple) : <= STALA_MAX blocs, pointe >= STALA_CLEAR au-dessus du chemin."""
    rnd = random.Random(seed)
    n = 0
    for _ in range(120):
        x = rnd.randrange(FULL0 + 2, FULL1 - 2)
        z = spec.CZ + int(round(spec.lat(x))) + rnd.randrange(-HW + 1, HW)
        if any(ax - 2 <= x <= ax + 3 for ax in avoid_x):
            continue
        ceil = ceil_at(w, x, z)
        if ceil is None:
            continue
        low = int(max(path.y(x - 1), path.y(x), path.y(x + 1))) + STALA_CLEAR
        length = min(rnd.choice([1, 2, 2, 3]), STALA_MAX, ceil - low)
        if length >= 1:
            w.box(x, ceil - length, z, x, ceil - 1, z, 'packed_ice')
            n += 1
    return n


def air_voxels(w):
    """Blocs d'air sous la voute (cellules a deux intervalles : sol et plafond) moins les blocs ajoutes (stalactites...)."""
    out = set()
    for i in range(w.nx):
        for j in range(w.nz):
            iv = w.cells[i][j]
            if len(iv) != 2:
                continue
            x0, z0 = w.cell_x(i), w.cell_z(j)
            for y in range(iv[0][1] + 1, iv[1][0]):
                for x in range(x0, x0 + T.S):
                    for z in range(z0, z0 + T.S):
                        if (x, y, z) not in w.vox:
                            out.add((x, y, z))
    return out


def spread(levels, air, src, level=LIGHT_LEVEL):
    """Propage la lumiere depuis `src` (parcours en largeur, -1 par bloc, seulement dans l'air) en ne gardant que les ameliorations."""
    if levels.get(src, 0) >= level:
        return
    levels[src] = level
    frontier = [src]
    while frontier:
        nxt = []
        for (x, y, z) in frontier:
            lv = levels[(x, y, z)] - 1
            if lv < 1:
                continue
            for dx, dy, dz in NEIGH:
                p = (x + dx, y + dy, z + dz)
                if p in air and levels.get(p, 0) < lv:
                    levels[p] = lv
                    nxt.append(p)
        frontier = nxt


def place_lights(w, path, spec):
    """Reseau de lumieres (tous les LIGHT_STEP blocs, 3 en travers, 2 en hauteur) puis completion : renvoie le nombre de lumieres."""
    air = air_voxels(w)
    levels, srcs = {}, []
    for x in range(X_ROOF0 + LIGHT_STEP, X_ROOF1, LIGHT_STEP):
        for dz in (-8, 0, 8):
            for dy in (-6, 6):
                p = (x, int(round(path.y(x))) + dy, spec.CZ + int(round(spec.lat(x))) + dz)
                if p in air:
                    srcs.append(p)
    for p in srcs:
        spread(levels, air, p)
    for p in sorted(air):                                    # completion deterministe : tout bloc encore sombre devient une source
        if levels.get(p, 0) < 1:
            srcs.append(p)
            spread(levels, air, p)
    for (x, y, z) in srcs:
        w.block(x, y, z, LIGHT)
    return len(srcs)


def light_problems(w):
    """Controle independant de la generation : relit les blocs light poses et verifie niveau >= 1 dans tout l'air sous la voute."""
    air = air_voxels(w)
    levels, bad = {}, []
    for cmd in w.cmds:
        if cmd[0] == 'set' and cmd[4] == LIGHT:
            if cmd[1:4] not in air:
                bad.append('grotte : bloc light hors de l\'air en %s' % (cmd[1:4],))
            else:
                spread(levels, air, cmd[1:4])
    dark = [p for p in air if levels.get(p, 0) < 1]
    if dark:
        bad.append('grotte : %d blocs d\'air sans lumiere (ex. %s)' % (len(dark), min(dark)))
    return bad
