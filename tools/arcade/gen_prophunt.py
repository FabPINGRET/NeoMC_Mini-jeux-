"""🎭 Prop Hunt (id 96). Quatre cartes tirées au sort à chaque partie : Manoir (z 23600), Entrepôt du port (z 23700),
Supermarché (z 23800), Serre (z 23900).

    python tools/arcade/gen_prophunt.py .

Cacheurs : invisibles et rapetissés, ils prennent l'apparence d'un objet (block_display qui les suit). Regarder un objet
du manoir et s'accroupir = se transformer en cet objet. Immobile 2 s = l'objet se cale sur la grille (verrouillé).
Toutes les 20 s, chaque cacheur fait un bruit ; il peut aussi en faire quand il veut avec sa corne (clic droit). Cacheurs : 5 cœurs (2 coups d'épée). Chercheurs : enfermés et aveugles pendant 30 s, puis 3 min 30 de chasse.
Frapper un objet suspect touche le cacheur (interaction autour de l'objet). Cacheur tué = devient chercheur.
Il reste un cacheur à la fin → les cacheurs gagnent ; plus aucun → les chercheurs gagnent.
Points des cacheurs (mg.phpt), pendant la chasse : +2 tous les quarts de seconde où un chercheur le regarde (24 blocs, sans mur entre),
+1 tous les quarts de seconde où il bouge. Classement et meilleur cacheur annoncés à la fin.
Seul : mode entraînement (pas de victoire, fin au chrono ou menu → Arrêter).
"""
import random
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
Z = 23600
HIDE, HUNT = 600, 4200
PROPS = ['barrel', 'crafting_table', 'bookshelf', 'hay_block', 'pumpkin', 'carved_pumpkin', 'melon', 'composter', 'cauldron', 'lantern',
         'anvil', 'furnace', 'smoker', 'loom', 'fletching_table', 'smithing_table', 'cartography_table', 'beehive', 'jukebox', 'note_block',
         'cake', 'brewing_stand', 'grindstone', 'stonecutter', 'potted_red_tulip', 'oak_leaves', 'cobweb', 'target', 'lectern', 'blast_furnace',
         'dried_kelp_block', 'sponge', 'iron_block', 'oxidized_copper', 'blue_wool', 'tnt', 'honey_block', 'red_wool', 'yellow_wool', 'white_wool',
         'packed_ice', 'blue_ice', 'moss_block', 'azalea', 'flowering_azalea', 'potted_fern']
PID = {p: i + 1 for i, p in enumerate(PROPS)}
ROOMS = [  # (x1, x2, z1, z2, sol, objets)
    (-19, -8, Z - 14, Z - 1, 'spruce_planks', ['furnace', 'smoker', 'cauldron', 'barrel', 'crafting_table', 'cake', 'blast_furnace', 'potted_red_tulip']),
    (-6, 6, Z - 14, Z - 1, 'oak_planks', ['bookshelf', 'lectern', 'lantern', 'potted_red_tulip', 'cartography_table', 'jukebox']),
    (8, 19, Z - 14, Z - 1, 'stone_bricks', ['anvil', 'grindstone', 'smithing_table', 'fletching_table', 'stonecutter', 'loom', 'barrel']),
    (-19, -8, Z + 1, Z + 14, 'dark_oak_planks', ['hay_block', 'pumpkin', 'carved_pumpkin', 'melon', 'composter', 'barrel', 'cobweb']),
    (-6, 6, Z + 1, Z + 14, 'birch_planks', ['jukebox', 'note_block', 'lantern', 'cake', 'potted_red_tulip', 'bookshelf', 'target']),
    (8, 19, Z + 1, Z + 14, 'moss_block', ['beehive', 'oak_leaves', 'potted_red_tulip', 'composter', 'target', 'pumpkin', 'hay_block']),
]

# ------------------------------------------------------------------ manoir
rnd = random.Random(96)
L = ['# 🎭 Manoir du Prop Hunt — x −20..20, z 23585..23615, sol y 80, toit y 87 ; cage des chercheurs sur le toit']
L += [f'fill -23 {y} {Z - 18} 23 {y} {Z + 18} minecraft:air' for y in range(78, 96)]
L += [f'fill -20 79 {Z - 15} 20 79 {Z + 15} minecraft:stone']
for (x1, x2, z1, z2, fl, _) in ROOMS:
    L.append(f'fill {x1 - 1} 80 {z1 - 1} {x2 + 1} 80 {z2 + 1} minecraft:{fl}')
L += [f'fill -20 80 {Z - 15} 20 86 {Z - 15} minecraft:stripped_oak_log', f'fill -20 80 {Z + 15} 20 86 {Z + 15} minecraft:stripped_oak_log',
      f'fill -20 80 {Z - 14} -20 86 {Z + 14} minecraft:stripped_oak_log', f'fill 20 80 {Z - 14} 20 86 {Z + 14} minecraft:stripped_oak_log',
      f'fill -7 81 {Z - 14} -7 86 {Z + 14} minecraft:white_terracotta', f'fill 7 81 {Z - 14} 7 86 {Z + 14} minecraft:white_terracotta',
      f'fill -19 81 {Z} 19 86 {Z} minecraft:white_terracotta',
      f'fill -20 87 {Z - 15} 20 87 {Z + 15} minecraft:dark_oak_planks']
# portes de 2 de large
L += [f'fill -7 81 {Z - 8} -7 83 {Z - 7} minecraft:air', f'fill -7 81 {Z + 7} -7 83 {Z + 8} minecraft:air',
      f'fill 7 81 {Z - 8} 7 83 {Z - 7} minecraft:air', f'fill 7 81 {Z + 7} 7 83 {Z + 8} minecraft:air',
      f'fill -14 81 {Z} -13 83 {Z} minecraft:air', f'fill -1 81 {Z} 0 83 {Z} minecraft:air', f'fill 13 81 {Z} 14 83 {Z} minecraft:air']
# fenêtres et éclairage
for x in range(-17, 18, 6):
    L += [f'fill {x} 82 {Z - 15} {x + 1} 84 {Z - 15} minecraft:glass_pane', f'fill {x} 82 {Z + 15} {x + 1} 84 {Z + 15} minecraft:glass_pane']
L += [f'setblock {x} 87 {z} minecraft:glowstone' for x in range(-17, 18, 5) for z in range(Z - 12, Z + 13, 5)]
# mobilier (~25 objets par pièce, parfois empilés)
door_cells = {(-8, Z - 8), (-8, Z - 7), (-6, Z - 8), (-6, Z - 7), (-8, Z + 7), (-8, Z + 8), (-6, Z + 7), (-6, Z + 8),
              (6, Z - 8), (6, Z - 7), (8, Z - 8), (8, Z - 7), (6, Z + 7), (6, Z + 8), (8, Z + 7), (8, Z + 8),
              (-14, Z - 1), (-13, Z - 1), (-14, Z + 1), (-13, Z + 1), (-1, Z - 1), (0, Z - 1), (-1, Z + 1), (0, Z + 1),
              (13, Z - 1), (14, Z - 1), (13, Z + 1), (14, Z + 1)}
