execute as @n[tag=deebo_marker,tag=active,distance=0..] at @s positioned ^ ^ ^1 positioned ~ 187 ~ as @a[gamemode=!spectator,tag=mg.flw] run function summon:smearblin

execute at @n[tag=deebo_marker,tag=active,distance=0..] run particle minecraft:enchant ~ ~ ~ 0.8 0.8 0.8 0 70
execute at @n[tag=deebo_marker,tag=active,distance=0..] run playsound minecraft:block.enchantment_table.use hostile @a[tag=mg.flw] ~ 186 ~ 1 0.8

schedule function floaty:sched/boss/mini/dark_eebo/painting/clear 1s
tag @e[tag=deebo,distance=0..] remove active
tag @e[tag=deebo_marker,distance=0..] remove active

function boss:mini/dark_eebo/schedule_attack
