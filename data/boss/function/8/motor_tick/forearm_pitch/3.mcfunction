execute if score boss:fs_forearm_pitch Value < boss:fs_forearm_pitch_goal Value as @n[tag=frostbyte_forearm,distance=0..] at @s run tp @s ~ ~ ~ ~ ~3
execute if score boss:fs_forearm_pitch Value < boss:fs_forearm_pitch_goal Value run scoreboard players add boss:fs_forearm_pitch Value 3
execute if score boss:fs_forearm_pitch Value > boss:fs_forearm_pitch_goal Value as @n[tag=frostbyte_forearm,distance=0..] at @s run tp @s ~ ~ ~ ~ ~-3
execute if score boss:fs_forearm_pitch Value > boss:fs_forearm_pitch_goal Value run scoreboard players remove boss:fs_forearm_pitch Value 3
