"""Quakecraft : petites cartes tout en hauteur (plusieurs étages, tremplins).

    python tools/quake/gen_vertical.py .        (depuis la racine du dépôt ; idempotent, après gen_sniper.py)

  $qm 10 « Spirale »  (id 233, centre 0 ~ 16100) : 27×27, pyramide centrale, balcon tout autour (y 86), boucle suspendue (y 94).
  $qm 11 « Chantier » (id 234, centre 0 ~ 16400) : 25×25, immeuble en construction à 3 étages, échafaudage, grue.
Tremplins : bloc de slime = petit saut (≈ 6 blocs), bloc d'émeraude = grand saut (≈ 10 blocs) — mg:quake/pads.
Pas de dégâts de chute en Quakecraft (attribut à 0 hors jeux qui l'activent).
Génère quake/build_7, quake/build_8, quake/pads et applique les crochets (request, go, prepare, spread, tick, forceloads, menus).
Relancer ensuite tools/variantes/gen_variants.py (étoiles, votes par carte).
"""
import json
import os
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
D = os.path.join(R, 'data/mg')
F = os.path.join(D, 'function')
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
import mcfn
_fn = mcfn.Fn(F)
w, patch, go_range = _fn.write, _fn.patch, _fn.go_range


def clear(x1, x2, z1, z2, y1, y2):
    return [f'fill {x1} {y} {z1} {x2} {y} {z2} minecraft:air' for y in range(y1, y2 + 1)]


def barrier(x1, x2, z1, z2, y1, y2):
    return [f'fill {x1} {y1} {z1} {x2} {y2} {z1} minecraft:barrier', f'fill {x1} {y1} {z2} {x2} {y2} {z2} minecraft:barrier',
            f'fill {x1} {y1} {z1} {x1} {y2} {z2} minecraft:barrier', f'fill {x2} {y1} {z1} {x2} {y2} {z2} minecraft:barrier',
            f'fill {x1} {y2} {z1} {x2} {y2} {z2} minecraft:barrier']


STAIR = {(1, 0): 'east', (-1, 0): 'west', (0, 1): 'south', (0, -1): 'north'}


def ramp(x0, z0, dx, dz, y0, n, wx, wz, width=2, stairs='minecraft:polished_blackstone_brick_stairs', mat='minecraft:polished_blackstone_bricks'):
    """Escalier de n marches qui monte dans la direction (dx, dz) depuis (x0, y0, z0), largeur `width` vers (wx, wz)"""
    L = []
    for i in range(n):
        x, z, y = x0 + dx * i, z0 + dz * i, y0 + i
        for k in range(width):
            xx, zz = x + wx * k, z + wz * k
            if y > y0:
                L.append(f'fill {xx} {y0} {zz} {xx} {y - 1} {zz} {mat}')
            L.append(f'setblock {xx} {y} {zz} {stairs}[facing={STAIR[(dx, dz)]}]')
    return L


# ------------------------------------------------------------- Spirale (0, 16100)
Z = 16100
L = ['# Quakecraft — carte verticale « Spirale » (centre 0 ~ 16100, 27×27), générée par tools/quake/gen_vertical.py']
L += clear(-16, 16, Z - 16, Z + 16, 60, 110)
L += [f'fill -13 79 {Z - 13} 13 79 {Z + 13} minecraft:deepslate', f'fill -13 80 {Z - 13} 13 80 {Z + 13} minecraft:polished_deepslate',
      f'fill -1 80 {Z - 13} 1 80 {Z + 13} minecraft:deepslate_tiles', f'fill -13 80 {Z - 1} 13 80 {Z + 1} minecraft:deepslate_tiles']
# balcon tout autour (sol y 85), piliers dessous, garde-corps intérieur à trous
L += [f'fill -13 85 {Z - 13} 13 85 {Z + 13} minecraft:polished_blackstone_bricks', f'fill -9 85 {Z - 9} 9 85 {Z + 9} minecraft:air']
for x in (-11, 0, 11):
    for z in (-11, 0, 11):
        if (x, z) != (0, 0):
            L.append(f'fill {x} 81 {Z + z} {x} 84 {Z + z} minecraft:polished_blackstone')
for s in (-10, 10):
    L += [f'fill -10 86 {Z + s} 10 86 {Z + s} minecraft:polished_blackstone_wall', f'fill {s} 86 {Z - 10} {s} 86 {Z + 10} minecraft:polished_blackstone_wall']
    for k in (-6, -2, 2, 6):
        L += [f'setblock {k} 86 {Z + s} minecraft:air', f'setblock {s} 86 {Z + k} minecraft:air']
