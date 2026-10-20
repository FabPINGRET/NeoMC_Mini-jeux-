"""🏰 Ombrelune : régions du sud (Khazgarde, Terres d'ombre, chapelle).
La chapelle (région w, entrée de donjon) reste ici : bloc contigu d'origine. Module importé par ol_structs.
"""
import math

from tv_build import Vox, AIR
import ol_world as W
from ol_skit import ARENAS, LORE, SPOTS, crenels, round_tower, spot


# ================================================================ KHAZGARDE
def dwarf_camp():
    cx, cz = W.P['dwarf_camp']
    y = 66
    v = Vox(801)
    r = v.r
    for i, (tx, tz) in enumerate(((cx - 12, cz - 6), (cx + 12, cz - 6), (cx - 12, cz + 6), (cx + 12, cz + 6), (cx, cz - 10))):
        c = ['gray', 'brown', 'light_gray', 'brown', 'blue'][i]
        for k in range(4):
            v.fill(tx - 3 + k, y + 1 + k, tz - 2, tx - 3 + k, y + 1 + k, tz + 2, f'{c}_wool')
            v.fill(tx + 3 - k, y + 1 + k, tz - 2, tx + 3 - k, y + 1 + k, tz + 2, f'{c}_wool')
        v.set(tx, y + 1, tz, 'barrel[facing=up]')
    v.set(cx, y + 1, cz, 'campfire[lit=true]')
    v.set(cx + 4, y + 1, cz + 2, 'anvil[facing=north]')
    v.set(cx + 5, y + 1, cz + 2, 'smithing_table')
    spot('thrain', cx - 2, y + 1, cz - 4)
    spot('waystone_s', cx + 3, y + 1, cz - 3)
    v.set(cx + 3, y + 1, cz - 3, 'lodestone')
    v.set(cx + 3, y + 2, cz - 3, 'amethyst_cluster[facing=up]')
    LORE.append(('s', cx + 12, y + 1, cz + 8))
    return v


