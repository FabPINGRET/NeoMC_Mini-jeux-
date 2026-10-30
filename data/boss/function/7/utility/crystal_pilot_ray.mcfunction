particle dust{scale:1,color:[1,1,1]} ^ ^ ^ 0.05 0.05 0.05 0 1

execute unless entity @n[tag=st_crystal,distance=..0.5] rotated ~ 0 if block ^ ^ ^ air positioned ^ ^ ^0.1 run function boss:7/utility/crystal_pilot_ray
