# Classement en direct (toutes les 4 ticks) : ordre = progression (tours, points de passage) ou ballons en bataille
scoreboard players reset * mg.sbg
execute as @a[tag=mg.play] run scoreboard players operation @s mg.sbg = @s mg.kpg
# En bataille, le nombre de ballons est affiché ; en course, seul l'ordre compte
execute if score $kbat mg.st matches 1 run scoreboard players display numberformat @a[tag=mg.play] mg.sbg styled {"color":"red"}
