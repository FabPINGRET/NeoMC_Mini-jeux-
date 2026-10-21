"""🏰 Ombrelune : régions du nord (Sylvanor, Givrecroc). Module importé par ol_structs.
"""
import math
import random

from tv_build import Vox, AIR
import ol_world as W
from ol_skit import ARENAS, LORE, cone_roof, round_tower, spiral_well, spot


# ================================================================ SYLVANOR
def giant_tree(v, cx, cz, y, h, r, plats, seed):
    rr = random.Random(seed)
    for yy in range(y - 2, y + h):
        rad = r + (2 if yy < y + 3 else 0) * (1 - (yy - y + 2) / 5) if yy < y + 3 else r * (1 - 0.25 * (yy - y) / h)
        for x in range(cx - r - 3, cx + r + 4):
            for z in range(cz - r - 3, cz + r + 4):
                d = math.hypot(x - cx, z - cz)
                if d <= rad + 0.3:
                    v.set(x, yy, z, 'jungle_wood' if d > rad - 1.2 else 'stripped_jungle_wood')
    # racines
    for a in range(0, 360, 45):
        for k in range(r, r + 7):
            x, z = round(cx + k * math.cos(math.radians(a))), round(cz + k * math.sin(math.radians(a)))
            yy = y + max(-1, 3 - (k - r))
            v.fill(x, y - 1, z, x, yy, z, 'jungle_wood')
    # couronne
    top = y + h
    for x in range(cx - 14, cx + 15):
        for z in range(cz - 14, cz + 15):
            for yy in range(top - 4, top + 6):
                d = math.hypot(x - cx, z - cz) + abs(yy - top) * 1.6
                if d < 13 - rr.random() * 2:
                    if v.get(x, yy, z) is None:
                        v.set(x, yy, z, 'azalea_leaves[persistent=true]' if rr.random() < 0.15 else 'jungle_leaves[persistent=true]')
    # plateformes circulaires + rambardes
    for py in plats:
        pr = r + 5
        for x in range(cx - pr, cx + pr + 1):
            for z in range(cz - pr, cz + pr + 1):
                d = math.hypot(x - cx, z - cz)
                if r + 0.5 < d <= pr:
                    v.set(x, py, z, 'birch_planks' if d < pr - 0.5 else 'stripped_birch_log[axis=y]')
                    if d > pr - 1:
                        v.set(x, py + 1, z, 'birch_fence')
        for a in range(0, 360, 60):
            x, z = round(cx + (r + 1) * math.cos(math.radians(a))), round(cz + (r + 1) * math.sin(math.radians(a)))
            v.set(x, py + 1, z, 'lantern')
    # escalier en colimaçon autour du tronc
    spiral_well(v, cx, cz, r + 2, y + 1, max(plats), 'birch_slab[type=top]', per_turn=24, keep=('jungle_wood', 'stripped_jungle_wood'))


def rope_bridge(v, a, b, y):
    (x1, z1), (x2, z2) = a, b
    n = max(1, round(max(abs(x2 - x1), abs(z2 - z1))))
    for i in range(n + 1):
        t = i / n
        x, z = round(x1 + (x2 - x1) * t), round(z1 + (z2 - z1) * t)
        sag = round(2 * math.sin(math.pi * t))
        yy = y - sag
        v.set(x, yy, z, 'bamboo_mosaic' if i % 2 else 'birch_planks')
        for k in (-1, 1):
            if abs(x2 - x1) > abs(z2 - z1):
                v.set(x, yy, z + k, 'birch_slab')
                v.set(x, yy + 1, z + k, 'birch_fence')
            else:
                v.set(x + k, yy, z, 'birch_slab')
                v.set(x + k, yy + 1, z, 'birch_fence')


