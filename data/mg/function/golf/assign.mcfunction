# @s : numéro de joueur (relie le joueur à sa balle), ligne du tableau
scoreboard players add $gfn mg.st 1
scoreboard players operation @s mg.gfi = $gfn mg.st
scoreboard players set @s mg.gfd 0
scoreboard players display numberformat @s mg.gfd fixed {"text":"0","color":"white"}
