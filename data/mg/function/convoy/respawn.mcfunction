# @s : réapparition loin du convoi (escorte derrière, défense devant)
scoreboard players set @s mg.deaths 0
tag @s remove mg.cvw
scoreboard players reset @s mg.cvrt
gamemode adventure @s
function mg:convoy/spawn
function mg:convoy/kit
effect give @s minecraft:resistance 3 4 true
effect give @s minecraft:instant_health 1 4 true
