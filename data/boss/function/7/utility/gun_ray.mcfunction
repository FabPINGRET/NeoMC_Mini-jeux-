#particle composter ^ ^ ^ 0.2 0.2 0.2 0 1
particle dust{scale:1,color:[0,1,0]} ^ ^ ^ 0.2 0.2 0.2 0 2
particle dust{scale:1,color:[0.95,1.00,0.95]} ^ ^ ^ 0.05 0.05 0.05 0 2


execute if block ^ ^ ^ air as @a[distance=..2,tag=mg.flw] run damage @s 16 minecraft:indirect_magic by @n[tag=st_hand_loc,tag=attacking,distance=0..]

execute if block ^ ^ ^ air positioned ^ ^ ^0.1 run function boss:7/utility/gun_ray
