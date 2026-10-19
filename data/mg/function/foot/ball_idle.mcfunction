# 20 s (10 passes) sans joueur à moins de 6 blocs de la balle : retour au centre
scoreboard players add $fti mg.ft 1
execute at @e[type=minecraft:sulfur_cube,tag=mg.ball,limit=1] if entity @a[distance=..6] run scoreboard players set $fti mg.ft 0
execute if score $fti mg.ft matches 10.. run function mg:foot/ball_home