def dwarf_gate():
    """Porte de Khazgarde taillée dans la falaise (z ≈ 140) + grande salle creusée dans la montagne (arène du Colosse)."""
    x0, zf = W.P['kgate']
    y = 66
    v = Vox(802)
    r = v.r
    deep = lambda x, yy, z: 'deepslate_bricks' if r.random() < 0.7 else ('deepslate_tiles' if r.random() < 0.5 else 'cracked_deepslate_bricks')
    # parvis
    v.fill(x0 - 14, y, zf - 10, x0 + 14, y, zf - 1, 'polished_deepslate')
    for z in range(zf - 10, zf):
        for x in (x0 - 14, x0 + 14):
            v.set(x, y + 1, z, 'deepslate_brick_wall')
    # façade : cadre de la porte, statues
    v.fill(x0 - 12, y, zf, x0 + 12, y + 30, zf + 1, deep)
    v.fill(x0 - 5, y + 1, zf, x0 + 5, y + 14, zf + 1, AIR)
    for yy in range(y + 15, y + 19):
        hw = 5 - (yy - y - 15)
        v.fill(x0 - hw, yy, zf, x0 + hw, yy, zf + 1, AIR)
    v.fill(x0 - 6, y + 1, zf - 1, x0 - 6, y + 16, zf - 1, 'polished_deepslate')
    v.fill(x0 + 6, y + 1, zf - 1, x0 + 6, y + 16, zf - 1, 'polished_deepslate')
    v.fill(x0 - 6, y + 17, zf - 1, x0 + 6, y + 17, zf - 1, 'chiseled_deepslate')
    # portes de pierre (fermées tant que les runes ne sont pas activées) : bloc témoin
    SPOTS['kgate_door'] = (x0 - 4, y + 1, zf, x0 + 4, y + 13, zf + 1)
    for sx in (-9, 9):
        x = x0 + sx
        v.fill(x - 1, y + 1, zf - 2, x + 1, y + 3, zf - 1, 'polished_deepslate')
        v.fill(x, y + 4, zf - 2, x, y + 14, zf - 2, 'chiseled_deepslate')
        v.fill(x - 1, y + 10, zf - 2, x + 1, y + 11, zf - 2, 'deepslate_tiles')
        v.set(x, y + 15, zf - 2, 'gold_block')
        v.set(x, y + 16, zf - 2, 'lightning_rod')
    # pierres runiques (4) sur le parvis
    runes = []
    for i, x in enumerate((x0 - 10, x0 - 4, x0 + 4, x0 + 10)):
        z = zf - 7
        v.set(x, y + 1, z, 'chiseled_tuff_bricks')
        v.set(x, y + 2, z, 'chiseled_tuff')
        runes.append((x + 0.5, y + 1, z + 0.5))
    SPOTS['runes'] = runes
    # grande salle creusée
    hz1, hz2 = zf + 2, zf + 64
    for z in range(hz1, hz2 + 1):
        for x in range(x0 - 16, x0 + 17):
            v.fill(x, y + 1, z, x, y + 22, z, AIR)
            v.set(x, y, z, 'polished_deepslate' if (x + z) % 2 else 'deepslate_tiles')
        for x in (x0 - 17, x0 + 17):
            v.fill(x, y - 1, z, x, y + 23, z, deep)
        v.fill(x0 - 17, y + 23, z, x0 + 17, y + 23, z, deep)
    v.fill(x0 - 17, y - 1, hz2 + 1, x0 + 17, y + 23, hz2 + 1, deep)
    v.fill(x0 - 17, y - 1, hz1 - 1, x0 - 6, y + 23, hz1 - 1, deep)
    v.fill(x0 + 6, y - 1, hz1 - 1, x0 + 17, y + 23, hz1 - 1, deep)
    for z in range(hz1 + 4, hz2 - 2, 8):
        for x in (x0 - 10, x0 + 10):
            v.fill(x - 1, y + 1, z - 1, x + 1, y + 22, z + 1, 'polished_deepslate')
            v.fill(x - 2, y + 18, z - 2, x + 2, y + 18, z + 2, 'chiseled_deepslate')
            v.set(x + 2, y + 8, z, 'lantern[hanging=false]') if False else None
            v.set(x, y + 8, z - 2, 'lantern') if False else None
        v.fill(x0 - 15, y, z, x0 - 13, y, z + 2, 'lava')
        v.fill(x0 + 13, y, z, x0 + 15, y, z + 2, 'lava')
    for z in range(hz1 + 2, hz2, 6):
        v.lamp(x0, y + 20, z, kind='lantern')
        v.set(x0, y + 21, z, 'iron_chain')
        v.set(x0, y + 22, z, 'iron_chain')
    # trône du roi (fond) et arène du Colosse
    v.fill(x0 - 4, y + 1, hz2 - 3, x0 + 4, y + 2, hz2, 'polished_deepslate')
    v.fill(x0 - 1, y + 3, hz2 - 1, x0 + 1, y + 6, hz2 - 1, 'gold_block')
    v.set(x0, y + 3, hz2 - 2, 'deepslate_brick_stairs[facing=north]')
    ARENAS['colosse'] = dict(c=(x0 + 0.5, y + 1, hz2 - 16 + 0.5), r=16)
    # piliers runiques du Colosse (4) : leviers
    lev = []
    for (dx, dz) in ((-12, -24), (12, -24), (-12, -6), (12, -6)):
        x, z = x0 + dx, hz2 + dz
        v.fill(x, y + 1, z, x, y + 4, z, 'chiseled_tuff_bricks')
        v.set(x, y + 5, z, 'light_blue_stained_glass')
        lev.append((x + 0.5, y + 1, z + 0.5))
    SPOTS['colosse_pillars'] = lev
    LORE.append(('s', x0 + 14, y + 1, hz1 + 3))
    spot('kgate_in', x0, y + 1, hz1 + 4)
    return v


# ================================================================ TERRES D'OMBRE
def rebel_camp():
    cx, cz = W.P['rebels']
    y = 64
    v = Vox(901)
    r = v.r
    for x in range(cx - 14, cx + 15):
        for z in range(cz - 14, cz + 15):
            d = max(abs(x - cx), abs(z - cz))
            if d == 14 and (abs(x - cx) > 2 and abs(z - cz) > 2):
                v.fill(x, y + 1, z, x, y + 2, z, 'spruce_fence' if r.random() < 0.6 else 'dark_oak_fence')
    for i, (tx, tz) in enumerate(((cx - 8, cz - 8), (cx + 8, cz - 8), (cx - 8, cz + 8), (cx + 8, cz + 8))):
        c = ['red', 'blue', 'white', 'yellow'][i]
        for k in range(4):
            v.fill(tx - 3 + k, y + 1 + k, tz - 2, tx - 3 + k, y + 1 + k, tz + 2, f'{c}_wool')
            v.fill(tx + 3 - k, y + 1 + k, tz - 2, tx + 3 - k, y + 1 + k, tz + 2, f'{c}_wool')
    v.set(cx, y + 1, cz, 'soul_campfire[lit=true]')
    v.fill(cx - 2, y + 1, cz + 3, cx + 2, y + 1, cz + 3, 'spruce_planks')
    v.set(cx, y + 2, cz + 3, 'cartography_table') if False else v.set(cx, y + 1, cz + 4, 'cartography_table')
    spot('aldric_sw', cx + 2, y + 1, cz + 2)
    spot('waystone_sw', cx - 3, y + 1, cz + 2)
    v.set(cx - 3, y + 1, cz + 2, 'lodestone')
    v.set(cx - 3, y + 2, cz + 2, 'amethyst_cluster[facing=up]')
    LORE.append(('sw', cx + 9, y + 1, cz + 10))
    return v


