"""🧟 Plans des cartes Zombies « complexes » (tools/arcade/gen_zombies.py, réglage `layout`).

Coordonnées relatives : x absolu, z relatif au Z de la carte. Le sol est en y 80, on marche en y 81, toit en y 86.
Tout le rectangle de la carte est d'abord plein (murs), puis chaque salle est creusée : entre deux salles voisines, il reste
un mur d'un bloc (portes à acheter dedans), et les zones hors salle restent pleines (les enclos des fenêtres y sont creusés).

Salle : (x1, x2, z1, z2) = intérieur. Porte : (nom, coût, (x1, z1, x2, z2) de la barricade dans le mur, interaction (x, z), salle ouverte).
Fenêtre : (salle, x, z du trou dans le mur extérieur, nx, nz normale vers l'extérieur) — 4 blocs pleins derrière.
Achat au mur (murs nord-sud seulement) : (tag, nom, coût, x du mur, z, côté 'w' = mur à l'ouest de la salle | 'e', arme).
Machine : (bloc x, z, côté 'w' | 'e' | 'n' | 's') — l'interaction est sur la case devant la machine.

Niveaux (cartes « hôpital », « mine ») : une salle peut avoir un 5e élément y (sol, 80 par défaut) et un 6e h (hauteur
intérieure, 5 par défaut : air y+1..y+h, plafond y+h+1). Deux salles peuvent être superposées (plafond de l'une = sol de
l'autre). Le niveau d'un objet est celui de sa salle : déduit de sa position (la plus basse si superposées) ou donné en
dernier élément (clé de salle) pour les achats au mur, machines, boîte, caisses, départ. Porte : 6e élément y facultatif
(sinon le sol de la salle ouverte). Fenêtre : 6e élément y facultatif. `extra` : blocs posés après le creusement
(('fill', x1, y1, z1, x2, y2, z2, bloc) ou ('set', x, y, z, bloc), z relatifs) — escaliers, balcons, terrasses, trous.
`centers` : {salle: (x, z)} centre de répartition (Infection) si le centre géométrique tombe dans un escalier.
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


def stairs(x1, x2, z1, z2, y0, n, facing, block='stone_brick_stairs', support='stone_bricks'):
    """n marches montant vers `facing` à partir de y0 + 1, sur la bande x1..x2 (marches le long de z) ou z1..z2 (le long de x)"""
    out = []
    for k in range(1, n + 1):
        if facing in ('north', 'south'):
            z = z1 - k + 1 if facing == 'north' else z1 + k - 1
            box = (x1, z, x2, z)
        else:
            x = x1 - k + 1 if facing == 'west' else x1 + k - 1
            box = (x, z1, x, z2)
        if k > 1:
            out.append(('fill', box[0], y0 + 1, box[1], box[2], y0 + k - 1, box[3], support))
        out.append(('fill', box[0], y0 + k, box[1], box[2], y0 + k, box[3], f'{block}[facing={facing}]'))
    return out



def _rail(x1, z1, x2, z2, y, b='iron_bars'):
    return ('fill', x1, y, z1, x2, y, z2, b)


# 🏥 Hôpital : deux étages superposés. RDC (y 80) : accueil, couloir, urgences, morgue ; cage d'escalier haute (y 80..91) ;
# étage (y 86) : salle au-dessus de l'accueil, passerelle au-dessus du couloir, bloc opératoire. Les urgences ont une galerie
# (balcon y 86) qu'on atteint par l'escalier intérieur ou par la passerelle de l'étage.
_H_EXTRA = (
    # cage d'escalier : 5 marches vers le nord (z 3 → −1), palier y 86 de z −2 à −12
    stairs(-13, -11, 3, 3, 80, 5, 'north', 'polished_andesite_stairs', 'smooth_stone') +
    [('fill', -16, 86, -12, -10, 86, -2, 'polished_andesite'), _rail(-16, -2, -14, -2, 87), _rail(-10, -2, -10, -2, 87),
     ('set', -13, 86, -7, 'sea_lantern')] +
    # urgences : galerie y 86 sur x 32..36, garde-corps, escalier intérieur (x 41 → 37, z 8..10) vers l'ouest
    [('fill', 32, 86, -12, 36, 86, 12, 'polished_andesite'), _rail(36, -12, 36, 7, 87), _rail(36, 11, 36, 12, 87)] +
    stairs(41, 41, 8, 10, 80, 5, 'west', 'polished_andesite_stairs', 'smooth_stone') +
    [('set', 34, 86, z, 'sea_lantern') for z in (-10, -5, 0, 5, 10)] +
    # décor : lits (urgences), brancards (couloir)
    [('fill', 46, 81, z, 48, 81, z + 1, 'white_wool') for z in (-10, -4, 2)] +
    [('set', 49, 81, z, 'white_concrete') for z in (-10, -4, 2)]
)
LAYOUTS['hopital'] = dict(
    rooms={'a': (-8, 8, -8, 8), 'b': (10, 30, -3, 3), 'c': (32, 50, -12, 12, 80, 11), 'd': (-16, -10, -12, 12, 80, 11),
           'g': (10, 30, -22, -5), 'f': (-8, 8, -8, 8, 86), 'h': (10, 30, -3, 3, 86), 'e': (-34, -18, -12, 4, 86)},
    names={'a': 'Accueil', 'b': 'Couloir', 'c': 'Urgences', 'd': 'Escalier', 'g': 'Morgue', 'f': 'Étage', 'h': 'Passerelle',
           'e': 'Bloc opératoire'},
    floors={'a': 'white_terracotta', 'b': 'light_gray_concrete', 'c': 'white_concrete', 'd': 'smooth_stone', 'g': 'polished_andesite',
            'f': 'white_terracotta', 'h': 'iron_block', 'e': 'light_blue_terracotta'},
    wall='white_concrete', band='lime_terracotta', roof='smooth_quartz', light='sea_lantern',
    doors={1: ('Accueil → Couloir', 750, (9, -1, 9, 1), (9.5, 0.5), 'b'),
           2: ('Couloir → Urgences', 1000, (31, -1, 31, 1), (31.5, 0.5), 'c'),
           3: ('Accueil → Escalier', 750, (-9, -1, -9, 1), (-8.5, 0.5), 'd'),
           4: ('Escalier → Étage', 1000, (-9, -8, -9, -6), (-8.5, -6.5), 'f', 86),
           5: ('Escalier → Bloc opératoire', 1250, (-17, -8, -17, -6), (-16.5, -6.5), 'e', 86),
           6: ('Étage → Passerelle', 1000, (9, -1, 9, 1), (9.5, 0.5), 'h'),
           7: ('Passerelle → Galerie', 1250, (31, -1, 31, 1), (31.5, 0.5), 'c', 86),
           8: ('Couloir → Morgue', 1000, (19, -4, 21, -4), (20.5, -3.5), 'g')},
    windows=[('a', 0, 9, 0, 1), ('a', 5, -9, 0, -1), ('b', 20, 4, 0, 1), ('c', 51, 0, 1, 0), ('c', 41, 13, 0, 1),
             ('c', 44, -13, 0, -1), ('d', -13, 13, 0, 1), ('d', -17, 8, -1, 0), ('e', -35, -4, -1, 0), ('e', -26, -13, 0, -1),
             ('f', 0, 9, 0, 1), ('f', -4, -9, 0, -1), ('g', 20, -23, 0, -1), ('g', 9, -14, -1, 0), ('h', 25, 4, 0, 1),
             ('h', 15, -4, 0, -1)],
    wall_buys=[('zb11', 'Fusil M14', 500, -9, 5, 'w', 4), ('zb12', 'Fusil à pompe', 500, 9, -5, 'e', 3),
               ('zb13', 'Mitraillette', 1000, 9, -19, 'w', 2), ('zb14', 'Sniper', 1500, -35, -10, 'w', 5),
               ('zb15', 'Grenades singe ×3', 1000, 51, 8, 'e', 11)],
    perks={'zb23': (-8, 5, 'w', 'f'), 'zb24': (30, -20, 'e'), 'zb25': (-16, 10, 'w'), 'zb26': (32, -10, 'w'), 'zb27': (-26, 4, 's')},
    jug=(8, 5, 'e', 'f'), speed=(50, -8, 'e'), box=(20, -14),
    barrels=[(-5, -5), (4, 3), (40, 5), (44, -7), (-30, -9), (-22, 0), (13, -11), (25, -18), (-4, 3, 'f'), (4, -6, 'f')],
    extra=_H_EXTRA, centers={'d': (-14, 8)}, start=(0, 0))

# ⛏ Mine : rampe qui monte de la galerie d'entrée au puits (y 86), galerie basse sous le puits (on peut y tomber par un trou),
# carrière à deux terrasses (y 83, y 86) menant à l'atelier haut, salle des wagonnets au nord du puits.
_M_EXTRA = (
    # rampe : marches vers l'est sur z 2..4 (x 15 → 19), plateforme pleine x 20..28 jusqu'à y 86 avec un tunnel z −1..1 (y 81..83)
    stairs(15, 15, 2, 4, 80, 5, 'east', 'cobblestone_stairs', 'cobblestone') +
    [('fill', 20, 81, -4, 28, 86, 4, 'cobblestone'), ('fill', 20, 81, -1, 28, 83, 1, 'air'), ('set', 24, 84, 0, 'glowstone'),
     ('fill', 20, 86, -4, 28, 86, 4, 'spruce_planks'), _rail(15, -4, 19, -4, 81, 'oak_fence')] +
    # carrière : terrasse 1 (z 0..6, y 83), terrasse 2 (z 7..14, y 86), escaliers vers le sud
    [('fill', -30, 81, 0, -10, 83, 6, 'stone'), ('fill', -30, 81, 7, -10, 86, 14, 'stone'),
     ('fill', -30, 83, 0, -10, 83, 6, 'gravel'), ('fill', -30, 86, 7, -10, 86, 14, 'coarse_dirt')] +
    stairs(-22, -20, -3, -3, 80, 3, 'south', 'cobblestone_stairs', 'cobblestone') +
    stairs(-14, -12, 4, 4, 83, 3, 'south', 'cobblestone_stairs', 'cobblestone') +
    [_rail(-30, 0, -23, 0, 84, 'oak_fence'), _rail(-19, 0, -10, 0, 84, 'oak_fence'),       # bords des terrasses (sauf escaliers)
     _rail(-30, 7, -15, 7, 87, 'oak_fence'), _rail(-11, 7, -10, 7, 87, 'oak_fence')] +
    # puits : trou dans le sol (on tombe dans la galerie basse), rails décoratifs
    [('fill', 38, 86, 2, 40, 86, 4, 'air'), ('fill', 31, 87, -9, 31, 87, 9, 'rail[shape=north_south]'),
     ('fill', 46, 81, -9, 46, 81, 9, 'rail[shape=north_south]')]
)
LAYOUTS['mine'] = dict(
    rooms={'a': (-8, 8, -6, 6), 'b': (10, 28, -4, 4, 80, 11), 'g': (30, 48, -10, 10), 'c': (30, 48, -10, 10, 86),
           'd': (-30, -10, -14, 14, 80, 11), 'e': (-30, -10, 16, 30, 86), 'f': (30, 48, -30, -12, 86)},
    names={'a': 'Entrée', 'b': 'Rampe', 'g': 'Galerie basse', 'c': 'Puits', 'd': 'Carrière', 'e': 'Atelier haut', 'f': 'Wagonnets'},
    floors={'a': 'gravel', 'b': 'cobblestone', 'g': 'coarse_dirt', 'c': 'spruce_planks', 'd': 'cobblestone', 'e': 'spruce_planks',
            'f': 'stone_bricks'},
    wall='stone', band='andesite', roof='deepslate', light='glowstone',
    doors={1: ('Entrée → Rampe', 750, (9, -1, 9, 1), (9.5, 0.5), 'b'),
           2: ('Entrée → Carrière', 750, (-9, -4, -9, -2), (-8.5, -2.5), 'd'),
           3: ('Rampe → Galerie basse', 1000, (29, -1, 29, 1), (29.5, 0.5), 'g'),
           4: ('Rampe → Puits', 1000, (29, -1, 29, 1), (29.5, 0.5), 'c', 86),
           5: ('Carrière → Atelier haut', 1250, (-14, 15, -12, 15), (-12.5, 15.5), 'e'),
           6: ('Puits → Wagonnets', 1250, (38, -11, 40, -11), (39.5, -10.5), 'f')},
    windows=[('a', 0, 7, 0, 1), ('a', 0, -7, 0, -1), ('b', 12, 5, 0, 1), ('b', 24, -5, 0, -1, 86), ('c', 49, 0, 1, 0),
             ('c', 40, 11, 0, 1), ('d', -31, -6, -1, 0), ('d', -20, -15, 0, -1), ('e', -31, 24, -1, 0), ('e', -20, 31, 0, 1),
             ('f', 49, -20, 1, 0), ('f', 40, -31, 0, -1), ('g', 49, -4, 1, 0), ('g', 36, 11, 0, 1)],
    wall_buys=[('zb11', 'Fusil M14', 500, -9, 4, 'w', 4), ('zb12', 'Fusil à pompe', 500, 9, -4, 'e', 3),
               ('zb13', 'Mitraillette', 1000, 49, 6, 'e', 2), ('zb14', 'Sniper', 1500, -31, 20, 'w', 5),
               ('zb15', 'Grenades singe ×3', 1000, 49, -6, 'e', 11, 'c')],
    perks={'zb23': (-30, -10, 'w'), 'zb24': (33, 10, 's', 'c'), 'zb25': (-10, 28, 'e'), 'zb26': (48, -28, 'e'), 'zb27': (32, -30, 'n')},
    jug=(30, -8, 'w', 'g'), speed=(-30, 17, 'w'), box=(36, -6, 'c'),
    barrels=[(-6, 3), (5, -5), (-26, -10), (-15, -12), (42, 6, 'c'), (32, -8, 'c'), (40, -7, 'g'), (34, 6, 'g'), (-22, 22), (-14, 26),
             (36, -20), (44, -24)],
    extra=_M_EXTRA, centers={'b': (12, 0), 'd': (-20, -8)}, start=(0, 0))

def get(name, Z):
    """Plan `name` en coordonnées absolues pour une carte en Z"""
    L = LAYOUTS[name]
    zz = lambda z: Z + z
    R = L['rooms']
    ry = {r: (t[4] if len(t) > 4 else 80) for r, t in R.items()}
    rh = {r: (t[5] if len(t) > 5 else 5) for r, t in R.items()}
    rooms = {r: (t[0], t[1], zz(t[2]), zz(t[3])) for r, t in R.items()}

    def yat(x, z, room=None):
        """sol de la salle `room`, sinon de la plus basse salle contenant (x, z relatif)"""
        if room:
            return ry[room]
        hit = [ry[r] for r, t in R.items() if t[0] <= x <= t[1] and t[2] <= z <= t[3]]
        if not hit:
            raise SystemExit(f'zombie_layouts {name} : ({x}, {z}) hors de toute salle')
        return min(hit)

    doors = {d: (t[0], t[1], (t[2][0], zz(t[2][1]), t[2][2], zz(t[2][3])), (t[3][0], zz(t[3][1])), t[4]) for d, t in L['doors'].items()}
    door_y = {d: (t[5] if len(t) > 5 else ry[t[4]]) for d, t in L['doors'].items()}
    wins = [(t[0], t[1], zz(t[2]), t[3], t[4]) for t in L['windows']]
    win_y = [(t[5] if len(t) > 5 else ry[t[0]]) for t in L['windows']]
    walls = [wall_buy(t[0], t[1], t[2], t[3], zz(t[4]), t[5], t[6]) for t in L['wall_buys']]
    wall_y = [yat(t[3] + (1 if t[5] == 'w' else -1), t[4], t[7] if len(t) > 7 else None) for t in L['wall_buys']]
    xs = [v for (x1, x2, _, _) in rooms.values() for v in (x1, x2)]
    zs = [v for (_, _, z1, z2) in rooms.values() for v in (z1, z2)]
    area = (min(xs) - 6, min(zs) - 6, max(xs) + 6, max(zs) + 6)
    m = lambda t: machine(t[0], zz(t[1]), t[2])
    my = lambda t: yat(t[0], t[1], t[3] if len(t) > 3 else None)
    bx = L['box']
    ex = []
    for e in L.get('extra', []):
        if e[0] == 'fill':
            _, x1, y1, z1, x2, y2, z2, b = e
            ex.append(f'fill {x1} {y1} {zz(z1)} {x2} {y2} {zz(z2)} minecraft:{b}')
        else:
            _, x, y, z, b = e
            ex.append(f'setblock {x} {y} {zz(z)} minecraft:{b}')
    centers = {r: ((t[0] + t[1]) / 2, (zz(t[2]) + zz(t[3])) / 2) for r, t in R.items()}
    centers.update({r: (x, zz(z)) for r, (x, z) in L.get('centers', {}).items()})
    return dict(rooms=rooms, doors=doors, wins=wins, walls=walls, perks={k: m(v) for k, v in L['perks'].items()},
                jug=m(L['jug']), speed=m(L['speed']), box=(bx[0], zz(bx[1])),
                barrels=[(t[0], zz(t[1])) for t in L['barrels']], start=(L['start'][0], zz(L['start'][1])), area=area,
                floors=L['floors'], names=L['names'], wall=L['wall'], band=L['band'], roof=L['roof'], light=L['light'],
                ry=ry, rh=rh, top=max(ry[r] + rh[r] + 1 for r in R), extra=ex, centers=centers,
                ys=dict(doors=door_y, wins=win_y, walls=wall_y, perks={k: my(v) for k, v in L['perks'].items()},
                        jug=my(L['jug']), speed=my(L['speed']), box=yat(bx[0], bx[1], bx[2] if len(bx) > 2 else None),
                        barrels=[yat(t[0], t[1], t[2] if len(t) > 2 else None) for t in L['barrels']],
                        start=yat(*L['start'][:2], L['start'][2] if len(L['start']) > 2 else None)))
