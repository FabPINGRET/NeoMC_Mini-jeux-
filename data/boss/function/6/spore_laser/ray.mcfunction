particle dragon_breath ^ ^ ^ 0.2 0.2 0.2 0 1
particle mycelium ^ ^ ^ 0.4 0.4 0.4 0 4

execute if block ^ ^ ^ air as @a[distance=..4,tag=mg.flw] run damage @s 26 minecraft:mob_projectile by @n[tag=boss_sh_dm_sporelaser,distance=0..]

execute if block ^ ^ ^ air positioned ^ ^ ^0.1 run function boss:6/spore_laser/ray
