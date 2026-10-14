"""🧟 Plans des cartes Zombies « complexes » (tools/arcade/gen_zombies.py, réglage `layout`).

Coordonnées relatives : x absolu, z relatif au Z de la carte. Le sol est en y 80, on marche en y 81, toit en y 86.
Tout le rectangle de la carte est d'abord plein (murs), puis chaque salle est creusée : entre deux salles voisines, il reste
un mur d'un bloc (portes à acheter dedans), et les zones hors salle restent pleines (les enclos des fenêtres y sont creusés).

Salle : (x1, x2, z1, z2) = intérieur. Porte : (nom, coût, (x1, z1, x2, z2) de la barricade dans le mur, interaction (x, z), salle ouverte).
Fenêtre : (salle, x, z du trou dans le mur extérieur, nx, nz normale vers l'extérieur) — 4 blocs pleins derrière.
Achat au mur (murs nord-sud seulement) : (tag, nom, coût, x du mur, z, côté 'w' = mur à l'ouest de la salle | 'e', arme).
Machine : (bloc x, z, côté 'w' | 'e' | 'n' | 's') — l'interaction est sur la case devant la machine.
"""


def machine(bx, bz, side):
    """→ (bloc (x, z), interaction (x, z), étiquette (x, z)) pour une machine contre un mur de salle"""
    if side == 'w':
        return (bx, bz), (bx + 1.5, bz + 0.5), (bx + 2.0, bz + 0.5)
    if side == 'e':
        return (bx, bz), (bx - 0.5, bz + 0.5), (bx - 1.0, bz + 0.5)
    if side == 'n':
        return (bx, bz), (bx + 0.5, bz + 1.5), (bx + 0.5, bz + 1.0)
    return (bx, bz), (bx + 0.5, bz - 0.5), (bx + 0.5, bz + 0.0)


def wall_buy(tag, nm, cost, wx, z, side, gun):
    """→ entrée WALL de gen_zombies : interaction devant le mur, arme collée à la face du mur"""
    if side == 'w':
        return (tag, nm, cost, (wx + 1.5, z + 0.5), gun, (wx + 1.05, z + 0.5), 90)
    return (tag, nm, cost, (wx - 0.5, z + 0.5), gun, (wx - 0.05, z + 0.5), -90)