def aelindor():
    cx, cz = W.P['aelindor']
    y = 68
    v = Vox(301)
    trees = [(cx, cz, 5, 44, (y + 10, y + 20, y + 32)), (cx - 15, cz + 12, 3, 34, (y + 10, y + 20)), (cx + 15, cz + 10, 3, 34, (y + 10, y + 20)),
             (cx + 2, cz - 16, 3, 32, (y + 10, y + 20))]
    for i, (tx, tz, rr, h, plats) in enumerate(trees):
        giant_tree(v, tx, tz, y + 1, h, rr, plats, 300 + i)
    for (tx, tz, rr, h, plats) in trees[1:]:
        rope_bridge(v, (cx + (tx - cx) * 0.35, cz + (tz - cz) * 0.35), (tx - (tx - cx) * 0.3, tz - (tz - cz) * 0.3), y + 10)
        rope_bridge(v, (cx + (tx - cx) * 0.35, cz + (tz - cz) * 0.35), (tx - (tx - cx) * 0.3, tz - (tz - cz) * 0.3), y + 20)
    # salle de la reine (plateforme haute de l'arbre central) : trône de bouleau, tapis
    py = y + 32
    v.fill(cx - 2, py + 1, cz - 9, cx + 2, py + 1, cz - 8, 'moss_carpet')
    v.set(cx, py + 1, cz - 9, 'birch_stairs[facing=south]')
    spot('elyndra', cx, py + 1, cz - 7)
    # la couronne d'un arbre voisin déborde sur la salle : on dégage le feuillage autour de la reine
    v.fill(cx - 10, py + 1, cz - 10, cx + 10, py + 3, cz + 10, AIR, only=('jungle_leaves[persistent=true]', 'azalea_leaves[persistent=true]'))
    spot('waystone_nw', cx + 4, y + 1, cz + 9)
    v.set(cx + 4, y + 1, cz + 9, 'lodestone')
    v.set(cx + 4, y + 2, cz + 9, 'amethyst_cluster[facing=up]')
    spot('elf_ground', cx - 8, y + 1, cz + 8)
    # maisons elfiques au sol (blanches, toits de feuilles)
    for (hx, hz) in ((cx - 18, cz - 8), (cx + 18, cz - 6), (cx - 6, cz + 18)):
        round_tower(v, hx, hz, y + 1, 3, 5, 'calcite', floor='birch_planks', windows='light_blue_stained_glass_pane')
        cone_roof(v, hx, hz, y + 6, 4, 'flowering_azalea_leaves[persistent=true]', 4, 'end_rod')
        v.fill(hx + 3, y + 1, hz, hx + 3, y + 2, hz, AIR)
    # fontaines de lumière
    for (fx, fz) in ((cx + 8, cz + 4), (cx - 8, cz - 2)):
        v.set(fx, y + 1, fz, 'chiseled_quartz_block')
        v.set(fx, y + 2, fz, 'pearlescent_froglight')
    LORE.append(('nw', cx + 6, py + 1, cz + 2))
    return v


def spider_lair():
    """Antre de la reine-araignée Ysh'tar : cratère tapissé de toiles, œufs, os."""
    x0, z0 = W.P['spider_lair']
    y = 72
    v = Vox(302)
    r = v.r
    for x in range(x0 - 18, x0 + 19):
        for z in range(z0 - 14, z0 + 15):
            d = math.hypot((x - x0) / 1.25, z - z0)
            if d <= 11:
                v.set(x, y - 1, z, 'moss_block' if r.random() < 0.6 else 'coarse_dirt')
                v.fill(x, y, z, x, y + 12, z, AIR)
                if r.random() < 0.06:
                    v.set(x, y, z, 'cobweb')
            elif d <= 14:
                hh = round(6 + (d - 11) * 2 + r.random() * 2)
                v.fill(x, y - 1, z, x, y + hh, z, 'mossy_cobblestone' if r.random() < 0.5 else 'stone')
    # toiles en voûte
    for _ in range(140):
        x, z = r.randint(x0 - 13, x0 + 13), r.randint(z0 - 10, z0 + 10)
        if math.hypot((x - x0) / 1.25, z - z0) < 11:
            v.set(x, y + r.randint(7, 12), z, 'cobweb')
    # cocons
    for _ in range(10):
        x, z = r.randint(x0 - 12, x0 + 12), r.randint(z0 - 9, z0 + 9)
        if math.hypot((x - x0) / 1.25, z - z0) < 10:
            v.fill(x, y, z, x, y + 1, z, 'white_wool')
            v.set(x, y + 2, z, 'cobweb')
    # entrée (côté est)
    v.fill(x0 + 11, y, z0 - 2, x0 + 18, y + 5, z0 + 2, AIR)
    v.fill(x0 + 11, y - 1, z0 - 2, x0 + 18, y - 1, z0 + 2, 'coarse_dirt')
    ARENAS['ystar'] = dict(c=(x0 + 0.5, y, z0 + 0.5), r=13)
    return v


def shrine():
    x0, z0 = W.P['shrine_nw']
    y = 69
    v = Vox(303)
    for a in range(0, 360, 30):
        x, z = round(x0 + 7 * math.cos(math.radians(a))), round(z0 + 7 * math.sin(math.radians(a)))
        hgt = v.r.randint(2, 6)
        v.fill(x, y + 1, z, x, y + hgt, z, 'mossy_stone_bricks' if v.r.random() < 0.5 else 'quartz_pillar')
    for x in range(x0 - 4, x0 + 5):
        for z in range(z0 - 4, z0 + 5):
            if math.hypot(x - x0, z - z0) <= 4.5:
                v.set(x, y, z, 'mossy_stone_bricks' if (x + z) % 3 else 'chiseled_stone_bricks')
    v.set(x0, y + 1, z0, 'lectern[facing=south]')
    LORE.append(('nw', x0, y + 1, z0 + 1))
    return v


