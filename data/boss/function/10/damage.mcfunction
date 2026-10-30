scoreboard players remove boss:ta BossHealth 1

execute if score boss:ta BossHealth matches 6 run bossbar set boss:ta value 6
execute if score boss:ta BossHealth matches 5 run bossbar set boss:ta value 5
execute if score boss:ta BossHealth matches 4 run bossbar set boss:ta value 4
execute if score boss:ta BossHealth matches 3 run bossbar set boss:ta value 3
execute if score boss:ta BossHealth matches 3 run bossbar set boss:ta color yellow
execute if score boss:ta BossHealth matches 2 run bossbar set boss:ta value 2
execute if score boss:ta BossHealth matches 1 run bossbar set boss:ta value 1
execute if score boss:ta BossHealth matches 1 run bossbar set boss:ta color red
execute if score boss:ta BossHealth matches 0 run bossbar set boss:ta value 0

#execute if score boss:ta BossHealth matches 0 run schedule function boss:9/win 0.1s
#execute if score boss:ta BossHealth matches 0 run schedule function boss:9/cutscene/lord_1 2s

#Stop damage check
setblock -11804 203 351 air

function boss:10/phase_2_out
execute if score boss:ta BossHealth matches 2..6 run schedule function floaty:sched/boss/10/phase_1_in 5s
execute if score boss:ta BossHealth matches 1 run setblock -11798 202 313 minecraft:redstone_block
execute if score boss:ta BossHealth matches 0 run function boss:10/win_1
