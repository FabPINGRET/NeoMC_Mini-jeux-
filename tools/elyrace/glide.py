"""Physique du vol en elytres (reprise des formules vanilla), pilote automatique et verifications.

Sert uniquement a la generation : le pilote automatique vole le parcours dans un modele du terrain
(terrain.World) pour prouver que chaque anneau est franchissable sans collision et que chaque
reapparition au checkpoint permet de rejoindre l'anneau suivant.
Python stdlib uniquement (compatible 3.8).
"""
import math

GRAV = 0.08                    # gravite vanilla (blocs/tick^2)
HALF_W, BOX_H = 0.3, 0.6       # hitbox du joueur en vol plane : 0,6 x 0,6
ROCKET_TICKS = 16              # duree moyenne d'une fusee (flight_duration 1 : 10 + 0..5 + 0..6 ticks)
OPEN_DELAY = 8                 # ticks de chute avant l'ouverture des elytres apres une reapparition
TURBO_G = 0.13                 # gravite pendant le turbo d'un anneau d'or (game.gold_hit pose le meme attribut)
TURBO_TICKS = 60               # duree du turbo : 3 s (mg.xu, game.gold_hit)
EPS = 1e-7


class State:
    """Position (pieds), vitesse, fusee en cours, gravite de base du parcours (g), ticks de turbo restants."""
    __slots__ = ('x', 'y', 'z', 'vx', 'vy', 'vz', 'rocket', 'rockets', 'gliding', 'g', 'turbo')

    def __init__(self, x, y, z, vx=0.0, vy=0.0, vz=0.0, rockets=0, g=GRAV):
        self.x, self.y, self.z, self.vx, self.vy, self.vz = x, y, z, vx, vy, vz
        self.rocket, self.rockets, self.gliding = 0, rockets, True
        self.g, self.turbo = g, 0

    def hspeed(self):
        return math.hypot(self.vx, self.vz)

    def copy(self):
        s = State(self.x, self.y, self.z, self.vx, self.vy, self.vz, self.rockets, self.g)
        s.rocket, s.gliding, s.turbo = self.rocket, self.gliding, self.turbo
        return s


def look(dx, dz, pitch):
    """Vecteur de visee : cap horizontal (dx, dz) normalise, tangage `pitch` en radians (positif = vers le haut)."""
    h = math.hypot(dx, dz) or 1.0
    c = math.cos(pitch)
    return dx / h * c, math.sin(pitch), dz / h * c


def _sweep(solid, s, axis, d):
    """Deplace la hitbox le long d'un axe en s'arretant contre le premier bloc plein. Renvoie la distance reellement parcourue."""
    if abs(d) < EPS:
        return 0.0
    mn = (s.x - HALF_W, s.y, s.z - HALF_W)
    mx = (s.x + HALF_W, s.y + BOX_H, s.z + HALF_W)
    if d > 0:
        edge = mx[axis]
        rng = range(math.floor(edge - EPS) + 1, math.floor(edge + d - EPS) + 1)
    else:
        edge = mn[axis]
        rng = range(math.ceil(edge - EPS) - 1, math.floor(edge + d + EPS) - 1, -1)
    other = [range(math.floor(mn[k] + EPS), math.floor(mx[k] - EPS) + 1) if k != axis else (0,) for k in range(3)]
    for c in rng:
        for u in other[0]:
            for v in other[1]:
                for w in other[2]:
                    p = (c if axis == 0 else u, c if axis == 1 else v, c if axis == 2 else w)
                    if solid(*p):
                        return (c - edge) if d > 0 else (c + 1 - edge)
    return d


def move(solid, s, dx, dy, dz):
    """Equivalent de Entity.move : Y d'abord, puis l'axe horizontal le plus long, puis l'autre. Renvoie (collision_x, collision_y, collision_z)."""
    hit = [False, False, False]
    order = [1] + ([0, 2] if abs(dx) >= abs(dz) else [2, 0])
    for ax in order:
        d = (dx, dy, dz)[ax]
        r = _sweep(solid, s, ax, d)
        if abs(r - d) > EPS:
            hit[ax] = True
        if ax == 0:
            s.x += r
        elif ax == 1:
            s.y += r
        else:
            s.z += r
    return hit


def step(solid, s, ldx, ldz, pitch, rocket=False):
    """Un tick de vol plane. Retourne (choc_horizontal_degats, contact_sol)."""
    if rocket and s.rockets > 0 and s.rocket == 0:
        s.rockets -= 1
        s.rocket = ROCKET_TICKS
    lx, ly, lz = look(ldx, ldz, pitch)
    d0 = math.hypot(lx, lz)
    d1 = s.hspeed()
    f = -pitch                                   # vanilla : xRot positif = vers le bas
    d3 = math.cos(f) ** 2
    if s.rocket > 0:                             # fusee : tire la vitesse vers 1,5 x la visee
        s.vx += lx * 0.1 + (lx * 1.5 - s.vx) * 0.5
        s.vy += ly * 0.1 + (ly * 1.5 - s.vy) * 0.5
        s.vz += lz * 0.1 + (lz * 1.5 - s.vz) * 0.5
        s.rocket -= 1
    g = TURBO_G if s.turbo > 0 else s.g          # turbo d'un anneau d'or : gravite renforcee pendant TURBO_TICKS ticks
    if s.turbo > 0:
        s.turbo -= 1
    vx, vy, vz = s.vx, s.vy + g * (-1.0 + d3 * 0.75), s.vz
    if vy < 0.0 and d0 > 0.0:
        d4 = vy * -0.1 * d3
        vx += lx * d4 / d0
        vy += d4
        vz += lz * d4 / d0
    if f < 0.0 and d0 > 0.0:
        d5 = d1 * (-math.sin(f)) * 0.04
        vx += -lx * d5 / d0
        vy += d5 * 3.2
        vz += -lz * d5 / d0
    if d0 > 0.0:
        vx += (lx / d0 * d1 - vx) * 0.1
        vz += (lz / d0 * d1 - vz) * 0.1
    s.vx, s.vy, s.vz = vx * 0.99, vy * 0.98, vz * 0.99
    before = math.hypot(s.vx, s.vz)
    hx, hy, hz = move(solid, s, s.vx, s.vy, s.vz)
    if hx:
        s.vx = 0.0
    if hz:
        s.vz = 0.0
    if hy:
        s.vy = 0.0
    after = math.hypot(s.vx, s.vz)
    dmg = (hx or hz) and (before - after) * 10.0 - 3.0 > 0.0
    return bool(dmg), bool(hy and s.vy == 0.0 and _ground(solid, s))


