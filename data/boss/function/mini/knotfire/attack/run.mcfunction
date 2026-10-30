execute as @n[tag=knotfire_run_dest,distance=0..] at @s rotated as @n[tag=knotfire_statue,tag=active,distance=0..] run tp @s ~ ~ ~ ~ ~

execute as @n[tag=knotfire_statue,tag=active,distance=0..] at @s run function boss:mini/knotfire/attack/run_ray