used = set()
for (x1, x2, z1, z2, fl, pal) in ROOMS:
    n = 0
    tries = 0
    while n < 26 and tries < 400:
        tries += 1
        x, z = rnd.randint(x1, x2), rnd.randint(z1, z2)
        if (x, z) in door_cells or (x, z) in used or any((x + dx, z + dz) in used for dx in (-1, 0, 1) for dz in (-1, 0, 1) if rnd.random() < 0.35):
            continue
        used.add((x, z))
        p = rnd.choice(pal)
        blk = 'oak_leaves[persistent=true]' if p == 'oak_leaves' else p
        L.append(f'setblock {x} 81 {z} minecraft:{blk}')
        if p in ('barrel', 'hay_block', 'bookshelf', 'melon') and rnd.random() < 0.4:
            L.append(f'setblock {x} 82 {z} minecraft:{blk}')
        n += 1
# cage des chercheurs (sur le toit)
L += [f'fill -3 88 {Z - 3} 3 92 {Z + 3} minecraft:black_stained_glass', f'fill -2 89 {Z - 2} 2 91 {Z + 2} minecraft:air',
      f'fill -2 88 {Z - 2} 2 88 {Z + 2} minecraft:black_concrete']
w('ph/build', L)


def blk(p):
    return 'oak_leaves[persistent=true]' if p == 'oak_leaves' else p


def scatter(out, rnd, cells, n, pal, stack=False):
    """n objets de pal sur des cases (x, y, z) au hasard, rarement collés ; empilés parfois"""
    cells = list(cells)
    rnd.shuffle(cells)
    used = set()
    for (x, y, z) in cells:
        if n <= 0:
            break
        if (x, y, z) in used or any((x + dx, y, z + dz) in used for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1))) and rnd.random() < 0.7:
            continue
        used.add((x, y, z))
        p = rnd.choice(pal)
        out.append(f'setblock {x} {y} {z} minecraft:{blk(p)}')
        if stack and p in ('barrel', 'hay_block', 'dried_kelp_block', 'blue_wool', 'tnt', 'white_wool', 'red_wool', 'yellow_wool', 'melon') and rnd.random() < 0.35:
            out.append(f'setblock {x} {y + 1} {z} minecraft:{blk(p)}')
        n -= 1


def clear(out, x, z1, z2, y1, y2):
    out += [f'fill {-x} {y} {z1} {x} {y} {z2} minecraft:air' for y in range(y1, y2 + 1)]


def cage(out, Z, y):
    out += [f'fill -3 {y} {Z - 3} 3 {y + 4} {Z + 3} minecraft:black_stained_glass', f'fill -2 {y + 1} {Z - 2} 2 {y + 3} {Z + 2} minecraft:air',
            f'fill -2 {y} {Z - 2} 2 {y} {Z + 2} minecraft:black_concrete']


# ------------------------------------------------------------------ carte 2 : entrepôt du port (mezzanines, conteneurs, étagères)
Z2 = 23700
r2 = random.Random(9602)
P2 = ['barrel', 'hay_block', 'composter', 'cauldron', 'lantern', 'target', 'note_block', 'grindstone', 'crafting_table',
      'dried_kelp_block', 'sponge', 'iron_block', 'oxidized_copper', 'blue_wool', 'tnt']
L2 = [f'# 🎭 Prop Hunt, entrepôt du port : x -24..24, z {Z2 - 16}..{Z2 + 16}, sol y 80, mezzanines y 85, toit y 92']
clear(L2, 27, Z2 - 19, Z2 + 19, 78, 99)
L2 += [f'fill -24 79 {Z2 - 16} 24 79 {Z2 + 16} minecraft:stone', f'fill -24 80 {Z2 - 16} 24 80 {Z2 + 16} minecraft:smooth_stone',
       f'fill -24 80 {Z2 - 16} 24 91 {Z2 - 16} minecraft:gray_concrete', f'fill -24 80 {Z2 + 16} 24 91 {Z2 + 16} minecraft:gray_concrete',
       f'fill -24 80 {Z2 - 16} -24 91 {Z2 + 16} minecraft:gray_concrete', f'fill 24 80 {Z2 - 16} 24 91 {Z2 + 16} minecraft:gray_concrete',
       f'fill -24 92 {Z2 - 16} 24 92 {Z2 + 16} minecraft:spruce_planks']
L2 += [f'fill -23 80 {Z2 + d} 23 80 {Z2 + d} minecraft:yellow_concrete' for d in (-8, -3, 3, 8)]
L2 += [f'fill {x} 80 {Z2 + sg * 16} {x} 91 {Z2 + sg * 16} minecraft:stripped_spruce_log' for x in range(-24, 25, 6) for sg in (-1, 1)]
L2 += [f'fill {x} 80 {z} {x} 91 {z} minecraft:stripped_spruce_log' for x in (-24, 24) for z in range(Z2 - 16, Z2 + 17, 8)]
L2 += [f'fill {x} 88 {Z2 + sg * 16} {x + 1} 89 {Z2 + sg * 16} minecraft:glass_pane' for x in range(-21, 21, 6) for sg in (-1, 1)]
L2 += [f'fill -4 81 {Z2 + 16} 4 85 {Z2 + 16} minecraft:iron_bars']
L2 += [f'setblock {x} 92 {z} minecraft:sea_lantern' for x in range(-20, 21, 5) for z in range(Z2 - 14, Z2 + 15, 5)]
# mezzanines et escaliers
L2 += [f'fill -23 85 {Z2 - 15} 23 85 {Z2 - 11} minecraft:spruce_planks', f'fill -23 85 {Z2 + 11} 23 85 {Z2 + 15} minecraft:spruce_planks',
       f'fill -23 86 {Z2 - 10} 15 86 {Z2 - 10} minecraft:spruce_fence', f'fill 21 86 {Z2 - 10} 23 86 {Z2 - 10} minecraft:spruce_fence',
       f'fill -15 86 {Z2 + 10} 23 86 {Z2 + 10} minecraft:spruce_fence', f'fill -23 86 {Z2 + 10} -21 86 {Z2 + 10} minecraft:spruce_fence']
