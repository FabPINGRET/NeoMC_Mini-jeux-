scoreboard players remove boss:sop BossHealth 1
playsound minecraft:entity.enderman.hurt hostile @a[tag=mg.flw] -9934 191 148 1 0.1 1
playsound minecraft:entity.ghast.warn hostile @a[tag=mg.flw] -9934 191 148 1 2 1

execute if score boss:sop BossHealth matches 9 run bossbar set boss:sop value 9
execute if score boss:sop BossHealth matches 8 run bossbar set boss:sop value 8
execute if score boss:sop BossHealth matches 7 run bossbar set boss:sop value 7
execute if score boss:sop BossHealth matches 6 run bossbar set boss:sop value 6
execute if score boss:sop BossHealth matches 5 run bossbar set boss:sop value 5
execute if score boss:sop BossHealth matches 5 run bossbar set boss:sop color yellow
execute if score boss:sop BossHealth matches 4 run bossbar set boss:sop value 4
execute if score boss:sop BossHealth matches 3 run bossbar set boss:sop value 3
execute if score boss:sop BossHealth matches 2 run bossbar set boss:sop value 2
execute if score boss:sop BossHealth matches 1 run bossbar set boss:sop value 1
execute if score boss:sop BossHealth matches 1 run bossbar set boss:sop color red
execute if score boss:sop BossHealth matches 0 run bossbar set boss:sop value 0
