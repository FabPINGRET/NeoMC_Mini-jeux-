tag @s add deebo_trident_target
execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing entity @n[tag=deebo_trident_target,distance=0..] eyes run function boss:mini/dark_eebo/attack/trident_launch
tag @a[tag=mg.flw] remove deebo_trident_target
