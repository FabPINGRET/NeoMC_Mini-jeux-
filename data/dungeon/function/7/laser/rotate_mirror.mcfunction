execute as @n[tag=st_mirror,distance=..10] at @s run tp @s ~ ~ ~ ~90 0

execute as @n[tag=st_mirror,distance=..10] if entity @s[tag=nw] run tag @s add change_ne
execute as @n[tag=st_mirror,distance=..10] if entity @s[tag=ne] run tag @s add change_se
execute as @n[tag=st_mirror,distance=..10] if entity @s[tag=se] run tag @s add change_sw
execute as @n[tag=st_mirror,distance=..10] if entity @s[tag=sw] run tag @s add change_nw

execute as @n[tag=st_mirror,distance=..10] run tag @s remove nw
execute as @n[tag=st_mirror,distance=..10] run tag @s remove sw
execute as @n[tag=st_mirror,distance=..10] run tag @s remove ne
execute as @n[tag=st_mirror,distance=..10] run tag @s remove se

execute as @n[tag=st_mirror,distance=..10] if entity @s[tag=change_ne] run tag @s add ne
execute as @n[tag=st_mirror,distance=..10] if entity @s[tag=change_se] run tag @s add se
execute as @n[tag=st_mirror,distance=..10] if entity @s[tag=change_sw] run tag @s add sw
execute as @n[tag=st_mirror,distance=..10] if entity @s[tag=change_nw] run tag @s add nw

execute as @n[tag=st_mirror,distance=..10] run tag @s remove change_nw
execute as @n[tag=st_mirror,distance=..10] run tag @s remove change_sw
execute as @n[tag=st_mirror,distance=..10] run tag @s remove change_ne
execute as @n[tag=st_mirror,distance=..10] run tag @s remove change_se
