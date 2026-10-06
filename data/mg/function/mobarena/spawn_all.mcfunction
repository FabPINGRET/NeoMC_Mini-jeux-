# Mob Arena — placement des joueurs (@a[tag=mg.play]) selon le thème
execute unless score $mt mg.st matches 6..10 run spreadplayers 0 1800 2 8 under 66 false @a[tag=mg.play]
execute if score $mt mg.st matches 6 run spreadplayers 0 9086 2 5 under 76 false @a[tag=mg.play]
execute if score $mt mg.st matches 7 run spreadplayers 0 9488 2 4 under 74 false @a[tag=mg.play]
execute if score $mt mg.st matches 8 run spreadplayers 0 9880 2 2 under 80 false @a[tag=mg.play]
execute if score $mt mg.st matches 9 run tp @a[tag=mg.play] 0.5 66 10290.5
execute if score $mt mg.st matches 9 run spreadplayers 0 10290 2 4 under 90 false @a[tag=mg.play]
execute if score $mt mg.st matches 10 run spreadplayers 0 10685 2 4 under 76 false @a[tag=mg.play]
