execute if entity @e[tag=lash_base_1,tag=lash_ready,distance=0..] run summon area_effect_cloud -9932 166 148 {Tags:["lash_temp","1","exclude"]}
execute if entity @e[tag=lash_base_2,tag=lash_ready,distance=0..] run summon area_effect_cloud -9932 166 148 {Tags:["lash_temp","2","exclude"]}
execute if entity @e[tag=lash_base_3,tag=lash_ready,distance=0..] run summon area_effect_cloud -9932 166 148 {Tags:["lash_temp","3","exclude"]}
execute if entity @e[tag=lash_base_4,tag=lash_ready,distance=0..] run summon area_effect_cloud -9932 166 148 {Tags:["lash_temp","4","exclude"]}
execute if entity @e[tag=lash_base_5,tag=lash_ready,distance=0..] run summon area_effect_cloud -9932 166 148 {Tags:["lash_temp","5","exclude"]}
execute if entity @e[tag=lash_base_6,tag=lash_ready,distance=0..] run summon area_effect_cloud -9932 166 148 {Tags:["lash_temp","6","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=lash_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=lash_temp,tag=exclude,distance=0..]

execute if entity @e[tag=lash_temp,tag=1,distance=0..] as @e[tag=lash_base_1,distance=0..] at @s anchored eyes run function boss:1/lash_ray
execute if entity @e[tag=lash_temp,tag=1,distance=0..] run tag @e[tag=lash_base_1,distance=0..] remove lash_ready
execute if entity @e[tag=lash_temp,tag=2,distance=0..] as @e[tag=lash_base_2,distance=0..] at @s anchored eyes run function boss:1/lash_ray
execute if entity @e[tag=lash_temp,tag=2,distance=0..] run tag @e[tag=lash_base_2,distance=0..] remove lash_ready
execute if entity @e[tag=lash_temp,tag=3,distance=0..] as @e[tag=lash_base_3,distance=0..] at @s anchored eyes run function boss:1/lash_ray
execute if entity @e[tag=lash_temp,tag=3,distance=0..] run tag @e[tag=lash_base_3,distance=0..] remove lash_ready
execute if entity @e[tag=lash_temp,tag=4,distance=0..] as @e[tag=lash_base_4,distance=0..] at @s anchored eyes run function boss:1/lash_ray
execute if entity @e[tag=lash_temp,tag=4,distance=0..] run tag @e[tag=lash_base_4,distance=0..] remove lash_ready
execute if entity @e[tag=lash_temp,tag=5,distance=0..] as @e[tag=lash_base_5,distance=0..] at @s anchored eyes run function boss:1/lash_ray
execute if entity @e[tag=lash_temp,tag=5,distance=0..] run tag @e[tag=lash_base_5,distance=0..] remove lash_ready
execute if entity @e[tag=lash_temp,tag=6,distance=0..] as @e[tag=lash_base_6,distance=0..] at @s anchored eyes run function boss:1/lash_ray
execute if entity @e[tag=lash_temp,tag=6,distance=0..] run tag @e[tag=lash_base_6,distance=0..] remove lash_ready

kill @e[type=minecraft:area_effect_cloud,tag=lash_temp,distance=0..]
