"""🏗 Terra Nova : structures détaillées (camps, station, fort, caldeira, labo, forge) et donjons des régions.
Chaque fonction renvoie un Vox (tv_build) en coordonnées absolues ; gh(x, z) = hauteur du sol (bloc de dessus) à cet endroit.
"""
import math
from tv_build import Vox, AIR


# ================================================================ camp avancé (balise de voyage au centre, sur la plate-forme)
def camp(cx, cz, y, gh, wood='spruce', roof='green', accent='lantern'):
    v = Vox(cx * 31 + cz)
    log, planks = f'{wood}_log', f'{wood}_planks'
    v.clear(cx - 8, y + 1, cz - 8, cx + 8, y + 14, cz + 8)
    # plate-forme sur pilotis
    v.fill(cx - 7, y, cz - 7, cx + 7, y, cz + 7, planks)
    v.fill(cx - 7, y, cz - 7, cx + 7, y, cz - 7, f'stripped_{log}[axis=x]')
    v.fill(cx - 7, y, cz + 7, cx + 7, y, cz + 7, f'stripped_{log}[axis=x]')
    for x in (cx - 7, cx, cx + 7):
        for z in (cz - 7, cz, cz + 7):
            bottom = min(gh(x, z), y - 1)
            v.fill(x, bottom - 2, z, x, y - 1, z, log)
    v.fill(cx - 7, y + 1, cz - 7, cx + 7, y + 1, cz + 7, f'{wood}_fence', outline=True)
    v.fill(cx - 7, y + 1, cz - 7, cx + 7, y + 1, cz + 7, AIR, only=(AIR,))
    for (a, b) in [(-1, -7), (0, -7), (1, -7), (-1, 7), (0, 7), (1, 7), (-7, -1), (-7, 0), (-7, 1), (7, -1), (7, 0), (7, 1)]:
        v.set(cx + a, y + 1, cz + b, AIR)
    for (a, b) in [(-7, -7), (7, -7), (-7, 7), (7, 7)]:
        v.fill(cx + a, y + 1, cz + b, cx + a, y + 3, cz + b, log)
        v.set(cx + a, y + 4, cz + b, f'{accent}[hanging=false]')
    # escaliers d'accès (4 côtés)
    for (dx, dz, f) in [(0, -1, 'south'), (0, 1, 'north'), (-1, 0, 'east'), (1, 0, 'west')]:
        for i in range(1, 7):
            x, z = cx + dx * (7 + i), cz + dz * (7 + i)
            if gh(x, z) >= y - i + 1:
                break
            for w in (-1, 0, 1):
                xx, zz = (x + w, z) if dx == 0 else (x, z + w)
                v.set(xx, y - i + 1, zz, f'{wood}_stairs[facing={f},half=bottom]')
                v.fill(xx, gh(xx, zz) + 1, zz, xx, y - i, zz, planks, keep=True)
    # cabane (dortoir + table des cartes)
    x1, z1, x2, z2 = cx - 7, cz + 1, cx - 2, cz + 6
    v.fill(x1, y + 1, z1, x2, y + 4, z2, planks, hollow=True)
    v.frame_walls(x1, z1, x2, z2, y + 1, y + 4, planks, f'stripped_{log}')
    v.fill(x1 + 1, y + 1, z1 + 1, x2 - 1, y + 4, z2 - 1, AIR)
    v.windows(x1, z1, x2, z2, y + 2, 2, 'glass_pane', every=2)
    v.opening(cx - 4, y + 1, z1, cx - 4, y + 2, z1)
    v.door(cx - 4, y + 1, z1, 'north', wood)
    v.gable_roof(x1, z1, x2, z2, y + 5, 'z', f'{wood}_stairs', f'{wood}_slab', planks, overhang=1)
    v.fill(x1 + 1, y + 5, z1, x2 - 1, y + 5, z2, planks)
    v.bed(x1 + 1, y + 1, z2 - 2, 'south', roof)
    v.bed(x2 - 1, y + 1, z2 - 2, 'south', roof)
    v.set(x1 + 1, y + 1, z1 + 1, 'cartography_table')
    v.set(x1 + 2, y + 1, z1 + 1, 'barrel[facing=up]')
    v.set(x2 - 1, y + 1, z1 + 1, 'crafting_table')
    v.lamp(cx - 4, y + 4, cz + 4)
    # tour de guet
    tx, tz = cx + 5, cz - 5
    v.fill(tx - 1, y + 1, tz - 1, tx + 1, y + 8, tz + 1, log, outline=True)
    v.fill(tx, y + 1, tz, tx, y + 8, tz, AIR)
    v.fill(tx, y + 1, tz, tx, y + 9, tz, 'ladder[facing=south]')
    v.fill(tx - 1, y + 1, tz - 1, tx + 1, y + 8, tz - 1, log)
    v.set(tx - 1, y + 1, tz + 1, AIR)
    v.set(tx - 1, y + 2, tz + 1, AIR)
    v.fill(tx - 2, y + 9, tz - 2, tx + 2, y + 9, tz + 2, f'{wood}_slab[type=bottom]')
    v.set(tx, y + 9, tz, f'{wood}_trapdoor[facing=south,half=bottom,open=false]')
    v.fill(tx - 2, y + 10, tz - 2, tx + 2, y + 10, tz + 2, f'{wood}_fence', outline=True)
    v.pillars(tx - 2, tz - 2, tx + 2, tz + 2, y + 10, y + 12, log)
    v.gable_roof(tx - 2, tz - 2, tx + 2, tz + 2, y + 13, 'x', f'{wood}_stairs', f'{wood}_slab', planks, overhang=0)
    v.lamp(tx, y + 12, tz)
    # feu de camp et bancs, caisses, antenne
    v.set(cx + 4, y + 1, cz + 4, 'campfire[lit=true]')
    for (a, b, ax) in [(2, 4, 'z'), (6, 4, 'z'), (4, 2, 'x'), (4, 6, 'x')]:
        v.set(cx + a, y + 1, cz + b, f'stripped_{log}[axis={ax}]')
    for (a, b) in [(-6, -6), (-5, -6), (-6, -5), (-4, -6)]:
        v.set(cx + a, y + 1, cz + b, v.r.choice(['barrel[facing=up]', 'barrel[facing=north]', f'{wood}_planks', 'hay_block']))
    v.set(cx - 6, y + 2, cz - 6, 'barrel[facing=up]')
    v.fill(cx + 6, y + 1, cz + 6, cx + 6, y + 6, cz + 6, 'iron_bars')
    v.set(cx + 6, y + 7, cz + 6, 'lightning_rod')
    v.set(cx + 5, y + 5, cz + 6, 'iron_trapdoor[facing=west,half=bottom,open=true]')
    # balise de voyage (lodestone, éclair sur pied, socle)
    v.fill(cx - 1, y, cz - 1, cx + 1, y, cz + 1, 'polished_andesite')
    v.set(cx, y, cz, 'lodestone')
    v.set(cx, y + 1, cz, 'lightning_rod')
    v.clear(cx - 1, y + 1, cz - 1, cx + 3, y + 3, cz + 1)
    v.set(cx, y + 1, cz, 'lightning_rod')
    return v


