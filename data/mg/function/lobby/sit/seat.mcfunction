# @s = joueur ; position = point d'assise, rotation = sens du regard (posés par sit/try ou sit/bench) ; retourne 1
summon minecraft:item_display ~ ~ ~ {Tags:["mg.seat","mg.seatn"]}
# s'asseoir arrête le mouvement d'une emote en cours (sit_move.py), avant le tp qui fixe le regard
execute if entity @s[tag=mg.lsm] run function mg:lobby/sit/move_stop
tp @s ~ ~ ~ ~ ~
execute store success score #sitm mg.st run ride @s mount @e[type=minecraft:item_display,tag=mg.seatn,distance=..1,sort=nearest,limit=1]
execute if score #sitm mg.st matches 1 run tag @s add mg.sit
execute if score #sitm mg.st matches 1 run scoreboard players add $sit mg.lsn 1
execute if score #sitm mg.st matches 1 run title @s actionbar {"text":"🪑 Assis · Maj pour te lever","color":"gray"}
execute if score #sitm mg.st matches 0 run title @s actionbar {"text":"🪑 Impossible de s'asseoir ici.","color":"gray"}
execute if score #sitm mg.st matches 0 run kill @e[type=minecraft:item_display,tag=mg.seatn,distance=..1]
tag @e[type=minecraft:item_display,tag=mg.seatn] remove mg.seatn
return 1
