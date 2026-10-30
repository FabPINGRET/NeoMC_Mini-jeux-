# 1 - SLAM
# 2 - SPORE LASER
# 3 - SPIT ARROWS
# 4 - SHELL BEAM
# 5 - SPIT HONEYBOMB
# 6 - HONEY CONTROL
# 7 - SUMMON MONSTERS

execute unless score boss:sh_lastattack Value matches 1 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","1","exclude"]}
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @a[tag=bossroom,gamemode=!spectator,distance=..4,tag=mg.flw] unless score boss:sh_lastattack Value matches 1 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","1","exclude"]}
execute unless score boss:sh_lastattack Value matches 2 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","2","exclude"]}
execute unless score boss:sh_lastattack Value matches 3 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","3","exclude"]}
execute unless score boss:sh_lastattack Value matches 4 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","4","exclude"]}
execute unless score boss:sh BossHealth < 6 Value unless score boss:sh_lastattack Value matches 5 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","5","exclude"]}
execute unless score boss:sh BossHealth < 6 Value if block -10478 42 -72 lime_wool unless score boss:sh_lastattack Value matches 5 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","5","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~ ~ honey_block unless score boss:sh_lastattack Value matches 6 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","6","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~ ~ honey_block unless score boss:sh_lastattack Value matches 6 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","6","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~ ~ honey_block unless score boss:sh_lastattack Value matches 6 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","6","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~ ~ honey_block unless score boss:sh_lastattack Value matches 6 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","6","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~-1 ~ honey_block unless score boss:sh_lastattack Value matches 6 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","6","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~-1 ~ honey_block unless score boss:sh_lastattack Value matches 6 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","6","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~-1 ~ honey_block unless score boss:sh_lastattack Value matches 6 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","6","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~-1 ~ honey_block unless score boss:sh_lastattack Value matches 6 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","6","exclude"]}
execute unless entity @e[tag=fungloom,distance=0..] unless score boss:sh_lastattack Value matches 7 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","7","exclude"]}

execute unless entity @e[tag=sh_attack_temp,type=area_effect_cloud,distance=0..] run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","3","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=sh_attack_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=sh_attack_temp,tag=exclude,distance=0..]

execute if entity @e[tag=sh_attack_temp,tag=1,distance=0..] run setblock -10465 42 -59 minecraft:redstone_block
execute if entity @e[tag=sh_attack_temp,tag=2,distance=0..] run setblock -10465 42 -65 minecraft:redstone_block
execute if entity @e[tag=sh_attack_temp,tag=3,distance=0..] run setblock -10465 42 -68 minecraft:redstone_block
execute if entity @e[tag=sh_attack_temp,tag=4,distance=0..] run setblock -10465 42 -71 minecraft:redstone_block
execute if entity @e[tag=sh_attack_temp,tag=5,distance=0..] run setblock -10465 42 -74 minecraft:redstone_block
execute if entity @e[tag=sh_attack_temp,tag=6,distance=0..] run setblock -10465 42 -80 minecraft:redstone_block
execute if entity @e[tag=sh_attack_temp,tag=7,distance=0..] run setblock -10465 42 -83 minecraft:redstone_block

execute if entity @e[tag=sh_attack_temp,tag=1,distance=0..] run scoreboard players set boss:sh_lastattack Value 1
execute if entity @e[tag=sh_attack_temp,tag=2,distance=0..] run scoreboard players set boss:sh_lastattack Value 2
execute if entity @e[tag=sh_attack_temp,tag=3,distance=0..] run scoreboard players set boss:sh_lastattack Value 3
execute if entity @e[tag=sh_attack_temp,tag=4,distance=0..] run scoreboard players set boss:sh_lastattack Value 4
execute if entity @e[tag=sh_attack_temp,tag=5,distance=0..] run scoreboard players set boss:sh_lastattack Value 5
execute if entity @e[tag=sh_attack_temp,tag=6,distance=0..] run scoreboard players set boss:sh_lastattack Value 6
execute if entity @e[tag=sh_attack_temp,tag=7,distance=0..] run scoreboard players set boss:sh_lastattack Value 7

execute unless entity @e[tag=sh_attack_temp,tag=5,distance=0..] run fill -10478 42 -72 -10478 42 -72 lime_wool replace minecraft:blue_wool
execute unless entity @e[tag=sh_attack_temp,tag=5,distance=0..] run fill -10478 42 -72 -10478 42 -72 blue_wool replace minecraft:black_wool
execute if entity @e[tag=sh_attack_temp,tag=5,distance=0..] run setblock -10478 42 -72 black_wool

kill @e[type=minecraft:area_effect_cloud,tag=sh_attack_temp,distance=0..]

fill -10478 42 -70 -10478 42 -71 minecraft:black_wool

tag @a[tag=mg.flw] remove sh_targeted
