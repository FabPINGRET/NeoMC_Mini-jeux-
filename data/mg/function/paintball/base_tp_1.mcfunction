# Paintball (carte 1) — renvoie un joueur (@s) dans sa base
execute if entity @s[team=mg_red] run spreadplayers 0 12283 1 2 under 90 false @s
execute if entity @s[team=mg_blue] run spreadplayers 0 12317 1 2 under 90 false @s
execute if entity @s[team=mg_red] at @s run tp @s ~ ~ ~ 0 0
execute if entity @s[team=mg_blue] at @s run tp @s ~ ~ ~ 180 0
