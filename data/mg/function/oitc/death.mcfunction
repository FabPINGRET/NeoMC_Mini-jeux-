# Mort ou chute (@s = joueur) : retour dans l'arène avec le kit de départ (respawn illimité)
scoreboard players set @s mg.deaths 0
tellraw @a [{"selector":"@s","color":"red"},{"text":" est mort !","color":"gray"}]
execute at @s run particle minecraft:poof ~ ~1 ~ 0.3 0.5 0.3 0.05 20
execute if score $ar mg.st matches 1.. run function mg:var/spread_one
execute if score $ar mg.st matches 0 if score $om mg.st matches 0 run spreadplayers 0 5800 5 10 under 90 false @s
execute if score $ar mg.st matches 0 if score $om mg.st matches 1 run spreadplayers 0 11700 5 17 under 84 false @s
execute if score $ar mg.st matches 0 if score $om mg.st matches 2 run spreadplayers 0 12000 8 30 under 86 false @s
function mg:oitc/kit
scoreboard players set @s mg.cd 0
effect clear @s
effect give @s minecraft:resistance 3 4 true
effect give @s minecraft:saturation infinite 0 true
