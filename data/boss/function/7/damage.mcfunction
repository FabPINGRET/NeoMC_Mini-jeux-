scoreboard players remove boss:st BossHealth 1

execute if score boss:st BossHealth matches 6 run bossbar set boss:st value 6
execute if score boss:st BossHealth matches 5 run bossbar set boss:st value 5
execute if score boss:st BossHealth matches 4 run bossbar set boss:st value 4
execute if score boss:st BossHealth matches 3 run bossbar set boss:st value 3
execute if score boss:st BossHealth matches 3 run bossbar set boss:st color yellow
execute if score boss:st BossHealth matches 2 run bossbar set boss:st value 2
execute if score boss:st BossHealth matches 1 run bossbar set boss:st value 1
execute if score boss:st BossHealth matches 1 run bossbar set boss:st color red
execute if score boss:st BossHealth matches 0 run bossbar set boss:st value 0

kill @e[tag=st_hand_shadow_1,distance=0..]
kill @e[tag=st_hand_shadow_2,distance=0..]
kill @e[tag=st_hand_shadow_3,distance=0..]
kill @e[tag=st_hand_shadow_4,distance=0..]

execute as @e[tag=st_hand_dest,distance=0..] run function boss:7/target/none
tag @a[tag=mg.flw] remove targeted
setblock -10446 -48 -392 air

schedule clear floaty:sched/boss/7/target_check

execute if score boss:st BossHealth > 0 Value run playsound minecraft:entity.iron_golem.hurt hostile @a[tag=mg.flw] -10473 -21 -378 3 0.5
execute if score boss:st BossHealth > 0 Value run playsound minecraft:entity.ravager.hurt hostile @a[tag=mg.flw] -10473 -21 -378 3 0.5
execute if score boss:st BossHealth > 0 Value run playsound minecraft:entity.creaking.spawn hostile @a[tag=mg.flw] -10473 -21 -378 2 2

#execute if score boss:st BossHealth matches 0 run WIN

execute if score boss:st BossHealth matches 0 run setblock -10446 -48 -376 minecraft:redstone_block
