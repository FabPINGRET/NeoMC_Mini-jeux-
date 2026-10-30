fill -10247 93 411 -10197 104 459 air replace minecraft:white_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:green_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:lime_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:red_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:verdant_froglight[axis=x]
fill -10247 93 411 -10197 104 459 air replace minecraft:verdant_froglight[axis=z]
fill -10247 93 411 -10197 104 459 air replace minecraft:smooth_quartz_stairs

execute as @e[tag=boss_skt_hole_2,distance=0..] at @s run clone -10175 73 430 -10167 77 443 ~-4 ~1 ~-1
execute as @e[tag=boss_skt_hole_2,distance=0..] at @s run clone -10199 73 429 -10197 73 431 ~-1 ~ ~-1

summon armor_stand -10212 93 425 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_skt_evoker"],DisabledSlots:4144959,Rotation:[0F,0F]}
summon armor_stand -10212 93 425 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_skt_evoker"],DisabledSlots:4144959,Rotation:[355F,0F]}
summon armor_stand -10212 93 425 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_skt_evoker"],DisabledSlots:4144959,Rotation:[350F,0F]}
summon armor_stand -10212 93 425 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_skt_evoker"],DisabledSlots:4144959,Rotation:[5F,0F]}
summon armor_stand -10212 93 425 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_skt_evoker"],DisabledSlots:4144959,Rotation:[10F,0F]}

playsound minecraft:entity.phantom.bite hostile @a[tag=mg.flw] -10212 94 425 3 0.1
particle minecraft:crit -10212 94 425 1 1 1 0.1 25
