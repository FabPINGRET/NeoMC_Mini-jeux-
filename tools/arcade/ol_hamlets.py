"""🏰 Ombrelune : villages de Valdor (village générique, Brumecombe, moulin, fort des bandits). Module importé par ol_structs.
"""
import math
import random

from tv_build import Vox, AIR
import ol_world as W
from ol_skit import ARENAS, HOUSE_STYLES, LORE, brace_ladders, cone_roof, house, round_tower, spot


# ================================================================ VALDOR
def village(cx, cz, y, n_houses, seed, style_ids=(0, 1, 2, 3), name='village', well=True, fields=True):
    v = Vox(seed)
    r = random.Random(seed)
    # place centrale
    for x in range(cx - 6, cx + 7):
        for z in range(cz - 6, cz + 7):
            if math.hypot(x - cx, z - cz) <= 6.5:
                v.set(x, y, z, 'gravel' if r.random() < 0.3 else 'cobblestone')
    if well:
        v.fill(cx - 1, y + 1, cz - 1, cx + 1, y + 1, cz + 1, 'cobblestone', hollow=False)
        v.set(cx, y + 1, cz, 'water')
        for (x, z) in ((cx - 1, cz - 1), (cx + 1, cz - 1), (cx - 1, cz + 1), (cx + 1, cz + 1)):
            v.fill(x, y + 2, z, x, y + 3, z, 'oak_fence')
        v.fill(cx - 1, y + 4, cz - 1, cx + 1, y + 4, cz + 1, 'oak_slab')
        v.set(cx, y + 3, cz, 'iron_chain')
    spots = []
    angs = [i * 2 * math.pi / n_houses + r.uniform(-0.2, 0.2) for i in range(n_houses)]
    for i, a in enumerate(angs):
        d = r.uniform(13, 17)
        w_, dd = r.randint(6, 9), r.randint(6, 8)
        hx, hz = round(cx + d * math.cos(a) - w_ / 2), round(cz + d * math.sin(a) - dd / 2)
        ddx, ddz = cx - (hx + w_ / 2), cz - (hz + dd / 2)
        facing = ('east' if ddx > 0 else 'west') if abs(ddx) > abs(ddz) else ('south' if ddz > 0 else 'north')
        door = house(v, hx, hz, w_, dd, y, facing, HOUSE_STYLES[r.choice(style_ids)], floors=r.choice([1, 2]), r=r)
        spots.append(door)
        # chemin vers la place
        px, pz = door[0], door[2]
        for t in range(20):
            qx, qz = round(px + (cx - px) * t / 20), round(pz + (cz - pz) * t / 20)
            if v.get(qx, y, qz) is None:
                v.set(qx, y, qz, 'dirt_path')
    if fields:
        for (fx, fz) in ((cx + 22, cz - 8), (cx - 28, cz + 6)):
            for x in range(fx, fx + 9):
                for z in range(fz, fz + 9):
                    if (x - fx) % 4 == 0:
                        v.set(x, y, z, 'water')
                    else:
                        v.set(x, y, z, 'farmland[moisture=7]')
                        v.set(x, y + 1, z, r.choice(['wheat[age=7]', 'carrots[age=7]', 'potatoes[age=7]', 'wheat[age=5]']))
            v.fill(fx - 1, y + 1, fz - 1, fx + 9, y + 1, fz + 9, 'oak_fence', outline=True)
            v.set(fx + 4, y + 1, fz - 1, 'oak_fence_gate[facing=north]')
    # lanternes
    for a in range(0, 360, 90):
        x, z = round(cx + 7.5 * math.cos(math.radians(a + 45))), round(cz + 7.5 * math.sin(math.radians(a + 45)))
        v.fill(x, y + 1, z, x, y + 2, z, 'spruce_fence')
        v.set(x, y + 3, z, 'lantern')
    return v, spots


