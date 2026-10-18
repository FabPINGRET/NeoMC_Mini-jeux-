# Prise : un bidon rouillé (junk, poids 50 sur 1000) ; @s = joueur, effets au marqueur mg.lfx
scoreboard players add $junk mg.lfn 1
title @s actionbar {"text":"🎣 Un bidon rouillé... ça ne se mange pas.","color":"dark_gray"}
execute at @e[type=minecraft:marker,tag=mg.lfx,limit=1] run playsound minecraft:entity.villager.no player @a[distance=..16] ~ ~ ~ 1 1.2
execute at @e[type=minecraft:marker,tag=mg.lfx,limit=1] run particle minecraft:smoke ~ ~0.3 ~ 0.2 0.1 0.2 0.02 8 normal @a[distance=..16]
