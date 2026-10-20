# Terra Nova : colonie (fill / setb / building) et avant-postes ; exécuté par gen_terranova.py (exec), à la place exacte de ce bloc.
# Tranche contiguë de l'ancien gen_terranova.py : mêmes globals que la façade, aucun import, aucune copie de w/js/patch.
# Utilise : EXITA, G, OUTPOSTS, OUT_H, WALL, rnd, w

# ---------------------------------------------------------------- colonie
S = []


def fill(x1, y1, z1, x2, y2, z2, b, mode=''):
    S.append(f'fill {x1} {y1} {z1} {x2} {y2} {z2} minecraft:{b}{" " + mode if mode else ""}')


def setb(x, y, z, b):
    S.append(f'setblock {x} {y} {z} minecraft:{b}')


def building(x1, z1, x2, z2, hgt, wall, floor, roof, pillar, door, windows='glass_pane'):
    """door = (côté 'n'|'s'|'e'|'w', centre, largeur)"""
    top_y = G + hgt
    fill(x1, G, z1, x2, G, z2, floor)
    fill(x1, G + 1, z1, x2, top_y, z2, wall, 'hollow')
    fill(x1 + 1, G + 1, z1 + 1, x2 - 1, top_y, z2 - 1, 'air')
    for (x, z) in [(x1, z1), (x1, z2), (x2, z1), (x2, z2)]:
        fill(x, G + 1, z, x, top_y, z, pillar)
    fill(x1 - 1, top_y + 1, z1 - 1, x2 + 1, top_y + 1, z2 + 1, roof)
    for x in range(x1 + 2, x2 - 1, 3):
        fill(x, G + 2, z1, x, G + 3, z1, windows)
        fill(x, G + 2, z2, x, G + 3, z2, windows)
    for z in range(z1 + 2, z2 - 1, 3):
        fill(x1, G + 2, z, x1, G + 3, z, windows)
        fill(x2, G + 2, z, x2, G + 3, z, windows)
    side, c, wd = door
    a, b = c - wd // 2, c + wd // 2
    if side in 'ew':
        x = x2 if side == 'e' else x1
        fill(x, G + 1, a, x, G + 3, b, 'air')
        fill(x, G + 4, a - 1, x, G + 4, b + 1, pillar)
    else:
        z = z2 if side == 's' else z1
        fill(a, G + 1, z, b, G + 3, z, 'air')
        fill(a - 1, G + 4, z, b + 1, G + 4, z, pillar)
    for x in range(x1 + 3, x2 - 1, 5):
        for z in range(z1 + 3, z2 - 1, 5):
            setb(x, top_y, z, 'lantern[hanging=true]')


# sol : herbe, routes, place
fill(-WALL + 1, G, -WALL + 1, WALL - 1, G, WALL - 1, 'grass_block')
fill(-2, G, -WALL, 2, G, WALL, 'packed_mud')
fill(-WALL + 1, G, -2, WALL - 1, G, 2, 'packed_mud')
for x in range(-8, 9):
    for z in range(-8, 9):
        if x * x + z * z <= 56:
            setb(x, G, z, 'polished_andesite' if (x + z) % 2 else 'andesite')
fill(-1, G, -1, 1, G, 1, 'chiseled_stone_bricks')
for _y in range(G + 1, G + 13):
    fill(-WALL + 1, _y, -WALL + 1, WALL - 1, _y, WALL - 1, 'air')
# palissade
for (a, b, c, d) in [(-WALL, -WALL, WALL, -WALL), (-WALL, WALL, WALL, WALL), (-WALL, -WALL, -WALL, WALL), (WALL, -WALL, WALL, WALL)]:
    fill(a, G - 2, b, c, G + 6, d, 'spruce_log')
    fill(a, G + 7, b, c, G + 7, d, 'spruce_fence')
for zg, lab in [(-WALL, 'n'), (WALL, 's')]:
    fill(-3, G + 1, zg, 3, G + 5, zg, 'air')
    fill(-3, G + 7, zg, 3, G + 7, zg, 'air')
    fill(-4, G + 1, zg, -4, G + 9, zg, 'dark_oak_log')
    fill(4, G + 1, zg, 4, G + 9, zg, 'dark_oak_log')
    fill(-4, G + 6, zg, 4, G + 7, zg, 'stripped_dark_oak_log[axis=x]')
    fill(-3, G + 5, zg, 3, G + 5, zg, 'iron_bars')
    setb(-4, G + 10, zg, 'lantern')
    setb(4, G + 10, zg, 'lantern')
    fill(-3, G, zg - 1, 3, G, zg + 1, 'packed_mud')
