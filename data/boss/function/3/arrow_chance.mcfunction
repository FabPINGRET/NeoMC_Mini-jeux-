summon area_effect_cloud ~ ~ ~ {Tags:["lod_boss_arrow_temp","1","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["lod_boss_arrow_temp","2","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["lod_boss_arrow_temp","2","exclude"]}


tag @e[type=minecraft:area_effect_cloud,tag=lod_boss_arrow_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=lod_boss_arrow_temp,tag=exclude,distance=0..]

execute if entity @e[tag=lod_boss_arrow_temp,tag=1,distance=0..] at @e[tag=lod_boss_loc,distance=0..] run summon item ~ ~ ~ {Item:{id:"minecraft:arrow",Count:1b}}


kill @e[type=minecraft:area_effect_cloud,tag=lod_boss_arrow_temp,distance=0..]
