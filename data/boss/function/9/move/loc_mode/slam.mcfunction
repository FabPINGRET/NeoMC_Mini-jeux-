# 0 = RING, 1 = GROUND RING, 2 = STATIC, 3 = SLAM

scoreboard players set @s Value 3
scoreboard players set wm_follow_dest bool 0
execute at @n[tag=wm_drone_draw,tag=1,distance=0..] run summon armor_stand ~ ~ ~ {Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["wm_grav_ref","1"],attributes:[{id:"minecraft:gravity",base:0.2}],DisabledSlots:4144959}
execute at @n[tag=wm_drone_draw,tag=2,distance=0..] run summon armor_stand ~ ~ ~ {Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["wm_grav_ref","2"],attributes:[{id:"minecraft:gravity",base:0.2}],DisabledSlots:4144959}
execute at @n[tag=wm_drone_draw,tag=3,distance=0..] run summon armor_stand ~ ~ ~ {Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["wm_grav_ref","3"],attributes:[{id:"minecraft:gravity",base:0.2}],DisabledSlots:4144959}
setblock -11199 -35 -105 minecraft:redstone_block
