# Cœur de l'Arbre-Mère : remis à zéro (plus personne)
scoreboard players set $trda0 mg.st 0
scoreboard players set $trdc0 mg.st 10
execute if score $trds0 mg.st matches 2.. run scoreboard players set $trdc0 mg.st 60
scoreboard players set $trds0 mg.st 0
scoreboard players set $trdr0 mg.st 0
execute as @e[tag=mg.trdg_arbre] at @s run tp @s ~ -400 ~
kill @e[tag=mg.trdg_arbre]
execute as @e[tag=mg.trdw0] at @s run tp @s ~ -400 ~
kill @e[tag=mg.trdw0]
bossbar set mg:trdg0 players
