"""TNT Tag — cartes 4 « Icebergs » (centre 0, 31200) et 5 « Patinoire » (centre 0, 31500), sur la glace.

Chargé par gen_maps.py (cartes(globals()) : Carte, IR, hsh viennent de gen_maps), jamais lancé seul.
- Icebergs : mer gelée (glace compacte et glace bleue, glissante), icebergs enneigés en pente douce, igloo, pics de glace.
- Patinoire : grande piste de glace bleue (lignes en glace compacte), gradins de neige, buts en clôture, sculptures de glace.
"""
import math


def cartes(g):
    globals().update(Carte=g['Carte'], IR=g['IR'], hsh=g['hsh'])
    return [carte4(), carte5()]

def adoucir(H, fixes=()):
    """pente d'un bloc au plus entre voisins (on rabote les sommets)"""
    changed = True
    while changed:
        changed = False
        for (x, z), h in list(H.items()):
            if (x, z) in fixes:
                continue
            m = min([H[(x + dx, z + dz)] + 1 for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (x + dx, z + dz) in H])
            if h > m:
                H[(x, z)] = m
                changed = True


def carte4():
    c = Carte(4, 'ICEBERGS', 31200, 'aqua', 'mer gelée glissante, icebergs enneigés, igloo et pics de glace')
    c.filler = 'packed_ice'
    SEA = 81
    bergs = [(-13, -12, 6.5, 5.5, 6), (14, -11, 5.0, 4.5, 4), (13, 13, 6.5, 6.0, 6), (-14, 14, 5.5, 5.0, 5),
             (0, -20, 4.0, 3.5, 3), (21, 2, 3.0, 4.5, 3), (-21, -1, 3.0, 4.0, 3), (-2, 19, 4.0, 3.0, 3)]
    H = {}
    for x in IR:
        for z in IR:
            h = SEA
            for bx, bz, rx, rz, a in bergs:
                d = ((x - bx) / rx) ** 2 + ((z - bz) / rz) ** 2
                if d < 1:
                    h = max(h, SEA + int(round(a * (1 - d) ** 0.5)))
            H[(x, z)] = h
    adoucir(H)
    c.H = H

    def mat(x, y, z, h):
        if h == SEA:
            if y < h:
                return 'packed_ice'
            return 'blue_ice' if hsh(x, z, 41) < 0.3 else 'packed_ice'
        if y == h:
            return 'snow_block'
        return 'packed_ice' if hsh(x, y, z, 42) < 0.6 else 'snow_block'
    c.terrain(mat)

    # igloo (dôme de neige, entrée au sud) sur la glace, centre (3, 2)
    ix, iz = 3, 2
    for x in range(ix - 3, ix + 4):
        for z in range(iz - 3, iz + 4):
            d = math.hypot(x - ix, z - iz)
            if 2.5 <= d < 3.6 and not (x == ix and z > iz):
                c.box(x, SEA + 1, z, x, SEA + 2, z, 'snow_block')
            if d < 2.6:
                c.set(x, SEA + 3, z, 'snow_block')
    c.set(ix, SEA + 4, iz, 'snow_block')
    c.set(ix, SEA + 2, iz, 'lantern')
    c.set(ix, SEA + 1, iz, 'air')

    # pics de glace sur la mer gelée
    for (x, z, hgt) in ((-4, -8, 4), (7, -5, 3), (-8, 4, 5), (8, 6, 3), (-1, 10, 4), (-20, 9, 3), (19, -20, 4), (-19, -21, 3),
                        (21, 21, 3), (2, -14, 3)):
        if H[(x, z)] == SEA and c.get(x, SEA + 1, z) == 'air':
            c.box(x, SEA + 1, z, x, SEA + hgt, z, 'packed_ice')
            c.set(x, SEA + hgt + 1, z, 'blue_ice')

    # lanternes sur les icebergs
    for (x, z) in ((-13, -12), (13, 13), (-14, 14), (14, -11)):
        c.lamp_post(x, z, wood='spruce_fence')

    c.home = (0, SEA + 1, -6)
    pts = [(0, -6), (-6, -2), (6, -1), (10, 5), (-9, 8), (2, 9), (-4, -15), (9, -17), (20, -8), (21, 10),
           (-21, 6), (-20, -10), (-11, -11), (11, 12), (-12, 13), (0, 22)]
    c.spawns = [(x, c.top(x, z) + 1, z) for x, z in pts]
    return c


def carte5():
    c = Carte(5, 'PATINOIRE', 31500, 'light_purple', 'grande patinoire glissante, gradins de neige, buts et sculptures de glace')
    c.filler = 'snow_block'
    ICE = 82
    H = {}
    rink = set()
    for x in IR:
        for z in IR:
            # piste : rectangle arrondi 35 x 27 (coins de rayon 6)
            ax, az = max(0, abs(x) - 11), max(0, abs(z) - 7)
            d = math.hypot(ax, az)
            if d <= 6:
                rink.add((x, z))
                H[(x, z)] = ICE
            else:
                H[(x, z)] = min(ICE + 4, ICE + int(math.ceil((d - 6) / 1.2)))
    adoucir(H, fixes=rink)
    c.H = H

    def mat(x, y, z, h):
        if (x, z) in rink:
            if y < h:
                return 'packed_ice'
            if x == 0 or (3.5 <= math.hypot(x, z) <= 4.5):
                return 'packed_ice'
            if abs(x) == 9:
                return 'light_blue_concrete'
            return 'blue_ice'
        if y == h:
            return 'snow_block'
        return 'snow_block'
    c.terrain(mat)

    # buts (cadres de clôture) aux deux bouts de la piste
    for sx in (-1, 1):
        gx = sx * 15
        for z in (-2, 2):
            c.box(gx, ICE + 1, z, gx, ICE + 2, z, 'spruce_fence')
        c.box(gx + sx, ICE + 1, -2, gx + sx, ICE + 1, 2, 'spruce_fence')
    # sculptures de glace (piliers) et blocs à contourner
    for (x, z, hgt) in ((0, 0, 3), (-6, -5, 2), (6, 5, 2), (-6, 5, 1), (6, -5, 1), (-11, 0, 1), (11, 0, 1)):
        c.box(x, ICE + 1, z, x, ICE + hgt, z, 'packed_ice')
    c.set(0, ICE + 4, 0, 'sea_lantern')
    for (x, z) in ((-3, -9), (3, 9), (-12, 7), (12, -7)):
        c.box(x, ICE + 1, z, x + 1, ICE + 1, z, 'packed_ice')
    # lampadaires sur les gradins
    for (x, z) in ((-20, -15), (20, -15), (-20, 15), (20, 15), (0, -18), (0, 18), (-22, 0), (22, 0)):
        if (x, z) not in rink:
            c.lamp_post(x, z)

    c.home = (0, ICE + 1, -10)
    pts = [(0, -10), (0, 10), (-8, -3), (8, 3), (-13, -8), (13, 8), (-13, 8), (13, -8), (-4, 4), (4, -4),
           (-20, -20), (20, 20), (-20, 20), (20, -20), (-22, 8), (22, -8)]
    c.spawns = [(x, c.top(x, z) + 1, z) for x, z in pts]
    return c
