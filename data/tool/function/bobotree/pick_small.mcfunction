summon area_effect_cloud ~ ~ ~ {Tags:["bobo_temp","1","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["bobo_temp","2","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["bobo_temp","3","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["bobo_temp","4","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=bobo_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=bobo_temp,tag=exclude,distance=0..]

execute if entity @e[tag=bobo_temp,tag=1,distance=0..] run function tool:bobotree/small/east
execute if entity @e[tag=bobo_temp,tag=2,distance=0..] run function tool:bobotree/small/west
execute if entity @e[tag=bobo_temp,tag=3,distance=0..] run function tool:bobotree/small/south
execute if entity @e[tag=bobo_temp,tag=4,distance=0..] run function tool:bobotree/small/north

kill @e[type=minecraft:area_effect_cloud,tag=bobo_temp,distance=0..]
