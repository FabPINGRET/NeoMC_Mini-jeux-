# @s : départ n° ykb
execute if score $ykb mg.st matches 0 run tp @s 10.5 65 40709.5
execute if score $ykb mg.st matches 1 run tp @s 10.5 65 40691.5
execute if score $ykb mg.st matches 2 run tp @s 10.5 65 40701.5
execute if score $ykb mg.st matches 3 run tp @s 6.5 65 40709.5
execute if score $ykb mg.st matches 4.. run return run function mg:bman/extra
execute at @s run spawnpoint @s ~ ~ ~
scoreboard players add $ykb mg.st 1
