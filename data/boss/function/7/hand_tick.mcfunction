execute unless entity @a[tag=bossroom,tag=targeted,tag=mg.flw] run tag @r[tag=bossroom,gamemode=!spectator,tag=mg.flw] add targeted

execute as @n[tag=st_boss_statue,distance=0..] at @s run setblock ~ ~ ~ barrier
execute as @n[tag=st_boss_statue,distance=0..] at @s if entity @s[tag=on] if score boss:st_glass bool matches 0 run summon zombie ~ ~ ~ {Silent:1b,Invulnerable:1b,PersistenceRequired:1b,Health:9999f,IsBaby:1b,Tags:["st_boss_walking_statue"],equipment:{feet:{id:"minecraft:netherite_boots",count:1,components:{"minecraft:trim":{material:"minecraft:iron",pattern:"minecraft:spire"}}},legs:{id:"minecraft:netherite_leggings",count:1,components:{"minecraft:trim":{material:"minecraft:iron",pattern:"minecraft:spire"}}},chest:{id:"minecraft:netherite_chestplate",count:1,components:{"minecraft:trim":{material:"minecraft:iron",pattern:"minecraft:spire"}}},head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{id:[I;1080111988,1100367586,-1845895429,-1077775666],properties:[{name:"textures",value:"ewogICJ0aW1lc3RhbXAiIDogMTczMjAzNjMwNzgyMywKICAicHJvZmlsZUlkIiA6ICJhODgyMzAzMDVkOWY0ODRiYjNjNjc2OTg1OTYxYjc2YSIsCiAgInByb2ZpbGVOYW1lIiA6ICJMb3JkRHJld3BpY3VzIiwKICAic2lnbmF0dXJlUmVxdWlyZWQiIDogdHJ1ZSwKICAidGV4dHVyZXMiIDogewogICAgIlNLSU4iIDogewogICAgICAidXJsIiA6ICJodHRwOi8vdGV4dHVyZXMubWluZWNyYWZ0Lm5ldC90ZXh0dXJlL2YwYTFmNmJjNTlhZmJlMTY1NDYzY2M2OWM2ZTc0YjNiZDQxMjkxN2ZhY2YxOGVmZWEzZGNlOTFhZmE3ZWM4YzAiCiAgICB9CiAgfQp9"}]}}}},active_effects:[{id:"minecraft:invisibility",amplifier:0,duration:-1,show_particles:0b}],attributes:[{id:"minecraft:attack_damage",base:0},{id:"minecraft:max_health",base:9999},{id:"minecraft:movement_speed",base:0.15}]}
execute as @n[tag=st_boss_statue,distance=0..] at @s if entity @s[tag=on] if score boss:st_glass bool matches 0 as @n[tag=st_boss_walking_statue,distance=0..] at @s facing entity @p[tag=mg.flw] eyes run tp @s ~ ~ ~ ~ ~
execute as @n[tag=st_boss_statue,distance=0..] at @s if entity @s[tag=on] if score boss:st_glass bool matches 0 run fill ~ ~ ~ ~ ~ ~ air replace barrier
execute as @n[tag=st_boss_statue,distance=0..] at @s if entity @s[tag=on] if score boss:st_glass bool matches 0 run kill @s
execute if score boss:st_glass bool matches 1 run tag @n[tag=st_boss_statue,distance=0..] remove on

#1
execute as @n[tag=st_hand_inter_1,distance=0..] at @s facing entity @n[tag=st_hand_dest_1,distance=0..] eyes run tp @s ~ ~ ~ ~ ~

execute unless entity @e[tag=st_hand_dest_1,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_1,distance=0..] at @s if entity @n[tag=st_hand_dest_1,distance=..1,tag=!punch_speed] at @n[tag=st_hand_dest_1,tag=!punch_speed,distance=0..] run tp @s ~ ~ ~
execute unless entity @e[tag=st_hand_dest_1,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_1,distance=0..] at @s unless entity @n[tag=st_hand_dest_1,distance=..1,tag=!punch_speed] run tp @s ^ ^ ^1