L2 += [f'setblock {x} 85 {Z2 + sg * 13} minecraft:sea_lantern' for x in range(-21, 22, 6) for sg in (-1, 1)]
for i in range(5):
    if i:
        L2 += [f'fill {16 + i} 81 {Z2 - 10} {16 + i} {80 + i} {Z2 - 10} minecraft:spruce_planks',
               f'fill {-16 - i} 81 {Z2 + 10} {-16 - i} {80 + i} {Z2 + 10} minecraft:spruce_planks']
    L2 += [f'setblock {16 + i} {81 + i} {Z2 - 10} minecraft:spruce_stairs[facing=east]', f'setblock {-16 - i} {81 + i} {Z2 + 10} minecraft:spruce_stairs[facing=west]']
# conteneurs (creux, ouverts aux deux bouts) et étagères
CONT = [(-12, -6, 'red_concrete'), (6, 12, 'blue_concrete')]
for (x1, x2, c) in CONT:
    L2 += [f'fill {x1} 81 {Z2 - 1} {x2} 83 {Z2 + 1} minecraft:{c}', f'fill {x1} 81 {Z2} {x2} 82 {Z2} minecraft:air']
RACK = [(-19, -13), (-9, -3), (3, 9), (13, 19)]
RZ = (-6, -5, 5, 6)
for (x1, x2) in RACK:
    for (z0, z1_) in ((Z2 - 6, Z2 - 5), (Z2 + 5, Z2 + 6)):
        L2 += [f'fill {x1} 83 {z0} {x2} 83 {z1_} minecraft:spruce_planks',
               f'fill {x1} 81 {z0} {x1} 82 {z1_} minecraft:spruce_fence', f'fill {x2} 81 {z0} {x2} 82 {z1_} minecraft:spruce_fence']
blocked = {(x, Z2 + d) for (x1, x2, _) in CONT for x in range(x1, x2 + 1) for d in (-1, 1)}
blocked |= {(x, Z2 + d) for (x1, x2) in RACK for x in (x1, x2) for d in RZ}
blocked |= {(16 + i, Z2 - 10) for i in range(-1, 5)} | {(-16 - i, Z2 + 10) for i in range(-1, 5)}
floor2 = [(x, 81, z) for x in range(-23, 24) for z in range(Z2 - 15, Z2 + 16) if (x, z) not in blocked]
scatter(L2, r2, floor2, 80, P2, stack=True)
scatter(L2, r2, [(x, 84, Z2 + d) for (x1, x2) in RACK for x in range(x1, x2 + 1) for d in RZ], 22, P2)
scatter(L2, r2, [(x, 84, z) for (x1, x2, _) in CONT for x in range(x1, x2 + 1) for z in range(Z2 - 1, Z2 + 2)], 8, P2)
mezz = [(x, 86, z) for x in range(-23, 24) for z in list(range(Z2 - 15, Z2 - 10)) + list(range(Z2 + 11, Z2 + 16))
        if not (z == Z2 - 11 and 15 <= x <= 21) and not (z == Z2 + 11 and -21 <= x <= -15)]
scatter(L2, r2, mezz, 26, P2, stack=True)
cage(L2, Z2, 93)
w('ph/build2', L2)

# ------------------------------------------------------------------ carte 3 : supermarché (rayons sur 3 niveaux, caisses, rayon frais)
Z3 = 23800
r3 = random.Random(9603)
P3 = ['melon', 'pumpkin', 'hay_block', 'cake', 'barrel', 'honey_block', 'red_wool', 'yellow_wool', 'white_wool', 'dried_kelp_block',
      'composter', 'lantern', 'jukebox', 'note_block', 'carved_pumpkin']
L3 = [f'# 🎭 Prop Hunt, supermarché : x -22..22, z {Z3 - 14}..{Z3 + 14}, sol y 80, plafond y 86']
clear(L3, 25, Z3 - 17, Z3 + 17, 78, 94)
L3 += [f'fill -22 79 {Z3 - 14} 22 79 {Z3 + 14} minecraft:stone']
L3 += [f'fill -22 80 {z} 22 80 {z} minecraft:{"white_concrete" if z % 2 else "light_gray_concrete"}' for z in range(Z3 - 14, Z3 + 15)]
L3 += [f'fill -22 80 {Z3 - 14} 22 85 {Z3 - 14} minecraft:white_terracotta', f'fill -22 80 {Z3 + 14} 22 85 {Z3 + 14} minecraft:white_terracotta',
       f'fill -22 80 {Z3 - 14} -22 85 {Z3 + 14} minecraft:white_terracotta', f'fill 22 80 {Z3 - 14} 22 85 {Z3 + 14} minecraft:white_terracotta',
       f'fill -22 83 {Z3 - 14} 22 83 {Z3 - 14} minecraft:red_terracotta', f'fill -22 83 {Z3 + 14} 22 83 {Z3 + 14} minecraft:red_terracotta',
       f'fill -22 83 {Z3 - 14} -22 83 {Z3 + 14} minecraft:red_terracotta', f'fill 22 83 {Z3 - 14} 22 83 {Z3 + 14} minecraft:red_terracotta',
       f'fill -22 86 {Z3 - 14} 22 86 {Z3 + 14} minecraft:white_concrete', f'fill -5 81 {Z3 + 14} 5 84 {Z3 + 14} minecraft:glass_pane']
L3 += [f'setblock {x} 86 {z} minecraft:sea_lantern' for x in range(-20, 21, 5) for z in range(Z3 - 12, Z3 + 13, 4)]
SH = [-16, -10, -4, 2, 8, 14]
for x in SH:
    L3 += [f'fill {x} 82 {Z3 - 8} {x + 1} 82 {Z3 + 3} minecraft:birch_slab[type=top]', f'fill {x} 84 {Z3 - 8} {x + 1} 84 {Z3 + 3} minecraft:birch_slab[type=top]',
           f'fill {x} 81 {Z3 - 9} {x + 1} 84 {Z3 - 9} minecraft:birch_fence', f'fill {x} 81 {Z3 + 4} {x + 1} 84 {Z3 + 4} minecraft:birch_fence']
CK = [-17, -11, -5, 1, 7, 13]
L3 += [f'fill {x} 81 {Z3 + 8} {x} 81 {Z3 + 10} minecraft:smooth_quartz' for x in CK]
L3 += [f'fill -20 81 {Z3 - 13} 20 81 {Z3 - 13} minecraft:light_blue_stained_glass']
blocked = {(x + d, z) for x in SH for d in (0, 1) for z in range(Z3 - 9, Z3 + 5)} | {(x, z) for x in CK for z in range(Z3 + 8, Z3 + 11)}
blocked |= {(x, Z3 - 13) for x in range(-20, 21)}
floor3 = [(x, 81, z) for x in range(-21, 22) for z in range(Z3 - 13, Z3 + 14) if (x, z) not in blocked]
scatter(L3, r3, floor3, 55, P3, stack=True)
shelf = [(x + d, y, z) for x in SH for d in (0, 1) for z in range(Z3 - 8, Z3 + 4) for y in (81, 83, 85)]
scatter(L3, r3, shelf, 60, P3)
scatter(L3, r3, [(x, 82, Z3 - 13) for x in range(-20, 21)], 14, ['packed_ice', 'blue_ice', 'melon', 'cake', 'honey_block'])
cage(L3, Z3, 87)
w('ph/build3', L3)

