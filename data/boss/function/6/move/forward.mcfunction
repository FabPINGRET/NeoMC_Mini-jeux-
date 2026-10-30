execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] unless entity @s[tag=x5] run setblock -10462 42 -98 redstone_block
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] unless entity @s[tag=x1] run setblock -10462 42 -98 redstone_block
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] unless entity @s[tag=z5] run setblock -10462 42 -98 redstone_block
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] unless entity @s[tag=z1] run setblock -10462 42 -98 redstone_block


execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if entity @s[tag=x4] run tag @s add x5
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if entity @s[tag=x3] run tag @s add x4
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if entity @s[tag=x2] run tag @s add x3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if entity @s[tag=x1] run tag @s add x2

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] run tag @s remove x1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if entity @s[tag=x3] run tag @s remove x2
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if entity @s[tag=x4] run tag @s remove x3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=east] if entity @s[tag=x5] run tag @s remove x4

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if entity @s[tag=x2] run tag @s add x1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if entity @s[tag=x3] run tag @s add x2
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if entity @s[tag=x4] run tag @s add x3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if entity @s[tag=x5] run tag @s add x4

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] run tag @s remove x5
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if entity @s[tag=x3] run tag @s remove x4
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if entity @s[tag=x2] run tag @s remove x3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=west] if entity @s[tag=x1] run tag @s remove x2

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if entity @s[tag=z4] run tag @s add z5
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if entity @s[tag=z3] run tag @s add z4
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if entity @s[tag=z2] run tag @s add z3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if entity @s[tag=z1] run tag @s add z2

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] run tag @s remove z1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if entity @s[tag=z3] run tag @s remove z2
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if entity @s[tag=z4] run tag @s remove z3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=south] if entity @s[tag=z5] run tag @s remove z4

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if entity @s[tag=z2] run tag @s add z1
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if entity @s[tag=z3] run tag @s add z2
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if entity @s[tag=z4] run tag @s add z3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if entity @s[tag=z5] run tag @s add z4

execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] run tag @s remove z5
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if entity @s[tag=z3] run tag @s remove z4
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if entity @s[tag=z2] run tag @s remove z3
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @s[tag=north] if entity @s[tag=z1] run tag @s remove z2

fill -10478 42 -70 -10478 42 -70 red_wool replace minecraft:lime_wool
fill -10478 42 -70 -10478 42 -70 lime_wool replace minecraft:blue_wool
fill -10478 42 -70 -10478 42 -70 blue_wool replace minecraft:black_wool
