# Paintball — place chaque équipe dans sa base
execute if score $pbm mg.st matches 1 run return run function mg:paintball/base_tp_all_1
execute if score $pbm mg.st matches 2 run return run function mg:paintball/base_tp_all_2
spreadplayers 0 8773 2 3 under 90 false @a[team=mg_red,tag=mg.play]
spreadplayers 0 8827 2 3 under 90 false @a[team=mg_blue,tag=mg.play]
execute as @a[team=mg_red,tag=mg.play] at @s run tp @s ~ ~ ~ 0 0
execute as @a[team=mg_blue,tag=mg.play] at @s run tp @s ~ ~ ~ 180 0
