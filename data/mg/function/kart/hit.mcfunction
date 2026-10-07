# @s touché (carapace, banane, éclair, étoile) : tête-à-queue, sauf en étoile
execute if score @s mg.kst matches 1.. run return 0
scoreboard players set @s mg.khi 24
scoreboard players set @s mg.kbo 0
scoreboard players set @s mg.kdr 0
scoreboard players set @s mg.krc 0
title @s actionbar [{"text":"💥 Touché !","color":"red","bold":true}]
scoreboard players operation $kh mg.st = @s mg.ri
execute as @e[type=minecraft:block_display,tag=mg.kart] if score @s mg.ri = $kh mg.st at @s run particle minecraft:explosion ~ ~0.5 ~ 0.3 0.3 0.3 0 2
execute as @e[type=minecraft:block_display,tag=mg.kart] if score @s mg.ri = $kh mg.st at @s run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..24] ~ ~ ~ 0.4 1.6
