# @s : point de départ (solo : n'importe où au bord ; équipes : son camp)
execute as @s[team=mg_red] run spawnpoint @s -20 81 35500
execute as @s[team=mg_blue] run spawnpoint @s 20 81 35500
execute unless entity @s[team=mg_red] unless entity @s[team=mg_blue] run spawnpoint @s 0 81 35480
execute if score $khm mg.st matches 1 if entity @s[team=mg_red] run spreadplayers -20 35500 1 4 under 83 false @s
execute if score $khm mg.st matches 1 if entity @s[team=mg_blue] run spreadplayers 20 35500 1 4 under 83 false @s
execute if score $khm mg.st matches 0 run function mg:koth3/spawn_ring
execute at @s run tp @s ~ ~ ~ facing 0 85 35500
