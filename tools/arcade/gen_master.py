"""👑 Master dit — id 226. Ordres très rapides ; les consignes sans « Master dit » sont des pièges. Plateforme en z 38600.

    python tools/arcade/gen_master.py .

Ordres : sauter, s'accroupir, sprinter, regarder le ciel, regarder le sol, ne plus bouger, aller sur une couleur (4 quarts).
- « Master dit : … » → il faut le faire avant la fin du délai (sinon éliminé).
- La même consigne SANS « Master dit » (sauter, s'accroupir, sprinter seulement) → la faire = éliminé.
- Le délai raccourcit à chaque tour (3 s → 1 s). Si tout le monde rate le même tour, le tour est annulé.
- Dernier debout = victoire ; 5 min max (match nul s'il reste plusieurs joueurs). Seul : entraînement de 20 tours.
"""
import json
import os
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
GID = 226
Z = C.param('Z', 38600)
Y = 70
RAD = 9
LIMIT = 6000
GRACE = 6                     # ticks avant de compter un mouvement / une action piège

for name, inp in (('ms_jump', 'jump'), ('ms_sprint', 'sprint')):
    with open(os.path.join(C.D, 'predicate', f'{name}.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'condition': 'minecraft:entity_properties', 'entity': 'this',
                   'predicate': {'minecraft:type_specific/player': {'input': {inp: True}}}}, f, indent=2)
        f.write('\n')

# ordres : n, texte, piège possible
ORD = [(1, 'Sautez !', True), (2, 'Accroupissez-vous !', True), (3, 'Sprintez !', True), (4, 'Regardez le ciel !', False),
       (5, 'Regardez le sol !', False), (6, 'Ne bougez plus !', False), (7, 'Sur le ROUGE !', False), (8, 'Sur le BLEU !', False),
       (9, 'Sur le VERT !', False), (10, 'Sur le JAUNE !', False)]
COLORS = {7: 'red_concrete', 8: 'blue_concrete', 9: 'lime_concrete', 10: 'yellow_concrete'}

# ------------------------------------------------------------------ plateforme
B = [f'# 👑 Master dit — plateforme ronde (rayon {RAD}) en 0 {Y} {Z}, 4 quarts de couleur']
B += [f'fill -{RAD + 3} {y} {Z - RAD - 3} {RAD + 3} {y} {Z + RAD + 3} minecraft:air' for y in range(Y - 2, Y + 10)]
for x in range(-RAD - 1, RAD + 2):
    for z in range(-RAD - 1, RAD + 2):
        d = (x * x + z * z) ** 0.5
        if d <= RAD + 0.5:
            if d <= 1.6:
                blk = 'white_concrete'
            else:
                blk = {(True, True): 'red_concrete', (False, True): 'blue_concrete', (False, False): 'lime_concrete', (True, False): 'yellow_concrete'}[(x >= 0, z < 0)]
            B.append(f'setblock {x} {Y - 1} {Z + z} minecraft:{blk}')
        elif d <= RAD + 1.6:
            B += [f'setblock {x} {Y - 1} {Z + z} minecraft:quartz_block', f'fill {x} {Y} {Z + z} {x} {Y + 4} {Z + z} minecraft:barrier']
B += [f'fill -{RAD + 1} {Y + 5} {Z - RAD - 1} {RAD + 1} {Y + 5} {Z + RAD + 1} minecraft:barrier']
w('master/build', B)

PL = '@a[tag=mg.play]'
w('master/prepare', ['# 👑 Master dit — préparation', 'function mg:master/build', 'kill @e[tag=mg.msd]',
                     f'summon minecraft:text_display 0.5 {Y + 7} {Z}.5 {{Tags:["mg.msd","mg.fx"],billboard:"center",background:0,'
                     'text:{"text":"👑 MASTER","color":"gold","bold":true},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[3f,3f,3f]}}',
                     'scoreboard players set $px mg.st 0', f'scoreboard players set $py mg.st {Y + 9}', f'scoreboard players set $pz mg.st {Z}',
                     f'clear {PL}', f'effect clear {PL}', f'gamemode adventure {PL}', f'team join mg_sq {PL}',
                     f'spreadplayers 0 {Z} 2 {RAD - 2} under {Y + 3} false {PL}',
                     f'execute as {PL} at @s run spawnpoint @s ~ ~ ~', 'scoreboard players set $msr mg.st 0'])
w('master/go', ['# Départ : premier ordre dans 2 s', 'scoreboard players set $msp mg.st 0', 'scoreboard players set $mst mg.st 40',
                'scoreboard players set $msc mg.st 0',
                f'tellraw {PL} ' + js([{'text': '👑 MASTER DIT : ', 'color': 'gold', 'bold': True},
                                        {'text': 'obéis aux ordres qui commencent par « Master dit » ; les autres sont des pièges, ne les fais pas ! '
                                                 'Trop lent ou piégé = éliminé. Ça va de plus en plus vite…', 'color': 'gray'}])])
