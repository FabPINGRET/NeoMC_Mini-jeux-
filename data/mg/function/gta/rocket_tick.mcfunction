# @s : roquette en vol (âge mg.gpc, tireur mg.bid) : 3 pas de 0,7 bloc par tick
scoreboard players add @s mg.gpc 1
execute if score @s mg.gpc matches 60.. run return run function mg:gta/rocket_boom
execute at @s run function mg:gta/rocket_step
execute if entity @s at @s run function mg:gta/rocket_step
execute if entity @s at @s run function mg:gta/rocket_step
particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.02 3
particle minecraft:large_smoke ~ ~ ~ 0.1 0.1 0.1 0.01 2
