scoreboard players set boss:fs_motor Value 5
scoreboard players set boss:fs_jitter Value 0

execute store result score boss:fs_jitter Value run random value -5..5
scoreboard players operation boss:fs_bicep_pitch_goal Value += boss:fs_jitter Value

execute store result score boss:fs_jitter Value run random value -5..5
scoreboard players operation boss:fs_bicep_yaw_goal Value += boss:fs_jitter Value

execute store result score boss:fs_jitter Value run random value -5..5
scoreboard players operation boss:fs_forearm_pitch_goal Value += boss:fs_jitter Value

execute store result score boss:fs_jitter Value run random value -5..5
scoreboard players operation boss:fs_head_pitch_goal Value += boss:fs_jitter Value

schedule function floaty:sched/boss/8/jitter/restore 5t replace
