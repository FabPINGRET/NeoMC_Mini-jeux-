"""🏰 Ombrelune : donjons (enfilade de salles sous terre, thèmes). Module importé par ol_structs.
"""
import zlib

from tv_build import Vox, AIR
from ol_skit import DUNGEONS, dir_vec, opp


# ================================================================ DONJONS (générique) : enfilade de salles sous terre
DUN_THEMES = {
    'crypt': dict(wall='stone_bricks', alt='mossy_stone_bricks', crack='cracked_stone_bricks', floor='polished_andesite', pillar='chiseled_stone_bricks',
                  light='soul_lantern', deco=['cobweb', 'skeleton_skull', 'candle[candles=3,lit=true]', 'chiseled_stone_bricks'], door='iron_bars'),
    'nest': dict(wall='mossy_cobblestone', alt='mossy_stone_bricks', crack='cobblestone', floor='moss_block', pillar='oak_log',
                 light='verdant_froglight', deco=['cobweb', 'cobweb', 'cobweb', 'brown_mushroom'], door='cobweb'),
    'ice': dict(wall='packed_ice', alt='blue_ice', crack='snow_block', floor='packed_ice', pillar='blue_ice', light='sea_lantern',
                deco=['snow', 'ice', 'powder_snow', 'blue_ice'], door='iron_bars'),
    'sunken': dict(wall='prismarine_bricks', alt='mossy_stone_bricks', crack='dark_prismarine', floor='prismarine', pillar='prismarine_bricks',
                   light='sea_lantern', deco=['seagrass', 'moss_carpet', 'kelp_plant', 'sea_pickle[pickles=3,waterlogged=false]'], door='iron_bars'),
    'tomb': dict(wall='cut_sandstone', alt='chiseled_sandstone', crack='smooth_sandstone', floor='smooth_sandstone', pillar='chiseled_red_sandstone',
                 light='lantern', deco=['skeleton_skull', 'decorated_pot', 'cobweb', 'dead_bush'], door='iron_bars'),
    'forge': dict(wall='nether_bricks', alt='red_nether_bricks', crack='cracked_nether_bricks', floor='polished_blackstone', pillar='chiseled_nether_bricks',
                  light='shroomlight', deco=['magma_block', 'chain', 'blackstone', 'soul_lantern'], door='iron_bars'),
    'mine': dict(wall='deepslate_bricks', alt='deepslate_tiles', crack='cracked_deepslate_bricks', floor='polished_deepslate', pillar='stripped_spruce_log',
                 light='lantern', deco=['iron_ore', 'deepslate_gold_ore', 'cobweb', 'rail'], door='iron_bars'),
    'souls': dict(wall='polished_blackstone_bricks', alt='cracked_polished_blackstone_bricks', crack='gilded_blackstone', floor='soul_soil', pillar='crying_obsidian',
                  light='soul_lantern', deco=['soul_fire', 'wither_skeleton_skull', 'chain', 'soul_lantern'], door='iron_bars'),
}


