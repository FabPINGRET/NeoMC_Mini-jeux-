# Mine abandonnée : remis à zéro (plus personne)
scoreboard players set $trda2 mg.st 0
scoreboard players set $trdc2 mg.st 10
execute if score $trds2 mg.st matches 2.. run scoreboard players set $trdc2 mg.st 60
scoreboard players set $trds2 mg.st 0
scoreboard players set $trdr2 mg.st 0
execute as @e[tag=mg.trdg_mine] at @s run tp @s ~ -400 ~
kill @e[tag=mg.trdg_mine]
execute as @e[tag=mg.trdw2] at @s run tp @s ~ -400 ~
kill @e[tag=mg.trdw2]
bossbar set mg:trdg2 players
