"""Parcours 1 de la Course d'elytras : Canyon du Couchant (Far West), ~1000 blocs de long.

Mesa de depart, slalom entre cheminees de fee, 3 arches, viaduc ferroviaire, gorge en S, crete a franchir en
montee (fusees utiles), ville fantome. Ce module decrit le PARCOURS (profil, anneaux, points de reprise, anneaux
d'or) et le RELIEF ; les decors (cheminees, arches, viaduc, ville) sont dans props_canyon.py.

Methode : le profil d'altitude est derive d'un vol de reference simule (glide.Pilot) pour que chaque anneau soit
place sur une trajectoire physiquement realisable ; le relief est ensuite construit autour de cette trajectoire.
Python stdlib uniquement (compatible 3.8).
"""
import math

import glide as G
import terrain as T

KEY = 'canyon'
CZ = 27000                                   # axe du parcours (z)
X0, X1 = -16, 1040                           # emprise en x (66 chunks)
Z0, Z1 = 26848, 27152                        # emprise en z (19 chunks)
MESA = 250                                   # surface de la mesa de depart (bloc) : les pieds sont a y 251
EDGE_X = 32                                  # bord de la falaise
GATE_X = 27                                  # portillon de depart (x), devant les joueurs
HOLE = 9                                     # trou des anneaux : 9 x 9
FRAME = 8                                    # demi-cote exterieur du cadre (17 x 17)
TV, TH = 6, 2                                # epaisseur de la coque : verticale (blocs), horizontale (cellules)
ROWS = 4                                     # lignes de joueurs sur la plateforme de depart

# profil d'altitude voulu de la trajectoire (x, y) ; le vol de reference le suit a quelques blocs pres
YPTS = [(24, 250), (110, 222), (330, 190), (520, 160), (680, 135), (760, 118), (820, 112), (900, 106), (1000, 84)]

# anneaux obligatoires : (x, decalage lateral, zone). L'altitude vient du vol de reference.
RINGS = [
    (110, 0, 'dive'), (170, 14, 'slalom'), (225, -14, 'slalom'), (280, 12, 'slalom'),
    (335, -6, 'arch'), (395, 8, 'arch'), (455, -8, 'arch'), (505, 0, 'gate'),
    (560, 0, 'viaduct'), (612, 10, 'viaduct'), (665, 0, 'gorge'), (715, -13, 'gorge'),
    (765, 13, 'gorge'), (815, -12, 'gorge'), (868, 0, 'climb'), (915, 10, 'climb'),
    (950, -8, 'town'), (985, 0, 'town'),
]
CPS = [4, 8, 12, 15]                         # un point de reprise apres ces anneaux (numeros d'anneau)
GOLDS = [(481, 9), (638, -9), (842, 9)]   # anneaux d'or : (x, decalage lateral) ; altitude = trajectoire


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
    return G.State(EDGE_X + 0.3, MESA + 1, CZ + 0.5, 0.28, 0.0, 0.0)


def reference():
    """Vol de reference en l'air libre : renvoie la liste des anneaux [(x, cy, cz, zone)] (cy, cz = centre du trou)."""
    air = lambda x, y, z: y < 0
    s = start_state()
    G.freefall(air, s, G.OPEN_DELAY)
    tr = []
    ok, why, _, _ = G.fly(air, s, G.Pilot(reference_waypoints()), trace=tr)
    if not ok:
        raise SystemExit('vol de reference impossible : ' + why)
    out = []
    for x, d, zone in RINGS:
        y, z = interp_yz(tr, x)
        out.append((x, y, z, zone))
    return out, tr


def interp_yz(tr, x):
    """(cy, cz) : bloc central du trou pour une trajectoire qui franchit le plan x (centre du joueur = centre du trou)."""
    for a, b in zip(tr, tr[1:]):
        if a[0] < x <= b[0]:
            t = (x - a[0]) / (b[0] - a[0])
            y = a[1] + (b[1] - a[1]) * t + G.BOX_H / 2
            z = a[2] + (b[2] - a[2]) * t
            return int(math.floor(y)), int(math.floor(z))
    raise SystemExit('trajectoire de reference trop courte pour x=%d' % x)


