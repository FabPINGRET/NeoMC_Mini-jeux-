# Paintball — renvoie un joueur (@s) dans sa base
execute if score $pbm mg.st matches 1 run return run function mg:paintball/base_tp_1
execute if score $pbm mg.st matches 2 run return run function mg:paintball/base_tp_2
execute if entity @s[team=mg_red] run spreadplayers 0 8773 2 3 under 90 false @s
execute if entity @s[team=mg_blue] run spreadplayers 0 8827 2 3 under 90 false @s
execute if entity @s[team=mg_red] at @s run tp @s ~ ~ ~ 0 0
execute if entity @s[team=mg_blue] at @s run tp @s ~ ~ ~ 180 0