# 4 escaliers du sol au balcon (le long du bord intérieur)
L += ramp(-8, Z + 8, 1, 0, 81, 5, 0, 1) + ramp(8, Z - 9, -1, 0, 81, 5, 0, 1) + ramp(-9, Z - 8, 0, 1, 81, 5, 1, 0) + ramp(8, Z + 8, 0, -1, 81, 5, 1, 0)
# passages dans le garde-corps en haut des escaliers
L += [f'setblock -4 86 {Z + 10} minecraft:air', f'setblock 4 86 {Z - 10} minecraft:air', f'setblock -10 86 {Z - 4} minecraft:air', f'setblock 10 86 {Z + 4} minecraft:air']
# pyramide centrale à gradins (escalade en sautant), sommet y 86
for t in range(6):
    h = 5 - t
    L.append(f'fill {-h} {81 + t} {Z - h} {h} {81 + t} {Z + h} minecraft:{"tuff_bricks" if t % 2 == 0 else "polished_tuff"}')
# boucle suspendue (y 93) : 4 plates-formes 5×5 reliées par des passerelles d'un bloc
for sx in (-8, 8):
    for sz in (-8, 8):
        L += [f'fill {sx - 2} 93 {Z + sz - 2} {sx + 2} 93 {Z + sz + 2} minecraft:dark_prismarine',
              f'setblock {sx} 92 {Z + sz} minecraft:sea_lantern']
for s in (-8, 8):
    L += [f'fill -5 93 {Z + s} 5 93 {Z + s} minecraft:prismarine_bricks', f'fill {s} 93 {Z - 5} {s} 93 {Z + 5} minecraft:prismarine_bricks']
# croix au-dessus de la pyramide (relie les 4 passerelles)
L += [f'fill 0 93 {Z - 7} 0 93 {Z + 7} minecraft:prismarine_bricks', f'fill -7 93 {Z} 7 93 {Z} minecraft:prismarine_bricks',
      f'fill -1 93 {Z - 1} 1 93 {Z + 1} minecraft:dark_prismarine']
# tremplins : sol → balcon (slime), balcon → boucle (émeraude)
for (x, z) in [(-6, 0), (6, 0), (0, -6), (0, 6)]:
    L.append(f'setblock {x} 80 {Z + z} minecraft:slime_block')
for (x, z) in [(-12, -12), (12, -12), (-12, 12), (12, 12)]:
    L.append(f'setblock {x} 85 {Z + z} minecraft:emerald_block')
# abris au sol et lumière
for (x, z) in [(-5, -9), (5, 9), (-9, 5), (9, -5)]:
    L += [f'fill {x - 1} 81 {Z + z} {x + 1} 82 {Z + z} minecraft:tuff_brick_wall']
for x in (-12, 12):
    for z in (-6, 6):
        L += [f'setblock {x} 84 {Z + z} minecraft:sea_lantern', f'setblock {z} 84 {Z + x} minecraft:sea_lantern']
L += barrier(-14, 14, Z - 14, Z + 14, 60, 110)
w('quake/build_7', L)

# ------------------------------------------------------------- Chantier (0, 16400)
Z2 = 16400
L = ['# Quakecraft — carte verticale « Chantier » (centre 0 ~ 16400, 25×25), générée par tools/quake/gen_vertical.py']
L += clear(-15, 15, Z2 - 15, Z2 + 15, 60, 110)
L += [f'fill -12 79 {Z2 - 12} 12 79 {Z2 + 12} minecraft:dirt', f'fill -12 80 {Z2 - 12} 12 80 {Z2 + 12} minecraft:gravel',
      f'fill -12 80 {Z2 + 9} 12 80 {Z2 + 12} minecraft:coarse_dirt', f'fill 8 80 {Z2 - 12} 12 80 {Z2 - 8} minecraft:packed_mud']
# poteaux (y 81..95), 3 dalles percées
for x in (-7, 0, 7):
    for z in (-7, 0, 7):
        L.append(f'fill {x} 81 {Z2 + z} {x} 95 {Z2 + z} minecraft:gray_concrete')
L += [f'fill -7 85 {Z2 - 7} 7 85 {Z2 + 7} minecraft:smooth_stone', f'fill 1 85 {Z2 - 5} 5 85 {Z2 - 1} minecraft:air',
      f'fill -7 90 {Z2 - 7} 7 90 {Z2} minecraft:smooth_stone', f'fill -7 90 {Z2 + 1} 0 90 {Z2 + 7} minecraft:smooth_stone',
      f'fill -7 95 {Z2 - 7} -1 95 {Z2 - 1} minecraft:smooth_stone']
for x in (-7, 0, 7):
    for z in (-7, 0, 7):
        L.append(f'fill {x} 85 {Z2 + z} {x} 85 {Z2 + z} minecraft:gray_concrete')
