summon area_effect_cloud -11830 200 330 {Tags:["ta_head_order_temp","1","exclude"]}
summon area_effect_cloud -11830 200 330 {Tags:["ta_head_order_temp","2","exclude"]}
summon area_effect_cloud -11830 200 330 {Tags:["ta_head_order_temp","3","exclude"]}
summon area_effect_cloud -11830 200 330 {Tags:["ta_head_order_temp","4","exclude"]}


tag @e[type=minecraft:area_effect_cloud,tag=ta_head_order_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=ta_head_order_temp,tag=exclude,distance=0..]

execute if entity @e[tag=ta_head_order_temp,tag=1,distance=0..] run function boss:10/head_order/rictus
execute if entity @e[tag=ta_head_order_temp,tag=2,distance=0..] run function boss:10/head_order/wailing
execute if entity @e[tag=ta_head_order_temp,tag=3,distance=0..] run function boss:10/head_order/scornful
execute if entity @e[tag=ta_head_order_temp,tag=4,distance=0..] run function boss:10/head_order/cackling

kill @e[type=minecraft:area_effect_cloud,tag=ta_head_order_temp,distance=0..]
