# 🎄 Noël : particules qui tombent, densité selon $thi (1..8) ; appelé par noel/fx
execute if score $thi mg.st matches 1..2 run particle minecraft:snowflake ~ ~6 ~ 10 4 10 0 8 normal @s
execute if score $thi mg.st matches 3..4 run particle minecraft:snowflake ~ ~6 ~ 10 4 10 0 15 normal @s
execute if score $thi mg.st matches 5..6 run particle minecraft:snowflake ~ ~6 ~ 10 4 10 0 23 normal @s
execute if score $thi mg.st matches 7..8 run particle minecraft:snowflake ~ ~6 ~ 10 4 10 0 30 normal @s
execute if score $thi mg.st matches 1..2 run particle minecraft:white_ash ~ ~3 ~ 8 3 8 0 5 normal @s
execute if score $thi mg.st matches 3..4 run particle minecraft:white_ash ~ ~3 ~ 8 3 8 0 10 normal @s
execute if score $thi mg.st matches 5..6 run particle minecraft:white_ash ~ ~3 ~ 8 3 8 0 15 normal @s
execute if score $thi mg.st matches 7..8 run particle minecraft:white_ash ~ ~3 ~ 8 3 8 0 20 normal @s
