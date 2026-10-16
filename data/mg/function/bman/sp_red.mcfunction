# @s : départ n° ykr
execute if score $ykr mg.st matches 0 run tp @s -9.5 65 40691.5
execute if score $ykr mg.st matches 1 run tp @s -9.5 65 40709.5
execute if score $ykr mg.st matches 2 run tp @s -9.5 65 40699.5
execute if score $ykr mg.st matches 3 run tp @s -5.5 65 40691.5
execute if score $ykr mg.st matches 4.. run return run function mg:bman/extra
execute at @s run spawnpoint @s ~ ~ ~
scoreboard players add $ykr mg.st 1
