execute store result score boss:fs_bicep_yaw_goal Value run random value -62..62

scoreboard players set boss:fs_bicep_pitch_goal Value 70
scoreboard players set boss:fs_forearm_pitch_goal Value 80
scoreboard players set boss:fs_head_pitch_goal Value 0

execute if score boss:fs BossHealth matches 0..4 store result score boss:fs_forearm_pitch_goal Value run random value 0..80
