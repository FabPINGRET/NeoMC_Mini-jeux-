# Un pas (0,5 bloc) de la balle du policier
execute unless block ~ ~ ~ #mg:ray_pass run return run particle minecraft:smoke ~ ~ ~ 0.05 0.05 0.05 0 2
execute positioned ~-0.5 ~-0.5 ~-0.5 as @a[tag=mg.gtw,gamemode=!spectator,dx=0,dy=0,dz=0,limit=1] run return run function mg:gta/cop_hit
particle minecraft:crit ~ ~ ~ 0 0 0 0 1
scoreboard players remove $gcr mg.st 1
execute if score $gcr mg.st matches 1.. positioned ^ ^ ^0.5 run function mg:gta/cop_ray
