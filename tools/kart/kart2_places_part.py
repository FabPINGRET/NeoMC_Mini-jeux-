# Lieux : départ, ville, pyramide, château, lac (structures posées via S()) : exécuté par gen_kart2.py (exec) dans l'ordre des parts.
# Utilise : B, BE, CA, CB, H, HX, HZ, LAKE, NP, PYR, ROAD, ROADSET, START, W, WALLD, basalt_pillar, bush, cactus,
#   cardinal, cloud, col, disc, fl, flag, frame, free, jungle_tree, lamp, math, mushroom, near_wp, occ, palm, pipe,
#   pts, qblock, random, region, rock, sb, sdist, spot, toad_house, tree, umbrella, yaw_of
# ------------------------------------------------------------------ structures
struct_ = []
def S(s): struct_.append(s)

# Ville : portique de départ, tribunes avec spectateurs, drapeaux, maisons Toad, fontaine, lampadaires
sx, sz, tx, tz, nx, nz, ry = frame(START)
SEATS = []
for side in (-1, 1):
    px, pz = round(sx + nx * 9 * side), round(sz + nz * 9 * side)
    fl(px, ry + 1, pz, px, ry + 10, pz, 'black_concrete')
    sb(px, ry + 11, pz, 'sea_lantern')
for b in range(-9, 10):
    x, z = round(sx + nx * b), round(sz + nz * b)
    sb(x, ry + 11, z, 'black_concrete' if b % 2 else 'white_concrete')
    sb(x, ry + 12, z, 'white_concrete' if b % 2 else 'black_concrete')
    if b in (-4, -2, 0, 2, 4): sb(x, ry + 10, z, 'redstone_lamp[lit=true]')
