fill -10247 93 411 -10197 104 459 air replace minecraft:white_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:green_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:lime_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:red_stained_glass
fill -10247 93 411 -10197 104 459 air replace minecraft:verdant_froglight[axis=x]
fill -10247 93 411 -10197 104 459 air replace minecraft:verdant_froglight[axis=z]
fill -10247 93 411 -10197 104 459 air replace minecraft:smooth_quartz_stairs

execute as @e[tag=boss_skt_hole_12,distance=0..] at @s run clone -10181 73 405 -10168 77 413 ~-12 ~1 ~-4
execute as @e[tag=boss_skt_hole_12,distance=0..] at @s run clone -10199 73 425 -10197 73 427 ~-1 ~ ~-1

summon armor_stand -10213 93 424 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_skt_evoker"],DisabledSlots:4144959,Rotation:[90F,0F]}
summon armor_stand -10213 93 424 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_skt_evoker"],DisabledSlots:4144959,Rotation:[95F,0F]}
summon armor_stand -10213 93 424 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_skt_evoker"],DisabledSlots:4144959,Rotation:[100F,0F]}
summon armor_stand -10213 93 424 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_skt_evoker"],DisabledSlots:4144959,Rotation:[80F,0F]}
summon armor_stand -10213 93 424 {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["boss_skt_evoker"],DisabledSlots:4144959,Rotation:[85F,0F]}

playsound minecraft:entity.phantom.bite hostile @a[tag=mg.flw] -10213 94 424 3 0.1
particle minecraft:crit -10213 94 424 1 1 1 0.1 25
