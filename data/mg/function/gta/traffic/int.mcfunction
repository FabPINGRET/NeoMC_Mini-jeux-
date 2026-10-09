# @s (zone cliquable d'une voiture PNJ) : le joueur qui a cliqué la vole
scoreboard players operation $gv mg.st = @s mg.gvid
execute on target run tag @s add mg.gthief
execute as @e[type=minecraft:marker,tag=mg.gtraf] if score @s mg.gvid = $gv mg.st at @s run function mg:gta/traffic/steal
tag @a remove mg.gthief
