# @s = balle : reçoit la vitesse ($gfvx/$gfvy/$gfvz) et se met en mouvement
scoreboard players operation @s mg.gfu = $gfvx mg.st
scoreboard players operation @s mg.gfv = $gfvy mg.st
scoreboard players operation @s mg.gfw = $gfvz mg.st
tag @s add mg.gfmv
execute if score $gfvy mg.st matches 1.. run tag @s remove mg.gfg
execute at @s run particle minecraft:cloud ~ ~0.1 ~ 0.1 0.05 0.1 0.02 4
