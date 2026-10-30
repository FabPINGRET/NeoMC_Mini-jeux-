execute as @e[tag=pretzel_emerald_spawn,sort=random,limit=2,distance=0..] at @s run tag @s add pretzel_turtle_spawn

execute as @e[tag=pretzel_turtle_spawn,distance=0..] at @s run function boss:mini/pretzel/utility/turtle_spawn

tag @e[tag=pretzel_emerald_spawn,distance=0..] remove pretzel_turtle_spawn

setblock -10355 61 443 minecraft:redstone_block

playsound minecraft:entity.turtle.death hostile @a[tag=mg.flw] -10340 89 446 2 0.1
particle minecraft:egg_crack -10340 92.5 446 1 1 1 1 40
