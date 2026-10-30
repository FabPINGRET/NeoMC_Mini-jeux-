execute positioned -12384 123 355 run playsound minecraft:block.conduit.deactivate master @a[tag=mg.flw] ~ ~ ~ 5 0.5

execute as @e[tag=wv_morbex_tumor,distance=0..] run data merge entity @s {start_interpolation:0,interpolation_duration:20,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.5f,2.5f,1.5f]}}

schedule function floaty:sched/boss/final/cutscene/23 1s replace
#Start fight tick
setblock -12346 43 342 minecraft:redstone_block
function boss:final/virus/display/pose/cutscene
function boss:final/virus/display/target/cutscene
scoreboard players set wv_eye_speed Value 0
scoreboard players set wv_wrist_speed Value 0

function boss:final/virus/setup/joints
function boss:final/virus/setup/models



#","color":"white"},{"text":"
