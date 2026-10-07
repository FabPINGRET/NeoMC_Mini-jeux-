# Effets : fumée, étincelles de dérapage (bleues, orange, violettes), flammes de boost, étoile
execute if score @s mg.ksp matches 20.. as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s rotated ~ 0 positioned ^ ^0.3 ^-0.9 run particle minecraft:smoke ~ ~ ~ 0.08 0.04 0.08 0.01 1
execute if score @s mg.kdr matches 20..44 as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s rotated ~ 0 positioned ^0.5 ^0.15 ^-0.7 run particle minecraft:soul_fire_flame ~ ~ ~ 0.04 0.04 0.04 0.02 2
execute if score @s mg.kdr matches 20..44 as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s rotated ~ 0 positioned ^-0.5 ^0.15 ^-0.7 run particle minecraft:soul_fire_flame ~ ~ ~ 0.04 0.04 0.04 0.02 2
execute if score @s mg.kdr matches 45..79 as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s rotated ~ 0 positioned ^0.5 ^0.15 ^-0.7 run particle minecraft:flame ~ ~ ~ 0.04 0.04 0.04 0.02 3
execute if score @s mg.kdr matches 45..79 as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s rotated ~ 0 positioned ^-0.5 ^0.15 ^-0.7 run particle minecraft:flame ~ ~ ~ 0.04 0.04 0.04 0.02 3
execute if score @s mg.kdr matches 80.. as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s rotated ~ 0 positioned ^0.5 ^0.15 ^-0.7 run particle minecraft:dust{color:[0.75f,0.25f,1.0f],scale:1.2f} ~ ~ ~ 0.05 0.05 0.05 0 4
execute if score @s mg.kdr matches 80.. as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s rotated ~ 0 positioned ^-0.5 ^0.15 ^-0.7 run particle minecraft:dust{color:[0.75f,0.25f,1.0f],scale:1.2f} ~ ~ ~ 0.05 0.05 0.05 0 4
execute if score @s mg.kbo matches 1.. as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s rotated ~ 0 positioned ^ ^0.3 ^-1.0 run particle minecraft:flame ~ ~ ~ 0.12 0.08 0.12 0.03 4
execute if score @s mg.kst matches 1.. as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s run particle minecraft:end_rod ~ ~0.7 ~ 0.5 0.4 0.5 0.05 4
