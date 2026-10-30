function boss:mini/dark_eebo/painting/clear
function boss:mini/dark_eebo/select_active_random

function boss:mini/dark_eebo/painting/deebo_1
schedule function floaty:sched/boss/mini/dark_eebo/painting/deebo_2 0.6s
schedule function floaty:sched/boss/mini/dark_eebo/painting/deebo_3 1.2s

execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s run tp @n[tag=deebo_stand,distance=0..] ^ ^ ^-2
execute as @n[tag=deebo_stand,distance=0..] at @s rotated as @n[tag=deebo_marker,tag=active,distance=0..] run tp @s ~ ~ ~ ~ ~

schedule function floaty:sched/boss/mini/dark_eebo/attack/deebo_out_attack 3.5s replace
setblock -11549 173 -171 minecraft:white_wool
