execute store result score boss:fs_bicep_pitch Value run data get entity @n[tag=frostbyte_bicep,distance=0..] Rotation[1]
execute store result score boss:fs_bicep_yaw Value run data get entity @n[tag=frostbyte_bicep,distance=0..] Rotation[0]
execute store result score boss:fs_forearm_pitch Value run data get entity @n[tag=frostbyte_forearm,distance=0..] Rotation[1]
execute store result score boss:fs_head_pitch Value run data get entity @n[tag=frostbyte_head,distance=0..] Rotation[1]

scoreboard players add boss:fs_bicep_yaw Value 90

execute as @n[tag=frostbyte_head,distance=0..] at @s run tp @s ~ ~ ~ -90 ~
