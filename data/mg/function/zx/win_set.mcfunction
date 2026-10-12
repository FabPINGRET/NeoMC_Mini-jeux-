# Blocs de la fenêtre (@s, à sa position) selon ses planches
execute if score @s mg.zws matches 5.. run fill ~ ~ ~ ~ ~1 ~ minecraft:spruce_planks
execute if score @s mg.zws matches 3..4 run setblock ~ ~ ~ minecraft:spruce_planks
execute if score @s mg.zws matches 3..4 run setblock ~ ~1 ~ minecraft:spruce_fence
execute if score @s mg.zws matches 1..2 run setblock ~ ~ ~ minecraft:spruce_fence
execute if score @s mg.zws matches 1..2 run setblock ~ ~1 ~ minecraft:air
execute if score @s mg.zws matches ..0 run fill ~ ~ ~ ~ ~1 ~ minecraft:air
