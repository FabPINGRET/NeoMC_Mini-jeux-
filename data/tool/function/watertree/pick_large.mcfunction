summon area_effect_cloud ~ ~ ~ {Tags:["water_temp","1","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["water_temp","2","exclude"]}


tag @e[type=minecraft:area_effect_cloud,tag=water_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=water_temp,tag=exclude,distance=0..]

execute if entity @e[tag=water_temp,tag=1,distance=0..] run function tool:watertree/large/6
execute if entity @e[tag=water_temp,tag=2,distance=0..] run function tool:watertree/large/7

kill @e[type=minecraft:area_effect_cloud,tag=water_temp,distance=0..]
