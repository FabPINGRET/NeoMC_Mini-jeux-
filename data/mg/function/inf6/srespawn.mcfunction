# @s (entraînement, seul) : mort ou chute → retour au bunker, kit rendu
scoreboard players set @s mg.deaths 0
execute as @s run tp @s @e[type=minecraft:marker,tag=mg.zrc,sort=random,limit=1]
execute at @s run spawnpoint @s ~ ~ ~
function mg:inf6/kit
effect give @s minecraft:resistance 2 4 true
effect give @s minecraft:instant_health 1 4 true
tellraw @s {"text":"🧪 Entraînement : retour au bunker.","color":"yellow"}
