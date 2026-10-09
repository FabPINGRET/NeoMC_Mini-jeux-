"""Galerie de mine du Canyon du Couchant (section G) : voute au-dessus de la faille, cadres de bois, lumieres et controle
de l'eclairage. Meme methode que la grotte du Pic Blanc (cave_blanc.py) : un plafond a UP blocs au-dessus de la trajectoire,
des blocs `light` sur un reseau tous les LIGHT_STEP blocs, completes jusqu'a ce que chaque bloc d'air de la galerie soit
eclaire (niveau >= 1 : pas de monstre). CV.air_voxels voit toutes les cellules a deux intervalles du monde (les arches
aussi) : on ne garde que l'emprise de la galerie.
Python stdlib uniquement (compatible 3.8).
"""
import math

import cave_blanc as CV
import terrain as T

X_T0, X_T1 = 824, 887            # emprise de la galerie (x) : cellules entieres de 4 blocs
UP = 9                           # plafond au-dessus de la trajectoire
DOWN = 11                        # plancher au-dessous de la trajectoire (table DEPTH de course_canyon a cet endroit)
SEAL = 8                         # cellules voisines de la faille relevees jusqu'au dessus de la montagne (galerie close)
SUP_STEP = 12                    # espacement des cadres de bois
POST = 10                        # decalage lateral des poteaux (la faille fait 12 de demi-largeur)
LIGHT_STEP = 8                   # espacement du reseau de lumieres


def roof(w, path, spec):
    """Voute : pour chaque cellule de la faille entre X_T0 et X_T1, plancher et plafond arrondis a 3 blocs, dessus de montagne ;
    les cellules voisines sont relevees jusqu'au dessus (parois verticales : aucune ouverture sur le cote)."""
    for i in range(w.nx):
        x0 = w.cell_x(i)
        if x0 < X_T0 or x0 + T.S - 1 > X_T1:
            continue
        xs = range(x0, x0 + T.S)
        ceil = 3 * int(math.ceil(max(path.y(x) + UP for x in xs) / 3.0))            # arrondis a 3 blocs, vers la marge
        floor = 3 * int(math.floor(min(path.y(x) - DOWN for x in xs) / 3.0))
        for j in range(w.nz):
            xc, zc = x0 + 2, w.cell_z(j) + 2
            d = abs(zc - spec.CZ - spec.lat(xc)) - T.lerp_pts(spec.HALFW, xc)
            top = max(3 * int(round(spec.plateau_y(path, xc) / 3.0)), ceil + 4)
            if d <= 0:
                w.cells[i][j] = [[-T.BIG, min(floor, w.top(i, j))], [ceil, top]]
            elif d <= SEAL:
                w.cells[i][j] = [[-T.BIG, max(w.top(i, j), top)]]


def supports(w, path, spec, avoid_x, gold_xs=()):
    """Cadres de bois (deux poteaux, une poutre sous le plafond, lanterne accrochee) : au portail d'entree (X_T0), tous les SUP_STEP
    blocs jusqu'a X_T1 - 7, et au portail de sortie (X_T1 - 1) ; sauf pres d'un anneau (`avoid_x` : de x - 3 a x + 4) et dans la
    fenetre d'un anneau d'or (de gx - 10 a gx + 8, `gold_xs`) : le detour de l'or passe par la, un cadre l'y bloquerait.
    Sur le Canyon, l'or en x 888 (fenetre 878..896) retire donc le cadre de x 886 (portail de sortie)."""
    for x in list(range(X_T0, X_T1 - 6, SUP_STEP)) + [X_T1 - 1]:
        if any(a - 3 <= x <= a + 4 for a in avoid_x) or any(g - 10 <= x <= g + 8 for g in gold_xs):
            continue
        cz = spec.CZ + int(round(spec.lat(x)))
        i, j = w.ij(x, cz)
        floor, ceil = w.cells[i][j][0][1], w.cells[i][j][1][0]
        for dz in (-POST, POST):
            w.box(x, floor + 1, cz + dz, x, ceil - 1, cz + dz, 'stripped_oak_log')
        w.box(x, ceil - 1, cz - POST, x, ceil - 1, cz + POST, 'dark_oak_planks')
        w.block(x, ceil - 2, cz, 'lantern[hanging=true]')


def air(w):
    """Blocs d'air de la galerie (voir CV.air_voxels), restreints a X_T0..X_T1."""
    return {p for p in CV.air_voxels(w) if X_T0 <= p[0] <= X_T1}


def place_lights(w, path, spec):
    """Reseau de lumieres (tous les LIGHT_STEP blocs, 3 en travers, 2 en hauteur) puis completion : renvoie le nombre de lumieres."""
    free = air(w)
    levels, srcs = {}, []
    for x in range(X_T0 + LIGHT_STEP // 2, X_T1, LIGHT_STEP):
        for dz in (-8, 0, 8):
            for dy in (-6, 6):
                p = (x, int(round(path.y(x))) + dy, spec.CZ + int(round(spec.lat(x))) + dz)
                if p in free:
                    srcs.append(p)
    for p in srcs:
        CV.spread(levels, free, p)
    for p in sorted(free):                                   # completion deterministe : tout bloc encore sombre devient une source
        if levels.get(p, 0) < 1:
            srcs.append(p)
            CV.spread(levels, free, p)
    for (x, y, z) in srcs:
        w.block(x, y, z, CV.LIGHT)
    return len(srcs)


def light_problems(w):
    """Controle independant de la generation : relit les blocs light poses et verifie niveau >= 1 dans tout l'air de la galerie."""
    free = air(w)
    levels, bad = {}, []
    for cmd in w.cmds:
        if cmd[0] == 'set' and cmd[4] == CV.LIGHT and X_T0 <= cmd[1] <= X_T1:
            if cmd[1:4] not in free:
                bad.append('galerie : bloc light hors de l\'air en %s' % (cmd[1:4],))
            else:
                CV.spread(levels, free, cmd[1:4])
    dark = [p for p in free if levels.get(p, 0) < 1]
    if dark:
        bad.append('galerie : %d blocs d\'air sans lumiere (ex. %s)' % (len(dark), min(dark)))
    return bad