# tours de guet (coins)
for cx in (-WALL, WALL):
    for cz in (-WALL, WALL):
        fill(cx - 2, G - 2, cz - 2, cx + 2, G + 11, cz + 2, 'spruce_planks', 'hollow')
        fill(cx - 2, G + 12, cz - 2, cx + 2, G + 12, cz + 2, 'dark_oak_slab')
        for (x, z) in [(cx - 2, cz - 2), (cx - 2, cz + 2), (cx + 2, cz - 2), (cx + 2, cz + 2)]:
            fill(x, G - 2, z, x, G + 13, z, 'stripped_spruce_log')
        fill(cx - 2, G + 9, cz, cx + 2, G + 10, cz, 'light_gray_stained_glass_pane')
        fill(cx, G + 9, cz - 2, cx, G + 10, cz + 2, 'light_gray_stained_glass_pane')
        setb(cx, G + 13, cz, 'lightning_rod')
        setb(cx, G + 14, cz, 'end_rod')
        setb(cx - 1, G + 13, cz - 1, 'lantern')
        setb(cx + 1, G + 13, cz + 1, 'lantern')
# dépôt d'équipement (nord-ouest)
building(-24, -25, -8, -11, 6, 'spruce_planks', 'smooth_stone', 'dark_oak_slab', 'stripped_dark_oak_log', ('e', -18, 3))
fill(-23, G + 1, -24, -9, G + 1, -24, 'barrel[facing=up]')
PADS = [(-23, 'sonic'), (-21, 'mk2'), (-19, 'net'), (-17, 'netx'), (-15, 'trap'), (-13, 'med'), (-11, 'armor'), (-9, 'saddle')]
SHOP_FIX = ['# Socles des présentoirs du dépôt (corrige un monde construit avant le 8e présentoir)',
            f'fill -23 {G + 1} -22 -9 {G + 1} -22 minecraft:air'] + [f'setblock {x} {G + 1} -22 minecraft:polished_andesite' for (x, _) in PADS]
w('terra/shop_fix', SHOP_FIX)
for (x, _) in PADS:
    setb(x, G + 1, -22, 'polished_andesite')
for x in range(-22, -9, 4):
    setb(x, G + 7, -18, 'daylight_detector')
# QG (nord-est) + tableau des missions
building(10, -25, 24, -11, 7, 'light_gray_concrete', 'spruce_planks', 'smooth_stone_slab', 'stripped_spruce_log', ('w', -18, 3))
setb(17, G + 1, -18, 'cartography_table')
setb(18, G + 1, -18, 'lectern[facing=west]')
fill(22, G + 1, -24, 23, G + 2, -24, 'bookshelf')
fill(17, G + 9, -18, 17, G + 12, -18, 'iron_bars')
setb(17, G + 13, -18, 'lightning_rod')
for x in range(12, 24, 3):
    setb(x, G + 9, -13, 'daylight_detector')
    setb(x, G + 9, -23, 'daylight_detector')
fill(9, G + 1, -24, 9, G + 3, -21, 'spruce_planks')
fill(9, G + 4, -25, 9, G + 4, -20, 'spruce_slab')
fill(9, G + 1, -25, 9, G + 4, -25, 'stripped_spruce_log')
fill(9, G + 1, -20, 9, G + 4, -20, 'stripped_spruce_log')
fill(3, G, -24, 8, G, -21, 'packed_mud')
# infirmerie (sud-est)
building(8, 10, 24, 24, 5, 'white_concrete', 'white_terracotta', 'smooth_stone_slab', 'light_gray_concrete', ('w', 17, 3))
fill(8, G + 4, 13, 8, G + 4, 21, 'white_concrete')
fill(7, G + 7, 16, 7, G + 7, 18, 'red_concrete')
fill(7, G + 6, 17, 7, G + 8, 17, 'red_concrete')
for z in (12, 15, 20, 23):
    setb(23, G + 1, z, 'red_bed[facing=west,part=head]')
    setb(22, G + 1, z, 'red_bed[facing=west,part=foot]')
setb(12, G + 1, 11, 'brewing_stand')
setb(13, G + 1, 11, 'cauldron')
# maisons des colons (sud-ouest) + portail du temps
for (x1, z1, dz_door) in [(-25, 20, 2), (-25, 7, 4)]:                          # maison 2 : porte à z=11, hors du four de la forge (z 8..10)
    building(x1, z1, x1 + 8, z1 + 5, 4, 'birch_planks', 'spruce_planks', 'dark_oak_slab', 'stripped_birch_log', ('e', z1 + dz_door, 1))
    setb(x1 + 6, G + 1, z1 + 1, 'barrel[facing=up]')
    setb(x1 + 1, G + 1, z1 + 4, 'crafting_table')
