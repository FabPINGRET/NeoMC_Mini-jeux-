effect give @s minecraft:levitation 2 1
effect give @s minecraft:darkness 4 0 true
title @s actionbar {"text":"🕸 Malédiction de Morvaine !","color":"dark_purple"}
scoreboard players set @s mg.olal 30
execute at @s run playsound minecraft:entity.witch.celebrate hostile @s ~ ~ ~ 1 0.6
