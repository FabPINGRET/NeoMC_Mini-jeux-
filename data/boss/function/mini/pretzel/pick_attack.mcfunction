execute unless score pretzel_lastattack Value matches 0 unless score pretzel_lastattack Value matches 3 run function boss:mini/pretzel/open_box_remark
execute if score pretzel_lastattack Value matches 3 run function boss:mini/pretzel/retreat_remark

execute if score pretzel_lastattack Value matches 0 positioned -10341 89 445 run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute if score pretzel_lastattack Value matches 0 run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Pretzel Jenkins","color":"red"},{"text":"> Opening it now, here it goes!","color":"white"}]

execute unless score pretzel_lastattack Value matches 1 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","1","exclude"]}
execute unless score pretzel_lastattack Value matches 2 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","2","exclude"]}
execute unless score pretzel_since_sword Value matches 0..3 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..4 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..5 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..5 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..6 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..6 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..6 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..7 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..7 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..7 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..7 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..8 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..8 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..8 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..8 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless score pretzel_since_sword Value matches 0..8 unless score pretzel_lastattack Value matches 3 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","3","exclude"]}
execute unless entity @e[tag=pretzel_rabbit,distance=0..] unless score pretzel_lastattack Value matches 4 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","4","exclude"]}
execute unless entity @e[tag=pretzel_pufferfish,distance=0..] unless score pretzel_lastattack Value matches 5 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","5","exclude"]}
execute unless score pretzel_lastattack Value matches 6 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","6","exclude"]}
execute unless score pretzel_lastattack Value matches 7 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","7","exclude"]}
execute unless score pretzel_lastattack Value matches 8 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","8","exclude"]}
execute unless score pretzel_lastattack Value matches 9 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","9","exclude"]}
execute unless score pretzel_lastattack Value matches 10 run summon area_effect_cloud -10340 79 446 {Tags:["pretzel_attack_temp","10","exclude"]}


tag @e[type=minecraft:area_effect_cloud,tag=pretzel_attack_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=pretzel_attack_temp,tag=exclude,distance=0..]

execute if entity @e[tag=pretzel_attack_temp,tag=1,distance=0..] run schedule function floaty:sched/boss/mini/pretzel/rig/potion 30t replace
execute if entity @e[tag=pretzel_attack_temp,tag=1,distance=0..] run scoreboard players set pretzel_lastattack Value 1
execute if entity @e[tag=pretzel_attack_temp,tag=2,distance=0..] run schedule function floaty:sched/boss/mini/pretzel/rig/shotgun 30t replace
execute if entity @e[tag=pretzel_attack_temp,tag=2,distance=0..] run scoreboard players set pretzel_lastattack Value 2
execute if entity @e[tag=pretzel_attack_temp,tag=3,distance=0..] run schedule function floaty:sched/boss/mini/pretzel/rig/sword 30t replace
execute if entity @e[tag=pretzel_attack_temp,tag=3,distance=0..] run scoreboard players set pretzel_lastattack Value 3
execute if entity @e[tag=pretzel_attack_temp,tag=4,distance=0..] run schedule function floaty:sched/boss/mini/pretzel/rig/carrot 30t replace
execute if entity @e[tag=pretzel_attack_temp,tag=4,distance=0..] run scoreboard players set pretzel_lastattack Value 4
execute if entity @e[tag=pretzel_attack_temp,tag=5,distance=0..] run schedule function floaty:sched/boss/mini/pretzel/rig/pufferfish 30t replace
execute if entity @e[tag=pretzel_attack_temp,tag=5,distance=0..] run scoreboard players set pretzel_lastattack Value 5
execute if entity @e[tag=pretzel_attack_temp,tag=6,distance=0..] run schedule function floaty:sched/boss/mini/pretzel/rig/string 30t replace
execute if entity @e[tag=pretzel_attack_temp,tag=6,distance=0..] run scoreboard players set pretzel_lastattack Value 6
execute if entity @e[tag=pretzel_attack_temp,tag=7,distance=0..] run schedule function floaty:sched/boss/mini/pretzel/rig/turtle 30t replace
execute if entity @e[tag=pretzel_attack_temp,tag=7,distance=0..] run scoreboard players set pretzel_lastattack Value 7
execute if entity @e[tag=pretzel_attack_temp,tag=8,distance=0..] run schedule function floaty:sched/boss/mini/pretzel/rig/book 30t replace
execute if entity @e[tag=pretzel_attack_temp,tag=8,distance=0..] run scoreboard players set pretzel_lastattack Value 8
execute if entity @e[tag=pretzel_attack_temp,tag=9,distance=0..] run schedule function floaty:sched/boss/mini/pretzel/rig/brick 30t replace
execute if entity @e[tag=pretzel_attack_temp,tag=9,distance=0..] run scoreboard players set pretzel_lastattack Value 9
execute if entity @e[tag=pretzel_attack_temp,tag=10,distance=0..] run schedule function floaty:sched/boss/mini/pretzel/rig/emerald 30t replace
execute if entity @e[tag=pretzel_attack_temp,tag=10,distance=0..] run scoreboard players set pretzel_lastattack Value 10

kill @e[type=minecraft:area_effect_cloud,tag=pretzel_attack_temp,distance=0..]

scoreboard players add pretzel_since_sword Value 1
