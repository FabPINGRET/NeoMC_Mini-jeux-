"""🎢 Montagne russe du spawn (à l'ouest de l'île, gare en x −88 z 0). Pas un mini-jeu : une attraction libre.

    python tools/arcade/gen_coaster.py .

Physique vanilla 26.2 (l'expérience « minecart improvements » n'est pas activable sur un monde existant) :
rails propulseurs alimentés par un bloc de redstone dessous sur toutes les lignes droites et les pentes,
rails simples dans les virages. Les rails sont posés en mode `strict` (aucune mise à jour de voisins → les formes
calculées ici sont gardées).

Monter : marcher sur la plaque dorée de la gare → un wagonnet apparaît, on y est assis, départ.
Arrivée : retour par la voie parallèle (z −6), le wagonnet disparaît en gare.
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js

D = {'E': (1, 0), 'W': (-1, 0), 'S': (0, 1), 'N': (0, -1)}
NAME = {(1, 0): 'east', (-1, 0): 'west', (0, 1): 'south', (0, -1): 'north'}
START = (-118, 64, 0)   # gare décalée hors du plot 8 (x -108..-84) ; accès par une passerelle entre les plots 7 et 8
# (direction, longueur, dénivelé) — le dénivelé est réparti au milieu du segment (jamais sur les 2 premiers/derniers pas)
SEG = [('W', 14, 0), ('W', 44, 34), ('N', 12, 0), ('E', 40, -28), ('N', 12, 0), ('W', 36, 10), ('N', 12, 0),
       ('E', 36, -8), ('N', 8, 0), ('W', 50, -2), ('S', 38, -4), ('E', 64, -2)]


def path():
    x, y, z = START
    pts = [(x, y, z)]
    for d, n, dy in SEG:
        dx, dz = D[d]
        k = abs(dy)
        s = 1 if dy > 0 else -1
        first = (n - k) // 2
        for i in range(n):
            x += dx
            z += dz
            if first <= i < first + k:
                y += s
            pts.append((x, y, z))
    return pts


P = path()


def shape(i):
    x, y, z = P[i]
    a = (P[i][0] - P[i - 1][0], P[i][2] - P[i - 1][2]) if i > 0 else (P[1][0] - P[0][0], P[1][2] - P[0][2])
    b = (P[i + 1][0] - x, P[i + 1][2] - z) if i < len(P) - 1 else a
    up_next = i < len(P) - 1 and P[i + 1][1] > y
    up_prev = i > 0 and P[i - 1][1] > y
    if up_next:
        assert a == b, i
        return 'ascending_' + NAME[b], True
    if up_prev:
        assert a == b, i
        return 'ascending_' + NAME[(-a[0], -a[1])], True
    if a == b:
        return ('east_west' if a[1] == 0 else 'north_south'), True
    sides = {NAME[(-a[0], -a[1])], NAME[b]}
    ns = 'north' if 'north' in sides else 'south'
    ew = 'east' if 'east' in sides else 'west'
    return f'{ns}_{ew}', False


# contrôles : pas de croisement trop bas, pas de rails voisins non consécutifs (sinon jonctions)
cells = {}
for i, (x, y, z) in enumerate(P):
    for j in cells.get((x, z), []):
        assert abs(P[j][1] - y) >= 4, ('croisement trop bas', P[j], (x, y, z))
    cells.setdefault((x, z), []).append(i)
for i, (x, y, z) in enumerate(P):
    for dx, dz in D.values():
        for j in cells.get((x + dx, z + dz), []):
            assert abs(j - i) == 1 or abs(P[j][1] - y) >= 3, ('rails voisins', P[i], P[j])
xs = [p[0] for p in P]
zs = [p[2] for p in P]
ys = [p[1] for p in P]
END = P[-1]
assert END[0] > -126 and END[2] == -6, END
BB = (min(xs) - 2, min(ys) - 2, min(zs) - 2, max(xs) + 2, max(ys) + 4, max(zs) + 2)

L = ['# 🎢 Montagne russe — voie (générée, ne pas éditer à la main : tools/arcade/gen_coaster.py)']
for i, (x, y, z) in enumerate(P):
    sh, powered = shape(i)
    if powered:
        L.append(f'setblock {x} {y - 1} {z} minecraft:redstone_block strict')
    else:
        L.append(f'setblock {x} {y - 1} {z} minecraft:polished_blackstone strict')
for i, (x, y, z) in enumerate(P):
    sh, powered = shape(i)
    if powered:
        L.append(f'setblock {x} {y} {z} minecraft:powered_rail[shape={sh},powered=true] strict')
    else:
        L.append(f'setblock {x} {y} {z} minecraft:rail[shape={sh}] strict')
    if i % 12 == 6 and not sh.startswith('asc'):
        L.append(f'setblock {x} {y - 2} {z} minecraft:sea_lantern strict')
# butée en bout de voie
L.append(f'setblock {END[0] + 1} {END[1]} {END[2]} minecraft:polished_blackstone_wall')
w('coaster/track', L)

sx, sy, sz = START
w('coaster/build_start', ['# 🎢 Montagne russe : charge la zone puis construit (3 s plus tard)',
                          f'forceload add {BB[0]} {BB[2]} {BB[3]} {BB[5]}', 'schedule function mg:coaster/build 3s'])
w('coaster/build', ['# 🎢 Montagne russe : gare + voie',
                    # nettoyage de la zone de la voie (en tranches : 32768 blocs max par fill) ; marge à l'est pour l'ancienne voie
                    ] + [f'fill {BB[0]} {y} {BB[2]} -109 {min(y + 7, BB[4])} {BB[5]} minecraft:air strict' for y in range(BB[1], BB[4] + 1, 8)] + [
                    # ancienne gare (x -124..-104, mordait sur le plot 8) : on retire ce qu'elle avait posé et on répare le plot
                    'fill -124 62 -9 -109 70 3 minecraft:air',
                    'fill -108 64 -9 -104 68 3 minecraft:air replace minecraft:spruce_fence', 'fill -108 64 -9 -104 68 3 minecraft:air replace minecraft:spruce_log',
                    'fill -108 64 -9 -104 68 3 minecraft:air replace minecraft:spruce_slab', 'fill -108 64 -9 -104 68 3 minecraft:air replace minecraft:lantern',
                    'fill -108 62 -9 -104 62 3 minecraft:air replace minecraft:stripped_spruce_log',
                    'fill -107 63 -9 -107 63 3 minecraft:stone_bricks replace minecraft:spruce_planks',
                    'fill -106 63 -9 -104 63 3 minecraft:grass_block replace minecraft:spruce_planks',
                    'fill -108 63 -9 -108 63 3 minecraft:stone_bricks replace minecraft:spruce_planks',
                    'function mg:plot/walls {x1:-108,x2:-84,z1:-12,z2:12}',
                    # gare : x -130..-110, z -9..3 (voies en z 0 et z -6), entrée au sud
                    'fill -130 63 -9 -110 63 3 minecraft:spruce_planks', 'fill -130 62 -9 -110 62 3 minecraft:stripped_spruce_log',
                    'fill -130 64 -9 -110 64 -9 minecraft:spruce_fence', 'fill -130 64 3 -110 64 3 minecraft:spruce_fence',
                    'fill -110 64 -8 -110 64 2 minecraft:spruce_fence', 'fill -130 64 -8 -130 64 2 minecraft:spruce_fence',
                    'fill -130 64 0 -130 64 0 minecraft:air', 'fill -130 64 -6 -130 64 -6 minecraft:air',
                    'fill -115 64 3 -114 64 3 minecraft:air',
                    'fill -129 68 -9 -111 68 3 minecraft:spruce_slab[type=bottom]',
                    'fill -129 64 -9 -129 67 -9 minecraft:spruce_log', 'fill -111 64 -9 -111 67 -9 minecraft:spruce_log',
                    'fill -129 64 3 -129 67 3 minecraft:spruce_log', 'fill -111 64 3 -111 67 3 minecraft:spruce_log',
                    'setblock -116 67 -3 minecraft:lantern[hanging=true]', 'setblock -124 67 -3 minecraft:lantern[hanging=true]',
                    'fill -117 63 1 -115 63 1 minecraft:gold_block', 'setblock -116 64 1 minecraft:light_weighted_pressure_plate',
                    # passerelle : du bord du spawn (x -71, z 16..17) vers l'ouest entre les plots 7 et 8, puis au nord jusqu'à la gare
                    'fill -115 63 16 -71 63 17 minecraft:spruce_planks', 'fill -115 62 16 -71 62 17 minecraft:stripped_spruce_log',
                    'fill -115 64 15 -73 64 15 minecraft:spruce_fence', 'fill -115 64 18 -73 64 18 minecraft:spruce_fence',
                    'fill -115 63 4 -114 63 15 minecraft:spruce_planks', 'fill -115 62 4 -114 62 15 minecraft:stripped_spruce_log',
                    'fill -116 64 4 -116 64 18 minecraft:spruce_fence', 'fill -113 64 4 -113 64 14 minecraft:spruce_fence',
                    'fill -114 64 15 -114 64 15 minecraft:air', 'fill -115 64 15 -115 64 15 minecraft:air',
                    'setblock -116 65 16 minecraft:lantern', 'setblock -92 65 15 minecraft:lantern', 'setblock -92 65 18 minecraft:lantern',
                    'setblock -73 65 15 minecraft:lantern', 'setblock -73 65 18 minecraft:lantern', 'setblock -113 65 8 minecraft:lantern',
                    'function mg:coaster/track',
                    'kill @e[tag=mg.cst]', 'kill @e[tag=mg.csd]',
                    'summon minecraft:text_display -116 66.6 1.5 {Tags:["mg.csd"],billboard:"center",text:[{"text":"🎢 Montagne russe","color":"gold","bold":true},{"text":"\\nmarche sur la plaque dorée","color":"gray"}]}',
                    'summon minecraft:text_display -70.5 66 16.9 {Tags:["mg.csd"],billboard:"center",text:{"text":"🎢 Montagne russe →","color":"gold","bold":true}}',
                    f'forceload remove {BB[0]} {BB[2]} {BB[3]} {BB[5]}', 
                    'data modify storage mg:lobby coaster1 set value 1b', 'data modify storage mg:lobby coaster2 set value 1b',
                    'tellraw @a[tag=mg.admin] {"text":"🎢 Montagne russe construite (gare à l\'ouest du spawn).","color":"gold"}'])
w('coaster/tick', ['# 🎢 Montagne russe — tick (seulement si quelqu\'un est en gare ou en wagon)',
                   'execute as @a[x=-117,y=64,z=1,dx=1,dy=1,dz=0,tag=!mg.play,tag=!mg.csr] unless predicate mg:coaster_riding run function mg:coaster/board',
                   'tag @a[tag=mg.csr] remove mg.csr', 'tag @a[x=-117,y=64,z=1,dx=1,dy=1,dz=0] add mg.csr',
                   # arrivée, abandon, chute
                   f'execute as @e[type=minecraft:minecart,tag=mg.cst,x={END[0] - 4},y={END[1] - 1},z={END[2] - 1},dx=6,dy=3,dz=2] run function mg:coaster/arrive',
                   'execute as @e[type=minecraft:minecart,tag=mg.cst] unless predicate mg:coaster_has_rider run kill @s',
                   'execute as @e[type=minecraft:minecart,tag=mg.cst] at @s if entity @s[y=-64,dy=104] run kill @s'])
w('coaster/board', ['# @s monte dans un wagonnet (départ immédiat vers l\'ouest)',
                    f'summon minecraft:minecart {sx}.5 {sy} {sz}.5 {{Tags:["mg.cst","mg.csn"],Motion:[-0.4d,0d,0d]}}',
                    'ride @s mount @e[type=minecraft:minecart,tag=mg.csn,limit=1]', 'tag @e[tag=mg.csn] remove mg.csn',
                    'playsound minecraft:entity.minecart.riding master @s ~ ~ ~ 0.6 1.2',
                    'title @s actionbar {"text":"🎢 Accroche-toi !","color":"gold"}'])
w('coaster/arrive', ['# Wagonnet en gare : le passager descend sur le quai',
                     'execute on passengers run tag @s add mg.csx', 'ride @a[tag=mg.csx,limit=1] dismount',
                     'tp @a[tag=mg.csx] -120.5 64 -3.5 -90 0', 'tag @a[tag=mg.csx] remove mg.csx', 'kill @s'])
import os, json
os.makedirs(os.path.join(C.D, 'predicate'), exist_ok=True)
json.dump({'condition': 'minecraft:entity_properties', 'entity': 'this', 'predicate': {'vehicle': {}}},
          open(os.path.join(C.D, 'predicate/coaster_riding.json'), 'w'), indent=2)
json.dump({'condition': 'minecraft:entity_properties', 'entity': 'this', 'predicate': {'passenger': {}}},
          open(os.path.join(C.D, 'predicate/coaster_has_rider.json'), 'w'), indent=2)

C.patch('core/tick', 'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block 24 63 19 minecraft:gold_block run function mg:lobby/food_build',
        ['execute if score $setup mg.st matches 1 if entity @a[x=-200,y=40,z=-60,dx=130,dy=80,dz=80] run function mg:coaster/tick'])
C.patch('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:lobby food1 run schedule function mg:lobby/food_build 12s',
        ['execute if score $setup mg.st matches 1 unless data storage mg:lobby coaster2 run schedule function mg:coaster/build_start 16s'])
C.patch('desinstaller', 'schedule clear mg:lobby/food_build',
        ['schedule clear mg:coaster/build_start', 'schedule clear mg:coaster/build', 'kill @e[tag=mg.cst]', 'kill @e[tag=mg.csd]',
         'data remove storage mg:lobby coaster1', 'data remove storage mg:lobby coaster2'])
print('Montagne russe OK :', len(P), 'rails, bbox', BB, 'fin', END)
