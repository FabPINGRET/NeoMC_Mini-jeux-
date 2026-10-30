summon area_effect_cloud ~ ~ ~ {Tags:["st_shuffle_temp","1","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["st_shuffle_temp","2","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["st_shuffle_temp","3","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["st_shuffle_temp","4","exclude"]}
tag @e[type=minecraft:area_effect_cloud,tag=st_shuffle_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=st_shuffle_temp,tag=exclude,distance=0..]

execute as @n[tag=st_shuffle_temp,distance=0..] if entity @s[tag=1] run function dungeon:7/laser/rotate_mirror

execute as @n[tag=st_shuffle_temp,distance=0..] if entity @s[tag=2] run function dungeon:7/laser/rotate_mirror
execute as @n[tag=st_shuffle_temp,distance=0..] if entity @s[tag=2] run function dungeon:7/laser/rotate_mirror

execute as @n[tag=st_shuffle_temp,distance=0..] if entity @s[tag=3] run function dungeon:7/laser/rotate_mirror
execute as @n[tag=st_shuffle_temp,distance=0..] if entity @s[tag=3] run function dungeon:7/laser/rotate_mirror
execute as @n[tag=st_shuffle_temp,distance=0..] if entity @s[tag=3] run function dungeon:7/laser/rotate_mirror


kill @e[type=minecraft:area_effect_cloud,tag=st_shuffle_temp,distance=0..]
