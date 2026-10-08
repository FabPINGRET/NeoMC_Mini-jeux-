# @s = marqueur du bloc courant (position = coin du bloc) : le porteur l'a quitté → mur de 2 blocs à sa couleur
execute if score @s mg.trc matches 0 run fill ~ ~ ~ ~ ~1 ~ minecraft:red_wool replace #minecraft:air
execute if score @s mg.trc matches 1 run fill ~ ~ ~ ~ ~1 ~ minecraft:blue_wool replace #minecraft:air
execute if score @s mg.trc matches 2 run fill ~ ~ ~ ~ ~1 ~ minecraft:lime_wool replace #minecraft:air
execute if score @s mg.trc matches 3 run fill ~ ~ ~ ~ ~1 ~ minecraft:yellow_wool replace #minecraft:air
execute if score @s mg.trc matches 4 run fill ~ ~ ~ ~ ~1 ~ minecraft:orange_wool replace #minecraft:air
execute if score @s mg.trc matches 5 run fill ~ ~ ~ ~ ~1 ~ minecraft:magenta_wool replace #minecraft:air
execute if score @s mg.trc matches 6 run fill ~ ~ ~ ~ ~1 ~ minecraft:cyan_wool replace #minecraft:air
execute if score @s mg.trc matches 7 run fill ~ ~ ~ ~ ~1 ~ minecraft:white_wool replace #minecraft:air
execute if score @s mg.trc matches 8 run fill ~ ~ ~ ~ ~1 ~ minecraft:purple_wool replace #minecraft:air
execute if score @s mg.trc matches 9 run fill ~ ~ ~ ~ ~1 ~ minecraft:pink_wool replace #minecraft:air
execute if score @s mg.trc matches 10 run fill ~ ~ ~ ~ ~1 ~ minecraft:light_blue_wool replace #minecraft:air
execute if score @s mg.trc matches 11 run fill ~ ~ ~ ~ ~1 ~ minecraft:green_wool replace #minecraft:air
execute if score @s mg.trc matches 12 run fill ~ ~ ~ ~ ~1 ~ minecraft:brown_wool replace #minecraft:air
execute if score @s mg.trc matches 13 run fill ~ ~ ~ ~ ~1 ~ minecraft:light_gray_wool replace #minecraft:air
execute if score @s mg.trc matches 14 run fill ~ ~ ~ ~ ~1 ~ minecraft:gray_wool replace #minecraft:air
execute if score @s mg.trc matches 15 run fill ~ ~ ~ ~ ~1 ~ minecraft:black_wool replace #minecraft:air
tp @e[tag=mg.tpm,limit=1] @s
tp @s @e[tag=mg.tcar,limit=1]
scoreboard players set @a[tag=mg.tme] mg.trs 0
