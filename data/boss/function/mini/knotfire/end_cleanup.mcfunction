fill -10704 72 96 -10690 73 82 air

tp @n[tag=knotfire_statue,tag=crashed,distance=0..] @n[tag=knotfire_run_dest,distance=0..]

execute as @e[tag=knotfire_statue,distance=0..] run function boss:mini/knotfire/pose/blank
execute as @e[tag=knotfire_statue,distance=0..] at @s facing -10697 72 89 run tp @s ~ ~ ~ ~ ~

tag @e[tag=knotfire_statue,distance=0..] remove crashed
kill @e[tag=knotfire_run_dest,distance=0..]

fill -10714 72 72 -10680 73 106 suspicious_sand replace minecraft:brown_glazed_terracotta
fill -10714 72 72 -10680 73 106 suspicious_sand replace minecraft:cyan_glazed_terracotta
fill -10714 72 72 -10680 73 106 cut_sandstone replace minecraft:suspicious_sand
fill -10714 61 72 -10680 64 106 air replace redstone_block
execute positioned -10697 72 89 run kill @e[tag=walking_statue,distance=..30]
