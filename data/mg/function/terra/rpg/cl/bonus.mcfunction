# @s : bonus de départ de l'ingénieur (une fois par visite)
execute unless score @s mg.trcl matches 4 run return 0
execute if entity @s[tag=mg.trkb] run return 0
tag @s add mg.trkb
scoreboard players add @s mg.tvnet 3
scoreboard players add @s mg.tvtr 3
