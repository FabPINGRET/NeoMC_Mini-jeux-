"""Verification d'un parcours par le pilote automatique : chaque anneau doit etre franchi par son trou sans choc,
meme avec un ecart de trajectoire, et chaque reapparition a un point de reprise doit rejoindre l'anneau suivant.
Python stdlib uniquement (compatible 3.8).
"""
import math

import glide as G

OFFSETS = [(0, 0), (3, 3), (-3, 3), (3, -3), (-3, -3)]     # ecarts (dy, dz) de la ligne suivie par le pilote
BUMP_W = 40.0                                              # largeur des detours vers les anneaux d'or
GOLD_LOOK = 3.0                                            # anticipation reduite du pilote : il vise l'anneau d'or de pres
GOLD_TOL = 2.7                                             # ecart maximal au centre d'un anneau d'or (trou 7 x 7 moins le demi-joueur)
RESPAWN_X = 3                                              # la reapparition est 3 blocs apres le plan de l'anneau
RESPAWN_DELAY = 12                                         # ticks de chute avant l'ouverture des elytres
GOLD_MIN_DETOUR = 8                                        # detour minimal (blocs) hors de la ligne anneau a anneau, pour un or strict


def _ramp(d, width=BUMP_W):
    """Detour vers un anneau d'or : monte sur `width` blocs, plateau de 12 blocs autour de l'anneau, redescend."""
    t = (abs(d) - 6.0) / max(width, 1.0)
    if t <= 0:
        return 1.0
    if t >= 1:
        return 0.0
    u = 1.0 - t
    return u * u * (3 - 2 * u)


def polyline(c, x_from=0, dy=0, dz=0, bumps=()):
    """Ligne suivie : celle du vol de reference (spec.reference_waypoints), decalee de (dy, dz).
    `bumps` = [(x, ecart lateral[, largeur avant, largeur apres])] : detours lisses vers les anneaux d'or (largeurs de rampe :
    BUMP_W par defaut)."""
    pts = []
    for x, y, z in c.spec.reference_waypoints():
        if x >= x_from:
            for bump in bumps:
                bx, off = bump[:2]
                z += off * _ramp(x - bx, (bump[2] if x < bx else bump[3]) if len(bump) > 2 else BUMP_W)
            pts.append((x, y + dy, z + dz))
    return pts


def hole_errors(c, tr, kinds=None):
    """Pour chaque anneau croise par la trace : (numero, ecart y, ecart z) du centre du joueur / centre du trou."""
    out = {}
    for n, (x, cy, cz, zone) in enumerate(c.rings, 1):
        for a, b in zip(tr, tr[1:]):
            if a[0] < x <= b[0]:
                t = (x - a[0]) / (b[0] - a[0])
                y = a[1] + (b[1] - a[1]) * t + G.BOX_H / 2
                z = a[2] + (b[2] - a[2]) * t
                out[n] = (y - (cy + 0.5), z - (cz + 0.5))
                break
    return out


def check_flight(c, s, wps, first_ring=1, rockets=()):
    """Vole le long de wps depuis l'etat s ; renvoie (ok, message). Verifie que chaque anneau >= first_ring est franchi par le trou."""
    tr = []
    ok, why, _, _ = G.fly(c.world.solid, s, G.Pilot(wps), trace=tr)
    if not ok:
        return False, why
    errs = hole_errors(c, tr)
    for n in range(first_ring, len(c.rings) + 1):
        if n not in errs:
            return False, 'anneau %d non franchi' % n
        ey, ez = errs[n]
        if abs(ey) > 4.2 or abs(ez) > 4.2:
            return False, 'anneau %d rate (ecart %.1f / %.1f)' % (n, ey, ez)
    return True, 'ok'