execute if entity @e[tag=st_hand_dest_1,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_1,distance=0..] at @s if entity @n[tag=st_hand_dest_1,distance=..2,tag=punch_speed] at @n[tag=st_hand_dest_1,tag=punch_speed,distance=0..] run tp @s ~ ~ ~
execute if entity @e[tag=st_hand_dest_1,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_1,distance=0..] at @s unless entity @n[tag=st_hand_dest_1,distance=..2,tag=punch_speed] run tp @s ^ ^ ^2

execute as @n[tag=st_hand_inter_1,distance=0..] at @s unless entity @e[tag=st_hand_draw_1,tag=freefall,distance=0..] run tp @n[tag=st_hand_loc_1,distance=0..] ~ ~ ~
execute as @n[tag=st_hand_draw_1,distance=0..] if entity @s[tag=full_rotation] as @n[tag=st_hand_loc_1,distance=0..] at @s if entity @s[tag=!attacking] facing entity @p[gamemode=!spectator,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_1,distance=0..] ~ ~-2 ~ ~ ~
execute as @n[tag=st_hand_draw_1,distance=0..] if entity @s[tag=full_rotation] as @n[tag=st_hand_loc_1,distance=0..] at @s if entity @s[tag=attacking] facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_1,distance=0..] ~ ~-2 ~ ~ ~
execute as @n[tag=st_hand_draw_1,distance=0..] if entity @s[tag=flat_rotation] as @n[tag=st_hand_loc_1,distance=0..] at @s if entity @s[tag=!attacking] facing entity @p[gamemode=!spectator,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_1,distance=0..] ~ ~-2 ~ ~ 0
execute as @n[tag=st_hand_draw_1,distance=0..] if entity @s[tag=flat_rotation] as @n[tag=st_hand_loc_1,distance=0..] at @s if entity @s[tag=attacking] facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_1,distance=0..] ~ ~-2 ~ ~ 0
execute as @n[tag=st_hand_draw_1,distance=0..] if entity @s[tag=locked] as @n[tag=st_hand_loc_1,distance=0..] at @s run tp @n[tag=st_hand_draw_1,distance=0..] ~ ~-2 ~
execute as @n[tag=st_hand_draw_1,distance=0..] if entity @s[tag=freefall] as @n[tag=st_hand_loc_1,distance=0..] at @s run tp @n[tag=st_hand_draw_1,distance=0..] ~ ~-2 ~

execute as @n[tag=st_hand_draw_1,distance=0..] if entity @s[tag=crystal_rotation] as @n[tag=st_hand_loc_1,distance=0..] at @s facing entity @n[tag=st_hand_loc_3,distance=0..] eyes facing ^ ^ ^-1 rotated ~ 0 run tp @n[tag=st_hand_draw_1,distance=0..] ~ ~-3 ~ ~ ~

execute as @n[tag=st_hand_inter_1,distance=0..] at @s run tp @n[tag=st_hand_shadow_1,distance=0..] ~ -23 ~
execute as @n[tag=st_hand_shadow_1,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] eyes if entity @e[tag=st_hand_draw_1,tag=flat_rotation,distance=0..] facing ^ ^ ^-1 run tp @n[tag=st_hand_shadow_1,distance=0..] ~ ~ ~ ~ 0

#2
execute as @n[tag=st_hand_inter_2,distance=0..] at @s facing entity @n[tag=st_hand_dest_2,distance=0..] eyes run tp @s ~ ~ ~ ~ ~

execute unless entity @e[tag=st_hand_dest_2,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_2,distance=0..] at @s if entity @n[tag=st_hand_dest_2,distance=..1,tag=!punch_speed] at @n[tag=st_hand_dest_2,tag=!punch_speed,distance=0..] run tp @s ~ ~ ~
execute unless entity @e[tag=st_hand_dest_2,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_2,distance=0..] at @s unless entity @n[tag=st_hand_dest_2,distance=..1,tag=!punch_speed] run tp @s ^ ^ ^1

execute if entity @e[tag=st_hand_dest_2,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_2,distance=0..] at @s if entity @n[tag=st_hand_dest_2,distance=..2,tag=punch_speed] at @n[tag=st_hand_dest_2,tag=punch_speed,distance=0..] run tp @s ~ ~ ~
execute if entity @e[tag=st_hand_dest_2,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_2,distance=0..] at @s unless entity @n[tag=st_hand_dest_2,distance=..2,tag=punch_speed] run tp @s ^ ^ ^2