ex, ez = EXITA
fill(ex, G, ez - 3, ex, G, ez + 3, 'polished_blackstone_bricks')
fill(ex, G + 1, ez - 2, ex, G + 6, ez - 2, 'polished_blackstone')
fill(ex, G + 1, ez + 2, ex, G + 6, ez + 2, 'polished_blackstone')
fill(ex, G + 7, ez - 2, ex, G + 7, ez + 2, 'polished_blackstone_brick_slab')
fill(ex, G + 1, ez - 3, ex, G + 5, ez - 3, 'crying_obsidian')
fill(ex, G + 1, ez + 3, ex, G + 5, ez + 3, 'crying_obsidian')
setb(ex, G + 6, ez - 3, 'amethyst_cluster')
setb(ex, G + 6, ez + 3, 'amethyst_cluster')
fill(ex + 1, G, ez - 1, -3, G, ez + 1, 'packed_mud')
# éclairage des routes, réserves
for z in range(-24, 25, 8):
    for x in (-3, 3):
        if abs(z) > 9:
            setb(x, G + 1, z, 'spruce_fence')
            setb(x, G + 2, z, 'spruce_fence')
            setb(x, G + 3, z, 'lantern')
for (x, z) in [(-6, 10), (-7, 10), (-6, 11), (6, -6), (7, -6), (-24, -4), (-23, -4), (-24, -5), (24, 6), (24, 7)]:
    setb(x, G + 1, z, rnd.choice(['barrel[facing=up]', 'hay_block', 'composter', 'spruce_trapdoor[half=top]']))

# ---------------------------------------------------------------- outposts (blocs « légers » : le carnotaure les casse)
LIGHT = ['oak_planks', 'oak_fence', 'oak_slab', 'white_wool', 'glass_pane', 'scaffolding', 'oak_trapdoor', 'lantern']
OUT_B = {}


def ring(x1, y, z1, x2, z2, b):
    """Contour d'une couche (un fill outline d'une seule couche la remplit entièrement)."""
    return [f'fill {x1} {y} {z1} {x2} {y} {z1} minecraft:{b}', f'fill {x1} {y} {z2} {x2} {y} {z2} minecraft:{b}',
            f'fill {x1} {y} {z1} {x1} {y} {z2} minecraft:{b}', f'fill {x2} {y} {z1} {x2} {y} {z2} minecraft:{b}']


for k, (name, ox, oz) in enumerate(OUTPOSTS, 1):
    h = OUT_H[name]
    L = [f'# Outpost {name} : (re)construction',
         f'fill {ox - 6} {h + 1} {oz - 6} {ox + 6} {h + 7} {oz + 6} minecraft:air',
         f'fill {ox - 5} {h} {oz - 5} {ox + 5} {h} {oz + 5} minecraft:oak_planks',
         *ring(ox - 5, h + 1, oz - 5, ox + 5, oz + 5, 'oak_fence'),
         f'fill {ox - 1} {h + 1} {oz - 5} {ox + 1} {h + 1} {oz - 5} minecraft:air', f'fill {ox - 1} {h + 1} {oz + 5} {ox + 1} {h + 1} {oz + 5} minecraft:air',
         f'fill {ox - 5} {h + 1} {oz - 1} {ox - 5} {h + 1} {oz + 1} minecraft:air', f'fill {ox + 5} {h + 1} {oz - 1} {ox + 5} {h + 1} {oz + 1} minecraft:air',
         f'setblock {ox} {h + 1} {oz} minecraft:iron_block', f'setblock {ox} {h + 2} {oz} minecraft:lodestone',
         f'setblock {ox} {h + 3} {oz} minecraft:lightning_rod',
         f'fill {ox - 1} {h + 1} {oz - 1} {ox + 1} {h + 1} {oz + 1} minecraft:oak_slab replace minecraft:air',
         *ring(ox + 2, h + 1, oz + 2, ox + 4, oz + 4, 'oak_fence'),
         f'fill {ox + 2} {h + 2} {oz + 2} {ox + 4} {h + 2} {oz + 4} minecraft:white_wool',
         *ring(ox - 4, h + 1, oz + 2, ox - 2, oz + 4, 'oak_fence'),
         f'fill {ox - 4} {h + 2} {oz + 2} {ox - 2} {h + 2} {oz + 4} minecraft:white_wool',
         f'fill {ox - 4} {h + 1} {oz - 4} {ox - 4} {h + 3} {oz - 4} minecraft:oak_fence',
         f'setblock {ox - 4} {h + 4} {oz - 4} minecraft:lantern',
         f'fill {ox + 3} {h + 1} {oz - 4} {ox + 4} {h + 2} {oz - 3} minecraft:scaffolding',
         f'fill {ox - 1} {h + 2} {oz - 1} {ox + 1} {h + 2} {oz - 1} minecraft:glass_pane',
         f'fill {ox - 1} {h + 2} {oz + 1} {ox + 1} {h + 2} {oz + 1} minecraft:glass_pane']
    OUT_B[k] = L
    w(f'terra/out_build_{k}', L)
    S.append(f'function mg:terra/out_build_{k}')