# garde-corps provisoires (barrières rouges et blanches) au bord des dalles, avec des trous
L += [f'fill -7 86 {Z2 + 7} 7 86 {Z2 + 7} minecraft:red_concrete_powder', f'fill -7 91 {Z2 - 7} 7 91 {Z2 - 7} minecraft:white_concrete_powder']
for k in (-5, -1, 3):
    L += [f'fill {k} 86 {Z2 + 7} {k + 1} 86 {Z2 + 7} minecraft:air', f'fill {k} 91 {Z2 - 7} {k + 1} 91 {Z2 - 7} minecraft:air']
# échafaudage à l'ouest (du sol au toit) et échelles sur deux poteaux
L += [f'fill -10 81 {Z2 - 2} -9 95 {Z2 + 2} minecraft:scaffolding', f'fill -10 81 {Z2} -9 95 {Z2} minecraft:air',
      f'fill 8 81 {Z2} 8 95 {Z2} minecraft:ladder[facing=east]', f'fill 0 81 {Z2 + 8} 0 90 {Z2 + 8} minecraft:ladder[facing=south]']
# grue sur le toit : mât à échelle + flèche (perchoir de tireur, y 104)
L += [f'fill -4 96 {Z2 - 4} -4 104 {Z2 - 4} minecraft:yellow_concrete', f'fill -3 96 {Z2 - 4} -3 104 {Z2 - 4} minecraft:ladder[facing=east]',
      f'fill -2 104 {Z2 - 4} 10 104 {Z2 - 4} minecraft:yellow_concrete', f'fill -7 104 {Z2 - 4} -5 105 {Z2 - 4} minecraft:yellow_concrete',
      f'fill 10 100 {Z2 - 4} 10 103 {Z2 - 4} minecraft:iron_chain', f'fill 9 99 {Z2 - 5} 11 99 {Z2 - 3} minecraft:stripped_spruce_wood']
# tremplins : sol → 1er étage (slime), 1er → 2e (émeraude sous le vide du 2e étage), sol → 2e (émeraude)
L += [f'setblock 9 80 {Z2 + 3} minecraft:slime_block', f'setblock -9 80 {Z2 + 6} minecraft:slime_block', f'setblock 3 80 {Z2 - 9} minecraft:slime_block',
      f'setblock 4 85 {Z2 + 4} minecraft:emerald_block', f'setblock 10 80 {Z2 + 10} minecraft:emerald_block']
# matériaux du chantier (abris au sol)
for (x, z, b) in [(-10, -10, 'bricks'), (-4, 10, 'bricks'), (10, -6, 'stone_bricks'), (4, -10, 'oak_planks'), (-11, 9, 'stone_bricks')]:
    L += [f'fill {x} 81 {Z2 + z} {x + 1} 82 {Z2 + z + 1} minecraft:{b}', f'setblock {x} 83 {Z2 + z} minecraft:{b}']
L += [f'fill 3 81 {Z2 + 10} 4 82 {Z2 + 10} minecraft:barrel[facing=up]', f'setblock -2 81 {Z2 - 11} minecraft:cauldron']
for (x, y, z) in [(-7, 89, 3), (7, 89, -3), (-3, 94, -7), (3, 84, 7)]:
    L.append(f'setblock {x} {y} {Z2 + z} minecraft:lantern[hanging=true]')
L += barrier(-13, 13, Z2 - 13, Z2 + 13, 60, 110)
w('quake/build_8', L)

# tremplins (contexte : $qm 10..11)
w('quake/pads', ['# Quakecraft (cartes verticales) : tremplins — slime = petit saut, émeraude = grand saut',
                 'execute as @a[tag=mg.play,gamemode=adventure] at @s if block ~ ~-0.3 ~ minecraft:slime_block run function mg:quake/pad {a:5}',
                 'execute as @a[tag=mg.play,gamemode=adventure] at @s if block ~ ~-0.3 ~ minecraft:emerald_block run function mg:quake/pad {a:9}'])
w('quake/pad', ['# @s sur un tremplin : envolée d\'une seconde (macro : $(a) = force)', '$effect give @s minecraft:levitation 1 $(a) true',
                'effect give @s minecraft:slow_falling 3 0 true', 'playsound minecraft:entity.breeze.jump player @a ~ ~ ~ 0.8 1.2',
                'particle minecraft:gust ~ ~0.2 ~ 0.3 0.1 0.3 0 3'])


# ------------------------------------------------------------- crochets
go_range(234)
patch('core/request', 'execute if score $game mg.st matches 79..80 run scoreboard players set $game mg.st 31', [
    '# Quake vertical : 233 = Spirale, 234 = Chantier → $qm 10 / 11',
    'execute if score $game mg.st matches 233 run scoreboard players set $qm mg.st 10',
    'execute if score $game mg.st matches 234 run scoreboard players set $qm mg.st 11',
    'execute if score $game mg.st matches 233..234 run scoreboard players set $game mg.st 31'])
