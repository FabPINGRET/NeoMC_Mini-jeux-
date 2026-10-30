scoreboard players remove boss:secret BossHealth 1

execute if score boss:secret BossHealth matches 6 run bossbar set boss:secret value 6
execute if score boss:secret BossHealth matches 5 run bossbar set boss:secret value 5
execute if score boss:secret BossHealth matches 4 run bossbar set boss:secret value 4
execute if score boss:secret BossHealth matches 3 run bossbar set boss:secret value 3
execute if score boss:secret BossHealth matches 3 run bossbar set boss:secret color yellow
execute if score boss:secret BossHealth matches 2 run bossbar set boss:secret value 2
execute if score boss:secret BossHealth matches 1 run bossbar set boss:secret value 1
execute if score boss:secret BossHealth matches 1 run bossbar set boss:secret color red
execute if score boss:secret BossHealth matches 0 run bossbar set boss:secret value 0

execute at @n[tag=sc_boss_pos,distance=0..] run playsound minecraft:entity.wither.hurt hostile @a[tag=mg.flw] ~ ~ ~ 5 0.7
execute at @n[tag=sc_boss_pos,distance=0..] run playsound minecraft:entity.happy_ghast.hurt hostile @a[tag=mg.flw] ~ ~ ~ 5 0.7
execute as @n[tag=sc_boss_pos,distance=0..] at @s positioned ~ ~3 ~ run particle minecraft:witch ~ ~ ~ 1 1 1 1 400

execute if score boss:secret BossHealth matches 4..6 run schedule function floaty:sched/boss/secret/pick_attack 3s
execute if score boss:secret BossHealth matches 1..2 run schedule function floaty:sched/boss/secret/pick_attack 3s

execute if score boss:secret BossHealth matches 3 run schedule function floaty:sched/boss/secret/attack/do_ring_spawn 3s
execute if score boss:secret BossHealth matches 0 run function boss:secret/win
