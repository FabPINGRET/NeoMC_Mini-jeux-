# Un pas du rayon (0,5 bloc) : bloc solide = impact ; joueur = touché ; sinon on avance (traverse air, herbes, lumières)
execute unless block ~ ~ ~ #mg:kart_pass run return run function mg:lobby/laser_hit
execute positioned ~ ~-0.9 ~ as @a[tag=!mg.lsr,distance=..0.95,limit=1,sort=nearest] run return run function mg:lobby/laser_touch
particle minecraft:dust{color:[1.0,0.12,0.12],scale:1.2} ~ ~ ~ 0 0 0 0 1 force
particle minecraft:dust{color:[1.0,0.9,0.9],scale:0.5} ~ ~ ~ 0 0 0 0 1 force
execute if score $lr mg.st matches 46.. run particle minecraft:electric_spark ~ ~ ~ 0.06 0.06 0.06 0.05 1
scoreboard players remove $lr mg.st 1
execute if score $lr mg.st matches 1.. positioned ^ ^ ^0.5 run function mg:lobby/laser_ray
