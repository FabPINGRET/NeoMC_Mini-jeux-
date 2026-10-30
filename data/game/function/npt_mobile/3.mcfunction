execute as @n[tag=npt_mobile,tag=3,distance=0..] at @s run tp @s ~ ~ ~ ~45 0
execute as @n[tag=npt_mobile,tag=3,distance=0..] at @s run tp @n[tag=npt_mobile_planet,tag=3,distance=0..] ^ ^ ^4
scoreboard players add npt_mobile_3 Value 1
execute if score npt_mobile_3 Value matches 8 run scoreboard players set npt_mobile_3 Value 0

execute if score npt_mobile_1 Value matches 5 if score npt_mobile_2 Value matches 2 if score npt_mobile_3 Value matches 7 run setblock -199 46 -1201 minecraft:redstone_block
