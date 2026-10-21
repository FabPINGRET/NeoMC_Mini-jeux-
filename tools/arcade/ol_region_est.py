"""🏰 Ombrelune : régions de l'est (Fangebrume, Azhar, Pyrecendre). Module importé par ol_structs.
"""
import math

from tv_build import Vox, AIR
import ol_access as A
import ol_world as W
from ol_skit import ARENAS, LORE, SPOTS, brace_ladders, cone_roof, crenels, round_tower, spot


# ================================================================ FANGEBRUME
def stilt_village():
    cx, cz = W.P['stilts']
    y = 63
    v = Vox(501)
    r = v.r
    deck = y + 4
    huts = []
    for i in range(8):
        a = i * 2 * math.pi / 8 + 0.3
        hx, hz = round(cx + 14 * math.cos(a)), round(cz + 12 * math.sin(a))
        huts.append((hx, hz))
        v.fill(hx - 3, y - 3, hz - 3, hx - 3, deck, hz - 3, 'mangrove_log')
        v.fill(hx + 3, y - 3, hz - 3, hx + 3, deck, hz - 3, 'mangrove_log')
        v.fill(hx - 3, y - 3, hz + 3, hx - 3, deck, hz + 3, 'mangrove_log')
        v.fill(hx + 3, y - 3, hz + 3, hx + 3, deck, hz + 3, 'mangrove_log')
        v.fill(hx - 3, deck, hz - 3, hx + 3, deck, hz + 3, 'mangrove_planks')
        v.fill(hx - 2, deck + 1, hz - 2, hx + 2, deck + 3, hz + 2, 'mud_bricks', hollow=True)
        v.fill(hx - 1, deck + 1, hz - 1, hx + 1, deck + 3, hz + 1, AIR)
        v.gable_roof(hx - 2, hz - 2, hx + 2, hz + 2, deck + 4, 'x', 'mangrove_stairs', 'mangrove_slab', 'mangrove_planks')
        ddx, ddz = (cx - hx), (cz - hz)
        if abs(ddx) > abs(ddz):
            ex = hx + (2 if ddx > 0 else -2)
            v.fill(ex, deck + 1, hz, ex, deck + 2, hz, AIR)
        else:
            ez = hz + (2 if ddz > 0 else -2)
            v.fill(hx, deck + 1, ez, hx, deck + 2, ez, AIR)
        v.set(hx, deck + 3, hz, 'lantern[hanging=true]')
    # passerelles vers la plateforme centrale
    v.fill(cx - 5, deck, cz - 5, cx + 5, deck, cz + 5, 'mangrove_planks')
    v.fill(cx - 5, deck + 1, cz - 5, cx + 5, deck + 1, cz + 5, 'mangrove_fence', outline=True)
    for (x, z) in ((cx - 5, cz - 5), (cx + 5, cz - 5), (cx - 5, cz + 5), (cx + 5, cz + 5)):
        v.fill(x, y - 3, z, x, deck - 1, z, 'mangrove_log')
    for (hx, hz) in huts:
        n = max(abs(hx - cx), abs(hz - cz))
        for i in range(n):
            x, z = round(cx + (hx - cx) * i / n), round(cz + (hz - cz) * i / n)
            if v.get(x, deck, z) is None:
                v.set(x, deck, z, 'mangrove_slab[type=top]')
    for (x, z) in ((cx, cz - 5), (cx, cz + 5), (cx - 5, cz), (cx + 5, cz)):
        v.set(x, deck + 1, z, AIR)
    # échelle d'accès (côté ouest)
    v.fill(cx - 6, y, cz, cx - 6, deck, cz, 'ladder[facing=west]')
    v.fill(cx - 7, y - 1, cz - 1, cx - 7, y, cz + 1, 'mangrove_planks')
    v.set(cx, deck + 1, cz, 'cauldron')
    spot('maelle', cx + 2, deck + 1, cz + 2)
    spot('waystone_ne', cx - 2, deck + 1, cz - 2)
    v.set(cx - 2, deck + 1, cz - 2, 'lodestone')
    v.set(cx - 2, deck + 2, cz - 2, 'amethyst_cluster[facing=up]')
    spot('herbalist', cx - 3, deck + 1, cz + 3)
    LORE.append(('ne', huts[3][0], deck + 1, huts[3][1]))
    brace_ladders(v, 'mangrove_log')
    return v


