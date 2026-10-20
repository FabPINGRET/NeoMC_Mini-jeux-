"""🏰 Ombrelune : la cité de Havreclair (hub). Module importé par ol_structs.
"""
import math
import random

from tv_build import Vox, AIR
from ol_city_b import alchemist, castle, forge_b, guild, mage_tower, market, stables, tavern, temple
from ol_skit import G, HOUSE_STYLES, SPOTS, brace_ladders, dir_vec, house, round_tower, spot, stone_mix


# ================================================================ HAVRECLAIR
def city():
    v = Vox(101)
    r = v.r
    Y = G
    WALL = 58
    sm = stone_mix(r)
    # ---- sol : douves, pavés
    for x in range(-67, 68):
        for z in range(-67, 68):
            m = max(abs(x), abs(z))
            if 61 <= m <= 65:
                v.fill(x, Y - 4, z, x, Y - 4, z, 'mud')
                v.fill(x, Y - 3, z, x, Y - 1, z, 'water')
                v.set(x, Y, z, AIR)
            elif m in (60, 66):
                v.fill(x, Y - 3, z, x, Y, z, 'stone_bricks' if m == 60 else 'mossy_cobblestone')
    # rues : croix principale, rue circulaire, place
    for x in range(-WALL + 3, WALL - 2):
        for z in range(-WALL + 3, WALL - 2):
            m = max(abs(x), abs(z))
            road = abs(x) <= 3 or abs(z) <= 3 or 50 <= m <= 53
            if road:
                q = r.random()
                v.set(x, Y, z, 'stone_bricks' if q < 0.5 else ('cobblestone' if q < 0.8 else ('andesite' if q < 0.93 else 'mossy_cobblestone')))
            else:
                v.set(x, Y, z, 'grass_block')
    for x in range(-14, 15):
        for z in range(-14, 15):
            d = math.hypot(x, z)
            if d <= 13.5:
                ring = int(d) % 4
                v.set(x, Y, z, ['polished_andesite', 'chiseled_stone_bricks' if (x + z) % 2 else 'stone_bricks', 'polished_diorite', 'smooth_stone'][ring])
    # fontaine et statue du Chevalier de l'Aube
    for x in range(-5, 6):
        for z in range(-5, 6):
            d = math.hypot(x, z)
            if d <= 5.4:
                v.set(x, Y, z, 'chiseled_stone_bricks' if d > 4.4 else 'water')
                if 4.4 < d <= 5.4:
                    v.set(x, Y + 1, z, 'stone_brick_wall')
                if d <= 4.4:
                    v.set(x, Y - 1, z, 'prismarine_bricks')
    v.fill(-1, Y, -1, 1, Y + 2, 1, 'chiseled_quartz_block')
    v.fill(0, Y + 3, 0, 0, Y + 5, 0, 'quartz_pillar')
    v.set(0, Y + 6, 0, 'gold_block')
    v.fill(-1, Y + 4, 0, 1, Y + 4, 0, 'quartz_slab[type=top]')
    v.set(0, Y + 7, 0, 'end_rod')
    for (x, z) in ((-2, 0), (2, 0), (0, -2), (0, 2)):
        v.set(x, Y + 1, z, 'water')
    spot('plaza', 0, Y + 1, 8)
    spot('waystone_hub', 6, Y + 1, 6)
    v.set(6, Y + 1, 6, 'lodestone')
    v.set(6, Y + 2, 6, 'amethyst_cluster[facing=up]')
    # lampadaires des rues
    for k in range(-50, 51, 10):
        if abs(k) > 14:
            for (x, z) in ((4, k), (-4, k), (k, 4), (k, -4)):
                v.set(x, Y + 1, z, 'polished_blackstone_wall')
                v.set(x, Y + 2, z, 'polished_blackstone_wall')
                v.set(x, Y + 3, z, 'lantern')
    for a in range(0, 360, 45):
        x, z = round(12 * math.cos(math.radians(a))), round(12 * math.sin(math.radians(a)))
        v.fill(x, Y + 1, z, x, Y + 2, z, 'spruce_fence')
        v.set(x, Y + 3, z, 'lantern')
    # ---- remparts
    for x in range(-WALL, WALL + 1):
        for z in range(-WALL, WALL + 1):
            m = max(abs(x), abs(z))
            if WALL - 2 <= m <= WALL:
                v.fill(x, Y - 3, z, x, Y + 9, z, sm)
                if m == WALL:
                    v.set(x, Y + 10, z, 'stone_brick_wall' if (x + z) % 2 else AIR)
                    if (x + z) % 2 == 0:
                        v.set(x, Y + 10, z, 'stone_bricks')
                        v.set(x, Y + 11, z, 'stone_brick_slab')
                elif m == WALL - 2:
                    v.set(x, Y + 10, z, 'stone_brick_wall')
                v.set(x, Y + 9, z, 'stone_bricks' if m < WALL else v.get(x, Y + 9, z))
    # meurtrières
    for k in range(-WALL + 4, WALL - 3, 4):
        for (x, z) in ((k, -WALL), (k, WALL), (-WALL, k), (WALL, k)):
            v.set(x, Y + 6, z, 'iron_bars')
    # tours d'angle et de flanc
    for (cx, cz) in [(-WALL, -WALL), (WALL, -WALL), (-WALL, WALL), (WALL, WALL), (-WALL, -29), (-WALL, 29), (WALL, -29), (WALL, 29),
                     (-29, -WALL), (29, -WALL), (-29, WALL), (29, WALL)]:
        corner = abs(cx) == WALL and abs(cz) == WALL
        rr = 5 if corner else 4
        round_tower(v, cx, cz, Y - 3, rr, 17 if corner else 15, sm, floor='spruce_planks', floors=(Y + 6,),
                    crenel='stone_bricks', roof='blue_terracotta' if corner else None, roof_h=9)
        v.lamp(cx, Y + 12, cz)
    # portes (N, S, E, O) : passage 5 de large, herse, tours de flanc
    for facing, (gx, gz) in (('north', (0, -WALL)), ('south', (0, WALL)), ('west', (-WALL, 0)), ('east', (WALL, 0))):
        along_x = facing in ('north', 'south')
        for k in range(-2, 3):
            for t in range(-2, 1):
                x, z = (gx + k, gz + t * (1 if gz > 0 else -1)) if along_x else (gx + t * (1 if gx > 0 else -1), gz + k)
                v.fill(x, Y + 1, z, x, Y + 6, z, AIR)
                v.set(x, Y, z, 'stone_bricks')
        for k in (-6, 6):
            x, z = (gx + k, gz) if along_x else (gx, gz + k)
            round_tower(v, x, z, Y - 3, 2, 15, sm, floor='spruce_planks', crenel='stone_bricks')
        # arche
        for k in range(-2, 3):
            x, z = (gx + k, gz) if along_x else (gx, gz + k)
            v.set(x, Y + 7, z, 'chiseled_stone_bricks' if k == 0 else 'stone_bricks')
            v.set(x, Y + 6, z, 'iron_bars' if abs(k) <= 1 else 'stone_brick_stairs[facing=' + ('east' if (k < 0) == along_x else 'west') + ',half=top]'
                  if along_x else 'iron_bars')
        bx, bz = (gx + 0, gz) if along_x else (gx, gz)
        for k in (-4, 4):
            x, z = (gx + k, gz + (1 if gz < 0 else -1) * -1) if along_x else (gx + (1 if gx < 0 else -1) * -1, gz + k)
            v.set(x, Y + 5, z, 'blue_wall_banner[facing=' + facing + ']')
        # pont sur les douves
        for t in range(1, 10):
            for k in range(-2, 3):
                dx_, dz_ = dir_vec(facing)
                x, z = (gx + k + dx_ * t, gz + dz_ * t) if along_x else (gx + dx_ * t, gz + k + dz_ * t)
                v.set(x, Y, z, 'spruce_planks' if abs(k) < 2 else 'stripped_spruce_log[axis=' + ('z' if along_x else 'x') + ']')
                v.set(x, Y - 1, z, AIR if 3 <= t <= 7 else 'stone_bricks')
                if abs(k) == 2:
                    v.set(x, Y + 1, z, 'spruce_fence')
                    if t in (1, 9):
                        v.set(x, Y + 2, z, 'lantern')
        spot('gate_' + facing, gx + dir_vec(facing)[0] * 12, Y + 1, gz + dir_vec(facing)[1] * 12)
    # ---- château (nord)
    castle(v, Y)
    temple(v, Y)
    mage_tower(v, Y)
    guild(v, Y)
    tavern(v, Y)
    forge_b(v, Y)
    market(v, Y)
    stables(v, Y)
    alchemist(v, Y)
    # ---- maisons (quartiers restants)
    taken = [(-22, -50, 22, -24), (22, -46, 45, -18), (-42, -42, -26, -26), (-46, -18, -20, -2), (-46, 6, -22, 26), (20, 6, 42, 24),
             (14, -15, 46, -4), (22, 28, 44, 46), (-46, 28, -28, 44)]
    houses = []
    rh = random.Random(77)

    def free(box):
        if any(not (box[2] < a or box[0] > c or box[3] < b or box[1] > d) for (a, b, c, d) in taken):
            return False
        if max(abs(box[0]), abs(box[2]), abs(box[1]), abs(box[3])) > 48:
            return False
        if box[0] <= 4 and box[2] >= -4:
            return False
        if any(math.hypot(px_, pz_) < 15 for px_ in (box[0], box[2]) for pz_ in (box[1], box[3])):
            return False
        return not (box[1] <= 4 and box[3] >= -4)
    # rangées de maisons mitoyennes le long des rues (façade sur la rue)
    ROWS = [('z', 5, 'west'), ('z', -11, 'east'), ('x', 5, 'north'), ('x', -11, 'south'),
            ('x', -49, 'north'), ('x', 43, 'south'), ('z', -49, 'west'), ('z', 43, 'east')]
    for axis, band, facing in ROWS:
        t = -49
        while t < 49:
            w_ = rh.randint(5, 7)
            if axis == 'z':                      # rangée le long de z, profondeur selon x
                x1, z1, ww, dd = band, t, 7, w_
            else:
                x1, z1, ww, dd = t, band, w_, 7
            box = (x1, z1, x1 + ww - 1, z1 + dd - 1)
            if free(box):
                taken.append(box)
                houses.append(house(v, x1, z1, ww, dd, Y, facing, rh.choice(HOUSE_STYLES), floors=rh.choice([2, 2, 3]), r=rh))
                t += w_
            else:
                t += 1
    for _ in range(6000):
        w_, d_ = rh.randint(5, 8), rh.randint(5, 8)
        x1, z1 = rh.randint(-48, 48 - w_), rh.randint(-48, 48 - d_)
        box = (x1 - 1, z1 - 1, x1 + w_, z1 + d_)
        if not free(box):
            continue
        cx, cz = x1 + w_ // 2, z1 + d_ // 2
        # porte vers la rue la plus proche (croix ou rue circulaire)
        cands = [(abs(cx) - 4, 'west' if cx > 0 else 'east'), (abs(cz) - 4, 'north' if cz > 0 else 'south'),
                 (50 - abs(cx), 'east' if cx > 0 else 'west'), (50 - abs(cz), 'south' if cz > 0 else 'north')]
        facing = min(cands)[1]
        taken.append(box)
        houses.append(house(v, x1, z1, w_, d_, Y, facing, rh.choice(HOUSE_STYLES), floors=rh.choice([1, 2, 2, 3]), r=rh))
    # jardinets et arbres dans ce qui reste
    for _ in range(600):
        x, z = rh.randint(-48, 48), rh.randint(-48, 48)
        if free((x - 1, z - 1, x + 1, z + 1)) and v.get(x, Y, z) == 'grass_block' and v.get(x, Y + 1, z) is None:
            q = rh.random()
            if q < 0.08:
                v.fill(x, Y + 1, z, x, Y + 4, z, 'oak_log')
                for dx in range(-2, 3):
                    for dz in range(-2, 3):
                        for dy in (4, 5, 6):
                            if abs(dx) + abs(dz) + (dy - 4) <= 3 and v.get(x + dx, Y + dy, z + dz) is None:
                                v.set(x + dx, Y + dy, z + dz, 'oak_leaves[persistent=true]')
                taken.append((x - 2, z - 2, x + 2, z + 2))
            elif q < 0.5:
                v.set(x, Y + 1, z, rh.choice(['short_grass', 'poppy', 'dandelion', 'cornflower', 'oxeye_daisy', 'azure_bluet', 'bush', 'short_grass']))
    # un lampadaire devant une porte de maison la bloque : on l'enlève (AIR explicite, le monde est déjà construit)
    for k in range(-50, 51, 10):
        if abs(k) > 14:
            for (x, z) in ((4, k), (-4, k), (k, 4), (k, -4)):
                if any('_door[' in (v.get(x + ddx, Y + 1, z + ddz) or '') for ddx, ddz in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    v.fill(x, Y + 1, z, x, Y + 3, z, AIR)
    # échelles intérieures des maisons : dos étayé
    brace_ladders(v, 'stripped_spruce_log')
    SPOTS['city_houses'] = houses
    # arbres et jardins dans les espaces verts
    return v
