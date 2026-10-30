execute as @n[tag=frostbyte_bicep,distance=0..] at @s run tp @s ~ ~ ~ -90 0
scoreboard players set boss:fs_bicep_pitch Value 0
scoreboard players set boss:fs_bicep_pitch_goal Value 0
scoreboard players set boss:fs_bicep_yaw Value 0
scoreboard players set boss:fs_bicep_yaw_goal Value 0
execute as @n[tag=frostbyte_forearm,distance=0..] at @s run tp @s ~ ~ ~ -90 0
scoreboard players set boss:fs_forearm_pitch Value 0
scoreboard players set boss:fs_forearm_pitch_goal Value 0
execute as @n[tag=frostbyte_head,distance=0..] at @s run tp @s ~ ~ ~ -90 0
scoreboard players set boss:fs_head_pitch Value 0
scoreboard players set boss:fs_head_pitch_goal Value 0

scoreboard players set boss:fs_motor Value 1
