# Terrain : zones (zone_set), tampon de blocs (stamp), signature, murs du bord de piste : exécuté par gen_kart2.py (exec) dans l'ordre des parts.
# Utilise : BE, BOOSTS, CA, CB, GAPH, GAPL, GAPW, HW, HX, HZ, LAGOON, NP, PAL, QUICK, RIVER, ROAD, RY, SEA, START, W,
#   WALLD, YB, base, frame, in_range, island, math, nearest, pts, region, river_d, sdist
# ------------------------------------------------------------------ colonnes
col = {}
ROADSET = set()
for x in range(-HX, HX + 1):
    for z in range(-HZ, HZ + 1):
        d, si = nearest(x, z)
        e = island(x, z)
        if d <= 18: e = min(e, 0.9)
        if e > 1.0: continue
        reg = region(x, z)
        h, top, sub, core, liq, lvl = base(x, z, reg)
        c = {'top': top, 'sub': sub, 'core': core, 'liq': liq, 'lvl': lvl, 'd': d, 'i': si, 'wall': False, 'reg': reg,
             'bridge': False, 'roof': None, 'cwall': None}
        if reg == 'plage' and x > 215 and e <= 0.95:
            h, c['top'], c['sub'], c['liq'], c['lvl'] = 57, 'sand', 'sand', 'water', SEA
        lx, lz, lr = LAGOON
        dg = math.hypot(x - lx, z - lz)
        if dg < lr and d > 10: h, c['top'], c['sub'], c['liq'], c['lvl'] = 58, 'sand', 'sand', 'water', SEA
        if reg == 'jungle' and d > 6:
            rd = river_d(x, z)
            pond = min(math.dist((x, z), RIVER[0]), math.dist((x, z), RIVER[-1]))
            if rd < 3.5 or pond < 6: h, c['top'], c['sub'], c['liq'], c['lvl'] = 58, 'sand', 'clay', 'water', SEA
            elif rd < 5 or pond < 7.5: h, c['top'] = max(ROAD, h), 'sand'
        if si >= 0:
            ry = RY(si)
            if d <= 11 and not c['liq']:
                t = max(0, (d - 8) / 3)
                h = round(ry * (1 - t) + h * t)
            elif d <= 9 and c['liq'] and not (reg == 'jungle' and river_d(x, z) < 3.5):
                h, c['liq'] = ry, None
        if e > 0.95 and not c['liq']:
            if e > 0.975: h = min(h, ROAD - 1 - int((e - 0.975) * 80)); c['top'] = 'stone' if e > 0.988 else c['top']
            else: h = max(h, SEA + 1)
        if e > 0.95 and c['liq'] and e > 0.955: h, c['liq'], c['top'] = SEA + 1, None, 'sand'
        reg_t = region(*pts[si]) if si >= 0 else reg
        if si >= 0 and in_range(si, CA, CB) and d <= 12.5: reg_t = 'chateau'
        c['regt'] = reg_t
        if si >= 0 and d <= HW:
            ry = RY(si)
            h = ry
            road, ca, cb, _ = PAL[reg_t]
            c['top'] = road if d <= 4.5 else (ca if d <= 5.0 else (ca if (si // 6) % 2 else cb))
            c['liq'] = None
            ROADSET.add((x, z))
        elif si >= 0 and d <= WALLD:
            h = RY(si); c['wall'] = True; c['liq'] = None
            c['top'] = PAL[reg_t][1] if reg_t != 'ville' else 'white_concrete'
        c['h'] = h
        col[(x, z)] = c

def zone_set(c, h, top, liq, lvl):
    c.update(h=h, top=top, liq=liq, lvl=lvl)

for (x, z), c in col.items():
    si, d = c['i'], c['d']
    if si < 0: continue
    ry = RY(si)
    # château : canaux de lave entre la route et les murs, toit
    if in_range(si, CA, CB) and d <= 12.5:
        c['roof'] = ry + 10
        if WALLD < d <= 10.5: zone_set(c, ry - 3, 'magma_block', 'lava', ry - 1)
        elif d > 10.5: c['cwall'] = ry + 9; c['h'] = ry; c['top'] = 'nether_bricks'
    # pont au-dessus de la lave à la sortie du château
    if in_range(si, CB, BE) and d <= 17:
        if d <= WALLD: c.update(bridge=True, bed=ROAD - 3, liq='lava', lvl=ROAD - 1)
        else: zone_set(c, ROAD - 3, 'magma_block', 'lava', ROAD - 1)
    # douve de lave (saut) et bras de mer (saut)
    for g, liq, lvl, reach in ((GAPL, 'lava', ROAD - 1, 14), (GAPW, 'water', SEA, 0)):
        a = sdist(g, si)
        if abs(a) <= GAPH and d <= WALLD:
            zone_set(c, ROAD - 4, 'magma_block' if liq == 'lava' else 'sand', liq, lvl); c['wall'] = False
            ROADSET.discard((x, z)); c['gap'] = True
        elif liq == 'lava' and abs(a) <= 12 and WALLD < d <= reach:
            zone_set(c, ROAD - 3, 'magma_block', 'lava', lvl)
    # chenal du bras de mer : de la piste jusqu'à la mer (côté est) et petite crique côté ouest
    a = sdist(GAPW, si)
    if abs(a) <= GAPH and d > WALLD:
        if x > pts[GAPW][0] or d <= 11: zone_set(c, ROAD - 4, 'sand', 'water', SEA)
    if abs(a) <= GAPH + 2 and d > WALLD and not c['liq']: c['top'] = 'sand'; c['h'] = max(c['h'], ROAD - 1)
    # rivière de la jungle : pont de bois
    if c['reg'] == 'jungle' and d <= WALLD and river_d(x, z) < 4.5:
        c.update(bridge=True, bed=58, liq='water', lvl=SEA)
        if d <= HW: c['top'] = 'spruce_planks'

# ligne d'arrivée, plaques de boost, tremplins, sables mouvants
def stamp(i, w_from, w_to, l_from, l_to, block_fn):
    cx, cz, tx, tz, nx, nz, _ = frame(i)
    for a in [l_from + k * 0.5 for k in range(int((l_to - l_from) * 2) + 1)]:
        for b in [w_from + k * 0.5 for k in range(int((w_to - w_from) * 2) + 1)]:
            x, z = round(cx + tx * a + nx * b), round(cz + tz * a + nz * b)
            if (x, z) in ROADSET:
                col[(x, z)]['top'] = block_fn(round(a), round(b))
stamp(START, -4.5, 4.5, -1, 1, lambda a, b: 'black_concrete' if (a + b) % 2 else 'white_concrete')
for bi in BOOSTS:
    stamp(bi, -2, 2, 0, 3, lambda a, b: 'orange_glazed_terracotta')
for g in (GAPL, GAPW):
    stamp((g - int((GAPH + 4) * 2)) % NP, -4.5, 4.5, 0, 1.5, lambda a, b: 'lime_concrete')
stamp(QUICK, -4.5, 0.5, -6, 6, lambda a, b: 'soul_sand')

# ------------------------------------------------------------------ émission du terrain
def sig(c):
    return (c['h'], c['top'], c['sub'], c['core'], c['liq'], c['lvl'], c['bridge'], c.get('bed', 0))
terrain, seen = [], set()
for x in range(-HX, HX + 1):
    for z in range(-HZ, HZ + 1):
        if (x, z) not in col or (x, z) in seen: continue
        s = sig(col[(x, z)])
        w = 1
        while w < 16 and (x, z + w) in col and (x, z + w) not in seen and sig(col[(x, z + w)]) == s: w += 1
        hh = 1
        while hh < 16 and all((x + hh, z + k) in col and (x + hh, z + k) not in seen and sig(col[(x + hh, z + k)]) == s for k in range(w)): hh += 1
        for a in range(hh):
            for k in range(w): seen.add((x + a, z + k))
        h, top, sub, core, liq, lvl, bridge, bed = s
        x1, x2, z1, z2 = x, x + hh - 1, W(z), W(z + w - 1)
        floor = bed if bridge else h
        if floor - 4 >= YB: terrain.append(f'fill {x1} {YB} {z1} {x2} {floor - 4} {z2} minecraft:{core}')
        terrain.append(f'fill {x1} {max(YB, floor - 3)} {z1} {x2} {floor - 1} {z2} minecraft:{sub}')
        if bridge:
            terrain.append(f'fill {x1} {bed} {z1} {x2} {bed} {z2} minecraft:{"magma_block" if liq == "lava" else "sand"}')
            terrain.append(f'fill {x1} {bed + 1} {z1} {x2} {lvl} {z2} minecraft:{liq}')
            terrain.append(f'fill {x1} {h} {z1} {x2} {h} {z2} minecraft:{top}')
        else:
            terrain.append(f'fill {x1} {h} {z1} {x2} {h} {z2} minecraft:{top}')
            if liq and h + 1 <= lvl:
                terrain.append(f'fill {x1} {h + 1} {z1} {x2} {lvl} {z2} minecraft:{liq}')

# murs : barrières sur 4 blocs, décor visible selon la zone
walls = []
for (x, z), c in col.items():
    if not c['wall']: continue
    h = c['h']
    walls.append(f'fill {x} {h + 1} {W(z)} {x} {h + 4} {W(z)} minecraft:barrier')
    deco_w = PAL[c['regt']][3]
    k = (c['i'] // 10) % 5
    if deco_w == 'tire':
        if k == 0: walls.append(f'setblock {x} {h + 1} {W(z)} minecraft:black_concrete')
        elif k == 2: walls.append(f'setblock {x} {h + 1} {W(z)} minecraft:oak_fence')
    elif deco_w and (k in (0, 1, 3) or c['bridge']):
        walls.append(f'setblock {x} {h + 1} {W(z)} minecraft:{deco_w}')
