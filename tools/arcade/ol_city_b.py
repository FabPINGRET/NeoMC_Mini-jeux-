"""🏰 Ombrelune : bâtiments de la cité de Havreclair (château, temple, tour du mage, guilde, taverne, forge, marché, écuries, alchimiste).
Module importé par ol_city et réexporté par ol_structs.
"""
import math
import random

from tv_build import AIR
from ol_skit import HOUSE_STYLES, cone_roof, crenels, house, round_tower, spiral_well, spot, stone_mix


def castle(v, Y):
    r = random.Random(5)
    sm = stone_mix(r, 'stone_bricks', 'mossy_stone_bricks', 'cracked_stone_bricks', 0.06, 0.05)
    x1, z1, x2, z2 = -20, -50, 20, -26
    # cour et enceinte intérieure
    v.fill(x1, Y, z1, x2, Y, z2, 'polished_andesite')
    v.walls(x1, z1, x2, z2, Y + 1, Y + 6, sm)
    crenels(v, x1, z1, x2, z1, Y + 7, 'stone_bricks')
    crenels(v, x1, z2, x2, z2, Y + 7, 'stone_bricks')
    crenels(v, x1, z1, x1, z2, Y + 7, 'stone_bricks')
    crenels(v, x2, z1, x2, z2, Y + 7, 'stone_bricks')
    v.fill(-2, Y + 1, z2, 2, Y + 5, z2, AIR)
    v.fill(-2, Y + 6, z2, 2, Y + 6, z2, 'chiseled_stone_bricks')
    for x in (-3, 3):
        v.set(x, Y + 4, z2 + 1, 'blue_wall_banner[facing=south]')
    # donjon
    kx1, kz1, kx2, kz2 = -13, -47, 13, -31
    v.fill(kx1, Y, kz1, kx2, Y, kz2, 'polished_deepslate')
    for f, (ya, yb) in enumerate(((Y + 1, Y + 8), (Y + 9, Y + 15), (Y + 16, Y + 21))):
        v.walls(kx1, kz1, kx2, kz2, ya, yb, sm)
        v.fill(kx1 + 1, ya + (1 if f else 0), kz1 + 1, kx2 - 1, yb, kz2 - 1, AIR)   # sans effacer le plancher de l'étage du dessous
        v.fill(kx1 + 1, yb + 1, kz1 + 1, kx2 - 1, yb + 1, kz2 - 1, 'dark_oak_planks')
        for x in range(kx1 + 3, kx2 - 1, 4):
            v.fill(x, ya + 2, kz1, x, ya + 4, kz1, 'blue_stained_glass_pane' if f else 'glass_pane')
            if f or abs(x) > 3:   # pas de vitre au-dessus de la porte
                v.fill(x, ya + 2, kz2, x, ya + 4, kz2, 'blue_stained_glass_pane' if f else 'glass_pane')
    v.fill(kx1, Y + 22, kz1, kx2, Y + 22, kz2, 'stone_bricks')
    crenels(v, kx1, kz1, kx2, kz1, Y + 23, 'stone_bricks')
    crenels(v, kx1, kz2, kx2, kz2, Y + 23, 'stone_bricks')
    crenels(v, kx1, kz1, kx1, kz2, Y + 23, 'stone_bricks')
    crenels(v, kx2, kz1, kx2, kz2, Y + 23, 'stone_bricks')
    # salle du trône (rez-de-chaussée)
    v.fill(-1, Y, kz1 + 2, 1, Y, kz2, 'red_carpet' if False else 'red_wool')
    v.fill(-1, Y + 1, kz1 + 2, 1, Y + 1, kz2 - 1, 'red_carpet')
    v.fill(-2, Y + 1, kz1 + 1, 2, Y + 1, kz1 + 2, 'polished_deepslate')
    v.set(0, Y + 2, kz1 + 1, 'dark_oak_stairs[facing=south]')
    v.set(-1, Y + 2, kz1 + 1, 'gold_block')
    v.set(1, Y + 2, kz1 + 1, 'gold_block')
    v.fill(-1, Y + 3, kz1 + 1, 1, Y + 4, kz1 + 1, 'blue_wool')
    for x in (-8, -4, 4, 8):
        v.fill(x, Y + 1, kz1 + 3, x, Y + 8, kz1 + 3, 'quartz_pillar')
        v.fill(x, Y + 1, kz2 - 3, x, Y + 8, kz2 - 3, 'quartz_pillar')
        v.set(x, Y + 6, kz1 + 4, 'blue_wall_banner[facing=south]')
    for x in range(-10, 11, 5):
        v.lamp(x, Y + 7, (kz1 + kz2) // 2, kind='lantern')
    v.fill(-2, Y + 1, kz2, 2, Y + 4, kz2, AIR)
    v.door(-1, Y + 1, kz2, 'south', 'dark_oak', width=1)
    v.door(1, Y + 1, kz2, 'south', 'dark_oak', width=1)
    v.set(0, Y + 1, kz2, AIR)
    spot('throne', 0, Y + 1, kz1 + 4)
    spot('regent', 2, Y + 1, kz1 + 3)
    # tours du donjon
    for (cx, cz) in ((kx1, kz1), (kx2, kz1), (kx1, kz2), (kx2, kz2)):
        round_tower(v, cx, cz, Y + 1, 3, 26, sm, floor='spruce_planks', crenel='stone_bricks', roof='blue_terracotta', roof_h=8)
    # escalier intérieur
    v.stair_run(kx2 - 2, Y + 1, kz2 - 4, 0, -1, 9, 'dark_oak_stairs', 'north', support='stone_bricks')   # pied hors de l'anneau de la tour SE
    v.fill(kx2 - 2, Y + 9, kz1 + 5, kx2 - 2, Y + 9, kz2 - 4, AIR)
    # étage 2 -> 3 : volée du côté ouest, en sens inverse
    v.stair_run(kx1 + 2, Y + 10, kz1 + 5, 0, 1, 7, 'dark_oak_stairs', 'south', support='stone_bricks')
    v.fill(kx1 + 2, Y + 16, kz1 + 5, kx1 + 2, Y + 16, kz2 - 6, AIR)
    # bannières et drapeaux
    v.fill(0, Y + 23, (kz1 + kz2) // 2, 0, Y + 30, (kz1 + kz2) // 2, 'spruce_fence')
    v.fill(1, Y + 28, (kz1 + kz2) // 2, 3, Y + 30, (kz1 + kz2) // 2, 'blue_wool')
    # caserne (contre l'enceinte ouest de la cour)
    v.fill(x1 + 1, Y + 1, z2 - 6, x1 + 7, Y + 4, z2 - 1, 'spruce_planks', hollow=True)
    v.fill(x1 + 1, Y + 5, z2 - 6, x1 + 7, Y + 5, z2 - 1, 'spruce_slab')
    v.set(x1 + 7, Y + 1, z2 - 3, AIR)
    v.set(x1 + 7, Y + 2, z2 - 3, AIR)
    for z in range(z2 - 5, z2 - 1, 2):
        v.bed(x1 + 2, Y + 1, z, 'west', 'blue')
    for z in range(z2 - 5, z2 - 1):
        v.set(x1 + 9, Y + 1, z, 'armor_stand' if False else 'spruce_fence')
    spot('aldric', 6, Y + 1, z2 - 4)
    # jardin de la cour
    for x in range(14, 23):
        for z in range(z2 - 5, z2):
            v.set(x, Y, z, 'grass_block')
            if (x + z) % 3 == 0:
                v.set(x, Y + 1, z, r.choice(['rose_bush', 'peony', 'lilac']) + '[half=lower]')
                v.set(x, Y + 2, z, v.get(x, Y + 1, z).replace('lower', 'upper'))


def temple(v, Y):
    """Temple de l'Aube (nord-est) : nef, vitraux, clocher, autel de la Pierre-Lune."""
    r = random.Random(6)
    x1, z1, x2, z2 = 24, -44, 43, -20
    mat = lambda x, y, z: 'calcite' if r.random() < 0.7 else 'smooth_quartz'
    v.fill(x1, Y, z1, x2, Y, z2, 'polished_diorite')
    # nef (le long de z)
    nx1, nx2 = 28, 39
    v.walls(nx1, z1, nx2, z2, Y + 1, Y + 12, mat)
    v.fill(nx1 + 1, Y + 1, z1 + 1, nx2 - 1, Y + 12, z2 - 1, AIR)
    for z in range(z1 + 2, z2 - 1, 4):
        v.fill(nx1, Y + 3, z, nx1, Y + 9, z, 'yellow_stained_glass_pane')
        v.fill(nx2, Y + 3, z, nx2, Y + 9, z, 'orange_stained_glass_pane')
        v.fill(nx1, Y + 1, z + 2, nx1, Y + 12, z + 2, 'quartz_pillar')
        v.fill(nx2, Y + 1, z + 2, nx2, Y + 12, z + 2, 'quartz_pillar')
    # rosace (pignon sud)
    for y in range(Y + 4, Y + 12):
        for x in range(nx1 + 1, nx2):
            d = math.hypot(x - 33, y - (Y + 8))
            if d < 3.6:
                v.set(x, y, z2, 'magenta_stained_glass_pane' if d < 1.5 else ('yellow_stained_glass_pane' if d < 2.6 else 'light_blue_stained_glass_pane'))
    v.gable_roof(nx1, z1, nx2, z2, Y + 13, 'z', 'deepslate_tile_stairs', 'deepslate_tile_slab', 'deepslate_tiles')
    # transept
    v.walls(x1, -34, x2, -28, Y + 1, Y + 10, mat)
    v.fill(x1 + 1, Y + 1, -33, x2 - 1, Y + 10, -29, AIR)
    v.fill(nx1 + 1, Y + 1, -33, nx2 - 1, Y + 10, -29, AIR)
    v.gable_roof(x1, -34, x2, -28, Y + 11, 'x', 'deepslate_tile_stairs', 'deepslate_tile_slab', 'deepslate_tiles')
    # entrée (sud)
    v.fill(31, Y + 1, z2, 35, Y + 4, z2, AIR)
    v.fill(31, Y + 5, z2, 35, Y + 5, z2, 'chiseled_quartz_block')
    # bancs, tapis, autel
    v.fill(32, Y + 1, z1 + 4, 34, Y + 1, z2 - 1, 'yellow_carpet')
    for z in range(z1 + 9, z2 - 2, 2):
        for x in (30, 31, 36, 37):
            v.set(x, Y + 1, z, 'spruce_stairs[facing=north]')
    v.fill(31, Y + 1, z1 + 2, 35, Y + 1, z1 + 3, 'polished_diorite')
    v.fill(32, Y + 2, z1 + 2, 34, Y + 2, z1 + 2, 'chiseled_quartz_block')
    v.set(33, Y + 3, z1 + 2, 'amethyst_cluster[facing=up]')
    v.set(33, Y + 2, z1 + 3, 'enchanting_table')
    spot('altar', 33, Y + 1, z1 + 5)
    spot('liora_t', 35, Y + 1, z1 + 5)
    for x in (30, 37):
        v.set(x, Y + 1, z1 + 2, 'candle[candles=4,lit=true]')
    for z in range(z1 + 4, z2 - 1, 6):
        v.lamp(33, Y + 11, z, kind='soul_lantern' if False else 'lantern')
    # clocher (coin sud-ouest)
    v.fill(nx1 - 4, Y + 1, z2 - 4, nx1, Y + 22, z2, mat)
    v.fill(nx1 - 3, Y + 1, z2 - 3, nx1 - 1, Y + 22, z2 - 1, AIR)
    for (x, z) in ((nx1 - 2, z2 - 4), (nx1 - 2, z2), (nx1 - 4, z2 - 2), (nx1, z2 - 2)):
        v.fill(x, Y + 17, z, x, Y + 20, z, AIR)
    v.set(nx1 - 2, Y + 20, z2 - 2, 'bell[attachment=ceiling,facing=north]')
    v.fill(nx1 - 2, Y + 21, z2 - 2, nx1 - 2, Y + 21, z2 - 2, 'iron_chain')
    cone_roof(v, nx1 - 2, z2 - 2, Y + 23, 3, 'deepslate_tiles', 8, 'lightning_rod')


def mage_tower(v, Y):
    r = random.Random(8)
    cx, cz = -34, -34
    wall = lambda x, y, z: 'purpur_block' if (y % 7 == 0) else ('deepslate_bricks' if r.random() < 0.8 else 'cracked_deepslate_bricks')
    round_tower(v, cx, cz, Y + 1, 6, 34, wall, floor='dark_oak_planks', floors=(Y + 9, Y + 17, Y + 25), roof='purple_terracotta', roof_h=14)
    spiral_well(v, cx, cz, 4, Y + 1, Y + 25, 'polished_deepslate_slab[type=top]', per_turn=16)
    for fy in (Y + 9, Y + 17, Y + 25):
        for k in range(16):
            a = 2 * math.pi * k / 16
            x, z = round(cx + 5 * math.cos(a)), round(cz + 5 * math.sin(a))
            if k % 4 == 0:
                v.set(x, fy + 1, z, 'bookshelf')
                v.set(x, fy + 2, z, 'bookshelf')
        v.lamp(cx, fy + 6, cz, kind='soul_lantern')
    v.set(cx, Y + 1, cz, 'enchanting_table')
    v.set(cx + 1, Y + 1, cz, 'brewing_stand')
    v.set(cx - 1, Y + 1, cz, 'lectern[facing=east]')
    v.fill(cx + 6, Y + 1, cz, cx + 6, Y + 2, cz, AIR)
    v.door(cx + 6, Y + 1, cz, 'east', 'dark_oak')
    spot('liora', cx + 2, Y + 1, cz + 2)
    for a in range(0, 360, 60):
        x, z = round(cx + 8 * math.cos(math.radians(a))), round(cz + 8 * math.sin(math.radians(a)))
        v.set(x, Y + 1, z, 'amethyst_block')
        v.set(x, Y + 2, z, 'amethyst_cluster[facing=up]')


def guild(v, Y):
    """Guilde des aventuriers (ouest) : tableau des contrats, maître d'armes."""
    x1, z1, x2, z2 = -44, -16, -22, -4
    st = HOUSE_STYLES[1]
    v.fill(x1, Y, z1, x2, Y, z2, 'stone_bricks')
    v.fill(x1 + 1, Y, z1 + 1, x2 - 1, Y, z2 - 1, 'spruce_planks')
    v.frame_walls(x1, z1, x2, z2, Y + 1, Y + 6, 'smooth_sandstone', 'dark_oak_log', 'stripped_dark_oak_log', step=3)
    v.fill(x1 + 1, Y + 1, z1 + 1, x2 - 1, Y + 6, z2 - 1, AIR)
    v.windows(x1, z1, x2, z2, Y + 2, 2, 'glass_pane', every=3)
    v.gable_roof(x1, z1, x2, z2, Y + 7, 'x', 'dark_oak_stairs', 'dark_oak_slab', 'dark_oak_planks')
    v.fill(x2, Y + 1, -11, x2, Y + 3, -9, AIR)
    v.set(x2 + 1, Y + 4, -12, 'red_wall_banner[facing=east]')
    v.set(x2 + 1, Y + 4, -8, 'red_wall_banner[facing=east]')
    # tableau des contrats (mur nord, intérieur)
    v.fill(-36, Y + 2, z1 + 1, -30, Y + 4, z1 + 1, 'spruce_planks')
    v.fill(-37, Y + 1, z1 + 1, -37, Y + 5, z1 + 1, 'stripped_spruce_log')
    v.fill(-29, Y + 1, z1 + 1, -29, Y + 5, z1 + 1, 'stripped_spruce_log')
    spot('board', -33, Y + 1, z1 + 2)
    # mannequins d'entraînement, râtelier
    for x in (-42, -40):
        v.set(x, Y + 1, z2 - 2, 'hay_block')
        v.set(x, Y + 2, z2 - 2, 'carved_pumpkin[facing=east]')
    v.fill(-26, Y + 1, z1 + 1, -24, Y + 1, z1 + 1, 'barrel[facing=up]')
    v.set(-25, Y + 2, z1 + 1, 'grindstone[face=floor,facing=north]')
    for x in range(-42, -24, 6):
        v.lamp(x, Y + 5, -10)
    spot('orren', -27, Y + 1, -10)


def tavern(v, Y):
    """Taverne du Sanglier Doré (sud-ouest), deux étages, comptoir, tables, cheminée."""
    x1, z1, x2, z2 = -44, 8, -24, 24
    r = random.Random(9)
    v.fill(x1, Y, z1, x2, Y, z2, 'cobblestone')
    v.fill(x1 + 1, Y, z1 + 1, x2 - 1, Y, z2 - 1, 'spruce_planks')
    v.frame_walls(x1, z1, x2, z2, Y + 1, Y + 4, 'cobblestone', 'spruce_log', 'stripped_spruce_log', step=4)
    v.frame_walls(x1, z1, x2, z2, Y + 5, Y + 8, 'white_terracotta', 'spruce_log', 'stripped_spruce_log', step=4)
    v.fill(x1 + 1, Y + 1, z1 + 1, x2 - 1, Y + 8, z2 - 1, AIR)
    v.fill(x1 + 1, Y + 5, z1 + 1, x2 - 1, Y + 5, z2 - 1, 'spruce_planks')
    v.fill(x1 + 2, Y + 5, z1 + 5, x1 + 4, Y + 5, z1 + 7, AIR)   # trou d'étage au-dessus de la volée
    v.stair_run(x1 + 2, Y + 1, z1 + 8, 0, -1, 5, 'spruce_stairs', 'north', support='spruce_planks')
    v.windows(x1, z1, x2, z2, Y + 2, 2, 'glass_pane', every=4)
    v.windows(x1, z1, x2, z2, Y + 6, 2, 'glass_pane', every=4)
    v.gable_roof(x1, z1, x2, z2, Y + 9, 'x', 'spruce_stairs', 'spruce_slab', 'spruce_planks')
    v.fill(x2, Y + 1, 15, x2, Y + 2, 16, AIR)
    v.door(x2, Y + 1, 15, 'east', 'spruce', width=2)
    v.set(x2 + 1, Y + 4, 13, 'yellow_wall_banner[facing=east]')
    # comptoir
    v.fill(x1 + 8, Y + 1, z2 - 4, x1 + 16, Y + 1, z2 - 4, 'spruce_planks')
    v.fill(x1 + 8, Y + 2, z2 - 4, x1 + 16, Y + 2, z2 - 4, 'spruce_slab')
    v.fill(x1 + 8, Y + 1, z2 - 1, x1 + 16, Y + 2, z2 - 1, 'barrel[facing=north]')
    spot('innkeeper', x1 + 12, Y + 1, z2 - 2)
    # tables
    for (tx, tz) in ((x1 + 5, z1 + 4), (x1 + 11, z1 + 4), (x1 + 16, z1 + 4), (x1 + 5, z1 + 9), (x1 + 11, z1 + 9), (x1 + 16, z1 + 9)):
        v.table(tx, Y + 1, tz, 'spruce_pressure_plate', 'spruce_fence')
        v.set(tx + 1, Y + 1, tz, 'spruce_stairs[facing=west]')
        v.set(tx - 1, Y + 1, tz, 'spruce_stairs[facing=east]')
        v.set(tx, Y + 3, tz, 'candle[candles=3,lit=true]') if False else None
    # cheminée
    v.fill(x1 + 1, Y + 1, z1 + 12, x1 + 1, Y + 14, z1 + 14, 'bricks')
    v.set(x1 + 2, Y + 1, z1 + 13, 'campfire[lit=true,facing=east]')
    v.set(x1 + 2, Y + 2, z1 + 12, 'brick_stairs[facing=south,half=top]')
    for x in range(x1 + 4, x2 - 2, 5):
        v.lamp(x, Y + 3, z1 + 7)
    # chambres (étage)
    for k, x in enumerate(range(x1 + 6, x2 - 2, 5)):
        v.bed(x, Y + 6, z2 - 2, 'south', ['red', 'yellow', 'green'][k % 3])


def forge_b(v, Y):
    """Forge (sud-est) : atelier ouvert, cheminée, enclumes, lave."""
    x1, z1, x2, z2 = 22, 8, 40, 22
    v.fill(x1, Y, z1, x2, Y, z2, 'polished_andesite')
    v.fill(x1, Y + 1, z1, x2, Y + 5, z1, 'stone_bricks')
    v.fill(x1, Y + 1, z1, x1, Y + 5, z2, 'stone_bricks')
    for (x, z) in ((x2, z1), (x2, z2), (x1, z2), (31, z2), (x2, 15)):
        v.fill(x, Y + 1, z, x, Y + 5, z, 'stripped_dark_oak_log')
    v.fill(x1, Y + 6, z1, x2, Y + 6, z2, 'dark_oak_slab')
    v.fill(x1 + 1, Y + 1, z1 + 1, x1 + 4, Y + 1, z1 + 4, 'bricks')
    v.fill(x1 + 1, Y + 2, z1 + 1, x1 + 4, Y + 12, z1 + 4, 'bricks', hollow=True)
    v.fill(x1 + 2, Y + 1, z1 + 2, x1 + 3, Y + 1, z1 + 3, 'lava')
    v.fill(x1 + 2, Y + 2, z1 + 4, x1 + 3, Y + 3, z1 + 4, 'iron_bars')
    v.set(x1 + 6, Y + 1, z1 + 2, 'anvil[facing=east]')
    v.set(x1 + 9, Y + 1, z1 + 2, 'chipped_anvil[facing=east]')
    v.set(x1 + 12, Y + 1, z1 + 1, 'blast_furnace[facing=south]')
    v.set(x1 + 13, Y + 1, z1 + 1, 'blast_furnace[facing=south]')
    v.set(x1 + 15, Y + 1, z1 + 1, 'smithing_table')
    v.set(x1 + 16, Y + 1, z1 + 1, 'grindstone[face=floor,facing=south]')
    v.set(x1 + 2, Y + 1, z2 - 2, 'water_cauldron[level=3]')
    v.fill(x1 + 6, Y + 1, z2 - 1, x1 + 12, Y + 1, z2 - 1, 'barrel[facing=up]')
    spot('blacksmith', x1 + 8, Y + 1, z1 + 4)
    for x in (x1 + 6, x1 + 12):
        v.lamp(x, Y + 5, z1 + 8)


def market(v, Y):
    """Marché (est de la place) : étals à auvents colorés."""
    cols = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'cyan', 'lime']
    k = 0
    for x0 in range(17, 44, 7):
        for z0, face in ((-13, 'south'), (-8, 'north')):
            c = cols[k % len(cols)]
            k += 1
            v.fill(x0, Y + 1, z0, x0 + 4, Y + 1, z0, 'spruce_planks' if face == 'south' else 'oak_planks')
            for (x, z) in ((x0, z0), (x0 + 4, z0)):
                v.fill(x, Y + 1, z, x, Y + 3, z, 'spruce_fence')
            v.fill(x0, Y + 4, z0 - (1 if face == 'south' else 0), x0 + 4, Y + 4, z0 + (0 if face == 'south' else 1), f'{c}_wool')
            v.set(x0 + 2, Y + 2, z0, ['melon', 'pumpkin', 'hay_block', 'barrel[facing=up]', 'composter', 'bee_nest[facing=south]'][k % 6])
    spot('merchant', 24, Y + 1, -10)
    spot('armorer', 31, Y + 1, -10)
    spot('trader', 38, Y + 1, -10)


def stables(v, Y):
    x1, z1, x2, z2 = 24, 30, 42, 44
    v.fill(x1, Y, z1, x2, Y, z2, 'coarse_dirt')
    v.fill(x1, Y + 1, z1, x2, Y + 1, z2, 'oak_fence', outline=True)
    v.fill(x1 + 8, Y + 1, z1, x1 + 10, Y + 1, z1, AIR)
    v.fill(x1, Y + 1, z2 - 5, x2, Y + 4, z2, 'oak_planks', hollow=True)
    v.fill(x1 + 1, Y + 1, z2 - 4, x2 - 1, Y + 4, z2 - 1, AIR)
    v.fill(x1, Y + 5, z2 - 6, x2, Y + 5, z2, 'oak_slab')
    for x in range(x1 + 2, x2 - 1, 4):
        v.fill(x, Y + 1, z2 - 5, x + 1, Y + 3, z2 - 5, AIR)
        v.set(x, Y + 1, z2 - 2, 'hay_block')
        v.set(x + 1, Y + 1, z2 - 1, 'water_cauldron[level=3]')
    for x in range(x1 + 3, x2 - 2, 6):
        v.set(x, Y + 1, z1 + 4, 'hay_block')
    spot('stablemaster', x1 + 9, Y + 1, z1 + 2)
    spot('stable_pen', (x1 + x2) // 2, Y + 1, z1 + 6)


def alchemist(v, Y):
    x1, z1, x2, z2 = -44, 30, -30, 42
    house(v, x1, z1, x2 - x1 + 1, z2 - z1 + 1, Y, 'north', dict(frame='stripped_mangrove_log', post='mangrove_log', fill='green_terracotta',
                                                                  base='mossy_stone_bricks', roof='mangrove', roof_b='mangrove_planks', floor='spruce_planks'), floors=2)
    v.set(x1 + 3, Y + 1, z1 + 3, 'brewing_stand')
    v.set(x1 + 4, Y + 1, z1 + 3, 'water_cauldron[level=3]')
    v.set(x1 + 5, Y + 1, z1 + 3, 'brewing_stand')
    spot('alchemist', x1 + 6, Y + 1, z1 - 2)
    for x in range(x1, x2 + 1, 2):
        if x == x1 + 6:                          # place de Fenna : AIR explicite (un ancien pot a pu être construit)
            v.set(x, Y + 1, z1 - 2, AIR)
        else:
            v.set(x, Y + 1, z1 - 2, 'potted_red_mushroom' if x % 4 else 'potted_crimson_fungus')
