# @s (entraînement, seul) : mort ou chute → retour au bunker, kit rendu
scoreboard players set @s mg.deaths 0
spreadplayers 11 23189 4 18 under 84 false @s
execute at @s run spawnpoint @s ~ ~ ~
function mg:inf/kit
effect give @s minecraft:resistance 2 4 true
effect give @s minecraft:instant_health 1 4 true
tellraw @s {"text":"🧪 Entraînement : retour au bunker.","color":"yellow"}
