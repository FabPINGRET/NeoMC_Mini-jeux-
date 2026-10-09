# Présentoirs : réassort, achat par le joueur le plus proche (une fois par passage : tag mg.gbuy)
scoreboard players remove @e[type=minecraft:marker,tag=mg.gpad,scores={mg.gpc=1..}] mg.gpc 10
execute as @e[type=minecraft:marker,tag=mg.gpad,scores={mg.gpc=0}] at @s unless entity @e[type=minecraft:item_display,tag=mg.gpdi,distance=..1.5] run function mg:gta/pad_show
execute as @a[tag=mg.gbuy] at @s unless entity @e[type=minecraft:marker,tag=mg.gpad,distance=..2.2] run tag @s remove mg.gbuy
execute as @e[type=minecraft:marker,tag=mg.gpad,scores={mg.gpc=..0}] at @s if entity @a[tag=mg.gtw,tag=!mg.gbuy,gamemode=!spectator,distance=..1.6] run function mg:gta/pad_take
