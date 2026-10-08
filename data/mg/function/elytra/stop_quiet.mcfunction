# Fin du parcours sans téléportation (@s) : objets et effets retirés
tag @s remove mg.ely
scoreboard players set @s mg.est 0
clear @s minecraft:elytra[minecraft:custom_data~{mg_ely:1b}]
clear @s minecraft:firework_rocket[minecraft:custom_data~{mg_ely:1b}]
effect clear @s minecraft:resistance
