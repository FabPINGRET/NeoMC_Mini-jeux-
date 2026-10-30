execute store result score wahrog_forking_x_rotation Value run data get entity @s Rotation[0] 1
execute store result score wahrog_forking_y_rotation Value run data get entity @s Rotation[1] 1
execute store result score wahrog_forking_x_delta Value run random value -20..20
execute store result score wahrog_forking_y_delta Value run random value -20..20
scoreboard players operation wahrog_forking_x_rotation Value += wahrog_forking_x_delta Value
scoreboard players operation wahrog_forking_y_rotation Value += wahrog_forking_y_delta Value
execute store result entity @s Rotation[0] double 1 run scoreboard players get wahrog_forking_x_rotation Value
execute store result entity @s Rotation[1] double 1 run scoreboard players get wahrog_forking_y_rotation Value
