# Spawn : promenade, place, avenues, armurerie, stand, portails, garage, jardins et ponts ; exécuté par gen_lobby.py (exec) après l'île et les helpers de déco.
# Utilise : G, ISET, ISL, JETS, MASK, PLOTS, TOP, bench, box, disc, facing_of, hedge, inplot, lamp, math, paint, put, rnd, setif, vn

# ------------------------------------------------------------------ promenade circulaire + chemins vers les ponts
for (x, z) in ISL:
    r = math.hypot(x, z)
    if 60 <= r < 63.5:
        u = vn(x, z, 2.5, 7)
        paint(x, z, 'dirt_path' if u < 0.72 else ('coarse_dirt' if u < 0.9 else 'packed_mud'))

# ------------------------------------------------------------------ place centrale
for (x, z) in ISL:
    r = math.hypot(x, z)
    if r > 15.5: continue
    a = math.degrees(math.atan2(z, x)) % 360
    if r < 1.6: b = 'gold_block'
    elif r < 4.6:
        da = min(a % 45, 45 - a % 45)
        ray = r * math.sin(math.radians(da)) < 0.55
        b = ('gold_block' if round(a / 45) % 2 == 0 else 'waxed_cut_copper') if ray else 'smooth_quartz'
    elif r < 5.6: b = 'polished_blackstone_bricks'
    elif r < 9.0:
        if abs(x) <= 1 or abs(z) <= 1: b = 'smooth_quartz'
        else: b = 'water'; MASK[(x, z)] = 'w'
    elif r < 10.0: b = 'chiseled_stone_bricks' if int(a / 15) % 2 == 0 and a % 15 < 4 else 'stone_bricks'
    elif r < 14.5: b = ['polished_andesite', 'polished_diorite'][(int(r) + int(a / 11.25)) % 2]
    else: b = 'gilded_blackstone' if a % 45 < 3 else 'polished_blackstone_bricks'
    if b == 'water': TOP[(x, z)] = 'water'
    else: paint(x, z, b)
for (x, z) in ISL:          # fond des douves
    r = math.hypot(x, z)
    if 5.6 <= r < 9.0 and TOP[(x, z)] == 'water':
        a = math.degrees(math.atan2(z, x)) % 360
        put(x, 62, z, 'sea_lantern' if a % 30 < 4 and 7 <= r < 8 else ('dark_prismarine' if (x + z) % 3 == 0 else 'prismarine'))
for sx in (-5, 5):          # jets d'eau sur les diagonales
    for sz in (-5, 5):
        TOP[(sx, sz)] = 'prismarine_bricks'
        put(sx, 64, sz, 'prismarine_bricks'); put(sx, 65, sz, 'prismarine_bricks'); put(sx, 66, sz, 'sea_lantern')
        JETS.append((sx, 67, sz))
for k in range(8):          # lampadaires et massifs de fleurs autour de la place
    a = math.radians(22.5 + 45 * k)
    lamp(round(14 * math.cos(a)), round(14 * math.sin(a)))
for k in range(4):
    a = math.radians(45 + 90 * k); cx, cz = 11.6 * math.cos(a), 11.6 * math.sin(a)
    for (x, z) in disc(cx, cz, 1.9):
        paint(x, z, 'grass_block', 'f')
    put(round(cx), 64, round(cz), 'flowering_azalea')

# ------------------------------------------------------------------ avenues
def av(d, u, v):
    return {'E': (u, v), 'W': (-u, v), 'S': (v, u), 'N': (v, -u)}[d]
