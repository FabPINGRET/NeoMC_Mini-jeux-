"""Quakecraft : cartes de sniper (longues lignes de tir, tours, portée du railgun portée à 120 blocs).

    python tools/quake/gen_sniper.py .        (depuis la racine du dépôt ; idempotent)

  $qm 8  « Ravin »  (id 79, centre 0 ~ 15450) : 41×121, deux plateaux face à face avec tours, ravin à découvert.
  $qm 9  « Tours »  (id 80, centre 0 ~ 15800) : plaine 101×101, 9 tours à échelles, murets bas.
Génère quake/build_5, quake/build_6 et applique les crochets (request, go, prepare, spread, shoot, forceloads, menus).
Relancer ensuite tools/variantes/gen_variants.py (étoiles, votes par carte).
"""
import json
import os
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
D = os.path.join(R, 'data/mg')
F = os.path.join(D, 'function')


def w(rel, lines):
    with open(os.path.join(F, rel + '.mcfunction'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


def clear(x1, x2, z1, z2, y1, y2):
    return [f'fill {x1} {y} {z1} {x2} {y} {z2} minecraft:air' for y in range(y1, y2 + 1)]


def barrier(x1, x2, z1, z2, y1, y2):
    return [f'fill {x1} {y1} {z1} {x2} {y2} {z1} minecraft:barrier', f'fill {x1} {y1} {z2} {x2} {y2} {z2} minecraft:barrier',
            f'fill {x1} {y1} {z1} {x1} {y2} {z2} minecraft:barrier', f'fill {x2} {y1} {z1} {x2} {y2} {z2} minecraft:barrier',
            f'fill {x1} {y2} {z1} {x2} {y2} {z2} minecraft:barrier']


def tower(cx, cz, y0, h, mat='minecraft:stone_bricks', ladder_face='south'):
    """Tour creuse 5×5 (y0 = sol), porte, échelle intérieure, plate-forme + parapet à créneaux."""
    top = y0 + h
    L = [f'fill {cx - 2} {y0} {cz - 2} {cx + 2} {top} {cz + 2} {mat}',
         f'fill {cx - 1} {y0} {cz - 1} {cx + 1} {top - 1} {cz + 1} minecraft:air',
         # porte côté sud (+z) et meurtrières
         f'fill {cx} {y0} {cz + 2} {cx} {y0 + 1} {cz + 2} minecraft:air',
         f'setblock {cx - 2} {y0 + h // 2} {cz} minecraft:air', f'setblock {cx + 2} {y0 + h // 2} {cz} minecraft:air',
         f'setblock {cx} {y0 + h // 2} {cz - 2} minecraft:air',
         # échelle contre le mur nord (intérieur), jusqu'au toit
         f'fill {cx} {y0} {cz - 1} {cx} {top} {cz - 1} minecraft:ladder[facing=south]',
         # parapet à créneaux
         f'fill {cx - 2} {top + 1} {cz - 2} {cx + 2} {top + 1} {cz + 2} minecraft:stone_brick_wall',
         f'fill {cx - 1} {top + 1} {cz - 1} {cx + 1} {top + 1} {cz + 1} minecraft:air',
         f'setblock {cx} {top + 1} {cz - 2} minecraft:air', f'setblock {cx} {top + 1} {cz + 2} minecraft:air',
         f'setblock {cx - 2} {top + 1} {cz} minecraft:air', f'setblock {cx + 2} {top + 1} {cz} minecraft:air',
         f'setblock {cx} {top + 1} {cz - 1} minecraft:air']
    return L


def rock(x, z, y=81, w_=3, h=2, d=2, mat='minecraft:andesite'):
    return [f'fill {x} {y} {z} {x + w_ - 1} {y + h - 1} {z + d - 1} {mat}',
            f'setblock {x + 1} {y + h} {z} minecraft:mossy_cobblestone']


# ------------------------------------------------------------- Ravin (0, 15450)
Z = 15450
L = ['# Quakecraft — carte sniper « Ravin » (centre 0 ~ 15450, 41×121), générée par tools/quake/gen_sniper.py']
L += clear(-22, 22, Z - 62, Z + 62, 60, 112)
L += [f'fill -20 79 {Z - 60} 20 79 {Z + 60} minecraft:dirt', f'fill -20 80 {Z - 60} 20 80 {Z + 60} minecraft:coarse_dirt',
      f'fill -20 80 {Z - 30} 20 80 {Z + 30} minecraft:gravel']
for s in (-1, 1):   # plateaux (y 81..86) aux deux bouts
    z1, z2 = (Z - 60, Z - 38) if s < 0 else (Z + 38, Z + 60)
    L += [f'fill -20 81 {z1} 20 85 {z2} minecraft:stone', f'fill -20 86 {z1} 20 86 {z2} minecraft:grass_block']
    # escaliers d'accès (x 14..18) depuis le ravin
    edge = z2 if s < 0 else z1
    for i in range(6):
        zz = edge - s * (6 - i)   # marche i : hauteur 81+i, du ravin vers le plateau
        L.append(f'fill 14 {81 + i} {zz} 18 {81 + i} {zz} minecraft:stone_brick_stairs[facing={"north" if s < 0 else "south"}]')
        if i:
            L.append(f'fill 14 81 {zz} 18 {80 + i} {zz} minecraft:stone')
    # escaliers symétriques côté x -18..-14
    for i in range(6):
        zz = edge - s * (6 - i)
        L.append(f'fill -18 {81 + i} {zz} -14 {81 + i} {zz} minecraft:stone_brick_stairs[facing={"north" if s < 0 else "south"}]')
        if i:
            L.append(f'fill -18 81 {zz} -14 {80 + i} {zz} minecraft:stone')
    # deux tours de tir sur chaque plateau, mur de protection au bord
    cz = Z - 50 if s < 0 else Z + 50
    L += tower(-11, cz, 87, 9) + tower(11, cz, 87, 9)
    wz = z2 if s < 0 else z1
    L += [f'fill -10 87 {wz} 10 87 {wz} minecraft:stone_brick_wall', f'fill -4 88 {wz} 4 88 {wz} minecraft:stone_brick_wall',
          f'fill -2 87 {wz} 2 88 {wz} minecraft:air']
# ravin : rochers, murets, arche centrale
for (x, z) in [(-16, -26), (8, -22), (-4, -14), (13, -6), (-14, 4), (2, 10), (-9, 18), (12, 24), (-2, -2)]:
    L += rock(x, Z + z)
L += [f'fill -20 81 {Z - 8} -12 82 {Z - 8} minecraft:cobblestone_wall', f'fill 12 81 {Z + 8} 20 82 {Z + 8} minecraft:cobblestone_wall',
      f'fill -3 81 {Z} -3 87 {Z} minecraft:sandstone', f'fill 3 81 {Z} 3 87 {Z} minecraft:sandstone', f'fill -3 88 {Z} 3 88 {Z} minecraft:sandstone',
      f'fill -2 81 {Z} 2 87 {Z} minecraft:air']
L += barrier(-21, 21, Z - 61, Z + 61, 60, 112)
w('quake/build_5', L)

# ------------------------------------------------------------- Tours (0, 15800)
Z2 = 15800
L = ['# Quakecraft — carte sniper « Tours » (centre 0 ~ 15800, 101×101), générée par tools/quake/gen_sniper.py']
L += clear(-52, 52, Z2 - 52, Z2 + 52, 60, 114)
L += [f'fill -50 79 {Z2 - 50} 50 79 {Z2 + 50} minecraft:dirt', f'fill -50 80 {Z2 - 50} 50 80 {Z2 + 50} minecraft:grass_block']
for gx in (-35, 0, 35):
    for gz in (-35, 0, 35):
        h = 16 if (gx, gz) == (0, 0) else (12 if gx and gz else 8)
        L += tower(gx, Z2 + gz, 81, h)
# murets bas et haies (couverture au sol)
for (x1, z1, x2, z2) in [(-25, -20, -12, -20), (12, -20, 25, -20), (-25, 20, -12, 20), (12, 20, 25, 20),
                          (-20, -12, -20, 12), (20, -12, 20, 12), (-45, -5, -40, -5), (40, 5, 45, 5), (-5, 40, 5, 40), (-5, -40, 5, -40)]:
    L.append(f'fill {x1} 81 {Z2 + z1} {x2} 81 {Z2 + z2} minecraft:cobblestone_wall')
for (x, z) in [(-28, -44), (27, -42), (-44, 26), (44, -27), (-8, 27), (9, -26), (-27, 8), (26, -9), (40, 42), (-42, -40)]:
    L += [f'fill {x} 81 {Z2 + z} {x + 2} 82 {Z2 + z + 1} minecraft:oak_leaves[persistent=true]', f'setblock {x + 1} 81 {Z2 + z} minecraft:hay_block']
L += barrier(-51, 51, Z2 - 51, Z2 + 51, 60, 114)
w('quake/build_6', L)


# ------------------------------------------------------------- crochets
def patch(rel, anchor, new_lines, where='after'):
    p = os.path.join(F, rel + '.mcfunction')
    lines = open(p, encoding='utf-8').read().split('\n')
    if all(l in lines for l in new_lines):
        return
    idx = [i for i, l in enumerate(lines) if l == anchor]
    if len(idx) != 1:
        raise SystemExit(f'{rel} : ancre {anchor!r} trouvée {len(idx)} fois')
    i = idx[0] + (1 if where == 'after' else 0)
    lines[i:i] = new_lines
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))


