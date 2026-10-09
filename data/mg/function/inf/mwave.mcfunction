execute as @e[type=minecraft:marker,tag=mg.zsp,sort=random,limit=1] at @s run function mg:zm/spawn_one with storage mg:zm
scoreboard players remove $imw mg.st 1
execute if score $imw mg.st matches 1.. run function mg:inf/mwave