for side in (-1, 1):
    for k in range(-22, 23):
        for row in range(6):
            x, z = round(sx + tx * k + nx * (12 + row) * side), round(sz + tz * k + nz * (12 + row) * side)
            if (x, z) in col and (x, z) not in ROADSET:
                colr = ['red', 'blue', 'yellow', 'lime', 'orange', 'light_blue'][(k // 4) % 6]
                fl(x, ry + 1, z, x, ry + 1 + row, z, f'{colr}_concrete')
                occ.add((x, z))
                if k % 3 == 0 and row in (1, 3, 5): SEATS.append((x + 0.5, ry + 2 + row, z + 0.5, yaw_of(-nx * side, -nz * side)))
    for k in (-24, 24):
        x, z = round(sx + tx * k + nx * 14 * side), round(sz + tz * k + nz * 14 * side)
        fl(x, ry + 1, z, x, ry + 11, z, 'white_concrete')
        fl(x, ry + 9, z, x + 2, ry + 11, z, 'red_wool' if side < 0 else 'blue_wool')
for i in range(0, NP, 28):
    if region(*pts[i]) != 'ville': continue
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    for side in (-1, 1):
        x, z = round(cx + nx2 * 9.5 * side), round(cz + nz2 * 9.5 * side)
        if (x, z) in col and free(x, z, 0) and not col[(x, z)]['liq']: lamp(x, z); occ.add((x, z))
for k in range(14):
    p = spot('ville', 14, 6)
    if p:
        x, z = p
        toad_house(x, z, cardinal(*(lambda c: (pts[c][0] - x, pts[c][1] - z))(col[(x, z)]['i'])))
for k in range(10):
    p = spot('ville', 10, 1)
    if p: flag(p[0], p[1], random.choice(['red', 'blue', 'yellow', 'lime', 'orange', 'purple']))
p = spot('ville', 16, 5)
if p:
    x, z = p; y = H(x, z) + 1
    disc(x, y, z, 4, 'stone_bricks'); disc(x, y + 1, z, 3, 'water'); fl(x, y, z, x, y + 3, z, 'quartz_pillar')
    sb(x, y + 4, z, 'water')

# Plage : palmiers, parasols, rochers, tour de sauveteur
for k in range(36):
    p = spot('plage', 10, 2, tops={'sand'})
    if p: palm(*p)
for k in range(16):
    p = spot('plage', 9, 2, tops={'sand'})
    if p: umbrella(*p)
for k in range(10):
    p = spot('plage', 9, 2, tops={'sand'})
    if p: rock(*p, random.choice(['andesite', 'stone', 'tuff']))
p = spot('plage', 12, 3, tops={'sand'})
if p:
    x, z = p; y = H(x, z) + 1
    for a, b in ((-1, -1), (1, -1), (-1, 1), (1, 1)): fl(x + a, y, z + b, x + a, y + 4, z + b, 'oak_fence')
    fl(x - 1, y + 5, z - 1, x + 1, y + 5, z + 1, 'oak_planks'); fl(x - 1, y + 8, z - 1, x + 1, y + 8, z + 1, 'red_wool')
    for a, b in ((-1, -1), (1, -1), (-1, 1), (1, 1)): fl(x + a, y + 6, z + b, x + a, y + 7, z + b, 'oak_fence')

# Jungle : grands arbres, buissons, tuyaux, ruines
for k in range(70):
    p = spot('jungle', 11, 3)
    if p: jungle_tree(*p)
for k in range(90):
    p = spot('jungle', 9, 1)
    if p: bush(*p, random.choice(['oak', 'jungle', 'azalea']))
for k in range(4):
    p = spot('jungle', 14, 5)
    if p:
        x, z = p; y = H(x, z) + 1
        for a in (-4, 4):
            for b in (-4, 4): fl(x + a, y, z + b, x + a, y + random.randint(3, 7), z + b, 'mossy_stone_bricks')
        fl(x - 4, y, z - 4, x + 4, y, z + 4, 'mossy_cobblestone')
        fl(x - 1, y + 1, z - 1, x + 1, y + 1, z + 1, 'chiseled_stone_bricks')

# Désert : pyramide traversée par la piste, cactus, buissons morts, oasis, ruines
px0, pz0, ptx, ptz, pnx, pnz, pry = frame(PYR)
PX, PZ = round(px0), round(pz0)
for k in range(0, 24):
    hb = 24 - k
    S(f'fill {PX - hb} {pry + 1 + k} {W(PZ - hb)} {PX + hb} {pry + 1 + k} {W(PZ + hb)} minecraft:{"sandstone" if k % 3 else "smooth_sandstone"}')
S(f'setblock {PX} {pry + 25} {W(PZ)} minecraft:gold_block')
TUNNEL = []
for (x, z), c in col.items():
    if abs(x - PX) <= 25 and abs(z - PZ) <= 25 and c['d'] <= WALLD + 1.5 and c['i'] >= 0 and abs(sdist(PYR, c['i'])) < 40:
        TUNNEL.append(f'fill {x} {c["h"] + 1} {W(z)} {x} {c["h"] + 7} {W(z)} minecraft:air')
        if c['d'] > WALLD + 0.5:
            TUNNEL.append(f'setblock {x} {c["h"] + 4} {W(z)} minecraft:chiseled_sandstone')
        elif c['d'] < 1 and (c['i'] // 8) % 2 == 0:
            TUNNEL.append(f'setblock {x} {c["h"] + 8} {W(z)} minecraft:sea_lantern')
for (x, z), c in col.items():
    if abs(x - PX) <= 25 and abs(z - PZ) <= 25: occ.add((x, z))
for k in range(70):
    p = spot('desert', 9, 1, tops={'sand', 'red_sand'})
    if p: cactus(*p)
for k in range(60):
    p = spot('desert', 8, 0, tops={'sand', 'red_sand'})
    if p: sb(p[0], H(*p) + 1, p[1], 'dead_bush')
for k in range(8):
    p = spot('desert', 12, 3)
    if p:
        x, z = p; y = H(x, z) + 1
        fl(x, y, z, x, y + random.randint(3, 8), z, random.choice(['cut_sandstone', 'chiseled_sandstone', 'sandstone']))
        sb(x + 1, y, z, 'bone_block')
p = spot('desert', 16, 6)
if p:
    x, z = p; y = H(x, z)
    disc(x, y, z, 4, 'water'); disc(x, y - 1, z, 4, 'sand')
    for a, b in ((-6, 0), (6, 0), (0, 6), (0, -6)):
        if (x + a, z + b) in col: palm(x + a, z + b)

# Volcan : château de Bowser (murs, tours, créneaux, statue), piliers de basalte, colonnes de lave du pont
castle = []
def C(s): castle.append(s)
for (x, z), c in col.items():
    if c.get('cwall'):
        C(f'fill {x} {c["h"] + 1} {W(z)} {x} {c["cwall"]} {W(z)} minecraft:{"polished_blackstone_bricks" if (x + z) % 9 else "cracked_polished_blackstone_bricks"}')
        if c['d'] > 11.6 and (x + z) % 2 == 0: C(f'setblock {x} {c["roof"] + 1} {W(z)} minecraft:nether_brick_wall')
    if c.get('roof'):
        C(f'setblock {x} {c["roof"]} {W(z)} minecraft:nether_bricks')
        if c['d'] < 1 and (c['i'] // 10) % 2 == 0: C(f'setblock {x} {c["roof"]} {W(z)} minecraft:shroomlight')
        if WALLD < c['d'] <= 10.5 and (c['i'] // 14) % 3 == 0 and (x + z) % 3 == 0:
            C(f'setblock {x} {c["roof"] - 1} {W(z)} minecraft:soul_lantern[hanging=true]')
for (i, side) in ((CA, -1), (CA, 1), (CB, -1), (CB, 1)):
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    ox, oz = round(cx + nx2 * 14 * side), round(cz + nz2 * 14 * side)
    for a in range(-4, 5):
        for b in range(-4, 5):
            if a * a + b * b <= 17: C(f'fill {ox + a} {ry2 - 2} {W(oz + b)} {ox + a} {ry2 + 20} {W(oz + b)} minecraft:nether_bricks')
    for a in range(-5, 6):
        for b in range(-5, 6):
            if a * a + b * b <= 26 and (a + b) % 2 == 0: C(f'setblock {ox + a} {ry2 + 21} {W(oz + b)} minecraft:nether_brick_wall')
    for k, r in enumerate((4, 3, 3, 2, 1, 1)):
        for a in range(-r, r + 1):
            for b in range(-r, r + 1):
                if a * a + b * b <= r * r: C(f'setblock {ox + a} {ry2 + 22 + k} {W(oz + b)} minecraft:red_nether_bricks')
    C(f'setblock {ox} {ry2 + 28} {W(oz)} minecraft:shroomlight')
    for k in range(6, 19, 6): C(f'setblock {round(ox - nx2 * 4.5 * side)} {ry2 + k} {W(round(oz - nz2 * 4.5 * side))} minecraft:iron_bars')
    for (x, z), c in col.items():
        if (x - ox) ** 2 + (z - oz) ** 2 <= 30: occ.add((x, z))
# portes : arche d'entrée et de sortie
for i in (CA, CB):
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    for b in range(-12, 13):
        x, z = round(cx + nx2 * b), round(cz + nz2 * b)
        if abs(b) >= 8: C(f'fill {x} {ry2 + 1} {W(z)} {x} {ry2 + 13} {W(z)} minecraft:nether_bricks')
        else: C(f'fill {x} {ry2 + 11} {W(z)} {x} {ry2 + 14} {W(z)} minecraft:nether_bricks')
        if abs(b) <= 7 and b % 2 == 0: C(f'setblock {x} {ry2 + 15} {W(z)} minecraft:nether_brick_wall')
    for b in (-7, 7):
        x, z = round(cx + nx2 * b), round(cz + nz2 * b)
        C(f'setblock {x} {ry2 + 9} {W(z)} minecraft:soul_lantern[hanging=true]')
# statue de Bowser sur le toit de l'entrée, tournée vers les karts qui arrivent
cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(CA)
fwd = cardinal(-tx2, -tz2)
sox, soz, soy = round(cx), round(cz), ry2 + 15
G, Y, O, R, Wb, K = 'lime_terracotta', 'yellow_terracotta', 'orange_terracotta', 'red_wool', 'white_concrete', 'black_concrete'
STATUE = [(-1, 1, -4, -2, 0, 1, O), (-1, 1, 2, 4, 0, 1, O),                       # pieds
          (-1, 1, -3, -2, 2, 4, G), (-1, 1, 2, 3, 2, 4, G),                       # jambes
          (-2, 2, -4, 4, 5, 12, G), (1, 2, -3, 3, 5, 11, Y),                      # corps, ventre
          (-5, -3, -5, 5, 5, 13, 'green_concrete'), (-6, -6, -4, 4, 6, 12, Wb),   # carapace et bord
          (-7, -7, -3, -3, 8, 8, Wb), (-7, -7, 0, 0, 10, 10, Wb), (-7, -7, 3, 3, 8, 8, Wb), (-7, -7, 0, 0, 6, 6, Wb),  # pointes
          (-1, 3, -7, -5, 9, 10, O), (-1, 3, 5, 7, 9, 10, O), (2, 3, -7, -6, 11, 11, K), (2, 3, 6, 7, 11, 11, K),    # bras
          (-2, 3, -3, 3, 13, 18, G), (3, 5, -2, 2, 13, 15, Y), (4, 5, -2, 2, 13, 13, 'magma_block'),               # tête, museau, gueule
          (4, 5, -2, -2, 14, 14, Wb), (4, 5, 2, 2, 14, 14, Wb),                                                    # crocs
          (3, 3, -2, -1, 16, 17, Wb), (3, 3, 1, 2, 16, 17, Wb), (3, 3, -1, -1, 16, 16, K), (3, 3, 1, 1, 16, 16, K),  # yeux
          (-3, 0, -3, 3, 19, 20, R), (-4, -3, -2, 2, 14, 19, R),                                                   # cheveux
          (-1, 0, -4, -4, 19, 22, Wb), (-1, 0, 4, 4, 19, 22, Wb)]                                                   # cornes
for (u1, u2, v1, v2, y1, y2, blk) in STATUE:
    fx, fz = fwd; vx, vz = -fz, fx
    C(f'fill {sox + fx * u1 + vx * v1} {soy + y1} {W(soz + fz * u1 + vz * v1)} {sox + fx * u2 + vx * v2} {soy + y2} {W(soz + fz * u2 + vz * v2)} minecraft:{blk}')
# piles du pont au-dessus de la lave + garde-corps
for i in range(CB, CB + ((BE - CB) % NP), 14):
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    for side in (-1, 1):
        x, z = round(cx + nx2 * 6 * side), round(cz + nz2 * 6 * side)
        C(f'fill {x} {ROAD - 3} {W(z)} {x} {ry2 - 1} {W(z)} minecraft:nether_bricks')
        C(f'setblock {x} {ry2 + 1} {W(z)} minecraft:nether_brick_fence')
        C(f'setblock {x} {ry2 + 2} {W(z)} minecraft:soul_lantern')
# piles du pont de la jungle
for (x, z), c in col.items():
    if c['bridge'] and c['reg'] == 'jungle' and c['wall'] and (x + z) % 4 == 0:
        C(f'fill {x} {c["bed"] + 1} {W(z)} {x} {c["h"] - 1} {W(z)} minecraft:stripped_spruce_log')
for k in range(40):
    p = spot('volcan', 10, 1)
    if p: basalt_pillar(*p)
for k in range(14):
    p = spot('volcan', 10, 0)
    if p: sb(p[0], H(*p) + 1, p[1], random.choice(['soul_campfire', 'crying_obsidian', 'obsidian']))

# Centre : lac et son île au bloc ?, arc-en-ciel, montagne, champignons, arbres, tuyaux, nuages, blocs ? volants
lx, lz, la, lb = LAKE
qblock(lx - 2, ROAD + 5, lz - 2); fl(lx - 2, ROAD + 2, lz - 2, lx + 3, ROAD + 2, lz + 3, 'grass_block')
fl(lx - 2, ROAD + 3, lz - 2, lx + 3, ROAD + 4, lz + 3, 'yellow_concrete'); fl(lx - 1, ROAD + 3, lz - 1, lx + 2, ROAD + 4, lz + 2, 'orange_concrete')
RAIN = ['red', 'orange', 'yellow', 'lime', 'light_blue', 'blue', 'purple']
RBI = near_wp(-15, -25)
rcx, rcz, rtx, rtz, rnx, rnz, rry = frame(RBI)
for band, colr in enumerate(RAIN):
    r = 26 - band
    for a in range(0, 181):
        th = math.radians(a)
        bx, bz, y = rcx + rnx * r * math.cos(th), rcz + rnz * r * math.cos(th), round(rry + r * math.sin(th) * 0.75)
        for k in (-1, 0, 1):
            B(f'setblock {round(bx + rtx * k)} {y} {W(round(bz + rtz * k))} minecraft:{colr}_concrete')
for k in range(26):
    p = spot('centre', 14, 5)
    if p: mushroom(*p, big=random.random() < 0.3)
for k in range(70):
    p = spot('centre', 11, 3)
    if p and H(*p) < ROAD + 10: tree(*p)
for k in range(6):
    p = spot('centre', 12, 4)
    if p: pipe(*p, random.randint(4, 7))
for k in range(26):
    cloud(random.randint(-HX + 10, HX - 10), random.randint(100, 118), random.randint(-HZ + 10, HZ - 10))
for i in range(0, NP, 150):
    cx, cz, tx2, tz2, nx2, nz2, ry2 = frame(i)
    x, z = round(cx + nx2 * 11), round(cz + nz2 * 11)
    if (x, z) in col and not col[(x, z)].get('roof'): qblock(x, ry2 + 8, z)
for (x, z), c in col.items():
    if (x, z) in occ or c['d'] < 9 or c['liq'] or c.get('roof'): continue
    r = random.random()
    if c['top'] == 'grass_block' and r < 0.07:
        sb(x, c['h'] + 1, z, random.choice(['poppy', 'dandelion', 'cornflower', 'oxeye_daisy', 'red_tulip', 'short_grass', 'short_grass', 'short_grass']))
    elif c['top'] in ('podzol', 'moss_block') and r < 0.18:
        sb(x, c['h'] + 1, z, random.choice(['fern', 'short_grass', 'fern']))
