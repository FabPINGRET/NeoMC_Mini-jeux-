"""🎢 Montagne russe du spawn : grand tour de l'île en hauteur (y 82..98). Pas un mini-jeu : une attraction libre.

    python tools/arcade/gen_coaster.py .

Physique vanilla 26.2 (l'expérience « minecart improvements » n'est pas activable sur un monde existant) :
rails propulseurs alimentés par un bloc de redstone dessous sur toutes les lignes droites et les pentes,
rails simples dans les virages. Les rails sont posés en mode `strict` (aucune mise à jour de voisins → les formes
calculées ici sont gardées).

Monter : marcher sur la plaque dorée du guichet (jardin sud-ouest) → on est placé dans un wagonnet en haut de la voie, départ.
Arrivée : après le tour complet, le wagonnet s'arrête 3 blocs avant le départ et on redescend au guichet.
L'ancienne voie (à l'ouest, hors de l'île) est effacée une fois (drapeau mg:lobby coaster3).
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js

D = {'E': (1, 0), 'W': (-1, 0), 'S': (0, 1), 'N': (0, -1)}
NAME = {(1, 0): 'east', (-1, 0): 'west', (0, 1): 'south', (0, -1): 'north'}

# ancienne voie (à l'ouest, hors de l'île) : gardée ici seulement pour l'effacer une fois
OLD_START = (-118, 64, 0)
OLD_SEG = [('W', 14, 0), ('W', 44, 34), ('N', 12, 0), ('E', 40, -28), ('N', 12, 0), ('W', 36, 10), ('N', 12, 0),
           ('E', 36, -8), ('N', 8, 0), ('W', 50, -2), ('S', 38, -4), ('E', 64, -2)]

# nouvelle voie : grand tour du spawn en hauteur, au-dessus du bord de l'île (carré aux coins coupés, côtés à ±64)
Y = 86
START = (-64, Y, 30)
KIOSK = (-45, 64, 41)          # guichet au sol (jardin sud-ouest) : la plaque dorée envoie dans le wagon, là-haut
# (direction, longueur, dénivelé) ; direction composée ('N', 'E') = diagonale en escalier (2 rails par pas, pas de dénivelé)
SEG = [('N', 10, 0), ('N', 28, 12), ('N', 28, 0),            # côté ouest : montée
       (('N', 'E'), 28, 0),                                   # coin nord-ouest
       ('E', 36, -16), ('E', 36, 12),                         # côté nord : plongée puis remontée
       (('E', 'S'), 28, 0),                                   # coin nord-est
       ('S', 24, -10), ('S', 24, 10), ('S', 24, -6),          # côté est : bosses
       (('S', 'W'), 28, 0),                                   # coin sud-est
       ('W', 36, 6), ('W', 36, -8),                           # côté sud
       (('W', 'N'), 28, 0),                                   # coin sud-ouest
       ('N', 2, 0)]                                           # arrivée, 3 blocs avant le départ


def path(start, segs):
    x, y, z = start
    pts = [(x, y, z)]
    for d, n, dy in segs:
        if isinstance(d, tuple):                                # escalier : alternance des deux directions
            assert dy == 0
            for _ in range(n):
                for e in d:
                    x += D[e][0]
                    z += D[e][1]
                    pts.append((x, y, z))
            continue
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


P = path(START, SEG)
OLD_P = path(OLD_START, OLD_SEG)


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
assert END[0] == START[0] and END[1] == START[1] and END[2] - START[2] == 4, (END, START)   # arrivée juste au sud du départ
BB = (min(xs) - 2, min(ys) - 3, min(zs) - 2, max(xs) + 2, max(ys) + 3, max(zs) + 2)

L = ['# 🎢 Montagne russe — voie (générée, ne pas éditer à la main : tools/arcade/gen_coaster.py)']
for i, (x, y, z) in enumerate(P):
    sh, powered = shape(i)
    L.append(f'setblock {x} {y - 1} {z} minecraft:{"redstone_block" if powered else "polished_blackstone"} strict')
for i, (x, y, z) in enumerate(P):
    sh, powered = shape(i)
    L += [f'setblock {x} {y + 1} {z} minecraft:air strict', f'setblock {x} {y + 2} {z} minecraft:air strict']   # feuillage éventuel
    if powered:
        L.append(f'setblock {x} {y} {z} minecraft:powered_rail[shape={sh},powered=true] strict')
    else:
        L.append(f'setblock {x} {y} {z} minecraft:rail[shape={sh}] strict')
    if i % 12 == 6 and not sh.startswith('asc'):
        L.append(f'setblock {x} {y - 2} {z} minecraft:sea_lantern strict')
# butée en bout de voie (l'arrivée remonte vers le nord, le départ est 3 blocs plus loin)
L.append(f'setblock {END[0]} {END[1]} {END[2] - 1} minecraft:polished_blackstone_wall strict')
w('coaster/track', L)

# effacement de l'ancienne voie à l'ouest (une fois) : rails, supports, lanternes, butée, gare, passerelle
O = ['# 🎢 Ancienne montagne russe (ouest, hors de l\'île) : on retire tout ce qu\'elle avait posé']
for (x, y, z) in OLD_P:
    O += [f'setblock {x} {y} {z} minecraft:air strict', f'setblock {x} {y - 1} {z} minecraft:air strict', f'setblock {x} {y - 2} {z} minecraft:air strict']
O += [f'setblock {OLD_P[-1][0] + 1} {OLD_P[-1][1]} {OLD_P[-1][2]} minecraft:air',
      'fill -130 62 -9 -110 68 3 minecraft:air',
      'kill @e[tag=mg.csd]']
for blk in ('spruce_planks', 'stripped_spruce_log', 'spruce_fence', 'lantern'):     # passerelle (hors des plots 7 et 8)
    O += [f'fill -115 62 15 -71 65 18 minecraft:air replace minecraft:{blk}', f'fill -116 62 4 -113 65 14 minecraft:air replace minecraft:{blk}']
w('coaster/clear_old', O)

sx, sy, sz = START
kx, ky, kz = KIOSK
w('coaster/build_start', ['# 🎢 Montagne russe : charge la zone puis construit (3 s plus tard)',
                          f'forceload add {BB[0]} {BB[2]} {BB[3]} {BB[5]}', 'forceload add -130 -12 -71 20',
                          'schedule function mg:coaster/build 3s'])
w('coaster/build', ['# 🎢 Montagne russe : guichet + voie autour du spawn',
                    'execute unless data storage mg:lobby coaster3 run function mg:coaster/clear_old',
                    # guichet au sol : petit kiosque en épicéa, plaque dorée au centre
                    f'fill {kx - 2} 63 {kz - 2} {kx + 2} 63 {kz + 2} minecraft:spruce_planks',
                    f'fill {kx - 2} 64 {kz - 2} {kx + 2} 67 {kz + 2} minecraft:air',
                    f'setblock {kx - 2} 64 {kz - 2} minecraft:spruce_log', f'setblock {kx + 2} 64 {kz - 2} minecraft:spruce_log',
                    f'setblock {kx - 2} 64 {kz + 2} minecraft:spruce_log', f'setblock {kx + 2} 64 {kz + 2} minecraft:spruce_log',
                    f'fill {kx - 2} 65 {kz - 2} {kx - 2} 66 {kz - 2} minecraft:spruce_log', f'fill {kx + 2} 65 {kz - 2} {kx + 2} 66 {kz - 2} minecraft:spruce_log',
                    f'fill {kx - 2} 65 {kz + 2} {kx - 2} 66 {kz + 2} minecraft:spruce_log', f'fill {kx + 2} 65 {kz + 2} {kx + 2} 66 {kz + 2} minecraft:spruce_log',
                    f'fill {kx - 2} 67 {kz - 2} {kx + 2} 67 {kz + 2} minecraft:spruce_slab[type=bottom]',
                    f'setblock {kx} 66 {kz} minecraft:lantern[hanging=true]',
                    f'setblock {kx} 63 {kz} minecraft:gold_block', f'setblock {kx} 64 {kz} minecraft:light_weighted_pressure_plate',
                    'function mg:coaster/track',
                    'kill @e[tag=mg.cst]', 'kill @e[tag=mg.csd]',
                    f'summon minecraft:text_display {kx}.5 66.2 {kz}.5 {{Tags:["mg.csd"],billboard:"center",text:[{{"text":"🎢 Montagne russe","color":"gold","bold":true}},{{"text":"\\nle tour du spawn — marche sur la plaque dorée","color":"gray"}}]}}',
                    f'forceload remove {BB[0]} {BB[2]} {BB[3]} {BB[5]}', 'forceload remove -130 -12 -71 20',
                    # la zone du spawn est aussi gardée chargée par core/forceloads : on la remet
                    'function mg:core/forceloads',
                    'data modify storage mg:lobby coaster1 set value 1b', 'data modify storage mg:lobby coaster2 set value 1b',
                    'data modify storage mg:lobby coaster3 set value 1b',
                    'tellraw @a[tag=mg.admin] {"text":"🎢 Montagne russe construite : tour du spawn, guichet au sud-ouest.","color":"gold"}'])
w('coaster/tick', ['# 🎢 Montagne russe — tick (seulement si quelqu\'un est au guichet ou en wagon)',
                   f'execute as @a[x={kx},y=64,z={kz},dx=0,dy=1,dz=0,tag=!mg.play,tag=!mg.csr] unless predicate mg:coaster_riding run function mg:coaster/board',
                   'tag @a[tag=mg.csr] remove mg.csr', f'tag @a[x={kx},y=64,z={kz},dx=0,dy=1,dz=0] add mg.csr',
                   # arrivée, abandon, chute
                   f'execute as @e[type=minecraft:minecart,tag=mg.cst,x={END[0] - 1},y={END[1] - 1},z={END[2] - 1},dx=2,dy=3,dz=3] run function mg:coaster/arrive',
                   'execute as @e[type=minecraft:minecart,tag=mg.cst] unless predicate mg:coaster_has_rider run kill @s',
                   f'execute as @e[type=minecraft:minecart,tag=mg.cst] at @s if entity @s[y=-64,dy={min(ys) - 6 + 64}] run kill @s'])
w('coaster/board', ['# @s monte dans un wagonnet, en haut de la voie (départ immédiat vers le nord)',
                    f'tp @s {sx}.5 {sy} {sz}.5 180 10',
                    f'summon minecraft:minecart {sx}.5 {sy} {sz}.5 {{Tags:["mg.cst","mg.csn"],Motion:[0d,0d,-0.4d]}}',
                    'ride @s mount @e[type=minecraft:minecart,tag=mg.csn,limit=1]', 'tag @e[tag=mg.csn] remove mg.csn',
                    'playsound minecraft:entity.minecart.riding master @s ~ ~ ~ 0.6 1.2',
                    'title @s actionbar {"text":"🎢 Accroche-toi !","color":"gold"}'])
w('coaster/arrive', ['# Wagonnet arrivé : le passager redescend au guichet',
                     'execute on passengers run tag @s add mg.csx', 'ride @a[tag=mg.csx,limit=1] dismount',
                     f'tp @a[tag=mg.csx] {kx}.5 64 {kz + 3}.5 0 0', 'tag @a[tag=mg.csx] remove mg.csx', 'kill @s'])
import os, json
os.makedirs(os.path.join(C.D, 'predicate'), exist_ok=True)
json.dump({'condition': 'minecraft:entity_properties', 'entity': 'this', 'predicate': {'vehicle': {}}},
          open(os.path.join(C.D, 'predicate/coaster_riding.json'), 'w'), indent=2)
json.dump({'condition': 'minecraft:entity_properties', 'entity': 'this', 'predicate': {'passenger': {}}},
          open(os.path.join(C.D, 'predicate/coaster_has_rider.json'), 'w'), indent=2)

TICK_OLD = 'execute if score $setup mg.st matches 1 if entity @a[x=-200,y=40,z=-60,dx=130,dy=80,dz=80] run function mg:coaster/tick'
TICK = 'execute if score $setup mg.st matches 1 if entity @a[x=-75,y=55,z=-75,dx=150,dy=60,dz=150] run function mg:coaster/tick'
C.patch('core/tick', 'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block 24 63 19 minecraft:gold_block run function mg:lobby/food_build', [TICK])
C.patch('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:lobby food1 run schedule function mg:lobby/food_build 12s',
        ['execute if score $setup mg.st matches 1 unless data storage mg:lobby coaster3 run schedule function mg:coaster/build_start 16s'])
C.patch('desinstaller', 'schedule clear mg:lobby/food_build',
        ['schedule clear mg:coaster/build_start', 'schedule clear mg:coaster/build', 'kill @e[tag=mg.cst]', 'kill @e[tag=mg.csd]',
         'data remove storage mg:lobby coaster1', 'data remove storage mg:lobby coaster2', 'data remove storage mg:lobby coaster3'])
# anciennes versions de ces lignes : retirées
for rel, gone in (('core/tick', TICK_OLD),
                  ('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:lobby coaster2 run schedule function mg:coaster/build_start 16s')):
    fp = os.path.join(C.D, 'function', rel + '.mcfunction')
    s = open(fp, encoding='utf-8').read().split('\n')
    open(fp, 'w', encoding='utf-8', newline='\n').write('\n'.join(l for l in s if l != gone))
print('Montagne russe OK :', len(P), 'rails, bbox', BB, 'fin', END)
