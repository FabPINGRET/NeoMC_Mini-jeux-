summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","1","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","2","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","3","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","4","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","5","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","6","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=attestor_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=attestor_temp,tag=exclude,distance=0..]

execute if entity @e[tag=attestor_temp,tag=1,distance=0..] run setblock -10687 132 -261 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=2,distance=0..] run setblock -10687 132 -259 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=3,distance=0..] run setblock -10687 132 -257 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=4,distance=0..] run setblock -10687 132 -255 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=5,distance=0..] run setblock -10687 132 -253 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=6,distance=0..] run setblock -10687 132 -251 minecraft:redstone_block

kill @e[type=minecraft:area_effect_cloud,tag=attestor_temp,distance=0..]

playsound minecraft:entity.iron_golem.damage hostile @a[tag=mg.flw] -10720 109 -260 2 0.1
