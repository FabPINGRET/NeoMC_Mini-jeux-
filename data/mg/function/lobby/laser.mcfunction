# Pistolet laser (@s = joueur, position = joueur) : rayon inoffensif de 30 blocs
scoreboard players reset @s mg.qs
tag @s add mg.lsr
scoreboard players set $lr mg.st 60
execute anchored eyes positioned ^ ^ ^0.5 run function mg:lobby/laser_ray
tag @s remove mg.lsr
playsound minecraft:entity.firework_rocket.shoot master @a ~ ~ ~ 1 1.8
