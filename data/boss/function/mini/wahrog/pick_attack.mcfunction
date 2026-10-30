#WAVE
#SUBSURFACE
#TRIDENT
#SUMMON
#FORKING

execute unless score wahrog_lastattack Value matches 1 run summon area_effect_cloud -11146 40 332 {Tags:["wahrog_attack_temp","1","exclude"]}
execute unless score wahrog_lastattack Value matches 1 run summon area_effect_cloud -11146 40 332 {Tags:["wahrog_attack_temp","1","exclude"]}

execute if score wahrog_counter Value matches 3.. unless score wahrog_lastattack Value matches 2 run summon area_effect_cloud -11146 40 332 {Tags:["wahrog_attack_temp","2","exclude"]}
execute if score wahrog_counter Value matches 4.. unless score wahrog_lastattack Value matches 2 run summon area_effect_cloud -11146 40 332 {Tags:["wahrog_attack_temp","2","exclude"]}
execute if score wahrog_counter Value matches 5.. unless score wahrog_lastattack Value matches 2 run summon area_effect_cloud -11146 40 332 {Tags:["wahrog_attack_temp","2","exclude"]}
execute if score wahrog_counter Value matches 6.. unless score wahrog_lastattack Value matches 2 run summon area_effect_cloud -11146 40 332 {Tags:["wahrog_attack_temp","2","exclude"]}
execute if score wahrog_counter Value matches 7.. unless score wahrog_lastattack Value matches 2 run summon area_effect_cloud -11146 40 332 {Tags:["wahrog_attack_temp","2","exclude"]}
execute if score wahrog_counter Value matches 8.. unless score wahrog_lastattack Value matches 2 run summon area_effect_cloud -11146 40 332 {Tags:["wahrog_attack_temp","2","exclude"]}

execute unless score wahrog_lastattack Value matches 3 run summon area_effect_cloud -11146 40 332 {Tags:["wahrog_attack_temp","3","exclude"]}
execute unless score wahrog_lastattack Value matches 3 run summon area_effect_cloud -11146 40 332 {Tags:["wahrog_attack_temp","3","exclude"]}
execute unless entity @e[tag=c_parasite,distance=0..] unless score wahrog_lastattack Value matches 4 run summon area_effect_cloud -11146 40 332 {Tags:["wahrog_attack_temp","4","exclude"]}
execute unless entity @e[tag=c_parasite,distance=0..] unless score wahrog_lastattack Value matches 4 run summon area_effect_cloud -11146 40 332 {Tags:["wahrog_attack_temp","4","exclude"]}
execute unless score wahrog_lastattack Value matches 5 run summon area_effect_cloud -11146 40 332 {Tags:["wahrog_attack_temp","5","exclude"]}
execute unless score wahrog_lastattack Value matches 5 run summon area_effect_cloud -11146 40 332 {Tags:["wahrog_attack_temp","5","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=wahrog_attack_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=wahrog_attack_temp,tag=exclude,distance=0..]

execute if block -11146 83 332 light[level=15,waterlogged=false] if entity @e[tag=wahrog_attack_temp,tag=1,distance=0..] run function boss:mini/wahrog/attack/do_wave
execute if block -11146 83 332 light[level=15,waterlogged=true] if entity @e[tag=wahrog_attack_temp,tag=1,distance=0..] run function boss:mini/wahrog/attack/do_wave_wet
execute if entity @e[tag=wahrog_attack_temp,tag=1,distance=0..] run scoreboard players set wahrog_lastattack Value 1
execute if entity @e[tag=wahrog_attack_temp,tag=2,distance=0..] run function boss:mini/wahrog/attack/do_subsurface
execute if entity @e[tag=wahrog_attack_temp,tag=2,distance=0..] run scoreboard players set wahrog_lastattack Value 2
execute if entity @e[tag=wahrog_attack_temp,tag=3,distance=0..] run function boss:mini/wahrog/attack/do_trident
execute if entity @e[tag=wahrog_attack_temp,tag=3,distance=0..] run scoreboard players set wahrog_lastattack Value 3
execute if entity @e[tag=wahrog_attack_temp,tag=4,distance=0..] run function boss:mini/wahrog/attack/do_summon
execute if entity @e[tag=wahrog_attack_temp,tag=4,distance=0..] run scoreboard players set wahrog_lastattack Value 4
execute if entity @e[tag=wahrog_attack_temp,tag=4,distance=0..] run scoreboard players remove wahrog_counter Value 1
execute if entity @e[tag=wahrog_attack_temp,tag=5,distance=0..] run function boss:mini/wahrog/attack/do_forking
execute if entity @e[tag=wahrog_attack_temp,tag=5,distance=0..] run scoreboard players set wahrog_lastattack Value 5

kill @e[type=minecraft:area_effect_cloud,tag=wahrog_attack_temp,distance=0..]

scoreboard players add wahrog_counter Value 1
