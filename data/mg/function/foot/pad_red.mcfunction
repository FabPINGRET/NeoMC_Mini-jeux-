# @s marche sur le socle red : équipe Équipe rouge (foot/tick ne l'appelle pas à qui a déjà mg.ftr)
tag @s add mg.ftr
tag @s remove mg.ftb
team join mg_ftr @s
scoreboard players add $eq mg.ftn 1
title @s actionbar {"text":"🔴 Équipe rouge","color":"red","bold":true}
execute at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.2