def citadel():
    """Citadelle de Malveth : enceinte noire, 3 pylônes dans la cour, donjon (trône de Malveth), sommet (arène de Nyxar)."""
    x1, z1, x2, z2 = -206, 144, -138, 212
    y = 66
    v = Vox(902)
    r = v.r
    wl = lambda x, yy, z: 'polished_blackstone_bricks' if r.random() < 0.7 else ('cracked_polished_blackstone_bricks' if r.random() < 0.6 else 'gilded_blackstone')
    cx, cz = (x1 + x2) // 2, (z1 + z2) // 2
    v.fill(x1, y, z1, x2, y, z2, 'polished_blackstone')
    v.walls(x1, z1, x2, z2, y + 1, y + 14, wl)
    for k in (0, 1):
        v.walls(x1 + 1 + k, z1 + 1 + k, x2 - 1 - k, z2 - 1 - k, y + 1, y + 13, wl)
    crenels(v, x1, z1, x2, z1, y + 15, 'polished_blackstone_bricks')
    crenels(v, x1, z2, x2, z2, y + 15, 'polished_blackstone_bricks')
    crenels(v, x1, z1, x1, z2, y + 15, 'polished_blackstone_bricks')
    crenels(v, x2, z1, x2, z2, y + 15, 'polished_blackstone_bricks')
    for (tx, tz) in ((x1, z1), (x2, z1), (x1, z2), (x2, z2), (cx, z1), (cx, z2), (x1, cz), (x2, cz)):
        round_tower(v, tx, tz, y + 1, 5, 22, wl, floor='polished_blackstone', crenel='polished_blackstone_bricks', roof='black_concrete', roof_h=10)
        v.set(tx, y + 23, tz, 'soul_lantern') if False else None
    # porte (est, vers le camp rebelle)
    v.fill(x2 - 5, y + 1, cz - 2, x2 + 5, y + 9, cz + 2, AIR)       # traverse aussi l'anneau (rayon 5) de la tour de la porte ; 5 de large comme les barreaux
    v.fill(x2 - 5, y + 10, cz - 2, x2 + 5, y + 10, cz + 2, 'chiseled_polished_blackstone')
    v.fill(x2, y + 1, cz - 2, x2, y + 8, cz + 2, 'iron_bars')
    v.fill(x2, y + 1, cz - 4, x2, y + 9, cz - 3, wl)                  # flancs des barreaux : l'intérieur de la tour (rayon 5) les laissait contourner
    v.fill(x2, y + 1, cz + 3, x2, y + 9, cz + 4, wl)
    v.fill(x2, y + 9, cz - 2, x2, y + 9, cz + 2, wl)                  # fente au-dessus des barreaux
    SPOTS['cit_gate'] = (x2, y + 1, cz - 2, x2, y + 8, cz + 2)
    spot('cit_out', x2 + 6, y + 1, cz)
    # pylônes de la cour
    pyl = []
    for (dx, dz) in ((18, -16), (18, 16), (-4, 22)):
        x, z = cx + dx, cz + dz
        v.fill(x - 1, y + 1, z - 1, x + 1, y + 2, z + 1, 'crying_obsidian')
        v.fill(x, y + 3, z, x, y + 9, z, 'obsidian')
        v.set(x, y + 10, z, 'respawn_anchor[charges=4]')
        pyl.append((x + 0.5, y + 1, z + 0.5))
    SPOTS['pylons'] = pyl
    # donjon central (salle du trône au rez-de-chaussée, sommet = arène de Nyxar)
    kx1, kz1, kx2, kz2 = cx - 14, cz - 14, cx + 14, cz + 14
    v.walls(kx1, kz1, kx2, kz2, y + 1, y + 34, wl)
    v.fill(kx1 + 1, y + 1, kz1 + 1, kx2 - 1, y + 33, kz2 - 1, AIR)
    v.fill(kx1, y + 35, kz1, kx2, y + 35, kz2, 'polished_blackstone_bricks')
    crenels(v, kx1, kz1, kx2, kz1, y + 36, 'polished_blackstone_bricks')
    crenels(v, kx1, kz2, kx2, kz2, y + 36, 'polished_blackstone_bricks')
    crenels(v, kx1, kz1, kx1, kz2, y + 36, 'polished_blackstone_bricks')
    crenels(v, kx2, kz1, kx2, kz2, y + 36, 'polished_blackstone_bricks')
    for x in range(kx1 + 3, kx2 - 2, 5):
        for (zz) in (kz1, kz2):
            v.fill(x, y + 4, zz, x, y + 12, zz, 'purple_stained_glass_pane')
    v.fill(kx2, y + 1, cz - 2, kx2, y + 6, cz + 2, AIR)
    # trône de Malveth (ouest de la salle)
    v.fill(kx1 + 1, y + 1, cz - 4, kx1 + 4, y + 2, cz + 4, 'crying_obsidian')
    v.fill(kx1 + 1, y + 3, cz - 1, kx1 + 1, y + 9, cz + 1, 'obsidian')
    v.set(kx1 + 2, y + 3, cz, 'polished_blackstone_stairs[facing=east]')
    for z in range(kz1 + 3, kz2 - 2, 6):
        for x in range(kx1 + 6, kx2 - 2, 7):
            v.fill(x, y + 1, z, x, y + 33, z, 'polished_blackstone')
            v.set(x, y + 20, z + 1, 'soul_lantern') if False else None
    for z in range(kz1 + 4, kz2 - 3, 5):
        v.lamp(cx, y + 30, z, kind='soul_lantern')
    ARENAS['malveth'] = dict(c=(cx + 0.5, y + 1, cz + 0.5), r=13, throne=(kx1 + 3.5, y + 3, cz + 0.5))
    # escalier vers le sommet (coin sud-est intérieur), en colimaçon carré
    sx, sz = kx2 - 3, kz2 - 3
    for i, yy in enumerate(range(y + 1, y + 35)):
        k = i % 8
        dx, dz = [(0, 0), (-1, 0), (-2, 0), (-2, -1), (-2, -2), (-1, -2), (0, -2), (0, -1)][k]
        v.set(sx + dx, yy, sz + dz, 'polished_blackstone_brick_slab[type=top]')
    v.fill(sx - 2, y + 35, sz - 2, sx, y + 35, sz, AIR)
    ARENAS['nyxar'] = dict(c=(cx + 0.5, y + 36, cz + 0.5), r=13)
    LORE.append(('sw', kx1 + 5, y + 1, kz1 + 4))
    return v


