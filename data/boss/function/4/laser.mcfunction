particle lava ^ ^ ^ 0.2 0.2 0.2 0 2
particle landing_lava ^ ^ ^ 0.4 0.4 0.4 0 2

execute if block ^ ^ ^ air as @a[distance=..4,tag=mg.flw] run damage @s 16 minecraft:mob_projectile by @e[limit=1,tag=boss_ed_name,distance=0..]

execute if block ^ ^ ^ air positioned ^ ^ ^0.1 run function boss:4/laser
