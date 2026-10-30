#SWORD SPIKE
#EYE LASER
#SWORD CHOP
#STAB 3 TIMES
#CENTER PLATFORM CLEAR
#WITHER SKULLS FROM SMALL ARM
#SUMMON MUTARID FIRECASTERS
#LIGHTNING AND WITHER ZONES


execute if score wv_alive bool matches 1 unless score wv_lastattack Value matches 1 run summon area_effect_cloud -12384 110 355 {Tags:["wv_attack_temp","1","exclude"]}
execute if score wv_alive bool matches 1 unless score wv_lastattack Value matches 2 run summon area_effect_cloud -12384 110 355 {Tags:["wv_attack_temp","2","exclude"]}
execute if score wv_alive bool matches 1 unless score wv_lastattack Value matches 3 run summon area_effect_cloud -12384 110 355 {Tags:["wv_attack_temp","3","exclude"]}
execute if score wv_alive bool matches 1 unless score wv_lastattack Value matches 4 run summon area_effect_cloud -12384 110 355 {Tags:["wv_attack_temp","4","exclude"]}
execute if score wv_alive bool matches 1 unless score wv_lastattack Value matches 6 run summon area_effect_cloud -12384 110 355 {Tags:["wv_attack_temp","6","exclude"]}
execute if score wv_alive bool matches 1 unless score wv_lastattack Value matches 7 unless entity @e[tag=m_caster,distance=0..] run summon area_effect_cloud -12384 110 355 {Tags:["wv_attack_temp","7","exclude"]}
execute if score wv_alive bool matches 1 unless score wv_lastattack Value matches 7 unless entity @e[tag=m_caster,distance=0..] run summon area_effect_cloud -12384 110 355 {Tags:["wv_attack_temp","7","exclude"]}
execute if score wv_alive bool matches 1 unless score wv_lastattack Value matches 7 unless entity @e[tag=m_caster,distance=0..] run summon area_effect_cloud -12384 110 355 {Tags:["wv_attack_temp","7","exclude"]}
execute if score wv_alive bool matches 1 unless score wv_lastattack Value matches 8 run summon area_effect_cloud -12384 110 355 {Tags:["wv_attack_temp","8","exclude"]}


#force center clear if they're in the middle
execute if score wv_alive bool matches 1 positioned -12384 123 355 if entity @a[distance=..10,gamemode=!spectator,tag=mg.flw] run kill @e[type=minecraft:area_effect_cloud,tag=wv_attack_temp,distance=0..]
execute if score wv_alive bool matches 1 positioned -12384 123 355 if entity @a[distance=..10,gamemode=!spectator,tag=mg.flw] run summon area_effect_cloud -12384 110 355 {Tags:["wv_attack_temp","5","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=wv_attack_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=wv_attack_temp,tag=exclude,distance=0..]

execute if score wv_alive bool matches 1 if entity @e[tag=wv_attack_temp,tag=1,distance=0..] run function boss:final/virus/attack/do_spike
execute if entity @e[tag=wv_attack_temp,tag=1,distance=0..] run scoreboard players set wv_lastattack Value 1
execute if score wv_alive bool matches 1 if entity @e[tag=wv_attack_temp,tag=2,distance=0..] run function boss:final/virus/attack/do_eyelaser
execute if entity @e[tag=wv_attack_temp,tag=2,distance=0..] run scoreboard players set wv_lastattack Value 2
execute if score wv_alive bool matches 1 if entity @e[tag=wv_attack_temp,tag=3,distance=0..] run function boss:final/virus/attack/do_chop
execute if entity @e[tag=wv_attack_temp,tag=3,distance=0..] run scoreboard players set wv_lastattack Value 3
execute if score wv_alive bool matches 1 if entity @e[tag=wv_attack_temp,tag=4,distance=0..] run function boss:final/virus/attack/do_stab
execute if entity @e[tag=wv_attack_temp,tag=4,distance=0..] run scoreboard players set wv_lastattack Value 4
execute if score wv_alive bool matches 1 if entity @e[tag=wv_attack_temp,tag=5,distance=0..] run function boss:final/virus/attack/do_center_clear
execute if entity @e[tag=wv_attack_temp,tag=5,distance=0..] run scoreboard players set wv_lastattack Value 5
execute if score wv_alive bool matches 1 if entity @e[tag=wv_attack_temp,tag=6,distance=0..] run function boss:final/virus/attack/do_skulls
execute if entity @e[tag=wv_attack_temp,tag=6,distance=0..] run scoreboard players set wv_lastattack Value 6
execute if score wv_alive bool matches 1 if entity @e[tag=wv_attack_temp,tag=7,distance=0..] run function boss:final/virus/attack/do_summon
execute if entity @e[tag=wv_attack_temp,tag=7,distance=0..] run scoreboard players set wv_lastattack Value 7
execute if score wv_alive bool matches 1 if entity @e[tag=wv_attack_temp,tag=8,distance=0..] run function boss:final/virus/attack/do_lightning
execute if entity @e[tag=wv_attack_temp,tag=8,distance=0..] run scoreboard players set wv_lastattack Value 8

kill @e[type=minecraft:area_effect_cloud,tag=wv_attack_temp,distance=0..]
