# Un pas (0,25 bloc) du tir
scoreboard players remove $cmr mg.st 1
execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=minecraft:interaction,tag=mg.cmi,dx=0,dy=0,dz=0,limit=1] positioned ~0.5 ~0.5 ~0.5 run return run function mg:cham/shot_hit
execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=minecraft:interaction,tag=mg.cmdi,dx=0,dy=0,dz=0,limit=1] at @s run return run function mg:cham/decoy_pop
execute unless block ~ ~ ~ #mg:ray_pass run return run function mg:cham/shot_miss
particle minecraft:dust{color:[1.0,0.3,0.6],scale:0.6} ~ ~ ~ 0 0 0 0 1
execute if score $cmr mg.st matches 1.. positioned ^ ^ ^0.25 run function mg:cham/shot_ray
