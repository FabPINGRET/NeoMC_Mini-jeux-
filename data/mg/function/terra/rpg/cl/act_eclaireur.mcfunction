# @s (éclaireur) : sprint du chasseur
playsound minecraft:entity.breeze.wind_burst player @a ~ ~ ~ 0.8 1.4
particle minecraft:gust ~ ~0.5 ~ 0.3 0.1 0.3 0 3
execute if score $rk mg.st matches 1 run effect give @s minecraft:speed 6 2
execute if score $rk mg.st matches 1 run effect give @s minecraft:jump_boost 6 1
execute if score $rk mg.st matches 2.. run effect give @s minecraft:speed 9 2
execute if score $rk mg.st matches 2.. run effect give @s minecraft:jump_boost 9 1
execute if score $rk mg.st matches 3.. run effect give @s minecraft:invisibility 4 0
execute if score $rk mg.st matches 3.. as @e[tag=mg.tvhos,distance=..24] run function mg:terra/rpg/cl/lose
