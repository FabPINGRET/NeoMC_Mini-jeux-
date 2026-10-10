"""Verification d'un parcours par le pilote automatique : chaque anneau doit etre franchi par son trou sans choc,
meme avec un ecart de trajectoire, et chaque reapparition a un point de reprise doit rejoindre l'anneau suivant.
La decision « anneau franchi » est celle du jeu (sweep.hits, detection balayee) ; un anneau d'or ne change pas le vol (il donne un bonus
de temps : gold_costs mesure ce que coute son detour, a comparer au bonus, voir game.GOLD_BONUS).
Les marges du repli de choc (speed) sont dans verify_speed.py. Python stdlib uniquement (compatible 3.8).
"""
import glide as G
import sweep as SW

OFFSETS = [(0, 0), (3, 3), (-3, 3), (3, -3), (-3, -3)]     # ecarts (dy, dz) de la ligne suivie par le pilote
BUMP_W = 40.0                                              # largeur des detours vers les anneaux d'or
GOLD_LOOK = 5.0                                            # anticipation reduite du pilote : il vise l'anneau d'or de pres
GOLD_RETURN_MARGIN = 8                                     # le pilote rejoint la ligne ce nombre de blocs avant l'anneau suivant (comme un joueur qui le vise)
GOLD_TOL = 2.7                                             # ecart maximal au centre d'un anneau d'or (trou 7 x 7 moins le demi-joueur)
VMAX_CAP = 4.0                                             # vitesse horizontale maximale (b/tick) de tous les vols verifies : au-dela, un deplacement
                                                           # par tick approche sweep.STEP_MAX (verifie par checks.py) et le repli de choc n'est plus eprouve
RESPAWN_X = 3                                             # la reapparition est 3 blocs apres le plan de l'anneau
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
    if pts:                                          # le plan du dernier anneau est a x + 0,5 : le vol doit le depasser (pilote : constant apres le dernier point)
        pts.append((pts[-1][0] + 4, pts[-1][1], pts[-1][2]))
    return pts


def plane_error(tr, x, cy, cz):
    """(ecart y, ecart z) du centre du joueur au centre du trou, au plan de l'anneau x (x + 0,5) ; None si la trace ne le traverse pas."""
    for a, b in zip(tr, tr[1:]):
        if a[0] < x + 0.5 <= b[0]:
            t = (x + 0.5 - a[0]) / (b[0] - a[0])
            return (a[1] + (b[1] - a[1]) * t + G.BOX_H / 2 - (cy + 0.5), a[2] + (b[2] - a[2]) * t - (cz + 0.5))
    return None


def tick_hits(a, b, x, cy, cz, r):
    """sweep.hits avec un test grossier d'abord (le plan x + 0,5 est entre les deux positions) : la verification fait ~10^6 appels."""
    return a[0] < x + 1 and b[0] >= x and SW.hits(a, b, x, cy, cz, r)


def crosses(tr, x, cy, cz, r):
    """True si un tick de la trace franchit le trou de rayon r de l'anneau x."""
    return any(tick_hits(a, b, x, cy, cz, r) for a, b in zip(tr, tr[1:]))


def ring_hits(c, tr):
    """Numeros d'anneau (1..) dont le trou est franchi par la trace, selon sweep.hits (la regle du jeu)."""
    return {n for n, (x, cy, cz, zone) in enumerate(c.rings, 1) if crosses(tr, x, cy, cz, SW.HOLE_R)}


def missed(c, tr, first, last=None):
    """Premier message d'echec parmi les anneaux first..last (derniere = tous) que la trace ne franchit pas par le trou, sinon None."""
    hit = ring_hits(c, tr)
    for n in range(first, (last or len(c.rings)) + 1):
        if n not in hit:
            x, cy, cz, zone = c.rings[n - 1]
            err = plane_error(tr, x, cy, cz)
            return 'anneau %d rate (%s)' % (n, 'ecart %.1f / %.1f' % err if err else 'plan non traverse')
    return None


def check_flight(c, s, wps, first_ring=1, hook=None):
    """Vole le long de wps depuis l'etat s ; renvoie (ok, message). Verifie que chaque anneau >= first_ring est franchi par le trou."""
    tr = []
    ok, why, _, _ = G.fly(c.world.solid, s, G.Pilot(wps), trace=tr, hook=hook)
    if not ok:
        return False, why
    why = missed(c, tr, first_ring)
    return (False, why) if why else (True, 'ok')


def gold_flights(c):
    """Vols avec detour vers les ors : un par or, puis un qui les prend tous : [(etat, points, anticipation, crochet)] (crochet : aucun, l'or ne change pas le vol)."""
    hook = None
    bumps = [gold_bump(c, gx, gz) for gx, gy, gz in c.golds]
    flights = [(start(c), polyline(c, bumps=[b]), GOLD_LOOK, hook) for b in bumps]
    if bumps:
        flights.append((start(c), polyline(c, bumps=bumps), GOLD_LOOK, hook))
    return flights


def max_speed(c):
    """Vitesse horizontale maximale (blocs/tick) sur tous les vols que verify_all fait : departs avec ecarts, reprises, detours
    vers les anneaux d'or (un vol qui s'arrete en route compte jusqu'au choc)."""
    spec = c.spec
    flights = [(start(c), polyline(c, dy=dy, dz=dz), 10.0, None) for dy, dz in OFFSETS]
    flights += [(respawn_state(c, n, spec.R_UP[n]), polyline(c, x_from=c.rings[n - 1][0] + RESPAWN_X + 4), 10.0, None) for n in c.cps]
    best = 0.0
    for s, wps, look, hook in flights + gold_flights(c):
        tr = []
        G.fly(c.world.solid, s, G.Pilot(wps, look=look), trace=tr, hook=hook)
        best = max([best] + [t[3] for t in tr])
    return best