# ------------------------------------------------------------------ carte 4 : serre (arbres, bassin, cabane de jardin, massifs)
Z4 = 23900
r4 = random.Random(9604)
P4 = ['oak_leaves', 'moss_block', 'azalea', 'flowering_azalea', 'potted_red_tulip', 'potted_fern', 'hay_block', 'composter', 'pumpkin',
      'melon', 'beehive', 'barrel', 'target', 'carved_pumpkin', 'lantern']
L4 = [f'# 🎭 Prop Hunt, serre : x -20..20, z {Z4 - 15}..{Z4 + 15}, sol y 80, verrière y 88']
clear(L4, 23, Z4 - 18, Z4 + 18, 78, 96)
L4 += [f'fill -20 79 {Z4 - 15} 20 79 {Z4 + 15} minecraft:dirt', f'fill -20 80 {Z4 - 15} 20 88 {Z4 + 15} minecraft:glass',
       f'fill -19 81 {Z4 - 14} 19 87 {Z4 + 14} minecraft:air', f'fill -19 80 {Z4 - 14} 19 80 {Z4 + 14} minecraft:grass_block',
       f'fill -1 80 {Z4 - 14} 1 80 {Z4 + 14} minecraft:dirt_path', f'fill -19 80 {Z4 - 1} 19 80 {Z4 + 1} minecraft:dirt_path']
L4 += [f'fill {x} 81 {Z4 + sg * 15} {x} 87 {Z4 + sg * 15} minecraft:birch_log' for x in range(-20, 21, 5) for sg in (-1, 1)]
L4 += [f'fill {x} 81 {z} {x} 87 {z} minecraft:birch_log' for x in (-20, 20) for z in range(Z4 - 15, Z4 + 16, 5)]
L4 += [f'fill {x} 88 {Z4 - 15} {x} 88 {Z4 + 15} minecraft:white_concrete' for x in range(-20, 21, 5)]
L4 += [f'setblock {x} 88 {z} minecraft:sea_lantern' for x in range(-15, 16, 5) for z in range(Z4 - 12, Z4 + 13, 4)]
# bassin
L4 += [f'fill 6 79 {Z4 + 5} 12 79 {Z4 + 11} minecraft:sand', f'fill 6 80 {Z4 + 5} 12 80 {Z4 + 11} minecraft:water',
       f'fill 5 80 {Z4 + 4} 13 80 {Z4 + 4} minecraft:mossy_cobblestone', f'fill 5 80 {Z4 + 12} 13 80 {Z4 + 12} minecraft:mossy_cobblestone',
       f'fill 5 80 {Z4 + 4} 5 80 {Z4 + 12} minecraft:mossy_cobblestone', f'fill 13 80 {Z4 + 4} 13 80 {Z4 + 12} minecraft:mossy_cobblestone']
L4 += [f'setblock {x} 81 {z} minecraft:lily_pad' for x in range(6, 13) for z in range(Z4 + 5, Z4 + 12) if r4.random() < 0.2]
# arbres
TREES = [(-12, Z4 - 10), (-6, Z4 + 9), (12, Z4 - 9), (15, Z4 - 4), (4, Z4 - 11), (-15, Z4 + 10)]
for (tx, tz) in TREES:
    L4 += [f'fill {tx} 81 {tz} {tx} 84 {tz} minecraft:oak_log',
           f'fill {tx - 2} 84 {tz - 2} {tx + 2} 85 {tz + 2} minecraft:oak_leaves[persistent=true] replace minecraft:air',
           f'fill {tx - 1} 86 {tz - 1} {tx + 1} 86 {tz + 1} minecraft:oak_leaves[persistent=true]']
# massifs de fougères
BEDS = [(-11, -5, Z4 + 3, Z4 + 5), (3, 9, Z4 - 6, Z4 - 4), (15, 18, Z4 + 5, Z4 + 12)]
for (x1, x2, z1, z2) in BEDS:
    L4.append(f'fill {x1} 80 {z1} {x2} 80 {z2} minecraft:podzol')
    L4 += [f'setblock {x} 81 {z} minecraft:fern' for x in range(x1, x2 + 1) for z in range(z1, z2 + 1) if r4.random() < 0.5]
# cabane de jardin (porte côté allée)
L4 += [f'fill -19 81 {Z4 - 3} -14 84 {Z4 + 3} minecraft:spruce_planks', f'fill -18 81 {Z4 - 2} -15 84 {Z4 + 2} minecraft:air',
       f'fill -19 85 {Z4 - 3} -14 85 {Z4 + 3} minecraft:spruce_slab', f'fill -14 81 {Z4 - 1} -14 82 {Z4 + 1} minecraft:air',
       f'setblock -14 83 {Z4 - 2} minecraft:glass_pane', f'setblock -14 83 {Z4 + 2} minecraft:glass_pane']
blocked = {(x, z) for x in range(5, 14) for z in range(Z4 + 4, Z4 + 13)} | {(tx, tz) for tx, tz in TREES}
blocked |= {(x, z) for (x1, x2, z1, z2) in BEDS for x in range(x1, x2 + 1) for z in range(z1, z2 + 1)}
blocked |= {(x, z) for x in range(-19, -13) for z in range(Z4 - 3, Z4 + 4)} | {(-13, z) for z in range(Z4 - 1, Z4 + 2)}
floor4 = [(x, 81, z) for x in range(-19, 20) for z in range(Z4 - 14, Z4 + 15) if (x, z) not in blocked]
scatter(L4, r4, floor4, 75, P4)
scatter(L4, r4, [(x, 81, z) for x in range(-18, -14) for z in range(Z4 - 2, Z4 + 3)], 7, ['barrel', 'composter', 'hay_block', 'cobweb', 'lantern'])
cage(L4, Z4, 89)
w('ph/build4', L4)

# (n°, nom, z, y de la cage, hauteur max d'apparition, rayon d'apparition, objets)
MAPS = [(1, '🏚 Manoir', Z, 89, 85, 13, sorted({p for r in ROOMS for p in r[5]})), (2, '⚓ Entrepôt du port', Z2, 94, 90, 14, P2),
        (3, '🛒 Supermarché', Z3, 88, 84, 12, P3), (4, '🌿 Serre', Z4, 90, 87, 13, P4)]


def per_map(fmt):
    return [f'execute if score $phm mg.st matches {n} run ' + fmt.format(z=z, cy=cy, u=u, r=r, py=cy + 6) for (n, _, z, cy, u, r, _) in MAPS]


