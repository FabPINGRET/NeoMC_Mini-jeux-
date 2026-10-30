tag @s remove due_east
tag @s remove due_west
tag @s remove due_north
tag @s remove due_south
tag @s remove change_north
tag @s remove change_south
tag @s remove change_west
tag @s remove change_east

execute if entity @s[tag=east] run tag @s add due_east
execute if entity @s[tag=west] run tag @s add due_west
execute if entity @s[tag=north] run tag @s add due_north
execute if entity @s[tag=north] run tag @s add due_north

execute if entity @s[tag=south] run tag @s add due_south

particle egg_crack ~ ~ ~ 0.1 0.1 0.1 0 1

execute as @s at @s facing ^ ^ ^1 positioned ^ ^ ^1 run function dungeon:7/laser/ray
