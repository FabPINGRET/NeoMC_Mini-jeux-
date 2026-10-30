# Flip X
execute store result score #tmp_x Value run data get entity @s Motion[0] 1000
scoreboard players operation #tmp_x Value *= -1 Value
execute store result entity @s Motion[0] double 0.001 run scoreboard players get #tmp_x Value

# Flip Y
execute store result score #tmp_y Value run data get entity @s Motion[1] 1000
scoreboard players operation #tmp_y Value *= -1 Value
execute store result entity @s Motion[1] double 0.001 run scoreboard players get #tmp_y Value

# Flip Z
execute store result score #tmp_z Value run data get entity @s Motion[2] 1000
scoreboard players operation #tmp_z Value *= -1 Value
execute store result entity @s Motion[2] double 0.001 run scoreboard players get #tmp_z Value

scoreboard players set @s HBDeflectCD 12
