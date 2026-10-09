"""⚡ Tron — à pied (id 84) et à cheval « moto » (id 85). Arène 101×101 en z 20000, dans la pénombre.

    python tools/arcade/gen_tron.py .

Chaque joueur laisse un mur de laine de sa couleur (2 blocs de haut) derrière lui ; toucher un mur (le sien
compris, sauf le bloc qu'il vient de quitter) ou la bordure = éliminé ; rester immobile 2,5 s = éliminé.
Pas de saut à pied. Dernier en vie gagne. Moto : monture rapide, descendre = éliminé ; ⤴ saut au-dessus d'un mur toutes les 20 s.
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
Z = C.param('Z', 20000)
COLORS = ['red', 'blue', 'lime', 'yellow', 'orange', 'magenta', 'cyan', 'white', 'purple', 'pink', 'light_blue', 'green',
          'brown', 'light_gray', 'gray', 'black']
TXT = ['red', 'blue', 'green', 'yellow', 'gold', 'light_purple', 'dark_aqua', 'white', 'dark_purple', 'light_purple', 'aqua',
       'dark_green', 'gold', 'gray', 'dark_gray', 'black']

H = C.param('H', 50)   # demi-côté de l'arène (101×101 ; XXL : 201×201)


def fill(x1, y1, z1, x2, y2, z2, blk):
    """fill découpé en tranches (≤ 32768 blocs par commande)."""
    per = max(1, 32768 // ((x2 - x1 + 1) * (y2 - y1 + 1)))
    return [f'fill {x1} {y1} {z} {x2} {y2} {min(z + per - 1, z2)} {blk}' for z in range(z1, z2 + 1, per)]


L = [f'# ⚡ Tron — arène {2 * H + 1}×{2 * H + 1} (centre 0 80 {Z}) dans la pénombre : toit opaque, quelques lumières faibles, bordure cyan']
L += [c for y in range(79, 93) for c in fill(-H - 2, y, Z - H - 2, H + 2, y, Z + H + 2, 'minecraft:air')]
L += fill(-H - 1, 79, Z - H - 1, H + 1, 79, Z + H + 1, 'minecraft:barrier') + fill(-H, 80, Z - H, H, 80, Z + H, 'minecraft:black_concrete')
for k in range(-H, H + 1, 10):
    L += [f'fill {k} 80 {Z - H} {k} 80 {Z + H} minecraft:gray_concrete', f'fill {-H} 80 {Z + k} {H} 80 {Z + k} minecraft:gray_concrete']
L += [f'fill {-H - 1} 80 {Z - H - 1} {H + 1} 82 {Z - H - 1} minecraft:cyan_stained_glass', f'fill {-H - 1} 80 {Z + H + 1} {H + 1} 82 {Z + H + 1} minecraft:cyan_stained_glass',
      f'fill {-H - 1} 80 {Z - H} {-H - 1} 82 {Z + H} minecraft:cyan_stained_glass', f'fill {H + 1} 80 {Z - H} {H + 1} 82 {Z + H} minecraft:cyan_stained_glass',
      # murs et toit opaques au-dessus de la bordure : la lumière du ciel n'entre pas
      f'fill {-H - 1} 83 {Z - H - 1} {H + 1} 91 {Z - H - 1} minecraft:black_concrete', f'fill {-H - 1} 83 {Z + H + 1} {H + 1} 91 {Z + H + 1} minecraft:black_concrete',
      f'fill {-H - 1} 83 {Z - H} {-H - 1} 91 {Z + H} minecraft:black_concrete', f'fill {H + 1} 83 {Z - H} {H + 1} 91 {Z + H} minecraft:black_concrete',
      # bordure lumineuse (lumière invisible derrière la vitre)
      f'fill {-H - 2} 81 {Z - H - 2} {H + 2} 81 {Z - H - 2} minecraft:light[level=9]', f'fill {-H - 2} 81 {Z + H + 2} {H + 2} 81 {Z + H + 2} minecraft:light[level=9]',
      f'fill {-H - 2} 81 {Z - H - 1} {-H - 2} 81 {Z + H + 1} minecraft:light[level=9]', f'fill {H + 2} 81 {Z - H - 1} {H + 2} 81 {Z + H + 1} minecraft:light[level=9]']
# pénombre : lumières faibles en hauteur (au-dessus des murs, invisibles), juste assez pour voir le sol et empêcher les monstres
L += fill(-H - 1, 92, Z - H - 1, H + 1, 92, Z + H + 1, 'minecraft:black_concrete')
L += [f'setblock {x} 86 {Z + z} minecraft:light[level=7]' for x in range(-H + 5, H, 10) for z in range(-H + 5, H, 10)]
w('tron/build', L)
import json, os
os.makedirs(os.path.join(C.D, 'tags/block'), exist_ok=True)
json.dump({'values': ['#minecraft:wool', 'minecraft:cyan_stained_glass', 'minecraft:black_concrete']}, open(os.path.join(C.D, 'tags/block/tron_wall.json'), 'w'), indent=2)

w('tron/prepare', [
    '# ⚡ Tron — préparation ($trm : 0 à pied, 1 moto)',
    'scoreboard players set $trm mg.st 0', 'execute if score $game mg.st matches 85 run scoreboard players set $trm mg.st 1',
    'function mg:tron/build', 'kill @e[tag=mg.trm]', 'kill @e[tag=mg.trp]', 'kill @e[tag=mg.trh]',
    'scoreboard players set $tk mg.st 0', 'execute as @a[tag=mg.play,sort=random] run function mg:tron/assign',
    'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 90', f'scoreboard players set $pz mg.st {Z}',
    'gamemode adventure @a[tag=mg.play]', f'execute as @a[tag=mg.play] run spawnpoint @s 0 81 {Z}',
    'clear @a[tag=mg.play]',
    f'spreadplayers 0 {Z} 10 {H - 8} under 82 false @a[tag=mg.play]',
    f'execute as @a[tag=mg.play] at @s run tp @s ~ ~ ~ facing 0 81 {Z}',
    'execute as @a[tag=mg.play] run attribute @s minecraft:jump_strength base set 0',
    'execute if score $trm mg.st matches 1 as @a[tag=mg.play] at @s run function mg:tron/horse'])
w('tron/assign', ['scoreboard players operation @s mg.trc = $tk mg.st', 'scoreboard players add $tk mg.st 1',
                  'execute if score $tk mg.st matches 16.. run scoreboard players set $tk mg.st 0'])
w('tron/horse', ['# @s = joueur : sa moto (cheval rapide, sans saut, increvable)',
                 'summon minecraft:horse ~ ~ ~ {Tags:["mg.trh","mg.trnew","mg.npc"],Tame:1b,PersistenceRequired:1b,Invulnerable:1b,Silent:1b,'
                 'equipment:{saddle:{id:"minecraft:saddle",count:1}},'
                 'attributes:[{id:"minecraft:movement_speed",base:0.32d},{id:"minecraft:jump_strength",base:0.0d},{id:"minecraft:step_height",base:0.0d}]}',
                 'scoreboard players operation @e[tag=mg.trnew,limit=1] mg.trc = @s mg.trc',
                 'ride @s mount @e[tag=mg.trnew,limit=1]', 'tag @e[tag=mg.trnew] remove mg.trnew'])
w('tron/go', ['# Départ : marqueurs de traînée, vitesse', 'scoreboard players set $trt mg.st 0',
              'execute as @a[tag=mg.play] run function mg:tron/go_one',
              'execute if score $trm mg.st matches 0 run effect give @a[tag=mg.play] minecraft:speed infinite 1 true',
              'effect give @a[tag=mg.play] minecraft:saturation infinite 0 true', 'effect give @a[tag=mg.play] minecraft:resistance infinite 4 true',
              'effect give @a[tag=mg.play] minecraft:glowing infinite 0 true', 'effect give @e[tag=mg.trh] minecraft:glowing infinite 0 true',
              'scoreboard players set @a[tag=mg.play] mg.trj 200', 'scoreboard players reset @a[tag=mg.play] mg.qs',
              'execute if score $trm mg.st matches 1 run item replace entity @a[tag=mg.play] hotbar.0 with minecraft:warped_fungus_on_a_stick[custom_data={tron_jump:1b},custom_name=[{"text":"⤴ Saut","color":"gold","bold":true,"italic":false}],lore=[[{"text":"Clic droit puis Espace : saute par-dessus un mur","color":"gray","italic":false}],[{"text":"Recharge : 20 s","color":"gray","italic":false}]],unbreakable={}]',
              'tellraw @a[tag=mg.play] ' + js([{'text': '⚡ TRON : ', 'color': 'aqua', 'bold': True},
                                               {'text': 'tu laisses un mur derrière toi. Touche un mur (même le tien) ou la bordure = éliminé. Interdit de s’arrêter plus de 2 s. Dernier en vie gagne !', 'color': 'gray'}]),
              'execute if score $trm mg.st matches 1 run tellraw @a[tag=mg.play] {"text":"🏍 Moto : tu ne peux pas descendre. ⤴ Saut (clic droit, puis Espace) pour passer au-dessus d\'un mur, une fois toutes les 20 s.","color":"gold"}'])
w('tron/go_one', ['# @s = joueur : marqueurs « bloc courant » (mg.trm) et « dernier mur posé » (mg.trp)',
                  'execute at @s run summon minecraft:marker ~ ~ ~ {Tags:["mg.trm","mg.trnew"]}',
                  'execute at @s run summon minecraft:marker ~ ~ ~ {Tags:["mg.trp","mg.trnew"]}',
                  'scoreboard players operation @e[tag=mg.trnew] mg.trc = @s mg.trc', 'tag @e[tag=mg.trnew] remove mg.trnew',
                  'scoreboard players set @s mg.trs 0'])
w('tron/tick', ['# ⚡ Tron — tick', 'scoreboard players add $trt mg.st 1',
                'execute if score $trm mg.st matches 1 as @a[tag=mg.play] run function mg:tron/jump_tick',
                'scoreboard players reset @a[scores={mg.qs=1..}] mg.qs',
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
    'execute as @e[tag=mg.tcar] at @s if block ~ ~-0.25 ~ #minecraft:air run tag @s add mg.tair',
    'execute unless entity @e[tag=mg.tair] as @e[tag=mg.tcm,limit=1] at @s align xyz unless entity @e[tag=mg.tcar,dx=0,dy=0,dz=0] run function mg:tron/lay',
    'execute if entity @e[tag=mg.tair] as @e[tag=mg.tcm,limit=1] at @e[tag=mg.tcar,limit=1] run tp @s ~ 81 ~',
    'execute if entity @e[tag=mg.tair] run scoreboard players set @s mg.trs 0',
    'tag @e remove mg.tair',
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
lay.append('execute positioned ~ ~2 ~ if block ~ ~ ~ #minecraft:air run setblock ~ ~ ~ minecraft:light[level=6]')   # le mur luit dans la pénombre
lay += ['tp @e[tag=mg.tpm,limit=1] @s', 'tp @s @e[tag=mg.tcar,limit=1]', 'execute at @s run tp @s ~ 81 ~', 'scoreboard players set @a[tag=mg.tme] mg.trs 0']
w('tron/lay', lay)
w('tron/jump_tick', ['# @s (moto) : recharge du saut, clic droit = saut armé 3 s (Espace pour sauter)',
                     'scoreboard players remove @s[scores={mg.trj=1..}] mg.trj 1',
                     'scoreboard players operation $tid mg.st = @s mg.trc',
                     'execute if score @s mg.trj matches 1.. if score @s mg.qs matches 1.. run title @s actionbar [{"text":"⤴ Saut en recharge : ","color":"gray"},{"score":{"name":"@s","objective":"mg.trj"},"color":"yellow"},{"text":" ticks","color":"gray"}]',
                     'execute if score @s mg.trj matches ..0 if score @s mg.qs matches 1.. run function mg:tron/jump_arm',
                     'execute if score @s mg.trj matches 340 as @e[tag=mg.trh] if score @s mg.trc = $tid mg.st run attribute @s minecraft:jump_strength base set 0',
                     'execute if score @s mg.trj matches 1 run title @s actionbar {"text":"⤴ Saut prêt (clic droit)","color":"green"}'])
w('tron/jump_arm', ['# @s arme son saut : la moto peut sauter pendant 3 s', 'scoreboard players set @s mg.trj 400',
                    'execute as @e[tag=mg.trh] if score @s mg.trc = $tid mg.st run attribute @s minecraft:jump_strength base set 0.9',
                    'title @s actionbar {"text":"⤴ SAUT ARMÉ : maintiens Espace puis relâche !","color":"gold","bold":true}',
                    'execute at @s run playsound minecraft:entity.horse.jump master @s ~ ~ ~ 1 1.2'])
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
w('tron/cleanup', ['execute as @a run ride @s dismount', 'effect clear @a[tag=mg.play] minecraft:glowing', 'scoreboard players reset @a mg.trj', 'kill @e[tag=mg.trm]', 'kill @e[tag=mg.trp]', 'execute as @e[tag=mg.trh] run tp @s ~ -100 ~', 'kill @e[tag=mg.trh]',
                   'execute as @a run attribute @s minecraft:jump_strength base reset', 'scoreboard players reset @a mg.trc', 'scoreboard players reset @a mg.trs'])

C.register([84, 85], 'tron', [
    C.announce(84, '', '⚡ TRON', 'aqua', 'laisse un mur derrière toi, ne touche aucun mur !'),
    C.announce(85, '', '🏍 TRON MOTO', 'gold', 'à cheval, laisse un mur derrière toi, ne touche aucun mur !')])
C.objectives([('mg.trc', 'dummy'), ('mg.trs', 'dummy'), ('mg.trj', 'dummy')])
C.forceload([f'# Tron (z {Z})', f'forceload add {-H - 2} {Z - H - 2} {H + 2} {Z + H + 2}'])
print('Tron OK')
