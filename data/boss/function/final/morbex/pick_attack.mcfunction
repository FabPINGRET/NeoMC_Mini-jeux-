#LASER
#TRIDENT
#SUNRAY
#HONEYWAVE
#SUMMON
#SPINNING SWORDS

execute unless score morbex_lastattack Value matches 1 run summon area_effect_cloud -12384 110 355 {Tags:["morbex_attack_temp","1","exclude"]}
execute unless score morbex_lastattack Value matches 2 run summon area_effect_cloud -12384 110 355 {Tags:["morbex_attack_temp","2","exclude"]}
execute unless score morbex_lastattack Value matches 3 run summon area_effect_cloud -12384 110 355 {Tags:["morbex_attack_temp","3","exclude"]}
execute unless score morbex_lastattack Value matches 4 run summon area_effect_cloud -12384 110 355 {Tags:["morbex_attack_temp","4","exclude"]}
execute unless score morbex_lastattack Value matches 5 unless entity @e[tag=mutarid_strong,distance=0..] run summon area_effect_cloud -12384 110 355 {Tags:["morbex_attack_temp","5","exclude"]}
execute unless score morbex_lastattack Value matches 6 if block -12346 42 338 red_wool run summon area_effect_cloud -12384 110 355 {Tags:["morbex_attack_temp","6","exclude"]}
execute unless score morbex_lastattack Value matches 6 if block -12346 42 338 red_wool run summon area_effect_cloud -12384 110 355 {Tags:["morbex_attack_temp","6","exclude"]}
execute unless score morbex_lastattack Value matches 6 if block -12346 42 338 pink_wool run summon area_effect_cloud -12384 110 355 {Tags:["morbex_attack_temp","6","exclude"]}
execute unless score morbex_lastattack Value matches 6 if block -12346 42 338 pink_wool run summon area_effect_cloud -12384 110 355 {Tags:["morbex_attack_temp","6","exclude"]}
execute unless score morbex_lastattack Value matches 6 if block -12346 42 338 pink_wool run summon area_effect_cloud -12384 110 355 {Tags:["morbex_attack_temp","6","exclude"]}
execute unless score morbex_lastattack Value matches 6 if block -12346 42 338 pink_wool run summon area_effect_cloud -12384 110 355 {Tags:["morbex_attack_temp","6","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=morbex_attack_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=morbex_attack_temp,tag=exclude,distance=0..]

execute if entity @e[tag=morbex_attack_temp,tag=1,distance=0..] run function boss:final/morbex/attack/do_laser
execute if entity @e[tag=morbex_attack_temp,tag=1,distance=0..] run scoreboard players set morbex_lastattack Value 1
execute if entity @e[tag=morbex_attack_temp,tag=2,distance=0..] run function boss:final/morbex/attack/do_trident
execute if entity @e[tag=morbex_attack_temp,tag=2,distance=0..] run scoreboard players set morbex_lastattack Value 2
execute if entity @e[tag=morbex_attack_temp,tag=3,distance=0..] run function boss:final/morbex/attack/do_sunray
execute if entity @e[tag=morbex_attack_temp,tag=3,distance=0..] run scoreboard players set morbex_lastattack Value 3
execute if entity @e[tag=morbex_attack_temp,tag=4,distance=0..] run function boss:final/morbex/attack/do_honeywave
execute if entity @e[tag=morbex_attack_temp,tag=4,distance=0..] run scoreboard players set morbex_lastattack Value 4
execute if entity @e[tag=morbex_attack_temp,tag=5,distance=0..] run function boss:final/morbex/attack/do_summon
execute if entity @e[tag=morbex_attack_temp,tag=5,distance=0..] run scoreboard players set morbex_lastattack Value 5
execute if entity @e[tag=morbex_attack_temp,tag=6,distance=0..] run function boss:final/morbex/attack/do_spinning_swords
execute if entity @e[tag=morbex_attack_temp,tag=6,distance=0..] run scoreboard players set morbex_lastattack Value 6

kill @e[type=minecraft:area_effect_cloud,tag=morbex_attack_temp,distance=0..]

execute if block -12346 42 338 red_wool run setblock -12346 42 338 minecraft:pink_wool
execute if block -12346 42 338 lime_wool run setblock -12346 42 338 minecraft:red_wool
execute if block -12346 42 338 blue_wool run setblock -12346 42 338 minecraft:lime_wool
execute if block -12346 42 338 black_wool run setblock -12346 42 338 minecraft:blue_wool
