# @s : point de départ (solo : n'importe où au bord ; équipes : son camp)
execute as @s[team=mg_red] run spawnpoint @s -20 81 35300
execute as @s[team=mg_blue] run spawnpoint @s 20 81 35300
execute unless entity @s[team=mg_red] unless entity @s[team=mg_blue] run spawnpoint @s 0 81 35280
execute if score $khm mg.st matches 1 if entity @s[team=mg_red] run spreadplayers -20 35300 1 4 under 83 false @s
execute if score $khm mg.st matches 1 if entity @s[team=mg_blue] run spreadplayers 20 35300 1 4 under 83 false @s
execute if score $khm mg.st matches 0 run function mg:koth2/spawn_ring
execute at @s run tp @s ~ ~ ~ facing 0 85 35300
