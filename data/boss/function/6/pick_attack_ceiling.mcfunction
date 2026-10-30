# 8 - SLAM CEILING (HONEY FALLS)
# 9 - SPIT HONEYBOMB
# 10 - HONEY CONTROL
# 11 - SUMMON MONSTERS

execute unless score boss:sh_lastattack Value matches 8 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","8","exclude"]}
execute unless score boss:sh_lastattack Value matches 8 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","8","exclude"]}
execute unless score boss:sh_lastattack Value matches 9 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","9","exclude"]}
execute if block -10478 42 -72 lime_wool unless score boss:sh_lastattack Value matches 9 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","9","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~ ~ honey_block unless score boss:sh_lastattack Value matches 10 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","10","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~ ~ honey_block unless score boss:sh_lastattack Value matches 10 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","10","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~ ~ honey_block unless score boss:sh_lastattack Value matches 10 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","10","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~ ~ honey_block unless score boss:sh_lastattack Value matches 10 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","10","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~-1 ~ honey_block unless score boss:sh_lastattack Value matches 10 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","10","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~-1 ~ honey_block unless score boss:sh_lastattack Value matches 10 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","10","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~-1 ~ honey_block unless score boss:sh_lastattack Value matches 10 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","10","exclude"]}
execute as @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] at @s if entity @s[y=61,dy=5] if block ~ ~-1 ~ honey_block unless score boss:sh_lastattack Value matches 10 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","10","exclude"]}
execute unless entity @e[tag=fungloom,distance=0..] unless score boss:sh_lastattack Value matches 11 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","11","exclude"]}

#Failsafe attack
execute unless entity @e[tag=sh_attack_temp,type=area_effect_cloud,distance=0..] run summon area_effect_cloud -10486 41 -71 {Tags:["sh_attack_temp","8","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=sh_attack_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=sh_attack_temp,tag=exclude,distance=0..]

execute if entity @e[tag=sh_attack_temp,tag=8,distance=0..] run setblock -10465 42 -77 minecraft:redstone_block
execute if entity @e[tag=sh_attack_temp,tag=9,distance=0..] run setblock -10477 42 -74 minecraft:redstone_block
execute if entity @e[tag=sh_attack_temp,tag=10,distance=0..] run setblock -10477 42 -80 minecraft:redstone_block
execute if entity @e[tag=sh_attack_temp,tag=11,distance=0..] run setblock -10477 42 -83 minecraft:redstone_block

execute if entity @e[tag=sh_attack_temp,tag=8,distance=0..] run scoreboard players set boss:sh_lastattack Value 8
execute if entity @e[tag=sh_attack_temp,tag=9,distance=0..] run scoreboard players set boss:sh_lastattack Value 9
execute if entity @e[tag=sh_attack_temp,tag=10,distance=0..] run scoreboard players set boss:sh_lastattack Value 10
execute if entity @e[tag=sh_attack_temp,tag=11,distance=0..] run scoreboard players set boss:sh_lastattack Value 11

execute unless entity @e[tag=sh_attack_temp,tag=9,distance=0..] run fill -10478 42 -72 -10478 42 -72 lime_wool replace minecraft:blue_wool
execute unless entity @e[tag=sh_attack_temp,tag=9,distance=0..] run fill -10478 42 -72 -10478 42 -72 blue_wool replace minecraft:black_wool
execute if entity @e[tag=sh_attack_temp,tag=9,distance=0..] run setblock -10478 42 -72 black_wool

kill @e[type=minecraft:area_effect_cloud,tag=sh_attack_temp,distance=0..]

fill -10478 42 -70 -10478 42 -71 minecraft:black_wool

tag @a[tag=mg.flw] remove sh_targeted
