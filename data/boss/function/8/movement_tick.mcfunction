execute if score boss:fs_targeting Value matches 2 as @n[tag=frostbyte_head,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] feet run tp @s ~ ~ ~ ~ ~
execute if score boss:fs_targeting Value matches 3 as @n[tag=frostbyte_bicep,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] feet run tp @s ~ ~ ~ ~ ~
execute if score boss:fs_targeting Value matches 4 as @n[tag=frostbyte_head,distance=0..] at @s facing entity @n[tag=frostbyte_lightning_loc,distance=0..] feet run tp @s ~ ~ ~ ~ ~

#Set joint speed to master Motor speed
scoreboard players operation boss:fs_bicep_pitch_speed Value = boss:fs_motor Value
scoreboard players operation boss:fs_bicep_yaw_speed Value = boss:fs_motor Value
scoreboard players operation boss:fs_forearm_pitch_speed Value = boss:fs_motor Value
scoreboard players operation boss:fs_head_pitch_speed Value = boss:fs_motor Value

#Reduce speed if joint is close and speed is too high
execute if score boss:fs_bicep_pitch Value > boss:fs_bicep_pitch_goal Value run scoreboard players operation boss:fs_bicep_pitch_delta Value = boss:fs_bicep_pitch Value
execute if score boss:fs_bicep_pitch Value > boss:fs_bicep_pitch_goal Value run scoreboard players operation boss:fs_bicep_pitch_delta Value -= boss:fs_bicep_pitch_goal Value
execute if score boss:fs_bicep_pitch_goal Value > boss:fs_bicep_pitch Value run scoreboard players operation boss:fs_bicep_pitch_delta Value = boss:fs_bicep_pitch_goal Value
execute if score boss:fs_bicep_pitch_goal Value > boss:fs_bicep_pitch Value run scoreboard players operation boss:fs_bicep_pitch_delta Value -= boss:fs_bicep_pitch Value
execute if score boss:fs_bicep_pitch_delta Value < boss:fs_motor Value run scoreboard players operation boss:fs_bicep_pitch_speed Value = boss:fs_bicep_pitch_delta Value

#execute if score boss:fs_bicep_pitch Value = boss:fs_bicep_pitch_goal Value run scoreboard players set boss:fs_bicep_pitch_speed Value 0

execute if score boss:fs_bicep_yaw Value > boss:fs_bicep_yaw_goal Value run scoreboard players operation boss:fs_bicep_yaw_delta Value = boss:fs_bicep_yaw Value
execute if score boss:fs_bicep_yaw Value > boss:fs_bicep_yaw_goal Value run scoreboard players operation boss:fs_bicep_yaw_delta Value -= boss:fs_bicep_yaw_goal Value
execute if score boss:fs_bicep_yaw_goal Value > boss:fs_bicep_yaw Value run scoreboard players operation boss:fs_bicep_yaw_delta Value = boss:fs_bicep_yaw_goal Value
execute if score boss:fs_bicep_yaw_goal Value > boss:fs_bicep_yaw Value run scoreboard players operation boss:fs_bicep_yaw_delta Value -= boss:fs_bicep_yaw Value
execute if score boss:fs_bicep_yaw_delta Value < boss:fs_motor Value run scoreboard players operation boss:fs_bicep_yaw_speed Value = boss:fs_bicep_yaw_delta Value

execute if score boss:fs_forearm_pitch Value > boss:fs_forearm_pitch_goal Value run scoreboard players operation boss:fs_forearm_pitch_delta Value = boss:fs_forearm_pitch Value
execute if score boss:fs_forearm_pitch Value > boss:fs_forearm_pitch_goal Value run scoreboard players operation boss:fs_forearm_pitch_delta Value -= boss:fs_forearm_pitch_goal Value
execute if score boss:fs_forearm_pitch_goal Value > boss:fs_forearm_pitch Value run scoreboard players operation boss:fs_forearm_pitch_delta Value = boss:fs_forearm_pitch_goal Value
execute if score boss:fs_forearm_pitch_goal Value > boss:fs_forearm_pitch Value run scoreboard players operation boss:fs_forearm_pitch_delta Value -= boss:fs_forearm_pitch Value
execute if score boss:fs_forearm_pitch_delta Value < boss:fs_motor Value run scoreboard players operation boss:fs_forearm_pitch_speed Value = boss:fs_forearm_pitch_delta Value

execute if score boss:fs_head_pitch Value > boss:fs_head_pitch_goal Value run scoreboard players operation boss:fs_head_pitch_delta Value = boss:fs_head_pitch Value
execute if score boss:fs_head_pitch Value > boss:fs_head_pitch_goal Value run scoreboard players operation boss:fs_head_pitch_delta Value -= boss:fs_head_pitch_goal Value
execute if score boss:fs_head_pitch_goal Value > boss:fs_head_pitch Value run scoreboard players operation boss:fs_head_pitch_delta Value = boss:fs_head_pitch_goal Value
execute if score boss:fs_head_pitch_goal Value > boss:fs_head_pitch Value run scoreboard players operation boss:fs_head_pitch_delta Value -= boss:fs_head_pitch Value
execute if score boss:fs_head_pitch_delta Value < boss:fs_motor Value run scoreboard players operation boss:fs_head_pitch_speed Value = boss:fs_head_pitch_delta Value

