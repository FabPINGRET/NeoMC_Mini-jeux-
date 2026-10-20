# Bombardier, Central Park, rues, pont, comptage et tags : exécuté par gen_bomber.py (exec), à sa place dans l'ordre d'origine.
# Utilise : AV, BRIDGE_Z, C, CITY, GSET, HX, LAND, LOTX, LOTZ, PARK, PIDX, ST, fill, grid, in_park, json, math, os, put, px1, px2, pz1,
#   pz2, random.

# ---------------------------------------------------------------- Central Park : arbres, rochers (pas sur l'armurerie)
ARMORY = (-22, 24, -6, 34)                       # armurerie de Neo GTA, à l'entrée sud du parc (x1, z1, x2, z2)
BANK = (-2, 24, 14, 34)                          # banque (à l'est de l'armurerie)
SHOWROOM = (-40, 24, -24, 34)                    # concession (à l'ouest)
AIRFIELD = (-6, 46, 14, 62)                      # aérodrome (pelouse nord-est du parc)


def near_armory(x, z, m=3):
    return any(a - m <= x <= c + m and b - m <= z <= d + m for (a, b, c, d) in (ARMORY, BANK, SHOWROOM, AIRFIELD))


for _ in range(70):
    x, z = random.randint(px1 + 2, px2 - 2), random.randint(pz1 + 2, pz2 - 2)
    if math.hypot((x + 26) / 10, (z - 52) / 7) <= 1 or -15 <= x <= -9 or 39 <= z <= 44 or near_armory(x, z):
        continue
    kind = random.choice(['oak', 'oak', 'birch', 'dark_oak'])
    th = random.randint(4, 6)
    fill(x - 2, 65 + th - 2, z - 2, x + 2, 65 + th - 1, z + 2, f'{kind}_leaves[persistent=true]')
    fill(x - 1, 65 + th, z - 1, x + 1, 65 + th + 1, z + 1, f'{kind}_leaves[persistent=true]')
    fill(x, 65, z, x, 65 + th - 1, z, f'{kind}_log')
for _ in range(8):
    x, z = random.randint(px1 + 3, px2 - 3), random.randint(pz1 + 3, pz2 - 3)
    if not (-15 <= x <= -9 or 39 <= z <= 44) and math.hypot((x + 26) / 10, (z - 52) / 7) > 1 and not near_armory(x, z):
        fill(x, 65, z, x + 1, 65, z + 1, 'mossy_cobblestone'); put(x, 66, z, 'mossy_cobblestone')
fill(-27, 65, 42, -25, 65, 44, 'chiseled_stone_bricks'); put(-26, 66, 43, 'sea_lantern')

