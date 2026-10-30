#function boss:8/query_angles

scoreboard players set boss:fs_targeting Value 3

execute as @n[tag=frostbyte_head,distance=0..] at @s run tp @s ~ ~ ~ -90 ~
scoreboard players set boss:fs_head_pitch_goal Value 0