def max_speed(c):
    """Vitesse horizontale maximale (blocs/tick) sur tous les vols que verify_all fait : departs avec ecarts, reprises, detours
    vers les anneaux d'or (un vol qui s'arrete en route compte jusqu'au choc)."""
    spec = c.spec
    flights = [(start(c), polyline(c, dy=dy, dz=dz), 10.0) for dy, dz in OFFSETS]
    flights += [(respawn_state(c, n, spec.R_UP[n]), polyline(c, x_from=c.rings[n - 1][0] + RESPAWN_X + 4), 10.0) for n in c.cps]
    flights += [(start(c), polyline(c, bumps=[gold_bump(c, gx, gz)]), GOLD_LOOK) for gx, gy, gz in c.golds]
    best = 0.0
    for s, wps, look in flights:
        tr = []
        G.fly(c.world.solid, s, G.Pilot(wps, look=look), trace=tr)
        best = max([best] + [t[3] for t in tr])
    return best


def gold_bump(c, gx, gz):
    """Detour vers l'or (gx, gz) : ecart lateral a la ligne de reference, et, en mode strict, rampes d'approche et de retour
    limitees a la distance de l'anneau voisin moins le plateau (6 blocs) : le pilote doit etre revenu sur la ligne a l'anneau."""
    spec = c.spec
    off = gz - (spec.CZ + 0.5 + spec.lat(gx))
    if not getattr(spec, 'GOLD_STRICT', False):
        return (gx, off)
    before = [r[0] for r in c.rings if r[0] < gx][-1:] or [gx - BUMP_W - 6]
    after = [r[0] for r in c.rings if r[0] > gx][:1] or [gx + BUMP_W + 6]
    return (gx, off, min(BUMP_W, gx - before[0] - 6.0), min(BUMP_W, after[0] - gx - 6.0))


def gold_detour(c, gx, gz):
    """Ecart (blocs) entre l'or et la ligne qui relie les centres des anneaux voisins (celle qu'on suit sans detour)."""
    before = [r for r in c.rings if r[0] < gx][-1:]
    after = [r for r in c.rings if r[0] > gx][:1]
    if before and after:
        t = (gx - before[0][0]) / float(after[0][0] - before[0][0])
        return gz - (before[0][2] + (after[0][2] - before[0][2]) * t)
    return gz - (before or after)[0][2]


def check_golds(c):
    """Un vol avec detour par chaque anneau d'or (un a la fois) : la trace doit traverser son trou de 7 x 7 sans choc avant.
    Si spec.GOLD_STRICT : le detour fait au moins GOLD_MIN_DETOUR blocs hors de la ligne anneau a anneau, ses rampes sont
    limitees a la distance des anneaux voisins (gold_bump), le vol finit le parcours et franchit le trou de tous les anneaux
    a moins de BUMP_W + 6 blocs de l'or (le detour ne doit pas faire rater la suite)."""
    strict = getattr(c.spec, 'GOLD_STRICT', False)
    for gx, gy, gz in c.golds:
        if strict and abs(gold_detour(c, gx, gz)) < GOLD_MIN_DETOUR:
            return False, "anneau d'or en x=%d : detour de %.1f blocs seulement (minimum %d)" % (gx, abs(gold_detour(c, gx, gz)), GOLD_MIN_DETOUR)
        wps = polyline(c, bumps=[gold_bump(c, gx, gz)])
        tr = []
        ok, why, _, _ = G.fly(c.world.solid, start(c), G.Pilot(wps, look=GOLD_LOOK), trace=tr)
        if strict:
            if not ok:
                return False, "anneau d'or en x=%d : le vol du detour s'arrete (%s)" % (gx, why)
            errs = hole_errors(c, tr)
            for n, r in enumerate(c.rings, 1):
                if abs(r[0] - gx) <= BUMP_W + 6 and (n not in errs or abs(errs[n][0]) > 4.2 or abs(errs[n][1]) > 4.2):
                    return False, "anneau d'or en x=%d : anneau %d rate apres le detour (ecart %s)" % (gx, n, '%.1f / %.1f' % errs[n] if n in errs else 'non franchi')
        for a, b in zip(tr, tr[1:]):
            if a[0] < gx <= b[0]:
                t = (gx - a[0]) / (b[0] - a[0])
                ey = a[1] + (b[1] - a[1]) * t + G.BOX_H / 2 - (gy + 0.5)
                ez = a[2] + (b[2] - a[2]) * t - (gz + 0.5)
                if abs(ey) > GOLD_TOL or abs(ez) > GOLD_TOL:
                    return False, "anneau d'or en x=%d rate (ecart %.1f / %.1f)" % (gx, ey, ez)
                break
        else:
            return False, "anneau d'or en x=%d : vol interrompu avant" % gx
    return True, 'ok'


