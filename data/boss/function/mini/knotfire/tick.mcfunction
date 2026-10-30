execute as @n[tag=knotfire_green_fireball,distance=0..] at @s run particle minecraft:copper_fire_flame ~ ~ ~ 0.2 0.2 0.2 0.02 5
execute as @n[tag=knotfire_green_fireball,distance=0..] at @s run particle minecraft:copper_fire_flame ~ ~ ~ 0.4 0.4 0.4 0.04 5

execute as @n[tag=knotfire_green_fireball,distance=0..] at @s run particle minecraft:egg_crack ~ ~ ~ 0 0 0 0 1

execute as @n[tag=knotfire_green_fireball,distance=0..] at @s run tp @s ^ ^ ^0.8
execute as @n[tag=knotfire_green_fireball,distance=0..] at @s run playsound minecraft:entity.breeze.slide hostile @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute as @n[tag=knotfire_green_fireball,distance=0..] at @s unless block ~ ~ ~ air run function boss:mini/knotfire/attack/green_fireball_explosion

execute as @e[tag=knotfire_boss,distance=0..] at @s run particle minecraft:egg_crack ~ ~1.2 ~ 0.3 1 0.3 0 2
execute as @e[tag=knotfire_boss,distance=0..] at @s run particle minecraft:copper_fire_flame ~ ~2 ~ 0.7 1.5 0.7 0 2

execute as @e[tag=knotfire_rain_loc,distance=0..] at @s run tp @s ~ ~ ~ ~23 ~