def brumecombe():
    cx, cz = W.P['brumecombe']
    y = 66
    v, doors = village(cx, cz, y, 7, 201)
    spot('tessa', cx + 2, y + 1, cz + 2)
    spot('waystone_w', cx - 3, y + 1, cz - 3)
    v.set(cx - 3, y + 1, cz - 3, 'lodestone')
    v.set(cx - 3, y + 2, cz - 3, 'amethyst_cluster[facing=up]')
    spot('village_w', cx, y + 1, cz)
    # auberge (plus grande) au nord de la place
    house(v, cx - 6, cz - 30, 12, 9, y, 'south', HOUSE_STYLES[0], floors=2)
    spot('farmer', cx + 22, y + 1, cz - 10)
    brace_ladders(v, 'stripped_spruce_log')                  # échelles intérieures des maisons : dos étayé
    return v


def windmill():
    cx, cz = W.P['mill']
    y = 66
    v = Vox(202)
    round_tower(v, cx, cz, y + 1, 4, 14, lambda x, yy, z: 'white_terracotta' if yy % 4 else 'stripped_oak_log', floor='oak_planks', floors=(y + 7,))
    cone_roof(v, cx, cz, y + 15, 5, 'spruce_planks', 6, None)
    # ailes (croix devant la tour, face sud)
    for k in range(-9, 10):
        v.set(cx + k, y + 13, cz + 6, 'oak_fence' if abs(k) > 1 else 'stripped_oak_log[axis=z]')
        v.set(cx, y + 13 + k, cz + 6, 'oak_fence' if abs(k) > 1 else 'stripped_oak_log[axis=z]')
        if abs(k) > 2:
            v.set(cx + k, y + 14 if k > 0 else y + 12, cz + 6, 'white_wool')
            v.set(cx + (1 if k < 0 else -1), y + 13 + k, cz + 6, 'white_wool')
    v.set(cx, y + 13, cz + 5, 'stripped_oak_log[axis=z]')
    v.fill(cx, y + 1, cz + 4, cx, y + 2, cz + 4, AIR)
    v.door(cx, y + 1, cz + 4, 'south', 'oak')
    for k in range(3):
        v.set(cx - 2 + k * 2, y + 1, cz - 2, 'hay_block')
    return v


