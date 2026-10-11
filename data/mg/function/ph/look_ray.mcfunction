# Un pas (0,5 bloc) du regard du chercheur ; un mur l'arrête, le premier objet-cacheur touché est marqué
execute unless block ~ ~ ~ #mg:ray_pass run return 0
execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=minecraft:interaction,tag=mg.phi,dx=0,dy=0,dz=0] run tag @s add mg.phlk
execute positioned ~-0.5 ~-0.5 ~-0.5 if entity @e[type=minecraft:interaction,tag=mg.phi,dx=0,dy=0,dz=0] run return 0
scoreboard players remove $phr mg.st 1
execute if score $phr mg.st matches 1.. positioned ^ ^ ^0.5 run function mg:ph/look_ray
