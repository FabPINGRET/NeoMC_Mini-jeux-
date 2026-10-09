# Un pas (1 bloc) de la ligne de mire
execute unless block ~ ~ ~ #mg:ray_pass run return 0
execute positioned ~-0.5 ~-0.5 ~-0.5 if entity @e[tag=mg.gtg,tag=!mg.gaim,dx=0,dy=0,dz=0] run return run scoreboard players set $ga mg.st 1
scoreboard players remove $gar mg.st 1
execute if score $gar mg.st matches 1.. positioned ^ ^ ^1 run function mg:gta/aim_ray
