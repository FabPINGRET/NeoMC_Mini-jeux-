"""⚡ Tron — à pied (id 84) et à cheval « moto » (id 85). Arène 61×61 en z 20000.

    python tools/arcade/gen_tron.py .

Chaque joueur laisse un mur de laine de sa couleur (2 blocs de haut) derrière lui ; toucher un mur (le sien
compris, sauf le bloc qu'il vient de quitter) ou la bordure = éliminé ; rester immobile 2,5 s = éliminé.
Pas de saut. Dernier en vie gagne. Moto : monture rapide, descendre = éliminé.
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
Z = 20000
COLORS = ['red', 'blue', 'lime', 'yellow', 'orange', 'magenta', 'cyan', 'white', 'purple', 'pink', 'light_blue', 'green',
          'brown', 'light_gray', 'gray', 'black']
TXT = ['red', 'blue', 'green', 'yellow', 'gold', 'light_purple', 'dark_aqua', 'white', 'dark_purple', 'light_purple', 'aqua',
       'dark_green', 'gold', 'gray', 'dark_gray', 'black']

L = ['# ⚡ Tron — arène 61×61 (centre 0 80 20000), sol sombre quadrillé, bordure lumineuse (touche = éliminé)']
L += [f'fill -32 {y} {Z - 32} 32 {y} {Z + 32} minecraft:air' for y in range(79, 92)]
L += [f'fill -31 79 {Z - 31} 31 79 {Z + 31} minecraft:barrier', f'fill -30 80 {Z - 30} 30 80 {Z + 30} minecraft:black_concrete']
for k in range(-30, 31, 6):
    L += [f'fill {k} 80 {Z - 30} {k} 80 {Z + 30} minecraft:gray_concrete', f'fill -30 80 {Z + k} 30 80 {Z + k} minecraft:gray_concrete']
L += ['fill -31 80 {0} 31 82 {0} minecraft:cyan_stained_glass'.format(Z - 31), 'fill -31 80 {0} 31 82 {0} minecraft:cyan_stained_glass'.format(Z + 31),
      f'fill -31 80 {Z - 30} -31 82 {Z + 30} minecraft:cyan_stained_glass', f'fill 31 80 {Z - 30} 31 82 {Z + 30} minecraft:cyan_stained_glass',
      f'fill -31 83 {Z - 31} 31 90 {Z - 31} minecraft:barrier', f'fill -31 83 {Z + 31} 31 90 {Z + 31} minecraft:barrier',
      f'fill -31 83 {Z - 30} -31 90 {Z + 30} minecraft:barrier', f'fill 31 83 {Z - 30} 31 90 {Z + 30} minecraft:barrier',
      f'fill -31 91 {Z - 31} 31 91 {Z + 31} minecraft:barrier']
w('tron/build', L)
import json, os
os.makedirs(os.path.join(C.D, 'tags/block'), exist_ok=True)
json.dump({'values': ['#minecraft:wool', 'minecraft:cyan_stained_glass']}, open(os.path.join(C.D, 'tags/block/tron_wall.json'), 'w'), indent=2)

w('tron/prepare', [
    '# ⚡ Tron — préparation ($trm : 0 à pied, 1 moto)',
    'scoreboard players set $trm mg.st 0', 'execute if score $game mg.st matches 85 run scoreboard players set $trm mg.st 1',
    'function mg:tron/build', 'kill @e[tag=mg.trm]', 'kill @e[tag=mg.trp]', 'kill @e[tag=mg.trh]',
    'scoreboard players set $tk mg.st 0', 'execute as @a[tag=mg.play,sort=random] run function mg:tron/assign',
    'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 100', f'scoreboard players set $pz mg.st {Z}',
    'gamemode adventure @a[tag=mg.play]', f'execute as @a[tag=mg.play] run spawnpoint @s 0 81 {Z}',
    'clear @a[tag=mg.play]',
    f'spreadplayers 0 {Z} 7 24 under 82 false @a[tag=mg.play]',
    f'execute as @a[tag=mg.play] at @s run tp @s ~ ~ ~ facing 0 81 {Z}',
    'execute as @a[tag=mg.play] run attribute @s minecraft:jump_strength base set 0',
    'execute if score $trm mg.st matches 1 as @a[tag=mg.play] at @s run function mg:tron/horse'])
w('tron/assign', ['scoreboard players operation @s mg.trc = $tk mg.st', 'scoreboard players add $tk mg.st 1',
                  'execute if score $tk mg.st matches 16.. run scoreboard players set $tk mg.st 0'])
w('tron/horse', ['# @s = joueur : sa moto (cheval rapide, sans saut, increvable)',
                 'summon minecraft:horse ~ ~ ~ {Tags:["mg.trh","mg.trnew"],Tame:1b,PersistenceRequired:1b,Invulnerable:1b,Silent:1b,'
                 'equipment:{saddle:{id:"minecraft:saddle",count:1}},'
                 'attributes:[{id:"minecraft:movement_speed",base:0.32d},{id:"minecraft:jump_strength",base:0.0d},{id:"minecraft:step_height",base:0.0d}]}',
                 'scoreboard players operation @e[tag=mg.trnew,limit=1] mg.trc = @s mg.trc',
                 'ride @s mount @e[tag=mg.trnew,limit=1]', 'tag @e[tag=mg.trnew] remove mg.trnew'])
w('tron/go', ['# Départ : marqueurs de traînée, vitesse', 'scoreboard players set $trt mg.st 0',
              'execute as @a[tag=mg.play] run function mg:tron/go_one',
              'execute if score $trm mg.st matches 0 run effect give @a[tag=mg.play] minecraft:speed infinite 1 true',
              'effect give @a[tag=mg.play] minecraft:saturation infinite 0 true', 'effect give @a[tag=mg.play] minecraft:resistance infinite 4 true',
              'tellraw @a[tag=mg.play] ' + js([{'text': '⚡ TRON : ', 'color': 'aqua', 'bold': True},
                                               {'text': 'tu laisses un mur derrière toi. Touche un mur (même le tien) ou la bordure = éliminé. Interdit de s’arrêter plus de 2 s. Dernier en vie gagne !', 'color': 'gray'}]),
              'execute if score $trm mg.st matches 1 run tellraw @a[tag=mg.play] {"text":"🏍 Moto : tu ne peux pas descendre, fonce !","color":"gold"}'])
w('tron/go_one', ['# @s = joueur : marqueurs « bloc courant » (mg.trm) et « dernier mur posé » (mg.trp)',
                  'execute at @s run summon minecraft:marker ~ ~ ~ {Tags:["mg.trm","mg.trnew"]}',
                  'execute at @s run summon minecraft:marker ~ ~ ~ {Tags:["mg.trp","mg.trnew"]}',
                  'scoreboard players operation @e[tag=mg.trnew] mg.trc = @s mg.trc', 'tag @e[tag=mg.trnew] remove mg.trnew',
                  'scoreboard players set @s mg.trs 0'])
w('tron/tick', ['# ⚡ Tron — tick', 'scoreboard players add $trt mg.st 1',
                'execute as @a[tag=mg.play] run function mg:tron/step',
                'execute store result score $alive mg.st if entity @a[tag=mg.play]',
                'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run function mg:core/win_player',
                'execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw'])
w('tron/step', [
    '# @s = joueur : porteur (lui-même ou sa moto), collision, traînée, immobilité',
    'tag @s add mg.tme', 'scoreboard players operation $tid mg.st = @s mg.trc',
    'execute if score $trm mg.st matches 0 run tag @s add mg.tcar',
    'execute if score $trm mg.st matches 1 on vehicle run tag @s add mg.tcar',
    'execute if score $trm mg.st matches 1 unless entity @e[tag=mg.tcar] run function mg:tron/remount',
    'execute if score $trm mg.st matches 1 on vehicle run tag @s add mg.tcar',
    'execute if score $trm mg.st matches 1 unless entity @e[tag=mg.tcar] run return run function mg:tron/out_dismount',
    'execute as @e[tag=mg.trm] if score @s mg.trc = $tid mg.st run tag @s add mg.tcm',
    'execute as @e[tag=mg.trp] if score @s mg.trc = $tid mg.st run tag @s add mg.tpm',
    'scoreboard players set $tdead mg.st 0',
    'execute if score $trt mg.st matches 20.. as @e[tag=mg.tcar,limit=1] at @s run function mg:tron/probe',
    'scoreboard players add @s mg.trs 1',
    'execute as @e[tag=mg.tcm,limit=1] at @s align xyz unless entity @e[tag=mg.tcar,dx=0,dy=0,dz=0] run function mg:tron/lay',
    'tag @e remove mg.tcar', 'tag @e remove mg.tcm', 'tag @e remove mg.tpm', 'tag @s remove mg.tme',
    'execute if score $tdead mg.st matches 1 run return run function mg:tron/out_wall',
    'execute if score @s mg.trs matches 50.. run return run function mg:tron/out_still',
    'execute if score @s mg.trs matches 25 run title @s actionbar {"text":"⚠ Avance ! (immobile = éliminé)","color":"red"}'])
probe = ['# @s = porteur : touche-t-il un mur ? (4 sondes à mi-hauteur, hors bloc courant et dernier mur posé)',
         'execute if score $trm mg.st matches 0 run scoreboard players set $trr mg.st 0']
for r, cond in [('0.36', 0), ('0.78', 1)]:
    for dx, dz in [(r, '0'), ('-' + r, '0'), ('0', r), ('0', '-' + r)]:
        probe.append(f'execute if score $trm mg.st matches {cond} positioned ~{dx if dx != "0" else ""} ~0.5 ~{dz if dz != "0" else ""} align xyz '
                     f'unless entity @e[tag=mg.tpm,dx=0,dy=0,dz=0] unless entity @e[tag=mg.tcm,dx=0,dy=0,dz=0] '
                     f'if block ~ ~ ~ #mg:tron_wall run scoreboard players set $tdead mg.st 1')
w('tron/probe', probe)
lay = ['# @s = marqueur du bloc courant (position = coin du bloc) : le porteur l\'a quitté → mur de 2 blocs à sa couleur']
for k, c in enumerate(COLORS):
    lay.append(f'execute if score @s mg.trc matches {k} run fill ~ ~ ~ ~ ~1 ~ minecraft:{c}_wool replace #minecraft:air')
lay += ['tp @e[tag=mg.tpm,limit=1] @s', 'tp @s @e[tag=mg.tcar,limit=1]', 'scoreboard players set @a[tag=mg.tme] mg.trs 0']
w('tron/lay', lay)
w('tron/remount', ['# @s est descendu : on le remet sur sa moto (Maj ne sert à rien)',
                   'execute as @e[tag=mg.trh] if score @s mg.trc = $tid mg.st run tag @s add mg.thm',
                   'ride @s mount @e[tag=mg.thm,limit=1]', 'tag @e remove mg.thm'])
w('tron/out_wall', ['tellraw @a [{"selector":"@s","color":"yellow"},{"text":" s\'est écrasé contre un mur !","color":"gray"}]', 'function mg:tron/out'])
w('tron/out_still', ['tellraw @a [{"selector":"@s","color":"yellow"},{"text":" s\'est arrêté trop longtemps !","color":"gray"}]', 'function mg:tron/out'])
w('tron/out_dismount', ['tellraw @a [{"selector":"@s","color":"yellow"},{"text":" est descendu de sa moto !","color":"gray"}]', 'function mg:tron/out'])
w('tron/out', ['# @s éliminé : ses marqueurs et sa moto disparaissent, ses murs restent',
               'tag @s remove mg.tme', 'scoreboard players operation $tid mg.st = @s mg.trc', 'ride @s dismount',
               'execute as @e[tag=mg.trm] if score @s mg.trc = $tid mg.st run kill @s', 'execute as @e[tag=mg.trp] if score @s mg.trc = $tid mg.st run kill @s',
               'execute as @e[tag=mg.trh] if score @s mg.trc = $tid mg.st run tp @s ~ -100 ~',
               'execute at @s run particle minecraft:explosion ~ ~1 ~ 0.3 0.3 0.3 0 3', 'execute at @s run playsound minecraft:entity.generic.explode master @a ~ ~ ~ 0.6 1.6',
               'attribute @s minecraft:jump_strength base reset', 'function mg:core/eliminate'])
w('tron/cleanup', ['execute as @a run ride @s dismount', 'kill @e[tag=mg.trm]', 'kill @e[tag=mg.trp]', 'execute as @e[tag=mg.trh] run tp @s ~ -100 ~', 'kill @e[tag=mg.trh]',
                   'execute as @a run attribute @s minecraft:jump_strength base reset', 'scoreboard players reset @a mg.trc', 'scoreboard players reset @a mg.trs'])

C.register([84, 85], 'tron', [
    C.announce(84, '', '⚡ TRON', 'aqua', 'laisse un mur derrière toi, ne touche aucun mur !'),
    C.announce(85, '', '🏍 TRON MOTO', 'gold', 'à cheval, laisse un mur derrière toi, ne touche aucun mur !')])
C.objectives([('mg.trc', 'dummy'), ('mg.trs', 'dummy')])
C.forceload([f'# Tron (z {Z})', f'forceload add -32 {Z - 32} 32 {Z + 32}'])
print('Tron OK')
