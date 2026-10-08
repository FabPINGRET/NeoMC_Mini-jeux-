# Quakecraft — placement aléatoire selon la carte (@s)
execute if score $ar mg.st matches 1.. run return run function mg:var/spread_one
execute if score $qm mg.st matches 0 run spreadplayers 0 7300 5 13 under 90 false @s
execute if score $qm mg.st matches 1 run spreadplayers 0 7600 8 28 under 90 false @s
execute if score $qm mg.st matches 2 run spreadplayers 0 7900 8 28 under 90 false @s
execute if score $qm mg.st matches 3 run spreadplayers 0 8200 5 13 under 90 false @s
execute if score $qm mg.st matches 4 run spreadplayers 0 8500 3 7 under 90 false @s
execute if score $qm mg.st matches 5 run spreadplayers 0 11100 4 18 under 84 false @s
execute if score $qm mg.st matches 6 run spreadplayers 0 11300 4 18 under 84 false @s
execute if score $qm mg.st matches 7 run spreadplayers 0 11500 4 15 under 84 false @s
