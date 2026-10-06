# Mob Arena — ressuscite @s (joueur éliminé) au début de la vague suivante
tag @s remove mg.out
tag @s add mg.play
scoreboard players set @s mg.deaths 0
gamemode adventure @s
effect clear @s
clear @s
function mg:mobarena/spawn_one
function mg:mobarena/kit
execute if score $mt mg.st matches 8 run effect give @s minecraft:water_breathing infinite 0 true
effect give @s minecraft:instant_health 1 3 true
effect give @s minecraft:resistance 5 4 true
title @s title [{"text":"RESSUSCITÉ !","color":"green","bold":true}]
title @s subtitle [{"text":"Retourne au combat !","color":"gray"}]
tellraw @a [{"selector":"@s","color":"green"},{"text":" revient dans l'arène !","color":"gray"}]
execute at @s run playsound minecraft:item.totem.use master @a ~ ~ ~ 0.8 1.2