def replace(rel, old, new):
    p = os.path.join(F, rel + '.mcfunction')
    t = open(p, encoding='utf-8').read()
    if new in t:
        return
    assert t.count(old) == 1, (rel, old)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(t.replace(old, new))


replace('core/go', 'execute unless score @s mg.go matches 1..78 unless score @s mg.go matches 100..196',
        'execute unless score @s mg.go matches 1..80 unless score @s mg.go matches 100..196')
patch('core/request', 'execute if score $game mg.st matches 32..35 run scoreboard players set $game mg.st 31', [
    '# Quake sniper : 79 = Ravin, 80 = Tours → $qm 8 / 9',
    'execute if score $game mg.st matches 79 run scoreboard players set $qm mg.st 8',
    'execute if score $game mg.st matches 80 run scoreboard players set $qm mg.st 9',
    'execute if score $game mg.st matches 79..80 run scoreboard players set $game mg.st 31'])
ann = lambda qm, name, col, desc: (f'execute if score $game mg.st matches 31 if score $qm mg.st matches {qm} run tellraw @a ' + json.dumps([
    {'selector': '@s', 'color': 'yellow'}, {'text': ' lance une partie de ', 'color': 'gray'},
    {'text': f'QUAKECRAFT — {name} (SNIPER)', 'color': col, 'bold': True}, {'text': f' : {desc} !', 'color': 'gray'}], ensure_ascii=False))