AVLEN = {'E': 63, 'W': 35, 'S': 36, 'N': 44}
for d, L in AVLEN.items():
    for u in range(15, L + 1):
        for v in range(-6, 7):
            x, z = av(d, u, v)
            if (x, z) not in ISET: continue
            av_ = abs(v)
            if av_ <= 2:
                q = rnd.random()
                paint(x, z, 'mossy_stone_bricks' if q < 0.06 else ('cracked_stone_bricks' if q < 0.1 else 'stone_bricks'))
            elif av_ == 3: paint(x, z, 'polished_andesite')
            elif av_ == 4: paint(x, z, 'grass_block', 'h')
            else: paint(x, z, 'grass_block', 'f')
    for u in range(17, L - 1):
        for side in (-1, 1):
            x, z = av(d, u, 4 * side)
            if (u - 17) % 10 == 0 and (u // 10 + side) % 2 == 0: lamp(x, z)
            elif (u - 22) % 10 in (0, 1, 2) and u + 2 < L - 1:
                ox, oz = av(d, u, 5 * side); bx, bz = av(d, u, 4 * side)
                bench([(x, z)], facing_of(ox - bx, oz - bz))
            elif (u - 22) % 10 in (9, 3): pass
            else: hedge(x, z)

# ------------------------------------------------------------------ ARMURERIE (ouest) + STAND DE TIR
X1, X2, Z1, Z2 = -57, -35, -11, 11
for x in range(X1 - 2, X2 + 3):
    for z in range(Z1 - 2, Z2 + 3):
        if X1 <= x <= X2 and Z1 <= z <= Z2: paint(x, z, 'polished_deepslate' if (x + z) % 2 else 'deepslate_tiles', 'b')
        else: paint(x, z, 'cobblestone' if rnd.random() < 0.3 else 'stone_bricks', 'b')
def wallb(x, y, z, along):
    if y == 64: return 'deepslate_bricks'
    if y == 71: return f'stripped_dark_oak_log[axis={along}]'
    c = x if along == 'x' else z
    if c % 4 == 0: return 'dark_oak_log'
    q = rnd.random()
    return 'mossy_stone_bricks' if q < 0.14 else ('cracked_stone_bricks' if q < 0.22 else 'stone_bricks')
for y in range(64, 72):
    for x in range(X1, X2 + 1):
        for z in (Z1, Z2):
            win = (x - X1) % 6 in (2, 3) and 66 <= y <= 68 and X1 + 1 < x < X2 - 1
            put(x, y, z, 'iron_bars' if win else wallb(x, y, z, 'x'))
    for z in range(Z1 + 1, Z2):
        for x in (X1, X2):
            if x == X2 and abs(z) <= 2 and y <= 67: continue
            put(x, y, z, wallb(x, y, z, 'z'))
put(X2, 68, 0, 'chiseled_stone_bricks')
for z in (-2, 2): put(X2, 68, z, 'stone_brick_stairs[facing=' + ('north' if z < 0 else 'south') + ',half=top]')
for z in (-4, 4):
    put(X2 + 1, 68, z, 'red_wall_banner[facing=east]'); put(X2 + 1, 66, z, 'wall_torch[facing=east]')
# panneau d'armes (mur ouest)
for z in range(-7, 8):
    for y in range(65, 70): put(X1, y, z, 'stripped_dark_oak_log[axis=z]' if y in (65, 69) or abs(z) == 7 else 'dark_oak_planks')
# toit à deux pans (faîte selon x)
for k in range(12):
    for x in range(X1 - 1, X2 + 2):
        put(x, 72 + k, -12 + k, 'dark_oak_stairs[facing=south]')
        put(x, 72 + k, 12 - k, 'dark_oak_stairs[facing=north]')
for x in range(X1 - 1, X2 + 2): put(x, 83, 0, 'dark_oak_planks'); put(x, 84, 0, 'dark_oak_slab')
for gx in (X1, X2):
    for y in range(72, 84):
        for z in range(-(11 - (y - 72)), 12 - (y - 72)):
            win = math.hypot(z, (y - 77) * 1.0) < 2.4
            put(gx, y, z, 'orange_stained_glass' if win else ('stripped_dark_oak_log[axis=y]' if z == 0 else 'dark_oak_planks'))
# tours d'angle
for (tx, tz) in ((X1, Z1), (X1, Z2), (X2, Z1), (X2, Z2)):
    for y in range(63, 82):
        for x in range(tx - 2, tx + 3):
            for z in range(tz - 2, tz + 3):
                edge_ = abs(x - tx) == 2 or abs(z - tz) == 2
                if not edge_ and y > 63: continue
                corner = abs(x - tx) == 2 and abs(z - tz) == 2
                if y == 81:
                    if (x + z) % 2 == 0: put(x, y, z, 'stone_bricks')
                    continue
                slit = not corner and (x - tx == 0 or z - tz == 0) and y in (75, 76)
                if slit: continue
                q = rnd.random()
                put(x, y, z, 'polished_deepslate' if corner else ('mossy_stone_bricks' if q < 0.15 else 'stone_bricks'))
    box(tx - 1, 80, tz - 1, tx + 1, 80, tz + 1, 'spruce_planks')
    for k, rr in enumerate((1, 0)):
        box(tx - rr, 82 + k, tz - rr, tx + rr, 82 + k, tz + rr, 'deepslate_tiles')
    for y in range(84, 87): put(tx, y, tz, 'dark_oak_fence')
    put(tx, 87, tz, 'red_banner[rotation=4]')
    put(tx, 79, tz, 'lantern[hanging=true]')
# intérieur
for x in range(-48, X2):
    for z in (-1, 0, 1): put(x, 64, z, 'red_carpet')
PADS = [(-53, -9, 'red_concrete'), (-53, -5, 'yellow_concrete'), (-53, 3, 'cyan_concrete'), (-53, 7, 'white_concrete')]
for (px, pz, c) in PADS:
    for x in range(px, px + 3):
        for z in range(pz, pz + 3):
            corner = x in (px, px + 2) and z in (pz, pz + 2)
            put(x, 63, z, c if (x, z) == (px + 1, pz + 1) else ('sea_lantern' if corner else 'polished_blackstone'))
north = ['barrel[facing=up]', 'smithing_table', 'anvil[facing=east]', 'blast_furnace[facing=south,lit=true]', 'grindstone[face=floor,facing=east]',
         'lava_cauldron', 'crafting_table', 'barrel[facing=up]', 'fletching_table', 'barrel[facing=up]']
for i, b in enumerate(north): put(-47 + i, 64, Z1 + 1, b)
put(-47, 65, Z1 + 1, 'barrel[facing=up]'); put(-38, 65, Z1 + 1, 'lantern')
south = ['hay_block', 'barrel[facing=up]', 'target', 'barrel[facing=up]', 'hay_block', 'chiseled_bookshelf[facing=north]', 'loom[facing=north]',
         'cartography_table', 'barrel[facing=up]', 'hay_block']
for i, b in enumerate(south): put(-47 + i, 64, Z2 - 1, b)
put(-47, 65, Z2 - 1, 'lantern'); put(-38, 65, Z2 - 1, 'lantern')
for cx in (-50, -42):          # lustres
    for y in range(74, 83): put(cx, y, 0, 'iron_chain')
    put(cx, 73, 0, 'lantern[hanging=true]')
    for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        put(cx + dx, 74, dz, 'iron_chain'); put(cx + dx, 73, dz, 'lantern[hanging=true]')
for x in (-55, -45, -38):
    for z in (-8, 8): put(x, 67, z, 'light[level=14]')
# stand de tir (nord de l'armurerie)
RX1, RX2, RZ1, RZ2 = -57, -37, -34, -16
for x in range(RX1, RX2 + 1):
    for z in range(RZ1, RZ2 + 1):
        lane = x in (-50, -44)
        paint(x, z, 'mud_bricks' if lane else ('packed_mud' if rnd.random() < 0.8 else 'coarse_dirt'), 'b')
for x in range(RX1, RX2 + 1):
    for y in range(64, 72): put(x, y, RZ1, 'stone_bricks' if y < 71 else 'stone_brick_slab')
for z in range(RZ1 + 1, RZ2 + 1):
    put(RX1, 64, z, 'mossy_stone_bricks'); put(RX1, 65, z, 'stone_brick_wall')
for bx in (-52, -47, -42):
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            dd = max(abs(dx), abs(dy))
            put(bx + dx, 67 + dy, RZ1, 'target' if dd == 0 else ('white_wool' if dd == 1 else 'red_wool'))
    put(bx, 64, RZ1 + 1, 'hay_block'); put(bx - 2, 64, RZ1 + 1, 'hay_block[axis=x]'); put(bx + 2, 64, RZ1 + 1, 'hay_block[axis=x]')
for tx in (-54, -48, -41):
    put(tx, 64, -25, 'oak_fence'); put(tx, 65, -25, 'hay_block'); put(tx, 66, -25, 'target')
for x in range(RX1 + 2, RX2 - 1): put(x, 64, -18, 'spruce_slab[type=top]')
for x in range(RX1 + 1, RX2): put(x, 68, -17, 'spruce_slab'); put(x, 68, -16, 'spruce_slab'); put(x, 68, -18, 'spruce_slab')
for px in (RX1 + 1, -47, RX2 - 1):
    for y in range(64, 68): put(px, y, -16, 'dark_oak_log')
for lx in (-52, -42): put(lx, 67, -17, 'lantern[hanging=true]')

# ------------------------------------------------------------------ PORTE DU PARKOUR (est)
for x in range(64, 71):
    for z in range(-4, 5):
        if (x, z) in ISET: paint(x, z, 'smooth_quartz' if (x + z) % 2 else 'quartz_bricks')
for x in range(66, 69):
    for z in range(-1, 2): paint(x, z, 'emerald_block')
for pz in (-4, 4):
    for x in (64, 65):
        for y in range(64, 72): put(x, y, pz, 'sea_lantern' if y == 67 else ('lime_stained_glass' if y in (66, 68) else 'quartz_pillar'))
for x in (64, 65):
    for z in range(-4, 5):
        put(x, 72, z, 'emerald_block' if z == 0 else 'smooth_quartz'); put(x, 73, z, 'quartz_slab' if abs(z) < 4 else 'quartz_bricks')

# ------------------------------------------------------------------ PORTAIL DES PLOTS (nord)
PC = (0, -47)
for (x, z) in disc(0, -47, 8.4):
    if (x, z) not in ISET: continue
    r = math.hypot(x, z + 47); a = math.degrees(math.atan2(z + 47, x))
    b = 'purpur_block' if r > 7.2 else ('crying_obsidian' if (a + r * 22) % 90 < 20 else 'obsidian')
    paint(x, z, b)
for z in (-48, -47):
    for x in range(-7, 8):
        for y in range(64, 79):
            d = math.hypot(x, y - 71)
            if y < 71 and abs(x) < 5: continue
            if not (5 <= d <= 6.7 or (y < 71 and 5 <= abs(x) <= 6)): continue
            if y < 71 and abs(x) > 6: continue
            put(x, y, z, 'amethyst_block' if d < 5.6 or (y < 71 and abs(x) == 5) else ('crying_obsidian' if y < 66 else 'purpur_block'))
    put(0, 78, z, 'amethyst_cluster[facing=up]')
for y in (65, 69, 73): put(0, y, -47, 'light[level=15]')
for sx in (-8, 8):
    put(sx, 64, -47, 'purpur_pillar'); put(sx, 65, -47, 'purpur_pillar'); put(sx, 66, -47, 'end_rod[facing=up]')

# ------------------------------------------------------------------ GARAGE KART (sud)
GC = (0, 48)
for (x, z) in disc(0, 48, 13.4):
    if (x, z) not in ISET: continue
    r = math.hypot(x, z - 48); a = math.degrees(math.atan2(z - 48, x)) % 360
    if r < 6: b = 'black_concrete' if ((x // 2) + (z // 2)) % 2 else 'white_concrete'
    elif r < 7: b = 'red_concrete' if int(a / 10) % 2 else 'white_concrete'
    elif r < 10: b = 'light_gray_concrete' if 8.3 <= r < 8.8 and int(a / 8) % 2 else 'gray_concrete'
    elif r < 11: b = 'red_concrete' if int(a / 10) % 2 else 'white_concrete'
    else: b = None
    if b: paint(x, z, b, 'b')
for (x0, h, b) in ((-4, 2, 'iron_block'), (-1, 3, 'gold_block'), (2, 1, 'waxed_copper_block')):
    box(x0, 64, 47, x0 + 2, 63 + h, 49, b)
for px in (-6, 6):
    for y in range(64, 71): put(px, y, 36, 'red_concrete' if y % 2 else 'white_concrete'); put(px, y, 37, 'red_concrete' if y % 2 == 0 else 'white_concrete')
for x in range(-6, 7):
    for y in (71, 72):
        for z in (36, 37): put(x, y, z, 'black_concrete' if (x + y + z) % 2 else 'white_concrete')
PIPES = [(-12, 39), (12, 39), (-12, 57), (12, 57)]
for (cx, cz) in PIPES:
    for (x, z) in disc(cx, cz, 1.6):
        for y in range(64, 67): put(x, y, z, 'green_concrete')
    for (x, z) in disc(cx, cz, 2.3): put(x, 67, z, 'lime_concrete')
    for (x, z) in disc(cx, cz, 0.8): put(x, 67, z, 'black_concrete')
for (cx, cz) in ((-9, 60), (9, 60), (-13, 48), (13, 48)):     # piles de pneus
    for y in range(64, 64 + rnd.randint(2, 3)): put(cx, y, cz, 'black_wool' if y % 2 else 'coal_block')

# ------------------------------------------------------------------ jardins
POND = (30, -30, 6.6)
for (x, z) in disc(POND[0], POND[1], POND[2] + 1.2):
    if (x, z) not in ISET: continue
    r = math.hypot(x - POND[0], z - POND[1])
    if r <= POND[2]:
        TOP[(x, z)] = 'water'; MASK[(x, z)] = 'w'
        put(x, 62, z, 'water' if r < 3.5 else ('clay' if rnd.random() < 0.4 else 'sand'))
        if r < 3.5: put(x, 61, z, 'clay')
        if rnd.random() < 0.12 and r > 1.5: put(x, 64, z, 'lily_pad')
    else: paint(x, z, rnd.choice(['mossy_cobblestone', 'stone', 'moss_block', 'grass_block']), 'r')
FOUNT = (-30, 30)
for (x, z) in disc(FOUNT[0], FOUNT[1], 5.5):
    r = math.hypot(x - FOUNT[0], z - FOUNT[1])
    if r > 4.5: paint(x, z, 'polished_andesite')
    elif r > 3.5: paint(x, z, 'stone_bricks'); put(x, 64, z, 'stone_brick_slab')
    else: paint(x, z, 'stone_bricks', 'w'); put(x, 64, z, 'water')
for y in range(64, 67): put(FOUNT[0], y, FOUNT[1], 'chiseled_stone_bricks' if y == 66 else 'stone_brick_wall')
put(FOUNT[0], 66, FOUNT[1], 'chiseled_stone_bricks'); JETS.append((FOUNT[0], 67, FOUNT[1]))
for (x, z) in disc(FOUNT[0], FOUNT[1], 1.5):
    if (x, z) != FOUNT: put(x, 64, z, 'water')

# ponts vers chaque plot
def bridge(n, lx, lz, a, b_, c, d):
    ang = math.atan2(lz, lx); ux, uz = math.cos(ang), math.sin(ang); px_, pz_ = -uz, ux
    t = 58.0
    k = 0
    while t < 100:
        cx, cz = ux * t, uz * t
        if inplot(round(cx), round(cz)): break
        for o in (-1.5, -1, -0.5, 0, 0.5, 1, 1.5):
            x, z = round(cx + px_ * o), round(cz + pz_ * o)
            if inplot(x, z): continue
            if (x, z) in ISET:
                if math.hypot(x, z) >= 63.5: paint(x, z, 'dirt_path')
            else: put(x, G, z, 'spruce_planks'); setif(x, G - 1, z, 'spruce_slab[type=top]')
        for o in (-2.3, 2.3):
            x, z = round(cx + px_ * o), round(cz + pz_ * o)
            if (x, z) in ISET or inplot(x, z): continue
            put(x, G, z, 'spruce_planks'); put(x, G + 1, z, 'spruce_fence')
            if k % 10 == 0: put(x, G + 2, z, 'lantern')
        t += 0.5; k += 1
for p in PLOTS: bridge(*p)
# cascades au bord de l'île (petit ruisseau puis chute dans le vide)
for deg in (33.75, 123.75, 213.75, 303.75):
    a = math.radians(deg); ux, uz = math.cos(a), math.sin(a)
    t = 63.6
    while True:
        x, z = round(ux * t), round(uz * t)
        if (x, z) not in ISET: break
        TOP[(x, z)] = 'water'; MASK[(x, z)] = 'w'; put(x, 62, z, 'stone')
        t += 0.5
    JETS.append((x, G, z))