def soul_well_entry():
    x0, z0 = W.P['soul_well']
    y = 64
    v = Vox(903)
    for x in range(x0 - 5, x0 + 6):
        for z in range(z0 - 5, z0 + 6):
            d = math.hypot(x - x0, z - z0)
            if d <= 5.4:
                v.set(x, y, z, 'polished_blackstone_bricks')
    for a in range(0, 360, 45):
        x, z = round(x0 + 5 * math.cos(math.radians(a))), round(z0 + 5 * math.sin(math.radians(a)))
        v.fill(x, y + 1, z, x, y + 4, z, 'polished_blackstone_wall' if a % 90 else 'crying_obsidian')
        v.set(x, y + 5, z, 'soul_lantern') if a % 90 == 0 else None
    return v


# ================================================================ entrées des donjons (petits bâtiments) + donjons
def chapel():
    x0, z0 = W.P['crypt']
    y = 66
    v = Vox(204)
    r = v.r
    v.fill(x0 - 5, y + 1, z0 - 8, x0 + 5, y + 7, z0 + 4, 'stone_bricks', hollow=True)
    v.fill(x0 - 4, y + 1, z0 - 7, x0 + 4, y + 7, z0 + 3, AIR)
    v.ruin(x0 - 5, y + 1, z0 - 8, x0 + 5, y + 7, z0 + 4, 0.25, {'stone_bricks': 'mossy_stone_bricks'})
    v.fill(x0 - 1, y + 1, z0 + 4, x0 + 1, y + 4, z0 + 4, AIR)
    # tombes
    for i in range(10):
        x, z = x0 - 9 + (i % 5) * 4, z0 + 7 + (i // 5) * 4
        v.set(x, y + 1, z, 'cobblestone_wall' if r.random() < 0.5 else 'mossy_cobblestone_wall')
        v.set(x, y, z + 1, 'coarse_dirt')
    return v
