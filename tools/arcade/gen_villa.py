"""🏠 Neo Hills : la villa des joueurs de Neo GTA, un domaine sur la colline au nord de Neo City (dimension mg:gta seulement).

    python tools/arcade/gen_villa.py .        (avant gen_gta.py : il lit tools/arcade/neo_villa.json)

Le domaine (x -44..54, z -176..-92 autour de la ville en z 32400) : plateau herbeux à y 70 relié à l'avenue 20 par une rampe
(trouée dans le mur nord de la ville), portail, allée et rond-point à fontaine, manoir moderne sur trois niveaux, garage
de cinq places, piscine à débordement et pool house, terrain de tennis, hélistation et hangar, palmiers et jardins.
Construit dans la dimension mg:gta par étapes (mg:gta/villa/pN), à la suite de la ville (mg:gta/wb_step).
Les présentoirs (garage, salle d'armes), l'ascenseur et les points de livraison sont lus par gen_gta.py dans neo_villa.json.
"""
import json
import math
import os
import random
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
F = os.path.join(R, 'data/mg/function')
Z = 32400
G = 70                                           # dessus du plateau (on marche à y 71)
X1, X2, Z1, Z2 = -44, 54, -176, -92              # emprise du domaine
random.seed(77)
CMDS = []


def fill(x1, y1, z1, x2, y2, z2, b, mode=''):
    x1, x2 = sorted((x1, x2)); y1, y2 = sorted((y1, y2)); z1, z2 = sorted((z1, z2))
    area = (x2 - x1 + 1) * (z2 - z1 + 1)
    step = max(1, 32768 // area)
    for ya in range(y1, y2 + 1, step):
        yb = min(y2, ya + step - 1)
        if (x1, ya, z1) == (x2, yb, z2):
            CMDS.append(f'setblock {x1} {ya} {Z + z1} minecraft:{b}')
        else:
            CMDS.append(f'fill {x1} {ya} {Z + z1} {x2} {yb} {Z + z2} minecraft:{b}{(" " + mode) if mode else ""}')


def put(x, y, z, b):
    CMDS.append(f'setblock {x} {y} {Z + z} minecraft:{b}')


def palm(x, z, h=None):
    h = h or random.randint(6, 9)
    dx, dz = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
    for k in range(h):
        bend = 1 if k > h * 0.6 else 0
        put(x + dx * bend, G + 1 + k, z + dz * bend, 'jungle_log')
    tx, tz, ty = x + dx, z + dz, G + h
    put(tx, ty + 1, tz, 'jungle_leaves[persistent=true]')
    for (ax, az) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        for r in range(1, 4):
            put(tx + ax * r, ty + (1 if r == 1 else 0) - (1 if r == 3 else 0), tz + az * r, 'jungle_leaves[persistent=true]')
    for (ax, az) in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
        put(tx + ax, ty, tz + az, 'jungle_leaves[persistent=true]')
        put(tx + 2 * ax, ty - 1, tz + 2 * az, 'jungle_leaves[persistent=true]')


def lamp(x, z, y=G + 1):
    put(x, y, z, 'polished_blackstone_wall'); put(x, y + 1, z, 'polished_blackstone_wall'); put(x, y + 2, z, 'lantern')


def lounger(x, z, facing='south'):
    put(x, G + 1, z, f'white_wool'); put(x, G + 1, z + (1 if facing == 'south' else -1), f'quartz_stairs[facing={facing}]')


def umbrella(x, z, col):
    fill(x, G + 1, z, x, G + 2, z, 'oak_fence')
    fill(x - 1, G + 3, z - 1, x + 1, G + 3, z + 1, f'{col}_carpet')
    put(x, G + 3, z, f'{col}_wool')


# ---------------------------------------------------------------- terrain : plateau, coteau en terrasses, rampe
for y in range(G + 25, 55, -1):                    # effacement du haut vers le bas, sans mise à jour (tapis, fleurs, lanternes ne tombent pas en objets)
    CMDS.append(f'fill {X1} {y} {Z + Z1} {X2} {y} {Z + Z2} minecraft:air strict')
fill(X1, 56, Z1, X2, G - 4, Z2 - 9, 'stone')
fill(X1, G - 3, Z1, X2, G - 1, Z2 - 9, 'dirt')
fill(X1, G, Z1, X2, G, Z2 - 9, 'grass_block')
for k in range(9):                                 # coteau vers la ville (z -100 → -92), murets de pierre
    z = Z2 - 8 + k
    top = G - round((k + 1) * 6 / 9)
    fill(X1, 56, z, X2, top - 1, z, 'stone')
    fill(X1, top, z, X2, top, z, 'grass_block' if k % 3 else 'mossy_stone_bricks')
for k in range(12):                                # rampe depuis l'avenue 20 : une demi-marche par bloc (on marche de 65,5 à 71)
    z = -89 - k
    if k % 2 == 0:
        y = 65 + k // 2
        fill(16, 56, z, 24, y - 1, z, 'stone'); fill(17, y, z, 23, y, z, 'polished_andesite_slab')
    else:
        y = 65 + (k - 1) // 2
        fill(16, 56, z, 24, y, z, 'stone'); fill(17, y, z, 23, y, z, 'polished_andesite')
    fill(16, y + 1, z, 16, y + 1, z, 'stone_brick_wall'); fill(24, y + 1, z, 24, y + 1, z, 'stone_brick_wall')
    fill(17, y + 1, z, 23, G + 10, z, 'air')
fill(17, 66, -89, 23, 75, -89, 'air')
# muret d'enceinte et réverbères
fill(X1, G + 1, Z2 - 9, X2, G + 1, Z2 - 9, 'stone_brick_wall')
fill(X1, G + 1, Z1, X2, G + 1, Z1, 'stone_brick_wall')
fill(X1, G + 1, Z1, X1, G + 1, Z2 - 9, 'stone_brick_wall'); fill(X2, G + 1, Z1, X2, G + 1, Z2 - 9, 'stone_brick_wall')
for x in range(X1 + 4, X2, 9):
    lamp(x, Z2 - 9); lamp(x, Z1)
for z in range(Z1 + 6, Z2 - 9, 9):
    lamp(X1, z); lamp(X2, z)

# ---------------------------------------------------------------- portail « NEO HILLS »
GZ = Z2 - 9                                        # ligne du portail (z -101)
fill(17, G + 1, GZ, 23, G + 1, GZ, 'air')
for x in (15, 16, 24, 25):
    fill(x, G + 1, GZ, x, G + 6, GZ, 'quartz_pillar')
fill(15, G + 7, GZ, 25, G + 7, GZ, 'smooth_quartz')
fill(16, G + 8, GZ, 24, G + 8, GZ, 'gold_block')
fill(17, G + 5, GZ, 23, G + 6, GZ, 'iron_bars')
put(15, G + 8, GZ, 'lantern'); put(25, G + 8, GZ, 'lantern')
fill(26, G + 1, GZ - 3, 28, G + 3, GZ - 1, 'white_concrete'); fill(27, G + 2, GZ - 3, 27, G + 2, GZ - 1, 'glass')   # loge du gardien
fill(26, G + 4, GZ - 3, 28, G + 4, GZ - 1, 'dark_oak_slab')

# ---------------------------------------------------------------- allée, rond-point, fontaine
fill(17, G, GZ - 1, 23, G, -106, 'polished_andesite')
CX, CZ = 20, -112                                  # centre du rond-point
for x in range(CX - 7, CX + 8):
    for z in range(CZ - 7, CZ + 8):
        d = math.hypot(x - CX, z - CZ)
        if d <= 7.4:
            put(x, G, z, 'polished_andesite' if d > 3.4 else ('smooth_quartz' if d > 2.4 else 'grass_block'))
fill(CX - 2, G, CZ - 2, CX + 2, G, CZ + 2, 'smooth_quartz')                # bassin : fond, rebord, eau à l'intérieur, colonne au centre
fill(CX - 2, G + 1, CZ - 2, CX + 2, G + 1, CZ + 2, 'smooth_quartz')
fill(CX - 1, G + 1, CZ - 1, CX + 1, G + 1, CZ + 1, 'water')
put(CX, G + 1, CZ, 'quartz_pillar'); put(CX, G + 2, CZ, 'quartz_pillar'); put(CX, G + 3, CZ, 'quartz_pillar'); put(CX, G + 4, CZ, 'sea_lantern')
fill(17, G, -119, 23, G, -123, 'polished_andesite')                       # allée jusqu'à l'entrée
fill(-20, G, -119, 17, G, -122, 'polished_andesite')                      # vers le garage

# ---------------------------------------------------------------- manoir (x 0..40, z -148..-124), garage (x -20..-1)
MX1, MX2, MZ1, MZ2 = 0, 40, -148, -124
Y0, Y1, Y2 = G + 1, G + 7, G + 13                  # rez-de-chaussée 71..76, étage 77..82, toit 83
fill(MX1, G, MZ1, MX2, G, MZ2, 'polished_diorite')
fill(MX1, Y0, MZ1, MX2, Y2, MZ2, 'white_concrete')
fill(MX1 + 1, Y0, MZ1 + 1, MX2 - 1, Y2 - 1, MZ2 - 1, 'air')
fill(MX1, Y1 - 1, MZ1, MX2, Y1 - 1, MZ2, 'smooth_quartz')                  # plancher de l'étage
fill(MX1, Y2, MZ1, MX2, Y2, MZ2, 'smooth_quartz')                          # toit
# façades vitrées (grandes baies sur deux niveaux), bandeaux noirs, bardage bois
for (ya, yb) in ((Y0 + 1, Y1 - 2), (Y1 + 1, Y2 - 2)):
    fill(MX1 + 2, ya, MZ2, MX2 - 2, yb, MZ2, 'light_blue_stained_glass')
    fill(MX1 + 2, ya, MZ1, MX2 - 2, yb, MZ1, 'light_blue_stained_glass')
    fill(MX2, ya, MZ1 + 2, MX2, yb, MZ2 - 2, 'light_blue_stained_glass')
    fill(MX1, ya, MZ1 + 2, MX1, yb, MZ2 - 2, 'light_blue_stained_glass')
for x in range(MX1, MX2 + 1, 6):
    fill(x, Y0, MZ2, x, Y2 - 1, MZ2, 'black_concrete'); fill(x, Y0, MZ1, x, Y2 - 1, MZ1, 'black_concrete')
fill(MX1, Y1 - 1, MZ2, MX2, Y1 - 1, MZ2, 'black_concrete'); fill(MX1, Y2, MZ2, MX2, Y2, MZ2, 'black_concrete')
fill(MX1 + 1, Y1, MZ2, MX1 + 11, Y2 - 1, MZ2, 'stripped_dark_oak_wood')    # bardage bois (aile ouest)
fill(MX1 + 3, Y1 + 1, MZ2, MX1 + 9, Y2 - 2, MZ2, 'gray_stained_glass')
# porte-à-faux au-dessus de l'entrée, piliers
fill(12, Y1 - 1, MZ2 + 1, 28, Y1 - 1, MZ2 + 3, 'smooth_quartz')
fill(12, Y1, MZ2 + 3, 28, Y1, MZ2 + 3, 'glass')
for x in (12, 28):
    fill(x, Y0, MZ2 + 3, x, Y1 - 2, MZ2 + 3, 'quartz_pillar')
fill(17, Y0, MZ2, 23, Y0 + 3, MZ2, 'air')                                  # grande porte vitrée ouverte
fill(16, Y0, MZ2, 16, Y0 + 4, MZ2, 'black_concrete'); fill(24, Y0, MZ2, 24, Y0 + 4, MZ2, 'black_concrete')
# hall à double hauteur : trémie dans le plancher, lustre, grand escalier
fill(15, Y1 - 1, MZ2 - 9, 25, Y1 - 1, MZ2 - 1, 'air')
fill(20, Y1 + 1, MZ2 - 5, 20, Y2 - 1, MZ2 - 5, 'iron_chain')
fill(19, Y1, MZ2 - 6, 21, Y1, MZ2 - 4, 'glass'); put(20, Y1 - 1, MZ2 - 5, 'sea_lantern')
for (ax, az) in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
    put(20 + ax, Y1, MZ2 - 5 + az, 'end_rod[facing=down]')
fill(15, G, MZ2 - 9, 25, G, MZ2 - 1, 'polished_diorite')
fill(17, Y0, MZ2 - 7, 23, Y0, MZ2 - 2, 'red_carpet')
for k in range(6):                                                          # grand escalier au fond du hall
    fill(18, Y0 + k, MZ2 - 10 - k, 22, Y0 + k, MZ2 - 10 - k, 'quartz_stairs[facing=north]')
    fill(18, Y0, MZ2 - 10 - k, 22, Y0 + k - 1, MZ2 - 10 - k, 'smooth_quartz') if k else None
fill(18, Y1 - 1, MZ2 - 16, 22, Y1 - 1, MZ2 - 16, 'smooth_quartz')
fill(18, Y1 - 1, MZ2 - 14, 22, Y1 - 1, MZ2 - 10, 'air')                    # trémie au-dessus de l'escalier (hauteur sous plafond)
fill(17, Y1, MZ2 - 14, 17, Y1, MZ2 - 10, 'glass'); fill(23, Y1, MZ2 - 14, 23, Y1, MZ2 - 10, 'glass')   # garde-corps à l'étage
fill(17, Y1, MZ2 - 9, 17, Y1, MZ2 - 1, 'glass'); fill(23, Y1, MZ2 - 9, 23, Y1, MZ2 - 1, 'glass')   # garde-corps de la mezzanine
# cloisons du rez-de-chaussée
fill(14, Y0, MZ1 + 1, 14, Y1 - 2, MZ2 - 1, 'white_concrete'); fill(26, Y0, MZ1 + 1, 26, Y1 - 2, MZ2 - 1, 'white_concrete')
fill(14, Y0, MZ2 - 6, 14, Y0 + 2, MZ2 - 4, 'air'); fill(26, Y0, MZ2 - 6, 26, Y0 + 2, MZ2 - 4, 'air')
fill(15, Y0, MZ1 + 9, 25, Y1 - 2, MZ1 + 9, 'white_concrete'); fill(23, Y0, MZ1 + 9, 25, Y0 + 2, MZ1 + 9, 'air')   # porte de la salle d'armes, à côté de l'escalier
# salon (est) : canapés en L, table basse, mur télé, cheminée, tapis, plantes
fill(28, Y0 - 1, MZ2 - 18, 38, Y0 - 1, MZ2 - 2, 'dark_oak_planks')
fill(29, Y0, MZ2 - 12, 37, Y0, MZ2 - 6, 'light_gray_carpet')
fill(29, Y0, MZ2 - 13, 37, Y0, MZ2 - 13, 'gray_wool'); fill(29, Y0 + 1, MZ2 - 14, 37, Y0 + 1, MZ2 - 14, 'gray_wool')
fill(29, Y0, MZ2 - 12, 29, Y0, MZ2 - 7, 'gray_wool')
fill(32, Y0, MZ2 - 10, 34, Y0, MZ2 - 9, 'spruce_slab')
fill(30, Y0 + 1, MZ2 - 2, 36, Y0 + 3, MZ2 - 2, 'black_concrete')
fill(31, Y0 + 2, MZ2 - 2, 35, Y0 + 2, MZ2 - 2, 'black_stained_glass')
put(30, Y0 + 4, MZ2 - 2, 'sea_lantern'); put(36, Y0 + 4, MZ2 - 2, 'sea_lantern')
fill(MX2 - 1, Y0, MZ2 - 12, MX2 - 1, Y0 + 3, MZ2 - 8, 'bricks'); fill(MX2 - 1, Y0, MZ2 - 11, MX2 - 1, Y0 + 1, MZ2 - 9, 'air')
put(MX2 - 1, Y0, MZ2 - 10, 'campfire[lit=true]')
for (x, z) in [(27, MZ2 - 1), (39, MZ2 - 16), (27, MZ1 + 1)]:
    put(x, Y0, z, 'potted_bamboo')
for x in range(30, 38, 4):
    put(x, Y1 - 2, MZ2 - 8, 'sea_lantern')
# cuisine et salle à manger (ouest) : plans de travail, îlot, frigo, fours, évier, longue table
fill(1, Y0, MZ1 + 1, 13, Y0, MZ1 + 1, 'white_concrete'); fill(1, Y0 + 1, MZ1 + 1, 13, Y0 + 1, MZ1 + 1, 'smooth_quartz_slab')
put(3, Y0, MZ1 + 1, 'smoker'); put(4, Y0, MZ1 + 1, 'furnace'); put(6, Y0 + 1, MZ1 + 1, 'water_cauldron[level=3]')
fill(12, Y0, MZ1 + 1, 13, Y0 + 2, MZ1 + 1, 'iron_block')
fill(4, Y0, MZ1 + 5, 10, Y0, MZ1 + 6, 'white_concrete'); fill(4, Y0 + 1, MZ1 + 5, 10, Y0 + 1, MZ1 + 6, 'smooth_quartz_slab')
for x in range(4, 11, 2):
    put(x, Y0, MZ1 + 7, 'dark_oak_stairs[facing=north]')
fill(4, Y0, MZ2 - 10, 10, Y0, MZ2 - 10, 'dark_oak_fence'); fill(4, Y0 + 1, MZ2 - 10, 10, Y0 + 1, MZ2 - 10, 'dark_oak_slab')
fill(4, Y0 + 1, MZ2 - 11, 10, Y0 + 1, MZ2 - 9, 'air')
fill(4, Y0, MZ2 - 11, 10, Y0, MZ2 - 11, 'dark_oak_stairs[facing=south]'); fill(4, Y0, MZ2 - 9, 10, Y0, MZ2 - 9, 'dark_oak_stairs[facing=north]')
fill(4, Y0, MZ2 - 10, 10, Y0, MZ2 - 10, 'dark_oak_fence'); fill(4, Y0 + 1, MZ2 - 10, 10, Y0 + 1, MZ2 - 10, 'dark_oak_slab')
put(7, Y0 + 2, MZ2 - 10, 'candle[lit=true,candles=3]')
for x in (4, 7, 10):
    put(x, Y1 - 2, MZ2 - 10, 'sea_lantern')
# bar (fond du hall) : comptoir, bouteilles, tabourets
fill(15, Y0, MZ2 - 9, 15, Y0, MZ2 - 7, 'dark_oak_planks'); fill(15, Y0 + 1, MZ2 - 9, 15, Y0 + 1, MZ2 - 7, 'polished_blackstone_slab')   # bar contre le mur ouest du hall
put(15, Y0 + 2, MZ2 - 9, 'brewing_stand'); put(15, Y0 + 2, MZ2 - 7, 'brewing_stand')
for k in range(6):                                                          # main courante vitrée de l'escalier
    put(17, Y0 + k + 1, MZ2 - 10 - k, 'glass'); put(23, Y0 + k + 1, MZ2 - 10 - k, 'glass')
# salle d'armes (derrière le bar, nord du hall) : râteliers et tapis rouge (présentoirs posés par Neo GTA)
fill(15, Y0 - 1, MZ1 + 1, 25, Y0 - 1, MZ1 + 8, 'polished_deepslate')
fill(15, Y0, MZ1 + 1, 25, Y0, MZ1 + 1, 'red_carpet')
for x in range(15, 26, 2):
    fill(x, Y0 + 1, MZ1 + 1, x, Y0 + 3, MZ1 + 1, 'iron_bars')
fill(15, Y1 - 2, MZ1 + 4, 25, Y1 - 2, MZ1 + 4, 'redstone_lamp[lit=true]')
# étage : suite parentale (est), cinéma (ouest), salle de jeux et sport (centre)
fill(14, Y1, MZ1 + 1, 14, Y2 - 1, MZ2 - 1, 'white_concrete'); fill(26, Y1, MZ1 + 1, 26, Y2 - 1, MZ2 - 1, 'white_concrete')
fill(14, Y1, MZ2 - 12, 14, Y1 + 2, MZ2 - 11, 'air'); fill(26, Y1, MZ2 - 12, 26, Y1 + 2, MZ2 - 11, 'air')
fill(31, Y1, MZ2 - 12, 35, Y1, MZ2 - 9, 'white_wool'); fill(31, Y1, MZ2 - 13, 35, Y1 + 2, MZ2 - 13, 'dark_oak_planks')   # lit king size
fill(31, Y1, MZ2 - 12, 35, Y1, MZ2 - 12, 'red_wool')
put(30, Y1, MZ2 - 13, 'barrel'); put(36, Y1, MZ2 - 13, 'barrel'); put(30, Y1 + 1, MZ2 - 13, 'lantern'); put(36, Y1 + 1, MZ2 - 13, 'lantern')
fill(28, Y1, MZ1 + 1, 38, Y1 + 3, MZ1 + 1, 'barrel')                                                                     # dressing
fill(36, Y1, MZ1 + 4, 39, Y1, MZ1 + 6, 'smooth_quartz'); fill(37, Y1, MZ1 + 5, 38, Y1, MZ1 + 5, 'water_cauldron[level=3]')  # baignoire
fill(28, Y1, MZ2 - 6, 38, Y1, MZ2 - 2, 'white_carpet')
fill(MX2 + 1, Y1 - 1, MZ2 - 12, MX2 + 3, Y1 - 1, MZ2 - 4, 'smooth_quartz'); fill(MX2 + 3, Y1, MZ2 - 12, MX2 + 3, Y1, MZ2 - 4, 'glass')  # balcon
fill(MX2, Y1, MZ2 - 9, MX2, Y1 + 2, MZ2 - 7, 'air')
fill(1, Y1, MZ1 + 1, 13, Y2 - 1, MZ2 - 1, 'black_wool'); fill(2, Y1, MZ1 + 2, 12, Y2 - 2, MZ2 - 2, 'air')                   # cinéma
fill(2, Y1, MZ2 - 2, 13, Y2 - 1, MZ2 - 2, 'black_wool'); fill(13, Y1, MZ2 - 12, 13, Y1 + 2, MZ2 - 11, 'air')
fill(3, Y1 + 1, MZ1 + 2, 11, Y2 - 2, MZ1 + 2, 'white_concrete'); fill(3, Y2 - 1, MZ1 + 2, 11, Y2 - 1, MZ1 + 2, 'sea_lantern')
for k, z in enumerate(range(MZ1 + 7, MZ2 - 3, 3)):
    fill(3, Y1, z, 11, Y1, z, 'red_wool'); fill(3, Y1, z + 1, 11, Y1, z + 1, 'red_wool')
    fill(3, Y1 + 1, z + 1, 11, Y1 + 1, z + 1, 'black_wool')
fill(18, Y1, MZ1 + 4, 22, Y1, MZ1 + 6, 'dark_oak_planks'); fill(18, Y1 + 1, MZ1 + 4, 22, Y1 + 1, MZ1 + 6, 'green_carpet')   # billard
fill(15, Y1, MZ1 + 1, 25, Y1 + 3, MZ1 + 1, 'bookshelf')
put(16, Y1, MZ2 - 12, 'anvil'); put(24, Y1, MZ2 - 12, 'anvil')                                                             # salle de sport
fill(16, Y1, MZ2 - 14, 18, Y1, MZ2 - 14, 'black_concrete'); fill(22, Y1, MZ2 - 14, 24, Y1, MZ2 - 14, 'black_concrete')
for x in range(16, 25, 4):
    put(x, Y2 - 1, MZ1 + 5, 'sea_lantern')
# toit-terrasse : jacuzzi, transats, bar, garde-corps vitré
fill(MX1, Y2 + 1, MZ1, MX2, Y2 + 1, MZ1, 'glass'); fill(MX1, Y2 + 1, MZ2, MX2, Y2 + 1, MZ2, 'glass')
fill(MX1, Y2 + 1, MZ1, MX1, Y2 + 1, MZ2, 'glass'); fill(MX2, Y2 + 1, MZ1, MX2, Y2 + 1, MZ2, 'glass')
fill(30, Y2 + 1, MZ1 + 4, 36, Y2 + 1, MZ1 + 9, 'smooth_quartz'); fill(31, Y2 + 1, MZ1 + 5, 35, Y2 + 1, MZ1 + 8, 'water')
fill(31, Y2, MZ1 + 5, 35, Y2, MZ1 + 8, 'sea_lantern')
for x in range(4, 26, 3):
    put(x, Y2 + 1, MZ2 - 4, 'white_wool'); put(x, Y2 + 1, MZ2 - 3, 'quartz_stairs[facing=south]')
fill(4, Y2 + 1, MZ1 + 4, 12, Y2 + 1, MZ1 + 4, 'dark_oak_planks'); fill(4, Y2 + 2, MZ1 + 4, 12, Y2 + 2, MZ1 + 4, 'polished_blackstone_slab')
for x in (8, 22, 34):
    fill(x, Y2 + 1, MZ2 - 8, x, Y2 + 2, MZ2 - 8, 'oak_fence'); fill(x - 1, Y2 + 3, MZ2 - 9, x + 1, Y2 + 3, MZ2 - 7, 'white_carpet')
    put(x, Y2 + 3, MZ2 - 8, 'white_wool')
# garage (x -20..-1, z -140..-124) : 5 places, porte sur l'allée
GX1, GX2, GZ1, GZ2 = -20, -1, -140, -124
fill(GX1, G, GZ1, GX2, G, GZ2, 'smooth_quartz')
fill(GX1, Y0, GZ1, GX2, Y0 + 5, GZ2, 'light_gray_concrete'); fill(GX1 + 1, Y0, GZ1 + 1, GX2 - 1, Y0 + 4, GZ2 - 1, 'air')
fill(GX1, Y0 + 5, GZ1, GX2, Y0 + 5, GZ2, 'gray_concrete')
fill(GX1 + 2, Y0, GZ2, GX2 - 2, Y0 + 3, GZ2, 'air'); fill(GX1 + 1, Y0 + 4, GZ2, GX2 - 1, Y0 + 4, GZ2, 'black_concrete')
for x in range(GX1 + 3, GX2 - 1, 3):
    fill(x, Y0 - 1, GZ1 + 2, x, Y0 - 1, GZ2 - 2, 'yellow_concrete')
    put(x, Y0 + 4, (GZ1 + GZ2) // 2, 'sea_lantern')
fill(GX2, Y0, GZ2 - 8, MX1, Y0 + 2, GZ2 - 6, 'air')                         # passage garage → cuisine (à travers les deux murs)
fill(GX2, Y0 + 3, GZ2 - 9, MX1, Y0 + 3, GZ2 - 5, 'smooth_quartz'); fill(GX2, Y0, GZ2 - 9, MX1, Y0 + 2, GZ2 - 9, 'smooth_quartz')
fill(GX2, Y0, GZ2 - 5, MX1, Y0 + 2, GZ2 - 5, 'smooth_quartz')

# ---------------------------------------------------------------- piscine à débordement, plage, pool house (derrière le manoir)
PX1, PX2, PZ1, PZ2 = 4, 36, -166, -156
fill(PX1 - 2, G, PZ1 - 3, PX2 + 2, G, PZ2 + 6, 'smooth_quartz')            # plage
fill(PX1, G - 3, PZ1, PX2, G, PZ2, 'smooth_quartz'); fill(PX1 + 1, G - 2, PZ1 + 1, PX2 - 1, G, PZ2 - 1, 'water')
fill(PX1 + 1, G - 3, PZ1 + 1, PX2 - 1, G - 3, PZ2 - 1, 'light_blue_concrete')
for x in range(PX1 + 3, PX2, 6):
    put(x, G - 2, PZ1, 'sea_lantern'); put(x, G - 2, PZ2, 'sea_lantern')
fill(PX2 - 4, G + 1, PZ2 + 1, PX2 - 4, G + 1, PZ2 + 2, 'birch_slab')       # plongeoir
for k, x in enumerate(range(PX1, PX2 + 1, 4)):
    lounger(x, PZ2 + 3)
    if k % 2 == 0:
        umbrella(x + 2, PZ2 + 5, ['red', 'white', 'yellow', 'light_blue'][k // 2 % 4])
fill(PX2 + 4, G + 1, PZ1 - 1, PX2 + 12, G + 4, PZ2 + 1, 'white_concrete')   # pool house
fill(PX2 + 5, G + 1, PZ1, PX2 + 11, G + 3, PZ2, 'air')
fill(PX2 + 4, G + 1, PZ1 + 3, PX2 + 4, G + 3, PZ2 - 3, 'air')
fill(PX2 + 4, G + 5, PZ1 - 2, PX2 + 12, G + 5, PZ2 + 2, 'dark_oak_slab')
fill(PX2 + 6, G + 1, PZ1 + 1, PX2 + 10, G + 1, PZ1 + 1, 'dark_oak_planks'); fill(PX2 + 6, G + 2, PZ1 + 1, PX2 + 10, G + 2, PZ1 + 1, 'polished_blackstone_slab')
put(PX2 + 8, G + 3, PZ1 + 1, 'brewing_stand')

# ---------------------------------------------------------------- tennis (ouest, derrière le garage), hélistation et hangar (avant ouest)
TX1, TX2, TZ1, TZ2 = -40, -24, -170, -146
fill(TX1, G, TZ1, TX2, G, TZ2, 'green_concrete')
for (a, b, c, d) in [(TX1, TZ1, TX2, TZ1), (TX1, TZ2, TX2, TZ2), (TX1, TZ1, TX1, TZ2), (TX2, TZ1, TX2, TZ2), (TX1, -158, TX2, -158),
                     ((TX1 + TX2) // 2, TZ1 + 6, (TX1 + TX2) // 2, TZ2 - 6)]:
    fill(a, G, b, c, G, d, 'white_concrete')
fill(TX1, G + 1, -158, TX2, G + 1, -158, 'iron_bars')
fill(TX1 - 1, G + 1, TZ1 - 1, TX2 + 1, G + 3, TZ1 - 1, 'iron_bars'); fill(TX1 - 1, G + 1, TZ2 + 1, TX2 + 1, G + 3, TZ2 + 1, 'iron_bars')
fill(TX1 - 1, G + 1, TZ1 - 1, TX1 - 1, G + 3, TZ2 + 1, 'iron_bars'); fill(TX2 + 1, G + 1, TZ1 - 1, TX2 + 1, G + 3, TZ2 + 1, 'iron_bars')
fill(TX2 + 1, G + 1, -152, TX2 + 1, G + 2, -150, 'air')
HX_, HZ_ = -30, -114                                                        # hélistation
for x in range(HX_ - 6, HX_ + 7):
    for z in range(HZ_ - 6, HZ_ + 7):
        if math.hypot(x - HX_, z - HZ_) <= 6.4:
            put(x, G, z, 'gray_concrete')
fill(HX_ - 2, G, HZ_ - 3, HX_ - 2, G, HZ_ + 3, 'yellow_concrete'); fill(HX_ + 2, G, HZ_ - 3, HX_ + 2, G, HZ_ + 3, 'yellow_concrete')
fill(HX_ - 2, G, HZ_, HX_ + 2, G, HZ_, 'yellow_concrete')
for (ax, az) in [(6, 0), (-6, 0), (0, 6), (0, -6)]:
    put(HX_ + ax, G + 1, HZ_ + az, 'redstone_lamp[lit=true]')
fill(-43, G + 1, -136, -24, G + 7, -124, 'gray_concrete'); fill(-42, G + 1, -135, -25, G + 6, -125, 'air')   # hangar
fill(-43, G, -136, -24, G, -124, 'polished_andesite')

# ---------------------------------------------------------------- jardins : palmiers, massifs, haies, gloriette
for (x, z) in [(-6, -110), (6, -106), (34, -106), (46, -112), (30, -118), (-12, -106), (44, -104), (2, -116), (48, -128), (48, -140),
               (-38, -104), (-20, -104), (40, -156), (0, -170), (40, -170), (-16, -150), (-10, -166), (46, -150)]:
    palm(x, z)
for (x, z) in [(10, -104), (30, -110), (40, -120), (-14, -114), (50, -160)]:
    fill(x - 1, G, z - 1, x + 1, G, z + 1, 'moss_block')
    for (ax, az) in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
        put(x + ax, G + 1, z + az, random.choice(['red_tulip', 'poppy', 'allium', 'oxeye_daisy', 'cornflower', 'blue_orchid']))
fill(-2, G + 1, MZ2 + 5, -2, G + 1, -112, 'azalea_leaves[persistent=true]'); fill(42, G + 1, MZ2 + 5, 42, G + 1, -112, 'azalea_leaves[persistent=true]')
GLX, GLZ = 46, -132                                                          # gloriette
for (ax, az) in [(-2, -2), (2, -2), (-2, 2), (2, 2)]:
    fill(GLX + ax, G + 1, GLZ + az, GLX + ax, G + 3, GLZ + az, 'quartz_pillar')
fill(GLX - 3, G + 4, GLZ - 3, GLX + 3, G + 4, GLZ + 3, 'smooth_quartz_slab'); fill(GLX - 1, G + 1, GLZ - 1, GLX + 1, G + 1, GLZ + 1, 'white_carpet')
for (x, z) in [(12, -104), (28, -104), (-6, -122), (46, -122), (4, -152), (36, -152), (-22, -145), (-36, -110), (-24, -110)]:
    lamp(x, z)

# ---------------------------------------------------------------- détails (façade, pièces, toit, jardin)
FLOWERS = ['red_tulip', 'white_tulip', 'pink_tulip', 'allium', 'oxeye_daisy', 'cornflower', 'azure_bluet', 'lily_of_the_valley']
# façade sud : jardinières, appliques, spots sous le porte-à-faux, lames de bois sur les côtés
for x in range(MX1 + 1, MX2):
    if not 11 <= x <= 29:
        put(x, G + 1, MZ2 + 1, 'moss_block'); put(x, G + 2, MZ2 + 1, random.choice(FLOWERS))
for x in range(MX1 + 3, MX2, 6):
    if not 15 <= x <= 25:
        put(x, Y1 - 2, MZ2 + 1, 'end_rod[facing=south]'); put(x, Y2 - 2, MZ2 + 1, 'end_rod[facing=south]')
for x in (14, 18, 22, 26):
    put(x, Y1 - 1, MZ2 + 2, 'sea_lantern')
for z in range(MZ1 + 2, MZ2 - 1, 3):
    fill(MX2 + 1, Y1 + 1, z, MX2 + 1, Y2 - 1, z, 'stripped_dark_oak_log')
    fill(MX1 - 1, Y1 + 1, z, MX1 - 1, Y2 - 1, z, 'stripped_dark_oak_log')
# hall : damier de marbre, grandes plantes, tableaux en céramique, pampilles du lustre
for x in range(15, 26):
    for z in range(MZ2 - 9, MZ2):
        if not (17 <= x <= 23 and MZ2 - 7 <= z <= MZ2 - 2):
            put(x, G, z, 'polished_diorite' if (x + z) % 2 else 'smooth_quartz')
put(15, Y0, MZ2 - 1, 'potted_flowering_azalea_bush'); put(25, Y0, MZ2 - 1, 'potted_flowering_azalea_bush')
put(24, Y0, MZ2 - 1, 'potted_bamboo'); put(25, Y0, MZ2 - 8, 'decorated_pot')
fill(14, Y0 + 1, MZ2 - 3, 14, Y0 + 3, MZ2 - 2, 'cyan_glazed_terracotta'); fill(26, Y0 + 1, MZ2 - 3, 26, Y0 + 3, MZ2 - 2, 'magenta_glazed_terracotta')
for (ax, az) in [(-2, -2), (2, -2), (-2, 2), (2, 2)]:
    fill(20 + ax, Y1 + 2, MZ2 - 5 + az, 20 + ax, Y2 - 1, MZ2 - 5 + az, 'iron_chain')
    put(20 + ax, Y1 + 1, MZ2 - 5 + az, 'lantern[hanging=true]')
# salon : aquarium encastré, bibliothèque, piano à queue, lampadaires, coussins
fill(28, Y0, MZ1 + 1, 34, Y0 + 3, MZ1 + 2, 'glass')
fill(29, Y0 + 1, MZ1 + 1, 33, Y0 + 2, MZ1 + 1, 'water')
put(29, Y0 + 1, MZ1 + 1, 'sea_pickle[waterlogged=true,pickles=3]'); put(31, Y0 + 1, MZ1 + 1, 'kelp_plant'); put(31, Y0 + 2, MZ1 + 1, 'kelp')
put(33, Y0 + 1, MZ1 + 1, 'brain_coral_block'); put(32, Y0 + 1, MZ1 + 1, 'tube_coral[waterlogged=true]'); put(30, Y0 + 1, MZ1 + 1, 'fire_coral[waterlogged=true]')
fill(26, Y0, MZ1 + 2, 26, Y0 + 3, MZ1 + 7, 'bookshelf')
fill(36, Y0, MZ1 + 1, 38, Y0, MZ1 + 2, 'black_concrete'); fill(36, Y0 + 1, MZ1 + 1, 38, Y0 + 1, MZ1 + 1, 'black_concrete')
fill(36, Y0 + 1, MZ1 + 2, 38, Y0 + 1, MZ1 + 2, 'smooth_quartz_slab'); put(37, Y0, MZ1 + 3, 'dark_oak_slab')
for (x, z) in [(28, MZ2 - 1), (38, MZ2 - 1)]:
    put(x, Y0, z, 'polished_blackstone_wall'); put(x, Y0 + 1, z, 'polished_blackstone_wall'); put(x, Y0 + 2, z, 'end_rod[facing=up]')
put(33, Y0 + 1, MZ2 - 10, 'potted_red_tulip')
# cuisine et salle à manger : suspensions au-dessus de l'îlot, poteries, lustre de la table
for x in range(5, 11, 2):
    put(x, Y1 - 2, MZ1 + 5, 'iron_chain'); put(x, Y1 - 3, MZ1 + 5, 'lantern[hanging=true]')
put(2, Y0 + 2, MZ1 + 1, 'decorated_pot'); put(9, Y0 + 2, MZ1 + 1, 'flower_pot'); put(11, Y0 + 2, MZ1 + 1, 'potted_cactus')
for x in (5, 7, 9):
    put(x, Y1 - 2, MZ2 - 10, 'iron_chain'); put(x, Y1 - 3, MZ2 - 10, 'lantern[hanging=true]')
# garage : établi d'outils, pont élévateur, piles de pneus, taches d'huile, enseigne
put(GX1 + 2, Y0 + 1, GZ1 + 1, 'crafting_table'); put(GX1 + 3, Y0 + 1, GZ1 + 1, 'smithing_table'); put(GX1 + 4, Y0 + 1, GZ1 + 1, 'grindstone')
put(GX1 + 5, Y0 + 1, GZ1 + 1, 'anvil'); put(GX1 + 6, Y0 + 1, GZ1 + 1, 'stonecutter'); put(GX1 + 7, Y0 + 1, GZ1 + 1, 'lantern')
fill(GX1 + 2, Y0 + 2, GZ1 + 1, GX1 + 7, Y0 + 3, GZ1 + 1, 'iron_bars')
for (x, z) in [(GX1 + 1, GZ1 + 3), (GX1 + 1, GZ1 + 4), (GX2 - 1, GZ1 + 3)]:
    fill(x, Y0, z, x, Y0 + 2, z, 'black_concrete')
fill(GX2 - 7, Y0, GZ1 + 4, GX2 - 7, Y0 + 3, GZ1 + 4, 'iron_block'); fill(GX2 - 3, Y0, GZ1 + 4, GX2 - 3, Y0 + 3, GZ1 + 4, 'iron_block')
fill(GX2 - 7, Y0 + 3, GZ1 + 4, GX2 - 3, Y0 + 3, GZ1 + 4, 'iron_bars')
for (x, z) in [(GX1 + 4, GZ2 - 6), (GX1 + 9, GZ2 - 8), (GX1 + 14, GZ2 - 5)]:
    put(x, Y0, z, 'black_carpet')
fill(GX1 + 6, Y0 + 4, GZ2, GX1 + 13, Y0 + 4, GZ2, 'red_concrete')
# étage : salle de bain (vasques, douche vitrée), allée éclairée et pop-corn au cinéma, arcade et fléchettes, sport
put(30, Y1, MZ1 + 3, 'smooth_quartz'); put(32, Y1, MZ1 + 3, 'smooth_quartz')
put(30, Y1 + 1, MZ1 + 3, 'water_cauldron[level=3]'); put(32, Y1 + 1, MZ1 + 3, 'water_cauldron[level=3]')
fill(36, Y1, MZ1 + 7, 39, Y1 + 3, MZ1 + 7, 'glass'); fill(36, Y1 + 3, MZ1 + 4, 39, Y1 + 3, MZ1 + 6, 'white_stained_glass')
put(39, Y1, MZ1 + 9, 'potted_fern'); put(28, Y1, MZ2 - 2, 'potted_fern')
fill(7, Y1, MZ1 + 7, 7, Y1 + 2, MZ2 - 3, 'air')
for z in range(MZ1 + 7, MZ2 - 2, 2):
    put(7, Y1 - 1, z, 'sea_lantern')
put(12, Y1, MZ2 - 4, 'red_concrete'); put(12, Y1 + 1, MZ2 - 4, 'glass'); put(12, Y1 + 2, MZ2 - 4, 'red_concrete'); put(12, Y1 + 1, MZ2 - 5, 'yellow_concrete')
for (x, col) in [(16, 'lime'), (24, 'magenta')]:
    put(x, Y1, MZ1 + 9, 'black_concrete'); put(x, Y1 + 1, MZ1 + 9, f'{col}_stained_glass'); put(x, Y1 + 2, MZ1 + 9, 'black_concrete')
put(14, Y1 + 1, MZ1 + 4, 'target')
fill(16, Y1, MZ2 - 6, 17, Y1, MZ2 - 3, 'blue_carpet')
put(24, Y1, MZ2 - 4, 'anvil'); put(24, Y1, MZ2 - 6, 'anvil')
# toit : salon d'extérieur, brasero, jardinières, guirlandes
fill(14, Y2 + 1, MZ1 + 11, 16, Y2 + 1, MZ1 + 13, 'polished_blackstone_bricks'); put(15, Y2 + 1, MZ1 + 12, 'campfire[lit=true]')
fill(12, Y2 + 1, MZ1 + 10, 18, Y2 + 1, MZ1 + 10, 'gray_wool'); fill(12, Y2 + 1, MZ1 + 14, 18, Y2 + 1, MZ1 + 14, 'gray_wool')
for (x, z) in [(MX1 + 1, MZ1 + 1), (MX2 - 1, MZ1 + 1), (MX1 + 1, MZ2 - 1), (MX2 - 1, MZ2 - 1), (20, MZ1 + 1), (20, MZ2 - 1)]:
    put(x, Y2 + 1, z, 'moss_block'); put(x, Y2 + 2, z, 'flowering_azalea')
for x in range(MX1 + 2, MX2, 4):
    put(x, Y2 + 2, MZ1, 'end_rod[facing=up]'); put(x, Y2 + 2, MZ2, 'end_rod[facing=up]')
# jardin : bassin à carpes, barbecue près de la piscine, échelle de la piscine, pas japonais
for x in range(40, 46):
    for z in range(-148, -143):
        if math.hypot((x - 42.5) / 3.2, (z + 145.5) / 2.6) <= 1:
            put(x, G - 1, z, 'water'); put(x, G, z, 'water')
put(41, G + 1, -146, 'lily_pad'); put(43, G + 1, -145, 'lily_pad'); put(44, G + 1, -146, 'mossy_cobblestone')
put(PX1 - 3, G + 1, PZ1 + 3, 'smoker'); put(PX1 - 3, G + 1, PZ1 + 4, 'polished_blackstone'); put(PX1 - 3, G + 2, PZ1 + 4, 'iron_bars')
put(PX1 - 3, G + 1, PZ1 + 5, 'smooth_quartz'); put(PX1 - 3, G + 2, PZ1 + 5, 'flower_pot')
fill(PX1 + 1, G - 2, PZ1 + 5, PX1 + 1, G, PZ1 + 5, 'ladder[facing=east,waterlogged=true]')
for z in range(MZ2 + 1, -150, -3):
    put(43, G, z, 'smooth_stone_slab')

# ---------------------------------------------------------------- étapes de construction
import re as _re


def volume(c):                                     # nombre de blocs touchés par une commande
    m = _re.match(r'fill (-?\d+) (-?\d+) (-?\d+) (-?\d+) (-?\d+) (-?\d+)', c)
    if not m:
        return 1
    a = list(map(int, m.groups()))
    return (abs(a[3] - a[0]) + 1) * (abs(a[4] - a[1]) + 1) * (abs(a[5] - a[2]) + 1)


parts, cur, vol = [], [], 0                        # étapes de 60 000 blocs au plus (au plus 70 commandes) : ticks légers
for c in CMDS:
    v = volume(c)
    if cur and (vol + v > 60000 or len(cur) >= 70):
        parts.append(cur); cur, vol = [], 0
    cur.append(c); vol += v
if cur:
    parts.append(cur)
os.makedirs(os.path.join(F, 'gta/villa'), exist_ok=True)
for f in os.listdir(os.path.join(F, 'gta/villa')):
    os.remove(os.path.join(F, 'gta/villa', f))
for i, p in enumerate(parts, 1):
    with open(os.path.join(F, 'gta/villa', f'p{i}.mcfunction'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join([f'# Neo Hills, étape {i}/{len(parts)} (généré par tools/arcade/gen_villa.py ; contexte : dimension mg:gta)'] + p) + '\n')

DATA = {
    'parts': len(parts), 'area': [X1, Z1, X2, Z2], 'ground': G,
    'front': [20, -103],                                     # arrivée : derrière le portail
    'garage_pads': [[x, GZ2 - 3] for x in range(GX1 + 3, GX2 - 1, 3)][:5],
    'weapon_pads': [[x, MZ1 + 3] for x in range(15, 26, 2)][:6],
    'heal_pad': [17, MZ2 - 3], 'armor_pad': [23, MZ2 - 3],
    'lift_up': [25, MZ2 - 11], 'lift_y': [Y0, Y2 + 1],
    'car_drop': [[-16, -121], [-10, -121], [-4, -121]],
    'heli': [HX_, HZ_], 'plane': [-33, -130],
    'sign': [20, GZ], 'mansion': [MX1, MZ1, MX2, MZ2],
}
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'neo_villa.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump(DATA, f, indent=1)
    f.write('\n')
print(f'Neo Hills OK : {len(CMDS)} commandes en {len(parts)} étapes')
