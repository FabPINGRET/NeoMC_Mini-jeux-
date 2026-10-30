execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s run playsound minecraft:item.crossbow.shoot hostile @a[tag=mg.flw] ~ ~ ~ 2 1

execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^ ^-0.35 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch
execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^ ^-0.6 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch
execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^ ^-1 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch
execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^0.2 ^-0.6 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch
execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^-0.2 ^-0.6 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch
execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^0.2 ^-1 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch
execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^0.2 ^-0.35 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch
execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^-0.2 ^-1 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch
execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^-0.2 ^-0.35 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch

execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^-0.4 ^-0.35 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch
execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^-0.4 ^-0.6 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch
execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^-0.4 ^-1 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch

execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^0.4 ^-0.35 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch
execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^0.4 ^-0.6 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch
execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s facing ^0.4 ^-1 ^1 run function boss:mini/dark_eebo/attack/crossbow_launch

execute at @n[tag=deebo_marker,tag=active,distance=0..] run particle minecraft:flame ~ ~ ~ 0.8 0.8 0.8 0 70

schedule function floaty:sched/boss/mini/dark_eebo/painting/clear 1s
tag @e[tag=deebo,distance=0..] remove active
tag @e[tag=deebo_marker,distance=0..] remove active

function boss:mini/dark_eebo/schedule_attack
