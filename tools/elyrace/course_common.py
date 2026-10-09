"""Ce qui est commun a tous les parcours de la Course d'elytres : le resultat de build() (Course), la trajectoire de
reference (Path), le vol de reference d'une spec (reference) et le trou des anneaux (HOLE).
Un parcours est un module « spec » (course_canyon.py, ...) qui expose NUM, NAME, ICON, COLOR, STARS, TIP, FLAG, CZ, X0, X1, Z0, Z1, START_Y,
EDGE_X, GATE_X, RINGS, CPS, GOLDS, WINDS, R_UP, build(), reference_waypoints(), start_state() et lat() ; OLD_FLAGS (facultatif) liste
les drapeaux des versions precedentes, que elyrace/forget efface. Le suivi de mg:setup teste les FLAG (tools/setup/gen_setup_watch.py).
Python stdlib uniquement (compatible 3.8).
"""
import math

import glide as G

HOLE = 9                                     # trou des anneaux : 9 x 9
FN = 'data/mg/function/elyrace/'             # sortie generee (relative a la racine du depot)


def lines_to_text(lines):
    return '\n'.join(lines) + '\n'


def fn(spec, name):
    """Reference d'une fonction propre a un parcours : mg:elyrace/c<NUM>/<name>."""
    return 'mg:elyrace/c%d/%s' % (spec.NUM, name)


def per_course(specs, name):
    """Lignes qui appellent c<N>/<name> selon le parcours du joueur (@s mg.xcr : posé par prepare en groupe, par solo/start en solo)."""
    return ['execute if score @s mg.xcr matches %d run function %s' % (s.NUM, fn(s, name)) for s in specs]


class Course:
    """Resultat de build() : tout ce qu'il faut pour generer les fonctions et verifier le parcours."""

    def __init__(self, spec):
        self.spec = spec         # le module du parcours
        self.rings = []          # [(x, cy, cz, zone)]
        self.golds = []          # [(x, cy, cz)]
        self.winds = []          # [(x, cy, cz)] anneaux de vent (vide si wind.WIND est faux)
        self.cps = []            # [numero d'anneau] ; positions de reprise ajoutees par verify
        self.world = None
        self.path = None
        self.trace = None
        self.strata = None
        self.rects = []          # relief : [(x1, y1, z1, x2, y2, z2, bloc)]
        self.places = []         # [(x, z)] places de depart sur la plateforme


def interp_yz(tr, x):
    """(cy, cz) : bloc central du trou pour une trajectoire qui franchit le plan x (centre du joueur = centre du trou)."""
    for a, b in zip(tr, tr[1:]):
        if a[0] < x <= b[0]:
            t = (x - a[0]) / (b[0] - a[0])
            y = a[1] + (b[1] - a[1]) * t + G.BOX_H / 2
            z = a[2] + (b[2] - a[2]) * t
            return int(math.floor(y)), int(math.floor(z))
    raise SystemExit('trajectoire de reference trop courte pour x=%d' % x)


def reference(spec):
    """Vol de reference en l'air libre : renvoie la liste des anneaux [(x, cy, cz, zone)] (cy, cz = centre du trou)."""
    air = lambda x, y, z: y < 0
    s = spec.start_state()
    G.freefall(air, s, G.OPEN_DELAY)
    tr = []
    ok, why, _, _ = G.fly(air, s, G.Pilot(spec.reference_waypoints()), trace=tr)
    if not ok:
        raise SystemExit('vol de reference impossible : ' + why)
    out = []
    for x, d, zone in spec.RINGS:
        y, z = interp_yz(tr, x)
        out.append((x, y, z, zone))
    return out, tr


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
