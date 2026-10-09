"""Marges du repli de choc de game.py (speed) sur les vols du pilote automatique : le repli (chute du carre de la vitesse horizontale) ne
doit jamais se declencher sur un vol normal, y compris avec le turbo d'un anneau d'or, ni sur un cabre brutal a la vitesse maximale.
Separe de verify.py : une autre raison de changer (seuils DROP_SQ / DROP_REL de game.py). Python stdlib uniquement (compatible 3.8).
"""
import math

import glide as G
import verify as V

SYNTH_SPEED = V.VMAX_CAP   # vitesse (blocs/tick) du cabre brutal synthetique : le plafond de vitesse de tous les vols verifies


def would_trigger(prev_sq, now_sq, drop_sq, rel_pct):
    """Regle du repli de choc de game.py (speed) : chute du carre de la vitesse >= drop_sq ET >= rel_pct % du carre precedent."""
    drop = prev_sq - now_sq
    return drop >= drop_sq and drop * 100 >= prev_sq * rel_pct


def _states(c, s, wps, look=10.0, hook=None):
    """Etat du joueur apres chaque tick du vol de reference (meme etat modifie sur place ; `hook` : voir glide.fly)."""
    pilot = G.Pilot(wps, look=look)
    for _ in range(3000):
        if pilot.done():
            return
        before = (s.x, s.y, s.z)
        dmg, gnd = G.step(c.world.solid, s, *pilot.command(s))
        if dmg or gnd:                              # vol interrompu (deja signale par verify) : pas un faux choc
            return
        if hook is not None:
            hook(s, before, (s.x, s.y, s.z))
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


def _scaled(s, speed):
    s = s.copy()
    k = speed / s.hspeed()
    s.vx *= k
    s.vz *= k
    return s


def speed_margins(c, drop_sq, rel_pct):
    """Verifie le repli de choc contre un mur (chute de vitesse) : (liste d'echecs, resume). Sur les vols de reference
    (depart, ecarts, reprises, vols avec turbo des ors) il ne doit jamais se declencher, avec marge x3 sur la chute absolue et sur la
    chute relative ; un cabre brutal (+90 deg sur 2 ticks) a la vitesse maximale du parcours et a SYNTH_SPEED ne doit pas le declencher
    non plus (marge x2 sur la chute relative : seul le seuil relatif protege a grande vitesse)."""
    flights = [(V.start(c), V.polyline(c, dy=dy, dz=dz), 10.0, None) for dy, dz in V.OFFSETS]
    for n in c.cps:
        flights.append((V.respawn_state(c, n, c.spec.R_UP[n]), V.polyline(c, x_from=c.rings[n - 1][0] + V.RESPAWN_X + 4), 10.0, None))
    flights += V.gold_flights(c)
    bad, worst_drop, worst_rel, fastest = [], 0.0, 0.0, None
    for s, wps, look, hook in flights:
        prev = (s.hspeed() * 100.0) ** 2
        for st in _states(c, s, wps, look, hook):
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
