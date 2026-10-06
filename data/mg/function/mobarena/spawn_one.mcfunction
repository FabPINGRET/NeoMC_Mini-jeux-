# Mob Arena — placement des joueurs (@s) selon le thème
execute unless score $mt mg.st matches 6..10 run spawnpoint @s 0 80 1800
execute unless score $mt mg.st matches 6..10 run spreadplayers 0 1800 2 8 under 66 false @s
execute if score $mt mg.st matches 6 run spawnpoint @s 0 65 9086
execute if score $mt mg.st matches 6 run spreadplayers 0 9086 2 5 under 76 false @s
execute if score $mt mg.st matches 7 run spawnpoint @s 0 65 9488
execute if score $mt mg.st matches 7 run spreadplayers 0 9488 2 4 under 74 false @s
execute if score $mt mg.st matches 8 run spawnpoint @s 0 68 9880
execute if score $mt mg.st matches 8 run spreadplayers 0 9880 2 2 under 80 false @s
execute if score $mt mg.st matches 9 run spawnpoint @s 0 66 10290
execute if score $mt mg.st matches 9 run tp @s 0.5 66 10290.5
execute if score $mt mg.st matches 9 run spreadplayers 0 10290 2 4 under 90 false @s
execute if score $mt mg.st matches 10 run spawnpoint @s 0 65 10685
execute if score $mt mg.st matches 10 run spreadplayers 0 10685 2 4 under 76 false @s
