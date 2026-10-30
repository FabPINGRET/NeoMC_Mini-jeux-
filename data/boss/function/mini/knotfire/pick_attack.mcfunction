execute unless score knotfire_lastattack Value matches 1 run summon area_effect_cloud -10697 54 89 {Tags:["knotfire_attack_temp","1","exclude"]}
execute unless score knotfire_lastattack Value matches 2 run summon area_effect_cloud -10697 54 89 {Tags:["knotfire_attack_temp","2","exclude"]}
summon area_effect_cloud -10697 54 89 {Tags:["knotfire_attack_temp","3","exclude"]}
summon area_effect_cloud -10697 54 89 {Tags:["knotfire_attack_temp","3","exclude"]}
execute unless score knotfire_lastattack Value matches 4 run summon area_effect_cloud -10697 54 89 {Tags:["knotfire_attack_temp","4","exclude"]}


tag @e[type=minecraft:area_effect_cloud,tag=knotfire_attack_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=knotfire_attack_temp,tag=exclude,distance=0..]

execute if entity @e[tag=knotfire_attack_temp,tag=1,distance=0..] run function boss:mini/knotfire/attack/do_gift
execute if entity @e[tag=knotfire_attack_temp,tag=1,distance=0..] run scoreboard players set knotfire_lastattack Value 1
execute if entity @e[tag=knotfire_attack_temp,tag=2,distance=0..] run function boss:mini/knotfire/attack/do_fireball
execute if entity @e[tag=knotfire_attack_temp,tag=2,distance=0..] run scoreboard players set knotfire_lastattack Value 2
execute if entity @e[tag=knotfire_attack_temp,tag=3,distance=0..] run function boss:mini/knotfire/attack/do_run
execute if entity @e[tag=knotfire_attack_temp,tag=3,distance=0..] run scoreboard players set knotfire_lastattack Value 3
execute if entity @e[tag=knotfire_attack_temp,tag=4,distance=0..] run function boss:mini/knotfire/attack/do_rain
execute if entity @e[tag=knotfire_attack_temp,tag=4,distance=0..] run scoreboard players set knotfire_lastattack Value 4

kill @e[type=minecraft:area_effect_cloud,tag=knotfire_attack_temp,distance=0..]