def start(c):
    s = c.spec.start_state()
    G.freefall(c.world.solid, s, G.OPEN_DELAY)
    return s


def respawn_state(c, n, r_up):
    """Joueur reapparu apres l'anneau n : au repos, r_up blocs au-dessus du centre de l'anneau, chute libre avant l'ouverture."""
    x, cy, cz, zone = c.rings[n - 1]
    s = G.State(x + RESPAWN_X + 0.5, cy + r_up, cz + 0.5)
    G.freefall(c.world.solid, s, RESPAWN_DELAY)
    return s


def best_r_up(c, n, lo=10, hi=34):
    """Plus petite hauteur de reapparition (blocs au-dessus du centre de l'anneau n) qui permet de finir le parcours."""
    x = c.rings[n - 1][0] + RESPAWN_X
    last = ''
    for r in range(lo, hi + 1, 2):
        ok, why = check_flight(c, respawn_state(c, n, r), polyline(c, x_from=x + 4), first_ring=n + 1)
        if ok:
            return r, 'ok'
        last = why
    return None, last


SYNTH_SPEED = 2.5          # vitesse (blocs/tick) du cabre brutal synthetique : au-dessus de tout vol de reference


def would_trigger(prev_sq, now_sq, drop_sq, rel_pct):
    """Regle du repli de choc de game.py (speed) : chute du carre de la vitesse >= drop_sq ET >= rel_pct % du carre precedent."""
    drop = prev_sq - now_sq
    return drop >= drop_sq and drop * 100 >= prev_sq * rel_pct


def _states(c, s, wps):
    """Etat du joueur apres chaque tick du vol de reference (meme etat modifie sur place)."""
    pilot = G.Pilot(wps)
    for _ in range(3000):
        if pilot.done():
            return
        G.step(c.world.solid, s, *pilot.command(s))
        yield s
        while not pilot.done() and pilot.passed(s):
            pilot.k += 1


def _pullup(s, ticks_up=2, ticks=14):
    """Cabre brutal en plein ciel : tangage a +90 deg (vers le haut) pendant ticks_up ticks, puis retour a la croisiere.
    Renvoie les carres de vitesse horizontale (centiemes de bloc/tick) avant puis apres chaque tick."""
    s = s.copy()
    heading = math.atan2(s.vz, s.vx)
    sq = [(s.hspeed() * 100.0) ** 2]
    for t in range(ticks):
        G.step(lambda x, y, z: False, s, math.cos(heading), math.sin(heading), math.radians(90) if t < ticks_up else G.P0)
        sq.append((s.hspeed() * 100.0) ** 2)
    return sq


