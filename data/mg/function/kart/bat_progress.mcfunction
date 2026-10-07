# Classement en bataille : en lice (100 + ballons) devant les éliminés (ordre d'élimination)
scoreboard players operation @s mg.kpg = @s mg.kbl
scoreboard players add @s mg.kpg 100
execute if entity @s[tag=mg.kout] run scoreboard players operation @s mg.kpg = @s mg.kfp
