summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","1","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","1","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","2","exclude"]}

execute if score boss:attestor BossHealth < boss:attestor_two_thirds BossHealth run kill @e[type=minecraft:area_effect_cloud,tag=attestor_temp,distance=0..]
execute if score boss:attestor BossHealth < boss:attestor_two_thirds BossHealth run summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","3","exclude"]}
execute if score boss:attestor BossHealth < boss:attestor_two_thirds BossHealth run summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","3","exclude"]}
execute if score boss:attestor BossHealth < boss:attestor_two_thirds BossHealth run summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","4","exclude"]}

execute if score boss:attestor BossHealth < boss:attestor_third BossHealth run kill @e[type=minecraft:area_effect_cloud,tag=attestor_temp,distance=0..]
execute if score boss:attestor BossHealth < boss:attestor_third BossHealth run summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","5","exclude"]}
execute if score boss:attestor BossHealth < boss:attestor_third BossHealth run summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","5","exclude"]}
execute if score boss:attestor BossHealth < boss:attestor_third BossHealth run summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","6","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=attestor_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=attestor_temp,tag=exclude,distance=0..]

execute if entity @e[tag=attestor_temp,tag=1,distance=0..] run setblock -10699 123 -251 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=2,distance=0..] run setblock -10701 123 -251 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=3,distance=0..] run setblock -10699 127 -251 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=4,distance=0..] run setblock -10701 127 -251 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=5,distance=0..] run setblock -10699 131 -251 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=6,distance=0..] run setblock -10701 131 -251 minecraft:redstone_block

kill @e[type=minecraft:area_effect_cloud,tag=attestor_temp,distance=0..]