w('ph/rnd', ['# @s (cacheur) : un objet au hasard parmi ceux de la carte'] +
  [f'execute if score $phm mg.st matches {n} run function mg:ph/rnd_{n}' for (n, *_) in MAPS])
for (n, _, _, _, _, _, pal) in MAPS:
    w(f'ph/rnd_{n}', [f'execute store result score $phq mg.st run random value 0..{len(pal) - 1}'] +
      [f'execute if score $phq mg.st matches {i} run scoreboard players set @s mg.php {PID[p]}' for i, p in enumerate(pal)])

# ------------------------------------------------------------------ fonctions
w('ph/prepare', ['# 🎭 Prop Hunt, préparation : une carte au hasard', 'execute store result score $phm mg.st run random value 1..4',
                 'execute if score $phm mg.st matches 1 run function mg:ph/build'] +
  [f'execute if score $phm mg.st matches {n} run function mg:ph/build{n}' for (n, *_) in MAPS[1:]] +
  ['function mg:ph/kill_all', 'scoreboard players set $px mg.st 0'] + per_map('scoreboard players set $py mg.st {py}') + per_map('scoreboard players set $pz mg.st {z}') + [
                 'clear @a[tag=mg.play]', 'gamemode adventure @a[tag=mg.play]', 'tag @a[tag=mg.play] add mg.phx',
                 # rôles : 1 chercheur pour 4 joueurs (au moins 1)
                 'execute store result score $phn mg.st if entity @a[tag=mg.play]', 'scoreboard players set #4 mg.st 4',
                 'scoreboard players operation $phn mg.st /= #4 mg.st', 'execute if score $phn mg.st matches ..0 run scoreboard players set $phn mg.st 1',
                 'execute if score $n0 mg.st matches 2.. run function mg:ph/pick', 'execute as @a[tag=mg.play,tag=!mg.phs] run tag @s add mg.phh',
                 'team join mg_red @a[tag=mg.phs]', 'team join mg_ph @a[tag=mg.phh]',
                 ] + per_map('tp @a[tag=mg.phs] 0.5 {cy} {z}.5') + ['execute as @a[tag=mg.phs] at @s run spawnpoint @s ~ ~ ~'] +
  per_map('spreadplayers 0 {z} 2 {r} under {u} false @a[tag=mg.phh]') + ['execute as @a[tag=mg.phh] at @s run spawnpoint @s ~ ~ ~'])
w('ph/pick', ['execute as @a[tag=mg.play,tag=!mg.phs,sort=random,limit=1] run tag @s add mg.phs',
              'scoreboard players remove $phn mg.st 1', 'execute if score $phn mg.st matches 1.. run function mg:ph/pick'])
w('ph/kill_all', ['kill @e[tag=mg.phd]', 'kill @e[tag=mg.phi]'])
w('ph/go', ['# Départ : 30 s pour se cacher', 'scoreboard players set $pht mg.st 0', 'scoreboard players set $phc mg.st 0', 'scoreboard players set @a mg.deaths 0',
            'scoreboard players set @a[tag=mg.play] mg.phpt 0',
            'execute as @a[tag=mg.phh] run function mg:ph/become_prop', 'execute as @a[tag=mg.phs] run function mg:ph/seeker_kit',
            'effect give @a[tag=mg.phs] minecraft:blindness 31 0 true'] +
  [f'execute if score $phm mg.st matches {n} run tellraw @a[tag=mg.play] ' + js([{'text': '🗺 Carte : ', 'color': 'gray'}, {'text': nm, 'color': 'aqua', 'bold': True}])
   for (n, nm, *_) in MAPS] + [
            'tellraw @a[tag=mg.phh] ' + js([{'text': '🎭 PROP HUNT : tu te caches ! ', 'color': 'gold', 'bold': True},
                                            {'text': 'Regarde un objet de la carte et ACCROUPIS-TOI pour en prendre l\'apparence. Reste immobile 2 s pour te caler sur la grille. Les chercheurs arrivent dans 30 s ; toutes les 20 s tu fais un petit bruit, et ta corne (clic droit) en fait un quand tu veux. Attention : 5 cœurs seulement ! Points : plus un chercheur te regarde, plus tu en gagnes, et bouger en rapporte aussi.', 'color': 'gray'}]),
            # seul : entraînement, pas de victoire
            'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] ' + js([{'text': "🎭 Mode entraînement (seul) : tu es cacheur, essaie les déguisements (accroupi devant un objet) et le calage sur la grille. Pas de victoire ; il faut au moins 2 joueurs pour une vraie partie.", 'color': 'yellow'}]),
            'tellraw @a[tag=mg.phs] ' + js([{'text': '🎭 PROP HUNT — tu cherches ! ', 'color': 'red', 'bold': True},
                                            {'text': 'Les cacheurs se transforment en objets du manoir. Tu es libéré dans 30 s : frappe les objets suspects, écoute les bruits !', 'color': 'gray'}])])
w('ph/become_prop', ['# @s devient cacheur : invisible, petit, un objet au hasard',
                     'clear @s', 'scoreboard players add $phc mg.st 1', 'scoreboard players operation @s mg.pid = $phc mg.st',
                     'effect give @s minecraft:invisibility infinite 0 true', 'effect give @s minecraft:saturation infinite 0 true',
                     'attribute @s minecraft:scale base set 0.5',
                     '# Cacheur fragile : 5 cœurs (2 coups d\'épée de chercheur)',
                     'attribute @s minecraft:max_health base set 10', 'effect give @s minecraft:instant_health 1 0 true',
                     'item replace entity @s hotbar.0 with minecraft:goat_horn[instrument="minecraft:ponder_goat_horn",custom_name={"text":"📯 Faire du bruit","color":"gold","italic":false},lore=[{"text":"Clic droit : un bruit pour narguer les chercheurs","color":"gray","italic":false}]]',
                     'function mg:ph/rnd',
                     'execute at @s run summon minecraft:block_display ~ ~ ~ {Tags:["mg.phd","mg.phnew"],teleport_duration:1,block_state:{Name:"minecraft:barrel"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.5f,0f,-0.5f],scale:[1f,1f,1f]}}',
                     'execute at @s run summon minecraft:interaction ~ ~ ~ {Tags:["mg.phi","mg.phnew"],width:1.02f,height:1.02f}',
                     'scoreboard players operation @e[tag=mg.phnew] mg.pid = @s mg.pid', 'tag @e[tag=mg.phnew] remove mg.phnew',
                     'function mg:ph/apply'])
A = ['# @s (cacheur) : met l\'apparence de son objet ($php) sur son block_display',
     'scoreboard players operation $pid mg.st = @s mg.pid', 'scoreboard players operation $pp mg.st = @s mg.php']