execute if score boss:fs_bicep_pitch_speed Value matches 5 run function boss:8/motor_tick/bicep_pitch/5
execute if score boss:fs_bicep_pitch_speed Value matches 4 run function boss:8/motor_tick/bicep_pitch/4
execute if score boss:fs_bicep_pitch_speed Value matches 3 run function boss:8/motor_tick/bicep_pitch/3
execute if score boss:fs_bicep_pitch_speed Value matches 2 run function boss:8/motor_tick/bicep_pitch/2
execute if score boss:fs_bicep_pitch_speed Value matches 1 run function boss:8/motor_tick/bicep_pitch/1

execute if score boss:fs_bicep_yaw_speed Value matches 5 run function boss:8/motor_tick/bicep_yaw/5
execute if score boss:fs_bicep_yaw_speed Value matches 4 run function boss:8/motor_tick/bicep_yaw/4
execute if score boss:fs_bicep_yaw_speed Value matches 3 run function boss:8/motor_tick/bicep_yaw/3
execute if score boss:fs_bicep_yaw_speed Value matches 2 run function boss:8/motor_tick/bicep_yaw/2
execute if score boss:fs_bicep_yaw_speed Value matches 1 run function boss:8/motor_tick/bicep_yaw/1

execute if score boss:fs_forearm_pitch_speed Value matches 5 run function boss:8/motor_tick/forearm_pitch/5
execute if score boss:fs_forearm_pitch_speed Value matches 4 run function boss:8/motor_tick/forearm_pitch/4
execute if score boss:fs_forearm_pitch_speed Value matches 3 run function boss:8/motor_tick/forearm_pitch/3
execute if score boss:fs_forearm_pitch_speed Value matches 2 run function boss:8/motor_tick/forearm_pitch/2
execute if score boss:fs_forearm_pitch_speed Value matches 1 run function boss:8/motor_tick/forearm_pitch/1

execute if score boss:fs_head_pitch_speed Value matches 5 run function boss:8/motor_tick/head_pitch/5
execute if score boss:fs_head_pitch_speed Value matches 4 run function boss:8/motor_tick/head_pitch/4
execute if score boss:fs_head_pitch_speed Value matches 3 run function boss:8/motor_tick/head_pitch/3
execute if score boss:fs_head_pitch_speed Value matches 2 run function boss:8/motor_tick/head_pitch/2
execute if score boss:fs_head_pitch_speed Value matches 1 run function boss:8/motor_tick/head_pitch/1

#Position Forearm
execute as @n[tag=frostbyte_bicep,distance=0..] at @s positioned ^ ^ ^10 run tp @n[tag=frostbyte_forearm,distance=0..] ~ ~ ~

#Position Head
execute as @n[tag=frostbyte_forearm,distance=0..] at @s positioned ^ ^ ^6 run tp @n[tag=frostbyte_head,distance=0..] ~ ~ ~

#Draw Bicep
execute as @n[tag=frostbyte_bicep,distance=0..] at @s facing ^ ^ ^1 positioned ~ ~2 ~ run tp @n[tag=frostbyte_bicep_draw,distance=0..] ~ ~ ~ ~ ~

#Draw Forearm
execute as @n[tag=frostbyte_forearm,distance=0..] at @s facing ^ ^ ^1 positioned ~ ~2 ~ run tp @n[tag=frostbyte_forearm_draw,distance=0..] ~ ~ ~ ~ ~

#Draw Head
execute as @n[tag=frostbyte_head,distance=0..] at @s facing ^ ^ ^1 positioned ~ ~2 ~ run tp @n[tag=frostbyte_head_draw,distance=0..] ~ ~ ~ ~ ~


#OTHER

execute as @n[tag=frostbyte_shrapnel,tag=draw,distance=0..] at @s run particle minecraft:electric_spark ~ ~2 ~ 0.5 0.5 0.5 0.3 4 normal
execute as @n[tag=frostbyte_shrapnel,tag=pos,distance=0..] at @s run tp @n[tag=frostbyte_shrapnel,tag=draw,distance=0..] ~ ~-2 ~
execute as @e[type=arrow,nbt={inGround:1b,Tags:["frostbyte_shrapnel_arrow"]},distance=0..] run kill @s
execute as @n[tag=frostbyte_shrapnel,tag=pos,distance=0..] at @s unless block ~ ~-0.1 ~ air run setblock -10835 67 390 minecraft:redstone_block

function boss:8/crystal/tick
