execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s positioned ^ ^ ^1 run summon area_effect_cloud ~ 187 ~ {NoGravity:1b,Radius:5.5f,RadiusPerTick:-0.01f,Duration:120,potion_contents:{potion:"minecraft:strong_poison"}}

execute at @n[tag=deebo_marker,tag=active,distance=0..] run particle minecraft:sneeze ~ ~ ~ 0.8 0.8 0.8 0 70
execute at @n[tag=deebo_marker,tag=active,distance=0..] run playsound minecraft:block.brewing_stand.brew hostile @a[tag=mg.flw] ~ 186 ~ 1 0.8

schedule function floaty:sched/boss/mini/dark_eebo/painting/clear 1s
tag @e[tag=deebo,distance=0..] remove active
tag @e[tag=deebo_marker,distance=0..] remove active

function boss:mini/dark_eebo/schedule_attack
