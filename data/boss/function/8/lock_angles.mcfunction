execute store result score boss:fs_bicep_pitch_goal Value run data get entity @n[tag=frostbyte_bicep,distance=0..] Rotation[1]
execute store result score boss:fs_bicep_yaw_goal Value run data get entity @n[tag=frostbyte_bicep,distance=0..] Rotation[0]
execute store result score boss:fs_forearm_pitch_goal Value run data get entity @n[tag=frostbyte_forearm,distance=0..] Rotation[1]
execute store result score boss:fs_head_pitch_goal Value run data get entity @n[tag=frostbyte_head,distance=0..] Rotation[1]

scoreboard players add boss:fs_bicep_yaw_goal Value 90
