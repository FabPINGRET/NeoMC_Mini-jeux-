summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","1","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","2","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","3","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","4","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","5","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","6","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","7","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","8","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","9","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","10","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","11","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","12","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","13","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","14","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","15","exclude"]}
summon area_effect_cloud ~ ~ ~ {Tags:["fella_start_temp","16","exclude"]}

tag @e[type=minecraft:area_effect_cloud,tag=fella_start_temp,limit=1,sort=random,distance=0..] remove exclude

kill @e[type=minecraft:area_effect_cloud,tag=fella_start_temp,tag=exclude,distance=0..]

execute if entity @e[tag=fella_start_temp,tag=1,distance=0..] run summon armor_stand -10072 116 -341 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_north"],DisabledSlots:4144959}
execute if entity @e[tag=fella_start_temp,tag=2,distance=0..] run summon armor_stand -10065 116 -341 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_north"],DisabledSlots:4144959}
execute if entity @e[tag=fella_start_temp,tag=3,distance=0..] run summon armor_stand -10058 116 -341 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_north"],DisabledSlots:4144959}
execute if entity @e[tag=fella_start_temp,tag=4,distance=0..] run summon armor_stand -10051 116 -341 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_north"],DisabledSlots:4144959}

execute if entity @e[tag=fella_start_temp,tag=5,distance=0..] run summon armor_stand -10044 116 -341 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_west"],DisabledSlots:4144959}
execute if entity @e[tag=fella_start_temp,tag=6,distance=0..] run summon armor_stand -10044 116 -348 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_west"],DisabledSlots:4144959}
execute if entity @e[tag=fella_start_temp,tag=7,distance=0..] run summon armor_stand -10044 116 -355 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_west"],DisabledSlots:4144959}
execute if entity @e[tag=fella_start_temp,tag=8,distance=0..] run summon armor_stand -10044 116 -362 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_west"],DisabledSlots:4144959}

execute if entity @e[tag=fella_start_temp,tag=9,distance=0..] run summon armor_stand -10044 116 -369 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_south"],DisabledSlots:4144959}
execute if entity @e[tag=fella_start_temp,tag=10,distance=0..] run summon armor_stand -10051 116 -369 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_south"],DisabledSlots:4144959}
execute if entity @e[tag=fella_start_temp,tag=11,distance=0..] run summon armor_stand -10058 116 -369 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_south"],DisabledSlots:4144959}
execute if entity @e[tag=fella_start_temp,tag=12,distance=0..] run summon armor_stand -10065 116 -369 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_south"],DisabledSlots:4144959}

execute if entity @e[tag=fella_start_temp,tag=13,distance=0..] run summon armor_stand -10072 116 -369 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_east"],DisabledSlots:4144959}
execute if entity @e[tag=fella_start_temp,tag=14,distance=0..] run summon armor_stand -10072 116 -362 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_east"],DisabledSlots:4144959}
execute if entity @e[tag=fella_start_temp,tag=15,distance=0..] run summon armor_stand -10072 116 -355 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_east"],DisabledSlots:4144959}
execute if entity @e[tag=fella_start_temp,tag=16,distance=0..] run summon armor_stand -10072 116 -348 {NoGravity:1b,Invulnerable:1b,Small:1b,Marker:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_ed_fella","fella_east"],DisabledSlots:4144959}

kill @e[type=minecraft:area_effect_cloud,tag=fella_start_temp,distance=0..]

execute as @e[tag=fella_east,distance=0..] at @s facing ~1 ~ ~ run tp @s ~ ~ ~ ~ ~
execute as @e[tag=fella_south,distance=0..] at @s facing ~ ~ ~1 run tp @s ~ ~ ~ ~ ~
execute as @e[tag=fella_west,distance=0..] at @s facing ~-1 ~ ~ run tp @s ~ ~ ~ ~ ~
execute as @e[tag=fella_north,distance=0..] at @s facing ~ ~ ~-1 run tp @s ~ ~ ~ ~ ~

execute if entity @e[tag=fella_north,distance=0..] run setblock -10071 95 -385 redstone_block
execute if entity @e[tag=fella_south,distance=0..] run setblock -10073 95 -385 redstone_block
execute if entity @e[tag=fella_east,distance=0..] run setblock -10075 95 -385 redstone_block
execute if entity @e[tag=fella_west,distance=0..] run setblock -10077 95 -385 redstone_block

setblock -10071 95 -371 stone