# armurerie (porte au sud, côté rue) : briques sombres, vitrine, bandeau rouge, râteliers au fond
ax1, az1, ax2, az2 = ARMORY
fill(ax1, 65, az1, ax2, 65, az2, 'polished_andesite')
fill(ax1, 66, az1, ax2, 72, az1, 'deepslate_bricks'); fill(ax1, 66, az2, ax2, 72, az2, 'deepslate_bricks')
fill(ax1, 66, az1, ax1, 72, az2, 'deepslate_bricks'); fill(ax2, 66, az1, ax2, 72, az2, 'deepslate_bricks')
fill(ax1 + 1, 66, az1 + 1, ax2 - 1, 71, az2 - 1, 'air')
fill(ax1, 72, az1, ax2, 72, az2, 'polished_deepslate')
fill(ax1 + 1, 67, az1, ax2 - 1, 69, az1, 'gray_stained_glass')                 # vitrine
fill(ax1, 70, az1, ax2, 71, az1, 'red_concrete')                               # bandeau de l'enseigne
fill(-15, 66, az1, -13, 68, az1, 'air')                                        # porte
fill(-16, 66, az1, -16, 69, az1, 'iron_block'); fill(-12, 66, az1, -12, 69, az1, 'iron_block'); fill(-16, 69, az1, -12, 69, az1, 'iron_block')
fill(-15, 65, 21, -13, 65, az1 - 1, 'stone_bricks')                            # allée depuis la rue
for x in range(ax1 + 2, ax2 - 1, 4):
    put(x, 71, (az1 + az2) // 2, 'sea_lantern'); put(x, 71, az2 - 2, 'sea_lantern')
for x in range(ax1 + 1, ax2, 2):                                               # râteliers derrière les présentoirs
    fill(x, 67, az2 - 1, x, 69, az2 - 1, 'iron_bars')
fill(ax1 + 1, 66, az1 + 3, ax1 + 5, 66, az1 + 3, 'dark_oak_planks'); fill(ax1 + 1, 67, az1 + 3, ax1 + 5, 67, az1 + 3, 'smooth_quartz_slab')   # comptoir
fill(ax2 - 5, 66, az1 + 3, ax2 - 1, 66, az1 + 3, 'dark_oak_planks'); fill(ax2 - 5, 67, az1 + 3, ax2 - 1, 67, az1 + 3, 'smooth_quartz_slab')
fill(ax1 + 1, 66, az2 - 1, ax2 - 1, 66, az2 - 1, 'red_carpet')


def hall_box(x1, z1, x2, z2, wall, floor, roof, door_x):
    fill(x1, 65, z1, x2, 65, z2, floor)
    fill(x1, 66, z1, x2, 72, z1, wall); fill(x1, 66, z2, x2, 72, z2, wall)
    fill(x1, 66, z1, x1, 72, z2, wall); fill(x2, 66, z1, x2, 72, z2, wall)
    fill(x1 + 1, 66, z1 + 1, x2 - 1, 71, z2 - 1, 'air')
    fill(x1, 72, z1, x2, 72, z2, roof)
    fill(door_x - 1, 66, z1, door_x + 1, 68, z1, 'air')
    fill(door_x - 1, 65, 21, door_x + 1, 65, z1 - 1, 'stone_bricks')
    for x in range(x1 + 2, x2 - 1, 4):
        put(x, 71, (z1 + z2) // 2, 'sea_lantern')


# banque : colonnade blanche, bandeau doré, salle des coffres au fond (blocs d'or = bonus au Bombardier)
bx1, bz1_, bx2, bz2_ = BANK
hall_box(bx1, bz1_, bx2, bz2_, 'calcite', 'polished_diorite', 'smooth_quartz', 6)
for x in range(bx1, bx2 + 1, 3):
    if abs(x - 6) > 2:
        fill(x, 66, bz1_ - 1, x, 71, bz1_ - 1, 'quartz_pillar')
fill(bx1, 72, bz1_ - 1, bx2, 72, bz1_ - 1, 'smooth_quartz')
fill(bx1, 70, bz1_, bx2, 71, bz1_, 'gold_block')
fill(bx1 + 1, 66, bz1_ + 3, bx1 + 5, 67, bz1_ + 3, 'dark_oak_planks'); fill(bx2 - 5, 66, bz1_ + 3, bx2 - 1, 67, bz1_ + 3, 'dark_oak_planks')
fill(bx1 + 3, 66, bz2_ - 4, bx2 - 3, 70, bz2_ - 4, 'iron_block')                # mur de la salle des coffres
fill(5, 66, bz2_ - 4, 7, 68, bz2_ - 4, 'air')                                   # porte blindée ouverte
fill(bx1 + 4, 66, bz2_ - 1, bx1 + 5, 67, bz2_ - 1, 'gold_block'); fill(bx2 - 5, 66, bz2_ - 1, bx2 - 4, 67, bz2_ - 1, 'gold_block')
# concession : grande vitrine, sol clair
sx1, sz1, sx2, sz2 = SHOWROOM
hall_box(sx1, sz1, sx2, sz2, 'white_concrete', 'smooth_quartz', 'light_gray_concrete', -32)
fill(sx1 + 1, 66, sz1, sx2 - 1, 70, sz1, 'light_blue_stained_glass')
fill(-33, 66, sz1, -31, 68, sz1, 'air')
fill(sx1, 71, sz1, sx2, 71, sz1, 'purple_concrete')
# aérodrome : piste et hélisurface (tapis sur la pelouse)
fx1, fz1, fx2, fz2 = AIRFIELD
fill(fx1, 65, fz1 + 6, fx2, 65, fz1 + 10, 'gray_carpet')
for x in range(fx1 + 1, fx2, 3):
    put(x, 65, fz1 + 8, 'white_carpet')
fill(2, 65, fz1, 6, 65, fz1 + 4, 'yellow_carpet'); fill(3, 65, fz1 + 1, 3, 65, fz1 + 3, 'black_carpet'); fill(5, 65, fz1 + 1, 5, 65, fz1 + 3, 'black_carpet')
put(4, 65, fz1 + 2, 'black_carpet')

# ---------------------------------------------------------------- rues : taxis, voitures, réverbères
# chaussées dégagées (plus de voitures en blocs : à Neo GTA les voitures sont de vraies voitures pilotables)
for c in AV:
    for (za, zb) in ([(-HX, PARK[1] - 1), (PARK[3] + 1, HX)] if PARK[0] <= c <= PARK[2] else [(-HX, HX)]):
        fill(c - 3, 65, za, c + 3, 66, zb, 'air')
for c in ST:
    for (xa, xb) in ([(-HX, PARK[0] - 1), (PARK[2] + 1, LAND)] if PARK[1] <= c <= PARK[3] else [(-HX, LAND)]):
        fill(xa, 65, c - 2, xb, 66, c + 2, 'air')
for (lx1, lx2) in LOTX:
    for (lz1, lz2) in LOTZ:
        if in_park(lx1, lz1) or lx2 - lx1 < 6 or lz2 - lz1 < 6:
            continue
        for (x, z) in [(lx1, lz1), (lx2, lz1), (lx1, lz2), (lx2, lz2)]:
            fill(x, 65, z, x, 67, z, 'iron_bars'); put(x, 68, z, 'lantern')

# ---------------------------------------------------------------- pont suspendu (rue BRIDGE_Z) et statue
bz = BRIDGE_Z
fill(LAND - 3, 65, bz - 2, LAND, 68, bz + 2, 'stone_bricks')
fill(LAND - 6, 65, bz - 2, LAND - 4, 65, bz + 2, 'stone_brick_slab')
fill(LAND - 3, 69, bz - 2, HX, 69, bz + 2, 'dark_oak_planks')
fill(LAND - 3, 70, bz - 2, HX, 70, bz - 2, 'dark_oak_fence'); fill(LAND - 3, 70, bz + 2, HX, 70, bz + 2, 'dark_oak_fence')
for tx in (71, 83):
    for zz in (bz - 3, bz + 3):
        fill(tx - 1, 58, zz - 1 if zz < bz else zz, tx + 1, 92, zz if zz < bz else zz + 1, 'stone_bricks')
    fill(tx - 1, 88, bz - 2, tx + 1, 92, bz + 2, 'stone_bricks')
    fill(tx - 1, 88, bz - 1, tx + 1, 90, bz + 1, 'air')
    fill(tx - 1, 58, bz - 2, tx + 1, 68, bz + 2, 'stone_bricks')
for zz in (bz - 3, bz + 3):
    for x in range(LAND - 3, HX + 1):
        if x in (70, 71, 72, 82, 83, 84):
            continue
        y = round(71 + 21 * ((x - 77) / 6) ** 2) if 71 <= x <= 83 else round(92 - 2.2 * (71 - x if x < 71 else x - 83))
        y = max(71, min(y, 92))
        put(x, y, zz, 'iron_chain')
        if x % 2 == 0 and y > 71:
            fill(x, 71, zz, x, y - 1, zz, 'iron_chain')
# statue (bonus : cuivre oxydé et flamme dorée)
sx, sz = 78, -72
fill(sx - 3, 65, sz - 3, sx + 3, 70, sz + 3, 'stone_bricks')
fill(sx - 2, 71, sz - 2, sx + 2, 72, sz + 2, 'chiseled_stone_bricks')
fill(sx - 1, 73, sz - 1, sx + 1, 82, sz + 1, 'oxidized_copper')
fill(sx - 2, 73, sz - 1, sx + 2, 76, sz + 1, 'oxidized_cut_copper')
fill(sx, 83, sz, sx, 85, sz, 'oxidized_copper')
fill(sx - 1, 84, sz, sx + 1, 84, sz, 'oxidized_copper')
for (dx, dz) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    put(sx + dx, 86, sz + dz, 'oxidized_cut_copper')
fill(sx + 2, 80, sz, sx + 2, 88, sz, 'oxidized_copper')
fill(sx + 2, 89, sz, sx + 2, 90, sz, 'gold_block')
fill(sx - 2, 79, sz, sx - 2, 81, sz, 'oxidized_cut_copper')

# ---------------------------------------------------------------- comptage, tags
BONUS = {'gold_block', 'oxidized_copper', 'oxidized_cut_copper'}
CITY -= {'air'}
GSET.discard('barrier')
assert not (CITY & (GSET | {'barrier', 'water'})), CITY & GSET
cnt = {n: grid.count(bytes([PIDX[n]])) for n in CITY}
TOTAL = sum(cnt.values())
TB = sum(cnt[n] for n in BONUS if n in cnt)
os.makedirs(os.path.join(C.D, 'tags/block'), exist_ok=True)
for name, vals in [('bomb_city', sorted(CITY - BONUS)), ('bomb_bonus', sorted(BONUS)),
                   ('bomb_pass', ['air', 'cave_air', 'void_air', 'light'])]:
    with open(os.path.join(C.D, 'tags/block', name + '.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'values': ['minecraft:' + v for v in vals]}, f, indent=2)
        f.write('\n')