execute as @n[tag=st_hand_inter_2,distance=0..] at @s unless entity @e[tag=st_hand_draw_2,tag=freefall,distance=0..] run tp @n[tag=st_hand_loc_2,distance=0..] ~ ~ ~
execute as @n[tag=st_hand_draw_2,distance=0..] if entity @s[tag=full_rotation] as @n[tag=st_hand_loc_2,distance=0..] at @s if entity @s[tag=!attacking] facing entity @p[gamemode=!spectator,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_2,distance=0..] ~ ~-2 ~ ~ ~
execute as @n[tag=st_hand_draw_2,distance=0..] if entity @s[tag=full_rotation] as @n[tag=st_hand_loc_2,distance=0..] at @s if entity @s[tag=attacking] facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_2,distance=0..] ~ ~-2 ~ ~ ~
execute as @n[tag=st_hand_draw_2,distance=0..] if entity @s[tag=flat_rotation] as @n[tag=st_hand_loc_2,distance=0..] at @s if entity @s[tag=!attacking] facing entity @p[gamemode=!spectator,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_2,distance=0..] ~ ~-2 ~ ~ 0
execute as @n[tag=st_hand_draw_2,distance=0..] if entity @s[tag=flat_rotation] as @n[tag=st_hand_loc_2,distance=0..] at @s if entity @s[tag=attacking] facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_2,distance=0..] ~ ~-2 ~ ~ 0
execute as @n[tag=st_hand_draw_2,distance=0..] if entity @s[tag=locked] as @n[tag=st_hand_loc_2,distance=0..] at @s run tp @n[tag=st_hand_draw_2,distance=0..] ~ ~-2 ~
execute as @n[tag=st_hand_draw_2,distance=0..] if entity @s[tag=freefall] as @n[tag=st_hand_loc_2,distance=0..] at @s run tp @n[tag=st_hand_draw_2,distance=0..] ~ ~-2 ~

execute as @n[tag=st_hand_inter_2,distance=0..] at @s run tp @n[tag=st_hand_shadow_2,distance=0..] ~ -23 ~
execute as @n[tag=st_hand_shadow_2,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] eyes if entity @e[tag=st_hand_draw_2,tag=flat_rotation,distance=0..] facing ^ ^ ^-1 run tp @n[tag=st_hand_shadow_2,distance=0..] ~ ~ ~ ~ 0

#3
execute as @n[tag=st_hand_inter_3,distance=0..] at @s facing entity @n[tag=st_hand_dest_3,distance=0..] eyes run tp @s ~ ~ ~ ~ ~

execute unless entity @e[tag=st_hand_dest_3,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_3,distance=0..] at @s if entity @n[tag=st_hand_dest_3,distance=..1,tag=!punch_speed] at @n[tag=st_hand_dest_3,tag=!punch_speed,distance=0..] run tp @s ~ ~ ~
execute unless entity @e[tag=st_hand_dest_3,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_3,distance=0..] at @s unless entity @n[tag=st_hand_dest_3,distance=..1,tag=!punch_speed] run tp @s ^ ^ ^1

execute if entity @e[tag=st_hand_dest_3,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_3,distance=0..] at @s if entity @n[tag=st_hand_dest_3,distance=..2,tag=punch_speed] at @n[tag=st_hand_dest_3,tag=punch_speed,distance=0..] run tp @s ~ ~ ~
execute if entity @e[tag=st_hand_dest_3,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_3,distance=0..] at @s unless entity @n[tag=st_hand_dest_3,distance=..2,tag=punch_speed] run tp @s ^ ^ ^2