def _ground(solid, s):
    return any(solid(math.floor(s.x + ox), math.floor(s.y - 0.01), math.floor(s.z + oz)) for ox in (-0.29, 0.29) for oz in (-0.29, 0.29))


def freefall(solid, s, ticks):
    """Chute libre (elytres pas encore ouvertes), pour la reapparition. Renvoie True si on touche le sol."""
    for _ in range(ticks):
        s.vy = (s.vy - s.g) * 0.98
        s.vx *= 0.91
        s.vz *= 0.91
        hit = move(solid, s, s.vx, s.vy, s.vz)
        if hit[1]:
            return True
        if hit[0] or hit[2]:
            s.vx = s.vz = 0.0
    return False


# ---------------------------------------------------------------- pilote automatique
P_MIN, P_MAX = math.radians(-65), math.radians(50)
P0, KP = math.radians(-12), 1.5               # tangage de croisiere et gain de la loi
HEAD_MAX = math.tan(math.radians(40))         # ecart de cap maximal visé par rapport a l'axe x
GD_MAX = math.radians(12)                     # pente de montee maximale visee
PITCH_PER_SPEED = math.radians(50)            # tangage maximal autorise : -5 deg a 0,8 b/t, +50 deg par b/t en plus


class Pilot:
    """Suit une polyligne de points de passage (x, y, z[, fusee]) croissants en x : cap et tangage visent le point situe
    `look` blocs plus loin sur la ligne (virages doux), tangage corrige sur l'angle de trajectoire.
    Sert a prouver qu'un joueur raisonnablement adroit passe les anneaux ; ce n'est pas un modele de joueur optimal."""

    def __init__(self, wps, look=10.0):
        self.wps, self.k, self.look = wps, 0, look

    def done(self):
        return self.k >= len(self.wps)

    def at(self, x):
        """(y, z) de la polyligne a l'abscisse x (constant apres le dernier point)."""
        w = self.wps
        if x >= w[-1][0]:
            return w[-1][1], w[-1][2]
        i = self.k
        while i > 0 and w[i - 1][0] > x:
            i -= 1
        while i + 1 < len(w) and w[i][0] <= x:
            i += 1
        a, b = w[max(i - 1, 0)], w[i]
        t = 0.0 if b[0] == a[0] else max(0.0, min(1.0, (x - a[0]) / (b[0] - a[0])))
        return a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t

    def command(self, s):
        """(ldx, ldz, pitch, fusee) pour le tick courant."""
        spd = s.hspeed()
        ahead = self.look + 3.0 * spd
        ty, tz = self.at(s.x + ahead)
        hx = ahead
        hz = max(-ahead * HEAD_MAX, min(ahead * HEAD_MAX, tz - s.z))
        gd = min(math.atan2(ty - s.y, math.hypot(hx, hz)), GD_MAX)
        g = math.atan2(s.vy, max(spd, 0.05))
        p = max(P_MIN, min(P_MAX, P0 + KP * (gd - g)))
        p = min(p, max(P_MIN, min(P_MAX, math.radians(-5) + PITCH_PER_SPEED * (spd - 0.8))))   # pas de cabrage a basse vitesse
        rk = len(self.wps[self.k]) > 3 and bool(self.wps[self.k][3])
        return hx, hz, p, rk

    def passed(self, s):
        return self.wps[self.k][0] <= s.x


def fly(solid, s, pilot, max_ticks=3000, trace=None, hook=None):
    """Vole jusqu'au dernier point. Retourne (ok, raison, tick, liste (indice, ecart_y, ecart_z, vitesse)).
    `hook(s, avant, apres)` (facultatif) est appele apres chaque tick avec les positions (x, y, z) avant et apres : il peut modifier
    l'etat (turbo d'un anneau d'or, voir verify.turbo_hook) ; il agit des le tick suivant, comme une commande de fonction."""
    log = []
    for t in range(max_ticks):
        if pilot.done():
            return True, 'fini', t, log
        ldx, ldz, p, r = pilot.command(s)
        before = (s.x, s.y, s.z)
        dmg, gnd = step(solid, s, ldx, ldz, p, r)
        if hook is not None:
            hook(s, before, (s.x, s.y, s.z))
        if trace is not None:
            trace.append((s.x, s.y, s.z, s.hspeed(), s.vy))
        if dmg:
            return False, 'choc a (%.0f,%.0f,%.0f)' % (s.x, s.y, s.z), t, log
        if gnd:
            return False, 'sol a (%.0f,%.0f,%.0f)' % (s.x, s.y, s.z), t, log
        while not pilot.done() and pilot.passed(s):
            tx, ty, tz = pilot.wps[pilot.k][:3]
            log.append((pilot.k, s.y - ty, s.z - tz, s.hspeed()))
            pilot.k += 1
    return False, 'temps depasse', max_ticks, log
