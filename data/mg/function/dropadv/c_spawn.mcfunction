# Place @s sur un des 4 côtés du rebord du niveau de la manche ($dcl)
scoreboard players operation @s mg.dlv = $dcl mg.st
scoreboard players operation $dcs mg.st = $dci mg.st
scoreboard players operation $dcs mg.st %= #k4 mg.st
scoreboard players add $dci mg.st 1
execute if score $dcl mg.st matches 1 if score $dcs mg.st matches 0 run tp @s 0.5 301 23989.5 0 25
execute if score $dcl mg.st matches 1 if score $dcs mg.st matches 1 run tp @s 0.5 301 24011.5 180 25
execute if score $dcl mg.st matches 1 if score $dcs mg.st matches 2 run tp @s -10.5 301 24000.5 -90 25
execute if score $dcl mg.st matches 1 if score $dcs mg.st matches 3 run tp @s 11.5 301 24000.5 90 25
execute if score $dcl mg.st matches 2 if score $dcs mg.st matches 0 run tp @s 40.5 301 23989.5 0 25
execute if score $dcl mg.st matches 2 if score $dcs mg.st matches 1 run tp @s 40.5 301 24011.5 180 25
execute if score $dcl mg.st matches 2 if score $dcs mg.st matches 2 run tp @s 29.5 301 24000.5 -90 25
execute if score $dcl mg.st matches 2 if score $dcs mg.st matches 3 run tp @s 51.5 301 24000.5 90 25
execute if score $dcl mg.st matches 3 if score $dcs mg.st matches 0 run tp @s 80.5 301 23989.5 0 25
execute if score $dcl mg.st matches 3 if score $dcs mg.st matches 1 run tp @s 80.5 301 24011.5 180 25
execute if score $dcl mg.st matches 3 if score $dcs mg.st matches 2 run tp @s 69.5 301 24000.5 -90 25
execute if score $dcl mg.st matches 3 if score $dcs mg.st matches 3 run tp @s 91.5 301 24000.5 90 25
execute if score $dcl mg.st matches 4 if score $dcs mg.st matches 0 run tp @s 120.5 301 23989.5 0 25
execute if score $dcl mg.st matches 4 if score $dcs mg.st matches 1 run tp @s 120.5 301 24011.5 180 25
execute if score $dcl mg.st matches 4 if score $dcs mg.st matches 2 run tp @s 109.5 301 24000.5 -90 25
execute if score $dcl mg.st matches 4 if score $dcs mg.st matches 3 run tp @s 131.5 301 24000.5 90 25
execute if score $dcl mg.st matches 5 if score $dcs mg.st matches 0 run tp @s 160.5 301 23989.5 0 25
execute if score $dcl mg.st matches 5 if score $dcs mg.st matches 1 run tp @s 160.5 301 24011.5 180 25
execute if score $dcl mg.st matches 5 if score $dcs mg.st matches 2 run tp @s 149.5 301 24000.5 -90 25
execute if score $dcl mg.st matches 5 if score $dcs mg.st matches 3 run tp @s 171.5 301 24000.5 90 25
execute if score $dcl mg.st matches 6 if score $dcs mg.st matches 0 run tp @s 200.5 301 23989.5 0 25
execute if score $dcl mg.st matches 6 if score $dcs mg.st matches 1 run tp @s 200.5 301 24011.5 180 25
execute if score $dcl mg.st matches 6 if score $dcs mg.st matches 2 run tp @s 189.5 301 24000.5 -90 25
execute if score $dcl mg.st matches 6 if score $dcs mg.st matches 3 run tp @s 211.5 301 24000.5 90 25
execute if score $dcl mg.st matches 7 if score $dcs mg.st matches 0 run tp @s 240.5 301 23989.5 0 25
execute if score $dcl mg.st matches 7 if score $dcs mg.st matches 1 run tp @s 240.5 301 24011.5 180 25
execute if score $dcl mg.st matches 7 if score $dcs mg.st matches 2 run tp @s 229.5 301 24000.5 -90 25
execute if score $dcl mg.st matches 7 if score $dcs mg.st matches 3 run tp @s 251.5 301 24000.5 90 25
execute if score $dcl mg.st matches 8 if score $dcs mg.st matches 0 run tp @s 280.5 301 23989.5 0 25
execute if score $dcl mg.st matches 8 if score $dcs mg.st matches 1 run tp @s 280.5 301 24011.5 180 25
execute if score $dcl mg.st matches 8 if score $dcs mg.st matches 2 run tp @s 269.5 301 24000.5 -90 25
execute if score $dcl mg.st matches 8 if score $dcs mg.st matches 3 run tp @s 291.5 301 24000.5 90 25
execute if score $dcl mg.st matches 9 if score $dcs mg.st matches 0 run tp @s 320.5 301 23989.5 0 25
execute if score $dcl mg.st matches 9 if score $dcs mg.st matches 1 run tp @s 320.5 301 24011.5 180 25
execute if score $dcl mg.st matches 9 if score $dcs mg.st matches 2 run tp @s 309.5 301 24000.5 -90 25
execute if score $dcl mg.st matches 9 if score $dcs mg.st matches 3 run tp @s 331.5 301 24000.5 90 25
execute if score $dcl mg.st matches 10 if score $dcs mg.st matches 0 run tp @s 360.5 301 23989.5 0 25
execute if score $dcl mg.st matches 10 if score $dcs mg.st matches 1 run tp @s 360.5 301 24011.5 180 25
execute if score $dcl mg.st matches 10 if score $dcs mg.st matches 2 run tp @s 349.5 301 24000.5 -90 25
execute if score $dcl mg.st matches 10 if score $dcs mg.st matches 3 run tp @s 371.5 301 24000.5 90 25
scoreboard players set @s mg.cd 20
effect give @s minecraft:resistance 2 255 true