execute as @n[tag=st_hand_inter_3,distance=0..] at @s unless entity @e[tag=st_hand_draw_3,tag=freefall,distance=0..] run tp @n[tag=st_hand_loc_3,distance=0..] ~ ~ ~
execute as @n[tag=st_hand_draw_3,distance=0..] if entity @s[tag=full_rotation] as @n[tag=st_hand_loc_3,distance=0..] at @s if entity @s[tag=!attacking] facing entity @p[gamemode=!spectator,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_3,distance=0..] ~ ~-2 ~ ~ ~
execute as @n[tag=st_hand_draw_3,distance=0..] if entity @s[tag=full_rotation] as @n[tag=st_hand_loc_3,distance=0..] at @s if entity @s[tag=attacking] facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_3,distance=0..] ~ ~-2 ~ ~ ~
execute as @n[tag=st_hand_draw_3,distance=0..] if entity @s[tag=flat_rotation] as @n[tag=st_hand_loc_3,distance=0..] at @s if entity @s[tag=!attacking] facing entity @p[gamemode=!spectator,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_3,distance=0..] ~ ~-2 ~ ~ 0
execute as @n[tag=st_hand_draw_3,distance=0..] if entity @s[tag=flat_rotation] as @n[tag=st_hand_loc_3,distance=0..] at @s if entity @s[tag=attacking] facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_3,distance=0..] ~ ~-2 ~ ~ 0
execute as @n[tag=st_hand_draw_3,distance=0..] if entity @s[tag=locked] as @n[tag=st_hand_loc_3,distance=0..] at @s run tp @n[tag=st_hand_draw_3,distance=0..] ~ ~-2 ~
execute as @n[tag=st_hand_draw_3,distance=0..] if entity @s[tag=freefall] as @n[tag=st_hand_loc_3,distance=0..] at @s run tp @n[tag=st_hand_draw_3,distance=0..] ~ ~-2 ~

execute as @n[tag=st_hand_inter_3,distance=0..] at @s run tp @n[tag=st_hand_shadow_3,distance=0..] ~ -23 ~
execute as @n[tag=st_hand_shadow_3,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] eyes if entity @e[tag=st_hand_draw_3,tag=flat_rotation,distance=0..] facing ^ ^ ^-1 run tp @n[tag=st_hand_shadow_3,distance=0..] ~ ~ ~ ~ 0

#4
execute as @n[tag=st_hand_inter_4,distance=0..] at @s facing entity @n[tag=st_hand_dest_4,distance=0..] eyes run tp @s ~ ~ ~ ~ ~

execute unless entity @e[tag=st_hand_dest_4,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_4,distance=0..] at @s if entity @n[tag=st_hand_dest_4,distance=..1,tag=!punch_speed] at @n[tag=st_hand_dest_4,tag=!punch_speed,distance=0..] run tp @s ~ ~ ~
execute unless entity @e[tag=st_hand_dest_4,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_4,distance=0..] at @s unless entity @n[tag=st_hand_dest_4,distance=..1,tag=!punch_speed] run tp @s ^ ^ ^1

execute if entity @e[tag=st_hand_dest_4,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_4,distance=0..] at @s if entity @n[tag=st_hand_dest_4,distance=..2,tag=punch_speed] at @n[tag=st_hand_dest_4,tag=punch_speed,distance=0..] run tp @s ~ ~ ~
execute if entity @e[tag=st_hand_dest_4,tag=punch_speed,distance=0..] as @n[tag=st_hand_inter_4,distance=0..] at @s unless entity @n[tag=st_hand_dest_4,distance=..2,tag=punch_speed] run tp @s ^ ^ ^2

