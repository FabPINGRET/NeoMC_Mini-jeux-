execute in mg:floaty store result score sphere_cave_time Value run time query minecraft:day

execute if score sphere_cave_time Value matches 6000..18000 as @n[tag=sphere_cave_pivot,distance=0..] at @s run tp @s ~ ~ ~ 90 ~
execute unless score sphere_cave_time Value matches 6000..18000 as @n[tag=sphere_cave_pivot,distance=0..] at @s run tp @s ~ ~ ~ -90 ~

scoreboard players operation sphere_cave_neck_step_1 Value = sphere_cave_time Value
scoreboard players operation sphere_cave_neck_step_1 Value -= 6000 Value

scoreboard players operation sphere_cave_neck_step_2 Value = sphere_cave_neck_step_1 Value
scoreboard players operation sphere_cave_neck_step_2 Value /= 67 Value

scoreboard players operation sphere_cave_neck_angle Value = sphere_cave_neck_step_2 Value
scoreboard players operation sphere_cave_neck_angle Value -= 90 Value

scoreboard players operation sphere_cave_final_neck_angle Value = sphere_cave_neck_angle Value

# MORNING CHECKS

execute if score sphere_cave_neck_angle Value matches ..-90 run scoreboard players operation sphere_cave_final_neck_angle Value *= -1 Value
execute if score sphere_cave_neck_angle Value matches ..-90 run scoreboard players operation sphere_cave_final_neck_angle Value -= 180 Value

execute if score sphere_cave_neck_angle Value matches 90.. run scoreboard players operation sphere_cave_final_neck_angle Value *= -1 Value
execute if score sphere_cave_neck_angle Value matches 90.. run scoreboard players operation sphere_cave_final_neck_angle Value += 180 Value


execute store result entity @n[tag=sphere_cave_pivot,distance=0..] Rotation[1] float 1 run scoreboard players get sphere_cave_final_neck_angle Value

execute as @n[tag=sphere_cave_pivot,distance=0..] at @s run tp @n[tag=sphere_cave_sun,distance=0..] ^ ^ ^3
execute as @n[tag=sphere_cave_pivot,distance=0..] at @s run tp @n[tag=sphere_cave_moon,distance=0..] ^ ^ ^-3

execute as @n[tag=sphere_cave_moon,distance=0..] at @s run particle minecraft:end_rod ~ ~1 ~ 0.2 0.2 0.2 0 1
execute as @n[tag=sphere_cave_sun,distance=0..] at @s run particle minecraft:flame ~ ~1 ~ 0.2 0.2 0.2 0 1