ann = lambda qm, name, col, desc: (f'execute if score $game mg.st matches 31 if score $qm mg.st matches {qm} run tellraw @a ' + json.dumps([
    {'selector': '@s', 'color': 'yellow'}, {'text': ' lance une partie de ', 'color': 'gray'},
    {'text': f'QUAKECRAFT — {name}', 'color': col, 'bold': True}, {'text': f' : {desc} !', 'color': 'gray'}], ensure_ascii=False))
first_q = next(l for l in open(os.path.join(F, 'core/request.mcfunction'), encoding='utf-8').read().split('\n')
               if l.startswith('execute if score $game mg.st matches 31 if score $qm mg.st matches 4 run tellraw'))
patch('core/request', first_q, [ann(10, 'SPIRALE', 'light_purple', 'petite arène sur 3 niveaux, tremplins'),
                                ann(11, 'CHANTIER', 'yellow', 'immeuble en construction, échafaudage et grue')])
for qm, build, g, t, z in [(10, 'quake/build_7', 20, 7200, 16100), (11, 'quake/build_8', 20, 7200, 16400)]:
    patch('quake/prepare', 'kill @e[distance=0..,type=minecraft:item]', [
        f'execute if score $qm mg.st matches {qm} run function mg:{build}',
        f'execute if score $qm mg.st matches {qm} run scoreboard players set $qg mg.st {g}',
        f'execute if score $qm mg.st matches {qm} run scoreboard players set $qt mg.st {t}',
        f'execute if score $qm mg.st matches {qm} run scoreboard players set $pz mg.st {z}'], where='before')
patch('quake/prepare', 'scoreboard players set @a[tag=mg.play] mg.qk 0', [
    'execute if score $qm mg.st matches 10 run spawnpoint @a[tag=mg.play] 0 87 16100',
    'execute if score $qm mg.st matches 11 run spawnpoint @a[tag=mg.play] 0 81 16410'], where='before')
# placement : toute la carte, tous niveaux (sous le plafond de barrières)
patch('quake/spread_one', '# Quakecraft — placement aléatoire selon la carte (@s)', [
    'execute if score $qm mg.st matches 10 run spreadplayers 0 16100 3 12 under 100 false @s',
    'execute if score $qm mg.st matches 11 run spreadplayers 0 16400 3 11 under 100 false @s'])
patch('quake/spread_all', '# Quakecraft — placement aléatoire selon la carte (@a[tag=mg.play])', [
    'execute if score $qm mg.st matches 10..11 as @a[tag=mg.play] run function mg:quake/spread_one'])
patch('quake/tick', '# Minuteur', ['# Cartes verticales : tremplins', 'execute if score $ar mg.st matches 0 if score $qm mg.st matches 10..11 run function mg:quake/pads', ''],
      where='before')
patch('core/forceloads', 'function mg:tnttag/map/fl', ['# Quake vertical (Spirale z 16100, Chantier z 16400)',
                                                       'forceload add -16 16084 16 16116', 'forceload add -15 16385 15 16415'], where='before')
# menus
p = os.path.join(D, 'dialog/quakemaps.json')
d = json.load(open(p, encoding='utf-8'))
cmds = [a.get('action', {}).get('command') for a in d['actions']]
for gid, name, col, tip in [(234, '🏗 Chantier', 'yellow', 'Vertical : 25×25, immeuble à 3 étages, échafaudage, grue, tremplins'),
                            (233, '🌀 Spirale', 'light_purple', 'Vertical : 27×27, pyramide, balcon et boucle suspendue, tremplins')]:
    if f'trigger mg.go set {gid}' in cmds:
        continue
    pos = next(i for i, c in enumerate(cmds) if c == 'trigger mg.go set 80') + 1
    d['actions'].insert(pos, {'label': [{'text': name, 'color': col}], 'tooltip': [{'text': tip, 'color': 'gray'}],
                              'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.go set {gid}'}})
    cmds = [a.get('action', {}).get('command') for a in d['actions']]
with open(p, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
    f.write('\n')
chat = [l for l in open(os.path.join(F, 'core/menu_quake_chat.mcfunction'), encoding='utf-8').read().split('\n') if 'mg.go set 80' in l][0]
patch('core/menu_quake_chat', chat, ['tellraw @s ' + json.dumps(['', {'text': ' [🌀 Spirale (vertical)]', 'color': 'light_purple',
                                                                     'click_event': {'action': 'run_command', 'command': 'trigger mg.go set 233'}},
                                                               {'text': ' [🏗 Chantier (vertical)]', 'color': 'yellow',
                                                                'click_event': {'action': 'run_command', 'command': 'trigger mg.go set 234'}}], ensure_ascii=False)])
print('Quake vertical : build_7 (Spirale), build_8 (Chantier) + crochets')

import runpy
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rating', 'gen_rating.py'), run_name='__main__')