execute as @n[tag=st_hand_inter_4,distance=0..] at @s unless entity @e[tag=st_hand_draw_4,tag=freefall,distance=0..] run tp @n[tag=st_hand_loc_4,distance=0..] ~ ~ ~
execute as @n[tag=st_hand_draw_4,distance=0..] if entity @s[tag=full_rotation] as @n[tag=st_hand_loc_4,distance=0..] at @s if entity @s[tag=!attacking] facing entity @p[gamemode=!spectator,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_4,distance=0..] ~ ~-2 ~ ~ ~
execute as @n[tag=st_hand_draw_4,distance=0..] if entity @s[tag=full_rotation] as @n[tag=st_hand_loc_4,distance=0..] at @s if entity @s[tag=attacking] facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_4,distance=0..] ~ ~-2 ~ ~ ~
execute as @n[tag=st_hand_draw_4,distance=0..] if entity @s[tag=flat_rotation] as @n[tag=st_hand_loc_4,distance=0..] at @s if entity @s[tag=!attacking] facing entity @p[gamemode=!spectator,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_4,distance=0..] ~ ~-2 ~ ~ 0
execute as @n[tag=st_hand_draw_4,distance=0..] if entity @s[tag=flat_rotation] as @n[tag=st_hand_loc_4,distance=0..] at @s if entity @s[tag=attacking] facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] eyes facing ^ ^ ^-1 run tp @n[tag=st_hand_draw_4,distance=0..] ~ ~-2 ~ ~ 0
execute as @n[tag=st_hand_draw_4,distance=0..] if entity @s[tag=locked] as @n[tag=st_hand_loc_4,distance=0..] at @s run tp @n[tag=st_hand_draw_4,distance=0..] ~ ~-2 ~
execute as @n[tag=st_hand_draw_4,distance=0..] if entity @s[tag=freefall] as @n[tag=st_hand_loc_4,distance=0..] at @s run tp @n[tag=st_hand_draw_4,distance=0..] ~ ~-2 ~

execute as @n[tag=st_hand_inter_4,distance=0..] at @s run tp @n[tag=st_hand_shadow_4,distance=0..] ~ -23 ~
execute as @n[tag=st_hand_shadow_4,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] eyes if entity @e[tag=st_hand_draw_4,tag=flat_rotation,distance=0..] facing ^ ^ ^-1 run tp @n[tag=st_hand_shadow_4,distance=0..] ~ ~ ~ ~ 0

team join NoCollide @e[tag=st_hand_draw_1,distance=0..]
team join NoCollide @e[tag=st_hand_draw_2,distance=0..]
team join NoCollide @e[tag=st_hand_draw_3,distance=0..]
team join NoCollide @e[tag=st_hand_draw_4,distance=0..]


# IDLE POSITIONS
execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^-9 ^ ^-9 positioned ~ -8 ~ run tp @n[tag=st_hand_dest_1,tag=!attacking,tag=hand_pos_2,distance=0..] ~ ~ ~
execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^-9 ^ ^9 positioned ~ -8 ~ run tp @n[tag=st_hand_dest_2,tag=!attacking,tag=hand_pos_2,distance=0..] ~ ~ ~
execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^9 ^ ^9 positioned ~ -8 ~ run tp @n[tag=st_hand_dest_3,tag=!attacking,tag=hand_pos_2,distance=0..] ~ ~ ~
execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^9 ^ ^-9 positioned ~ -8 ~ run tp @n[tag=st_hand_dest_4,tag=!attacking,tag=hand_pos_2,distance=0..] ~ ~ ~

execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^-5 ^ ^-5 positioned ~ -8 ~ run tp @n[tag=st_hand_dest_1,tag=!attacking,tag=hand_pos_3,distance=0..] ~ ~ ~
execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^-7 ^ ^7 positioned ~ -7 ~ run tp @n[tag=st_hand_dest_2,tag=!attacking,tag=hand_pos_3,distance=0..] ~ ~ ~
execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^9 ^ ^9 positioned ~ -6 ~ run tp @n[tag=st_hand_dest_3,tag=!attacking,tag=hand_pos_3,distance=0..] ~ ~ ~
execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^11 ^ ^-11 positioned ~ -5 ~ run tp @n[tag=st_hand_dest_4,tag=!attacking,tag=hand_pos_3,distance=0..] ~ ~ ~

execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^-9 ^ ^-9 positioned ~ -16.5 ~ run tp @n[tag=st_hand_dest_1,tag=!attacking,tag=hand_pos_4,distance=0..] ~ ~ ~
execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^-9 ^ ^9 positioned ~ -16.5 ~ run tp @n[tag=st_hand_dest_2,tag=!attacking,tag=hand_pos_4,distance=0..] ~ ~ ~
execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^9 ^ ^9 positioned ~ -16.5 ~ run tp @n[tag=st_hand_dest_3,tag=!attacking,tag=hand_pos_4,distance=0..] ~ ~ ~
execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^9 ^ ^-9 positioned ~ -16.5 ~ run tp @n[tag=st_hand_dest_4,tag=!attacking,tag=hand_pos_4,distance=0..] ~ ~ ~

execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^-9 ^ ^-9 positioned ~ -8 ~ run tp @n[tag=st_hand_dest_1,tag=!attacking,tag=hand_pos_5,distance=0..] ~ ~ ~
execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^-9 ^ ^9 positioned ~ -8 ~ run tp @n[tag=st_hand_dest_2,tag=!attacking,tag=hand_pos_5,distance=0..] ~ ~ ~
execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^9 ^ ^9 positioned ~ -8 ~ run tp @n[tag=st_hand_dest_3,tag=!attacking,tag=hand_pos_5,distance=0..] ~ ~ ~
execute as @n[tag=st_boss_center_pos,distance=0..] at @s positioned ^9 ^ ^-9 positioned ~ -8 ~ run tp @n[tag=st_hand_dest_4,tag=!attacking,tag=hand_pos_5,distance=0..] ~ ~ ~

#execute as @n[tag=st_vortex_1] at @s positioned ~ -20 ~ run tp @n[tag=st_hand_dest_1,tag=!attacking,tag=hand_pos_6] ~ ~ ~
#execute as @n[tag=st_vortex_2] at @s positioned ~ -20 ~ run tp @n[tag=st_hand_dest_2,tag=!attacking,tag=hand_pos_6] ~ ~ ~
#execute as @n[tag=st_vortex_3] at @s positioned ~ -20 ~ run tp @n[tag=st_hand_dest_3,tag=!attacking,tag=hand_pos_6] ~ ~ ~
#execute as @n[tag=st_vortex_4] at @s positioned ~ -20 ~ run tp @n[tag=st_hand_dest_4,tag=!attacking,tag=hand_pos_6] ~ ~ ~

#Strafe targeting
execute as @n[tag=strafe_targeting,tag=st_hand_dest_1,distance=0..] at @n[tag=targeted,distance=0..] positioned ~ -12 ~ facing entity @n[tag=st_boss_center_pos,distance=0..] eyes positioned ^6 ^ ^4 if block ~ ~ ~ air run tp @s ~ ~ ~
execute as @n[tag=strafe_targeting,tag=st_hand_dest_2,distance=0..] at @n[tag=targeted,distance=0..] positioned ~ -12 ~ facing entity @n[tag=st_boss_center_pos,distance=0..] eyes positioned ^6 ^ ^4 if block ~ ~ ~ air run tp @s ~ ~ ~
execute as @n[tag=strafe_targeting,tag=st_hand_dest_3,distance=0..] at @n[tag=targeted,distance=0..] positioned ~ -12 ~ facing entity @n[tag=st_boss_center_pos,distance=0..] eyes positioned ^-6 ^ ^4 if block ~ ~ ~ air run tp @s ~ ~ ~
execute as @n[tag=strafe_targeting,tag=st_hand_dest_4,distance=0..] at @n[tag=targeted,distance=0..] positioned ~ -12 ~ facing entity @n[tag=st_boss_center_pos,distance=0..] eyes positioned ^-6 ^ ^4 if block ~ ~ ~ air run tp @s ~ ~ ~

#Ground strafe targeting
execute as @n[tag=ground_strafe_targeting,tag=st_hand_dest_1,distance=0..] at @n[tag=st_boss_center_pos,distance=0..] positioned ~ -19 ~ facing entity @n[tag=targeted,distance=0..] eyes positioned ^ ^ ^18 positioned ~ -19 ~ if block ~ ~ ~ air run tp @s ~ ~ ~
execute as @n[tag=ground_strafe_targeting,tag=st_hand_dest_2,distance=0..] at @n[tag=st_boss_center_pos,distance=0..] positioned ~ -19 ~ facing entity @n[tag=targeted,distance=0..] eyes positioned ^ ^ ^18 positioned ~ -19 ~ if block ~ ~ ~ air run tp @s ~ ~ ~
execute as @n[tag=ground_strafe_targeting,tag=st_hand_dest_3,distance=0..] at @n[tag=st_boss_center_pos,distance=0..] positioned ~ -19 ~ facing entity @n[tag=targeted,distance=0..] eyes positioned ^ ^ ^18 positioned ~ -19 ~ if block ~ ~ ~ air run tp @s ~ ~ ~
execute as @n[tag=ground_strafe_targeting,tag=st_hand_dest_4,distance=0..] at @n[tag=st_boss_center_pos,distance=0..] positioned ~ -19 ~ facing entity @n[tag=targeted,distance=0..] eyes positioned ^ ^ ^18 positioned ~ -19 ~ if block ~ ~ ~ air run tp @s ~ ~ ~

