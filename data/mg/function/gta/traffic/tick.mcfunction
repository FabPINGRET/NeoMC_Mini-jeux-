# @s : voiture PNJ (chaque tick) : avance de 0,3 bloc sauf obstacle, carrefour atteint, carrosserie
scoreboard players add @s mg.gtw8 1
execute positioned ^ ^ ^2.6 if entity @e[type=!minecraft:marker,type=!minecraft:block_display,type=!minecraft:item_display,type=!minecraft:text_display,type=!minecraft:item,type=!minecraft:arrow,distance=..1.9] run return run function mg:gta/traffic/blocked
execute positioned ^ ^ ^2.6 if entity @e[type=minecraft:marker,tag=mg.gtraf,distance=..1.9] run return run function mg:gta/traffic/blocked
scoreboard players set @s mg.gtw8 0
tp @s ^ ^ ^0.3
execute store result score $gpx mg.st run data get entity @s Pos[0] 10
execute store result score $gpz mg.st run data get entity @s Pos[2] 10
execute if score @s mg.gth matches 3 if score $gpx mg.st >= @s mg.gttx run function mg:gta/traffic/arrive
execute if score @s mg.gth matches 1 if score $gpx mg.st <= @s mg.gttx run function mg:gta/traffic/arrive
execute if score @s mg.gth matches 0 if score $gpz mg.st >= @s mg.gttz run function mg:gta/traffic/arrive
execute if score @s mg.gth matches 2 if score $gpz mg.st <= @s mg.gttz run function mg:gta/traffic/arrive
execute at @s run function mg:gta/traffic/sync
