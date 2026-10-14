tag @s remove mg.tvout
scoreboard players set @s mg.tval 40
title @s actionbar {"text":"🏠 De retour dans la colonie : tu es en sécurité","color":"green"}
execute at @s run playsound minecraft:block.note_block.chime player @s ~ ~ ~ 0.5 1.4
