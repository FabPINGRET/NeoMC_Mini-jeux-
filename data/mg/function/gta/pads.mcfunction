# Présentoirs : réassort, achat par le joueur le plus proche (une fois par passage : tag mg.gbz sur le présentoir, retiré quand plus personne n'est devant)
scoreboard players remove @e[type=minecraft:marker,tag=mg.gpad,scores={mg.gpc=1..}] mg.gpc 10
execute as @e[type=minecraft:marker,tag=mg.gpad,scores={mg.gpc=0}] at @s unless entity @e[type=minecraft:item_display,tag=mg.gpdi,distance=..1.5] run function mg:gta/pad_show
execute as @e[type=minecraft:marker,tag=mg.gpad,tag=mg.gbz] at @s unless entity @a[tag=mg.gtw,gamemode=!spectator,distance=..2] run tag @s remove mg.gbz
execute as @e[type=minecraft:marker,tag=mg.gpad,tag=!mg.gbz,scores={mg.gpc=..0}] at @s if entity @a[tag=mg.gtw,gamemode=!spectator,distance=..1.6] run function mg:gta/pad_take
tag @a remove mg.gbuy
