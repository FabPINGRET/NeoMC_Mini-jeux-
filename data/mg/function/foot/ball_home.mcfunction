# La balle revient au centre, immobile (appelé par un but, par la sortie du terrain, par l'inactivité)
execute as @e[type=minecraft:sulfur_cube,tag=mg.ball] run tp @s 2.5 48 -30.5
data modify entity @e[type=minecraft:sulfur_cube,tag=mg.ball,limit=1] Motion set value [0.0d,0.0d,0.0d]
scoreboard players set $fti mg.ft 0
