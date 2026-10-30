particle copper_fire_flame ~ ~ ~ 0 0 0 0 1

execute positioned ^ ^ ^0.1 positioned ~ 77 ~ if block ^ ^ ^ air unless entity @e[tag=knotfire_statue,tag=next_active,distance=..5.2] run function boss:mini/knotfire/arena/next_laser_ray
