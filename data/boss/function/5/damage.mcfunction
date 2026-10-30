scoreboard players remove boss:skt BossHealth 1

#execute unless score boss:skt BossHealth matches 0 run setblock ~ ~ ~ stone

execute if score boss:skt BossHealth matches 5 run bossbar set boss:skt value 5
execute if score boss:skt BossHealth matches 4 run bossbar set boss:skt value 4
execute if score boss:skt BossHealth matches 3 run bossbar set boss:skt value 3
execute if score boss:skt BossHealth matches 3 run bossbar set boss:skt color yellow
execute if score boss:skt BossHealth matches 2 run bossbar set boss:skt value 2
execute if score boss:skt BossHealth matches 1 run bossbar set boss:skt value 1
execute if score boss:skt BossHealth matches 1 run bossbar set boss:skt color red
execute if score boss:skt BossHealth matches 0 run bossbar set boss:skt value 0

kill @e[tag=r_soul,distance=0..]
execute if score boss:skt BossHealth matches 0 run kill @e[tag=boss_5_debris,distance=0..]
execute if score boss:skt BossHealth matches 0 run setblock -10215 55 405 redstone_block

#Stop giving darkness effect
setblock -10196 56 413 air
