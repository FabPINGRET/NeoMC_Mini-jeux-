# @s : bombe en vol (âge mg.bc4, type mg.bty, lanceur mg.bid)
scoreboard players add @s mg.bc4 1
execute if score @s mg.bc4 matches 300.. run return run kill @s
execute if entity @s[y=-64,dy=103] run return run kill @s
execute if score @s mg.bty matches 3 if score @s mg.bc4 matches 14 run return run function mg:bomber/split
particle minecraft:smoke ~ ~0.5 ~ 0.1 0.1 0.1 0 2
execute if score @s mg.bty matches 5 run particle minecraft:end_rod ~ ~0.5 ~ 0.2 0.2 0.2 0 2 force
execute unless block ~ ~-0.2 ~ #mg:bomb_pass run return run function mg:bomber/impact
execute unless block ~0.6 ~0.4 ~ #mg:bomb_pass run return run function mg:bomber/impact
execute unless block ~-0.6 ~0.4 ~ #mg:bomb_pass run return run function mg:bomber/impact
execute unless block ~ ~0.4 ~0.6 #mg:bomb_pass run return run function mg:bomber/impact
execute unless block ~ ~0.4 ~-0.6 #mg:bomb_pass run return run function mg:bomber/impact
