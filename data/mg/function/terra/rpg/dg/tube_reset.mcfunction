# Tube de lave : remis à zéro (plus personne)
scoreboard players set $trda3 mg.st 0
scoreboard players set $trdc3 mg.st 10
execute if score $trds3 mg.st matches 2.. run scoreboard players set $trdc3 mg.st 60
scoreboard players set $trds3 mg.st 0
scoreboard players set $trdr3 mg.st 0
execute as @e[tag=mg.trdg_tube] at @s run tp @s ~ -400 ~
kill @e[tag=mg.trdg_tube]
execute as @e[tag=mg.trdw3] at @s run tp @s ~ -400 ~
kill @e[tag=mg.trdw3]
bossbar set mg:trdg3 players
