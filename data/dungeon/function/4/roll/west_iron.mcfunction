fill ~-1 ~ ~-1 ~1 ~2 ~1 air
tp @s ~-3 ~ ~

tag @s add rolling

execute if entity @s[tag=rolling,tag=up] run tag @s add west
execute if entity @s[tag=rolling,tag=up] run tag @s remove rolling
execute if entity @s[tag=west,tag=up] run tag @s remove up

execute if entity @s[tag=rolling,tag=east] run tag @s add up
execute if entity @s[tag=rolling,tag=east] run tag @s remove rolling
execute if entity @s[tag=up,tag=east] run tag @s remove east

execute if entity @s[tag=rolling,tag=down] run tag @s add east
execute if entity @s[tag=rolling,tag=down] run tag @s remove rolling
execute if entity @s[tag=east,tag=down] run tag @s remove down

execute if entity @s[tag=rolling,tag=west] run tag @s add down
execute if entity @s[tag=rolling,tag=west] run tag @s remove rolling
execute if entity @s[tag=down,tag=west] run tag @s remove west

tag @s remove rolling

execute if entity @s[tag=west] at @s run clone -9947 77 -415 -9945 79 -413 ~-1 ~ ~-1
execute if entity @s[tag=south] at @s run clone -9947 77 -411 -9945 79 -409 ~-1 ~ ~-1
execute if entity @s[tag=east] at @s run clone -9947 77 -407 -9945 79 -405 ~-1 ~ ~-1
execute if entity @s[tag=north] at @s run clone -9947 77 -403 -9945 79 -401 ~-1 ~ ~-1
execute if entity @s[tag=up] at @s run clone -9947 77 -399 -9945 79 -397 ~-1 ~ ~-1
execute if entity @s[tag=down] at @s run clone -9947 77 -395 -9945 79 -393 ~-1 ~ ~-1