# nouvel ordre
NEW = ['# Nouvel ordre ($mso = ordre, $msv = 1 vrai / 0 piège, délai $msw)', 'scoreboard players add $msr mg.st 1',
       'execute store result score $mso mg.st run random value 1..10', 'scoreboard players set $msv mg.st 1',
       # piège ~35 % sur les ordres 1..3
       'execute store result score $r mg.st run random value 1..100',
       'execute if score $mso mg.st matches 1..3 if score $r mg.st matches ..35 run scoreboard players set $msv mg.st 0',
       # délai : 60 − 2 × tour, 20 minimum
       'scoreboard players set $msw mg.st 60', 'scoreboard players operation $r mg.st = $msr mg.st', 'scoreboard players operation $r mg.st *= #2 mg.st',
       'scoreboard players operation $msw mg.st -= $r mg.st', 'execute if score $msw mg.st matches ..19 run scoreboard players set $msw mg.st 20',
       'scoreboard players operation $mst mg.st = $msw mg.st', 'scoreboard players set $msp mg.st 1',
       f'tag {PL} remove mg.mso', f'tag {PL} remove mg.msf',
       f'execute store result storage mg:ms t.d int 1 run scoreboard players get $msw mg.st']
for n, txt, trap in ORD:
    NEW.append(f'execute if score $mso mg.st matches {n} if score $msv mg.st matches 1 run function mg:master/say {{t:"{txt}",m:"👑 Master dit : "}}')
    if trap:
        NEW.append(f'execute if score $mso mg.st matches {n} if score $msv mg.st matches 0 run function mg:master/say {{t:"{txt}",m:""}}')
w('master/new', NEW)
w('master/say', ['function mg:master/times with storage mg:ms t',
                 '$title @a[tag=mg.play] title [{"text":"$(m)","color":"gold","bold":true},{"text":"$(t)","color":"white","bold":true}]',
                 'title @a[tag=mg.play] subtitle ""',
                 'execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.bit master @s ~ ~ ~ 1 1.6'])
w('master/times', ['$title @a[tag=mg.play] times 0 $(d) 4'])
w('master/mark', ['# @s : position au début du délai (après la petite grâce)',
                  'execute store result score @s mg.msx run data get entity @s Pos[0] 100',
                  'execute store result score @s mg.msz run data get entity @s Pos[2] 100'])
w('master/moved', ['# @s a-t-il bougé (> 0,1 bloc) depuis la marque ?',
                   'execute store result score $a mg.st run data get entity @s Pos[0] 100', 'scoreboard players operation $a mg.st -= @s mg.msx',
                   'execute unless score $a mg.st matches -10..10 run return run tag @s add mg.msf',
                   'execute store result score $a mg.st run data get entity @s Pos[2] 100', 'scoreboard players operation $a mg.st -= @s mg.msz',
                   'execute unless score $a mg.st matches -10..10 run tag @s add mg.msf'])
w('master/pitch', ['execute store result score @s mg.t run data get entity @s Rotation[1]'])
# pendant le délai
W = ['# Pendant le délai : on note qui fait l\'action (mg.mso) ou qui tombe dans le piège / bouge (mg.msf)',
     'scoreboard players operation $e mg.st = $msw mg.st',
     'scoreboard players operation $e mg.st -= $mst mg.st',
     # vrais ordres
     f'execute if score $msv mg.st matches 1 if score $mso mg.st matches 1 as {PL} if predicate mg:ms_jump run tag @s add mg.mso',
     f'execute if score $msv mg.st matches 1 if score $mso mg.st matches 2 as {PL} if predicate mg:sneak run tag @s add mg.mso',
     f'execute if score $msv mg.st matches 1 if score $mso mg.st matches 3 as {PL} if predicate mg:ms_sprint run tag @s add mg.mso',
     f'execute if score $mso mg.st matches 4..5 as {PL} run function mg:master/pitch',
     'execute if score $mso mg.st matches 4 as @a[tag=mg.play,scores={mg.t=..-50}] run tag @s add mg.mso',
     'execute if score $mso mg.st matches 5 as @a[tag=mg.play,scores={mg.t=50..}] run tag @s add mg.mso',
     f'execute if score $mso mg.st matches 6 if score $e mg.st matches {GRACE * 2} as {PL} run function mg:master/mark',
     f'execute if score $mso mg.st matches 6 if score $e mg.st matches {GRACE * 2 + 1}.. as {PL} run function mg:master/moved',
     # pièges (après une petite grâce : le temps de lire)
     f'execute if score $msv mg.st matches 0 if score $e mg.st matches {GRACE}.. if score $mso mg.st matches 1 as {PL} if predicate mg:ms_jump run tag @s add mg.msf',
     f'execute if score $msv mg.st matches 0 if score $e mg.st matches {GRACE}.. if score $mso mg.st matches 2 as {PL} if predicate mg:sneak run tag @s add mg.msf',
     f'execute if score $msv mg.st matches 0 if score $e mg.st matches {GRACE}.. if score $mso mg.st matches 3 as {PL} if predicate mg:ms_sprint run tag @s add mg.msf']