def dungeon(key, region, entry, y_floor, theme, rooms_dir, name, alpha):
    """Donjon : escalier depuis l'entrée (x, z, y du sol), puis 4 salles reliées par des couloirs dans la direction rooms_dir.
    Salles 1-3 : vagues de monstres (portes fermées tant qu'il en reste), salle 4 : l'alpha, puis le trésor."""
    t = DUN_THEMES[theme]
    v = Vox(zlib.crc32(key.encode()) & 0xffff)
    r = v.r

    def wl(x, y, z):
        q = r.random()
        return t['alt'] if q < 0.18 else (t['crack'] if q < 0.28 else t['wall'])
    ex, ez, ey = entry
    dx, dz = dir_vec(rooms_dir)
    # escalier en descente (largeur 3) de ey à y_floor
    n = ey - y_floor
    sx, sz = ex, ez
    for i in range(n + 1):
        yy = ey - i
        for k in (-1, 0, 1):
            x, z = (sx + dx * i + (k if dz else 0), sz + dz * i + (k if dx else 0))
            v.fill(x, yy - 1, z, x, yy - 1, z, t['floor'])
            v.fill(x, yy, z, x, yy + 3, z, AIR)
        for k in (-2, 2):
            x, z = (sx + dx * i + (k if dz else 0), sz + dz * i + (k if dx else 0))
            v.fill(x, yy - 1, z, x, yy + 4, z, wl)
        x, z = sx + dx * i, sz + dz * i
        v.set(x - (0 if dz else 0), yy + 4, z, wl(0, 0, 0))
        for k in (-1, 0, 1):
            xx, zz = (x + (k if dz else 0), z + (k if dx else 0))
            v.set(xx, yy + 4, zz, wl(0, 0, 0))
        if i % 4 == 0:
            v.set(x, yy + 3, z, t['light'] + ('[hanging=true]' if t['light'] in ('lantern', 'soul_lantern') else ''))
    # salles
    cx, cz = sx + dx * (n + 4), sz + dz * (n + 4)
    rooms = []
    links = []
    sizes = [(7, 5), (8, 6), (8, 6), (11, 9)]
    pos = 0
    for i, (half, hgt) in enumerate(sizes):
        pos += half + (0 if i == 0 else 4)
        rx, rz = cx + dx * pos, cz + dz * pos
        y = y_floor
        v.fill(rx - half - 1, y - 1, rz - half - 1, rx + half + 1, y + hgt + 1, rz + half + 1, wl)
        v.fill(rx - half, y, rz - half, rx + half, y + hgt, rz + half, AIR)
        v.fill(rx - half, y - 1, rz - half, rx + half, y - 1, rz + half, t['floor'])
        for (px_, pz_) in ((rx - half + 2, rz - half + 2), (rx + half - 2, rz - half + 2), (rx - half + 2, rz + half - 2), (rx + half - 2, rz + half - 2)):
            v.fill(px_, y, pz_, px_, y + hgt, pz_, t['pillar'])
            v.set(px_ + (1 if px_ < rx else -1), y + hgt - 1, pz_, t['light'] + ('[hanging=false]' if t['light'] in ('lantern', 'soul_lantern') else ''))
        for _ in range(half * 2):
            x, z = r.randint(rx - half, rx + half), r.randint(rz - half, rz + half)
            if abs(x - rx) > 1 and abs(z - rz) > 1 and v.get(x, y, z) == AIR:
                b = r.choice(t['deco'])
                if b == 'chain':
                    v.set(x, y + hgt, z, 'iron_chain')
                else:
                    v.set(x, y, z, b)
        rooms.append(dict(c=(rx + 0.5, y, rz + 0.5), half=half, h=hgt))
        pos += half
        if i < len(sizes) - 1:
            links.append((rx, rz, half))
        rooms[-1]['door'] = (rx + dx * (half + 1), y, rz + dz * (half + 1))
    # couloirs vers la salle suivante (porte au bout) : creusés après TOUTES les coques, sinon la coque de la salle suivante les rebouche ;
    # le tronçon half+2 n'appartient à aucune coque et le sous-sol est vide : murs / plafond only=(None,) comme le couloir d'entrée
    for (rx, rz, half) in links:
        for k in range(1, 5):
            xx, zz = rx + dx * (half + k), rz + dz * (half + k)
            for w_ in (-1, 0, 1):
                x, z = (xx + (w_ if dz else 0), zz + (w_ if dx else 0))
                v.fill(x, y_floor, z, x, y_floor + 2, z, AIR)
                v.set(x, y_floor - 1, z, t['floor'])
                v.fill(x, y_floor + 3, z, x, y_floor + 3, z, wl, only=(None,))
            for w_ in (-2, 2):
                x, z = (xx + (w_ if dz else 0), zz + (w_ if dx else 0))
                v.fill(x, y_floor - 1, z, x, y_floor + 3, z, wl, only=(None,))
    # couloir d'entrée : de l'escalier (n) à la coque de la salle 1 (n + 3) ; sous la croûte le sous-sol est vide, d'où les murs only=(None,)
    for k in range(n + 1, n + 4):
        xx, zz = sx + dx * k, sz + dz * k
        for w_ in (-1, 0, 1):
            x, z = (xx + (w_ if dz else 0), zz + (w_ if dx else 0))
            v.fill(x, y_floor, z, x, y_floor + 2, z, AIR)
            v.set(x, y_floor - 1, z, t['floor'])
            v.fill(x, y_floor + 3, z, x, y_floor + 3, z, wl, only=(None,))
        for w_ in (-2, 2):
            x, z = (xx + (w_ if dz else 0), zz + (w_ if dx else 0))
            v.fill(x, y_floor - 1, z, x, y_floor + 3, z, wl, only=(None,))
    # trésor derrière la dernière salle
    last = rooms[-1]
    tx, tz = round(last['c'][0] - 0.5) + dx * (last['half'] - 1), round(last['c'][2] - 0.5) + dz * (last['half'] - 1)
    v.set(tx, y_floor, tz, 'chest[facing=' + opp(rooms_dir) + ']')
    v.fill(tx - (1 if dz else 0), y_floor - 1, tz - (1 if dx else 0), tx + (1 if dz else 0), y_floor - 1, tz + (1 if dx else 0), 'gold_block')
    DUNGEONS[key] = dict(region=region, name=name, alpha=alpha, theme=theme, entry=(ex + 0.5, ey, ez + 0.5), rooms=rooms, dir=rooms_dir,
                         chest=(tx, y_floor, tz), y=y_floor)
    return v
