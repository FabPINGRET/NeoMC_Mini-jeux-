# Pic du Nid : remis à zéro (plus personne)
scoreboard players set $trda1 mg.st 0
scoreboard players set $trdc1 mg.st 10
execute if score $trds1 mg.st matches 2.. run scoreboard players set $trdc1 mg.st 60
scoreboard players set $trds1 mg.st 0
scoreboard players set $trdr1 mg.st 0
execute as @e[tag=mg.trdg_pic] at @s run tp @s ~ -400 ~
kill @e[tag=mg.trdg_pic]
execute as @e[tag=mg.trdw1] at @s run tp @s ~ -400 ~
kill @e[tag=mg.trdw1]
bossbar set mg:trdg1 players