for p, i in PID.items():
    st = '{Name:"minecraft:oak_leaves",Properties:{persistent:"true"}}' if p == 'oak_leaves' else f'{{Name:"minecraft:{p}"}}'
    A.append(f'execute if score $pp mg.st matches {i} as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {st}')
for p, i in PID.items():
    A.append(f'execute if score $pp mg.st matches {i} run title @s actionbar [{{"text":"🎭 Tu es : ","color":"gold"}},{{"translate":"block.minecraft.{p}","color":"yellow","bold":true}}]')
w('ph/apply', A)
w('ph/srevive', ['# @s (entraînement, seul) : cacheur réapparu après sa mort → retrouve son déguisement', 'scoreboard players set @s mg.deaths 0',
                 'effect give @s minecraft:invisibility infinite 0 true', 'effect give @s minecraft:saturation infinite 0 true',
                 'attribute @s minecraft:scale base set 0.5', 'attribute @s minecraft:max_health base set 10', 'function mg:ph/apply'])
w('ph/copy', ['# @s (cacheur) s\'accroupit : copie l\'objet qu\'il regarde (5 blocs max)', 'scoreboard players set $phf mg.st 0',
              'scoreboard players set $phr mg.st 25', 'execute at @s anchored eyes positioned ^ ^ ^0.2 run function mg:ph/copy_ray',
              'execute if score $phf mg.st matches 0 run title @s actionbar {"text":"Regarde un objet du manoir (tonneau, citrouille, enclume…)","color":"gray"}',
              'execute if score $phf mg.st matches 1 run function mg:ph/apply',
              'execute if score $phf mg.st matches 1 at @s run playsound minecraft:entity.illusioner.mirror_move player @s ~ ~ ~ 0.6 1.4',
              'execute if score $phf mg.st matches 1 at @s run particle minecraft:poof ~ ~0.5 ~ 0.3 0.3 0.3 0.02 8'])
CR = ['# Un pas (0,2 bloc) du regard du cacheur', 'execute if block ~ ~ ~ #mg:ray_pass run scoreboard players remove $phr mg.st 1',
      'execute if block ~ ~ ~ #mg:ray_pass if score $phr mg.st matches 1.. positioned ^ ^ ^0.2 run return run function mg:ph/copy_ray']
for p, i in PID.items():
    CR.append(f'execute if block ~ ~ ~ minecraft:{p} run return run function mg:ph/got {{p:{i}}}')
w('ph/copy_ray', CR)
w('ph/got', ['$scoreboard players set @s mg.php $(p)', 'scoreboard players set $phf mg.st 1'])
w('ph/follow', ['# @s (cacheur) : son objet le suit ; immobile 2 s → calé sur la grille',
                'scoreboard players operation $pid mg.st = @s mg.pid',
                'execute store result score @s mg.tx run data get entity @s Pos[0] 20', 'execute store result score @s mg.tz run data get entity @s Pos[2] 20',
                'execute if score @s mg.tx = @s mg.phx if score @s mg.tz = @s mg.phz run scoreboard players add @s mg.phs 1',
                'execute unless score @s mg.tx = @s mg.phx run scoreboard players set @s mg.phs 0',
                'execute unless score @s mg.tz = @s mg.phz run scoreboard players set @s mg.phs 0',
                'scoreboard players operation @s mg.phx = @s mg.tx', 'scoreboard players operation @s mg.phz = @s mg.tz',
                'execute if score @s mg.phs matches ..39 as @e[tag=mg.phd] if score @s mg.pid = $pid mg.st run tp @s ~ ~ ~ 0 0',
                'execute if score @s mg.phs matches ..39 as @e[tag=mg.phi] if score @s mg.pid = $pid mg.st run tp @s ~ ~-0.01 ~',
                'execute if score @s mg.phs matches 40 align xyz positioned ~0.5 ~ ~0.5 as @e[tag=mg.phd] if score @s mg.pid = $pid mg.st run tp @s ~ ~ ~ 0 0',
                'execute if score @s mg.phs matches 40 align xyz positioned ~0.5 ~ ~0.5 as @e[tag=mg.phi] if score @s mg.pid = $pid mg.st run tp @s ~ ~-0.01 ~',
                'execute if score @s mg.phs matches 40 run title @s actionbar {"text":"🔒 Verrouillé sur la grille","color":"green"}',
                'execute if score @s mg.phs matches 41.. run scoreboard players set @s mg.phs 41'])
w('ph/hit_prop', ['# @s = interaction frappée : le cacheur lié prend un coup (si c\'est un chercheur)',
                  'execute on attacker if entity @s[tag=mg.phs] run tag @s add mg.phatk', 'data remove entity @s attack',
                  'scoreboard players operation $pid mg.st = @s mg.pid',
                  'execute if entity @a[tag=mg.phatk] as @a[tag=mg.phh] if score @s mg.pid = $pid mg.st run damage @s 5 minecraft:player_attack by @a[tag=mg.phatk,limit=1]',
                  'tag @a remove mg.phatk'])
w('ph/seeker_kit', ['# @s : chercheur', 'clear @s', 'effect clear @s minecraft:invisibility', 'attribute @s minecraft:scale base set 1',
                    'attribute @s minecraft:max_health base set 20', 'effect give @s minecraft:instant_health 1 4 true',
                    'item replace entity @s hotbar.0 with minecraft:iron_sword[unbreakable={}]',
                    'item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16711680,unbreakable={}]',
                    'item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=16711680,unbreakable={}]',
                    'effect give @s minecraft:saturation infinite 0 true', 'effect give @s minecraft:speed infinite 0 true'])
w('ph/release', ['# Fin de la cachette : les chercheurs entrent', 'effect clear @a[tag=mg.phs] minecraft:blindness'] +
  per_map('spreadplayers 0 {z} 1 4 under {u} false @a[tag=mg.phs]') + ['execute as @a[tag=mg.phs] at @s run spawnpoint @s ~ ~ ~',
                 'title @a[tag=mg.play] title {"text":"Les chercheurs arrivent !","color":"red","bold":true}',
                 'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.wolf.howl master @s ~ ~ ~ 0.7 1'])
w('ph/use_prop', ['# @s = interaction cliquée (clic droit) : si c\'est un cacheur → corne', 'execute on target if entity @s[tag=mg.phh] run tag @s add mg.phuse',
                  'data remove entity @s interaction'])
w('ph/horn', ['# @s (cacheur) : bruit volontaire, recharge 3 s',
              'execute if score @s mg.phcd matches 1.. run return run title @s actionbar {"text":"📯 Corne en recharge…","color":"gray"}',
              'scoreboard players set @s mg.phcd 60', 'function mg:ph/taunt_one',
              'playsound minecraft:item.goat_horn.sound.0 player @a ~ ~ ~ 1.5 1.2',
              'title @s actionbar {"text":"📯 Tu as fait du bruit !","color":"gold"}'])
