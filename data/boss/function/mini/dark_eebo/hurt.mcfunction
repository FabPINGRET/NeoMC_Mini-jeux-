scoreboard players set deebo_painting Value 0
setblock -11549 173 -171 minecraft:black_wool
scoreboard players remove boss:deebo BossHealth 1
execute store result bossbar boss:dark_eebo value run scoreboard players get boss:deebo BossHealth

execute if score boss:deebo BossHealth matches 3 run bossbar set boss:dark_eebo color yellow
execute if score boss:deebo BossHealth matches 1 run bossbar set boss:dark_eebo color red

execute if score boss:deebo BossHealth matches 0 run setblock -11552 173 -179 redstone_block


tp @n[tag=deebo_stand,distance=0..] -11538 220 -183

execute at @n[tag=deebo_marker,tag=active,distance=0..] run particle dust_color_transition{from_color:[1.000,0.204,0.220],to_color:[0.110,0.808,0.859],scale:3} ~ ~0.5 ~ 0.3 0.3 0.3 0 70 normal
execute at @n[tag=deebo_marker,tag=active,distance=0..] run playsound minecraft:entity.witch.death hostile @a[tag=mg.flw] ~ ~ ~ 1 1.7

schedule clear floaty:sched/boss/mini/dark_eebo/attack/deebo_out_attack
schedule clear floaty:sched/boss/mini/dark_eebo/attack/deebo_out_start

function boss:mini/dark_eebo/painting/clear

execute if score boss:deebo BossHealth matches 1.. run function boss:mini/dark_eebo/schedule_attack
