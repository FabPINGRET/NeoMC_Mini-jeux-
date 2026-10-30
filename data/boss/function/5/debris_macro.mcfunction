setblock -10204 55 423 minecraft:redstone_block
scoreboard players set boss:skt shortray 10
execute as @a[gamemode=!spectator,tag=mg.flw] run function boss:5/debris_summon
execute as @e[tag=boss_skt_tail,limit=1,distance=0..] at @s run playsound minecraft:entity.phantom.ambient hostile @a[tag=mg.flw] ~ ~ ~ 4 0.1

execute if block -10196 55 411 stone run schedule function floaty:sched/boss/5/pick_attack 10s replace