def gold_bump(c, gx, gz):
    """Detour vers l'or (gx, gz) : ecart lateral a la ligne de reference, et, en mode strict, rampes d'approche et de retour
    limitees a la distance de l'anneau voisin moins le plateau (6 blocs) ; la rampe de retour s'arrete GOLD_RETURN_MARGIN blocs plus tot : le pilote
    doit etre revenu sur la ligne avant l'anneau."""
    spec = c.spec
    off = gz - (spec.CZ + 0.5 + spec.lat(gx))
    if not getattr(spec, 'GOLD_STRICT', False):
        return (gx, off)
    before = [r[0] for r in c.rings if r[0] < gx][-1:] or [gx - BUMP_W - 6]
    after = [r[0] for r in c.rings if r[0] > gx][:1] or [gx + BUMP_W + 6]
    return (gx, off, min(BUMP_W, gx - before[0] - 6.0), max(1.0, min(BUMP_W, after[0] - gx - 6.0 - GOLD_RETURN_MARGIN)))


def gold_detour(c, gx, gz):
    """Ecart (blocs) entre l'or et la ligne qui relie les centres des anneaux voisins (celle qu'on suit sans detour)."""
    before = [r for r in c.rings if r[0] < gx][-1:]
    after = [r for r in c.rings if r[0] > gx][:1]
    if before and after:
        t = (gx - before[0][0]) / float(after[0][0] - before[0][0])
        return gz - (before[0][2] + (after[0][2] - before[0][2]) * t)
    return gz - (before or after)[0][2]


def check_golds(c):
    """Un vol avec detour par chaque anneau d'or (un a la fois) : la trace doit traverser son trou de 7 x 7
    (sweep.hits) sans choc avant, et tenir l'ecart au centre GOLD_TOL. Si spec.GOLD_STRICT : le detour fait au moins GOLD_MIN_DETOUR
    blocs hors de la ligne anneau a anneau, ses rampes sont limitees a la distance des anneaux voisins (gold_bump), le vol finit le
    parcours et franchit le trou de TOUS les anneaux a partir de BUMP_W + 6 blocs avant l'or (le detour ne doit pas
    faire rater la suite). Enfin le vol qui prend tous les ors finit le parcours et franchit tous les anneaux."""
    strict = getattr(c.spec, 'GOLD_STRICT', False)
    flights = gold_flights(c)
    for (gx, gy, gz), (s, wps, look, hook) in zip(c.golds, flights):
        if strict and abs(gold_detour(c, gx, gz)) < GOLD_MIN_DETOUR:
            return False, "anneau d'or en x=%d : detour de %.1f blocs seulement (minimum %d)" % (gx, abs(gold_detour(c, gx, gz)), GOLD_MIN_DETOUR)
        tr = []
        ok, why, _, _ = G.fly(c.world.solid, s, G.Pilot(wps, look=look), trace=tr, hook=hook)
        if strict:
            if not ok:
                return False, "anneau d'or en x=%d : le vol du detour s'arrete (%s)" % (gx, why)
            n0 = [n for n, r in enumerate(c.rings, 1) if r[0] >= gx - BUMP_W - 6][0]
            why = missed(c, tr, n0)
            if why:
                return False, "anneau d'or en x=%d : %s apres le detour" % (gx, why)
        err = plane_error(tr, gx, gy, gz)
        if err is None:
            return False, "anneau d'or en x=%d : vol interrompu avant" % gx
        if not crosses(tr, gx, gy, gz, SW.GOLD_R) or max(map(abs, err)) > GOLD_TOL:
            return False, "anneau d'or en x=%d rate (ecart %.1f / %.1f)" % (gx, err[0], err[1])
    if len(flights) > len(c.golds):
        s, wps, look, hook = flights[-1]
        tr = []
        ok, why, _, _ = G.fly(c.world.solid, s, G.Pilot(wps, look=look), trace=tr, hook=hook)
        if not ok:
            return False, "vol qui prend tous les ors : il s'arrete (%s)" % why
        why = missed(c, tr, 1) or ''.join("l'or en x=%d est rate" % g[0] for g in c.golds if not crosses(tr, g[0], g[1], g[2], SW.GOLD_R))
        if why:
            return False, 'vol qui prend tous les ors : ' + why
    return True, 'ok'


def gold_costs(c):
    """Cout en ticks du detour de chaque anneau d'or : [(x de l'or, duree du vol avec ce seul detour - duree du meme vol sans detour, avec
    l'anticipation GOLD_LOOK ; None si l'un des deux vols echoue)]. Le bonus de temps de l'or (game.GOLD_BONUS) doit le depasser."""
    ok0, _, t0, _ = G.fly(c.world.solid, start(c), G.Pilot(polyline(c), look=GOLD_LOOK))
    out = []
    for (gx, gy, gz), (s, wps, look, hook) in zip(c.golds, gold_flights(c)):
        ok, _, t, _ = G.fly(c.world.solid, s, G.Pilot(wps, look=look), hook=hook)
        out.append((gx, t - t0 if ok and ok0 else None))
    return out


def start(c):
    s = c.spec.start_state()
    G.freefall(c.world.solid, s, G.OPEN_DELAY)
    return s


def respawn_state(c, n, r_up):
    """Joueur reapparu apres l'anneau n : au repos, r_up blocs au-dessus du centre de l'anneau, chute libre avant l'ouverture."""
    x, cy, cz, zone = c.rings[n - 1]
    s = G.State(x + RESPAWN_X + 0.5, cy + r_up, cz + 0.5, g=c.spec.GRAVITY)       # c<N>/respawn repose la gravite de base du parcours
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
