execute if block ~ 38 ~ minecraft:redstone_wire[power=0] if score @s Value matches 0 run tp @s ~ ~ ~0.2 90 ~
execute if block ~ 38 ~ minecraft:redstone_wire[power=0] if score @s Value matches 1 run tp @s ~ ~ ~-0.2 105 ~
execute if block ~ 38 ~ minecraft:redstone_wire[power=0] if score @s Value matches 2 run tp @s ~ ~ ~-0.2 90 ~
execute if block ~ 38 ~ minecraft:redstone_wire[power=0] if score @s Value matches 3 run tp @s ~ ~ ~0.2 75 ~
execute if block ~ 38 ~ minecraft:redstone_wire[power=0] run scoreboard players add @s Value 1
execute if block ~ 38 ~ minecraft:redstone_wire[power=0] if score @s Value matches 4 run scoreboard players set @s Value 0
