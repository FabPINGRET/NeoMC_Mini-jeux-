tag @a[tag=mg.flw] remove targeted
execute unless entity @a[tag=bossroom,tag=targeted,tag=mg.flw] run tag @r[tag=bossroom,gamemode=!spectator,tag=mg.flw] add targeted

# 1 - VOLLEY
# 2 - CRYSTALS
# 3 - SHRAPNEL
# 4 - SUMMON
# 5 - ELBOW LASER
# 6 - DOWNBEAM
# 7 - LIGHTNING

execute unless score boss:fs_lastattack Value matches 1 if block -10842 67 373 minecraft:blue_wool run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","1","exclude"]}
execute unless score boss:fs_lastattack Value matches 1 if block -10842 67 373 minecraft:lime_wool run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","1","exclude"]}
execute unless score boss:fs_lastattack Value matches 1 if block -10842 67 373 minecraft:lime_wool run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","1","exclude"]}
execute unless score boss:fs_lastattack Value matches 1 if block -10842 67 373 minecraft:red_wool run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","1","exclude"]}
execute unless score boss:fs_lastattack Value matches 1 if block -10842 67 373 minecraft:red_wool run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","1","exclude"]}
execute unless score boss:fs_lastattack Value matches 1 if block -10842 67 373 minecraft:red_wool run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","1","exclude"]}
execute unless score boss:fs_lastattack Value matches 1 if block -10842 67 373 minecraft:pink_wool run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","1","exclude"]}
execute unless score boss:fs_lastattack Value matches 1 if block -10842 67 373 minecraft:pink_wool run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","1","exclude"]}
execute unless score boss:fs_lastattack Value matches 1 if block -10842 67 373 minecraft:pink_wool run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","1","exclude"]}
execute unless score boss:fs_lastattack Value matches 1 if block -10842 67 373 minecraft:pink_wool run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","1","exclude"]}
execute unless score boss:fs_lastattack Value matches 1 if block -10842 67 373 minecraft:pink_wool run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","1","exclude"]}

execute unless score boss:fs_lastattack Value matches 2 run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","2","exclude"]}
execute unless score boss:fs_lastattack Value matches 3 run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","3","exclude"]}
execute unless score boss:fs_lastattack Value matches 4 unless entity @e[tag=frodrone,distance=0..] run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","4","exclude"]}
execute unless score boss:fs_lastattack Value matches 4 unless entity @e[tag=frodrone,distance=0..] run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","4","exclude"]}
execute unless score boss:fs_lastattack Value matches 5 run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","5","exclude"]}
execute unless score boss:fs_lastattack Value matches 6 positioned -10867 89 382 if entity @a[gamemode=!spectator,distance=..13,tag=mg.flw] run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","6","exclude"]}
execute unless score boss:fs_lastattack Value matches 6 positioned -10867 89 382 if entity @a[gamemode=!spectator,distance=..13,tag=mg.flw] run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","6","exclude"]}
execute unless score boss:fs_lastattack Value matches 6 positioned -10867 89 382 if entity @a[gamemode=!spectator,distance=..13,tag=mg.flw] run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","6","exclude"]}
execute unless score boss:fs_lastattack Value matches 7 run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","7","exclude"]}

execute unless entity @e[tag=fs_attack_temp,type=area_effect_cloud,distance=0..] run summon area_effect_cloud -10849 81 382 {Tags:["fs_attack_temp","3","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=fs_attack_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=fs_attack_temp,tag=exclude,distance=0..]

execute if entity @e[tag=fs_attack_temp,tag=1,distance=0..] run setblock -10826 67 373 redstone_block
execute if entity @e[tag=fs_attack_temp,tag=2,distance=0..] run setblock -10826 67 382 redstone_block
execute if entity @e[tag=fs_attack_temp,tag=3,distance=0..] run setblock -10826 67 391 redstone_block
execute if entity @e[tag=fs_attack_temp,tag=4,distance=0..] run setblock -10826 67 388 redstone_block
execute if entity @e[tag=fs_attack_temp,tag=5,distance=0..] run setblock -10826 67 379 redstone_block
execute if entity @e[tag=fs_attack_temp,tag=6,distance=0..] run setblock -10826 67 394 redstone_block
execute if entity @e[tag=fs_attack_temp,tag=7,distance=0..] run setblock -10826 67 385 redstone_block

execute if entity @e[tag=fs_attack_temp,tag=1,distance=0..] run scoreboard players set boss:fs_lastattack Value 1
execute if entity @e[tag=fs_attack_temp,tag=2,distance=0..] run scoreboard players set boss:fs_lastattack Value 2
execute if entity @e[tag=fs_attack_temp,tag=3,distance=0..] run scoreboard players set boss:fs_lastattack Value 3
execute if entity @e[tag=fs_attack_temp,tag=4,distance=0..] run scoreboard players set boss:fs_lastattack Value 4
execute if entity @e[tag=fs_attack_temp,tag=5,distance=0..] run scoreboard players set boss:fs_lastattack Value 5
execute if entity @e[tag=fs_attack_temp,tag=6,distance=0..] run scoreboard players set boss:fs_lastattack Value 6
execute if entity @e[tag=fs_attack_temp,tag=7,distance=0..] run scoreboard players set boss:fs_lastattack Value 7

kill @e[type=minecraft:area_effect_cloud,tag=fs_attack_temp,distance=0..]

fill -10842 67 373 -10842 67 373 minecraft:pink_wool replace minecraft:red_wool
fill -10842 67 373 -10842 67 373 minecraft:red_wool replace minecraft:lime_wool
fill -10842 67 373 -10842 67 373 minecraft:lime_wool replace minecraft:blue_wool
fill -10842 67 373 -10842 67 373 minecraft:blue_wool replace minecraft:black_wool
