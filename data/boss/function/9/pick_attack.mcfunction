kill @e[type=trident,nbt={inGround:1b},distance=0..]
#say picking attack

#tag @a remove targeted
#execute unless entity @a[tag=bossroom,tag=targeted] run tag @r[tag=bossroom,gamemode=!spectator] add targeted

# IF AT LEAST ONE
# 1 - TRIDENT FROM EACH
# 2 - SUMMON
# 3 - RING, FACE CENTER THEN STATIC AND LASER
# 4 - FACE GROUND, SHOOT LASER DOWN AND READJUST POSITIONS
# 5 - SLAM DOWN, CREATE PUDDLE
# 6 - GROUND, FACE EACH OTHER, LASERS AND READJUSTING

execute unless score boss:wm_lastattack Value matches 1 run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_attack_temp","1","exclude"]}
execute unless score boss:wm_lastattack Value matches 1 run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_attack_temp","1","exclude"]}
execute unless entity @e[tag=encruster,distance=0..] unless score boss:wm_lastattack Value matches 2 run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_attack_temp","2","exclude"]}
execute unless entity @e[tag=encruster,distance=0..] unless score boss:wm_lastattack Value matches 2 run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_attack_temp","2","exclude"]}
execute unless score boss:wm_lastattack Value matches 3 run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_attack_temp","3","exclude"]}
execute unless score boss:wm_lastattack Value matches 4 run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_attack_temp","4","exclude"]}
execute unless score boss:wm_lastattack Value matches 5 run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_attack_temp","5","exclude"]}
execute unless score boss:wm_lastattack Value matches 5 if block -11218 -35 -115 minecraft:lime_wool run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_attack_temp","5","exclude"]}
execute unless score boss:wm_lastattack Value matches 5 if block -11218 -35 -115 minecraft:lime_wool run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_attack_temp","5","exclude"]}
execute unless score boss:wm_lastattack Value matches 6 run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_attack_temp","6","exclude"]}


#DEFAULT ATTACK
execute unless entity @e[tag=wm_attack_temp,type=area_effect_cloud,distance=0..] run summon area_effect_cloud -11223 -21 -109 {Tags:["wm_attack_temp","1","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=wm_attack_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=wm_attack_temp,tag=exclude,distance=0..]


execute if entity @e[tag=wm_attack_temp,tag=1,distance=0..] run setblock -11200 -35 -127 redstone_block
execute if entity @e[tag=wm_attack_temp,tag=2,distance=0..] run setblock -11200 -35 -124 redstone_block
execute if entity @e[tag=wm_attack_temp,tag=3,distance=0..] run setblock -11200 -35 -121 redstone_block
execute if entity @e[tag=wm_attack_temp,tag=4,distance=0..] run setblock -11200 -35 -118 redstone_block
execute if entity @e[tag=wm_attack_temp,tag=5,distance=0..] run setblock -11200 -35 -115 redstone_block
execute if entity @e[tag=wm_attack_temp,tag=6,distance=0..] run setblock -11200 -35 -112 redstone_block

execute if entity @e[tag=wm_attack_temp,tag=1,distance=0..] run scoreboard players set boss:wm_lastattack Value 1
execute if entity @e[tag=wm_attack_temp,tag=2,distance=0..] run scoreboard players set boss:wm_lastattack Value 2
execute if entity @e[tag=wm_attack_temp,tag=3,distance=0..] run scoreboard players set boss:wm_lastattack Value 3
execute if entity @e[tag=wm_attack_temp,tag=4,distance=0..] run scoreboard players set boss:wm_lastattack Value 4
execute if entity @e[tag=wm_attack_temp,tag=5,distance=0..] run scoreboard players set boss:wm_lastattack Value 5
execute if entity @e[tag=wm_attack_temp,tag=6,distance=0..] run scoreboard players set boss:wm_lastattack Value 6

kill @e[type=minecraft:area_effect_cloud,tag=wm_attack_temp,distance=0..]
