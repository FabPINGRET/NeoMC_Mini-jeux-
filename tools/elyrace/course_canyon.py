"""Parcours 1 de la Course d'elytras : Canyon du Couchant (Far West), ~1000 blocs de long.

Plongeon depuis la mesa de depart, slalom entre cheminees de fee, 3 arches etroites, viaduc ferroviaire et chevalet de
mine, passe basse, faille etroite, galerie de mine, descente dans la rue de la ville fantome. Parcours rapide : seule la
pente donne de la vitesse (les fusees freinent au-dessus de 1,7 b/tick). Ce module decrit le PARCOURS (profil, anneaux,
points de reprise, anneaux d'or) et le RELIEF ; les decors (cheminees, arches, viaduc, chevalet, ville) sont dans
props_canyon.py, la galerie de mine dans tunnel_canyon.py.

Methode : le profil d'altitude est derive d'un vol de reference simule (glide.Pilot) pour que chaque anneau soit
place sur une trajectoire physiquement realisable ; le relief est ensuite construit autour de cette trajectoire.
Python stdlib uniquement (compatible 3.8).
"""
import sys

import course_common as CC
import frames as F
import glide as G
import terrain as T

NUM = 1                                      # numero de parcours : dossier elyrace/c1/, drapeau de construction, bouton du menu
NAME = 'Canyon du Couchant'
ICON, COLOR, STARS = '🏜', 'gold', 3                      # bouton du menu : icone (menu texte), couleur, difficulte (etoiles sur 4)
TIP = ('Parcours 1 (Far West, ~1000 blocs) : plongeon, slalom entre cheminées de fée, arches étroites, viaduc, passe basse, '
       'faille, galerie de mine, rue de la ville fantôme.')
FLAG = 'v2'                                  # drapeau de construction (stockage mg:elyrace) : pose par la derniere tranche
CZ = 27000                                   # axe du parcours (z)
X0, X1 = -16, 1040                           # emprise en x (66 chunks)
Z0, Z1 = 26848, 27152                        # emprise en z (19 chunks)
MESA = 280                                   # surface de la mesa de depart (bloc) : les pieds sont a y 281
START_Y = MESA + 1                           # altitude des pieds sur la plateforme de depart
EDGE_X = 32                                  # bord de la falaise
GATE_X = 27                                  # portillon de depart (x), devant les joueurs
FRAME = 8                                    # demi-cote exterieur du cadre (17 x 17)
TV, TH = 6, 2                                # epaisseur de la coque : verticale (blocs), horizontale (cellules)
ROWS = 4                                     # lignes de joueurs sur la plateforme de depart
CLEAR_Y = (-10, 300)                         # hauteurs nettoyees (fill air, par passes) avant chaque tranche : un parcours reconstruit
                                             # sur une ancienne version n'en garde aucun reste

# profil d'altitude voulu de la trajectoire (x, y) ; le vol de reference le suit a quelques blocs pres
# profil « toboggan » : plongeon 1:2 au depart, pentes douces (1:7 a 1:10) qui gardent la vitesse, creux sous l'arche centrale,
# second toboggan 1:2 avant la passe basse, ralentissement doux a la sortie de la galerie, puis descente dans la rue
YPTS = [(24, 281), (110, 238), (154, 225), (250, 207), (320, 196), (345, 187), (385, 177), (405, 168), (450, 164), (505, 154),
        (625, 135), (670, 124), (700, 116), (760, 109), (820, 99), (900, 84), (960, 75), (990, 63), (1000, 61)]

