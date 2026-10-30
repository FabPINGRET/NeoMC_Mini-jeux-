function boss:6/move/frame/look_left

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] run tag @s add turning_north
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] run tag @s add turning_west
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] run tag @s add turning_south
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] run tag @s add turning_east

execute as @n[tag=boss_sh_loc,distance=0..] at @s run tag @s remove east
execute as @n[tag=boss_sh_loc,distance=0..] at @s run tag @s remove west
execute as @n[tag=boss_sh_loc,distance=0..] at @s run tag @s remove south
execute as @n[tag=boss_sh_loc,distance=0..] at @s run tag @s remove north

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=turning_east] run tag @s add east
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=turning_west] run tag @s add west
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=turning_south] run tag @s add south
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=turning_north] run tag @s add north

execute as @n[tag=boss_sh_loc,distance=0..] at @s run tag @s remove turning_east
execute as @n[tag=boss_sh_loc,distance=0..] at @s run tag @s remove turning_west
execute as @n[tag=boss_sh_loc,distance=0..] at @s run tag @s remove turning_south
execute as @n[tag=boss_sh_loc,distance=0..] at @s run tag @s remove turning_north

execute as @n[tag=boss_sh_loc,distance=0..] at @s run tp @s ~ ~ ~ ~-90 ~

schedule function floaty:sched/boss/6/move/frame/straight 15t replace

fill -10478 42 -71 -10478 42 -71 red_wool replace minecraft:lime_wool
fill -10478 42 -71 -10478 42 -71 lime_wool replace minecraft:blue_wool
fill -10478 42 -71 -10478 42 -71 blue_wool replace minecraft:black_wool