w('ph/taunt', ['# Toutes les 20 s : chaque cacheur fait un petit bruit',
               'execute as @a[tag=mg.phh] at @s run function mg:ph/taunt_one'])
w('ph/taunt_one', ['execute store result score $phq mg.st run random value 0..3',
                   'execute if score $phq mg.st matches 0 run playsound minecraft:entity.cat.ambient player @a ~ ~ ~ 1.2 1.2',
                   'execute if score $phq mg.st matches 1 run playsound minecraft:entity.chicken.ambient player @a ~ ~ ~ 1.2 1',
                   'execute if score $phq mg.st matches 2 run playsound minecraft:entity.villager.ambient player @a ~ ~ ~ 1.2 1.3',
                   'execute if score $phq mg.st matches 3 run playsound minecraft:block.note_block.bell player @a ~ ~ ~ 1.2 1.8',
                   'particle minecraft:note ~ ~1 ~ 0.2 0.2 0.2 1 2'])
w('ph/found', ['# @s (cacheur) trouvé : devient chercheur', 'scoreboard players set @s mg.deaths 0',
               'scoreboard players operation $pid mg.st = @s mg.pid',
               'execute as @e[tag=mg.phd] if score @s mg.pid = $pid mg.st run kill @s',
               'execute as @e[tag=mg.phi] if score @s mg.pid = $pid mg.st run kill @s',
               'tag @s remove mg.phh', 'tag @s add mg.phs', 'team join mg_red @s', 'function mg:ph/seeker_kit'] +
  per_map('spreadplayers 0 {z} 1 4 under {u} false @s') + [
               'tellraw @a[tag=mg.play] [{"text":"🎭 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a été trouvé et rejoint les chercheurs !","color":"gray"}]',
               'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.item.break master @s ~ ~ ~ 0.8 0.7'])
w('ph/tick', ['# 🎭 Prop Hunt — tick', 'scoreboard players add $pht mg.st 1',
              ] + [f'execute if score $pht mg.st matches ..{HIDE - 1} ' + l[8:] for l in per_map('tp @a[tag=mg.phs] 0.5 {cy} {z}.5')] + [
              f'execute if score $pht mg.st matches {HIDE} run function mg:ph/release',
              # copie d'objet (accroupi), suivi, coups sur les objets
              'execute as @a[tag=mg.phh,scores={mg.gsn=1..},tag=!mg.phsn] run function mg:ph/copy',
              'tag @a[tag=mg.phh,scores={mg.gsn=1..}] add mg.phsn', 'tag @a[tag=mg.phsn,scores={mg.gsn=0}] remove mg.phsn',
              'tag @a[tag=mg.phsn] remove mg.phsn' if False else 'execute as @a[tag=mg.phsn] unless score @s mg.gsn matches 1.. run tag @s remove mg.phsn',
              'scoreboard players set @a[tag=mg.phx] mg.gsn 0',
              'execute as @a[tag=mg.phh] at @s run function mg:ph/follow',
              # corne : le cacheur est DANS sa propre interaction (taille 0,5) → son clic droit touche l'interaction, pas la corne
              'execute as @e[type=minecraft:interaction,tag=mg.phi] if data entity @s interaction run function mg:ph/use_prop',
              'execute as @a[tag=mg.phh,scores={mg.phn=1..}] run tag @s add mg.phuse',
              'scoreboard players reset @a[scores={mg.phn=1..}] mg.phn',
              'scoreboard players remove @a[tag=mg.phx,scores={mg.phcd=1..}] mg.phcd 1',
              'execute as @a[tag=mg.phh,tag=mg.phuse] at @s run function mg:ph/horn',
              'tag @a remove mg.phuse',
              'execute as @e[type=minecraft:interaction,tag=mg.phi] if data entity @s attack run function mg:ph/hit_prop',
              'execute if score $n0 mg.st matches 2.. as @a[tag=mg.phh,scores={mg.deaths=1..}] run function mg:ph/found',
              # seul : le cacheur reste cacheur
              'execute unless score $n0 mg.st matches 2.. as @e[type=minecraft:player,tag=mg.phh,scores={mg.deaths=1..}] run function mg:ph/srevive',
              'execute as @a[tag=mg.phs,scores={mg.deaths=1..}] run scoreboard players set @s mg.deaths 0',
              'scoreboard players operation $phq mg.st = $pht mg.st', 'scoreboard players set #400 mg.st 400', 'scoreboard players operation $phq mg.st %= #400 mg.st',
              f'execute if score $pht mg.st matches {HIDE + 1}.. if score $phq mg.st matches 0 run function mg:ph/taunt',
              'scoreboard players operation $phq mg.st = $pht mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $phq mg.st %= #20 mg.st',
              'execute if score $phq mg.st matches 0 run function mg:ph/second',
              '# points des cacheurs, 4 fois par seconde pendant la chasse',
              'scoreboard players operation $phq mg.st = $pht mg.st', 'scoreboard players set #5 mg.st 5', 'scoreboard players operation $phq mg.st %= #5 mg.st',
              f'execute if score $pht mg.st matches {HIDE + 1}.. if score $phq mg.st matches 0 run function mg:ph/pts',
              'execute store result score $phh mg.st if entity @a[tag=mg.play,tag=mg.phh]',
              'execute store result score $phk mg.st if entity @a[tag=mg.play,tag=mg.phs]',
              'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $phh mg.st matches 0 run return run function mg:ph/seekers_win',
              'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $phk mg.st matches 0 run return run function mg:ph/hiders_win',
              f'execute if score $state mg.st matches 2 if score $pht mg.st matches {HIDE + HUNT}.. run function mg:ph/hiders_win'])
w('ph/second', [f'execute if score $pht mg.st matches {HIDE + 1}.. run function mg:ph/hpts', f'scoreboard players set $phl mg.st {(HIDE + HUNT) // 20}', 'scoreboard players operation $phs2 mg.st = $pht mg.st',
                'scoreboard players operation $phs2 mg.st /= #20 mg.st', 'scoreboard players operation $phl mg.st -= $phs2 mg.st',
                # seul : chrono restant
                'execute unless score $n0 mg.st matches 2.. run title @a[tag=mg.play] actionbar [{"text":"🎭 Entraînement : ","color":"yellow"},{"score":{"name":"$phl","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"gray"}]',
                f'execute if score $pht mg.st matches ..{HIDE} run title @a[tag=mg.phs] actionbar [{{"text":"🎭 Les cacheurs se cachent… ","color":"gray"}},{{"score":{{"name":"$phl","objective":"mg.st"}},"color":"yellow"}}]',
                f'execute if score $pht mg.st matches {HIDE + 1}.. run title @a[tag=mg.phs] actionbar [{{"text":"🎭 Cacheurs restants : ","color":"red"}},{{"score":{{"name":"$phh","objective":"mg.st"}},"color":"yellow","bold":true}},{{"text":" — ","color":"gray"}},{{"score":{{"name":"$phl","objective":"mg.st"}},"color":"yellow"}},{{"text":" s","color":"gray"}}]'])
