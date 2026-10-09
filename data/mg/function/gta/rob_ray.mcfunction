# Un pas (1 bloc) vers le passant visé
execute unless block ~ ~ ~ #mg:ray_pass run return 0
execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=minecraft:villager,tag=mg.gped,tag=!mg.grobbed,dx=0,dy=0,dz=0,limit=1] run return run tag @s add mg.grt
scoreboard players remove $gar mg.st 1
execute if score $gar mg.st matches 1.. positioned ^ ^ ^1 run function mg:gta/rob_ray
