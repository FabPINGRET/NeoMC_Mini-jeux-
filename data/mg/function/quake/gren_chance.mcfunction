# Quakecraft — après un kill (@s = tueur) : 1 chance sur 5 de gagner une grenade (une seule à la fois)
execute store result score $gc mg.st run clear @s minecraft:snowball 0
execute if score $gc mg.st matches 1.. run return 0
execute store result score $gr mg.st run random value 1..100
execute if score $gr mg.st matches 1..20 run function mg:quake/gren_give