w('ph/pts', ['# Points des cacheurs : regardé par un chercheur (+2), en mouvement (+1)',
             'execute as @a[tag=mg.phs,gamemode=!spectator] at @s anchored eyes positioned ^ ^ ^0.5 run function mg:ph/look',
             'execute as @e[type=minecraft:interaction,tag=mg.phlk] run function mg:ph/looked',
             'scoreboard players add @a[tag=mg.phh,scores={mg.phs=..4}] mg.phpt 1'])
w('ph/look', ['# @s (chercheur) : regard de 24 blocs', 'scoreboard players set $phr mg.st 48', 'function mg:ph/look_ray'])
w('ph/look_ray', ['# Un pas (0,5 bloc) du regard du chercheur ; un mur l\'arrête, le premier objet-cacheur touché est marqué',
                  'execute unless block ~ ~ ~ #mg:ray_pass run return 0',
                  'execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=minecraft:interaction,tag=mg.phi,dx=0,dy=0,dz=0] run tag @s add mg.phlk',
                  'execute positioned ~-0.5 ~-0.5 ~-0.5 if entity @e[type=minecraft:interaction,tag=mg.phi,dx=0,dy=0,dz=0] run return 0',
                  'scoreboard players remove $phr mg.st 1',
                  'execute if score $phr mg.st matches 1.. positioned ^ ^ ^0.5 run function mg:ph/look_ray'])
w('ph/looked', ['# @s : objet d\'un cacheur regardé par un chercheur', 'tag @s remove mg.phlk', 'scoreboard players operation $pid mg.st = @s mg.pid',
                'execute as @a[tag=mg.phh] if score @s mg.pid = $pid mg.st run scoreboard players add @s mg.phpt 2'])
w('ph/rank', ['# Fin : points de chaque cacheur et meilleur cacheur', 'scoreboard players set $phb mg.st 0',
              'execute as @a[tag=mg.phx] run scoreboard players operation $phb mg.st > @s mg.phpt',
              'execute if score $phb mg.st matches ..0 run return 0',
              'tellraw @a[tag=mg.phx] {"text":"🎭 Points des cacheurs (regardés par les chercheurs, en mouvement) :","color":"gold"}',
              'execute as @a[tag=mg.phx,scores={mg.phpt=1..}] run tellraw @a[tag=mg.phx] [{"text":" • ","color":"gray"},{"selector":"@s","color":"yellow"},{"text":" : ","color":"gray"},{"score":{"name":"@s","objective":"mg.phpt"},"color":"aqua","bold":true}]',
              'execute as @a[tag=mg.phx] if score @s mg.phpt = $phb mg.st run tellraw @a [{"text":"🏆 Meilleur cacheur : ","color":"gold","bold":true},{"selector":"@s","color":"yellow"},{"text":" (","color":"gray"},{"score":{"name":"$phb","objective":"mg.st"},"color":"aqua"},{"text":" points)","color":"gray"}]'])
w('ph/hpts', ['execute as @a[tag=mg.phh] run title @s actionbar [{"text":"🎭 Tes points : ","color":"gold"},{"score":{"name":"@s","objective":"mg.phpt"},"color":"aqua","bold":true},{"text":"  (regardé +2, en mouvement +1)","color":"gray"}]'])
w('ph/hiders_win', ['# Les cacheurs gagnent', 'function mg:ph/rank',
                    'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] ' + js([{'text': "🎭 Fin de l'entraînement.", 'color': 'yellow'}]),
                    'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                    'tag @a[tag=mg.play,tag=mg.phh] add mg.win', 'scoreboard players add @a[tag=mg.play,tag=mg.phh] mg.wins 1',
                    'scoreboard players set $state mg.st 3', 'scoreboard players set $timer mg.st 120',
                    'title @a[tag=!mg.surv] title {"text":"Les CACHEURS gagnent !","color":"gold","bold":true}',
                    'tellraw @a [{"text":"★ Victoire des cacheurs : ","color":"gold"},{"selector":"@a[tag=mg.play,tag=mg.phh]","color":"yellow"}]',
                    'execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1'])
w('ph/seekers_win', ['# Plus aucun cacheur', 'function mg:ph/rank', 'tellraw @a {"text":"🎭 Tous les cacheurs ont été trouvés !","color":"red","bold":true}', 'function mg:core/win_red'])
w('ph/cleanup', ['function mg:ph/kill_all', 'execute as @a[tag=mg.phx] run attribute @s minecraft:scale base set 1',
                 'execute as @a[tag=mg.phx] run attribute @s minecraft:max_health base set 20',
                 'effect clear @a[tag=mg.phx] minecraft:invisibility', 'effect clear @a[tag=mg.phx] minecraft:speed',
                 'effect clear @a[tag=mg.phx] minecraft:blindness', 'team leave @a[team=mg_ph]',
                 'tag @a remove mg.phh', 'tag @a remove mg.phs', 'tag @a remove mg.phsn', 'tag @a remove mg.phx'])

C.register([96], 'ph', [C.announce(96, '', '🎭 PROP HUNT', 'gold', 'cachez-vous en objets, les chercheurs arrivent dans 30 s !')])
C.objectives([('mg.phn', 'minecraft.used:minecraft.goat_horn'), ('mg.pid', 'dummy'), ('mg.php', 'dummy'), ('mg.phx', 'dummy'), ('mg.phz', 'dummy'), ('mg.phs', 'dummy')])
C.objectives([('mg.phpt', 'dummy'), ('mg.phcd', 'dummy')])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger', ['team add mg_ph', 'team modify mg_ph nametagVisibility never',
                                                                 'team modify mg_ph friendlyFire false', 'team modify mg_ph collisionRule never',
                                                                 'scoreboard players set #4 mg.st 4'])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['team remove mg_ph'])
C.forceload([f'# Prop Hunt (z {Z})', f'forceload add -23 {Z - 18} 23 {Z + 18}'])
C.forceload([f'# Prop Hunt, autres cartes (z {Z2}, {Z3}, {Z4})', f'forceload add -27 {Z2 - 19} 27 {Z2 + 19}',
             f'forceload add -25 {Z3 - 17} 25 {Z3 + 17}', f'forceload add -23 {Z4 - 18} 23 {Z4 + 18}'])
print('Prop Hunt OK')