def speed_margins(c, drop_sq, rel_pct):
    """Verifie le repli de choc contre un mur (chute de vitesse) : (liste d'echecs, resume). Sur les vols de reference
    (depart, ecarts, reprises) il ne doit jamais se declencher, avec marge x3 sur la chute absolue et sur la chute relative ;
    un cabre brutal (+90 deg sur 2 ticks) a la vitesse maximale du parcours et a SYNTH_SPEED ne doit pas le declencher non plus
    (marge x2 sur la chute relative : seul le seuil relatif protege a grande vitesse)."""
    flights = [(start(c), polyline(c, dy=dy, dz=dz)) for dy, dz in OFFSETS]
    for n in c.cps:
        flights.append((respawn_state(c, n, c.spec.R_UP[n]), polyline(c, x_from=c.rings[n - 1][0] + RESPAWN_X + 4)))
    bad, worst_drop, worst_rel, fastest = [], 0.0, 0.0, None
    for s, wps in flights:
        prev = (s.hspeed() * 100.0) ** 2
        for st in _states(c, s, wps):
            now = (st.hspeed() * 100.0) ** 2
            worst_drop = max(worst_drop, prev - now)
            if prev > 0:
                worst_rel = max(worst_rel, (prev - now) / prev)
            if would_trigger(prev, now, drop_sq, rel_pct):
                bad.append('vol de reference : faux choc (carre %.0f -> %.0f)' % (prev, now))
            if fastest is None or st.hspeed() > fastest.hspeed():
                fastest = st.copy()
            prev = now
    if worst_drop * 3 >= drop_sq or worst_rel * 3 * 100 >= rel_pct:
        bad.append('vol de reference : marge x3 insuffisante (chute %.0f pour %d, relative %.0f %% pour %d %%)'
                   % (worst_drop, drop_sq, worst_rel * 100, rel_pct))
    info = ['vols de reference : chute max %.0f (seuil %d), relative max %.1f %% (seuil %d %%)' % (worst_drop, drop_sq, worst_rel * 100, rel_pct)]
    for label, s0 in (('vitesse max du parcours %.2f' % fastest.hspeed(), fastest), ('%.2f b/tick' % SYNTH_SPEED, _scaled(fastest, SYNTH_SPEED))):
        sq = _pullup(s0)
        rel = max((a - b) / a for a, b in zip(sq, sq[1:]))
        info.append('cabre brutal a %s : chute relative max %.1f %%' % (label, rel * 100))
        if any(would_trigger(a, b, drop_sq, rel_pct) for a, b in zip(sq, sq[1:])) or rel * 2 * 100 >= rel_pct:
            bad.append('cabre brutal a %s : declenche (ou marge x2 insuffisante : %.1f %%)' % (label, rel * 100))
    return bad, info


def _scaled(s, speed):
    s = s.copy()
    k = speed / s.hspeed()
    s.vx *= k
    s.vz *= k
    return s


def check_respawn_columns(c, r_ups):
    """La colonne de reapparition de chaque point de reprise (du centre de l'anneau a r_up + 1 : le joueur fait 2 blocs)
    ne doit contenir aucun bloc solide : sinon le joueur reapparait dans la pierre."""
    bad = []
    for n, r in r_ups.items():
        x, cy, cz, zone = c.rings[n - 1]
        for y in range(cy, cy + r + 2):
            if c.world.solid(x + RESPAWN_X, y, cz):
                bad.append('colonne de reapparition apres l\'anneau %d : bloc solide en (%d, %d, %d)' % (n, x + RESPAWN_X, y, cz))
                break
    return bad


def verify_all(c, r_ups=None):
    """Execute toutes les verifications ; renvoie la liste des echecs (vide si tout passe)."""
    r_ups = r_ups or {n: c.spec.R_UP[n] for n in c.cps}
    bad = check_respawn_columns(c, r_ups)
    for dy, dz in OFFSETS:
        ok, why = check_flight(c, start(c), polyline(c, dy=dy, dz=dz))
        if not ok:
            bad.append('depart (ecart %d,%d) : %s' % (dy, dz, why))
    ok, why = check_golds(c)
    if not ok:
        bad.append('anneaux d\'or : ' + why)
    for n, r in r_ups.items():
        ok, why = check_flight(c, respawn_state(c, n, r), polyline(c, x_from=c.rings[n - 1][0] + RESPAWN_X + 4), first_ring=n + 1)
        if not ok:
            bad.append('reprise apres l\'anneau %d (+%d) : %s' % (n, r, why))
    return bad