# ================================================================ station de recherche engloutie (marais)
def station(sx, sz):
    v = Vox(77)
    y0 = 63
    v.clear(sx - 12, y0, sz - 10, sx + 12, y0 + 14, sz + 10)
    v.fill(sx - 11, 58, sz - 9, sx + 11, 62, sz + 9, 'cyan_terracotta')            # fondations
    v.fill(sx - 10, y0, sz - 8, sx + 10, y0, sz + 8, 'polished_andesite')
    # rez-de-chaussée
    v.fill(sx - 10, y0 + 1, sz - 8, sx + 10, y0 + 5, sz + 8, 'white_concrete', hollow=True)
    v.fill(sx - 10, y0 + 1, sz - 8, sx + 10, y0 + 1, sz + 8, 'light_gray_concrete', outline=True)
    v.fill(sx - 9, y0 + 1, sz - 7, sx + 9, y0 + 4, sz + 7, AIR)
    v.windows(sx - 10, sz - 8, sx + 10, sz + 8, y0 + 3, 2, 'cyan_stained_glass_pane', every=3)
    v.fill(sx - 10, y0 + 5, sz - 8, sx + 10, y0 + 5, sz + 8, 'smooth_stone')
    # étage (plus petit, terrasse devant)
    v.fill(sx - 10, y0 + 6, sz - 8, sx + 2, y0 + 9, sz + 8, 'white_concrete', hollow=True)
    v.fill(sx - 9, y0 + 6, sz - 7, sx + 1, y0 + 9, sz + 7, AIR)
    v.windows(sx - 10, sz - 8, sx + 2, sz + 8, y0 + 7, 2, 'cyan_stained_glass_pane', every=2)
    v.fill(sx - 10, y0 + 10, sz - 8, sx + 2, y0 + 10, sz + 8, 'light_gray_concrete')
    v.fill(sx + 3, y0 + 6, sz - 8, sx + 10, y0 + 6, sz + 8, 'iron_bars', outline=True)
    v.fill(sx + 3, y0 + 6, sz - 7, sx + 9, y0 + 6, sz + 7, AIR)
    # escalier intérieur
    v.stair_run(sx - 8, y0 + 1, sz + 6, 1, 0, 5, 'polished_andesite_stairs', 'east')
    v.fill(sx - 8, y0 + 5, sz + 5, sx - 3, y0 + 5, sz + 7, AIR)
    # porte principale (est) et sas
    v.opening(sx + 10, y0 + 1, sz - 1, sx + 10, y0 + 3, sz + 1)
    v.fill(sx + 11, y0, sz - 2, sx + 13, y0, sz + 2, 'polished_andesite')
    # laboratoire (rez-de-chaussée ouest) : paillasses, cuves, alambics
    v.fill(sx - 9, y0 + 1, sz - 7, sx - 4, y0 + 1, sz - 7, 'white_terracotta')
    for x in range(sx - 9, sx - 3, 2):
        v.set(x, y0 + 2, sz - 7, v.r.choice(['brewing_stand', 'flower_pot', 'cauldron']))
    for x in (sx - 9, sx - 7):
        v.fill(x, y0 + 1, sz - 2, x, y0 + 3, sz - 2, 'tinted_glass')
        v.fill(x, y0 + 1, sz - 1, x, y0 + 3, sz - 1, 'glass')
        v.set(x, y0 + 1, sz - 1, 'water')
        v.set(x, y0 + 4, sz - 1, 'iron_trapdoor[facing=north,half=top,open=false]')
    # salle des serveurs (rez-de-chaussée est)
    for z in (sz - 6, sz - 4):
        for x in range(sx + 3, sx + 8):
            v.fill(x, y0 + 1, z, x, y0 + 3, z, v.r.choice(['waxed_copper_grate', 'polished_blackstone', 'waxed_exposed_copper_grate']))
        v.set(sx + 8, y0 + 2, z, 'copper_bulb[lit=true]')
    # pupitres (lutrins = consoles), chaises
    for x in (sx - 2, sx + 1):
        v.set(x, y0 + 1, sz + 6, 'lectern[facing=north]')
        v.set(x, y0 + 1, sz + 4, 'birch_stairs[facing=south,half=bottom]')
    v.set(sx + 6, y0 + 1, sz + 5, 'crafter')
    v.set(sx + 7, y0 + 1, sz + 5, 'crafter')
    v.set(sx + 6, y0 + 2, sz + 5, 'daylight_detector')
    # éclairage
    for x in (sx - 6, sx, sx + 6):
        v.set(x, y0 + 4, sz, 'sea_lantern')
    v.set(sx - 4, y0 + 9, sz, 'sea_lantern')
    # étage : couchettes, bureau du chef, réserve
    v.bed(sx - 9, y0 + 6, sz - 6, 'south', 'light_blue')
    v.bed(sx - 7, y0 + 6, sz - 6, 'south', 'light_blue')
    v.bed(sx - 5, y0 + 6, sz - 6, 'south', 'light_blue')
    v.shelf(sx - 9, y0 + 6, sz + 7, sx - 6, sz + 7)
    v.set(sx - 1, y0 + 6, sz + 2, 'lectern[facing=west]')
    v.set(sx - 1, y0 + 6, sz - 3, 'cartography_table')
    # antenne et parabole sur la terrasse
    v.fill(sx + 7, y0 + 7, sz - 5, sx + 7, y0 + 13, sz - 5, 'iron_bars')
    v.set(sx + 7, y0 + 14, sz - 5, 'lightning_rod')
    for dx in range(-2, 3):
        for dz in range(-2, 3):
            if dx * dx + dz * dz <= 5:
                v.set(sx + 7 + dx, y0 + 11 + (1 if dx * dx + dz * dz >= 4 else 0), sz - 5 + dz, 'white_concrete')
    # inondation, effondrement, végétation
    v.fill(sx - 9, y0 + 1, sz + 1, sx - 1, y0 + 1, sz + 3, 'water', only=(AIR,))
    v.ruin(sx + 2, y0 + 3, sz - 8, sx + 10, y0 + 10, sz + 8, chance=0.22,
           mossy={'white_concrete': 'light_gray_concrete', 'polished_andesite': 'mossy_cobblestone'})
    v.ruin(sx - 10, y0 + 7, sz + 4, sx - 4, y0 + 10, sz + 8, chance=0.3)
    for i in range(18):
        x, z = sx + v.r.randint(-10, 10), v.r.choice([sz - 8, sz + 8])
        top = max([yy for yy in range(y0, y0 + 11) if v.get(x, yy, z) not in (None, AIR)] or [y0])
        for yy in range(top, top - v.r.randint(2, 5), -1):
            if v.get(x, yy, z + (1 if z > sz else -1)) in (None, AIR):
                v.set(x, yy, z + (1 if z > sz else -1), f'vine[{"north" if z > sz else "south"}=true]')
    # drone écrasé
    dx0, dz0 = sx + 16, sz + 10
    v.fill(dx0 - 2, 63, dz0 - 1, dx0 + 2, 64, dz0 + 1, 'iron_block')
    v.fill(dx0 - 1, 65, dz0 - 1, dx0 + 1, 65, dz0, 'light_gray_concrete')
    v.set(dx0, 65, dz0 + 1, 'tinted_glass')
    for (a, b) in [(-4, -3), (4, -3), (-4, 3), (4, 3)]:
        v.set(dx0 + a, 64, dz0 + b, 'iron_trapdoor[facing=north,half=top,open=false]')
        mx, mz = (dx0 + a // 2, dz0 + b // 2)
        v.set(mx, 64, mz, 'iron_bars')
    v.fill(dx0 - 3, 63, dz0 + 2, dx0 + 3, 63, dz0 + 3, 'coal_block')
    v.set(dx0 + 2, 64, dz0 - 2, 'campfire[lit=true,signal_fire=false]')
    v.clear(sx - 5, 64, sz + 3, sx - 5, 65, sz + 3)
    v.clear(sx + 5, 64, sz - 3, sx + 5, 65, sz - 3)
    v.clear(dx0, 66, dz0 + 1, dx0, 67, dz0 + 1)
    return v


# ================================================================ fort des Renégats (canyon)
def fort(fx, fz, fy=64):
    v = Vox(404)
    v.clear(fx - 23, fy + 1, fz - 23, fx + 23, fy + 22, fz + 23)
    v.fill(fx - 22, fy, fz - 22, fx + 22, fy, fz + 22, lambda x, y, z: 'coarse_dirt' if (x * 7 + z * 3) % 5 else 'packed_mud')
    # cour pavée et allées
    v.fill(fx - 2, fy, fz - 19, fx + 2, fy, fz + 19, 'dirt_path')
    v.fill(fx - 19, fy, fz - 2, fx + 20, fy, fz + 2, 'dirt_path')
    # palissade en rondins pointus, chemin de ronde
    for x in range(fx - 20, fx + 21):
        for z in (fz - 20, fz + 20):
            hgt = 7 + (x % 2)
            v.fill(x, fy + 1, z, x, fy + hgt, z, 'stripped_spruce_log')
            v.set(x, fy + hgt + 1, z, 'spruce_fence')
    for z in range(fz - 20, fz + 21):
        for x in (fx - 20, fx + 20):
            hgt = 7 + (z % 2)
            v.fill(x, fy + 1, z, x, fy + hgt, z, 'stripped_spruce_log')
            v.set(x, fy + hgt + 1, z, 'spruce_fence')
    v.fill(fx - 19, fy + 5, fz - 19, fx + 19, fy + 5, fz - 19, 'spruce_slab[type=top]')
    v.fill(fx - 19, fy + 5, fz + 19, fx + 19, fy + 5, fz + 19, 'spruce_slab[type=top]')
    v.fill(fx - 19, fy + 5, fz - 19, fx - 19, fy + 5, fz + 19, 'spruce_slab[type=top]')
    v.fill(fx + 19, fy + 5, fz - 19, fx + 19, fy + 5, fz + 19, 'spruce_slab[type=top]')
    for (x, z) in [(fx - 19, fz - 10), (fx - 19, fz + 10), (fx + 19, fz - 10), (fx + 19, fz + 10)]:
        v.fill(x, fy + 1, z, x, fy + 5, z, f'ladder[facing={"east" if x < fx else "west"}]')
    for x in range(fx - 18, fx + 19, 6):                                    # contreforts
        v.fill(x, fy + 1, fz - 19, x, fy + 4, fz - 19, 'spruce_fence')
        v.fill(x, fy + 1, fz + 19, x, fy + 4, fz + 19, 'spruce_fence')
    # porte est (poterne, herse, bannières)
    v.clear(fx + 20, fy + 1, fz - 2, fx + 20, fy + 5, fz + 2)
    v.fill(fx + 20, fy + 6, fz - 3, fx + 20, fy + 6, fz + 3, 'dark_oak_log[axis=z]')
    v.fill(fx + 21, fy + 1, fz - 4, fx + 23, fy + 9, fz - 3, 'spruce_planks')
    v.fill(fx + 21, fy + 1, fz + 3, fx + 23, fy + 9, fz + 4, 'spruce_planks')
    v.fill(fx + 21, fy + 7, fz - 2, fx + 23, fy + 9, fz + 2, 'spruce_planks')
    v.fill(fx + 21, fy + 10, fz - 4, fx + 23, fy + 10, fz + 4, 'spruce_fence', outline=True)
    v.fill(fx + 22, fy + 5, fz - 2, fx + 22, fy + 6, fz + 2, 'iron_bars')
    for z in (fz - 4, fz + 4):
        v.set(fx + 24, fy + 7, z, 'red_wall_banner[facing=east]')
    # tours d'angle (toit en pyramide, intérieur)
    for (a, b) in [(-20, -20), (20, -20), (-20, 20), (20, 20)]:
        cx, cz = fx + a, fz + b
        v.fill(cx - 3, fy + 1, cz - 3, cx + 3, fy + 13, cz + 3, 'spruce_planks', hollow=True)
        v.frame_walls(cx - 3, cz - 3, cx + 3, cz + 3, fy + 1, fy + 13, 'spruce_planks', 'stripped_dark_oak_log', step=3)
        v.fill(cx - 2, fy + 1, cz - 2, cx + 2, fy + 13, cz + 2, AIR)
        for yy in (fy + 5, fy + 10):
            v.fill(cx - 2, yy, cz - 2, cx + 2, yy, cz + 2, 'spruce_planks')
            v.set(cx + (1 if a < 0 else -1), yy, cz, AIR)
        v.fill(cx + (1 if a < 0 else -1), fy + 1, cz, cx + (1 if a < 0 else -1), fy + 13, cz, 'ladder[facing=' + ('west' if a < 0 else 'east') + ']')
        v.windows(cx - 3, cz - 3, cx + 3, cz + 3, fy + 11, 1, AIR, every=2)
        v.fill(cx - 4, fy + 14, cz - 4, cx + 4, fy + 14, cz + 4, 'dark_oak_planks')
        for i in range(5):
            v.fill(cx - 4 + i, fy + 15 + i, cz - 4 + i, cx + 4 - i, fy + 15 + i, cz + 4 - i, 'dark_oak_planks' if i < 4 else 'dark_oak_slab', outline=True)
        v.set(cx, fy + 20, cz, 'dark_oak_fence')
        v.set(cx, fy + 21, cz, 'red_wool')
        v.lamp(cx, fy + 12, cz)
        door_x = cx - 3 if a > 0 else cx + 3
        v.opening(door_x, fy + 1, cz, door_x, fy + 2, cz)
    # caserne (longue maison, couchettes)
    x1, z1, x2, z2 = fx - 16, fz - 16, fx - 4, fz - 8
    v.fill(x1, fy + 1, z1, x2, fy + 4, z2, 'dark_oak_planks', hollow=True)
    v.frame_walls(x1, z1, x2, z2, fy + 1, fy + 4, 'dark_oak_planks', 'stripped_spruce_log', beam='stripped_spruce_log', step=4)
    v.fill(x1 + 1, fy + 1, z1 + 1, x2 - 1, fy + 4, z2 - 1, AIR)
    v.windows(x1, z1, x2, z2, fy + 2, 2, 'spruce_trapdoor[facing=north,half=bottom,open=true]', every=4)
    v.gable_roof(x1, z1, x2, z2, fy + 5, 'x', 'spruce_stairs', 'spruce_slab', 'dark_oak_planks')
    v.opening(x2, fy + 1, fz - 12, x2, fy + 2, fz - 12)
    v.door(x2, fy + 1, fz - 12, 'east', 'spruce')
    for x in range(x1 + 1, x2 - 1, 3):
        v.bed(x, fy + 1, z1 + 2, 'north', 'red')
        v.bed(x, fy + 1, z2 - 2, 'south', 'red')
        v.set(x + 1, fy + 1, z1 + 1, 'chest[facing=south]')
    v.table(x1 + 2, fy + 1, fz - 12, 'spruce_pressure_plate')
    v.lamp((x1 + x2) // 2, fy + 4, fz - 12)
    # QG du lieutenant (2 niveaux, balcon)
    x1, z1, x2, z2 = fx - 14, fz + 4, fx - 4, fz + 14
    v.fill(x1, fy + 1, z1, x2, fy + 8, z2, 'spruce_planks', hollow=True)
    v.frame_walls(x1, z1, x2, z2, fy + 1, fy + 8, 'spruce_planks', 'stripped_dark_oak_log', step=5)
    v.fill(x1 + 1, fy + 1, z1 + 1, x2 - 1, fy + 8, z2 - 1, AIR)
    v.fill(x1 + 1, fy + 4, z1 + 1, x2 - 1, fy + 4, z2 - 1, 'spruce_planks')
    v.fill(x1 + 2, fy + 4, z1 + 1, x1 + 2, fy + 4, z1 + 3, AIR)
    v.fill(x1 + 2, fy + 1, z1 + 1, x1 + 2, fy + 4, z1 + 1, 'ladder[facing=south]')
    v.windows(x1, z1, x2, z2, fy + 2, 1, 'glass_pane', every=3)
    v.windows(x1, z1, x2, z2, fy + 6, 1, 'glass_pane', every=3)
    v.gable_roof(x1, z1, x2, z2, fy + 9, 'z', 'dark_oak_stairs', 'dark_oak_slab', 'spruce_planks')
    v.opening(x2, fy + 1, fz + 8, x2, fy + 3, fz + 10)
    v.fill(x2 + 1, fy + 4, fz + 7, x2 + 2, fy + 4, fz + 11, 'spruce_slab[type=top]')
    v.fill(x2 + 2, fy + 5, fz + 7, x2 + 2, fy + 5, fz + 11, 'spruce_fence')
    v.opening(x2, fy + 5, fz + 9, x2, fy + 6, fz + 9)
    v.set(fx - 9, fy + 1, fz + 12, 'cartography_table')                       # salle de guerre
    v.set(fx - 10, fy + 1, fz + 12, 'lectern[facing=north]')
    v.fill(fx - 11, fy + 1, fz + 6, fx - 7, fy + 1, fz + 6, 'spruce_stairs[facing=south,half=bottom]')
    v.shelf(x1 + 1, fy + 5, z2 - 1, x2 - 1, z2 - 1, ('bookshelf', 'chiseled_bookshelf[facing=north]', 'barrel[facing=north]'))
    v.bed(fx - 7, fy + 5, fz + 6, 'north', 'black')
    v.set(fx - 12, fy + 5, fz + 8, 'chest[facing=east]')
    v.lamp(fx - 9, fy + 3, fz + 9)
    v.lamp(fx - 9, fy + 7, fz + 9)
    v.clear(fx - 9, fy + 1, fz + 9, fx - 8, fy + 2, fz + 10)                 # place de Varek
    # entrepôt de la cellule
    x1, z1, x2, z2 = fx + 4, fz + 6, fx + 14, fz + 14
    v.fill(x1, fy + 1, z1, x2, fy + 5, z2, 'stripped_dark_oak_log', hollow=True)
    v.fill(x1 + 1, fy + 1, z1 + 1, x2 - 1, fy + 4, z2 - 1, AIR)
    v.fill(x1, fy + 5, z1, x2, fy + 5, z2, 'dark_oak_slab')
    v.opening(x1, fy + 1, fz + 9, x1, fy + 3, fz + 11)
    v.fill(x1 + 1, fy + 1, z1 + 1, x2 - 1, fy + 2, z1 + 1, 'barrel[facing=up]')
    v.fill(x1 + 1, fy + 1, z2 - 1, x2 - 1, fy + 1, z2 - 1, 'chest[facing=north]')
    v.fill(fx + 9, fy + 1, fz + 9, fx + 11, fy + 1, fz + 11, 'polished_blackstone')
    v.set(fx + 10, fy + 1, fz + 10, 'respawn_anchor[charges=4]')
    for (a, b) in [(9, 9), (11, 9), (9, 11), (11, 11)]:
        v.set(fx + a, fy + 2, fz + b, 'iron_chain')
    v.lamp(fx + 10, fy + 4, fz + 10)
    # forge, tentes, cibles, feux, foin
    v.set(fx + 8, fy + 1, fz - 6, 'anvil[facing=north]')
    v.set(fx + 9, fy + 1, fz - 6, 'grindstone[face=floor,facing=north]')
    v.set(fx + 10, fy + 1, fz - 6, 'smithing_table')
    v.fill(fx + 11, fy + 1, fz - 7, fx + 12, fy + 3, fz - 6, 'cobblestone')
    v.set(fx + 11, fy + 1, fz - 6, 'blast_furnace[facing=north,lit=true]')
    for (tx, tz, col) in [(fx - 16, fz, 'red'), (fx - 16, fz - 5, 'brown'), (fx + 6, fz - 16, 'red')]:
        for i in range(3):
            v.fill(tx - 2 + i, fy + 1 + i, tz - 1, tx - 2 + i, fy + 1 + i, tz + 1, f'{col}_wool')
            v.fill(tx + 2 - i, fy + 1 + i, tz - 1, tx + 2 - i, fy + 1 + i, tz + 1, f'{col}_wool')
    for x in range(fx + 6, fx + 17, 2):
        v.set(x, fy + 1, fz - 14, 'spruce_fence')
        v.set(x, fy + 2, fz - 14, 'target')
    v.fill(fx + 6, fy + 1, fz - 17, fx + 16, fy + 1, fz - 17, 'hay_block')
    for (a, b) in [(2, -10), (-2, 0), (8, -2), (-8, 0)]:
        v.set(fx + a, fy + 1, fz + b, 'campfire[lit=true]')
    v.scatter(fx - 18, fy + 1, fz - 18, fx + 18, fz + 18, ['barrel[facing=up]', 'hay_block', 'spruce_planks'], 14)
    return v


# ================================================================ caldeira : temple en ruine, faille temporelle
def caldera(vx, vz, cy, rift_z):
    v = Vox(666)
    # dallage en anneaux, estrade centrale à degrés
    for x in range(vx - 14, vx + 15):
        for z in range(vz - 14, vz + 15):
            d = math.hypot(x - vx, z - vz)
            if d <= 14:
                b = 'polished_blackstone_bricks' if int(d) % 4 == 0 else ('polished_blackstone' if (x + z) % 2 else 'blackstone')
                if d > 12.5:
                    b = 'magma_block'
                v.set(x, cy, z, b)
    for r, yy in ((5, 1), (3, 2)):
        for x in range(vx - r, vx + r + 1):
            for z in range(vz - r, vz + r + 1):
                if math.hypot(x - vx, z - vz) <= r + 0.3:
                    v.set(x, cy + yy, z, 'polished_blackstone_brick_slab[type=bottom]' if yy == 1 else 'chiseled_polished_blackstone')
    # colonnade brisée (12 colonnes)
    for i in range(12):
        a = 2 * math.pi * i / 12
        px, pz = round(vx + 11 * math.cos(a)), round(vz + 11 * math.sin(a))
        hgt = [9, 4, 7, 2, 8, 5, 9, 3, 6, 8, 2, 7][i]
        v.fill(px, cy + 1, pz, px, cy + 1, pz, 'polished_basalt[axis=y]')
        v.fill(px, cy + 2, pz, px, cy + hgt, pz, 'basalt[axis=y]')
        if hgt >= 7:
            v.set(px, cy + hgt + 1, pz, 'magma_block')
        else:
            for k in range(3):                                         # tronçons tombés
                bx, bz = round(px + (k + 1) * math.cos(a + 1.3)), round(pz + (k + 1) * math.sin(a + 1.3))
                v.set(bx, cy + 1, bz, 'basalt[axis=x]')
    # crâne géant (au sud-est), os épars
    sx, sz = vx + 6, vz + 7
    v.fill(sx - 2, cy + 1, sz - 2, sx + 2, cy + 4, sz + 2, 'bone_block')
    v.fill(sx - 1, cy + 2, sz - 2, sx + 1, cy + 3, sz + 2, AIR)
    v.set(sx - 1, cy + 3, sz - 2, 'bone_block')
    v.fill(sx + 3, cy + 1, sz - 1, sx + 5, cy + 2, sz + 1, 'bone_block')
    for k in range(4):
        v.set(sx + 3 + k % 2, cy + 3, sz - 1 + k // 2, 'white_concrete')
    v.scatter(vx - 12, cy + 1, vz - 12, vx + 12, vz + 12, ['bone_block[axis=x]', 'bone_block[axis=z]', 'skeleton_skull'], 16)
    # faille temporelle : arche d'obsidienne pleureuse, portail
    rz = rift_z
    v.fill(vx - 3, cy + 1, rz, vx + 3, cy + 9, rz, 'obsidian')
    v.fill(vx - 2, cy + 1, rz, vx + 2, cy + 7, rz, AIR)
    v.fill(vx - 2, cy + 1, rz, vx - 2, cy + 7, rz, 'crying_obsidian')
    v.fill(vx + 2, cy + 1, rz, vx + 2, cy + 7, rz, 'crying_obsidian')
    v.fill(vx - 2, cy + 8, rz, vx + 2, cy + 8, rz, 'crying_obsidian')
    v.fill(vx - 1, cy + 2, rz, vx + 1, cy + 7, rz, 'purple_stained_glass_pane')
    v.fill(vx - 3, cy + 10, rz, vx + 3, cy + 10, rz, 'polished_blackstone_brick_wall')
    v.set(vx, cy + 11, rz, 'end_rod[facing=up]')
    for x in (vx - 4, vx + 4):
        v.fill(x, cy + 1, rz, x, cy + 4, rz, 'chiseled_polished_blackstone')
        v.set(x, cy + 5, rz, 'soul_lantern[hanging=false]')
    v.fill(vx - 2, cy, rz + 1, vx + 2, cy, rz + 3, 'crying_obsidian')
    # cascades de lave dans des niches au bord (sources contenues)
    for a in (40, 140, 220, 320):
        r = math.radians(a)
        px, pz = round(vx + 14 * math.cos(r)), round(vz + 14 * math.sin(r))
        v.fill(px - 1, cy, pz - 1, px + 1, cy, pz + 1, 'blackstone')
        v.set(px, cy, pz, 'lava')
        v.fill(px - 1, cy + 1, pz - 1, px + 1, cy + 1, pz + 1, 'polished_blackstone_wall')
        v.set(px, cy + 1, pz, AIR)
    # cristaux de sulfure
    v.scatter(vx - 13, cy + 1, vz - 13, vx + 13, vz + 13, ['sulfur', 'potent_sulfur'], 10)
    v.clear(vx - 2, cy + 1, vz + 13, vx + 2, cy + 6, vz + 15)          # entrée sud (route)
    return v


# ================================================================ labo du Dr Ossei et forge de Jo (colonie)
def lab(G):
    v = Vox(5)
    x1, z1, x2, z2 = 10, -10, 20, -4
    v.clear(x1, G + 1, z1, x2, G + 9, z2)
    v.fill(x1, G, z1, x2, G, z2, 'polished_andesite')
    v.fill(x1 + 1, G, z1 + 1, x2 - 1, G, z2 - 1, lambda x, y, z: 'white_concrete' if (x + z) % 2 else 'light_gray_concrete')
    v.fill(x1, G + 1, z1, x2, G + 5, z2, 'white_concrete', hollow=True)
    v.frame_walls(x1, z1, x2, z2, G + 1, G + 5, 'white_concrete', 'light_gray_concrete', step=5)
    v.fill(x1 + 1, G + 1, z1 + 1, x2 - 1, G + 5, z2 - 1, AIR)
    v.windows(x1, z1, x2, z2, G + 2, 2, 'light_blue_stained_glass_pane', every=2, skip={(15, z2), (14, z2), (16, z2)})
    v.fill(x1 - 1, G + 6, z1 - 1, x2 + 1, G + 6, z2 + 1, 'smooth_stone_slab')
    v.fill(x1 + 2, G + 6, z1 + 2, x2 - 2, G + 6, z2 - 2, 'light_blue_stained_glass')    # verrière
    v.opening(14, G + 1, z2, 16, G + 3, z2)
    v.fill(13, G + 4, z2, 17, G + 4, z2, 'cyan_concrete')
    v.fill(13, G + 5, z2 + 1, 17, G + 5, z2 + 1, 'smooth_stone_slab')
    # paillasses, cuve à dinosaure, fossile, bestiaire
    v.fill(11, G + 1, z1 + 1, 13, G + 1, z1 + 1, 'white_terracotta')
    v.set(11, G + 2, z1 + 1, 'brewing_stand')
    v.set(12, G + 2, z1 + 1, 'flower_pot')
    v.set(13, G + 2, z1 + 1, 'sniffer_egg')
    v.fill(17, G + 1, z1 + 1, 19, G + 4, z1 + 1, 'tinted_glass')
    v.fill(18, G + 1, z1 + 1, 18, G + 3, z1 + 1, 'water')
    v.set(18, G + 1, z1 + 1, 'sea_pickle[pickles=4,waterlogged=true]')
    v.set(19, G + 1, z2 - 2, 'lectern[facing=west]')
    v.shelf(19, G + 2, z1 + 2, 19, z1 + 3, ('bookshelf', 'chiseled_bookshelf[facing=west]'))
    v.fill(11, G + 1, z2 - 2, 11, G + 3, z2 - 2, 'bone_block')
    v.set(11, G + 4, z2 - 2, 'skeleton_skull[rotation=4]')
    v.set(12, G + 1, z2 - 1, 'cauldron')
    v.lamp(15, G + 5, -7, True, 'lantern')
    v.set(13, G + 5, z1 + 1, 'sea_lantern')
    return v


def forge(G):
    v = Vox(6)
    v.clear(-17, G + 1, 3, -5, G + 9, 11)
    v.fill(-16, G, 4, -6, G, 10, lambda x, y, z: 'stone_bricks' if (x + z) % 3 else 'cracked_stone_bricks')
    for (x, z) in [(-16, 4), (-6, 4), (-16, 10), (-6, 10), (-11, 4), (-11, 10)]:
        v.fill(x, G + 1, z, x, G + 4, z, 'stripped_dark_oak_log')
    v.fill(-16, G + 5, 4, -6, G + 5, 4, 'dark_oak_log[axis=x]')
    v.fill(-16, G + 5, 10, -6, G + 5, 10, 'dark_oak_log[axis=x]')
    v.gable_roof(-16, 4, -6, 10, G + 5, 'x', 'deepslate_tile_stairs', 'deepslate_tile_slab', 'dark_oak_planks', overhang=1)
    # four et cheminée
    v.fill(-16, G + 1, 8, -13, G + 4, 10, 'bricks')
    v.fill(-15, G + 1, 9, -14, G + 2, 9, AIR)
    v.set(-15, G + 1, 9, 'lava')
    v.set(-14, G + 1, 9, 'magma_block')
    v.fill(-16, G + 5, 9, -14, G + 12, 10, 'bricks')
    v.fill(-15, G + 6, 9, -15, G + 12, 9, AIR)
    v.set(-15, G + 12, 9, 'campfire[lit=true,signal_fire=true]')
    v.set(-12, G + 1, 9, 'blast_furnace[facing=south,lit=true]')
    v.set(-11, G + 1, 9, 'smoker[facing=south,lit=true]')
    v.set(-10, G + 1, 6, 'anvil[facing=east]')
    v.set(-9, G + 1, 6, 'chipped_anvil[facing=east]')
    v.set(-8, G + 1, 9, 'smithing_table')
    v.set(-7, G + 1, 9, 'grindstone[face=floor,facing=south]')
    v.set(-13, G + 1, 5, 'water_cauldron[level=3]')
    v.fill(-7, G + 1, 5, -7, G + 2, 5, 'barrel[facing=up]')
    for x in (-10, -8):                                              # râtelier d'armes (barres + trappes)
        v.set(x, G + 1, 4, 'iron_bars')
        v.set(x, G + 2, 4, 'iron_trapdoor[facing=south,half=top,open=false]')
    v.lamp(-11, G + 4, 7)
    return v


# ================================================================ donjons
def tree_heart(mx, mz, g):
    """Nord : l'Arbre-Mère creux. Racines, tronc creux à escalier en colimaçon, plates-formes, nid au sommet."""
    v = Vox(13)
    R = 4
    top = g + 38
    v.clear(mx - 14, g + 1, mz - 14, mx + 14, top + 14, mz + 14)
    # butte de racines
    for x in range(mx - 9, mx + 10):
        for z in range(mz - 9, mz + 10):
            d = math.hypot(x - mx, z - mz)
            if d < 9:
                hh = round((9 - d) * 0.6)
                v.fill(x, g - 2, z, x, g + hh, z, 'rooted_dirt' if d > 5 else 'moss_block')
    for a in range(0, 360, 30):
        r = math.radians(a)
        for k in range(4, 12):
            x, z = round(mx + k * math.cos(r)), round(mz + k * math.sin(r))
            y = g + max(0, round(5 - k * 0.5))
            v.set(x, y, z, 'mangrove_wood')
            v.set(x, y - 1, z, 'mangrove_roots')
    # tronc creux
    for y in range(g, top + 1):
        rr = R + (2 if y < g + 6 else (1 if y < g + 14 else 0))
        for x in range(mx - rr - 1, mx + rr + 2):
            for z in range(mz - rr - 1, mz + rr + 2):
                d = math.hypot(x - mx, z - mz)
                if rr - 0.5 <= d <= rr + 0.6:
                    v.set(x, y, z, 'mangrove_log[axis=y]' if (x + z + y // 5) % 4 else 'mangrove_wood')
                elif d < rr - 0.5:
                    v.set(x, y, z, AIR)
    v.fill(mx - R + 1, g, mz - R + 1, mx + R - 1, g, mz + R - 1, 'moss_block', only=(AIR,))
    v.spiral(mx, mz, R - 1, g + 1, top - 1, 'mangrove_slab[type=top]', center='mangrove_log[axis=y]', per_turn=14)
    for yy in (g + 12, g + 24):                                              # paliers et fenêtres
        v.fill(mx - R + 1, yy, mz - R + 1, mx - 1, yy, mz + R - 1, 'mangrove_planks', only=(AIR, None))
        v.set(mx + R + (1 if yy < g + 14 else 0), yy + 1, mz, AIR)
        v.set(mx + R + (1 if yy < g + 14 else 0), yy + 2, mz, AIR)
        v.lamp(mx - 2, yy + 3, mz, True, 'lantern')
        v.set(mx - R + 1, yy + 1, mz + 1, 'barrel[facing=up]')
    # entrée entre les racines (est)
    v.clear(mx + R - 1, g + 1, mz - 1, mx + R + 3, g + 3, mz + 1)
    v.fill(mx + R + 3, g + 1, mz - 2, mx + R + 6, g + 1, mz + 2, AIR)
    v.lamp(mx + R + 2, g + 3, mz - 2, False, 'lantern')
    # couronne de feuillage, nid au sommet
    for (cx, cy, cz, r) in [(mx, top + 4, mz, 11), (mx - 9, top - 3, mz + 4, 6), (mx + 8, top - 2, mz - 6, 6), (mx + 3, top + 9, mz + 2, 7)]:
        for y in range(-r // 2, r // 2 + 1):
            rr = int((r * r - (2 * y) ** 2) ** 0.5) if r * r - (2 * y) ** 2 > 0 else 0
            for x in range(cx - rr, cx + rr + 1):
                for z in range(cz - rr, cz + rr + 1):
                    if math.hypot(x - cx, z - cz) <= rr and v.get(x, cy + y, z) in (None, AIR) and v.r.random() < 0.93:
                        v.set(x, cy + y, z, 'mangrove_leaves[persistent=true]')
    v.fill(mx - 5, top, mz - 5, mx + 5, top, mz + 5, 'mangrove_planks')
    v.clear(mx - 5, top + 1, mz - 5, mx + 5, top + 6, mz + 5)
    for x in range(mx - 4, mx + 5):
        for z in range(mz - 4, mz + 5):
            d = math.hypot(x - mx, z - mz)
            if 3 <= d <= 4.6:
                v.set(x, top + 1, z, 'hay_block')
            if d < 2.5:
                v.set(x, top + 1, z, 'moss_carpet')
    v.set(mx, top + 1, mz, 'sniffer_egg')
    v.set(mx + 1, top + 1, mz - 1, 'turtle_egg[eggs=3]')
    v.scatter(mx - 4, top + 1, mz - 4, mx + 4, mz + 4, ['bone_block[axis=x]', 'skeleton_skull'], 5)
    v.set(mx, top, mz, 'mangrove_planks')
    v.clear(mx - 1, top, mz - 1, mx - 1, top, mz - 1)                         # arrivée de l'escalier
    for a in range(0, 360, 40):
        r = math.radians(a)
        x, z = round(mx + 9 * math.cos(r)), round(mz + 9 * math.sin(r))
        v.fill(x, top - 10, z, x, top - 1, z, 'vine[north=true]', only=(AIR, None))
    return v, (mx + 0.5, top + 1, mz + 0.5), (mx + R + 4, g + 1, mz)


def spire_nest(px, pz, g):
    """Est : le Pic du Nid, piton creux, escalier intérieur, nid de la reine des ptéranodons au sommet."""
    v = Vox(21)
    top = g + 46
    for y in range(g - 2, top + 1):
        t = (y - g) / (top - g)
        r = 7.5 - 3.2 * max(0, t)
        for x in range(px - 9, px + 10):
            for z in range(pz - 9, pz + 10):
                d = math.hypot(x - px, z - pz) + 0.6 * math.sin(y * 0.7 + x * 0.3)
                if d <= r:
                    if d >= r - 1.6:
                        v.set(x, y, z, ['andesite', 'stone', 'tuff', 'stone', 'calcite'][(y // 5) % 5])
                    else:
                        v.set(x, y, z, AIR)
    v.spiral(px, pz, 3, g + 1, top - 1, 'stone_brick_slab[type=top]', center='stone_bricks', per_turn=12)
    v.clear(px - 9, g + 1, pz - 1, px - 4, g + 3, pz + 1)                      # entrée ouest
    v.set(px - 7, g + 4, pz, 'lantern[hanging=true]')
    for yy in range(g + 8, top, 8):                                          # meurtrières lumineuses
        v.set(px + round(6.5 - 2.6 * (yy - g) / (top - g)), yy, pz, 'glass')
        v.set(px, yy, pz - round(6.5 - 2.6 * (yy - g) / (top - g)), 'glass')
        v.lamp(px - 2, yy + 2, pz + 1, False, 'lantern')
    # nid au sommet
    v.fill(px - 6, top, pz - 6, px + 6, top, pz + 6, 'stone', only=(None, AIR))
    v.clear(px - 6, top + 1, pz - 6, px + 6, top + 6, pz + 6)
    for x in range(px - 6, px + 7):
        for z in range(pz - 6, pz + 7):
            d = math.hypot(x - px, z - pz)
            if d <= 6.4:
                v.set(x, top, z, 'stone')
            if 4.5 <= d <= 6.4:
                v.set(x, top + 1, z, 'hay_block' if (x + z) % 3 else 'dead_bush') if d <= 5.5 else v.set(x, top + 1, z, 'spruce_fence' if (x + z) % 2 else AIR)
            if d < 3:
                v.set(x, top + 1, z, 'brown_carpet')
    v.set(px, top + 1, pz, 'sniffer_egg')
    v.set(px + 1, top + 1, pz + 1, 'sniffer_egg')
    v.clear(px - 1, top, pz - 1, px, top, pz)                                 # trappe de l'escalier
    v.scatter(px - 5, top + 1, pz - 5, px + 5, pz + 5, ['bone_block[axis=x]', 'white_carpet', 'skeleton_skull'], 6)
    return v, (px + 0.5, top + 1, pz + 0.5), (px - 7, g + 1, pz)


def mine(mx, mz, g, h):
    """Ouest : la mine abandonnée, creusée dans une mesa (galeries étayées, rails, salles, repaire des slashers)."""
    v = Vox(31)
    y = g + 1
    # entrée (est), galerie principale vers l'ouest, deux galeries latérales, salle finale
    def tunnel(x1, z1, x2, z2, w=1, hgt=4):
        if x1 == x2:
            for z in range(min(z1, z2), max(z1, z2) + 1):
                v.fill(x1 - w, y, z, x1 + w, y + hgt - 1, z, AIR)
                v.fill(x1 - w, y - 1, z, x1 + w, y - 1, z, 'gravel' if (z % 5) else 'packed_mud')
                if z % 4 == 0:
                    v.fill(x1 - w - 1, y, z, x1 - w - 1, y + hgt - 1, z, 'spruce_log')
                    v.fill(x1 + w + 1, y, z, x1 + w + 1, y + hgt - 1, z, 'spruce_log')
                    v.fill(x1 - w - 1, y + hgt, z, x1 + w + 1, y + hgt, z, 'spruce_planks')
                    if z % 8 == 0:
                        v.set(x1, y + hgt - 1, z, 'lantern[hanging=true]')
            v.fill(x1, y, min(z1, z2), x1, y, max(z1, z2), 'rail[shape=north_south]')
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                v.fill(x, y, z1 - w, x, y + hgt - 1, z1 + w, AIR)
                v.fill(x, y - 1, z1 - w, x, y - 1, z1 + w, 'gravel' if (x % 5) else 'packed_mud')
                if x % 4 == 0:
                    v.fill(x, y, z1 - w - 1, x, y + hgt - 1, z1 - w - 1, 'spruce_log')
                    v.fill(x, y, z1 + w + 1, x, y + hgt - 1, z1 + w + 1, 'spruce_log')
                    v.fill(x, y + hgt, z1 - w - 1, x, y + hgt, z1 + w + 1, 'spruce_planks')
                    if x % 8 == 0:
                        v.set(x, y + hgt - 1, z1, 'lantern[hanging=true]')
            v.fill(min(x1, x2), y, z1, max(x1, x2), y, z1, 'rail[shape=east_west]')
    ex = mx + 22
    tunnel(ex, mz, mx - 6, mz)
    tunnel(mx + 8, mz - 12, mx + 8, mz + 12)
    tunnel(mx - 6, mz - 10, mx - 6, mz + 10)
    # salles
    def room(cx, cz, rx, rz, hgt=5):
        v.fill(cx - rx, y, cz - rz, cx + rx, y + hgt, cz + rz, AIR)
        v.fill(cx - rx, y - 1, cz - rz, cx + rx, y - 1, cz + rz, 'spruce_planks')
        for (a, b) in [(-rx, -rz), (rx, -rz), (-rx, rz), (rx, rz)]:
            v.fill(cx + a, y, cz + b, cx + a, y + hgt, cz + b, 'spruce_log')
        v.lamp(cx, y + hgt, cz)
    room(mx + 8, mz - 15, 4, 3)                                              # dépôt (nord)
    v.fill(mx + 5, y, mz - 17, mx + 11, y + 1, mz - 17, 'barrel[facing=south]')
    v.set(mx + 6, y, mz - 15, 'tnt')
    v.set(mx + 7, y, mz - 15, 'tnt')
    room(mx + 8, mz + 15, 4, 3)                                              # dortoir (sud)
    v.bed(mx + 5, y, mz + 17, 'south', 'brown')
    v.bed(mx + 7, y, mz + 17, 'south', 'brown')
    v.set(mx + 10, y, mz + 17, 'chest[facing=north]')
    v.set(mx + 11, y, mz + 13, 'crafting_table')
    # filons dans les parois
    for _ in range(70):
        x, z, yy = mx + v.r.randint(-12, 24), mz + v.r.randint(-20, 20), y + v.r.randint(0, 4)
        if v.get(x, yy, z) is None:
            nb = any(v.get(x + a, yy, z + b) == AIR for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            if nb:
                v.set(x, yy, z, v.r.choice(['iron_ore', 'gold_ore', 'coal_ore', 'copper_ore', 'iron_ore', 'raw_iron_block']))
    # repaire (salle finale, ouest) : grande caverne, os, toiles
    cx, cz = mx - 10, mz
    for x in range(cx - 8, cx + 9):
        for z in range(cz - 8, cz + 9):
            for yy in range(y, y + 9):
                d = math.hypot(x - cx, z - cz) / 8 + max(0, yy - y - 3) / 8
                if d < 1.0:
                    v.set(x, yy, z, AIR)
            if math.hypot(x - cx, z - cz) < 8:
                v.set(x, y - 1, z, 'coarse_dirt' if (x + z) % 3 else 'gravel')
    v.scatter(cx - 6, y, cz - 6, cx + 6, cz + 6, ['bone_block[axis=x]', 'bone_block[axis=z]', 'cobweb', 'skeleton_skull', 'hay_block'], 22)
    v.set(cx, y + 6, cz, 'iron_chain')
    v.set(cx, y + 5, cz, 'lantern[hanging=true]')
    v.set(cx - 6, y, cz, 'chest[facing=east]')
    # entrée : portique de bois et panneau
    v.fill(ex + 1, y, mz - 2, ex + 3, y + 4, mz + 2, AIR)
    v.fill(ex + 1, y, mz - 2, ex + 1, y + 4, mz - 2, 'spruce_log')
    v.fill(ex + 1, y, mz + 2, ex + 1, y + 4, mz + 2, 'spruce_log')
    v.fill(ex + 1, y + 4, mz - 2, ex + 1, y + 4, mz + 2, 'spruce_log[axis=z]')
    return v, (cx + 0.5, y, cz + 0.5), (ex + 3, y, mz)


def lava_tube(vx, vz, ex, y):
    """Sud : tube de lave creusé dans le flanc ouest du volcan, jusqu'à la crypte du carnotaure alpha."""
    v = Vox(41)
    end_x = vx - 22
    for x in range(ex - 2, end_x - 3):                                    # de l'entrée (ouest) jusqu'à la crypte
        t = (x - end_x) / (ex - end_x)
        cz = vz + round(4 * math.sin(t * 5))
        for z in range(cz - 4, cz + 5):
            for yy in range(y - 1, y + 6):
                dz, dy = (z - cz) / 3.4, (yy - (y + 1.6)) / 3.0
                if dz * dz + dy * dy <= 1:
                    v.set(x, yy, z, AIR)
                elif dz * dz + dy * dy <= 1.6:
                    v.set(x, yy, z, v.r.choice(['basalt[axis=y]', 'blackstone', 'magma_block', 'basalt[axis=y]', 'tuff']))
        v.set(x, y - 1, cz + 2, 'lava')                                   # rigole de lave le long du mur
        v.set(x, y - 2, cz + 2, 'blackstone')
        v.set(x, y - 1, cz + 3, 'blackstone')
        v.set(x, y - 1, cz + 1, 'blackstone')
        if x % 7 == 0:
            v.set(x, y + 4, cz - 1, 'shroomlight')
        if x % 9 == 3:
            v.set(x, y, cz - 2, 'sulfur')
    # crypte : salle en dôme, sarcophage d'os, fossile
    cx, cz = end_x - 6, vz
    for x in range(cx - 9, cx + 10):
        for z in range(cz - 9, cz + 10):
            for yy in range(y - 1, y + 10):
                d = math.hypot(x - cx, z - cz) / 8.5 + max(0, yy - y) / 9.5
                if d < 1:
                    v.set(x, yy, z, AIR)
            if math.hypot(x - cx, z - cz) < 8.5:
                v.set(x, y - 1, z, 'polished_blackstone_bricks' if (x + z) % 2 else 'cracked_polished_blackstone_bricks')
    for a in range(0, 360, 45):
        r = math.radians(a)
        px, pz = round(cx + 7 * math.cos(r)), round(cz + 7 * math.sin(r))
        v.fill(px, y, pz, px, y + 4, pz, 'polished_basalt[axis=y]')
        v.set(px, y + 5, pz, 'magma_block')
    v.fill(cx - 2, y, cz - 1, cx + 2, y, cz + 1, 'bone_block[axis=x]')
    v.fill(cx - 2, y + 1, cz, cx + 2, y + 1, cz, 'bone_block[axis=x]')
    v.set(cx + 3, y + 1, cz, 'skeleton_skull[rotation=4]')
    v.set(cx - 6, y, cz, 'chest[facing=east]')
    v.set(cx, y + 8, cz, 'iron_chain')
    v.set(cx, y + 7, cz, 'soul_lantern[hanging=true]')
    # entrée : arche de basalte sur le flanc
    ez = vz + round(4 * math.sin(5))
    v.fill(ex - 2, y, ez - 4, ex - 2, y + 5, ez - 4, 'polished_basalt[axis=y]')
    v.fill(ex - 2, y, ez + 4, ex - 2, y + 5, ez + 4, 'polished_basalt[axis=y]')
    v.fill(ex - 2, y + 5, ez - 4, ex - 2, y + 5, ez + 4, 'polished_blackstone_bricks')
    v.clear(ex - 6, y, ez - 2, ex - 2, y + 3, ez + 2)                      # parvis creusé dans la pente
    v.fill(ex - 6, y - 1, ez - 2, ex - 2, y - 1, ez + 2, 'basalt[axis=y]')
    return v, (cx + 4.5, y, cz + 0.5), (ex - 3, y, ez)
