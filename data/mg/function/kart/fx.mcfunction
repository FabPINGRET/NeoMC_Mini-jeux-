# Effets : fumée, étincelles de dérapage, flammes de boost, étoile
execute if score @s mg.ksp matches 20.. on vehicle at @s rotated ~ 0 positioned ^ ^0.4 ^-1.1 run particle minecraft:smoke ~ ~ ~ 0.1 0.05 0.1 0.01 1
execute if score @s mg.kdr matches 25..54 on vehicle at @s rotated ~ 0 positioned ^0.7 ^0.2 ^-0.9 run particle minecraft:soul_fire_flame ~ ~ ~ 0.05 0.05 0.05 0.02 2
execute if score @s mg.kdr matches 25..54 on vehicle at @s rotated ~ 0 positioned ^-0.7 ^0.2 ^-0.9 run particle minecraft:soul_fire_flame ~ ~ ~ 0.05 0.05 0.05 0.02 2
execute if score @s mg.kdr matches 55.. on vehicle at @s rotated ~ 0 positioned ^0.7 ^0.2 ^-0.9 run particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.02 3
execute if score @s mg.kdr matches 55.. on vehicle at @s rotated ~ 0 positioned ^-0.7 ^0.2 ^-0.9 run particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.02 3
execute if score @s mg.kbo matches 1.. on vehicle at @s rotated ~ 0 positioned ^ ^0.4 ^-1.2 run particle minecraft:flame ~ ~ ~ 0.15 0.1 0.15 0.03 4
execute if score @s mg.kst matches 1.. on vehicle at @s run particle minecraft:end_rod ~ ~0.8 ~ 0.6 0.5 0.6 0.05 4
