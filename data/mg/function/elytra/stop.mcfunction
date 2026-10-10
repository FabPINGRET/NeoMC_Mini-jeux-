# Fin du parcours (@s) : retour à son socle, protégé à l'atterrissage, baguette rendue
function mg:elytra/stop_quiet
execute if score @s mg.ecr matches 1 run tp @s 16.5 64 -10.5 facing 16.5 64 -16.5
execute if score @s mg.ecr matches 2 run tp @s 32.5 64 -16.5 facing 32.5 64 -22.5
effect give @s minecraft:resistance 3 4 true
function mg:core/heal
execute if score @s mg.ehw matches 1.. run function mg:lobby/give_wand
scoreboard players set @s mg.ehw 0
