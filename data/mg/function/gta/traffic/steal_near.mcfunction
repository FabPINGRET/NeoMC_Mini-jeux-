# @s (joueur accroupi) : vole la voiture PNJ la plus proche
tag @s add mg.gthief
execute as @e[type=minecraft:marker,tag=mg.gtraf,distance=..2.6,limit=1,sort=nearest] at @s run function mg:gta/traffic/steal
tag @a remove mg.gthief
