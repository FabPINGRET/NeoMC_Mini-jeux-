function boss:10/faces/mark_loc

#tag @a remove targeted
#execute unless entity @a[tag=bossroom,tag=targeted] run tag @r[tag=bossroom,gamemode=!spectator] add targeted

# 5 PREDICTIVE LASER
# 6 GROUND SPIKE
# 7 META KNIGHT TYPE BEAT
# 8 ADEPT SOUL SUMMON

execute unless score boss:ta_lastattack Value matches 5 run summon area_effect_cloud -11830 200 330 {Tags:["ta_attack_temp","1","exclude"]}
execute unless score boss:ta_lastattack Value matches 6 run summon area_effect_cloud -11830 200 330 {Tags:["ta_attack_temp","2","exclude"]}
execute unless score boss:ta_lastattack Value matches 7 run summon area_effect_cloud -11830 200 330 {Tags:["ta_attack_temp","3","exclude"]}
execute unless entity @e[tag=a_soul,distance=0..] unless score boss:ta_lastattack Value matches 8 run summon area_effect_cloud -11830 200 330 {Tags:["ta_attack_temp","4","exclude"]}


#DEFAULT ATTACK
execute unless entity @e[tag=ta_attack_temp,type=area_effect_cloud,distance=0..] run summon area_effect_cloud -11830 200 330 {Tags:["ta_attack_temp","1","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=ta_attack_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=ta_attack_temp,tag=exclude,distance=0..]

execute if entity @e[tag=ta_attack_temp,tag=1,distance=0..] run setblock -11798 202 330 minecraft:redstone_block
execute if entity @e[tag=ta_attack_temp,tag=2,distance=0..] run setblock -11798 202 327 minecraft:redstone_block
execute if entity @e[tag=ta_attack_temp,tag=3,distance=0..] run setblock -11798 202 324 minecraft:redstone_block
execute if entity @e[tag=ta_attack_temp,tag=4,distance=0..] run setblock -11798 202 321 minecraft:redstone_block

execute if entity @e[tag=ta_attack_temp,tag=1,distance=0..] run scoreboard players set boss:ta_lastattack Value 5
execute if entity @e[tag=ta_attack_temp,tag=2,distance=0..] run scoreboard players set boss:ta_lastattack Value 6
execute if entity @e[tag=ta_attack_temp,tag=3,distance=0..] run scoreboard players set boss:ta_lastattack Value 7
execute if entity @e[tag=ta_attack_temp,tag=4,distance=0..] run scoreboard players set boss:ta_lastattack Value 8

kill @e[type=minecraft:area_effect_cloud,tag=ta_attack_temp,distance=0..]
