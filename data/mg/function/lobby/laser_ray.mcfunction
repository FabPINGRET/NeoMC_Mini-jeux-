# Un pas du rayon (0,5 bloc) : bloc plein → impact ; joueur → touché ; air → on avance
execute unless block ~ ~ ~ #minecraft:air run return run function mg:lobby/laser_hit
execute positioned ~ ~-0.9 ~ as @a[tag=!mg.lsr,distance=..0.95,limit=1,sort=nearest] run return run function mg:lobby/laser_touch
particle minecraft:dust{color:[1.0,0.1,0.1],scale:0.7} ~ ~ ~ 0 0 0 0 1
scoreboard players remove $lr mg.st 1
execute if score $lr mg.st matches 1.. positioned ^ ^ ^0.5 run function mg:lobby/laser_ray
