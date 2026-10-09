"""🏰 The Towers — Rouge contre Bleu (id 88). Arène dans le vide en z 20800.

    python tools/arcade/gen_tower.py .

Le classique : chaque équipe a une île avec sa tour et son PUITS. Saute dans le puits adverse = +1 point.
5 points pour gagner (ou le plus de points au bout de 10 min). Construction et destruction libres (laine/terracotta
fournie, arène reconstruite à chaque partie), réapparition illimitée, ravitaillement au centre.
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
Z = 20800
WIN, LIMIT = 5, 12000
# pits : x de la case centrale
PIT = {'red': -37, 'blue': 37}
SPAWN = {'red': -30, 'blue': 30}


def island(x0, x1, top, side):
    return [f'fill {x0} 76 {Z - 7} {x1} 79 {Z + 7} minecraft:{side}', f'fill {x0} 80 {Z - 7} {x1} 80 {Z + 7} minecraft:{top}',
            f'fill {x0 + 2} 75 {Z - 5} {x1 - 2} 75 {Z + 5} minecraft:{side}', f'fill {x0 + 4} 74 {Z - 3} {x1 - 4} 74 {Z + 3} minecraft:{side}']


def tower(x, glass, wool):
    return [f'fill {x - 2} 81 {Z - 2} {x + 2} 88 {Z + 2} minecraft:stone_bricks hollow',
            f'fill {x - 2} 81 {Z} {x - 2} 83 {Z} minecraft:air', f'fill {x + 2} 81 {Z} {x + 2} 83 {Z} minecraft:air',
            f'fill {x - 2} 85 {Z - 2} {x + 2} 85 {Z + 2} minecraft:{glass}', f'fill {x - 1} 81 {Z - 1} {x + 1} 81 {Z + 1} minecraft:{wool}',
            f'fill {x - 2} 89 {Z - 2} {x + 2} 89 {Z + 2} minecraft:stone_brick_slab',
            f'setblock {x} 89 {Z} minecraft:sea_lantern']


def pit(x, wool, glass):
    return [f'fill {x - 2} 77 {Z - 2} {x + 2} 80 {Z + 2} minecraft:{wool}', f'fill {x - 1} 76 {Z - 1} {x + 1} 76 {Z + 1} minecraft:bedrock',
            f'fill {x - 1} 77 {Z - 1} {x + 1} 80 {Z + 1} minecraft:air',
            f'fill {x - 2} 81 {Z - 2} {x + 2} 81 {Z + 2} minecraft:{glass}', f'fill {x - 1} 81 {Z - 1} {x + 1} 81 {Z + 1} minecraft:air']


L = ['# 🏰 The Towers — vide, îles rouge (x −40..−26) et bleue (x 26..40), centre (x −5..5), puits aux extrémités']
L += [f'fill -48 {y} {Z - 16} 48 {y} {Z + 16} minecraft:air' for y in range(66, 106)]
L += island(-40, -26, 'red_terracotta', 'stone') + island(26, 40, 'blue_terracotta', 'stone')
L += [f'fill -5 77 {Z - 5} 5 79 {Z + 5} minecraft:stone', f'fill -5 80 {Z - 5} 5 80 {Z + 5} minecraft:smooth_stone',
      f'fill -3 76 {Z - 3} 3 76 {Z + 3} minecraft:stone', f'setblock 0 80 {Z} minecraft:gold_block',
      f'fill -1 81 {Z - 1} 1 81 {Z + 1} minecraft:iron_bars hollow', f'setblock 0 81 {Z} minecraft:air']
L += tower(SPAWN['red'], 'red_stained_glass', 'red_wool') + tower(SPAWN['blue'], 'blue_stained_glass', 'blue_wool')
L += pit(PIT['red'], 'red_wool', 'red_stained_glass') + pit(PIT['blue'], 'blue_wool', 'blue_stained_glass')
# passerelles d'un bloc (on peut les casser / en construire d'autres)
L += [f'fill -25 80 {Z} -6 80 {Z} minecraft:oak_planks', f'fill 6 80 {Z} 25 80 {Z} minecraft:oak_planks',
      f'fill -25 80 {Z - 6} -6 80 {Z - 6} minecraft:air', f'fill -20 80 {Z + 9} -10 80 {Z + 9} minecraft:cobblestone',
      f'fill 10 80 {Z - 9} 20 80 {Z - 9} minecraft:cobblestone']
# cage de barrières
L += [f'fill -48 66 {Z - 16} 48 105 {Z - 16} minecraft:barrier', f'fill -48 66 {Z + 16} 48 105 {Z + 16} minecraft:barrier',
      f'fill -48 66 {Z - 15} -48 105 {Z + 15} minecraft:barrier', f'fill 48 66 {Z - 15} 48 105 {Z + 15} minecraft:barrier',
      f'fill -47 105 {Z - 15} 47 105 {Z + 15} minecraft:barrier']
w('tower/build', L)

w('tower/prepare', ['# 🏰 The Towers — préparation', 'function mg:tower/build',
                    f'kill @e[type=minecraft:item,x=-50,y=50,z={Z - 20},dx=100,dy=60,dz=40]',
                    'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 95', f'scoreboard players set $pz mg.st {Z}',
                    'clear @a[tag=mg.play]', 'scoreboard players set $nt mg.st 2', 'function mg:core/assign_teams',
                    'scoreboard players reset Rouge mg.tw', 'scoreboard players reset Bleu mg.tw',
                    'gamemode adventure @a[tag=mg.play]', 'execute as @a[tag=mg.play] run function mg:tower/spawn'])
w('tower/spawn', ['# @s : dans sa tour',
                  f'execute if entity @s[team=mg_red] run spawnpoint @s {SPAWN["red"]} 82 {Z}',
                  f'execute if entity @s[team=mg_blue] run spawnpoint @s {SPAWN["blue"]} 82 {Z}',
                  f'execute if entity @s[team=mg_red] run tp @s {SPAWN["red"]}.5 82 {Z}.5 facing 0 82 {Z}',
                  f'execute if entity @s[team=mg_blue] run tp @s {SPAWN["blue"]}.5 82 {Z}.5 facing 0 82 {Z}'])
w('tower/kit', ['# @s : kit (blocs de l\'équipe pour construire, épée, arc, pioche)', 'clear @s',
                'give @s minecraft:stone_sword[unbreakable={}]', 'give @s minecraft:bow[unbreakable={}]',
                'give @s minecraft:stone_pickaxe[unbreakable={}]', 'give @s minecraft:arrow 16',
                'execute if entity @s[team=mg_red] run give @s minecraft:red_terracotta 64',
                'execute if entity @s[team=mg_blue] run give @s minecraft:blue_terracotta 64',
                'give @s minecraft:golden_apple 1',
                'execute if entity @s[team=mg_red] run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16711680,unbreakable={}]',
                'execute if entity @s[team=mg_blue] run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=255,unbreakable={}]',
                'execute if entity @s[team=mg_red] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=16711680,unbreakable={}]',
                'execute if entity @s[team=mg_blue] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=255,unbreakable={}]',
                'item replace entity @s armor.legs with minecraft:chainmail_leggings[unbreakable={}]',
                'item replace entity @s armor.feet with minecraft:leather_boots[unbreakable={}]',
                'effect give @s minecraft:saturation infinite 0 true'])
w('tower/go', ['# Départ : survie (construction libre)', 'scoreboard players set $twt mg.st 0',
               'gamemode survival @a[tag=mg.play]', 'execute as @a[tag=mg.play] run function mg:tower/kit',
               'scoreboard players set @a mg.deaths 0', 'scoreboard players reset @a mg.tw',
               'scoreboard players set Rouge mg.tw 0', 'scoreboard players set Bleu mg.tw 0',
               'scoreboard objectives setdisplay sidebar mg.tw',
               'tellraw @a[tag=mg.play] ' + js([{'text': '🏰 THE TOWERS : ', 'color': 'gold', 'bold': True},
                                                {'text': f'saute dans le PUITS de l\'équipe adverse (au bout de son île) = +1 point. {WIN} points pour gagner, 10 min max. Construis tes ponts, défends ton puits !', 'color': 'gray'}])])
rp, bp = PIT['red'], PIT['blue']
w('tower/tick', ['# 🏰 The Towers — tick', 'scoreboard players add $twt mg.st 1',
                 'execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:tower/respawn',
                 'execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]',
                 'execute as @a[tag=mg.play,scores={mg.t=..68}] run function mg:tower/respawn',
                 # puits : on ne peut pas les boucher
                 f'fill {rp - 1} 77 {Z - 1} {rp + 1} 81 {Z + 1} minecraft:air', f'fill {bp - 1} 77 {Z - 1} {bp + 1} 81 {Z + 1} minecraft:air',
                 # point : un bleu dans le puits rouge, un rouge dans le puits bleu
                 f'execute as @a[tag=mg.play,team=mg_blue,x={rp - 1},y=76,z={Z - 1},dx=2,dy=3,dz=2] run function mg:tower/score_blue',
                 f'execute as @a[tag=mg.play,team=mg_red,x={bp - 1},y=76,z={Z - 1},dx=2,dy=3,dz=2] run function mg:tower/score_red',
                 # ravitaillement au centre toutes les 15 s
                 'scoreboard players operation $twq mg.st = $twt mg.st', 'scoreboard players set #300 mg.st 300',
                 'scoreboard players operation $twq mg.st %= #300 mg.st',
                 f'execute if score $twq mg.st matches 0 run summon minecraft:item 0.5 81.2 {Z}.5 {{Item:{{id:"minecraft:arrow",count:4}}}}',
                 f'execute if score $twq mg.st matches 0 run summon minecraft:item 0.5 81.2 {Z}.5 {{Item:{{id:"minecraft:golden_apple",count:1}}}}',
                 f'execute if score $twq mg.st matches 0 run summon minecraft:item 0.5 81.2 {Z}.5 {{Item:{{id:"minecraft:white_terracotta",count:16}}}}',
                 f'execute if score $twt mg.st matches {LIMIT - 1200} run tellraw @a[tag=mg.play] {{"text":"🏰 Plus qu\'une minute !","color":"gold"}}',
                 f'execute if score $state mg.st matches 2 if score $twt mg.st matches {LIMIT}.. run function mg:tower/timeout',
                 'execute store result score $twr mg.st if entity @a[tag=mg.play,team=mg_red]',
                 'execute store result score $twb mg.st if entity @a[tag=mg.play,team=mg_blue]',
                 'execute if score $state mg.st matches 2 if score $twr mg.st matches 0 if score $twb mg.st matches 1.. run return run function mg:core/win_blue',
                 'execute if score $state mg.st matches 2 if score $twb mg.st matches 0 if score $twr mg.st matches 1.. run return run function mg:core/win_red',
                 'execute if score $state mg.st matches 2 if score $twb mg.st matches 0 if score $twr mg.st matches 0 run function mg:core/draw'])
for team, other, nm, col in [('red', 'blue', 'Rouge', 'red'), ('blue', 'red', 'Bleu', 'blue')]:
    w(f'tower/score_{team}', [f'# @s ({nm}) est tombé dans le puits adverse', f'scoreboard players add {nm} mg.tw 1',
                              'scoreboard players add @s mg.tw 1',
                              'tellraw @a[tag=mg.play] ' + js([{'text': '🏰 ', 'color': col}, {'selector': '@s', 'color': col},
                                                               {'text': ' marque dans le puits adverse ! ', 'color': 'gray'},
                                                               {'text': 'Rouge ', 'color': 'red'}, {'score': {'name': 'Rouge', 'objective': 'mg.tw'}, 'color': 'red'},
                                                               {'text': ' – ', 'color': 'gray'}, {'score': {'name': 'Bleu', 'objective': 'mg.tw'}, 'color': 'blue'},
                                                               {'text': ' Bleu', 'color': 'blue'}]),
                              'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.4',
                              'function mg:tower/spawn', 'effect give @s minecraft:instant_health 1 4 true',
                              f'execute if score $state mg.st matches 2 if score {nm} mg.tw matches {WIN}.. run function mg:core/win_{team}'])
w('tower/respawn', ['# @s : réapparition dans sa tour (kit rendu)', 'scoreboard players set @s mg.deaths 0',
                    'function mg:tower/spawn', 'function mg:tower/kit', 'effect give @s minecraft:resistance 3 4 true',
                    'effect give @s minecraft:instant_health 1 4 true'])
w('tower/timeout', ['# 10 min : le plus de points gagne',
                    'execute if score Rouge mg.tw > Bleu mg.tw run return run function mg:core/win_red',
                    'execute if score Bleu mg.tw > Rouge mg.tw run return run function mg:core/win_blue',
                    'function mg:core/draw'])
w('tower/cleanup', ['scoreboard players reset * mg.tw', f'kill @e[type=minecraft:item,x=-50,y=50,z={Z - 20},dx=100,dy=60,dz=40]'])

C.register([88], 'tower', [C.announce(88, '', '🏰 THE TOWERS', 'gold', f'rouges contre bleus, saute dans le puits adverse ({WIN} points) !')])
C.objectives([('mg.tw', 'dummy {"text":"🏰 The Towers","color":"gold"}')])
C.forceload([f'# The Towers (z {Z})', f'forceload add -48 {Z - 16} 48 {Z + 16}'])
print('Towers OK')
