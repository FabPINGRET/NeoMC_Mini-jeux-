particle copper_fire_flame ~ ~ ~ 0.1 0.1 0.1 0.01 1

execute as @a[distance=..0.3,tag=mg.flw] run damage @s 12 minecraft:dragon_breath by @n[tag=knotfire_boss,distance=0..]
execute positioned ~ ~-0.5 ~ as @a[distance=..0.3,tag=mg.flw] run damage @s 12 minecraft:dragon_breath by @n[tag=knotfire_boss,distance=0..]
execute positioned ~ ~1 ~ as @a[distance=..0.3,tag=mg.flw] run damage @s 12 minecraft:dragon_breath by @n[tag=knotfire_boss,distance=0..]


execute positioned ^ ^ ^0.1 if block ^ ^ ^ air run function boss:mini/knotfire/attack/laser_ray
