# @s (zombie) : dans un enclos au hasard, 2 s de protection
execute at @e[type=minecraft:marker,tag=mg.zsp,sort=random,limit=1] run tp @s ~ ~ ~
execute at @s run spawnpoint @s ~ ~ ~
effect give @s minecraft:resistance 2 4 true
effect give @s minecraft:instant_health 1 4 true
