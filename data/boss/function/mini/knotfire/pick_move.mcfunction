summon area_effect_cloud -10697 54 89 {Tags:["knotfire_move_temp","1","exclude"]}
summon area_effect_cloud -10697 54 89 {Tags:["knotfire_move_temp","2","exclude"]}
summon area_effect_cloud -10697 54 89 {Tags:["knotfire_move_temp","3","exclude"]}
summon area_effect_cloud -10697 54 89 {Tags:["knotfire_move_temp","4","exclude"]}


tag @e[type=minecraft:area_effect_cloud,tag=knotfire_move_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=knotfire_move_temp,tag=exclude,distance=0..]

execute if entity @e[tag=knotfire_move_temp,tag=1,distance=0..] run function boss:mini/knotfire/attack/repo_1
execute if entity @e[tag=knotfire_move_temp,tag=2,distance=0..] run function boss:mini/knotfire/attack/repo_2
execute if entity @e[tag=knotfire_move_temp,tag=3,distance=0..] run function boss:mini/knotfire/attack/repo_3
execute if entity @e[tag=knotfire_move_temp,tag=4,distance=0..] run function boss:mini/knotfire/pick_attack


kill @e[type=minecraft:area_effect_cloud,tag=knotfire_move_temp,distance=0..]
