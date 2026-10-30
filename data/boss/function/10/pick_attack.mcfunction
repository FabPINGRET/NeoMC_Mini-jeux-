#say picking attack

#tag @a remove targeted
#execute unless entity @a[tag=bossroom,tag=targeted] run tag @r[tag=bossroom,gamemode=!spectator] add targeted

# 1 RICTUS - CHARGE
# 2 WAILING - ARROW CLAWS
# 3 SCORNFUL - LASERS
# 4 CACKLING - SUMMON

execute unless score boss:ta_lastattack Value matches 1 run summon area_effect_cloud -11830 200 330 {Tags:["ta_attack_temp","1","exclude"]}
execute unless score boss:ta_lastattack Value matches 2 run summon area_effect_cloud -11830 200 330 {Tags:["ta_attack_temp","2","exclude"]}
execute unless score boss:ta_lastattack Value matches 3 run summon area_effect_cloud -11830 200 330 {Tags:["ta_attack_temp","3","exclude"]}
execute unless entity @e[tag=l_soul,distance=0..] unless score boss:ta_lastattack Value matches 4 run summon area_effect_cloud -11830 200 330 {Tags:["ta_attack_temp","4","exclude"]}


#DEFAULT ATTACK
execute unless entity @e[tag=ta_attack_temp,type=area_effect_cloud,distance=0..] run summon area_effect_cloud -11830 200 330 {Tags:["ta_attack_temp","1","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=ta_attack_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=ta_attack_temp,tag=exclude,distance=0..]

execute if entity @e[tag=ta_attack_temp,tag=1,distance=0..] run setblock -11798 202 348 minecraft:redstone_block
execute if entity @e[tag=ta_attack_temp,tag=2,distance=0..] run setblock -11798 202 345 minecraft:redstone_block
execute if entity @e[tag=ta_attack_temp,tag=3,distance=0..] run setblock -11798 202 342 minecraft:redstone_block
execute if entity @e[tag=ta_attack_temp,tag=4,distance=0..] run setblock -11798 202 339 minecraft:redstone_block

execute if entity @e[tag=ta_attack_temp,tag=1,distance=0..] run scoreboard players set boss:ta_lastattack Value 1
execute if entity @e[tag=ta_attack_temp,tag=2,distance=0..] run scoreboard players set boss:ta_lastattack Value 2
execute if entity @e[tag=ta_attack_temp,tag=3,distance=0..] run scoreboard players set boss:ta_lastattack Value 3
execute if entity @e[tag=ta_attack_temp,tag=4,distance=0..] run scoreboard players set boss:ta_lastattack Value 4

kill @e[type=minecraft:area_effect_cloud,tag=ta_attack_temp,distance=0..]