def witch_isle():
    x0, z0 = W.P['witch_isle']
    y = 64
    v = Vox(502)
    r = v.r
    # tour tordue
    for i, yy in enumerate(range(y + 1, y + 26)):
        ox = round(1.5 * math.sin(i / 5))
        oz = round(1.5 * math.cos(i / 7))
        rr = 4 if i < 18 else 3
        for x in range(x0 - rr - 2, x0 + rr + 3):
            for z in range(z0 - rr - 2, z0 + rr + 3):
                d = math.hypot(x - x0 - ox, z - z0 - oz)
                if d <= rr + 0.4:
                    v.set(x, yy, z, ('dark_oak_planks' if r.random() < 0.6 else 'mangrove_planks') if d > rr - 0.7 else AIR)
    cone_roof(v, x0 + round(1.5 * math.sin(25 / 5)), z0 + round(1.5 * math.cos(25 / 7)), y + 26, 5, 'purple_terracotta', 9, 'end_rod')
    v.fill(x0 - 1, y + 1, z0 + 3, x0 + 1, y + 3, z0 + 5, AIR)
    for (x, z) in ((x0 - 2, z0 - 1), (x0 + 2, z0 - 1)):
        v.set(x, y + 1, z, 'cauldron')
    # plancher et arène autour de la tour (sur l'île)
    for x in range(x0 - 10, x0 + 11):
        for z in range(z0 - 10, z0 + 11):
            d = math.hypot(x - x0, z - z0)
            if 5 < d <= 10:
                v.set(x, y, z, 'mud' if r.random() < 0.5 else 'moss_block')
    ARENAS['morvaine'] = dict(c=(x0 + 0.5, y + 1, z0 + 7.5), r=12)
    # totems (3) sur la rive
    tot = []
    for a in (200, 300, 60):
        x, z = round(x0 + 24 * math.cos(math.radians(a))), round(z0 + 24 * math.sin(math.radians(a)))
        gy = W.ground(x, z) if (x, z) in W.H else y
        v.fill(x, gy, z, x, gy + 3, z, 'stripped_dark_oak_log')
        v.set(x, gy + 4, z, 'carved_pumpkin[facing=south]')
        v.set(x, gy + 5, z, 'soul_lantern')
        tot.append((x + 0.5, gy, z + 0.5))
    SPOTS['totems'] = tot
    # ponton (passerelle depuis la rive sud) : tablier à y - 1, pour qu'on puisse y monter depuis l'eau ou la rive (à y, c'était un mur de 2 blocs)
    v.fill(x0 - 1, y, z0 + 10, x0 + 1, y, z0 + 29, AIR, keep=True)        # libère l'ancien niveau, sans toucher à l'anneau de l'île
    zend = next((z for z in range(z0 + 11, z0 + 45) if W.H[(x0, z)] >= W.WATER), None)      # jusqu'à la rive sud
    assert zend is not None, f"ponton : aucune rive au sud de l'île (x {x0}, z {z0 + 11}..{z0 + 44})"
    for z in range(z0 + 11, zend + 1):
        v.set(x0, y - 1, z, 'mangrove_planks')
        v.set(x0 - 1, y - 1, z, 'mangrove_slab[type=top]')
        v.set(x0 + 1, y - 1, z, 'mangrove_slab[type=top]')
    for z in range(z0 + 10, zend + 1):
        if z % 4 == 0:
            v.fill(x0 + 2, y - 4, z, x0 + 2, y + 1, z, 'mangrove_log')
            v.set(x0 + 2, y + 2, z, 'soul_lantern')
    LORE.append(('ne', x0 - 1, y + 1, z0 + 1))
    return v


