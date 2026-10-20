"""Élytra : placement du décor (graine fixe) et découpe en sections de construction asynchrone.
build(W, SUB) écrit les fonctions b/*, b_step, w_step et fl_secs_off via W et renvoie l'état utile aux autres étapes.
"""
import math
import os
import random

from sky_shapes import COLS, arch, cliff, cloud, island, pillar, ring, spike, tower, wind_column
from sky_track import ARENA, AXES, N, NS, PAD1, PATH, RINGS
from sky_vox import Vox, to_cmds


def seg_dist(p, a, b):
    ax_, ay, az = a; bx, by, bz = b; px, py, pz = p
    vx, vy, vz = bx - ax_, by - ay, bz - az
    L = vx * vx + vy * vy + vz * vz
    t = max(0, min(1, ((px - ax_) * vx + (py - ay) * vy + (pz - az) * vz) / L)) if L else 0
    return math.dist(p, (ax_ + vx * t, ay + vy * t, az + vz * t))


def path_dist(p):
    return min(seg_dist(p, PATH[i], PATH[i + 1]) for i in range(len(PATH) - 1))


def box_path_clear(bb, margin):
    """Aucun voxel de la boîte englobante (échantillonnée) à moins de margin de la trajectoire."""
    x0, y0, z0, x1, y1, z1 = bb
    for x in range(x0, x1 + 1, 3):
        for y in range(y0, y1 + 1, 3):
            for z in range(z0, z1 + 1, 3):
                if path_dist((x, y, z)) < margin:
                    return False
    return True


def sec_order(k):
    zone, gx, gz = k
    return (0 if zone == 'c' else 1, gz, gx)