#hover over targeting
execute as @n[tag=hover_over_targeting,tag=st_hand_dest_1,distance=0..] at @n[tag=targeted,distance=0..] rotated as @p[tag=targeted,tag=mg.flw] rotated ~ 0 positioned ^ ^ ^1.5 positioned ~ -14 ~ facing entity @p[tag=targeted,tag=mg.flw] eyes if block ~-1 ~ ~ air if block ~1 ~ ~ air if block ~ ~ ~-1 air if block ~ ~ ~1 air run tp @s ~ ~ ~
execute as @n[tag=hover_over_targeting,tag=st_hand_dest_2,distance=0..] at @n[tag=targeted,distance=0..] rotated as @p[tag=targeted,tag=mg.flw] rotated ~ 0 positioned ^ ^ ^1.5 positioned ~ -14 ~ facing entity @p[tag=targeted,tag=mg.flw] eyes if block ~-1 ~ ~ air if block ~1 ~ ~ air if block ~ ~ ~-1 air if block ~ ~ ~1 air run tp @s ~ ~ ~
execute as @n[tag=hover_over_targeting,tag=st_hand_dest_3,distance=0..] at @n[tag=targeted,distance=0..] rotated as @p[tag=targeted,tag=mg.flw] rotated ~ 0 positioned ^ ^ ^1.5 positioned ~ -14 ~ facing entity @p[tag=targeted,tag=mg.flw] eyes if block ~-1 ~ ~ air if block ~1 ~ ~ air if block ~ ~ ~-1 air if block ~ ~ ~1 air run tp @s ~ ~ ~
execute as @n[tag=hover_over_targeting,tag=st_hand_dest_4,distance=0..] at @n[tag=targeted,distance=0..] rotated as @p[tag=targeted,tag=mg.flw] rotated ~ 0 positioned ^ ^ ^1.5 positioned ~ -14 ~ facing entity @p[tag=targeted,tag=mg.flw] eyes if block ~-1 ~ ~ air if block ~1 ~ ~ air if block ~ ~ ~-1 air if block ~ ~ ~1 air run tp @s ~ ~ ~

#Crystal Strafe targeting
execute as @n[tag=crystal_strafe_targeting,tag=st_hand_dest_1,distance=0..] at @n[tag=targeted,distance=0..] positioned ~ -4 ~ facing entity @n[tag=st_boss_center_pos,distance=0..] eyes positioned ^4 ^ ^8 if block ~ ~ ~ air run tp @s ~ ~ ~
execute as @n[tag=crystal_strafe_targeting,tag=st_hand_dest_3,distance=0..] at @n[tag=targeted,distance=0..] positioned ~ -4 ~ facing entity @n[tag=st_boss_center_pos,distance=0..] eyes positioned ^-4 ^ ^8 if block ~ ~ ~ air run tp @s ~ ~ ~

#GUN
execute if entity @e[tag=st_hand_loc,tag=gun_attacking,distance=0..] run function boss:7/attack/gun_tick

#SMACK
execute if entity @e[tag=st_hand_loc,tag=smack_attacking,distance=0..] run function boss:7/attack/smack_tick

#PUNCH
execute if entity @e[tag=st_hand_loc,tag=punch_attacking,distance=0..] run function boss:7/attack/punch_tick

#VORTEX
execute if entity @e[tag=st_hand_loc,tag=vortex_attacking,distance=0..] run function boss:7/attack/vortex_tick

#CRYSTAL
execute if entity @e[tag=st_hand_loc,tag=crystal_attacking,distance=0..] run function boss:7/attack/crystal_tick

