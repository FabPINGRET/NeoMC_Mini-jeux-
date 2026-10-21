"""🌙 Ombrelune : accès à pied (rampe du volcan, brèche de la caldeira, gorges du col sud, parvis de Khazgarde).
Module importé par ol_world (relief) et ol_region_est (caldeira) ; il n'importe jamais ol_world : le relief H est calculé à l'import.
Les corrections ne font que remonter (rampe) ou creuser (brèche, gorges) le relief existant, et ne touchent ni la végétation ni les routes ailleurs.
"""
import math


def lerp(a, b, t):
    return a + (b - a) * t


def smooth(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


# ---------------------------------------------------------------- volcan : rampe nord et brèche dans le rebord de la caldeira
A0, A1, RC, Y0 = 252, 310, 23.5, 100   # rampe : angle de départ / d'arrivée (degrés), rayon médian, hauteur au départ
A_MAX = 318                            # au-delà de A1 la rampe reste à plat jusqu'ici (angle degrés)
BREACH_HW = 2.5                        # demi-largeur de la brèche (blocs)
CARVED = set()                         # colonnes creusées sous le relief d'origine (vidage d'air dans terrain_cmds)
_CB, _SB = math.cos(math.radians(A1)), math.sin(math.radians(A1))


def in_breach(x, z, c):
    """Vrai dans la brèche : bande de demi-largeur BREACH_HW, du centre du volcan vers l'angle A1 (nord-est), au bout de la rampe."""
    dx, dz = x - c[0], z - c[1]
    return dx * _CB + dz * _SB >= 0 and abs(-dx * _SB + dz * _CB) <= BREACH_HW


def breach_pt(c, y, r=18):
    """(x, y, z) du point de la brèche à r blocs de l'axe du volcan (pour spot())."""
    return math.floor(c[0] + r * _CB), y, math.floor(c[1] + r * _SB)


def volcano(x, z, h, c, cy):
    """Relief du cône en (x, z) : brèche au niveau de la caldeira, puis rampe de pente douce (jamais plus bas que h)."""
    dx, dz = x - c[0], z - c[1]
    r = math.hypot(dx, dz)
    if 15.5 <= r < 21.5 and in_breach(x, z, c):
        CARVED.add((x, z))
        return cy
    a = math.degrees(math.atan2(dz, dx)) % 360
    dr = abs(r - RC)
    if A0 <= a <= A_MAX and dr < 4:
        ry = lerp(Y0, cy, min(1, (a - A0) / (A1 - A0)))
        w = 1 if dr <= 2 else smooth(1 - (dr - 2) / 2)
        h = max(h, lerp(h, ry, w))
    return h


def ramp_routes(c):
    """Dallage de la rampe : trois arcs (rayons 22, 23.5, 24.8) et le segment radial de la brèche (r reste ≤ 24.8 : pas de végétation touchée)."""
    out = []
    for r in (22, RC, 24.8):
        out.append([(c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a))) for a in [*range(A0, A_MAX, 4), A_MAX]])
    out.append([(c[0] + r * _CB, c[1] + r * _SB) for r in (24.8, 14)])
    return out


# ---------------------------------------------------------------- Khazgarde : gorges des cols et parvis de la porte
PARVIS = (-15, 130, 15, 139, 66, 1)    # même format que FLAT : parvis de la porte naine
HALL_GUARD = (-19, 140, 19, 206)       # x0 z0 x1 z1 : la salle de Khazgarde (jamais entaillée)
GORGES = [([(84, 168), (60, 168), (40, 150), (12, 132)], [68, 68, 67, 66]),
          ([(-20, 132), (-60, 160), (-80, 168), (-84, 168)], [66] * 4)]   # (points, fonds) : cols se-s et s-sw


def _dist_seg(x, z, a, b):
    """(distance, t) du point (x, z) au segment a-b."""
    ax, az = a
    ex, ez = b[0] - ax, b[1] - az
    t = max(0.0, min(1.0, ((x - ax) * ex + (z - az) * ez) / (ex * ex + ez * ez)))
    return math.hypot(x - ax - t * ex, z - az - t * ez), t


def gorges(x, z, h):
    """Entaille (largeur 6 + raccord de 7 blocs) des gorges du côté sud : le relief ne fait que descendre vers le fond."""
    x0, z0, x1, z1 = HALL_GUARD
    if z < PARVIS[1] or (x0 <= x <= x1 and z0 <= z <= z1):
        return h
    best = None
    for pts, ys in GORGES:
        for i in range(len(pts) - 1):
            d, t = _dist_seg(x, z, pts[i], pts[i + 1])
            if best is None or d < best[0]:
                best = (d, lerp(ys[i], ys[i + 1], t))
    d, f = best
    if d >= 10:
        return h
    w = 1 if d <= 3 else smooth(1 - (d - 3) / 7)
    n = min(h, lerp(h, f, w))
    if n < h - 0.5:
        CARVED.add((x, z))
    return n


def carved(x, z):
    """Vrai si la colonne a été creusée (brèche, gorges, parvis) : terrain_cmds y vide l'air au-dessus du sol."""
    x0, z0, x1, z1 = PARVIS[:4]
    return (x, z) in CARVED or (x0 <= x <= x1 and z0 <= z <= z1)
