# Fin du parcours (@s) : retour au socle, protégé à l'atterrissage
function mg:elytra/stop_quiet
tp @s 16.5 64 -10.5 facing 16.5 64 -15
effect give @s minecraft:resistance 3 4 true
execute if score @s mg.ehw matches 1.. run function mg:lobby/give_wand
scoreboard players set @s mg.ehw 0
