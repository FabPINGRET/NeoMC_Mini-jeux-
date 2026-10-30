execute as @n[type=minecraft:armor_stand,tag=mlc_tracker,distance=0..] at @s facing entity @n[tag=mlc_tag,distance=0..] eyes run tp @s ^ ^ ^ ~ ~
execute as @n[type=minecraft:armor_stand,tag=mlc_main,distance=0..] at @n[tag=mlc_tracker,distance=0..] run tp @s ~ ~ ~
execute as @e[tag=mlc_tag,distance=0..] at @s run tp @e[type=minecraft:armor_stand,tag=mlc_tracker,distance=0..] ^-1.5 ^1.5 ^2.5
execute as @n[type=minecraft:armor_stand,tag=mlc_main,distance=0..] at @s run tp @s ~ ~ ~ ~2 ~
execute at @e[tag=mlc_main,distance=0..] run particle minecraft:soul_fire_flame ~ ~1 ~ 0.2 0.2 0.2 0.01 1 force

execute as @n[tag=mlc_tag,distance=0..] at @s unless block ~ ~-0.01 ~ air unless block ~ ~-0.01 ~ water unless block ~ ~-0.01 ~ lava unless block ~ ~-0.01 ~ ladder unless block ~ ~-0.01 ~ honey_block unless block ~ ~-0.01 ~ resin_bricks unless block ~ ~-0.01 ~ resin_brick_slab unless block ~ ~-0.01 ~ resin_brick_stairs unless block ~ ~-0.01 ~ resin_brick_wall run function main_quest:mlc/step_lose
