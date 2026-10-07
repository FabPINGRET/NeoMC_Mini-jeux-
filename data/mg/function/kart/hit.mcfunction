# @s touché (carapace, banane, éclair, étoile) : tête-à-queue, sauf en étoile
execute if score @s mg.kst matches 1.. run return 0
scoreboard players set @s mg.khi 24
scoreboard players set @s mg.kbo 0
scoreboard players set @s mg.kdr 0
title @s actionbar [{"text":"💥 Touché !","color":"red","bold":true}]
execute at @s run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..24] ~ ~ ~ 0.4 1.6
execute at @s run particle minecraft:explosion ~ ~0.5 ~ 0.3 0.3 0.3 0 2
