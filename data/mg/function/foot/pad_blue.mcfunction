# @s marche sur le socle blue : équipe Équipe bleue (foot/tick ne l'appelle pas à qui a déjà mg.ftb)
tag @s add mg.ftb
tag @s remove mg.ftr
team join mg_ftb @s
scoreboard players add $eq mg.ftn 1
title @s actionbar {"text":"🔵 Équipe bleue","color":"blue","bold":true}
execute at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.2
