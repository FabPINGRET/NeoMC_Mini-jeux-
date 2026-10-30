kill @e[tag=deebo_arrow,type=arrow,distance=0..]
kill @e[tag=deebo_trident,type=trident,distance=0..]

execute unless score deebo_lastattack Value matches 1 run summon area_effect_cloud -11538 175 -183 {Tags:["deebo_attack_temp","1","exclude"]}
execute unless score deebo_lastattack Value matches 2 run summon area_effect_cloud -11538 175 -183 {Tags:["deebo_attack_temp","2","exclude"]}
execute unless score deebo_lastattack Value matches 3 run summon area_effect_cloud -11538 175 -183 {Tags:["deebo_attack_temp","3","exclude"]}
execute unless score deebo_lastattack Value matches 4 unless entity @e[tag=smearblin,distance=0..] run summon area_effect_cloud -11538 175 -183 {Tags:["deebo_attack_temp","4","exclude"]}
execute if block -11549 173 -171 red_wool run summon area_effect_cloud -11538 175 -183 {Tags:["deebo_attack_temp","5","exclude"]}
execute if block -11549 173 -171 red_wool run summon area_effect_cloud -11538 175 -183 {Tags:["deebo_attack_temp","5","exclude"]}


tag @e[type=minecraft:area_effect_cloud,tag=deebo_attack_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=deebo_attack_temp,tag=exclude,distance=0..]

execute if entity @e[tag=deebo_attack_temp,tag=1,distance=0..] run function boss:mini/dark_eebo/attack/trident_start
execute if entity @e[tag=deebo_attack_temp,tag=1,distance=0..] run scoreboard players set deebo_lastattack Value 1
execute if entity @e[tag=deebo_attack_temp,tag=2,distance=0..] run function boss:mini/dark_eebo/attack/poison_start
execute if entity @e[tag=deebo_attack_temp,tag=2,distance=0..] run scoreboard players set deebo_lastattack Value 2
execute if entity @e[tag=deebo_attack_temp,tag=3,distance=0..] run function boss:mini/dark_eebo/attack/crossbow_start
execute if entity @e[tag=deebo_attack_temp,tag=3,distance=0..] run scoreboard players set deebo_lastattack Value 3
execute if entity @e[tag=deebo_attack_temp,tag=4,distance=0..] run function boss:mini/dark_eebo/attack/summon_start
execute if entity @e[tag=deebo_attack_temp,tag=4,distance=0..] run scoreboard players set deebo_lastattack Value 4
execute if entity @e[tag=deebo_attack_temp,tag=5,distance=0..] run function boss:mini/dark_eebo/attack/deebo_out_start
execute if entity @e[tag=deebo_attack_temp,tag=5,distance=0..] run scoreboard players set deebo_lastattack Value 5

kill @e[type=minecraft:area_effect_cloud,tag=deebo_attack_temp,distance=0..]

execute if block -11549 173 -171 green_wool run setblock -11549 173 -171 minecraft:red_wool
execute if block -11549 173 -171 blue_wool run setblock -11549 173 -171 minecraft:green_wool
execute if block -11549 173 -171 black_wool run setblock -11549 173 -171 minecraft:blue_wool
