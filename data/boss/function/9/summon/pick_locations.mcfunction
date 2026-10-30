execute run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_summon_temp","1","exclude"]}
execute run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_summon_temp","2","exclude"]}
execute run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_summon_temp","3","exclude"]}
execute run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_summon_temp","4","exclude"]}
execute run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_summon_temp","5","exclude"]}
execute run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_summon_temp","6","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=wm_summon_temp,limit=2,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=wm_summon_temp,tag=exclude,distance=0..]

execute if entity @e[tag=wm_summon_temp,tag=1,distance=0..] positioned -11211 17 -115 run function summon:encruster
execute if entity @e[tag=wm_summon_temp,tag=2,distance=0..] positioned -11225 20 -120 run function summon:encruster
execute if entity @e[tag=wm_summon_temp,tag=3,distance=0..] positioned -11234 19 -113 run function summon:encruster
execute if entity @e[tag=wm_summon_temp,tag=4,distance=0..] positioned -11232 17 -99 run function summon:encruster
execute if entity @e[tag=wm_summon_temp,tag=5,distance=0..] positioned -11216 16 -95 run function summon:encruster
execute if entity @e[tag=wm_summon_temp,tag=6,distance=0..] positioned -11214 20 -103 run function summon:encruster

kill @e[type=minecraft:area_effect_cloud,tag=wm_summon_temp,distance=0..]
