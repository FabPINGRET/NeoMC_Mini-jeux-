# Place @s sur le rebord de départ de son niveau (mg.dlv)
execute if score @s mg.dlv matches 1 run tp @s 0.5 201 23989.5 0 25
execute if score @s mg.dlv matches 2 run tp @s 40.5 201 23989.5 0 25
execute if score @s mg.dlv matches 3 run tp @s 80.5 201 23989.5 0 25
execute if score @s mg.dlv matches 4 run tp @s 120.5 201 23989.5 0 25
execute if score @s mg.dlv matches 5 run tp @s 160.5 201 23989.5 0 25
execute if score @s mg.dlv matches 6 run tp @s 200.5 201 23989.5 0 25
execute if score @s mg.dlv matches 7 run tp @s 240.5 201 23989.5 0 25
execute if score @s mg.dlv matches 8 run tp @s 280.5 201 23989.5 0 25
execute if score @s mg.dlv matches 9 run tp @s 320.5 201 23989.5 0 25
execute if score @s mg.dlv matches 10 run tp @s 360.5 201 23989.5 0 25
scoreboard players set @s mg.cd 10
effect give @s minecraft:resistance 2 255 true
