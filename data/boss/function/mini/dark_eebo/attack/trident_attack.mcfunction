execute as @a[gamemode=!spectator,tag=mg.flw] at @s run function boss:mini/dark_eebo/attack/trident_selftarget

execute at @n[tag=deebo_marker,tag=active,distance=0..] run particle minecraft:falling_water ~ ~ ~ 0.8 0.8 0.8 0 70

schedule function floaty:sched/boss/mini/dark_eebo/painting/clear 1s
tag @e[tag=deebo,distance=0..] remove active
tag @e[tag=deebo_marker,distance=0..] remove active

function boss:mini/dark_eebo/schedule_attack