# ================================================================ AZHAR
def oasis_town():
    cx, cz = W.P['oasis']
    y = 64
    v = Vox(601)
    r = v.r
    for (hx, hz, w_, d_, h_) in ((cx - 16, cz - 14, 8, 7, 5), (cx - 6, cz - 14, 7, 7, 4), (cx - 16, cz + 6, 9, 8, 6), (cx - 5, cz + 8, 7, 7, 4),
                                 (cx + 2, cz - 15, 8, 6, 5), (cx - 17, cz - 4, 6, 7, 4)):
        v.fill(hx, y, hz, hx + w_ - 1, y, hz + d_ - 1, 'smooth_sandstone')
        v.fill(hx, y + 1, hz, hx + w_ - 1, y + h_, hz + d_ - 1, 'sandstone', hollow=True)
        v.fill(hx + 1, y + 1, hz + 1, hx + w_ - 2, y + h_, hz + d_ - 2, AIR)
        v.fill(hx, y + h_ + 1, hz, hx + w_ - 1, y + h_ + 1, hz + d_ - 1, 'smooth_sandstone_slab')
        v.fill(hx, y + h_ + 2, hz, hx + w_ - 1, y + h_ + 2, hz + d_ - 1, 'sandstone_wall', outline=True)
        v.fill(hx + w_ // 2, y + 1, hz + d_ - 1, hx + w_ // 2, y + 2, hz + d_ - 1, AIR)
        for x in range(hx + 2, hx + w_ - 1, 3):
            v.set(x, y + 3, hz, 'orange_stained_glass_pane')
        v.set(hx + 1, y + 1, hz + 1, 'decorated_pot')
        v.set(hx + w_ - 2, y + 1, hz + 1, 'barrel[facing=up]')
        v.set(hx + w_ // 2, y + h_, hz + d_ // 2, 'lantern[hanging=true]')
    # dôme du marchand (centre)
    for x in range(cx - 5, cx + 6):
        for z in range(cz - 5, cz + 6):
            for yy in range(y + 1, y + 12):
                d = math.hypot(x - cx, z - cz, (yy - y - 6) * 1.1) if False else math.sqrt((x - cx) ** 2 + (z - cz) ** 2 + max(0, yy - y - 6) ** 2 * 1.2)
                if yy <= y + 6:
                    if math.hypot(x - cx, z - cz) <= 5 and math.hypot(x - cx, z - cz) > 4:
                        v.set(x, yy, z, 'cut_sandstone')
                elif 4 < d <= 5.2:
                    v.set(x, yy, z, 'cyan_terracotta' if (yy - y) % 2 else 'white_terracotta')
    v.fill(cx - 1, y + 1, cz + 4, cx + 1, y + 3, cz + 5, AIR)
    v.set(cx, y + 1, cz, 'cartography_table')
    spot('kassim', cx + 2, y + 1, cz + 1)
    # tentes du bazar
    for i, (tx, tz) in enumerate(((cx + 5, cz + 10), (cx + 10, cz + 12), (cx - 2, cz + 16))):
        c = ['red', 'orange', 'blue'][i]
        v.fill(tx - 2, y + 3, tz - 2, tx + 2, y + 3, tz + 2, f'{c}_wool')
        for (x, z) in ((tx - 2, tz - 2), (tx + 2, tz - 2), (tx - 2, tz + 2), (tx + 2, tz + 2)):
            v.fill(x, y + 1, z, x, y + 2, z, 'birch_fence')
        v.set(tx, y + 1, tz, r.choice(['barrel[facing=up]', 'decorated_pot', 'hay_block']))
    spot('waystone_e', cx + 6, y + 1, cz - 4)
    v.set(cx + 6, y + 1, cz - 4, 'lodestone')
    v.set(cx + 6, y + 2, cz - 4, 'amethyst_cluster[facing=up]')
    spot('sandmerchant', cx + 5, y + 1, cz + 9)
    return v


def pyramid():
    """Pyramide de Sethkar : 4 côtés en gradins, entrée nord, couloir, salle des scarabées (3 socles), chambre funéraire (arène)."""
    x0, z0 = W.P['pyramid']
    y = 64
    v = Vox(602)
    r = v.r
    B = 24
    for i in range(B):
        yy = y + 1 + i
        hb = B - i
        for x in range(x0 - hb, x0 + hb + 1):
            for z in range(z0 - hb, z0 + hb + 1):
                if max(abs(x - x0), abs(z - z0)) >= hb - 1:
                    v.set(x, yy, z, 'smooth_sandstone' if r.random() < 0.7 else ('cut_sandstone' if r.random() < 0.7 else 'chiseled_sandstone'))
                else:
                    v.set(x, yy, z, 'sandstone')
    v.set(x0, y + B + 1, z0, 'gold_block')
    # salle intérieure (chambre funéraire) : 21 × 21 × 9
    v.fill(x0 - 10, y + 1, z0 - 10, x0 + 10, y + 9, z0 + 10, AIR)
    v.fill(x0 - 10, y, z0 - 10, x0 + 10, y, z0 + 10, 'smooth_sandstone')
    for x in range(x0 - 10, x0 + 11):
        for z in range(z0 - 10, z0 + 11):
            if (x + z) % 6 == 0:
                v.set(x, y, z, 'orange_terracotta' if (x - z) % 4 else 'blue_terracotta')
    for (px_, pz_) in ((x0 - 6, z0 - 6), (x0 + 6, z0 - 6), (x0 - 6, z0 + 6), (x0 + 6, z0 + 6)):
        v.fill(px_, y + 1, pz_, px_, y + 9, pz_, 'chiseled_red_sandstone')
        v.set(px_ + (1 if px_ < x0 else -1), y + 6, pz_, 'lantern[hanging=false]')
    v.fill(x0 - 2, y + 1, z0 + 6, x0 + 2, y + 1, z0 + 8, 'gold_block')
    v.fill(x0 - 1, y + 2, z0 + 7, x0 + 1, y + 2, z0 + 7, 'chiseled_sandstone')
    ARENAS['sethkar'] = dict(c=(x0 + 0.5, y + 1, z0 + 0.5), r=10)
    # couloir d'entrée (nord) et salle des scarabées
    v.fill(x0 - 1, y + 1, z0 - B, x0 + 1, y + 4, z0 - 11, AIR)
    v.fill(x0 - 1, y, z0 - B, x0 + 1, y, z0 - 11, 'cut_sandstone')
    v.fill(x0 - 6, y + 1, z0 - 18, x0 + 6, y + 6, z0 - 13, AIR)
    v.fill(x0 - 6, y, z0 - 18, x0 + 6, y, z0 - 13, 'smooth_sandstone')
    sock = []
    for i, x in enumerate((x0 - 4, x0, x0 + 4)):
        v.set(x, y + 1, z0 - 17, 'chiseled_sandstone')
        v.set(x, y + 2, z0 - 17, 'decorated_pot')
        sock.append((x + 0.5, y + 1, z0 - 15.5))
    SPOTS['scarab_sockets'] = sock
    SPOTS['pyr_door'] = (x0, y + 1, z0 - 11)        # porte scellée (sable) vers la chambre
    v.fill(x0 - 1, y + 1, z0 - 11, x0 + 1, y + 3, z0 - 11, 'chiseled_sandstone')
    for z in range(z0 - B + 2, z0 - 11, 3):
        v.set(x0 - 1, y + 3, z, 'lantern[hanging=false]') if False else v.set(x0 - 2, y + 3, z, 'lantern') if False else None
    spot('pyr_entry', x0, y + 1, z0 - B - 2)
    LORE.append(('e', x0 + 5, y + 1, z0 - 14))
    return v


def obelisks():
    x0, z0 = W.P['obelisks']
    y = W.ground(x0, z0) - 1
    v = Vox(603)
    for (dx, dz) in ((-6, 0), (6, 0), (0, -6), (0, 6)):
        x, z = x0 + dx, z0 + dz
        gy = W.ground(x, z) - 1
        v.fill(x - 1, gy - 2, z - 1, x + 1, gy + 1, z + 1, 'cut_sandstone')
        v.fill(x, gy + 2, z, x, gy + 12, z, 'chiseled_sandstone')
        v.set(x, gy + 13, z, 'gold_block')
    LORE.append(('e', x0, W.ground(x0, z0), z0))
    return v


# ================================================================ PYRECENDRE
def bastion():
    cx, cz = W.P['bastion']
    y = 66
    v = Vox(701)
    r = v.r
    wl = lambda x, yy, z: 'polished_blackstone_bricks' if r.random() < 0.75 else 'cracked_polished_blackstone_bricks'
    x1, z1, x2, z2 = cx - 14, cz - 14, cx + 14, cz + 14
    v.fill(x1, y, z1, x2, y, z2, 'polished_blackstone')
    v.walls(x1, z1, x2, z2, y + 1, y + 7, wl)
    crenels(v, x1, z1, x2, z1, y + 8, 'polished_blackstone_bricks')
    crenels(v, x1, z2, x2, z2, y + 8, 'polished_blackstone_bricks')
    crenels(v, x1, z1, x1, z2, y + 8, 'polished_blackstone_bricks')
    crenels(v, x2, z1, x2, z2, y + 8, 'polished_blackstone_bricks')
    for (gx, gz, ax) in ((cx, z1, 'x'), (x1, cz, 'z'), (x2, cz, 'z'), (cx, z2, 'x')):
        if ax == 'x':
            v.fill(gx - 2, y + 1, gz, gx + 2, y + 5, gz, AIR)
        else:
            v.fill(gx, y + 1, gz - 2, gx, y + 5, gz + 2, AIR)
    for (tx, tz) in ((x1, z1), (x2, z1), (x1, z2), (x2, z2)):
        round_tower(v, tx, tz, y + 1, 3, 12, wl, floor='polished_blackstone', crenel='polished_blackstone_bricks')
        v.set(tx, y + 12, tz, 'campfire[lit=true]')
    # forge naine, salle commune
    v.fill(cx - 8, y + 1, cz - 10, cx + 8, y + 5, cz - 4, 'stone_bricks', hollow=True)
    v.fill(cx - 7, y + 1, cz - 9, cx + 7, y + 5, cz - 5, AIR)
    v.fill(cx - 8, y + 6, cz - 10, cx + 8, y + 6, cz - 4, 'polished_blackstone_slab')
    v.fill(cx - 1, y + 1, cz - 4, cx + 1, y + 3, cz - 4, AIR)
    v.set(cx - 5, y + 1, cz - 8, 'anvil[facing=east]')
    v.set(cx + 5, y + 1, cz - 8, 'blast_furnace[facing=south]')
    v.fill(cx - 2, y + 1, cz - 9, cx + 2, y + 1, cz - 9, 'lava')
    v.fill(cx - 2, y + 2, cz - 9, cx + 2, y + 2, cz - 9, 'iron_bars')
    spot('durgan', cx, y + 1, cz - 6)
    spot('waystone_se', cx + 4, y + 1, cz + 4)
    v.set(cx + 4, y + 1, cz + 4, 'lodestone')
    v.set(cx + 4, y + 2, cz + 4, 'amethyst_cluster[facing=up]')
    for (x, z) in ((cx - 6, cz + 6), (cx + 8, cz + 8), (cx - 9, cz - 1)):
        v.set(x, y + 1, z, 'magma_block')
        v.set(x, y + 2, z, 'campfire[lit=true]')
    LORE.append(('se', cx - 6, y + 1, cz - 8))
    return v


def caldera():
    """Nid d'Ignarok dans la caldeira : ossements, œufs de dragon, colonnes d'obsidienne, mares de lave."""
    x0, z0 = W.VX, W.VZ
    y = W.CALD_Y
    v = Vox(702)
    r = v.r
    for x in range(x0 - 16, x0 + 17):
        for z in range(z0 - 16, z0 + 17):
            d = math.hypot(x - x0, z - z0)
            if d <= 15.5:
                v.set(x, y, z, 'blackstone' if r.random() < 0.6 else ('basalt' if r.random() < 0.6 else 'magma_block'))
                v.fill(x, y + 1, z, x, y + 22, z, AIR)
                if 12.5 < d and r.random() < 0.25 and not A.in_breach(x, z, (x0, z0)):   # pas de lave dans la brèche
                    v.set(x, y, z, 'lava')
    for a in range(15, 360, 45):
        x, z = round(x0 + 12 * math.cos(math.radians(a))), round(z0 + 12 * math.sin(math.radians(a)))
        v.fill(x, y + 1, z, x, y + 6 + r.randint(0, 6), z, 'obsidian' if r.random() < 0.7 else 'crying_obsidian')
    # cage thoracique géante
    for k in range(-6, 7, 3):
        for i in range(10):
            a = math.pi * i / 9
            x, yy = x0 + k, y + round(7 * math.sin(a))
            z = z0 - 4 + round(5 * math.cos(a))
            v.set(x, yy, z, 'bone_block')
    v.fill(x0 - 7, y + 1, z0 - 4, x0 + 7, y + 1, z0 - 4, 'bone_block[axis=x]')
    for (x, z) in ((x0 + 6, z0 + 6), (x0 + 7, z0 + 5), (x0 + 5, z0 + 7)):
        v.set(x, y + 1, z, 'dragon_egg') if False else v.set(x, y + 1, z, 'sniffer_egg')
    ARENAS['ignarok'] = dict(c=(x0 + 0.5, y + 1, z0 + 0.5), r=14)
    spot('cald_in', *A.breach_pt((x0, z0), y + 1))   # bout de la rampe : objectif de la quête « gravis le volcan »
    LORE.append(('se', x0 - 10, y + 1, z0 + 8))
    return v
