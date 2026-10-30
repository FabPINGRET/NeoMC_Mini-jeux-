execute if score boss:fs_head_pitch Value < boss:fs_head_pitch_goal Value as @n[tag=frostbyte_head,distance=0..] at @s run tp @s ~ ~ ~ ~ ~2
execute if score boss:fs_head_pitch Value < boss:fs_head_pitch_goal Value run scoreboard players add boss:fs_head_pitch Value 2
execute if score boss:fs_head_pitch Value > boss:fs_head_pitch_goal Value as @n[tag=frostbyte_head,distance=0..] at @s run tp @s ~ ~ ~ ~ ~-2
execute if score boss:fs_head_pitch Value > boss:fs_head_pitch_goal Value run scoreboard players remove boss:fs_head_pitch Value 2
