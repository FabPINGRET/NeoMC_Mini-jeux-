# Flèche enchantée en vol (@s = la flèche, position = flèche)
scoreboard players add @s mg.ag 1
execute if score @s mg.ak matches 1 run particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.01 2
execute if score @s mg.ak matches 2 run particle minecraft:end_rod ~ ~ ~ 0 0 0 0.02 1
execute if score @s mg.ak matches 3 run particle minecraft:glow ~ ~ ~ 0.05 0.05 0.05 0.01 2
execute if entity @s[tag=mg.ex] run function mg:oitc/ex_check
