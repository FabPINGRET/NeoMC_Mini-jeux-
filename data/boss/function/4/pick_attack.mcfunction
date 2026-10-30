execute if block -10052 95 -352 stone run summon area_effect_cloud -10058 94 -355 {Tags:["ed_attack_temp","1","exclude"]}
execute if block -10053 95 -352 stone run summon area_effect_cloud -10058 94 -355 {Tags:["ed_attack_temp","2","exclude"]}
execute if block -10054 95 -352 stone run summon area_effect_cloud -10058 94 -355 {Tags:["ed_attack_temp","3","exclude"]}
execute if block -10055 95 -352 stone run summon area_effect_cloud -10058 94 -355 {Tags:["ed_attack_temp","4","exclude"]}
execute if block -10052 95 -349 stone if entity @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] run summon area_effect_cloud -10058 94 -355 {Tags:["ed_attack_temp","5","exclude"]}
execute if block -10053 95 -349 stone run summon area_effect_cloud -10058 94 -355 {Tags:["ed_attack_temp","6","exclude"]}
execute if block -10053 95 -349 glowstone run summon area_effect_cloud -10058 94 -355 {Tags:["ed_attack_temp","6","exclude"]}
execute if block -10053 95 -349 glowstone run summon area_effect_cloud -10058 94 -355 {Tags:["ed_attack_temp","6","exclude"]}
execute if block -10053 95 -349 red_glazed_terracotta run summon area_effect_cloud -10058 94 -355 {Tags:["ed_attack_temp","6","exclude"]}
execute if block -10053 95 -349 red_glazed_terracotta run summon area_effect_cloud -10058 94 -355 {Tags:["ed_attack_temp","6","exclude"]}
execute if block -10053 95 -349 red_glazed_terracotta run summon area_effect_cloud -10058 94 -355 {Tags:["ed_attack_temp","6","exclude"]}
execute if block -10054 95 -349 stone run summon area_effect_cloud -10058 94 -355 {Tags:["ed_attack_temp","7","exclude"]}

execute if entity @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] if block -10053 95 -349 glowstone run setblock -10053 95 -349 red_glazed_terracotta
execute if entity @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] if block -10053 95 -349 stone run setblock -10053 95 -349 glowstone
execute if entity @a[gamemode=!spectator,tag=bossroom,tag=mg.flw] if block -10053 95 -349 air run setblock -10053 95 -349 stone

tag @e[type=minecraft:area_effect_cloud,tag=ed_attack_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=ed_attack_temp,tag=exclude,distance=0..]

execute if entity @e[tag=ed_attack_temp,tag=1,distance=0..] run function boss:4/5hands
execute if entity @e[tag=ed_attack_temp,tag=2,distance=0..] run function boss:4/7hands
execute if entity @e[tag=ed_attack_temp,tag=3,distance=0..] run function boss:4/9hands
execute if entity @e[tag=ed_attack_temp,tag=4,distance=0..] run function boss:4/cannon
execute if entity @e[tag=ed_attack_temp,tag=5,distance=0..] run function boss:4/pick_laser
execute if entity @e[tag=ed_attack_temp,tag=6,distance=0..] run function boss:4/fella_start
execute if entity @e[tag=ed_attack_temp,tag=7,distance=0..] run setblock -10061 95 -358 redstone_block

execute unless entity @e[tag=ed_attack_temp,distance=0..] run function boss:4/cannon

kill @e[type=minecraft:area_effect_cloud,tag=ed_attack_temp,distance=0..]
