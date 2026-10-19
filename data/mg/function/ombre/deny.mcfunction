# @s entre dans une région pas encore ouverte : retour en arrière
execute store result storage mg:ombre d.x int 1 run scoreboard players get @s mg.olsx
execute store result storage mg:ombre d.y int 1 run scoreboard players get @s mg.olsy
execute store result storage mg:ombre d.z int 1 run scoreboard players get @s mg.olsz
function mg:ombre/back with storage mg:ombre d
tellraw @s {"text":"⛔ Cette région n'est pas encore accessible : suis la campagne (📜 dans le journal).","color":"red"}
execute at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 0.8 0.6
