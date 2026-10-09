# 🦎 Meccha Chameleon : préparation (maison, rôles, cage)
function mg:cham/build
function mg:cham/kill_all
data modify storage mg:cham mats set value [{Name:"minecraft:air"},{Name:"minecraft:white_concrete"},{Name:"minecraft:orange_concrete"},{Name:"minecraft:magenta_concrete"},{Name:"minecraft:light_blue_concrete"},{Name:"minecraft:yellow_concrete"},{Name:"minecraft:lime_concrete"},{Name:"minecraft:pink_concrete"},{Name:"minecraft:gray_concrete"},{Name:"minecraft:light_gray_concrete"},{Name:"minecraft:cyan_concrete"},{Name:"minecraft:purple_concrete"},{Name:"minecraft:blue_concrete"},{Name:"minecraft:brown_concrete"},{Name:"minecraft:green_concrete"},{Name:"minecraft:red_concrete"},{Name:"minecraft:black_concrete"},{Name:"minecraft:white_wool"},{Name:"minecraft:orange_wool"},{Name:"minecraft:magenta_wool"},{Name:"minecraft:light_blue_wool"},{Name:"minecraft:yellow_wool"},{Name:"minecraft:lime_wool"},{Name:"minecraft:pink_wool"},{Name:"minecraft:gray_wool"},{Name:"minecraft:light_gray_wool"},{Name:"minecraft:cyan_wool"},{Name:"minecraft:purple_wool"},{Name:"minecraft:blue_wool"},{Name:"minecraft:brown_wool"},{Name:"minecraft:green_wool"},{Name:"minecraft:red_wool"},{Name:"minecraft:black_wool"},{Name:"minecraft:terracotta"},{Name:"minecraft:white_terracotta"},{Name:"minecraft:orange_terracotta"},{Name:"minecraft:yellow_terracotta"},{Name:"minecraft:red_terracotta"},{Name:"minecraft:brown_terracotta"},{Name:"minecraft:light_blue_terracotta"},{Name:"minecraft:cyan_terracotta"},{Name:"minecraft:green_terracotta"},{Name:"minecraft:pink_terracotta"},{Name:"minecraft:purple_terracotta"},{Name:"minecraft:black_terracotta"},{Name:"minecraft:oak_planks"},{Name:"minecraft:spruce_planks"},{Name:"minecraft:birch_planks"},{Name:"minecraft:dark_oak_planks"},{Name:"minecraft:jungle_planks"},{Name:"minecraft:acacia_planks"},{Name:"minecraft:cherry_planks"},{Name:"minecraft:bookshelf"},{Name:"minecraft:stone"},{Name:"minecraft:stone_bricks"},{Name:"minecraft:bricks"},{Name:"minecraft:smooth_quartz"},{Name:"minecraft:quartz_bricks"},{Name:"minecraft:prismarine"},{Name:"minecraft:prismarine_bricks"},{Name:"minecraft:dark_prismarine"},{Name:"minecraft:sandstone"},{Name:"minecraft:smooth_stone"},{Name:"minecraft:deepslate_tiles"},{Name:"minecraft:polished_andesite"},{Name:"minecraft:calcite"},{Name:"minecraft:oak_leaves",Properties:{persistent:"true"}},{Name:"minecraft:moss_block"},{Name:"minecraft:grass_block"},{Name:"minecraft:hay_block"},{Name:"minecraft:pumpkin"},{Name:"minecraft:melon"},{Name:"minecraft:dirt"},{Name:"minecraft:iron_block"},{Name:"minecraft:gold_block"},{Name:"minecraft:sea_lantern"}]
clear @a[tag=mg.play]
gamemode adventure @a[tag=mg.play]
tag @a[tag=mg.play] add mg.cmx
execute store result score $cmn mg.st if entity @a[tag=mg.play]
scoreboard players set #4 mg.st 4
scoreboard players operation $cmn mg.st /= #4 mg.st
execute if score $cmn mg.st matches ..0 run scoreboard players set $cmn mg.st 1
function mg:cham/pick
execute as @a[tag=mg.play,tag=!mg.cms] run tag @s add mg.cmh
team join mg_red @a[tag=mg.cms]
team join mg_cm @a[tag=mg.cmh]
tp @a[tag=mg.cms] 0.5 89 26600.5
execute as @a[tag=mg.cms] at @s run spawnpoint @s ~ ~ ~
spreadplayers 0 26600 2 18 under 85 false @a[tag=mg.cmh]
execute as @a[tag=mg.cmh] at @s run spawnpoint @s ~ ~ ~
scoreboard players set @a[tag=mg.cmx] mg.cmpts 0
scoreboard players set @a[tag=mg.cmx] mg.cmf 0