# ================================================================ GIVRECROC
def longhouse(v, x1, z1, L, wdt, y, axis, r):
    """Longue maison nordique (rondins, toit très pentu)."""
    if axis == 'x':
        x2, z2 = x1 + L - 1, z1 + wdt - 1
    else:
        x2, z2 = x1 + wdt - 1, z1 + L - 1
    v.fill(x1, y, z1, x2, y, z2, 'spruce_planks')
    v.walls(x1, z1, x2, z2, y + 1, y + 3, 'stripped_spruce_log[axis=y]')
    v.fill(x1 + 1, y + 1, z1 + 1, x2 - 1, y + 3, z2 - 1, AIR)
    v.gable_roof(x1, z1, x2, z2, y + 4, axis, 'dark_oak_stairs', 'dark_oak_slab', 'spruce_planks', overhang=1)
    if axis == 'x':
        v.fill(x1, y + 1, (z1 + z2) // 2, x1, y + 2, (z1 + z2) // 2, AIR)
        v.set(x1 - 1, y + 4, (z1 + z2) // 2 - 1, 'skeleton_skull') if False else None
        v.set((x1 + x2) // 2, y + 1, (z1 + z2) // 2, 'campfire[lit=true]')
    else:
        v.fill((x1 + x2) // 2, y + 1, z1, (x1 + x2) // 2, y + 2, z1, AIR)
        v.set((x1 + x2) // 2, y + 1, (z1 + z2) // 2, 'campfire[lit=true]')
    for k in range(2):
        v.bed(x1 + 1 + k * 2, y + 1, z2 - 2, 'north', 'white')
    v.set(x2 - 1, y + 1, z1 + 1, 'barrel[facing=up]')


def hrafnheim():
    cx, cz = W.P['hrafnheim']
    y = 74
    v = Vox(401)
    r = v.r
    for x in range(cx - 22, cx + 23):
        for z in range(cz - 18, cz + 19):
            if r.random() < 0.15:
                v.set(x, y, z, 'snow_block')
    # palissade
    for x in range(cx - 21, cx + 22):
        for z in range(cz - 17, cz + 18):
            if x in (cx - 21, cx + 21) or z in (cz - 17, cz + 17):
                if abs(x - cx) <= 2 or abs(z - cz) <= 2:
                    continue
                v.fill(x, y - 1, z, x, y + 5 + (1 if (x + z) % 2 else 0), z, 'spruce_log')
    # grande halle du jarl (nord)
    longhouse(v, cx - 8, cz - 15, 17, 9, y, 'x', r)
    for x in (cx - 6, cx + 6):
        v.set(x, y + 4, cz - 10, 'white_wall_banner[facing=south]') if False else None
    spot('bjorn', cx, y + 1, cz - 13)            # derrière le feu de camp de la halle (cz - 11)
    for (hx, hz, ax) in ((cx - 18, cz - 4, 'z'), (cx + 12, cz - 4, 'z'), (cx - 18, cz + 6, 'z'), (cx + 12, cz + 6, 'z')):
        longhouse(v, hx, hz, 9, 6, y, ax, r)
    # braseros
    for (bx, bz) in ((cx - 4, cz + 2), (cx + 4, cz + 2), (cx, cz + 10)):
        v.set(bx, y + 1, bz, 'cobblestone_wall')
        v.set(bx, y + 2, bz, 'campfire[lit=true]')
    spot('waystone_n', cx + 3, y + 1, cz + 6)
    v.set(cx + 3, y + 1, cz + 6, 'lodestone')
    v.set(cx + 3, y + 2, cz + 6, 'amethyst_cluster[facing=up]')
    spot('furrier', cx - 6, y + 1, cz + 8)
    LORE.append(('n', cx - 15, y + 1, cz - 2))
    return v


def giant_hold():
    """Forteresse de glace du géant Hrimgar (sur un plateau) : enceinte, colonnes, trône, arène."""
    x0, z0 = W.P['giant_hold']
    y = 104
    v = Vox(402)
    r = v.r
    ice = lambda x, yy, z: 'packed_ice' if r.random() < 0.7 else ('blue_ice' if r.random() < 0.6 else 'snow_block')
    R = 16
    for x in range(x0 - R - 2, x0 + R + 3):
        for z in range(z0 - R - 2, z0 + R + 3):
            d = math.hypot(x - x0, z - z0)
            if d <= R:
                v.set(x, y, z, 'packed_ice' if (x + z) % 2 else 'snow_block')
                v.fill(x, y + 1, z, x, y + 16, z, AIR)
            elif d <= R + 1.5:
                hh = 10 + (3 if (round(math.degrees(math.atan2(z - z0, x - x0))) // 15) % 2 else 0)
                v.fill(x, y - 3, z, x, y + hh, z, ice)
    for a in range(0, 360, 30):
        x, z = round(x0 + (R - 3) * math.cos(math.radians(a))), round(z0 + (R - 3) * math.sin(math.radians(a)))
        v.fill(x, y + 1, z, x, y + 9 + r.randint(0, 4), z, 'blue_ice')
    # trône (nord)
    v.fill(x0 - 3, y + 1, z0 - R + 2, x0 + 3, y + 2, z0 - R + 3, 'packed_ice')
    v.fill(x0 - 1, y + 3, z0 - R + 2, x0 + 1, y + 8, z0 - R + 2, 'blue_ice')
    # entrée (sud), escalier de neige
    v.fill(x0 - 2, y + 1, z0 + R - 1, x0 + 2, y + 6, z0 + R + 2, AIR)
    ARENAS['hrimgar'] = dict(c=(x0 + 0.5, y + 1, z0 + 0.5), r=R - 1)
    LORE.append(('n', x0 + 2, y + 1, z0 - R + 4))
    return v