# anneaux obligatoires : (x, decalage lateral, zone). L'altitude vient du vol de reference.
RINGS = [
    (130, 0, 'dive'), (165, 8, 'slalom'), (185, -8, 'slalom'), (220, 8, 'slalom'), (255, -8, 'slalom'), (290, 8, 'slalom'),
    (335, -6, 'arch'), (395, 8, 'arch'), (455, -8, 'arch'), (505, 0, 'gate'),
    (560, 0, 'viaduct'), (612, 8, 'trestle'), (650, 0, 'low'), (690, -6, 'low'),
    (735, -8, 'slot'), (770, 8, 'slot'), (805, -6, 'slot'), (855, 0, 'mine'),
    (915, 2, 'town'), (945, -2, 'town'), (970, 2, 'town'), (990, 0, 'town'),
]
CPS = [6, 10, 14, 19]                        # un point de reprise apres ces anneaux (numeros d'anneau)
GOLDS = [(355, -14), (576, -10), (888, 10)]   # anneaux d'or : (x, decalage lateral) ; altitude = trajectoire - GOLD_DY
GOLD_STRICT = True                           # verify.check_golds : detour >= 8 blocs hors de la ligne anneau a anneau, rampes limitees a la distance
# des anneaux voisins, vol qui finit le parcours et franchit tous les anneaux proches. Il faut ~26 blocs avant l'anneau suivant pour
# revenir et un decalage >= 9 pour ne pas frotter l'enveloppe des vols a +-3 : (355, -14) arches, (576, -10) viaduc, (888, +10) sortie de la
# galerie ; la ville (anneaux a 25-30 blocs) et le reste de la faille ne laissent aucune place a un or
GOLD_DY = 2                                  # les anneaux d'or sont GOLD_DY blocs sous la trajectoire (le detour vole plus bas, voir course_blanc)
RING_LOW = 0.5                               # les trous sont RING_LOW bloc sous la trajectoire : sur une pente forte le pilote a anticipation courte
                                             # (detour vers un anneau d'or) vole plus bas et touchait le bas du cadre
WINDS = []                                   # anneaux de vent : aucun sur ce parcours
R_UP = {n: 28 for n in CPS}                  # hauteur de reapparition au-dessus du centre de l'anneau de chaque point de reprise
R_UP[19] = 26                                # apres l'anneau 19 le suivant est a 30 blocs : 28 rate au delai de chute de verify (RESPAWN_DELAY), 26 passe


def ydes(x):
    return T.lerp_pts(YPTS, x)


def lat(x):
    """Decalage lateral de la trajectoire (z - CZ) : polyligne passant par les anneaux."""
    pts = [(24, 0)] + [(r[0], r[1]) for r in RINGS]
    return T.smooth_pts(pts, x)


def reference_waypoints(step=12):
    """Points de passage du vol de reference : le profil voulu, un point tous les `step` blocs."""
    xs = list(range(60, 1000, step)) + [R[0] for R in RINGS]
    return [(x, ydes(x), CZ + lat(x) + 0.5) for x in sorted(set(xs))]


def start_state():
    """Etat du joueur qui saute de la mesa : il a couru jusqu'au bord, chute 8 ticks avant d'ouvrir ses elytres."""
    return G.State(EDGE_X + 0.3, START_Y, CZ + 0.5, 0.28, 0.0, 0.0)


# ---------------------------------------------------------------- relief
PALETTE = ['red_terracotta', 'orange_terracotta', 'terracotta', 'yellow_terracotta', 'white_terracotta',
           'brown_terracotta', 'light_gray_terracotta', 'red_sandstone', 'granite']
TOWN_Y = 60                                  # sol de la ville fantome (bloc)
HALFW = [(0, 60), (300, 55), (450, 50), (520, 56), (610, 52), (640, 34), (665, 30), (695, 30), (715, 12), (885, 12),
         (905, 30), (930, 55), (950, 80), (1040, 95)]
Q = 3                                        # quantification des hauteurs : terrasses de 3 blocs
# tables par abscisse (meme modele que course_blanc) : profondeur du fond sous la trajectoire, pente des parois (blocs de
# hauteur par bloc horizontal), amplitude du bruit. Passe basse (640-700) : fond remonte a 14 blocs sous la trajectoire ;
# faille (715-820) : parois a 8 pour 1 ; galerie de mine (825-885) : fond a tunnel_canyon.DOWN, parois lisses.
DEPTH = [(0, 78), (580, 78), (640, 14), (700, 14), (715, 22), (820, 22), (825, 11), (885, 11), (930, 27), (1140, 27)]
SLOPE = [(0, 2.2), (695, 2.2), (715, 8), (885, 8), (905, 2.2), (1140, 2.2)]
NOISE = [(0, 1.0), (600, 1.0), (640, 0.3), (700, 0.3), (715, 0.2), (820, 0.2), (825, 0.0), (885, 0.0), (905, 1.0), (1140, 1.0)]
TOWN_X, TOWN_W = 900, 40                     # le fond remonte vers la rue (TOWN_Y) entre TOWN_X et TOWN_X + TOWN_W


def floor_y(path, x):
    base = path.y(x) - T.lerp_pts(DEPTH, x)
    t = T.smooth((x - TOWN_X) / float(TOWN_W))
    return base * (1 - t) + TOWN_Y * t


