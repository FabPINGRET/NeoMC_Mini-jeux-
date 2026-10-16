# @s (joueur) touché par le venin
effect give @s minecraft:poison 4 0
effect give @s minecraft:blindness 3 0 true
damage @s 2 minecraft:mob_attack by @e[tag=mg.trsrc,limit=1]
particle minecraft:item_slime ~ ~1.5 ~ 0.3 0.3 0.3 0 12
title @s actionbar {"text":"🟢 Venin de dilophosaure !","color":"green","bold":true}
scoreboard players set @s mg.tval 30
