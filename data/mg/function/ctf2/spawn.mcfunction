# @s : dans sa base, derrière son drapeau
execute if entity @s[team=mg_red] run spawnpoint @s -39 81 41400
execute if entity @s[team=mg_blue] run spawnpoint @s 39 81 41400
execute if entity @s[team=mg_red] run spreadplayers -39 41400 1 3 under 83 false @s
execute if entity @s[team=mg_blue] run spreadplayers 39 41400 1 3 under 83 false @s
execute at @s run tp @s ~ ~ ~ facing 0 81 41400
