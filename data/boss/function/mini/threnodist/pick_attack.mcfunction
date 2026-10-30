#BIG
#FOUNTAIN
#GRAVITY
#OBSIDIAN
#LASER
#SUMMON
#REVERSE

execute unless score thren_lastattack Value matches 1 run summon area_effect_cloud -11144 55 430 {Tags:["thren_attack_temp","1","exclude"]}
execute unless score thren_lastattack Value matches 2 run summon area_effect_cloud -11144 55 430 {Tags:["thren_attack_temp","2","exclude"]}
execute unless score thren_lastattack Value matches 3 run summon area_effect_cloud -11144 55 430 {Tags:["thren_attack_temp","3","exclude"]}
execute unless score thren_lastattack Value matches 4 run summon area_effect_cloud -11144 55 430 {Tags:["thren_attack_temp","4","exclude"]}
execute unless score thren_lastattack Value matches 5 run summon area_effect_cloud -11144 55 430 {Tags:["thren_attack_temp","5","exclude"]}
execute unless entity @e[tag=d_hymnodist,distance=0..] unless score thren_lastattack Value matches 6 run summon area_effect_cloud -11144 55 430 {Tags:["thren_attack_temp","6","exclude"]}
execute unless entity @e[tag=d_hymnodist,distance=0..] unless score thren_lastattack Value matches 6 run summon area_effect_cloud -11144 55 430 {Tags:["thren_attack_temp","6","exclude"]}

execute if score thren_counter Value matches 4.. unless score thren_lastattack Value matches 7 run summon area_effect_cloud -11144 55 430 {Tags:["thren_attack_temp","7","exclude"]}
execute if score thren_counter Value matches 5.. unless score thren_lastattack Value matches 7 run summon area_effect_cloud -11144 55 430 {Tags:["thren_attack_temp","7","exclude"]}
execute if score thren_counter Value matches 5.. unless score thren_lastattack Value matches 7 run summon area_effect_cloud -11144 55 430 {Tags:["thren_attack_temp","7","exclude"]}
execute if score thren_counter Value matches 6.. unless score thren_lastattack Value matches 7 run summon area_effect_cloud -11144 55 430 {Tags:["thren_attack_temp","7","exclude"]}
execute if score thren_counter Value matches 6.. unless score thren_lastattack Value matches 7 run summon area_effect_cloud -11144 55 430 {Tags:["thren_attack_temp","7","exclude"]}
execute if score thren_counter Value matches 6.. unless score thren_lastattack Value matches 7 run summon area_effect_cloud -11144 55 430 {Tags:["thren_attack_temp","7","exclude"]}


tag @e[type=minecraft:area_effect_cloud,tag=thren_attack_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=thren_attack_temp,tag=exclude,distance=0..]

execute if entity @e[tag=thren_attack_temp,tag=1,distance=0..] run function boss:mini/threnodist/attack/do_big
execute if entity @e[tag=thren_attack_temp,tag=1,distance=0..] run scoreboard players set thren_lastattack Value 1
execute if entity @e[tag=thren_attack_temp,tag=2,distance=0..] run function boss:mini/threnodist/attack/do_fountain
execute if entity @e[tag=thren_attack_temp,tag=2,distance=0..] run scoreboard players set thren_lastattack Value 2
execute if entity @e[tag=thren_attack_temp,tag=3,distance=0..] run function boss:mini/threnodist/attack/do_gravity_center
execute if entity @e[tag=thren_attack_temp,tag=3,distance=0..] run scoreboard players set thren_lastattack Value 3
execute if entity @e[tag=thren_attack_temp,tag=4,distance=0..] run function boss:mini/threnodist/attack/do_obsidian
execute if entity @e[tag=thren_attack_temp,tag=4,distance=0..] run scoreboard players set thren_lastattack Value 4
execute if entity @e[tag=thren_attack_temp,tag=5,distance=0..] run function boss:mini/threnodist/attack/do_laser
execute if entity @e[tag=thren_attack_temp,tag=5,distance=0..] run scoreboard players set thren_lastattack Value 5
execute if entity @e[tag=thren_attack_temp,tag=6,distance=0..] run function boss:mini/threnodist/attack/do_summon
execute if entity @e[tag=thren_attack_temp,tag=6,distance=0..] run scoreboard players set thren_lastattack Value 6
execute if entity @e[tag=thren_attack_temp,tag=7,distance=0..] run function boss:mini/threnodist/attack/do_reverse
execute if entity @e[tag=thren_attack_temp,tag=7,distance=0..] run scoreboard players set thren_lastattack Value 7

kill @e[type=minecraft:area_effect_cloud,tag=thren_attack_temp,distance=0..]

scoreboard players add thren_counter Value 1
