#CENTER TARGET MODES
execute if score wv_target_mode Value matches 1 as @n[tag=wv_center,distance=0..] at @s facing entity @n[gamemode=!spectator,tag=targeted,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute if score wv_target_mode Value matches 2 as @n[tag=wv_center,distance=0..] at @s facing entity @n[gamemode=!spectator,tag=targeted,distance=0..] eyes run tp @s ~ ~ ~ ~ -20
execute if score wv_target_mode Value matches 3 as @n[tag=wv_center,distance=0..] at @s facing entity @n[tag=wv_wrist,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute if score wv_target_mode Value matches 4 as @n[tag=wv_center,distance=0..] at @s facing entity @n[tag=wv_platform_target,distance=0..] eyes run tp @s ~ ~ ~ ~ -20
execute if score wv_target_mode Value matches 5 as @n[gamemode=!spectator,tag=targeted,distance=0..] at @s positioned ^ ^ ^5 facing entity @n[tag=wv_center,distance=0..] eyes rotated ~180 ~ run tp @n[tag=wv_center,distance=0..] -12384 129 355 ~ 10
execute if score wv_target_mode Value matches 6 as @n[tag=wv_center,distance=0..] at @s run tp @s ~ ~ ~ ~ -30
execute if score wv_target_mode Value matches 7 as @n[tag=wv_center,distance=0..] at @s run tp @s ~ ~ ~ 90 0


#ROTATE EYE TO CENTER AND LIMBS TO EYE
execute store result score wv_center_xrotation Value run data get entity @n[tag=wv_center,distance=0..] Rotation[0]
execute if score wv_center_xrotation Value >= 360 Value as @n[tag=wv_center,distance=0..] at @s run tp @s ~ ~ ~ ~-360 ~
execute if score wv_center_xrotation Value < 0 Value as @n[tag=wv_center,distance=0..] at @s run tp @s ~ ~ ~ ~360 ~
execute store result score wv_eye_xrotation Value run data get entity @n[tag=wv_model_eye,tag=origin,distance=0..] Rotation[0]
execute if score wv_eye_xrotation Value >= 360 Value as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~-360 ~
execute if score wv_eye_xrotation Value < 0 Value as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~360 ~
scoreboard players operation wv_center_eye_xdelta Value = wv_center_xrotation Value
scoreboard players operation wv_center_eye_xdelta Value -= wv_eye_xrotation Value

execute store result score wv_center_yrotation Value run data get entity @n[tag=wv_center,distance=0..] Rotation[1]
execute store result score wv_eye_yrotation Value run data get entity @n[tag=wv_model_eye,tag=origin,distance=0..] Rotation[1]
scoreboard players operation wv_center_eye_ydelta Value = wv_center_yrotation Value
scoreboard players operation wv_center_eye_ydelta Value -= wv_eye_yrotation Value

#SPEED
#-1
execute if score wv_eye_speed Value matches -1 if score wv_center_eye_xdelta Value matches ..0 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~-0.6 ~
execute if score wv_eye_speed Value matches -1 if score wv_center_eye_xdelta Value matches 0.. as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~0.6 ~

execute if score wv_eye_speed Value matches -1 if score wv_center_eye_ydelta Value matches ..0 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~ ~-0.6
execute if score wv_eye_speed Value matches -1 if score wv_center_eye_ydelta Value matches 0.. as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~ ~0.6

#0
execute if score wv_eye_speed Value matches 0 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated as @n[tag=wv_center,distance=0..] run scoreboard players set wv_focused bool 1
execute if score wv_eye_speed Value matches 0 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated as @n[tag=wv_center,distance=0..] run tp @s ~ ~ ~ ~ ~

#1
execute if score wv_eye_speed Value matches 1 unless score wv_center_eye_xdelta Value matches -2..2 if score wv_center_eye_xdelta Value matches ..0 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~-4 ~
execute if score wv_eye_speed Value matches 1 unless score wv_center_eye_xdelta Value matches -2..2 if score wv_center_eye_xdelta Value matches 0.. as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~4 ~

execute if score wv_eye_speed Value matches 1 unless score wv_center_eye_ydelta Value matches -2..2 if score wv_center_eye_ydelta Value matches ..0 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~ ~-4
execute if score wv_eye_speed Value matches 1 unless score wv_center_eye_ydelta Value matches -2..2 if score wv_center_eye_ydelta Value matches 0.. as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~ ~4

execute if score wv_eye_speed Value matches 1 if score wv_center_eye_xdelta Value matches -2..2 if score wv_center_eye_ydelta Value matches -2..2 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated as @n[tag=wv_center,distance=0..] run scoreboard players set wv_focused bool 1
execute if score wv_eye_speed Value matches 1 if score wv_center_eye_xdelta Value matches -2..2 if score wv_center_eye_ydelta Value matches -2..2 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated as @n[tag=wv_center,distance=0..] run tp @s ~ ~ ~ ~ ~

#2
execute if score wv_eye_speed Value matches 2 unless score wv_center_eye_xdelta Value matches -5..5 if score wv_center_eye_xdelta Value matches ..0 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~-10 ~
execute if score wv_eye_speed Value matches 2 unless score wv_center_eye_xdelta Value matches -5..5 if score wv_center_eye_xdelta Value matches 0.. as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~10 ~

execute if score wv_eye_speed Value matches 2 unless score wv_center_eye_ydelta Value matches -5..5 if score wv_center_eye_ydelta Value matches ..0 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~ ~-10
execute if score wv_eye_speed Value matches 2 unless score wv_center_eye_ydelta Value matches -5..5 if score wv_center_eye_ydelta Value matches 0.. as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~ ~10

execute if score wv_eye_speed Value matches 2 if score wv_center_eye_xdelta Value matches -5..5 if score wv_center_eye_ydelta Value matches -5..5 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated as @n[tag=wv_center,distance=0..] run scoreboard players set wv_focused bool 1
execute if score wv_eye_speed Value matches 2 if score wv_center_eye_xdelta Value matches -5..5 if score wv_center_eye_ydelta Value matches -5..5 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated as @n[tag=wv_center,distance=0..] run tp @s ~ ~ ~ ~ ~


#CROWN
execute as @n[tag=wv_model_crown,tag=origin,distance=0..] at @s rotated as @n[tag=wv_model_eye,distance=0..] run tp @s ~ ~ ~ ~ 0

#WRIST
execute if score wv_wrist_speed Value matches 0 as @n[tag=wv_wrist,distance=0..] run tp @s @n[tag=wv_wrist_dest,distance=0..]

execute if score wv_wrist_speed Value matches 1 as @n[tag=wv_wrist,distance=0..] at @s facing entity @n[tag=wv_wrist_dest,distance=0..] eyes unless entity @n[tag=wv_wrist_dest,distance=..1] run tp @s ^ ^ ^1
execute if score wv_wrist_speed Value matches 1 as @n[tag=wv_wrist,distance=0..] at @s facing entity @n[tag=wv_wrist_dest,distance=0..] eyes if entity @n[tag=wv_wrist_dest,distance=..1] run tp @s @n[tag=wv_wrist_dest,distance=0..]

execute if score wv_wrist_speed Value matches 2 as @n[tag=wv_wrist,distance=0..] at @s facing entity @n[tag=wv_wrist_dest,distance=0..] eyes unless entity @n[tag=wv_wrist_dest,distance=..2] run tp @s ^ ^ ^2
execute if score wv_wrist_speed Value matches 2 as @n[tag=wv_wrist,distance=0..] at @s facing entity @n[tag=wv_wrist_dest,distance=0..] eyes if entity @n[tag=wv_wrist_dest,distance=..2] run tp @s @n[tag=wv_wrist_dest,distance=0..]

execute if score wv_wrist_speed Value matches 3 as @n[tag=wv_wrist,distance=0..] at @s facing entity @n[tag=wv_wrist_dest,distance=0..] eyes unless entity @n[tag=wv_wrist_dest,distance=..4] run tp @s ^ ^ ^4
execute if score wv_wrist_speed Value matches 3 as @n[tag=wv_wrist,distance=0..] at @s facing entity @n[tag=wv_wrist_dest,distance=0..] eyes if entity @n[tag=wv_wrist_dest,distance=..4] run tp @s @n[tag=wv_wrist_dest,distance=0..]

execute if score wv_wrist_speed Value matches 4 as @n[tag=wv_wrist,distance=0..] at @s facing entity @n[tag=wv_wrist_dest,distance=0..] eyes unless entity @n[tag=wv_wrist_dest,distance=..8] run tp @s ^ ^ ^8
execute if score wv_wrist_speed Value matches 4 as @n[tag=wv_wrist,distance=0..] at @s facing entity @n[tag=wv_wrist_dest,distance=0..] eyes if entity @n[tag=wv_wrist_dest,distance=..8] run tp @s @n[tag=wv_wrist_dest,distance=0..]

#SWORD
tp @n[tag=wv_model_sword,tag=origin,tag=!cutscene,distance=0..] @n[tag=wv_wrist,distance=0..]

#ARM 2
execute as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^7 ^ ^4 positioned ~ 130 ~ run tp @n[tag=wv_elbow2,distance=0..] ~ ~ ~

#ELBOW

#FOREARM
tp @n[tag=wv_model_forearm,tag=origin,distance=0..] @n[tag=wv_wrist,distance=0..]
execute as @n[tag=wv_model_forearm,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @n[tag=wv_model_forearm,tag=origin,distance=0..] at @s positioned ^ ^ ^16.375 run tp @n[tag=wv_model_bicep,tag=origin,distance=0..] ~ ~ ~ ~ ~

#BICEP
execute as @n[tag=wv_model_bicep,tag=origin,distance=0..] at @s facing entity @n[tag=wv_model_eye,tag=origin,distance=0..] eyes run tp @s ~ ~ ~ ~ ~

#ARM 2
execute as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s positioned ^ ^ ^8 run tp @n[tag=wv_model_forearm2,tag=origin,distance=0..] ~ ~ ~ ~90 -90
execute if score wv_fire_color bool matches 0 as @n[tag=wv_model_forearm2,tag=origin,distance=0..] at @s positioned ^ ^ ^3.8 run particle minecraft:soul_fire_flame ~ ~ ~ 0.2 0.2 0.2 0 2
execute if score wv_fire_color bool matches 1 as @n[tag=wv_model_forearm2,tag=origin,distance=0..] at @s positioned ^ ^ ^3.8 run particle minecraft:flame ~ ~ ~ 0.2 0.2 0.2 0 2

#SMALL ARM
execute as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^5 ^ ^5 positioned ~ ~-3 ~ run tp @n[tag=wv_smallarm,distance=0..] ~ ~ ~
execute as @n[tag=wv_model_smallarm,tag=origin,distance=0..] at @s facing entity @n[tag=wv_smallarm,distance=0..] eyes run tp @s ~ ~ ~ ~ ~

#POSES ---------------
# 1: IDLE
#Elbow
execute if score wv_pose Value matches 1 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-15 ^2 ^
#Wrist
execute if score wv_pose Value matches 1 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^-6 ^ ^12 positioned ~ 125 ~ run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 1 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s rotated as @n[tag=wv_model_crown,tag=origin,distance=0..] run tp @s ~ ~ ~ ~-10 25
#Arm 2
execute if score wv_pose Value matches 1 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -10

# 2: PREPARE TO SPIKE
#Elbow
execute if score wv_pose Value matches 2 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-15 ^2 ^
#Wrist
execute if score wv_pose Value matches 2 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^ ^ ^22 positioned ~ 137 ~ run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 2 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s rotated as @n[tag=wv_model_crown,tag=origin,distance=0..] run tp @s ~ ~ ~ ~ 90
#Arm 2
execute if score wv_pose Value matches 2 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -10

# 3: SPIKE
#Elbow
execute if score wv_pose Value matches 3 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-15 ^2 ^
#Wrist
execute if score wv_pose Value matches 3 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^ ^ ^22 positioned ~ 128 ~ run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 3 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s rotated as @n[tag=wv_model_crown,tag=origin,distance=0..] run tp @s ~ ~ ~ ~ 90
#Arm 2
execute if score wv_pose Value matches 3 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -10

# 4: SPIKE DOWN
#Elbow
execute if score wv_pose Value matches 4 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-15 ^2 ^
#Wrist
execute if score wv_pose Value matches 4 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^ ^ ^22 positioned ~ 126 ~ run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 4 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s rotated as @n[tag=wv_model_crown,tag=origin,distance=0..] run tp @s ~ ~ ~ ~ 90
#Arm 2
execute if score wv_pose Value matches 4 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -10

# 5: EYE LASER
#Elbow
execute if score wv_pose Value matches 5 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-15 ^2 ^
#Wrist
execute if score wv_pose Value matches 5 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^-6 ^ ^12 positioned ~ 123 ~ run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 5 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s rotated as @n[tag=wv_model_crown,tag=origin,distance=0..] run tp @s ~ ~ ~ ~-80 90
#Arm 2
execute if score wv_pose Value matches 5 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -10

# 6: PREP CHOP
#Elbow
execute if score wv_pose Value matches 6 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-15 ^5 ^
#Wrist
execute if score wv_pose Value matches 6 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^-2 ^ ^10 positioned ~ 134 ~ run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 6 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s rotated as @n[tag=wv_model_crown,tag=origin,distance=0..] run tp @s ~ ~ ~ ~-10 ~-30
#Arm 2
execute if score wv_pose Value matches 6 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -10

# 7: CHOP_NEAR
#Elbow
execute if score wv_pose Value matches 7 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-15 ^ ^
#Wrist
execute if score wv_pose Value matches 7 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^ ^ ^19 positioned ~ 124 ~ run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 7 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s rotated as @n[tag=wv_model_crown,tag=origin,distance=0..] run tp @s ~ ~ ~ ~ 90
#Arm 2
execute if score wv_pose Value matches 7 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -10

# 8: CHOP_FAR
#Elbow
execute if score wv_pose Value matches 8 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-15 ^ ^
#Wrist
execute if score wv_pose Value matches 8 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^ ^ ^24 positioned ~ 124 ~ run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 8 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s rotated as @n[tag=wv_model_crown,tag=origin,distance=0..] run tp @s ~ ~ ~ ~ 90
#Arm 2
execute if score wv_pose Value matches 8 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -10

# 9: PREP STAB
#Elbow
execute if score wv_pose Value matches 9 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-15 ^-2 ^
#Wrist
execute if score wv_pose Value matches 9 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^ ^ ^12 positioned ~ 125 ~ run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 9 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s rotated as @n[tag=wv_model_crown,tag=origin,distance=0..] run tp @s ~ ~ ~ ~ ~10
#Arm 2
execute if score wv_pose Value matches 9 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -10

# 10: STAB
#Elbow
execute if score wv_pose Value matches 10 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-15 ^-2 ^
#Wrist
execute if score wv_pose Value matches 10 as @n[tag=wv_stab_loc,distance=0..] at @s run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 10 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s rotated as @n[tag=wv_model_crown,tag=origin,distance=0..] run tp @s ~ ~ ~ ~ ~10
#Arm 2
execute if score wv_pose Value matches 10 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -10

# 11: SKULLS
#Elbow
execute if score wv_pose Value matches 11 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-15 ^2 ^
#Wrist
execute if score wv_pose Value matches 11 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^ ^ ^11 positioned ~ 122 ~ run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 11 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s rotated as @n[tag=wv_model_crown,tag=origin,distance=0..] run tp @s ~ ~ ~ ~ ~
#Arm 2
execute if score wv_pose Value matches 11 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -90

# 12: SUMMON
#Elbow
execute if score wv_pose Value matches 12 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-15 ^2 ^
#Wrist
execute if score wv_pose Value matches 12 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^-3 ^ ^11 positioned ~ 124 ~ run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 12 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s rotated as @n[tag=wv_model_crown,tag=origin,distance=0..] run tp @s ~ ~ ~ ~-90 90
#Arm 2
execute if score wv_pose Value matches 12 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ 10

# 13: LIGHTNING
#Elbow
execute if score wv_pose Value matches 13 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-15 ^2 ^
#Wrist
execute if score wv_pose Value matches 13 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^ ^ ^11 positioned ~ 124 ~ run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 13 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s rotated as @n[tag=wv_model_crown,tag=origin,distance=0..] run tp @s ~ ~ ~ ~-90 45
#Arm 2
execute if score wv_pose Value matches 13 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -10

# 14: CUTSCENE
#Elbow
execute if score wv_pose Value matches 14 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-9 ^2 ^
#Wrist
execute if score wv_pose Value matches 14 run tp @n[tag=wv_wrist_dest,distance=0..] -12384 109 355
#Sword
execute if score wv_pose Value matches 14 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~ ~
#Arm 2
execute if score wv_pose Value matches 14 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -10

# 15: CUTSCENE 2
#Elbow
execute if score wv_pose Value matches 15 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-9 ^2 ^-2
#Wrist
#execute if score wv_pose Value matches 15 as @n[tag=wv_model_eye,tag=origin] at @s rotated ~ 0 positioned ^ ^ ^ positioned ~ ~21.5 ~ run tp @n[tag=wv_wrist_dest] ~ ~ ~
execute if score wv_pose Value matches 15 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^ ^ ^ run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 15 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~ ~
#Arm 2
execute if score wv_pose Value matches 15 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -10

# 16: CUTSCENE 3
#Elbow
execute if score wv_pose Value matches 16 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 run tp @n[tag=wv_elbow,distance=0..] ^-9 ^2 ^
#Wrist
execute if score wv_pose Value matches 16 as @n[tag=wv_model_eye,tag=origin,distance=0..] at @s rotated ~ 0 positioned ^ ^ ^ positioned ~ ~11.5 ~ run tp @n[tag=wv_wrist_dest,distance=0..] ~ ~ ~
#Sword
execute if score wv_pose Value matches 16 as @n[tag=wv_model_sword,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~ ~
#Arm 2
execute if score wv_pose Value matches 16 as @n[tag=wv_model_bicep2,tag=origin,distance=0..] at @s facing entity @n[tag=wv_elbow2,distance=0..] eyes run tp @s ~ ~ ~ ~ -10


#LORDSWORD --------------
execute if score lordsword_mode bool matches 0 as @n[tag=wv_lordsword,tag=origin,distance=0..] at @s rotated ~ -90 run tp @s ~ ~ ~ ~7 ~
execute if score lordsword_mode bool matches 0 as @n[tag=wv_lordsword,tag=origin,distance=0..] at @s positioned ~ 123.5 ~ run tag @a[gamemode=!spectator,distance=..1.25,tag=mg.flw] add lordsword_armed
execute if score lordsword_mode bool matches 0 if entity @a[tag=lordsword_armed,tag=mg.flw] at @a[tag=lordsword_armed,tag=mg.flw] run playsound minecraft:item.armor.equip_diamond master @a[tag=mg.flw] ~ ~ ~
execute if score lordsword_mode bool matches 0 if entity @a[tag=lordsword_armed,tag=mg.flw] run scoreboard players set lordsword_mode bool 1
execute if score lordsword_mode bool matches 1 as @n[tag=wv_lordsword,tag=origin,distance=0..] at @n[tag=lordsword_armed,distance=0..] rotated as @n[tag=lordsword_armed,distance=0..] positioned ~ ~1 ~ positioned ^ ^ ^1 run tp @s ~ ~ ~ ~ ~
execute if score lordsword_mode bool matches 1 if score @n[tag=lordsword_armed,distance=0..] sneak_last matches 1.. at @n[tag=lordsword_armed,distance=0..] run playsound minecraft:item.trident.throw master @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute if score lordsword_mode bool matches 1 if score @n[tag=lordsword_armed,distance=0..] sneak_last matches 1.. run scoreboard players set lordsword_mode bool 2
execute if score lordsword_mode bool matches 2 run tag @a[tag=mg.flw] remove lordsword_armed
execute if score lordsword_mode bool matches 2 as @n[tag=wv_lordsword,tag=origin,distance=0..] at @s if block ^ ^ ^ #hb_passthrough run tp @s ^ ^ ^2
execute if score lordsword_mode bool matches 2 as @n[tag=wv_lordsword,tag=origin,distance=0..] at @s unless block ^ ^ ^-1 #hb_passthrough run function boss:final/virus/sword_explode
execute if score lordsword_mode bool matches 2 as @n[tag=wv_lordsword,tag=origin,distance=0..] at @s unless block ^ ^ ^-0.5 #hb_passthrough run function boss:final/virus/sword_explode
execute if score lordsword_mode bool matches 2 as @n[tag=wv_lordsword,tag=origin,distance=0..] at @s unless block ^ ^ ^ #hb_passthrough run function boss:final/virus/sword_explode

execute if score lordsword_mode bool matches 2 if score wv_one_left bool matches 1 as @n[tag=wv_lordsword,tag=origin,distance=0..] at @s if entity @n[tag=wv_center,distance=..1.5] run function boss:final/virus/kill


#sword particles
execute as @n[tag=wv_model_flamesword,distance=0..] at @s positioned ^ ^ ^1 run particle flame ~ ~ ~ 0.5 0.5 0.5 0 1
execute as @n[tag=wv_model_forestsword,distance=0..] at @s positioned ^ ^ ^1 run particle totem_of_undying ~ ~ ~ 0.5 0.5 0.5 0 1
execute as @n[tag=wv_model_sporessword,distance=0..] at @s positioned ^ ^ ^1 run particle mycelium ~ ~ ~ 0.5 0.5 0.5 0 1
execute as @n[tag=wv_model_stonesword,distance=0..] at @s positioned ^ ^ ^1 run particle block{block_state:"stone"} ~ ~ ~ 0.5 0.5 0.5 0 1
execute as @n[tag=wv_model_icesword,distance=0..] at @s positioned ^ ^ ^1 run particle electric_spark ~ ~ ~ 0.5 0.5 0.5 0 1
execute as @n[tag=wv_model_watersword,distance=0..] at @s positioned ^ ^ ^1 run particle splash ~ ~ ~ 0.5 0.5 0.5 0 1
execute as @n[tag=wv_model_valorsword,distance=0..] at @s positioned ^ ^ ^1 run particle sculk_soul ~ ~ ~ 0.5 0.5 0.5 0 1

#Misc particles
execute as @e[tag=wv_skull,distance=0..] at @s run particle minecraft:trial_omen ~ ~ ~ 0.1 0.1 0.1 0 1
#execute as @e[tag=wv_skull] at @s run particle minecraft:soul_fire_flame ~ ~ ~ 0.2 0.2 0.2 0 1

execute as @e[tag=m_caster,distance=0..] at @s if block ~ ~-0.1 ~ black_stained_glass run kill @s
