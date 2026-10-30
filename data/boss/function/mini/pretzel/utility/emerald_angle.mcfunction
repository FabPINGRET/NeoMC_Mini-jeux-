execute store result score pretzel_emerald_delta Value run random value -40..40
execute store result score pretzel_emerald_angle Value run data get entity @s Rotation[0] 1
scoreboard players operation pretzel_emerald_angle Value += pretzel_emerald_delta Value
execute store result entity @s Rotation[0] float 1 run scoreboard players get pretzel_emerald_angle Value
