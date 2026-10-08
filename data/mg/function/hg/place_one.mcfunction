# @s → socle n°$hgi
execute if score $hgi mg.st matches 0 run tp @s 7.5 83 22800.5 facing 0 83 22800
execute if score $hgi mg.st matches 1 run tp @s 7.5 83 22802.5 facing 0 83 22800
execute if score $hgi mg.st matches 2 run tp @s 6.5 83 22803.5 facing 0 83 22800
execute if score $hgi mg.st matches 3 run tp @s 5.5 83 22805.5 facing 0 83 22800
execute if score $hgi mg.st matches 4 run tp @s 4.5 83 22806.5 facing 0 83 22800
execute if score $hgi mg.st matches 5 run tp @s 2.5 83 22807.5 facing 0 83 22800
execute if score $hgi mg.st matches 6 run tp @s 0.5 83 22807.5 facing 0 83 22800
execute if score $hgi mg.st matches 7 run tp @s -1.5 83 22807.5 facing 0 83 22800
execute if score $hgi mg.st matches 8 run tp @s -2.5 83 22806.5 facing 0 83 22800
execute if score $hgi mg.st matches 9 run tp @s -4.5 83 22805.5 facing 0 83 22800
execute if score $hgi mg.st matches 10 run tp @s -5.5 83 22803.5 facing 0 83 22800
execute if score $hgi mg.st matches 11 run tp @s -6.5 83 22802.5 facing 0 83 22800
execute if score $hgi mg.st matches 12 run tp @s -6.5 83 22800.5 facing 0 83 22800
execute if score $hgi mg.st matches 13 run tp @s -6.5 83 22798.5 facing 0 83 22800
execute if score $hgi mg.st matches 14 run tp @s -5.5 83 22797.5 facing 0 83 22800
execute if score $hgi mg.st matches 15 run tp @s -4.5 83 22795.5 facing 0 83 22800
execute if score $hgi mg.st matches 16 run tp @s -3.5 83 22794.5 facing 0 83 22800
execute if score $hgi mg.st matches 17 run tp @s -1.5 83 22793.5 facing 0 83 22800
execute if score $hgi mg.st matches 18 run tp @s 0.5 83 22793.5 facing 0 83 22800
execute if score $hgi mg.st matches 19 run tp @s 2.5 83 22793.5 facing 0 83 22800
execute if score $hgi mg.st matches 20 run tp @s 4.5 83 22794.5 facing 0 83 22800
execute if score $hgi mg.st matches 21 run tp @s 5.5 83 22795.5 facing 0 83 22800
execute if score $hgi mg.st matches 22 run tp @s 6.5 83 22796.5 facing 0 83 22800
execute if score $hgi mg.st matches 23 run tp @s 7.5 83 22798.5 facing 0 83 22800
execute at @s run spawnpoint @s ~ ~ ~
scoreboard players add $hgi mg.st 1
execute if score $hgi mg.st matches 24.. run scoreboard players set $hgi mg.st 0
