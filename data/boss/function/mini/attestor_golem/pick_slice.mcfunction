summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","1","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","2","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","3","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","4","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","5","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","6","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","7","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","8","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","9","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","10","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","11","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","12","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","13","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","14","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","15","exclude"]}
summon area_effect_cloud -10691 123 -269 {Tags:["attestor_temp","16","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=attestor_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=attestor_temp,tag=exclude,distance=0..]

execute if entity @e[tag=attestor_temp,tag=1,distance=0..] run setblock -10687 123 -265 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=2,distance=0..] run setblock -10687 123 -263 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=3,distance=0..] run setblock -10687 123 -261 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=4,distance=0..] run setblock -10687 123 -259 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=5,distance=0..] run setblock -10687 123 -257 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=6,distance=0..] run setblock -10687 123 -255 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=7,distance=0..] run setblock -10687 123 -253 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=8,distance=0..] run setblock -10687 123 -251 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=9,distance=0..] run setblock -10694 123 -265 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=10,distance=0..] run setblock -10694 123 -263 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=11,distance=0..] run setblock -10694 123 -261 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=12,distance=0..] run setblock -10694 123 -259 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=13,distance=0..] run setblock -10694 123 -257 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=14,distance=0..] run setblock -10694 123 -255 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=15,distance=0..] run setblock -10694 123 -253 minecraft:redstone_block
execute if entity @e[tag=attestor_temp,tag=16,distance=0..] run setblock -10694 123 -251 minecraft:redstone_block

kill @e[type=minecraft:area_effect_cloud,tag=attestor_temp,distance=0..]

playsound minecraft:entity.iron_golem.damage hostile @a[tag=mg.flw] -10720 109 -260 2 0.1
