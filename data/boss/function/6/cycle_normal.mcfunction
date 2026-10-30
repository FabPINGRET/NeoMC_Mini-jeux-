# 1 - MOVE TO PLAYER
# 2 - PICK ATTACK (GROUND)
# 3 - PICK ATTACK (CEILING)
# 4 - BOUNCE TO CEILING

execute unless block -10478 42 -71 minecraft:red_wool if block -10478 42 -70 minecraft:black_wool run summon area_effect_cloud -10486 41 -71 {Tags:["sh_cycle_temp","1","exclude"]}
execute unless block -10478 42 -71 minecraft:red_wool if block -10478 42 -70 minecraft:black_wool run summon area_effect_cloud -10486 41 -71 {Tags:["sh_cycle_temp","1","exclude"]}
execute unless block -10478 42 -71 minecraft:red_wool if block -10478 42 -70 minecraft:black_wool run summon area_effect_cloud -10486 41 -71 {Tags:["sh_cycle_temp","1","exclude"]}

execute unless block -10478 42 -71 minecraft:red_wool if block -10478 42 -70 minecraft:blue_wool run summon area_effect_cloud -10486 41 -71 {Tags:["sh_cycle_temp","1","exclude"]}
execute unless block -10478 42 -71 minecraft:red_wool if block -10478 42 -70 minecraft:blue_wool run summon area_effect_cloud -10486 41 -71 {Tags:["sh_cycle_temp","1","exclude"]}

execute unless block -10478 42 -71 minecraft:red_wool if block -10478 42 -70 minecraft:lime_wool run summon area_effect_cloud -10486 41 -71 {Tags:["sh_cycle_temp","1","exclude"]}

execute if score boss:sh_ceiling bool matches 0 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_cycle_temp","2","exclude"]}
execute if score boss:sh_ceiling bool matches 1 run summon area_effect_cloud -10486 41 -71 {Tags:["sh_cycle_temp","3","exclude"]}

#SUPER SLIME BEAM CHECK
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @n[tag=boss_sh_superslimebeam,distance=..1] run kill @e[type=minecraft:area_effect_cloud,tag=sh_cycle_temp,distance=0..]
execute as @n[tag=boss_sh_loc,distance=0..] at @s if entity @n[tag=boss_sh_superslimebeam,distance=..1] run summon area_effect_cloud -10486 41 -71 {Tags:["sh_cycle_temp","4","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=sh_cycle_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=sh_cycle_temp,tag=exclude,distance=0..]

#RECYCLE IF NO PLAYER
execute unless entity @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] run schedule function floaty:sched/boss/6/select_cycle 30t replace
execute unless entity @a[tag=bossroom,gamemode=!spectator,tag=mg.flw] run kill @e[type=minecraft:area_effect_cloud,tag=sh_cycle_temp,distance=0..]
#execute unless entity @a[tag=bossroom,gamemode=!spectator] run say no player!

execute if entity @e[tag=sh_cycle_temp,tag=1,distance=0..] run function boss:6/move/to/player
execute if entity @e[tag=sh_cycle_temp,tag=2,distance=0..] run function boss:6/pick_attack
execute if entity @e[tag=sh_cycle_temp,tag=3,distance=0..] run function boss:6/pick_attack_ceiling
execute if entity @e[tag=sh_cycle_temp,tag=4,distance=0..] run setblock -10462 42 -90 minecraft:redstone_block

kill @e[type=minecraft:area_effect_cloud,tag=sh_cycle_temp,distance=0..]
