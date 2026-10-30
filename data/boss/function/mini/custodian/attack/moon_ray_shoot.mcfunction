execute as @e[tag=custodian_moon_ray_1,distance=0..] store result entity @s Rotation[1] double 0.01 run scoreboard players get custodian_midnight_moon_angle_1 Value
execute as @e[tag=custodian_moon_ray_2,distance=0..] store result entity @s Rotation[1] double 0.01 run scoreboard players get custodian_midnight_moon_angle_2 Value
execute as @e[tag=custodian_moon_ray_3,distance=0..] store result entity @s Rotation[1] double 0.01 run scoreboard players get custodian_midnight_moon_angle_3 Value

execute as @e[tag=custodian_moon_ray_1,distance=0..] at @s facing ^ ^ ^1 run function boss:mini/custodian/attack/moon_ray_ray
execute as @e[tag=custodian_moon_ray_2,distance=0..] at @s facing ^ ^ ^1 run function boss:mini/custodian/attack/moon_ray_ray
execute as @e[tag=custodian_moon_ray_3,distance=0..] at @s facing ^ ^ ^1 run function boss:mini/custodian/attack/moon_ray_ray



