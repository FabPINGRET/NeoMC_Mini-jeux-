execute unless score boss:fs_bicep_pitch_storage Value matches -999 run scoreboard players operation boss:fs_bicep_pitch_goal Value = boss:fs_bicep_pitch_storage Value
execute unless score boss:fs_bicep_yaw_storage Value matches -999 run scoreboard players operation boss:fs_bicep_yaw_goal Value = boss:fs_bicep_yaw_storage Value
execute unless score boss:fs_forearm_pitch_storage Value matches -999 run scoreboard players operation boss:fs_forearm_pitch_goal Value = boss:fs_forearm_pitch_storage Value
execute unless score boss:fs_head_pitch_storage Value matches -999 run scoreboard players operation boss:fs_head_pitch_goal Value = boss:fs_head_pitch_storage Value
execute unless score boss:fs_motor_storage Value matches -999 run scoreboard players operation boss:fs_motor Value = boss:fs_motor_storage Value

scoreboard players set boss:fs_bicep_pitch_storage Value -999
scoreboard players set boss:fs_bicep_yaw_storage Value -999
scoreboard players set boss:fs_forearm_pitch_storage Value -999
scoreboard players set boss:fs_head_pitch_storage Value -999
scoreboard players set boss:fs_motor_storage Value -999
