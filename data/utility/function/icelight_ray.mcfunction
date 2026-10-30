particle electric_spark ~ ~ ~ 0.1 0.1 0.1 0 1
particle ominous_spawning ~ ~ ~ 0 0 0 0 1

execute positioned ~ ~-1 ~ as @n[tag=icelight_nexttarget,distance=..0.45] at @s run return run function utility:icelight_chain_mark

execute positioned ^ ^ ^0.1 run function utility:icelight_ray
