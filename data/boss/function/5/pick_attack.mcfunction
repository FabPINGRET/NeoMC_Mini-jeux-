# 1 - RELOCATE
# 2 - DARK TAIL AND RELOCATE TAIL CENTER
# 3 - ECTOBEAM
# 4 - TAIL POISON
# 5 - PIRANHA PLANTS
# 6 - EVOKER FANG BITES
# 7 - SLOWNESS CLOUD BITES

execute if block -10204 55 418 minecraft:lime_wool run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","1","exclude"]}
execute if block -10204 55 418 minecraft:lime_wool run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","1","exclude"]}
execute if block -10204 55 418 minecraft:red_wool run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","1","exclude"]}
execute if block -10204 55 418 minecraft:red_wool run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","1","exclude"]}
execute if block -10204 55 418 minecraft:red_wool run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","1","exclude"]}

execute if block -10203 55 418 minecraft:red_wool run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","2","exclude"]}
execute if block -10203 55 418 minecraft:red_wool run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","2","exclude"]}
execute if block -10203 55 418 minecraft:red_wool run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","2","exclude"]}


fill -10203 55 418 -10204 55 418 minecraft:red_wool replace minecraft:lime_wool
fill -10203 55 418 -10204 55 418 minecraft:lime_wool replace minecraft:blue_wool
fill -10203 55 418 -10204 55 418 minecraft:blue_wool replace minecraft:black_wool

execute as @n[tag=boss_skt_hole_1,distance=0..] at @s if block ~ ~ ~ minecraft:lime_stained_glass run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","3","exclude"]}

execute unless score boss:skt_lastattack Value matches 4 run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","4","exclude"]}
execute unless score boss:skt_lastattack Value matches 4 run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","4","exclude"]}

execute unless score boss:skt_lastattack Value matches 5 run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","5","exclude"]}
execute unless score boss:skt_lastattack Value matches 5 run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","5","exclude"]}

execute unless score boss:skt_lastattack Value matches 6 run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","6","exclude"]}
execute unless score boss:skt_lastattack Value matches 6 run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","7","exclude"]}

execute unless entity @e[tag=cuauhtli,distance=0..] unless score boss:skt_lastattack Value matches 8 run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","8","exclude"]}
execute unless entity @e[tag=cuauhtli,distance=0..] unless score boss:skt_lastattack Value matches 8 run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","8","exclude"]}
execute unless entity @e[tag=cuauhtli,distance=0..] unless score boss:skt_lastattack Value matches 8 run summon area_effect_cloud -10222 54 434 {Tags:["skt_attack_temp","8","exclude"]}

execute as @n[tag=boss_skt_hole_1,distance=0..] at @s if block ~ ~ ~ minecraft:lime_stained_glass run kill @e[tag=skt_attack_temp,tag=!3,type=area_effect_cloud,distance=0..]

tag @e[type=minecraft:area_effect_cloud,tag=skt_attack_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=skt_attack_temp,tag=exclude,distance=0..]

execute if entity @e[tag=skt_attack_temp,tag=1,distance=0..] run function boss:5/reposition
execute if entity @e[tag=skt_attack_temp,tag=2,distance=0..] run function boss:5/tail_dark_start
execute if entity @e[tag=skt_attack_temp,tag=3,distance=0..] run function boss:5/ectobeam/attack_start
execute if entity @e[tag=skt_attack_temp,tag=4,distance=0..] run function boss:5/tail_poison_start
execute if entity @e[tag=skt_attack_temp,tag=5,distance=0..] run function boss:5/debris_macro
execute if entity @e[tag=skt_attack_temp,tag=6,distance=0..] run setblock -10196 55 423 minecraft:redstone_block
execute if entity @e[tag=skt_attack_temp,tag=7,distance=0..] run setblock -10198 55 423 minecraft:redstone_block
execute if entity @e[tag=skt_attack_temp,tag=8,distance=0..] run function boss:5/summon_start

execute if entity @e[tag=skt_attack_temp,tag=1,distance=0..] run scoreboard players set boss:skt_lastattack Value 1
execute if entity @e[tag=skt_attack_temp,tag=2,distance=0..] run scoreboard players set boss:skt_lastattack Value 2
execute if entity @e[tag=skt_attack_temp,tag=3,distance=0..] run scoreboard players set boss:skt_lastattack Value 3
execute if entity @e[tag=skt_attack_temp,tag=4,distance=0..] run scoreboard players set boss:skt_lastattack Value 4
execute if entity @e[tag=skt_attack_temp,tag=5,distance=0..] run scoreboard players set boss:skt_lastattack Value 5
execute if entity @e[tag=skt_attack_temp,tag=6,distance=0..] run scoreboard players set boss:skt_lastattack Value 6
execute if entity @e[tag=skt_attack_temp,tag=7,distance=0..] run scoreboard players set boss:skt_lastattack Value 6
execute if entity @e[tag=skt_attack_temp,tag=8,distance=0..] run scoreboard players set boss:skt_lastattack Value 8

#execute if entity @e[tag=skt_attack_temp,tag=1] run say REPOSITION
#execute if entity @e[tag=skt_attack_temp,tag=2] run say DARK TAIL
#execute if entity @e[tag=skt_attack_temp,tag=3] run say ECTO
#execute if entity @e[tag=skt_attack_temp,tag=4] run say TAIL POISON
#execute if entity @e[tag=skt_attack_temp,tag=5] run say PIRANHAS
#execute if entity @e[tag=skt_attack_temp,tag=6] run say EVOKER FANGS
#execute if entity @e[tag=skt_attack_temp,tag=7] run say SLOW FANGS
#execute if entity @e[tag=skt_attack_temp,tag=8] run say SUMMON

kill @e[type=minecraft:area_effect_cloud,tag=skt_attack_temp,distance=0..]