w('master/window', W)
# fin du délai : qui échoue ?
E = ['# Fin du délai : échecs → tag mg.msk ; tout le monde a raté → tour annulé', f'tag {PL} remove mg.msk',
     'execute if score $msv mg.st matches 1 if score $mso mg.st matches 1..5 as @a[tag=mg.play,tag=!mg.mso] run tag @s add mg.msk',
     'execute if score $mso mg.st matches 6 as @a[tag=mg.play,tag=mg.msf] run tag @s add mg.msk',
     'execute if score $msv mg.st matches 0 as @a[tag=mg.play,tag=mg.msf] run tag @s add mg.msk']
for n, blk in COLORS.items():
    E.append(f'execute if score $mso mg.st matches {n} as @a[tag=mg.play] at @s unless block ~ ~-0.5 ~ minecraft:{blk} run tag @s add mg.msk')
E += ['execute store result score $k mg.st if entity @a[tag=mg.msk]', 'execute store result score $a mg.st if entity @a[tag=mg.play]',
      'scoreboard players set $msp mg.st 2', 'scoreboard players set $mst mg.st 30',
      'execute if score $msv mg.st matches 0 if score $k mg.st matches 0 run title @a[tag=mg.play] actionbar {"text":"✔ Piège évité par tout le monde !","color":"green"}',
      'execute if score $k mg.st matches 0 if score $msv mg.st matches 1 run title @a[tag=mg.play] actionbar {"text":"✔ Tout le monde a réussi","color":"green"}',
      'execute if score $k mg.st matches 1.. if score $k mg.st = $a mg.st run return run function mg:master/void',
      'execute if score $k mg.st matches 1.. as @a[tag=mg.msk] run function mg:master/ko']
w('master/end_round', E)
w('master/void', ['tellraw @a[tag=mg.play] {"text":"👑 Tout le monde a raté : tour annulé !","color":"yellow"}', 'tag @a remove mg.msk',
                  'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.villager.no master @s ~ ~ ~ 1 1'])
w('master/ko', ['# @s a raté', 'tag @s remove mg.msk',
                'execute if score $msv mg.st matches 0 run tellraw @a[tag=!mg.surv] [{"text":"👑 ","color":"gold"},{"selector":"@s","color":"red"},{"text":" est tombé dans le piège !","color":"gray"}]',
                'execute if score $msv mg.st matches 1 run tellraw @a[tag=!mg.surv] [{"text":"👑 ","color":"gold"},{"selector":"@s","color":"red"},{"text":" a été trop lent !","color":"gray"}]',
                'scoreboard players add @s mg.msm 1',
                'execute if score $n0 mg.st matches 2.. run return run function mg:core/eliminate',
                'title @s actionbar {"text":"✖ Raté ! (entraînement)","color":"red"}'])
w('master/tick', ['# 👑 Master dit — tick', 'scoreboard players add $msc mg.st 1', 'scoreboard players remove $mst mg.st 1',
                  'execute if score $msp mg.st matches 1 run function mg:master/window',
                  'execute if score $msp mg.st matches 1 if score $mst mg.st matches ..0 run function mg:master/end_round',
                  'execute if score $msp mg.st matches 0 if score $mst mg.st matches ..0 run function mg:master/new',
                  'execute if score $msp mg.st matches 2 if score $mst mg.st matches ..0 run function mg:master/new',
                  'execute store result score $a mg.st if entity @a[tag=mg.play]',
                  'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $a mg.st matches ..1 run return run function mg:master/end',
                  'execute if score $state mg.st matches 2 unless score $n0 mg.st matches 2.. if score $msr mg.st matches 21.. run return run function mg:master/end',
                  f'execute if score $state mg.st matches 2 if score $msc mg.st matches {LIMIT}.. run function mg:master/end'])
w('master/end', ['# Fin : dernier debout gagne ; sinon match nul', 'execute unless score $state mg.st matches 2 run return 0',
                 'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"👑 Fin de l\'entraînement : ","color":"yellow"},{"score":{"name":"@p[tag=mg.play]","objective":"mg.msm"},"color":"red"},{"text":" erreur(s) sur 20 ordres.","color":"yellow"}]',
                 'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                 'execute store result score $a mg.st if entity @a[tag=mg.play]',
                 'execute if score $a mg.st matches 1 as @a[tag=mg.play,limit=1] run return run function mg:core/win_player',
                 'function mg:core/draw'])
w('master/cleanup', ['kill @e[tag=mg.msd]', 'tag @a remove mg.mso', 'tag @a remove mg.msf', 'tag @a remove mg.msk',
                     'scoreboard players reset * mg.msm', 'team leave @a[team=mg_sq]', 'title @a reset'])

C.register([GID], 'master', [C.announce(GID, '', '👑 MASTER DIT', 'gold', 'obéis vite aux ordres du Master… mais seulement quand il dit « Master dit » !')])
C.objectives([('mg.msx', 'dummy'), ('mg.msz', 'dummy'), ('mg.msm', 'dummy')])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['data remove storage mg:ms t'])
C.forceload([f'# Master dit (z {Z})', f'forceload add -{RAD + 3} {Z - RAD - 3} {RAD + 3} {Z + RAD + 3}'])
print('Master dit OK')
