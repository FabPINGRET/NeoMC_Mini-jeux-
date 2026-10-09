# @s → socle n°$hgi
execute if score $hgi mg.st matches 0 run tp @s 7.5 83 34600.5 facing 0 83 34600
execute if score $hgi mg.st matches 1 run tp @s 7.5 83 34602.5 facing 0 83 34600
execute if score $hgi mg.st matches 2 run tp @s 6.5 83 34603.5 facing 0 83 34600
execute if score $hgi mg.st matches 3 run tp @s 5.5 83 34605.5 facing 0 83 34600
execute if score $hgi mg.st matches 4 run tp @s 4.5 83 34606.5 facing 0 83 34600
execute if score $hgi mg.st matches 5 run tp @s 2.5 83 34607.5 facing 0 83 34600
execute if score $hgi mg.st matches 6 run tp @s 0.5 83 34607.5 facing 0 83 34600
execute if score $hgi mg.st matches 7 run tp @s -1.5 83 34607.5 facing 0 83 34600
execute if score $hgi mg.st matches 8 run tp @s -2.5 83 34606.5 facing 0 83 34600
execute if score $hgi mg.st matches 9 run tp @s -4.5 83 34605.5 facing 0 83 34600
execute if score $hgi mg.st matches 10 run tp @s -5.5 83 34603.5 facing 0 83 34600
execute if score $hgi mg.st matches 11 run tp @s -6.5 83 34602.5 facing 0 83 34600
execute if score $hgi mg.st matches 12 run tp @s -6.5 83 34600.5 facing 0 83 34600
execute if score $hgi mg.st matches 13 run tp @s -6.5 83 34598.5 facing 0 83 34600
execute if score $hgi mg.st matches 14 run tp @s -5.5 83 34597.5 facing 0 83 34600
execute if score $hgi mg.st matches 15 run tp @s -4.5 83 34595.5 facing 0 83 34600
execute if score $hgi mg.st matches 16 run tp @s -3.5 83 34594.5 facing 0 83 34600
execute if score $hgi mg.st matches 17 run tp @s -1.5 83 34593.5 facing 0 83 34600
execute if score $hgi mg.st matches 18 run tp @s 0.5 83 34593.5 facing 0 83 34600
execute if score $hgi mg.st matches 19 run tp @s 2.5 83 34593.5 facing 0 83 34600
execute if score $hgi mg.st matches 20 run tp @s 4.5 83 34594.5 facing 0 83 34600
execute if score $hgi mg.st matches 21 run tp @s 5.5 83 34595.5 facing 0 83 34600
execute if score $hgi mg.st matches 22 run tp @s 6.5 83 34596.5 facing 0 83 34600
execute if score $hgi mg.st matches 23 run tp @s 7.5 83 34598.5 facing 0 83 34600
execute at @s run spawnpoint @s ~ ~ ~
scoreboard players add $hgi mg.st 1
execute if score $hgi mg.st matches 24.. run scoreboard players set $hgi mg.st 0
