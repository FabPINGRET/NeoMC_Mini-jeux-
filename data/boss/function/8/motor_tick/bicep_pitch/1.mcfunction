execute if score boss:fs_bicep_pitch Value < boss:fs_bicep_pitch_goal Value as @n[tag=frostbyte_bicep,distance=0..] at @s run tp @s ~ ~ ~ ~ ~1
execute if score boss:fs_bicep_pitch Value < boss:fs_bicep_pitch_goal Value run scoreboard players add boss:fs_bicep_pitch Value 1
execute if score boss:fs_bicep_pitch Value > boss:fs_bicep_pitch_goal Value as @n[tag=frostbyte_bicep,distance=0..] at @s run tp @s ~ ~ ~ ~ ~-1
execute if score boss:fs_bicep_pitch Value > boss:fs_bicep_pitch_goal Value run scoreboard players remove boss:fs_bicep_pitch Value 1
