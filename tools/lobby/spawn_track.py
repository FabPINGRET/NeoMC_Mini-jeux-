# Spawn : circuit du spawn (kart libre) : spline, tangentes, points de passage ; exécuté par gen_lobby.py (exec) après la place, les jardins et les ponts.
# Utilise : G, ISET, W, math, paint, put

# ------------------------------------------------------------------ CIRCUIT DU SPAWN (kart libre) : départ derrière le garage, sort de l'île
# entre les plots 3 et 4, grande boucle au sud au-dessus du vide (saut, boosts), revient entre les plots 4 et 5.
KWP = [(0, 66), (9, 66.5), (15, 69), (18.5, 76), (18.5, 84), (18.5, 96), (18.5, 108), (19, 115), (28, 124), (48, 131), (72, 136), (92, 150),
       (100, 172), (92, 196), (70, 208), (50, 203), (40, 188), (28, 172), (10, 166), (-8, 174), (-24, 192), (-46, 208), (-72, 210), (-94, 196),
       (-102, 170), (-92, 146), (-70, 132), (-48, 126), (-28, 124), (-19, 115), (-18.5, 108), (-18.5, 96), (-18.5, 84), (-18.5, 76), (-15, 69), (-9, 66.5)]
def catmull(p0, p1, p2, p3, t):
    t2, t3 = t * t, t * t * t
    return tuple(0.5 * ((2 * p1[i]) + (-p0[i] + p2[i]) * t + (2 * p0[i] - 5 * p1[i] + 4 * p2[i] - p3[i]) * t2 + (-p0[i] + 3 * p1[i] - 3 * p2[i] + p3[i]) * t3) for i in (0, 1))
kraw = []
for i in range(len(KWP)):
    p0, p1, p2, p3 = KWP[i - 1], KWP[i], KWP[(i + 1) % len(KWP)], KWP[(i + 2) % len(KWP)]
    for k in range(40): kraw.append(catmull(p0, p1, p2, p3, k / 40))
KP = [kraw[0]]; acc = 0.0
for a, b in zip(kraw, kraw[1:] + kraw[:1]):
    d = math.dist(a, b)
    while acc + d >= 0.5:
        t = (0.5 - acc) / d; a = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t); d = math.dist(a, b); KP.append(a); acc = 0.0
    acc += d
KN = len(KP)
def ktan(i):
    a, b = KP[(i - 2) % KN], KP[(i + 2) % KN]; L = math.dist(a, b) or 1
    return ((b[0] - a[0]) / L, (b[1] - a[1]) / L)
def kyaw(dx, dz): return round(math.degrees(math.atan2(-dx, dz)), 1)
kworst = min(math.dist(KP[i], KP[j]) for i in range(0, KN, 4) for j in range(i + 80, KN - (80 if i < 80 else 0), 4))
assert kworst > 16, ('le circuit se croise', kworst)
kbuck = {}
for i, (x, z) in enumerate(KP): kbuck.setdefault((math.floor(x / 4), math.floor(z / 4)), []).append(i)
def knear(x, z):
    best, bi = 1e9, -1
    for gx in range(math.floor(x / 4) - 2, math.floor(x / 4) + 3):
        for gz in range(math.floor(z / 4) - 2, math.floor(z / 4) + 3):
            for i in kbuck.get((gx, gz), ()):
                d = (KP[i][0] - x) ** 2 + (KP[i][1] - z) ** 2
                if d < best: best, bi = d, i
    return (math.sqrt(best), bi) if bi >= 0 else (99, -1)
KJ = min(range(KN), key=lambda i: math.dist(KP[i], (-59, 209)))
KBOOST = [int(f * KN) for f in (0.12, 0.36, 0.62, 0.86)]
KSTAMP = {}
def kstamp(i, w1, w2, l1, l2, fn):
    cx, cz = KP[i]; tx, tz = ktan(i); nx, nz = -tz, tx
    for a in [l1 + k * 0.5 for k in range(int((l2 - l1) * 2) + 1)]:
        for b in [w1 + k * 0.5 for k in range(int((w2 - w1) * 2) + 1)]:
            KSTAMP[(round(cx + tx * a + nx * b), round(cz + tz * a + nz * b))] = fn(round(a), round(b))
kstamp(0, -4.5, 4.5, -1, 1, lambda a, b: 'black_concrete' if (a + b) % 2 else 'white_concrete')
for bi in KBOOST: kstamp(bi, -2, 2, 0, 3, lambda a, b: 'orange_glazed_terracotta')
kstamp((KJ - 14) % KN, -4.5, 4.5, 0, 1.5, lambda a, b: 'lime_concrete')
def kgap(x, z):
    jx, jz = KP[KJ]; tx, tz = ktan(KJ)
    return abs((x - jx) * tx + (z - jz) * tz) <= 2.5 and abs((x - jx) * -tz + (z - jz) * tx) < 9
KROADC = set()
for x in range(-115, 116):
    for z in range(55, 225):
        d, si = knear(x, z)
        if d > 5.5 or kgap(x, z): continue
        onisl = (x, z) in ISET
        if d <= 4.5:
            b = KSTAMP.get((x, z)) or ('gray_concrete' if d <= 3.5 else ('white_concrete' if d <= 4 else ('red_concrete' if (si // 6) % 2 else 'white_concrete')))
            KROADC.add((x, z))
            if onisl:
                paint(x, z, b, 'b')
                for y in range(64, 70): W.pop((x, y, z), None)
            else:
                put(x, G, z, b); put(x, G - 1, z, 'stone_bricks')
                if si % 16 == 0 and d < 1: put(x, G + 2, z, 'light[level=13]')
        elif not onisl:
            put(x, G, z, 'stone_bricks'); put(x, G - 1, z, 'stone_brick_slab[type=top]')
            put(x, G + 1, z, 'red_concrete' if (si // 8) % 2 else 'white_concrete'); put(x, G + 2, z, 'barrier')
            if si % 24 == 0: put(x, G + 3, z, 'lantern')
# portique de départ en damier et tapis d'embarquement (garage)
sx_, sz_ = KP[0]; tx_, tz_ = ktan(0); nx_, nz_ = -tz_, tx_
for o in (-6.5, 6.5):
    px, pz = round(sx_ + nx_ * o), round(sz_ + nz_ * o)
    for y in range(G, 71): put(px, y, pz, 'black_concrete' if y % 2 else 'white_concrete')
for o in [k * 0.5 for k in range(-13, 14)]:
    px, pz = round(sx_ + nx_ * o), round(sz_ + nz_ * o)
    for y in (71, 72): put(px, y, pz, 'black_concrete' if (px + pz + y) % 2 else 'white_concrete')
KPAD = (-1, 54)
for x in range(KPAD[0], KPAD[0] + 3):
    for z in range(KPAD[1], KPAD[1] + 3): paint(x, z, 'yellow_glazed_terracotta' if (x, z) != (KPAD[0] + 1, KPAD[1] + 1) else 'gold_block', 'b')
KK = int(KN * 0.5 / 10)
KCPS = []
for k in range(KK):
    i = int(k * KN / KK)
    if (i - KJ) % KN < 12 or (KJ - i) % KN < 8: i = (KJ + 16) % KN            # jamais dans le trou du saut : après la réception
    x, z = KP[i]; tx, tz = ktan(i)
    KCPS.append((round(x, 1), round(z, 1), kyaw(tx, tz)))
print('circuit du spawn : longueur', round(KN * 0.5), '| points de passage', KK, '| écart mini', round(kworst, 1))

