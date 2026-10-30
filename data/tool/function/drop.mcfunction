execute as @e[tag=carrying,distance=0..] at @s align xyz run tp @s ~0.5 ~ ~0.5
tag @e[type=minecraft:armor_stand,sort=nearest,limit=1,distance=0..] remove carrying
#execute as @n[type=armor_stand] at @s align xyz run tp @s ~0.5 ~ ~0.5