first_q = next(l for l in open(os.path.join(F, 'core/request.mcfunction'), encoding='utf-8').read().split('\n')
               if l.startswith('execute if score $game mg.st matches 31 if score $qm mg.st matches 4 run tellraw'))
patch('core/request', first_q, [ann(8, 'RAVIN', 'gold', 'deux plateaux face à face, railgun longue portée'),
                                ann(9, 'TOURS', 'green', '9 tours dans une grande plaine, railgun longue portée')])
for qm, build, g, t, z in [(8, 'quake/build_5', 25, 9600, 15450), (9, 'quake/build_6', 30, 12000, 15800)]:
    patch('quake/prepare', 'kill @e[distance=0..,type=minecraft:item]', [
        f'execute if score $qm mg.st matches {qm} run function mg:{build}',
        f'execute if score $qm mg.st matches {qm} run scoreboard players set $qg mg.st {g}',
        f'execute if score $qm mg.st matches {qm} run scoreboard players set $qt mg.st {t}',
        f'execute if score $qm mg.st matches {qm} run scoreboard players set $pz mg.st {z}'], where='before')
patch('quake/prepare', 'scoreboard players set @a[tag=mg.play] mg.qk 0', [
    'execute if score $qm mg.st matches 8 run spawnpoint @a[tag=mg.play] 0 87 15400',
    'execute if score $qm mg.st matches 9 run spawnpoint @a[tag=mg.play] 0 81 15770'], where='before')
