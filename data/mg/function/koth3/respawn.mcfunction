# @s : réapparition (kit rendu, 2 s de protection)
scoreboard players set @s mg.deaths 0
function mg:koth3/spawn
function mg:koth3/kit
effect give @s minecraft:resistance 2 4 true
effect give @s minecraft:instant_health 1 4 true
