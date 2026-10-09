"""🚚 Escorte de convoi — attaque/défense Rouge contre Bleu (id 89) et coop contre les monstres (id 90). z 21200.

    python tools/arcade/gen_convoy.py .

Une route droite de 120 blocs (x −60 → +60). Le convoi (un chariot) avance tout seul quand un escorteur est à
moins de 4 blocs et qu'aucun ennemi n'est à moins de 4 blocs (sinon il est bloqué).
- 89 : deux manches de 3 min, les équipes échangent les rôles. Score d'une manche = distance parcourue
  (+ temps restant s'il arrive). Meilleur score gagne.
- 90 : tout le monde escorte. Des vagues de monstres arrivent devant le convoi (plus nombreuses avec plus de joueurs)
  et l'abîment. Amener le convoi au bout avant 6 min, sans qu'il soit détruit.
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
Z = 21200
X0, X1 = -60, 60
ROUND, COOP_LIMIT, SPEED = 3600, 7200, 0.06
CV = '@e[type=minecraft:block_display,tag=mg.cvc,limit=1]'

L = ['# 🚚 Convoi — route x −70..70, z 21188..21212']
L += [f'fill -72 {y} {Z - 14} 72 {y} {Z + 14} minecraft:air' for y in range(79, 101)]
L += [f'fill -72 78 {Z - 14} 72 79 {Z + 14} minecraft:dirt', f'fill -72 80 {Z - 14} 72 80 {Z + 14} minecraft:grass_block',
      f'fill -70 80 {Z - 2} 70 80 {Z + 2} minecraft:gravel', f'fill -70 80 {Z - 1} 70 80 {Z + 1} minecraft:dirt_path',
      f'fill {X1} 80 {Z - 3} {X1 + 1} 80 {Z + 3} minecraft:gold_block', f'fill {X0 - 1} 80 {Z - 3} {X0} 80 {Z + 3} minecraft:iron_block']
# couvertures : murets, maisons en ruine, rochers de chaque côté
for i, x in enumerate(range(-50, 60, 12)):
    s = 1 if i % 2 else -1
    L += [f'fill {x} 81 {Z + s * 5} {x + 3} 82 {Z + s * 5} minecraft:cobblestone_wall',
          f'fill {x + 5} 81 {Z - s * 8} {x + 8} 84 {Z - s * 11} minecraft:oak_planks hollow',
          f'fill {x + 6} 81 {Z - s * 8} {x + 7} 82 {Z - s * 8} minecraft:air',
          f'fill {x + 2} 81 {Z + s * 10} {x + 3} 83 {Z + s * 11} minecraft:mossy_cobblestone',
          f'setblock {x + 1} 81 {Z - s * 4} minecraft:hay_block']
L += [f'fill -72 79 {Z - 14} 72 100 {Z - 14} minecraft:barrier', f'fill -72 79 {Z + 14} 72 100 {Z + 14} minecraft:barrier',
      f'fill -72 79 {Z - 13} -72 100 {Z + 13} minecraft:barrier', f'fill 72 79 {Z - 13} 72 100 {Z + 13} minecraft:barrier',
      f'fill -71 100 {Z - 13} 71 100 {Z + 13} minecraft:barrier']
w('convoy/build', L)

w('convoy/prepare', ['# 🚚 Convoi — préparation ($cvm : 0 attaque/défense, 1 coop)',
                     'scoreboard players set $cvm mg.st 0', 'execute if score $game mg.st matches 90 run scoreboard players set $cvm mg.st 1',
                     'function mg:convoy/build', 'function mg:convoy/kill_all',
                     'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 95', f'scoreboard players set $pz mg.st {Z}',
                     'clear @a[tag=mg.play]', 'gamemode adventure @a[tag=mg.play]',
                     'execute if score $cvm mg.st matches 0 run scoreboard players set $nt mg.st 2',
                     'execute if score $cvm mg.st matches 0 run function mg:core/assign_teams',
                     'execute if score $cvm mg.st matches 1 run team join mg_green @a[tag=mg.play]',
                     'scoreboard players set $cvr mg.st 1', 'scoreboard players set $cvo mg.st 0',
                     'function mg:convoy/reset_cart',
                     'execute as @a[tag=mg.play] run function mg:convoy/spawn'])
w('convoy/kill_all', [f'kill @e[tag=mg.cvc]', 'kill @e[tag=mg.cvl]', 'kill @e[tag=mg.cvm]',
                      f'kill @e[type=minecraft:item,x=-75,y=60,z={Z - 15},dx=150,dy=50,dz=30]',
                      f'kill @e[type=minecraft:arrow,x=-75,y=60,z={Z - 15},dx=150,dy=50,dz=30]'])
w('convoy/reset_cart', ['# Convoi au départ', 'kill @e[tag=mg.cvc]', 'kill @e[tag=mg.cvl]',
                        f'summon minecraft:block_display {X0 + 0.5} 81 {Z}.5 {{Tags:["mg.cvc"],Glowing:1b,teleport_duration:2,block_state:{{Name:"minecraft:barrel",Properties:{{facing:"up"}}}},transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.8f,0f,-0.8f],scale:[1.6f,1.3f,1.6f]}}}}',
                        f'summon minecraft:text_display {X0 + 0.5} 83 {Z}.5 {{Tags:["mg.cvl"],billboard:"center",teleport_duration:2,text:{{"text":"🚚 CONVOI","color":"gold","bold":true}}}}',
                        'scoreboard players set $cvh mg.st 100', 'scoreboard players set $cvt mg.st 0', 'scoreboard players set $cvp mg.st 0',
                        'bossbar add mg:convoy {"text":"🚚 Convoi"}', 'bossbar set mg:convoy max 120', 'bossbar set mg:convoy value 0',
                        'bossbar set mg:convoy color yellow', 'bossbar set mg:convoy players @a[tag=mg.play]'])
w('convoy/spawn', ['# @s : point d\'apparition (près du convoi : escorte derrière, défense devant)',
                   'scoreboard players set $cva mg.st 0',
                   'execute if score $cvm mg.st matches 1 run scoreboard players set $cva mg.st 1',
                   'execute if score $cvm mg.st matches 0 if score $cvo mg.st matches 0 if entity @s[team=mg_red] run scoreboard players set $cva mg.st 1',
                   'execute if score $cvm mg.st matches 0 if score $cvo mg.st matches 1 if entity @s[team=mg_blue] run scoreboard players set $cva mg.st 1',
                   # escorte : 25 blocs derrière le convoi (au pire au début de la route) ; défense : 40 blocs devant (au pire au bout)
                   f'execute if score $cva mg.st matches 1 if score $cvp mg.st matches 17.. at {CV} run tp @s ~-25 81 {Z}.5 facing ~ 81 {Z}.5',
                   f'execute if score $cva mg.st matches 1 if score $cvp mg.st matches ..16 run tp @s {X0 - 8} 81 {Z}.5 facing 0 81 {Z}.5',
                   f'execute if score $cva mg.st matches 0 if score $cvp mg.st matches ..87 at {CV} run tp @s ~40 81 {Z}.5 facing ~ 81 {Z}.5',
                   f'execute if score $cva mg.st matches 0 if score $cvp mg.st matches 88.. run tp @s {X1 + 8} 81 {Z}.5 facing -70 81 {Z}.5',
                   'execute at @s run spawnpoint @s ~ ~ ~'])
w('convoy/kit', ['# @s : kit', 'clear @s', 'give @s minecraft:iron_sword[unbreakable={}]', 'give @s minecraft:bow[unbreakable={}]',
                 'give @s minecraft:arrow 32', 'give @s minecraft:cooked_beef 16',
                 'item replace entity @s weapon.offhand with minecraft:shield[unbreakable={}]',
                 'item replace entity @s armor.chest with minecraft:iron_chestplate[unbreakable={}]',
                 'item replace entity @s armor.feet with minecraft:iron_boots[unbreakable={}]',
                 'execute if entity @s[team=mg_red] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=16711680,unbreakable={}]',
                 'execute if entity @s[team=mg_blue] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=255,unbreakable={}]',
                 'execute if entity @s[team=mg_green] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=65280,unbreakable={}]',
                 'item replace entity @s armor.legs with minecraft:chainmail_leggings[unbreakable={}]'])
w('convoy/go', ['# Départ', 'execute as @a[tag=mg.play] run function mg:convoy/kit', 'scoreboard players set @a mg.deaths 0',
                'scoreboard players set $cvw mg.st 0',
                'execute if score $cvm mg.st matches 0 run function mg:convoy/round_msg',
                'execute if score $cvm mg.st matches 1 run tellraw @a[tag=mg.play] ' + js([
                    {'text': '🚚 CONVOI (coop) : ', 'color': 'gold', 'bold': True},
                    {'text': 'restez près du convoi pour le faire avancer, les monstres le bloquent et l\'abîment. Amenez-le aux blocs d\'or avant 6 min !', 'color': 'gray'}])])
w('convoy/round_msg', ['# Annonce de la manche',
                       'execute if score $cvo mg.st matches 0 run tellraw @a[tag=mg.play] ' + js([
                           {'text': '🚚 MANCHE ', 'color': 'gold', 'bold': True}, {'score': {'name': '$cvr', 'objective': 'mg.st'}, 'color': 'gold', 'bold': True},
                           {'text': ' : les ', 'color': 'gray'}, {'text': 'ROUGES', 'color': 'red', 'bold': True},
                           {'text': ' escortent le convoi, les ', 'color': 'gray'}, {'text': 'BLEUS', 'color': 'blue', 'bold': True},
                           {'text': ' le bloquent. 3 minutes !', 'color': 'gray'}]),
                       'execute if score $cvo mg.st matches 1 run tellraw @a[tag=mg.play] ' + js([
                           {'text': '🚚 MANCHE ', 'color': 'gold', 'bold': True}, {'score': {'name': '$cvr', 'objective': 'mg.st'}, 'color': 'gold', 'bold': True},
                           {'text': ' : les ', 'color': 'gray'}, {'text': 'BLEUS', 'color': 'blue', 'bold': True},
                           {'text': ' escortent, les ', 'color': 'gray'}, {'text': 'ROUGES', 'color': 'red', 'bold': True},
                           {'text': ' bloquent. À battre : ', 'color': 'gray'}, {'score': {'name': '$cvs1', 'objective': 'mg.st'}, 'color': 'yellow'},
                           {'text': ' points.', 'color': 'gray'}])])

w('convoy/tick', ['# 🚚 Convoi — tick', 'scoreboard players add $cvt mg.st 1',
                  'execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:convoy/dead',
                  'execute as @a[tag=mg.play,tag=!mg.cvw] store result score @s mg.t run data get entity @s Pos[1]',
                  'execute as @a[tag=mg.play,tag=!mg.cvw,scores={mg.t=..74}] run function mg:convoy/dead',
                  'execute as @a[tag=mg.cvw] run function mg:convoy/wait',
                  # escorteurs / bloqueurs près du convoi
                  'scoreboard players set $cve mg.st 0', 'scoreboard players set $cvb mg.st 0',
                  f'execute if score $cvm mg.st matches 1 at {CV} store result score $cve mg.st if entity @a[tag=mg.play,gamemode=!spectator,distance=..4]',
                  f'execute if score $cvm mg.st matches 1 at {CV} store result score $cvb mg.st if entity @e[tag=mg.cvm,distance=..4]',
                  f'execute if score $cvm mg.st matches 0 if score $cvo mg.st matches 0 at {CV} store result score $cve mg.st if entity @a[tag=mg.play,team=mg_red,gamemode=!spectator,distance=..4]',
                  f'execute if score $cvm mg.st matches 0 if score $cvo mg.st matches 0 at {CV} store result score $cvb mg.st if entity @a[tag=mg.play,team=mg_blue,gamemode=!spectator,distance=..4]',
                  f'execute if score $cvm mg.st matches 0 if score $cvo mg.st matches 1 at {CV} store result score $cve mg.st if entity @a[tag=mg.play,team=mg_blue,gamemode=!spectator,distance=..4]',
                  f'execute if score $cvm mg.st matches 0 if score $cvo mg.st matches 1 at {CV} store result score $cvb mg.st if entity @a[tag=mg.play,team=mg_red,gamemode=!spectator,distance=..4]',
                  f'execute if score $cve mg.st matches 1.. if score $cvb mg.st matches 0 as {CV} at @s run tp @s ~{SPEED} ~ ~',
                  f'execute as @e[tag=mg.cvl] at {CV} run tp @s ~ ~2.2 ~',
                  f'execute store result score $cvp mg.st run data get entity {CV} Pos[0]',
                  f'scoreboard players add $cvp mg.st {-X0}', 'execute store result bossbar mg:convoy value run scoreboard players get $cvp mg.st',
                  'execute if score $cve mg.st matches 1.. if score $cvb mg.st matches 0 run bossbar set mg:convoy color green',
                  'execute if score $cvb mg.st matches 1.. run bossbar set mg:convoy color red',
                  'execute if score $cve mg.st matches 0 if score $cvb mg.st matches 0 run bossbar set mg:convoy color yellow',
                  f'execute if score $cve mg.st matches 1.. if score $cvb mg.st matches 0 at {CV} run particle minecraft:cloud ~ ~0.2 ~ 0.4 0.1 0.4 0 1',
                  'scoreboard players operation $cvq mg.st = $cvt mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $cvq mg.st %= #20 mg.st',
                  'execute if score $cvq mg.st matches 0 run function mg:convoy/second',
                  f'execute if score $state mg.st matches 2 if score $cvp mg.st matches {X1 - X0}.. run return run function mg:convoy/arrived',
                  f'execute if score $state mg.st matches 2 if score $cvm mg.st matches 0 if score $cvt mg.st matches {ROUND}.. run return run function mg:convoy/round_end',
                  f'execute if score $state mg.st matches 2 if score $cvm mg.st matches 1 if score $cvt mg.st matches {COOP_LIMIT}.. run return run function mg:convoy/coop_lose',
                  'execute store result score $alive mg.st if entity @a[tag=mg.play]',
                  'execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw'])
w('convoy/second', ['# Chaque seconde : temps restant, monstres (coop)',
                    'scoreboard players operation $cvs mg.st = $cvt mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $cvs mg.st /= #20 mg.st',
                    f'scoreboard players set $cvl mg.st {ROUND // 20}', f'execute if score $cvm mg.st matches 1 run scoreboard players set $cvl mg.st {COOP_LIMIT // 20}',
                    'scoreboard players operation $cvl mg.st -= $cvs mg.st',
                    'execute if score $cvm mg.st matches 0 run bossbar set mg:convoy name [{"text":"🚚 Convoi — manche ","color":"gold"},{"score":{"name":"$cvr","objective":"mg.st"}},{"text":" — "},{"score":{"name":"$cvl","objective":"mg.st"},"color":"yellow"},{"text":" s"}]',
                    'execute if score $cvm mg.st matches 1 run bossbar set mg:convoy name [{"text":"🚚 Convoi — ","color":"gold"},{"score":{"name":"$cvh","objective":"mg.st"},"color":"red"},{"text":" ❤ — "},{"score":{"name":"$cvl","objective":"mg.st"},"color":"yellow"},{"text":" s"}]',
                    'execute if score $cvm mg.st matches 1 run function mg:convoy/coop_second'])
w('convoy/coop_second', ['# Coop : dégâts au convoi, vague toutes les 8 s',
                         f'execute at {CV} store result score $cvn mg.st if entity @e[tag=mg.cvm,distance=..3]',
                         'scoreboard players operation $cvh mg.st -= $cvn mg.st', 'scoreboard players operation $cvh mg.st -= $cvn mg.st',
                         f'execute if score $cvn mg.st matches 1.. at {CV} run particle minecraft:damage_indicator ~ ~1 ~ 0.4 0.3 0.4 0 3',
                         'execute if score $state mg.st matches 2 if score $cvh mg.st matches ..0 run return run function mg:convoy/coop_lose',
                         f'kill @e[type=minecraft:item,x=-75,y=60,z={Z - 15},dx=150,dy=50,dz=30]',
                         'scoreboard players add $cvw mg.st 1',
                         'execute if score $cvw mg.st matches 8.. run function mg:convoy/wave'])
w('convoy/wave', ['# Vague : 1 + nombre de joueurs monstres (max 8), devant le convoi ; 30 au plus en même temps',
                  'scoreboard players set $cvw mg.st 0',
                  'execute store result score $cvk mg.st if entity @e[tag=mg.cvm]', 'execute if score $cvk mg.st matches 30.. run return 0',
                  'execute store result score $cvk mg.st if entity @a[tag=mg.play]', 'scoreboard players add $cvk mg.st 1',
                  'execute if score $cvk mg.st matches 9.. run scoreboard players set $cvk mg.st 8',
                  f'execute if score $cvp mg.st matches 101.. run scoreboard players set $cvk mg.st 0',
                  f'execute at {CV} positioned ~20 81 {Z}.5 run function mg:convoy/wave_one'])
w('convoy/wave_one', ['# Un monstre (husk / pillard / vindicateur), position variable',
                      'execute if score $cvk mg.st matches ..0 run return 0', 'scoreboard players remove $cvk mg.st 1',
                      'execute store result score $cvz mg.st run random value 0..5',
                      'execute if score $cvz mg.st matches 0..2 run summon minecraft:husk ~ ~ ~-4 {Tags:["mg.cvm","mg.mob"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty"}',
                      'execute if score $cvz mg.st matches 3..4 run summon minecraft:pillager ~1 ~ ~4 {Tags:["mg.cvm","mg.mob"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",drop_chances:{mainhand:0f}}',
                      'execute if score $cvz mg.st matches 5 run summon minecraft:vindicator ~2 ~ ~ {Tags:["mg.cvm","mg.mob"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",drop_chances:{mainhand:0f}}',
                      'execute positioned ~1 ~ ~ run function mg:convoy/wave_one'])
w('convoy/arrived', ['# Le convoi est arrivé',
                     'execute if score $cvm mg.st matches 1 run return run function mg:convoy/coop_win',
                     'tellraw @a[tag=mg.play] {"text":"🚚 Le convoi est arrivé !","color":"gold","bold":true}',
                     'function mg:convoy/round_end'])
w('convoy/round_end', ['# Fin d\'une manche (attaque/défense) : score = distance ×10 (+ temps restant si arrivé)',
                       'scoreboard players operation $cvx mg.st = $cvp mg.st', 'scoreboard players set #10 mg.st 10',
                       'scoreboard players operation $cvx mg.st *= #10 mg.st',
                       f'scoreboard players set $cvy mg.st {ROUND}', 'scoreboard players operation $cvy mg.st -= $cvt mg.st',
                       'scoreboard players set #20 mg.st 20', 'scoreboard players operation $cvy mg.st /= #20 mg.st',
                       f'execute if score $cvp mg.st matches {X1 - X0}.. run scoreboard players operation $cvx mg.st += $cvy mg.st',
                       'execute if score $cvr mg.st matches 1 run scoreboard players operation $cvs1 mg.st = $cvx mg.st',
                       'execute if score $cvr mg.st matches 2 run scoreboard players operation $cvs2 mg.st = $cvx mg.st',
                       'tellraw @a[tag=mg.play] ' + js([{'text': '🚚 Fin de la manche : ', 'color': 'gold'},
                                                        {'score': {'name': '$cvx', 'objective': 'mg.st'}, 'color': 'yellow', 'bold': True},
                                                        {'text': ' points (', 'color': 'gray'}, {'score': {'name': '$cvp', 'objective': 'mg.st'}, 'color': 'gray'},
                                                        {'text': ' blocs)', 'color': 'gray'}]),
                       'execute if score $cvr mg.st matches 2 run return run function mg:convoy/final',
                       'scoreboard players set $cvr mg.st 2', 'scoreboard players set $cvo mg.st 1',
                       'function mg:convoy/reset_cart', 'execute as @a[tag=mg.play] run function mg:convoy/respawn',
                       'function mg:convoy/round_msg'])
w('convoy/final', ['# Après la 2e manche : rouges = manche 1, bleus = manche 2',
                   'execute if score $cvs1 mg.st > $cvs2 mg.st run return run function mg:core/win_red',
                   'execute if score $cvs2 mg.st > $cvs1 mg.st run return run function mg:core/win_blue',
                   'function mg:core/draw'])
w('convoy/coop_win', ['# Coop : convoi livré', 'kill @e[tag=mg.cvm]', 'tag @a[tag=mg.play] add mg.win',
                      'scoreboard players add @a[tag=mg.play] mg.wins 1', 'scoreboard players set $state mg.st 3', 'scoreboard players set $timer mg.st 120',
                      'title @a[tag=!mg.surv] title {"text":"CONVOI LIVRÉ !","color":"gold","bold":true}',
                      'tellraw @a {"text":"★ Le convoi est arrivé à bon port — bravo à l\'escorte !","color":"gold"}',
                      'execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1'])
w('convoy/coop_lose', ['# Coop : convoi détruit ou trop lent', 'kill @e[tag=mg.cvm]', 'scoreboard players set $state mg.st 3', 'scoreboard players set $timer mg.st 60',
                       'title @a[tag=!mg.surv] title {"text":"CONVOI PERDU...","color":"dark_red","bold":true}',
                       'tellraw @a ' + js([{'text': '☠ Le convoi s\'est arrêté à ', 'color': 'gray'}, {'score': {'name': '$cvp', 'objective': 'mg.st'}, 'color': 'red', 'bold': True},
                                           {'text': ' blocs sur 120.', 'color': 'gray'}]),
                       'execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.wither.death master @s ~ ~ ~ 0.5 0.8'])
RESPAWN = 100      # 5 s
w('convoy/dead', ['# @s vient de mourir (ou de tomber) : spectateur au-dessus du convoi pendant 5 s',
                  'scoreboard players set @s mg.deaths 0', 'tag @s add mg.cvw', f'scoreboard players set @s mg.cvrt {RESPAWN}',
                  'gamemode spectator @s', f'execute at {CV} run tp @s ~ 92 ~6 facing entity {CV}',
                  'title @s times 0 25 5', 'title @s title {"text":"☠ Éliminé","color":"red","bold":true}'])
w('convoy/wait', ['# @s attend sa réapparition (compte à rebours dans la barre d\'action)',
                  'scoreboard players remove @s mg.cvrt 1',
                  'execute if score @s mg.cvrt matches ..0 run return run function mg:convoy/respawn',
                  'scoreboard players operation $cvs mg.st = @s mg.cvrt', 'scoreboard players add $cvs mg.st 19',
                  'scoreboard players set #20 mg.st 20', 'scoreboard players operation $cvs mg.st /= #20 mg.st',
                  'title @s actionbar [{"text":"Réapparition dans ","color":"gray"},{"score":{"name":"$cvs","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"gray"}]'])
w('convoy/respawn', ['# @s : réapparition loin du convoi (escorte derrière, défense devant)', 'scoreboard players set @s mg.deaths 0',
                     'tag @s remove mg.cvw', 'scoreboard players reset @s mg.cvrt', 'gamemode adventure @s', 'function mg:convoy/spawn',
                     'function mg:convoy/kit', 'effect give @s minecraft:resistance 3 4 true', 'effect give @s minecraft:instant_health 1 4 true'])
w('convoy/cleanup', ['function mg:convoy/kill_all', 'bossbar remove mg:convoy', 'tag @a remove mg.cvw', 'scoreboard players reset @a mg.cvrt'])
C.objectives([('mg.cvrt', 'dummy')])

C.register([89, 90], 'convoy', [
    C.announce(89, '', '🚚 CONVOI', 'gold', 'rouges contre bleus, escortez ou bloquez le convoi (2 manches) !'),
    C.announce(90, '', '🚚 CONVOI — COOP', 'gold', 'escortez le convoi à travers les monstres !')])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['bossbar remove mg:convoy'])
C.forceload([f'# Convoi (z {Z})', f'forceload add -72 {Z - 14} 72 {Z + 14}'])
print('Convoi OK')