def plateau_y(path, x):
    return min(MESA, path.y(x) + 50)


def relief(path):
    """Cree le World et y pose le relief : mesa, canyon, parois en terrasses, plateau."""
    nx, nz = (X1 - X0) // T.S, (Z1 - Z0) // T.S
    w = T.World(X0, Z0, nx, nz)
    for i in range(nx):
        xc = w.cell_x(i) + 2
        for j in range(nz):
            zc = w.cell_z(j) + 2
            if xc < EDGE_X:
                h = MESA
            else:
                amp = T.lerp_pts(NOISE, xc)
                u = abs(zc - CZ - lat(xc)) + 7 * amp * T.fbm(xc, zc, 11, 3, 40.0)
                d = u - T.lerp_pts(HALFW, xc)
                town = T.smooth((xc - TOWN_X) / float(TOWN_W))
                fl = floor_y(path, xc) + 2.5 * amp * (T.fbm(xc, zc, 5, 3, 30.0) + 1) * (1 - town)
                top = plateau_y(path, xc) + 4 * amp * (T.fbm(xc, zc, 23, 3, 70.0) + 1)
                h = fl if d <= 0 else min(top, fl + d * T.lerp_pts(SLOPE, xc) + 3 * amp * T.fbm(xc, zc, 31, 2, 20.0))
            w.ground(i, j, Q * round(h / Q))
    return w


def extra_checks(c):
    """Controles propres au Canyon : tout ce qui est construit tient dans la zone nettoyee CLEAR_Y, lumiere de la galerie de mine."""
    import tunnel_canyon as TN
    bad = []
    ys = [y for r in c.rects for y in (r[1], r[4])]
    for cmd in c.world.cmds:
        ys += [cmd[2]] if cmd[0] == 'set' else [cmd[2], cmd[5]]
    if min(ys) < CLEAR_Y[0] or max(ys) > CLEAR_Y[1]:
        bad.append('construction hors de la zone nettoyee CLEAR_Y %s : y %d..%d' % (CLEAR_Y, min(ys), max(ys)))
    return bad + TN.light_problems(c.world)


def build():
    """Construit le parcours complet (relief, decors, anneaux). Retourne un Course."""
    import props_canyon as P
    import town_canyon as TW
    import tunnel_canyon as TN
    me = sys.modules[__name__]
    c = CC.Course(me)
    c.rings, c.trace = CC.reference(c.spec)
    low = [(t[0], t[1] - RING_LOW) + tuple(t[2:]) for t in c.trace]       # trou centre RING_LOW bloc sous la trajectoire
    c.rings = [(x, CC.interp_yz(low, x)[0], cz, zone) for x, cy, cz, zone in c.rings]
    c.path = CC.Path(c.trace)
    c.strata = T.make_strata(7, PALETTE)
    w = c.world = relief(c.path)
    for x, cy, cz, zone in c.rings:
        if zone == 'arch':
            P.arch(w, c.path, x, cy, cz)
    TN.roof(w, c.path, me)
    c.rects = w.rects(w.shell(TV, TH), c.strata, 0)
    for gx, off in GOLDS:
        c.golds.append((gx, int(round(c.path.y(gx))) - GOLD_DY, CZ + int(round(lat(gx))) + off))
    P.start_area(w)
    P.hoodoos(w, c.strata, c.path, c.rings, c.golds)
    for x, cy, cz, zone in c.rings:
        if zone == 'viaduct':
            P.viaduct(w, c.path, x, cy, cz)
        elif zone == 'trestle':
            P.trestle(w, c.path, x, cy, cz)
    TW.town(w)
    TN.supports(w, c.path, me, [r[0] for r in c.rings], [g[0] for g in c.golds])
    for n, (x, cy, cz, zone) in enumerate(c.rings, 1):
        F.ring_frame(w, x, cy, cz, 'finish' if n == len(c.rings) else 'ring')
    c.cps = list(CPS)
    for gx, gy, gz in c.golds:
        F.gold_frame(w, gx, gy, gz)
    for n in CPS:
        x, cy, cz, zone = c.rings[n - 1]
        F.cp_gate(w, x, cy, cz)
    TN.place_lights(w, c.path, me)                         # en dernier : apres tous les cadres (ils effaceraient les lumieres)
    for r in range(ROWS * 4):                              # places de depart : deux rangees de 8 (16 places)
        c.places.append((GATE_X - 2 - 4 * (r // 8), CZ - 10 + 3 * (r % 8)))
    return c