def bandit_fort():
    """Fort des brigands de Brennic : palissade, tours de guet, tentes, grande hutte (arène du boss dans la cour)."""
    x1, z1, x2, z2 = -222, -60, -188, -24
    y = 70
    v = Vox(203)
    r = v.r
    cx, cz = (x1 + x2) // 2, (z1 + z2) // 2
    v.fill(x1, y, z1, x2, y, z2, 'coarse_dirt')
    for x in range(x1, x2 + 1):
        for z in range(z1, z2 + 1):
            if r.random() < 0.3:
                v.set(x, y, z, r.choice(['dirt_path', 'gravel', 'podzol']))
    for x in range(x1, x2 + 1):
        for z in range(z1, z2 + 1):
            if x in (x1, x2) or z in (z1, z2):
                hgt = 6 + r.randint(0, 1)
                v.fill(x, y - 2, z, x, y + hgt, z, 'spruce_log')
                if (x + z) % 2 == 0:
                    v.set(x, y + hgt + 1, z, 'spruce_fence')
    # porte est (vers le village)
    v.fill(x2, y + 1, cz - 2, x2, y + 7, cz + 2, AIR)
    v.fill(x2, y + 6, cz - 3, x2, y + 6, cz + 3, 'stripped_spruce_log[axis=z]')
    for zz in (cz - 3, cz + 3):
        v.fill(x2 + 1, y + 1, zz, x2 + 1, y + 9, zz, 'spruce_log')
        v.set(x2 + 1, y + 10, zz, 'skeleton_skull')
    # chemin de ronde
    for x in range(x1 + 1, x2):
        for z in (z1 + 1, z2 - 1):
            v.set(x, y + 4, z, 'spruce_slab[type=top]')
    for z in range(z1 + 1, z2):
        for x in (x1 + 1, x2 - 1):
            v.set(x, y + 4, z, 'spruce_slab[type=top]')
    # tours de guet
    for (tx, tz) in ((x1 + 2, z1 + 2), (x2 - 2, z1 + 2), (x1 + 2, z2 - 2), (x2 - 2, z2 - 2)):
        for (px_, pz_) in ((tx - 1, tz - 1), (tx + 1, tz - 1), (tx - 1, tz + 1), (tx + 1, tz + 1)):
            v.fill(px_, y + 1, pz_, px_, y + 11, pz_, 'spruce_log')
        v.fill(tx - 2, y + 10, tz - 2, tx + 2, y + 10, tz + 2, 'spruce_planks')
        v.fill(tx - 2, y + 11, tz - 2, tx + 2, y + 11, tz + 2, 'spruce_fence', outline=True)
        v.fill(tx - 2, y + 14, tz - 2, tx + 2, y + 14, tz + 2, 'dark_oak_slab')
        v.fill(tx, y + 1, tz, tx, y + 10, tz, 'ladder[facing=north]')
        v.fill(tx, y + 1, tz + 1, tx, y + 9, tz + 1, 'spruce_log')       # dos de l'échelle
        v.set(tx, y + 11, tz, AIR)                                         # sortie haute dégagée (AIR explicite : l'ancien feu de camp)
        v.set(tx, y + 12, tz, AIR)
        v.set(tx + 1, y + 11, tz + 1, 'campfire[lit=true]')                # remplace le haut du poteau d'angle (tx+1, tz+1)
    # grande hutte de Brennic (ouest)
    hx1, hz1, hx2, hz2 = x1 + 3, cz - 6, x1 + 13, cz + 6
    v.fill(hx1, y + 1, hz1, hx2, y + 5, hz2, 'spruce_planks', hollow=True)
    v.fill(hx1 + 1, y + 1, hz1 + 1, hx2 - 1, y + 5, hz2 - 1, AIR)
    v.gable_roof(hx1, hz1, hx2, hz2, y + 6, 'z', 'spruce_stairs', 'spruce_slab', 'spruce_planks')
    v.fill(hx2, y + 1, cz - 1, hx2, y + 3, cz + 1, AIR)
    v.set(hx1 + 1, y + 1, cz, 'chest[facing=east]')
    v.fill(hx1 + 1, y + 1, hz1 + 1, hx1 + 3, y + 1, hz1 + 1, 'barrel[facing=up]')
    v.set(hx1 + 2, y + 1, cz, 'dark_oak_stairs[facing=east]')
    v.set(hx1 + 2, y + 2, cz - 1, 'red_wall_banner[facing=east]') if False else None
    # tentes
    for (tx, tz, c) in ((cx + 6, z1 + 6, 'red'), (cx + 12, z1 + 6, 'brown'), (cx + 6, z2 - 7, 'green'), (cx + 12, z2 - 7, 'red')):
        for i in range(4):
            v.fill(tx - 2 + i, y + 1 + i, tz - 2, tx - 2 + i, y + 1 + i, tz + 2, f'{c}_wool')
            v.fill(tx + 3 - i, y + 1 + i, tz - 2, tx + 3 - i, y + 1 + i, tz + 2, f'{c}_wool')
        v.set(tx, y + 1, tz, f'{c}_bed[facing=north,part=foot]')
        v.set(tx, y + 1, tz - 1, f'{c}_bed[facing=north,part=head]')
    # feu de camp central, caisses
    v.set(cx, y + 1, cz, 'campfire[lit=true]')
    for (x, z) in ((cx + 3, cz + 3), (cx - 3, cz + 3), (cx + 3, cz - 3)):
        v.set(x, y + 1, z, 'spruce_log[axis=x]')
    for _ in range(14):
        x, z = r.randint(x1 + 3, x2 - 3), r.randint(z1 + 3, z2 - 3)
        if v.get(x, y + 1, z) in (None, AIR):
            v.set(x, y + 1, z, r.choice(['barrel[facing=up]', 'hay_block', 'composter', 'chest[facing=north]']))
    ARENAS['brennic'] = dict(c=(cx + 0.5, y + 1, cz + 0.5), r=18, home=(hx2 + 2.5, y + 1, cz + 0.5))
    spot('fort_gate', x2 + 4, y + 1, cz)
    LORE.append(('w', hx1 + 1, y + 1, cz + 3))
    return v