# placement : Ravin = sur un des deux plateaux au hasard ; Tours = plaine entière
patch('quake/spread_one', '# Quakecraft — placement aléatoire selon la carte (@s)', [
    'execute if score $qm mg.st matches 8 store result score $qsr mg.st run random value 0..1',
    'execute if score $qm mg.st matches 8 if score $qsr mg.st matches 0 run spreadplayers 0 15401 2 9 under 90 false @s',
    'execute if score $qm mg.st matches 8 if score $qsr mg.st matches 1 run spreadplayers 0 15499 2 9 under 90 false @s',
    'execute if score $qm mg.st matches 9 run spreadplayers 0 15800 4 46 under 90 false @s'])
patch('quake/spread_all', '# Quakecraft — placement aléatoire selon la carte (@a[tag=mg.play])', [
    'execute if score $qm mg.st matches 8..9 as @a[tag=mg.play] run function mg:quake/spread_one'])
patch('quake/shoot', 'scoreboard players set $rs mg.st 140', [
    '# cartes sniper : portée 120 blocs',
    'execute if score $ar mg.st matches 0 if score $qm mg.st matches 8..9 run scoreboard players set $rs mg.st 240'])
patch('core/forceloads', 'function mg:tnttag/map/fl', ['# Quake sniper (Ravin z 15450, Tours z 15800)',
                                                       'forceload add -24 15386 24 15514', 'forceload add -54 15746 54 15854'], where='before')
# menus
p = os.path.join(D, 'dialog/quakemaps.json')
d = json.load(open(p, encoding='utf-8'))
cmds = [a.get('action', {}).get('command') for a in d['actions']]
for gid, name, col, tip in [(80, 'Tours', 'green', 'Sniper : plaine 101×101, 9 tours à échelles, portée 120 blocs'),
                            (79, 'Ravin', 'gold', 'Sniper : 41×121, deux plateaux face à face, portée 120 blocs')]:
    if f'trigger mg.go set {gid}' in cmds:
        continue
    pos = next(i for i, c in enumerate(cmds) if c == 'trigger mg.go set 49') + 1
    d['actions'].insert(pos, {'label': [{'text': f'🎯 {name}', 'color': col}], 'tooltip': [{'text': tip, 'color': 'gray'}],
                              'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.go set {gid}'}})
    cmds = [a.get('action', {}).get('command') for a in d['actions']]
with open(p, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
    f.write('\n')
chat = [l for l in open(os.path.join(F, 'core/menu_quake_chat.mcfunction'), encoding='utf-8').read().split('\n') if 'mg.go set 49' in l][0]
patch('core/menu_quake_chat', chat, ['tellraw @s ' + json.dumps(['', {'text': ' [🎯 Ravin (sniper)]', 'color': 'gold',
                                                                     'click_event': {'action': 'run_command', 'command': 'trigger mg.go set 79'}},
                                                               {'text': ' [🎯 Tours (sniper)]', 'color': 'green',
                                                                'click_event': {'action': 'run_command', 'command': 'trigger mg.go set 80'}}], ensure_ascii=False)])
print('Quake sniper : build_5 (Ravin), build_6 (Tours) + crochets')
