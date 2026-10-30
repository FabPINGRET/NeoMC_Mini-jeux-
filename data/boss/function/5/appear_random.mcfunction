execute unless entity @e[tag=boss_skt_hole_2,tag=boss_skt_hole_last,distance=0..] run summon area_effect_cloud -10222 54 434 {Tags:["skt_appear_temp","2","exclude"]}
execute unless entity @e[tag=boss_skt_hole_3,tag=boss_skt_hole_last,distance=0..] run summon area_effect_cloud -10222 54 434 {Tags:["skt_appear_temp","3","exclude"]}
execute unless entity @e[tag=boss_skt_hole_4,tag=boss_skt_hole_last,distance=0..] run summon area_effect_cloud -10222 54 434 {Tags:["skt_appear_temp","4","exclude"]}
execute unless entity @e[tag=boss_skt_hole_5,tag=boss_skt_hole_last,distance=0..] run summon area_effect_cloud -10222 54 434 {Tags:["skt_appear_temp","5","exclude"]}
execute unless entity @e[tag=boss_skt_hole_6,tag=boss_skt_hole_last,distance=0..] run summon area_effect_cloud -10222 54 434 {Tags:["skt_appear_temp","6","exclude"]}
execute unless entity @e[tag=boss_skt_hole_7,tag=boss_skt_hole_last,distance=0..] run summon area_effect_cloud -10222 54 434 {Tags:["skt_appear_temp","7","exclude"]}
execute unless entity @e[tag=boss_skt_hole_8,tag=boss_skt_hole_last,distance=0..] run summon area_effect_cloud -10222 54 434 {Tags:["skt_appear_temp","8","exclude"]}
execute unless entity @e[tag=boss_skt_hole_9,tag=boss_skt_hole_last,distance=0..] run summon area_effect_cloud -10222 54 434 {Tags:["skt_appear_temp","9","exclude"]}
execute unless entity @e[tag=boss_skt_hole_10,tag=boss_skt_hole_last,distance=0..] run summon area_effect_cloud -10222 54 434 {Tags:["skt_appear_temp","10","exclude"]}
execute unless entity @e[tag=boss_skt_hole_11,tag=boss_skt_hole_last,distance=0..] run summon area_effect_cloud -10222 54 434 {Tags:["skt_appear_temp","11","exclude"]}
execute unless entity @e[tag=boss_skt_hole_12,tag=boss_skt_hole_last,distance=0..] run summon area_effect_cloud -10222 54 434 {Tags:["skt_appear_temp","12","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=skt_appear_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=skt_appear_temp,tag=exclude,distance=0..]

execute if entity @e[tag=skt_appear_temp,tag=2,distance=0..] run function boss:5/appear/2
execute if entity @e[tag=skt_appear_temp,tag=3,distance=0..] run function boss:5/appear/3
execute if entity @e[tag=skt_appear_temp,tag=4,distance=0..] run function boss:5/appear/4
execute if entity @e[tag=skt_appear_temp,tag=5,distance=0..] run function boss:5/appear/5
execute if entity @e[tag=skt_appear_temp,tag=6,distance=0..] run function boss:5/appear/6
execute if entity @e[tag=skt_appear_temp,tag=7,distance=0..] run function boss:5/appear/7
execute if entity @e[tag=skt_appear_temp,tag=8,distance=0..] run function boss:5/appear/8
execute if entity @e[tag=skt_appear_temp,tag=9,distance=0..] run function boss:5/appear/9
execute if entity @e[tag=skt_appear_temp,tag=10,distance=0..] run function boss:5/appear/10
execute if entity @e[tag=skt_appear_temp,tag=11,distance=0..] run function boss:5/appear/11
execute if entity @e[tag=skt_appear_temp,tag=12,distance=0..] run function boss:5/appear/12

kill @e[type=minecraft:area_effect_cloud,tag=skt_appear_temp,distance=0..]

schedule function floaty:sched/boss/5/tail_to_last 0.5s replace
