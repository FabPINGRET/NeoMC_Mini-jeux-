particle composter ^ ^ ^ 0.2 0.2 0.2 0 1
#particle dust{scale:1,color:[0,1,0]} ^ ^ ^ 0.2 0.2 0.2 0 1
#particle dust{scale:1,color:[0.95,1.00,0.95]} ^ ^ ^ 0.05 0.05 0.05 0 1


execute if block ^ ^ ^ air as @a[distance=..1.5,tag=mg.flw] run damage @s 6 minecraft:magic by @n[tag=st_hand_loc,tag=!attacking,tag=point_down,distance=0..]

execute if block ^ ^ ^ air positioned ~ ~-1 ~ run function boss:7/utility/point_down_ray
