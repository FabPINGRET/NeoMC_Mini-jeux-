"""🎉 Événements surprises du lobby : python tools/lobby/gen_events.py .

Toutes les 30 min (jeu au repos, au moins un joueur au lobby), annonce 1 min avant puis un des trois événements (3 min) :
  👑 Roi Zombie : un husk géant (vie selon le nombre de joueurs) et ses sbires ; épée prêtée ; le plus gros cogneur gagne.
  💰 Pluie de pièces : des pépites (1) et des lingots (5) tombent sur l'île pendant 60 s ; le plus riche gagne.
  🗝 Chasse au trésor : un coffre caché sur l'île, indices chaud / froid ; le premier qui clique dessus gagne.
Gagnant : couronne (jusqu'à la prochaine partie), feu d'artifice, mg.evw + 1. Une partie qui démarre arrête l'événement.
Admin : /function mg:lobby/ev/force (au hasard, annonce 10 s) ou mg:lobby/ev/force_1..3.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arcade'))
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
EVERY, LEN = 1800, 180                             # secondes
L = '@a[tag=mg.evl]'
NAMES = {1: ('👑 Roi Zombie', 'red', 'Un zombie géant attaque le spawn ! Tape-le fort, le plus gros cogneur gagne.'),
         2: ('💰 Pluie de pièces', 'gold', 'Des pièces tombent du ciel ! Pépite = 1, lingot = 5. Le plus riche gagne.'),
         3: ('🗝 Chasse au trésor', 'aqua', 'Un coffre est caché sur l\'île. Suis les indices, le premier qui le trouve gagne.')}
EVI = '[minecraft:custom_data~{mg_ev:1b}]'

w('lobby/ev/tick', ['# Événements surprises (chaque tick, $setup 1)',
                    'scoreboard players add $evtk mg.st 1',
                    'execute if score $evtk mg.st matches 20.. run function mg:lobby/ev/second',
                    'execute if score $evon mg.st matches 1 run function mg:lobby/ev/e1_tick',
                    'execute if score $evon mg.st matches 3 as @e[type=minecraft:interaction,tag=mg.evti] if data entity @s interaction run function mg:lobby/ev/e3_click'])

w('lobby/ev/second', ['scoreboard players set $evtk mg.st 0',
                      'tag @a remove mg.evl',
                      'execute in minecraft:overworld run tag @a[x=-70,y=30,z=-70,dx=140,dy=100,dz=140,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] add mg.evl',
                      'execute unless score $evn mg.st matches -2147483648.. run scoreboard players set $evn mg.st ' + str(EVERY),
                      'execute if score $evon mg.st matches 1.. unless score $state mg.st matches 0 run return run function mg:lobby/ev/stop',
                      'execute if score $evon mg.st matches 1.. run return run function mg:lobby/ev/run',
                      'execute unless score $state mg.st matches 0 run return 0',
                      f'execute unless entity {L} run return 0',
                      'scoreboard players remove $evn mg.st 1',
                      'execute if score $evn mg.st matches 60 run function mg:lobby/ev/pick',
                      'execute if score $evn mg.st matches 1..60 run function mg:lobby/ev/countdown',
                      'execute if score $evn mg.st matches ..0 run function mg:lobby/ev/start'])

w('lobby/ev/pick', ['execute unless score $evk mg.st matches 1..3 store result score $evk mg.st run random value 1..3',
                    'bossbar add mg:ev ""', 'bossbar set mg:ev max 60', 'bossbar set mg:ev style notched_10'] +
  [f'execute if score $evk mg.st matches {k} run function mg:lobby/ev/ann_{k}' for k in NAMES])
for k, (nm, col, desc) in NAMES.items():
    w(f'lobby/ev/ann_{k}', [f'bossbar set mg:ev name ' + js([{'text': 'Événement : ', 'color': 'white'}, {'text': nm, 'color': col, 'bold': True}, {'text': ' dans 1 min', 'color': 'gray'}]),
                            f'bossbar set mg:ev color {"red" if col == "red" else "yellow" if col == "gold" else "blue"}',
                            'tellraw @a ' + js([{'text': '🎉 ÉVÉNEMENT SURPRISE au spawn dans 1 minute : ', 'color': 'light_purple', 'bold': True},
                                                {'text': nm, 'color': col, 'bold': True}, {'text': f'\n{desc}', 'color': 'gray'}]),
                            f'execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.bell.use master @s ~ ~ ~ 1 0.8'])
w('lobby/ev/countdown', [f'bossbar set mg:ev players {L}',
                         'execute store result bossbar mg:ev value run scoreboard players get $evn mg.st',
                         f'execute if score $evn mg.st matches 1..5 as {L} at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.4',
                         f'execute if score $evn mg.st matches 10 run title {L} actionbar {{"text":"🎉 L\'événement commence dans 10 s !","color":"light_purple"}}'])

w('lobby/ev/force', ['# Admin : événement au hasard dans 10 s', 'scoreboard players reset $evk mg.st', 'scoreboard players set $evn mg.st 61',
                     'function mg:lobby/ev/force_go'])
w('lobby/ev/force_go', ['execute unless score $state mg.st matches 0 run return run tellraw @s {"text":"Une partie est en cours.","color":"red"}',
                        'scoreboard players set $evn mg.st 60', 'function mg:lobby/ev/pick', 'scoreboard players set $evn mg.st 11'])
for k in NAMES:
    w(f'lobby/ev/force_{k}', [f'# Admin : événement {k} dans 10 s', f'scoreboard players set $evk mg.st {k}', 'function mg:lobby/ev/force_go'])

w('lobby/ev/start', [f'scoreboard players set $evn mg.st {EVERY}', 'scoreboard players operation $evon mg.st = $evk mg.st',
                     'scoreboard players reset $evk mg.st', f'scoreboard players set $evt mg.st {LEN}',
                     f'bossbar set mg:ev max {LEN}', 'bossbar set mg:ev style progress', f'bossbar set mg:ev players {L}',
                     'scoreboard players reset * mg.evd', 'scoreboard players reset * mg.evc',
                     f'execute as {L} at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1.2'] +
  [f'execute if score $evon mg.st matches {k} run function mg:lobby/ev/e{k}_start' for k in NAMES])

w('lobby/ev/run', ['scoreboard players remove $evt mg.st 1', f'bossbar set mg:ev players {L}'] +
  [f'execute if score $evon mg.st matches {k} run function mg:lobby/ev/e{k}_sec' for k in NAMES] +
  ['execute if score $evon mg.st matches 1.. if score $evt mg.st matches ..0 run function mg:lobby/ev/timeup'])
w('lobby/ev/timeup', ['execute if score $evon mg.st matches 1 run function mg:lobby/ev/e1_end',
                      'execute if score $evon mg.st matches 2 run function mg:lobby/ev/e2_end',
                      'execute if score $evon mg.st matches 3 run tellraw @a {"text":"🗝 Personne n\'a trouvé le trésor... il a disparu !","color":"gray"}',
                      'function mg:lobby/ev/stop'])
w('lobby/ev/stop', ['# Fin (ou partie lancée) : tout ce que l\'événement a posé disparaît',
                    'scoreboard players set $evon mg.st 0', 'bossbar remove mg:ev',
                    'kill @e[tag=mg.evx]', f'clear @a minecraft:gold_nugget{EVI}', f'clear @a minecraft:gold_ingot{EVI}',
                    f'clear @a minecraft:iron_sword{EVI}'])
w('lobby/ev/win', ['# @s : gagnant de l\'événement',
                   'scoreboard players add @s mg.evw 1',
                   'item replace entity @s armor.head with minecraft:golden_helmet[minecraft:item_name={"text":"👑 Couronne de champion","color":"gold","bold":true},'
                   'minecraft:enchantment_glint_override=true,minecraft:unbreakable={},minecraft:custom_data={mg_ev:1b}]',
                   'tellraw @a ' + js([{'text': '🏆 ', 'color': 'gold'}, {'selector': '@s', 'color': 'yellow', 'bold': True},
                                       {'text': ' remporte l\'événement ! (', 'color': 'gold'}, {'score': {'name': '@s', 'objective': 'mg.evw'}, 'color': 'yellow'},
                                       {'text': ' victoire(s) d\'événement)', 'color': 'gold'}]),
                   'title @s title {"text":"🏆 Champion !","color":"gold","bold":true}',
                   'execute at @s run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:20,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1,explosions:[{shape:"star",colors:[I;16766720,16777215],has_twinkle:true}]}}}}',
                   'execute at @s run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:30,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:2,explosions:[{shape:"large_ball",colors:[I;16711680,65535],has_trail:true}]}}}}',
                   'execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1'])

# ---------------------------------------------------------------- 👑 Roi Zombie
SWORD = ('minecraft:iron_sword[minecraft:item_name={"text":"⚔ Épée du spawn","color":"red"},minecraft:unbreakable={},'
         'minecraft:custom_data={mg_ev:1b}]')
w('lobby/ev/e1_start', ['execute store result storage mg:ev hp int 120 if entity @a[tag=mg.evl]',
                        'execute store result score $evhp mg.st run data get storage mg:ev hp',
                        'execute if score $evhp mg.st matches ..199 run data modify storage mg:ev hp set value 200',
                        'execute if score $evhp mg.st matches 1001.. run data modify storage mg:ev hp set value 1000',
                        'execute in minecraft:overworld run function mg:lobby/ev/e1_summon with storage mg:ev',
                        f'give {L} {SWORD}',
                        'bossbar set mg:ev color red',
                        f'title {L} title {{"text":"👑 LE ROI ZOMBIE","color":"red","bold":true}}',
                        f'title {L} subtitle {{"text":"Prends l\'épée et tape-le !","color":"gray"}}',
                        f'execute as {L} at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.7 1.3'])
w('lobby/ev/e1_summon', ['$summon minecraft:husk 0 65 6 {Tags:["mg.evx","mg.evb","mg.mob"],PersistenceRequired:1b,Glowing:1b,Health:$(hp)f,'
                         'CustomName:{"text":"👑 Roi Zombie","color":"red","bold":true},CustomNameVisible:1b,'
                         'equipment:{head:{id:"minecraft:golden_helmet",count:1},mainhand:{id:"minecraft:golden_axe",count:1}},drop_chances:{head:0f,mainhand:0f},'
                         'attributes:[{id:"minecraft:scale",base:3.5},{id:"minecraft:max_health",base:$(hp)},{id:"minecraft:attack_damage",base:3},'
                         '{id:"minecraft:movement_speed",base:0.22},{id:"minecraft:knockback_resistance",base:1},{id:"minecraft:follow_range",base:48}]}',
                         '$bossbar set mg:ev max $(hp)'])
w('lobby/ev/e1_tick', ['execute as @e[type=minecraft:husk,tag=mg.evx] at @s if entity @s[y=-64,dy=110] run tp @s 0 66 6'])
w('lobby/ev/e1_sec', ['execute unless entity @e[tag=mg.evb] run return run function mg:lobby/ev/e1_dead',
                      'bossbar set mg:ev name [{"text":"👑 Roi Zombie","color":"red","bold":true},{"text":"  (tape-le !)","color":"gray"}]',
                      'execute store result bossbar mg:ev value run data get entity @e[tag=mg.evb,limit=1] Health',
                      'scoreboard players operation $evm mg.st = $evt mg.st', 'scoreboard players operation $evm mg.st %= #ev10 mg.st',
                      'execute if score $evm mg.st matches 0 if score $evt mg.st matches 1..170 at @e[tag=mg.evb,limit=1] run function mg:lobby/ev/e1_minions'])
w('lobby/ev/e1_minions', ['execute if entity @e[type=minecraft:husk,tag=mg.evm,limit=6] run return 0',
                          'summon minecraft:husk ~1 ~ ~ {Tags:["mg.evx","mg.evm","mg.mob"],IsBaby:1b,PersistenceRequired:1b,attributes:[{id:"minecraft:attack_damage",base:1}]}',
                          'summon minecraft:husk ~-1 ~ ~ {Tags:["mg.evx","mg.evm","mg.mob"],IsBaby:1b,PersistenceRequired:1b,attributes:[{id:"minecraft:attack_damage",base:1}]}',
                          'playsound minecraft:entity.zombie.ambient hostile @a ~ ~ ~ 2 0.5',
                          'particle minecraft:large_smoke ~ ~2 ~ 1 1 1 0.05 30'])
w('lobby/ev/e1_dead', ['tellraw @a {"text":"👑 Le Roi Zombie est tombé !","color":"red","bold":true}',
                       'function mg:lobby/ev/e1_end', 'function mg:lobby/ev/stop'])
w('lobby/ev/e1_end', ['execute if entity @e[tag=mg.evb] run tellraw @a {"text":"👑 Le Roi Zombie retourne dans son trou...","color":"gray"}',
                      'scoreboard players set $evbest mg.st 0', f'execute as {L} run scoreboard players operation $evbest mg.st > @s mg.evd',
                      f'execute if score $evbest mg.st matches 1.. as {L} if score @s mg.evd = $evbest mg.st run tag @s add mg.evwin',
                      'execute as @a[tag=mg.evwin,limit=1,sort=random] run function mg:lobby/ev/win', 'tag @a remove mg.evwin'])

# ---------------------------------------------------------------- 💰 Pluie de pièces (60 s)
COIN = 'components:{{"minecraft:custom_data":{{mg_ev:1b}},"minecraft:item_name":{{"text":"{n}","color":"gold"}}}}'
w('lobby/ev/e2_start', [f'scoreboard players set $evt mg.st 60', 'bossbar set mg:ev max 60', 'bossbar set mg:ev color yellow',
                        f'title {L} title {{"text":"💰 PLUIE DE PIÈCES","color":"gold","bold":true}}',
                        f'title {L} subtitle {{"text":"Ramasse tout ce qui tombe !","color":"gray"}}'])
w('lobby/ev/e2_sec', ['bossbar set mg:ev name {"text":"💰 Pluie de pièces","color":"gold","bold":true}',
                      'execute store result bossbar mg:ev value run scoreboard players get $evt mg.st',
                      'execute in minecraft:overworld run function mg:lobby/ev/e2_coin', 'execute in minecraft:overworld run function mg:lobby/ev/e2_coin',
                      'execute in minecraft:overworld run function mg:lobby/ev/e2_coin', 'execute in minecraft:overworld run function mg:lobby/ev/e2_coin',
                      'execute in minecraft:overworld run function mg:lobby/ev/e2_coin', 'execute in minecraft:overworld run function mg:lobby/ev/e2_coin',
                      f'execute as {L} run function mg:lobby/ev/e2_count'])
w('lobby/ev/e2_coin', ['summon minecraft:marker 0 64 0 {Tags:["mg.evx","mg.evp"]}',
                       'spreadplayers 0 0 0 40 under 85 false @e[type=minecraft:marker,tag=mg.evp]',
                       'execute store result score $evr mg.st run random value 1..8',
                       'execute at @e[type=minecraft:marker,tag=mg.evp] if score $evr mg.st matches 1 run summon minecraft:item ~ ~14 ~ {Tags:["mg.evx","mg.keep"],Glowing:1b,Item:{id:"minecraft:gold_ingot",count:1,'
                       + COIN.format(n='Gros lingot (5)') + '}}',
                       'execute at @e[type=minecraft:marker,tag=mg.evp] unless score $evr mg.st matches 1 run summon minecraft:item ~ ~14 ~ {Tags:["mg.evx","mg.keep"],Item:{id:"minecraft:gold_nugget",count:1,'
                       + COIN.format(n='Pièce (1)') + '}}',
                       'execute at @e[type=minecraft:marker,tag=mg.evp] run particle minecraft:wax_on ~ ~14 ~ 0.3 0.3 0.3 0 5',
                       'kill @e[type=minecraft:marker,tag=mg.evp]'])
w('lobby/ev/e2_count', [f'execute store result score @s mg.evc run clear @s minecraft:gold_nugget{EVI} 0',
                        f'execute store result score #evi mg.st run clear @s minecraft:gold_ingot{EVI} 0',
                        'scoreboard players operation #evi mg.st *= #ev5 mg.st', 'scoreboard players operation @s mg.evc += #evi mg.st',
                        'title @s actionbar [{"text":"💰 ","color":"gold"},{"score":{"name":"@s","objective":"mg.evc"},"color":"yellow","bold":true},{"text":" pièces","color":"gold"}]'])
w('lobby/ev/e2_end', [f'execute as {L} run function mg:lobby/ev/e2_count',
                      'scoreboard players set $evbest mg.st 0', f'execute as {L} run scoreboard players operation $evbest mg.st > @s mg.evc',
                      f'execute if score $evbest mg.st matches 1.. as {L} if score @s mg.evc = $evbest mg.st run tag @s add mg.evwin',
                      'execute as @a[tag=mg.evwin,limit=1,sort=random] run tellraw @a [{"text":"💰 Le plus riche : ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" (","color":"gray"},{"score":{"name":"$evbest","objective":"mg.st"},"color":"yellow"},{"text":" pièces)","color":"gray"}]',
                      'execute as @a[tag=mg.evwin,limit=1,sort=random] run function mg:lobby/ev/win', 'tag @a remove mg.evwin'])

# ---------------------------------------------------------------- 🗝 Chasse au trésor
w('lobby/ev/e3_start', ['bossbar set mg:ev color blue',
                        'execute in minecraft:overworld run summon minecraft:marker 0 64 0 {Tags:["mg.evx","mg.evt"]}',
                        'execute in minecraft:overworld run spreadplayers 0 0 0 45 under 75 false @e[type=minecraft:marker,tag=mg.evt]',
                        'execute in minecraft:overworld at @e[type=minecraft:marker,tag=mg.evt] align xz positioned ~0.5 ~ ~0.5 run function mg:lobby/ev/e3_place',
                        f'title {L} title {{"text":"🗝 CHASSE AU TRÉSOR","color":"aqua","bold":true}}',
                        f'title {L} subtitle {{"text":"Un coffre est caché sur l\'île","color":"gray"}}'])
w('lobby/ev/e3_place', ['summon minecraft:item_display ~ ~0.5 ~ {Tags:["mg.evx","mg.evtc"],item:{id:"minecraft:chest",count:1},item_display:"none"}',
                        'summon minecraft:interaction ~ ~ ~ {Tags:["mg.evx","mg.evti"],width:1.1f,height:1.1f,response:1b}'])
w('lobby/ev/e3_sec', ['bossbar set mg:ev name {"text":"🗝 Chasse au trésor","color":"aqua","bold":true}',
                      'execute store result bossbar mg:ev value run scoreboard players get $evt mg.st',
                      f'execute as {L} run title @s actionbar {{"text":"❄ Froid","color":"blue"}}',
                      f'execute at @e[type=minecraft:marker,tag=mg.evt] as @a[tag=mg.evl,distance=..45] run title @s actionbar {{"text":"🌡 Tiède","color":"yellow"}}',
                      f'execute at @e[type=minecraft:marker,tag=mg.evt] as @a[tag=mg.evl,distance=..22] run title @s actionbar {{"text":"🔥 Chaud !","color":"gold"}}',
                      f'execute at @e[type=minecraft:marker,tag=mg.evt] as @a[tag=mg.evl,distance=..9] run title @s actionbar {{"text":"🔥🔥 Brûlant !!","color":"red","bold":true}}',
                      'execute if score $evt mg.st matches 90 run data merge entity @e[type=minecraft:item_display,tag=mg.evtc,limit=1] {Glowing:1b,glow_color_override:16766720}',
                      'execute if score $evt mg.st matches 90 run tellraw @a[tag=mg.evl] {"text":"🗝 Indice : le coffre brille maintenant !","color":"aqua"}',
                      'execute if score $evt mg.st matches 45 at @e[type=minecraft:marker,tag=mg.evt] run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:25,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:2,explosions:[{shape:"burst",colors:[I;65535]}]}}}}',
                      'execute if score $evt mg.st matches 45 run tellraw @a[tag=mg.evl] {"text":"🗝 Indice : regarde la fusée !","color":"aqua"}',
                      'execute at @e[type=minecraft:marker,tag=mg.evt] run particle minecraft:end_rod ~ ~0.5 ~ 0.3 0.3 0.3 0.01 2'])
w('lobby/ev/e3_click', ['# @s : le coffre, quelqu\'un a cliqué', 'execute on target if entity @s[tag=mg.evl] run tag @s add mg.evwin',
                        'data remove entity @s interaction',
                        'execute unless entity @a[tag=mg.evwin] run return 0',
                        'tellraw @a [{"text":"🗝 ","color":"aqua"},{"selector":"@a[tag=mg.evwin,limit=1]","color":"yellow"},{"text":" a trouvé le trésor !","color":"aqua"}]',
                        'execute at @s run particle minecraft:totem_of_undying ~ ~0.5 ~ 0.4 0.4 0.4 0.4 60',
                        'execute as @a[tag=mg.evwin,limit=1] run function mg:lobby/ev/win', 'tag @a remove mg.evwin',
                        'function mg:lobby/ev/stop'])

# ---------------------------------------------------------------- câblage
C.objectives([('mg.evd', 'minecraft.custom:minecraft.damage_dealt'), ('mg.evc', 'dummy'), ('mg.evw', 'dummy')])
C.patch('core/load', 'scoreboard objectives add mg.evw dummy', ['scoreboard players set #ev5 mg.st 5', 'scoreboard players set #ev10 mg.st 10'])
C.patch('core/tick', 'execute if score $setup mg.st matches 1 run function mg:lobby/armory_tick',
        ['execute if score $setup mg.st matches 1 run function mg:lobby/ev/tick'])
print('ok')
