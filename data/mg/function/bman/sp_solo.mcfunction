# @s : départ n° ykx
execute if score $ykx mg.st matches 0 run tp @s -9.5 65 40691.5
execute if score $ykx mg.st matches 1 run tp @s 10.5 65 40709.5
execute if score $ykx mg.st matches 2 run tp @s 10.5 65 40691.5
execute if score $ykx mg.st matches 3 run tp @s -9.5 65 40709.5
execute if score $ykx mg.st matches 4 run tp @s 0.5 65 40691.5
execute if score $ykx mg.st matches 5 run tp @s 0.5 65 40709.5
execute if score $ykx mg.st matches 6 run tp @s -9.5 65 40701.5
execute if score $ykx mg.st matches 7 run tp @s 10.5 65 40699.5
execute if score $ykx mg.st matches 8.. run return run function mg:bman/extra
execute at @s run spawnpoint @s ~ ~ ~
scoreboard players add $ykx mg.st 1