LAYOUTS = {
    # 🏭 Usine : hall, couloir nord, atelier, entrepôt, salle des machines, bureaux, quai — deux chemins vers la salle des machines
    'usine': dict(
        rooms={'a': (-8, 8, -8, 8), 'b': (-4, 4, -30, -10), 'c': (-30, -10, -12, 12), 'd': (10, 32, -14, 14),
               'e': (-12, 14, -52, -32), 'f': (-30, -14, -36, -14), 'g': (16, 34, -44, -16)},
        names={'a': 'Hall', 'b': 'Couloir', 'c': 'Atelier', 'd': 'Entrepôt', 'e': 'Salle des machines', 'f': 'Bureaux', 'g': 'Quai'},
        floors={'a': 'polished_andesite', 'b': 'iron_block', 'c': 'smooth_stone', 'd': 'spruce_planks', 'e': 'polished_deepslate',
                'f': 'dark_oak_planks', 'g': 'stone_bricks'},
        wall='gray_concrete', band='cyan_terracotta', roof='smooth_stone', light='sea_lantern',
        doors={1: ('Hall → Couloir', 750, (-1, -9, 1, -9), (0.5, -8.5), 'b'),
               2: ('Hall → Atelier', 750, (-9, -1, -9, 1), (-8.5, 0.5), 'c'),
               3: ('Hall → Entrepôt', 750, (9, -1, 9, 1), (9.5, 0.5), 'd'),
               4: ('Couloir → Salle des machines', 1000, (-1, -31, 1, -31), (0.5, -30.5), 'e'),
               5: ('Atelier → Bureaux', 1000, (-23, -13, -21, -13), (-21.5, -12.5), 'f'),
               6: ('Entrepôt → Quai', 1000, (23, -15, 25, -15), (24.5, -14.5), 'g'),
               7: ('Quai → Salle des machines', 1250, (15, -42, 15, -40), (15.5, -40.5), 'e'),
               8: ('Bureaux → Salle des machines', 1250, (-13, -35, -13, -33), (-12.5, -33.5), 'e')},
        windows=[('a', 7, -9, 0, -1), ('a', 0, 9, 0, 1), ('b', -5, -20, -1, 0), ('b', 5, -24, 1, 0),
                 ('c', -31, 0, -1, 0), ('c', -20, 13, 0, 1), ('d', 33, 0, 1, 0), ('d', 20, 15, 0, 1),
                 ('e', 0, -53, 0, -1), ('e', -13, -45, -1, 0), ('f', -31, -25, -1, 0), ('f', -22, -37, 0, -1),
                 ('g', 35, -30, 1, 0), ('g', 25, -45, 0, -1)],
        wall_buys=[('zb11', 'Fusil M14', 500, -9, 5, 'w', 4), ('zb12', 'Fusil à pompe', 500, 9, -5, 'e', 3),
                   ('zb13', 'Mitraillette', 1000, -31, -8, 'w', 2), ('zb14', 'Sniper', 1500, 15, -48, 'e', 5),
                   ('zb15', 'Grenades singe ×3', 1000, 33, 10, 'e', 11)],
        perks={'zb23': (-30, 6, 'w'), 'zb24': (4, -20, 'e'), 'zb25': (-30, -30, 'w'), 'zb26': (34, -20, 'e'), 'zb27': (1, -52, 'n')},
        jug=(32, -8, 'e'), speed=(34, -36, 'e'), box=(1, -42),
        barrels=[(14, -10), (14, 6), (20, -6), (20, 4), (26, -10), (26, 6), (-24, -6), (-16, 4), (-26, 8),
                 (-6, -46), (8, -46), (-6, -38), (8, -38), (20, -38), (28, -26), (-24, -28), (-18, -20), (-5, 4), (4, -5)],
        start=(0, 0)),
    # 🚇 Station : hall central, deux couloirs vers les quais est et ouest, longue galerie nord qui les relie, réacteur au sud
    'station': dict(
        rooms={'a': (-7, 7, -7, 7), 'b': (-25, -9, -2, 2), 'c': (9, 25, -2, 2), 'd': (-45, -27, -12, 12), 'e': (27, 45, -12, 12),
               'f': (-45, 45, -30, -14), 'g': (-12, 12, 9, 29)},
        names={'a': 'Hall', 'b': 'Couloir ouest', 'c': 'Couloir est', 'd': 'Quai ouest', 'e': 'Quai est', 'f': 'Galerie', 'g': 'Réacteur'},
        floors={'a': 'smooth_quartz', 'b': 'light_gray_concrete', 'c': 'light_gray_concrete', 'd': 'polished_diorite',
                'e': 'polished_diorite', 'f': 'white_terracotta', 'g': 'warped_planks'},
        wall='white_concrete', band='light_blue_terracotta', roof='smooth_quartz', light='sea_lantern',
        doors={1: ('Hall → Couloir ouest', 750, (-8, -1, -8, 1), (-7.5, 0.5), 'b'),
               2: ('Hall → Couloir est', 750, (8, -1, 8, 1), (8.5, 0.5), 'c'),
               3: ('Couloir → Quai ouest', 1000, (-26, -1, -26, 1), (-25.5, 0.5), 'd'),
               4: ('Couloir → Quai est', 1000, (26, -1, 26, 1), (26.5, 0.5), 'e'),
               5: ('Quai ouest → Galerie', 1250, (-37, -13, -35, -13), (-35.5, -12.5), 'f'),
               6: ('Quai est → Galerie', 1250, (35, -13, 37, -13), (36.5, -12.5), 'f'),
               7: ('Hall → Réacteur', 1500, (-1, 8, 1, 8), (0.5, 8.5), 'g')},
        windows=[('a', -4, -8, 0, -1), ('a', 4, -8, 0, -1), ('b', -17, -3, 0, -1), ('b', -17, 3, 0, 1),
                 ('c', 17, -3, 0, -1), ('c', 17, 3, 0, 1), ('d', -46, 0, -1, 0), ('d', -36, 13, 0, 1),
                 ('e', 46, 0, 1, 0), ('e', 36, 13, 0, 1), ('f', -25, -31, 0, -1), ('f', 0, -31, 0, -1), ('f', 25, -31, 0, -1),
                 ('g', 0, 30, 0, 1), ('g', -13, 20, -1, 0), ('g', 13, 22, 1, 0)],
        wall_buys=[('zb11', 'Fusil M14', 500, -8, 5, 'w', 4), ('zb12', 'Fusil à pompe', 500, 8, -5, 'e', 3),
                   ('zb13', 'Mitraillette', 1000, -46, -8, 'w', 2), ('zb14', 'Sniper', 1500, 46, 4, 'e', 5),
                   ('zb15', 'Grenades singe ×3', 1000, -46, -22, 'w', 11)],
        perks={'zb23': (-45, 8, 'w'), 'zb24': (45, -8, 'e'), 'zb25': (-10, -30, 'n'), 'zb26': (10, -30, 'n'), 'zb27': (0, 29, 's')},
        jug=(30, -30, 'n'), speed=(12, 14, 'e'), box=(0, -22),
        barrels=[(-40, -6), (-32, 4), (-40, 6), (32, -6), (40, 4), (-36, -26), (-20, -22), (16, -24), (36, -20), (-6, 14), (6, 22)],
        start=(0, 0)),
}


def get(name, Z):
    """Plan `name` en coordonnées absolues pour une carte en Z"""
    L = LAYOUTS[name]
    zz = lambda z: Z + z
    rooms = {r: (x1, x2, zz(z1), zz(z2)) for r, (x1, x2, z1, z2) in L['rooms'].items()}
    doors = {d: (nm, c, (x1, zz(z1), x2, zz(z2)), (ix, zz(iz)), room) for d, (nm, c, (x1, z1, x2, z2), (ix, iz), room) in L['doors'].items()}
    wins = [(r, x, zz(z), nx, nz) for (r, x, z, nx, nz) in L['windows']]
    walls = [wall_buy(t, nm, c, wx, zz(z), s, g) for (t, nm, c, wx, z, s, g) in L['wall_buys']]
    xs = [v for (x1, x2, _, _) in rooms.values() for v in (x1, x2)]
    zs = [v for (_, _, z1, z2) in rooms.values() for v in (z1, z2)]
    area = (min(xs) - 6, min(zs) - 6, max(xs) + 6, max(zs) + 6)
    m = lambda t: machine(t[0], zz(t[1]), t[2])
    return dict(rooms=rooms, doors=doors, wins=wins, walls=walls, perks={k: m(v) for k, v in L['perks'].items()},
                jug=m(L['jug']), speed=m(L['speed']), box=(L['box'][0], zz(L['box'][1])),
                barrels=[(x, zz(z)) for (x, z) in L['barrels']], start=(L['start'][0], zz(L['start'][1])), area=area,
                floors=L['floors'], names=L['names'], wall=L['wall'], band=L['band'], roof=L['roof'], light=L['light'])