def build(W, SUB):
    """Construit les sections ; renvoie (features, sec_keys, steps_b, steps_w, stats)."""
    # =====================================================================================
    # Placement du décor (graine fixe), avec dégagement autour de la trajectoire
    # =====================================================================================
    rng = random.Random(7431)

    features = []   # (nom, Vox, zone 'c' parcours / 'a' arène)

    def add_feature(name, fn, zone, check=True, margin=9, tries=1):
        V = Vox()
        fn(V)
        bb = V.bbox()
        if zone == 'c':
            if bb[0] < -200 or bb[3] > 200 or bb[2] < 27600 or bb[5] > 28400 or bb[1] < 90 or bb[4] > 250:
                return False
        else:
            if bb[1] < 90 or bb[4] > 220 or math.hypot(max(abs(bb[0]), abs(bb[3])), max(abs(bb[2] - ARENA[1]), abs(bb[5] - ARENA[1]))) > 101 * 1.42:
                return False
            if max(abs(bb[0]), abs(bb[3])) > 100 or max(abs(bb[2] - ARENA[1]), abs(bb[5] - ARENA[1])) > 100:
                return False
        for (_, W2, _) in features:
            b2 = W2.bbox()
            if not (bb[3] + 3 < b2[0] or b2[3] + 3 < bb[0] or bb[4] + 3 < b2[1] or b2[4] + 3 < bb[1] or bb[5] + 3 < b2[2] or b2[5] + 3 < bb[2]):
                if check:
                    return False
        if zone == 'c' and check and not box_path_clear(bb, margin):
            return False
        features.append((name, V, zone))
        return True

    # Anneaux (toujours)
    for i in range(N):
        add_feature(f'anneau {i+1}', lambda V, i=i: ring(V, i), 'c', check=False)
    # Île sous la plateforme de départ (plus petite que la plateforme : on tombe dans le vide en sautant)
    add_feature('socle départ', lambda V: island(V, PAD1[0], PAD1[1] - 1, PAD1[2], 5, rng, depth=14, trees=False, top='stone'), 'c', check=False)
    # Arches autour de quelques anneaux (plan de l'anneau)
    for i in (2, 7, 12, 18):
        x, y, z, size, _ = RINGS[i]
        add_feature(f'arche {i+1}', lambda V, x=x, y=y, z=z, i=i: arch(V, x, y - 2, z, AXES[i], 13, rng), 'c', check=False)

    # Îles suspendues bien visibles sous/à côté de la trajectoire
    placed = 0
    for _ in range(4000):
        if placed >= 14:
            break
        i = rng.randrange(N)
        x, y, z, _, _ = RINGS[i]
        r = rng.randint(8, 15)
        px, pz = x + rng.randint(-40, 40), z + rng.randint(-40, 40)
        py = y + rng.randint(-34, -14)
        if add_feature('île', lambda V: island(V, px, py, pz, r, rng), 'c', margin=r * 0.4 + 8):
            placed += 1
    placed = 0
    for _ in range(4000):
        if placed >= 6:
            break
        x, z = rng.randint(-185, 185), rng.randint(27630, 28380)
        a, b, H = rng.randint(10, 16), rng.randint(4, 7), rng.randint(45, 75)
        y0 = rng.randint(95, 150)
        if add_feature('falaise', lambda V: cliff(V, x, y0, z, a, b, H, rng.random() * 3.14, rng), 'c', margin=10):
            placed += 1
    placed = 0
    for _ in range(4000):
        if placed >= 4:
            break
        x, z = rng.randint(-180, 180), rng.randint(27640, 28370)
        r, H = rng.randint(3, 5), rng.randint(30, 55)
        y0 = rng.randint(110, 160)
        if add_feature('tour', lambda V: tower(V, x, y0, z, r, H, rng), 'c', margin=10):
            placed += 1
    placed = 0
    for _ in range(4000):
        if placed >= 9:
            break
        x, z, y = rng.randint(-185, 185), rng.randint(27620, 28385), rng.randint(140, 240)
        if add_feature('nuage', lambda V: cloud(V, x, y, z, rng), 'c', margin=9):
            placed += 1

    # ---- Arène (mode 3)
    for (cx, cz) in COLS:
        add_feature('colonne de vent', lambda V, cx=cx, cz=cz: wind_column(V, cx, cz), 'a', check=False)
    for k in range(16):
        ang = math.radians(k * 22.5 + rng.uniform(-6, 6))
        rad = rng.uniform(80, 90)
        x, z = round(ARENA[0] + rad * math.cos(ang)), round(ARENA[1] + rad * math.sin(ang))
        if k % 2 == 0:
            add_feature('pic', lambda V, x=x, z=z: spike(V, x, rng.randint(105, 140), z, rng.randint(4, 6), rng.randint(32, 55), True, rng), 'a', check=False)
        else:
            add_feature('pic suspendu', lambda V, x=x, z=z: spike(V, x, rng.randint(195, 212), z, rng.randint(4, 6), rng.randint(30, 50), False, rng), 'a', check=False)
    placed = 0
    for _ in range(4000):
        if placed >= 8:
            break
        ang, rad = rng.random() * 6.283, rng.uniform(24, 64)
        x, z = round(ARENA[0] + rad * math.cos(ang)), round(ARENA[1] + rad * math.sin(ang))
        if min(math.hypot(x - cx, z - cz) for cx, cz in COLS) < 16:
            continue
        r, y = rng.randint(5, 9), rng.randint(115, 180)
        if add_feature('rocher', lambda V: island(V, x, y, z, r, rng), 'a'):
            placed += 1
    placed = 0
    for _ in range(4000):
        if placed >= 4:
            break
        ang, rad = rng.random() * 6.283, rng.uniform(26, 70)
        x, z = round(ARENA[0] + rad * math.cos(ang)), round(ARENA[1] + rad * math.sin(ang))
        if min(math.hypot(x - cx, z - cz) for cx, cz in COLS) < 12:
            continue
        if add_feature('pilier', lambda V: pillar(V, x, rng.randint(110, 140), z, rng.randint(28, 45), rng), 'a'):
            placed += 1

    # =====================================================================================
    # Sections de construction
    # =====================================================================================
    CELL = 96
    sections = {}
    for (name, V, zone) in features:
        bb = V.bbox()
        key = (zone, (bb[0] + bb[3]) // 2 // CELL, (bb[2] + bb[5]) // 2 // CELL)
        sections.setdefault(key, []).append((name, V))

    sec_keys = sorted(sections, key=sec_order)
    steps_b, steps_w = [], []
    stats = []
    PART_VOL = 14000
    os.makedirs(SUB, exist_ok=True)
    for si, key in enumerate(sec_keys):
        feats = sections[key]
        merged = Vox()
        for (_, V) in feats:
            merged.v.update(V.v)
        bbs = [V.bbox() for (_, V) in feats]
        x0, z0 = min(b[0] for b in bbs), min(b[2] for b in bbs)
        x1, z1 = max(b[3] for b in bbs), max(b[5] for b in bbs)
        nch = ((x1 >> 4) - (x0 >> 4) + 1) * ((z1 >> 4) - (z0 >> 4) + 1)
        assert nch <= 256, (key, nch)
        W(f'b/fl{si}', [f'# Section {si} : chargement temporaire ({", ".join(sorted(set(n for n, _ in feats)))})',
                       f'forceload add {x0} {z0} {x1} {z1}', 'return 1'])
        ld = [f'# Section {si} : 1 quand tous les tronçons sont chargés']
        for cx in range(x0 >> 4, (x1 >> 4) + 1):
            for cz in range(z0 >> 4, (z1 >> 4) + 1):
                ld.append(f'execute unless loaded {cx * 16 + 8} 100 {cz * 16 + 8} run return 0')
        ld.append('return 1')
        W(f'b/ld{si}', ld)
        W(f'b/rm{si}', [f'forceload remove {x0} {z0} {x1} {z1}', 'return 1'])
        cmds = to_cmds(merged.v)
        parts, cur, vol = [], [], 0
        for (v, _, c) in cmds:
            if cur and (vol + v > PART_VOL or len(cur) >= 250):
                parts.append(cur)
                cur, vol = [], 0
            cur.append(c)
            vol += v
        if cur:
            parts.append(cur)
        steps_b += [f'b/fl{si}', f'b/ld{si}']
        for pi, p in enumerate(parts):
            W(f'b/s{si}_{pi}', [f'# Section {si}, morceau {pi + 1}/{len(parts)} (généré)'] + p + ['return 1'])
            steps_b.append(f'b/s{si}_{pi}')
        steps_b.append(f'b/rm{si}')
        wipe = [f'# Section {si} : effacement du décor (boîtes englobantes)']
        for (_, V) in feats:
            a0, b0, c0, a1, b1, c1 = V.bbox()
            h = max(1, 32768 // ((a1 - a0 + 1) * (c1 - c0 + 1)))
            y = b0
            while y <= b1:
                wipe.append(f'fill {a0} {y} {c0} {a1} {min(b1, y + h - 1)} {c1} minecraft:air')
                y += h
        W(f'b/w{si}', wipe + ['return 1'])
        steps_w += [f'b/fl{si}', f'b/ld{si}', f'b/w{si}', f'b/rm{si}']
        stats.append((si, key, len(cmds), len(parts), nch, len(merged.v)))

    W('b_step', ['# Étape courante de la construction ($skbs) — renvoie 1 si terminée, 0 s\'il faut attendre (généré)']
      + [f'execute if score $skbs mg.st matches {i} run return run function {NS}/{s}' for i, s in enumerate(steps_b)] + ['return 1'])
    W('w_step', ['# Étape courante de l\'effacement ($skbs) — renvoie 1 si terminée, 0 s\'il faut attendre (généré)']
      + [f'execute if score $skbs mg.st matches {i} run return run function {NS}/{s}' for i, s in enumerate(steps_w)] + ['return 1'])
    W('fl_secs_off', ['# Retire tous les chargements temporaires des sections (construction interrompue)']
      + [f'function {NS}/b/rm{si}' for si in range(len(sec_keys))])

    return features, sec_keys, steps_b, steps_w, stats