# ---------------------------------------------------------------- relief
PALETTE = ['red_terracotta', 'orange_terracotta', 'terracotta', 'yellow_terracotta', 'white_terracotta',
           'brown_terracotta', 'light_gray_terracotta', 'red_sandstone', 'granite']
TOWN_Y = 60                                  # sol de la ville fantome (bloc)
HALFW = [(0, 60), (300, 55), (450, 50), (520, 56), (640, 52), (665, 30), (715, 26), (815, 26), (870, 32),
         (915, 52), (950, 80), (1040, 95)]
Q = 3                                        # quantification des hauteurs : terrasses de 3 blocs
SLOPE = 2.2                                  # pente des parois : blocs de hauteur par bloc horizontal


class Path:
    """Altitude de la trajectoire de reference a chaque abscisse entiere."""

    def __init__(self, tr):
        self.ys = {}
        for a, b in zip(tr, tr[1:]):
            for x in range(int(math.ceil(a[0])), int(math.floor(b[0])) + 1):
                if a[0] <= x <= b[0] and b[0] > a[0]:
                    self.ys[x] = a[1] + (b[1] - a[1]) * (x - a[0]) / (b[0] - a[0])
        self.lo, self.hi = min(self.ys), max(self.ys)

    def y(self, x):
        return self.ys[max(self.lo, min(self.hi, int(round(x))))]


def floor_y(path, x):
    base = path.y(x) - 78
    t = T.smooth((x - 860) / 70.0)
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
                u = abs(zc - CZ - lat(xc)) + 7 * T.fbm(xc, zc, 11, 3, 40.0)
                d = u - T.lerp_pts(HALFW, xc)
                fl = floor_y(path, xc) + 2.5 * (T.fbm(xc, zc, 5, 3, 30.0) + 1) * (1 - T.smooth((xc - 860) / 70.0))
                top = plateau_y(path, xc) + 4 * (T.fbm(xc, zc, 23, 3, 70.0) + 1)
                h = fl if d <= 0 else min(top, fl + d * SLOPE + 3 * T.fbm(xc, zc, 31, 2, 20.0))
            w.ground(i, j, Q * round(h / Q))
    return w


class Course:
    """Resultat de build() : tout ce qu'il faut pour generer les fonctions et verifier le parcours."""

    def __init__(self):
        self.rings = []          # [(x, cy, cz, zone)]
        self.golds = []          # [(x, cy, cz)]
        self.cps = []            # [numero d'anneau] ; positions de reprise ajoutees par verify
        self.world = None
        self.path = None
        self.trace = None
        self.strata = None
        self.rects = []          # relief : [(x1, y1, z1, x2, y2, z2, bloc)]
        self.places = []         # [(x, z)] places de depart sur la plateforme


def build():
    """Construit le parcours complet (relief, decors, anneaux). Retourne un Course."""
    import props_canyon as P
    import town_canyon as TW
    c = Course()
    c.rings, c.trace = reference()
    c.path = Path(c.trace)
    c.strata = T.make_strata(7, PALETTE)
    w = c.world = relief(c.path)
    for x, cy, cz, zone in c.rings:
        if zone == 'arch':
            P.arch(w, c.path, x, cy, cz)
    P.ridge(w, 892, int(c.path.y(892)) - 7)
    c.rects = w.rects(w.shell(TV, TH), c.strata, 0)
    for gx, off in GOLDS:
        c.golds.append((gx, int(round(c.path.y(gx))), CZ + int(round(lat(gx))) + off))
    P.start_area(w)
    P.hoodoos(w, c.strata, c.path, c.rings, c.golds)
    for x, cy, cz, zone in c.rings:
        if zone == 'viaduct':
            P.viaduct(w, c.path, x, cy, cz)
            break
    TW.town(w)
    for n, (x, cy, cz, zone) in enumerate(c.rings, 1):
        P.ring_frame(w, x, cy, cz, 'finish' if n == len(c.rings) else 'ring')
    c.cps = list(CPS)
    for gx, gy, gz in c.golds:
        P.gold_frame(w, gx, gy, gz)
    for n in CPS:
        x, cy, cz, zone = c.rings[n - 1]
        P.cp_gate(w, x, cy, cz)
    for r in range(ROWS * 4):                              # places de depart : deux rangees de 8 (16 places)
        c.places.append((GATE_X - 2 - 4 * (r // 8), CZ - 10 + 3 * (r % 8)))
    return c
