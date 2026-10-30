fill ~-1 ~ ~-1 ~1 ~2 ~1 air
tp @s ~ ~ ~-3

tag @s add rolling

execute if entity @s[tag=rolling,tag=up] run tag @s add north
execute if entity @s[tag=rolling,tag=up] run tag @s remove rolling
execute if entity @s[tag=north,tag=up] run tag @s remove up

execute if entity @s[tag=rolling,tag=north] run tag @s add down
execute if entity @s[tag=rolling,tag=north] run tag @s remove rolling
execute if entity @s[tag=down,tag=north] run tag @s remove north

execute if entity @s[tag=rolling,tag=down] run tag @s add south
execute if entity @s[tag=rolling,tag=down] run tag @s remove rolling
execute if entity @s[tag=south,tag=down] run tag @s remove down

execute if entity @s[tag=rolling,tag=south] run tag @s add up
execute if entity @s[tag=rolling,tag=south] run tag @s remove rolling
execute if entity @s[tag=up,tag=south] run tag @s remove south

tag @s remove rolling

execute if entity @s[tag=west] at @s run clone -9943 77 -415 -9941 79 -413 ~-1 ~ ~-1
execute if entity @s[tag=south] at @s run clone -9943 77 -411 -9941 79 -409 ~-1 ~ ~-1
execute if entity @s[tag=east] at @s run clone -9943 77 -407 -9941 79 -405 ~-1 ~ ~-1
execute if entity @s[tag=north] at @s run clone -9943 77 -403 -9941 79 -401 ~-1 ~ ~-1
execute if entity @s[tag=up] at @s run clone -9943 77 -399 -9941 79 -397 ~-1 ~ ~-1
execute if entity @s[tag=down] at @s run clone -9943 77 -395 -9941 79 -393 ~-1 ~ ~-1

