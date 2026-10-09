scoreboard players set $imc mg.st 0
execute as @e[type=minecraft:marker,tag=mg.zsp,sort=random,limit=1] at @s unless entity @a[tag=mg.play,tag=!mg.inf,distance=..5] run function mg:zm/spawn_one with storage mg:zm
