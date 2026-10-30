execute as @e[tag=boss_skt_ectobeam_slime,distance=0..] at @s run particle minecraft:totem_of_undying ~ ~ ~ 0.1 0.1 0.1 0.2 1
execute as @e[tag=boss_skt_ectobeam_slime,distance=0..] at @s as @a[distance=..3,tag=mg.flw] run damage @s 16 minecraft:mob_attack by @n[tag=boss_skt_ectobeam_slime,distance=0..]

execute positioned -10222 97 434 as @e[tag=boss_skt_ectobeam_slime,distance=8..] at @s if block ~ ~ ~ minecraft:white_stained_glass run setblock -10196 55 416 minecraft:redstone_block
execute positioned -10222 97 434 as @e[tag=boss_skt_ectobeam_slime,distance=8..] at @s if block ~ ~ ~ minecraft:lime_stained_glass run setblock -10196 55 416 minecraft:redstone_block

execute positioned -10222 97 434 as @e[tag=boss_skt_ectobeam_slime,sort=furthest,limit=1,distance=0..] at @s run playsound minecraft:block.azalea.break hostile @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute positioned -10222 97 434 as @e[tag=boss_skt_ectobeam_slime,sort=furthest,limit=1,distance=0..] at @s run playsound minecraft:block.bamboo.break hostile @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned -10222 97 434 as @e[tag=boss_skt_ectobeam_slime,sort=furthest,limit=1,distance=0..] at @s run playsound minecraft:item.bucket.empty_powder_snow hostile @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned -10222 97 434 as @e[tag=boss_skt_ectobeam_slime,sort=furthest,limit=1,distance=0..] at @s run playsound minecraft:entity.warden.sonic_boom hostile @a[tag=mg.flw] ~ ~ ~ 1 2

tp @e[tag=boss_skt_ectobeam_slime,distance=0..] ~ -100 ~
kill @e[tag=boss_skt_ectobeam_slime,distance=0..]

execute if block -10196 55 411 stone run schedule function floaty:sched/boss/5/pick_attack 3s