#POINT DOWN
execute as @e[tag=st_hand_loc,tag=!attacking,tag=point_down,distance=0..] at @s align y positioned ~ ~-3 ~ run function boss:7/utility/point_down_ray

#Throw Arrow Back

execute unless entity @n[tag=st_hand_dest_1,tag=attacking,distance=0..] as @e[tag=st_hand_draw_1,tag=idle,distance=0..] at @s if entity @n[type=arrow,distance=..2] as @n[tag=st_hand_loc_1,distance=0..] run function boss:7/attack/catch_arrow
execute unless entity @n[tag=st_hand_dest_2,tag=attacking,distance=0..] as @e[tag=st_hand_draw_2,tag=idle,distance=0..] at @s if entity @n[type=arrow,distance=..2] as @n[tag=st_hand_loc_2,distance=0..] run function boss:7/attack/catch_arrow
execute unless entity @n[tag=st_hand_dest_3,tag=attacking,distance=0..] as @e[tag=st_hand_draw_3,tag=idle,distance=0..] at @s if entity @n[type=arrow,distance=..2] as @n[tag=st_hand_loc_3,distance=0..] run function boss:7/attack/catch_arrow
execute unless entity @n[tag=st_hand_dest_4,tag=attacking,distance=0..] as @e[tag=st_hand_draw_4,tag=idle,distance=0..] at @s if entity @n[type=arrow,distance=..2] as @n[tag=st_hand_loc_4,distance=0..] run function boss:7/attack/catch_arrow

execute as @n[tag=st_hand_loc_1,tag=throwing_arrow,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/return_arrow
execute as @n[tag=st_hand_loc_2,tag=throwing_arrow,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/return_arrow
execute as @n[tag=st_hand_loc_3,tag=throwing_arrow,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/return_arrow
execute as @n[tag=st_hand_loc_4,tag=throwing_arrow,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/return_arrow

execute as @n[tag=st_hand_loc_1,tag=gun_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/gun_fire
execute as @n[tag=st_hand_loc_2,tag=gun_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/gun_fire
execute as @n[tag=st_hand_loc_3,tag=gun_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/gun_fire
execute as @n[tag=st_hand_loc_4,tag=gun_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/gun_fire

execute as @n[tag=st_hand_loc_1,tag=smack_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/smack_down
execute as @n[tag=st_hand_loc_2,tag=smack_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/smack_down
execute as @n[tag=st_hand_loc_3,tag=smack_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/smack_down
execute as @n[tag=st_hand_loc_4,tag=smack_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/smack_down

execute as @n[tag=st_hand_loc_1,tag=punch_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/punch_fire
execute as @n[tag=st_hand_loc_2,tag=punch_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/punch_fire
execute as @n[tag=st_hand_loc_3,tag=punch_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/punch_fire
execute as @n[tag=st_hand_loc_4,tag=punch_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/punch_fire

execute as @n[tag=st_hand_loc_1,tag=summon_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/summon_chance
execute as @n[tag=st_hand_loc_2,tag=summon_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/summon_chance
execute as @n[tag=st_hand_loc_3,tag=summon_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/summon_chance
execute as @n[tag=st_hand_loc_4,tag=summon_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/summon_chance

execute as @n[tag=st_hand_loc_1,tag=vortex_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/vortex_return
execute as @n[tag=st_hand_loc_2,tag=vortex_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/vortex_return
execute as @n[tag=st_hand_loc_3,tag=vortex_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/vortex_return
execute as @n[tag=st_hand_loc_4,tag=vortex_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/vortex_return

execute as @n[tag=st_hand_loc_1,tag=crystal_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/crystal_return
execute as @n[tag=st_hand_loc_3,tag=crystal_attacking,distance=0..] if score @s Countdown matches 1 at @s run function boss:7/attack/crystal_return

scoreboard players remove @n[tag=st_hand_loc_1,distance=0..] Countdown 1
scoreboard players remove @n[tag=st_hand_loc_2,distance=0..] Countdown 1
scoreboard players remove @n[tag=st_hand_loc_3,distance=0..] Countdown 1
scoreboard players remove @n[tag=st_hand_loc_4,distance=0..] Countdown 1
