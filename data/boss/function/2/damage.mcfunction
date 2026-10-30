scoreboard players remove boss:cob BossHealth 1
playsound minecraft:entity.skeleton_horse.hurt hostile @a[tag=mg.flw] -10153 155 -31 1 2 1
playsound minecraft:entity.stray.hurt hostile @a[tag=mg.flw] -10153 155 -31 1 0.1 1
playsound minecraft:entity.strider.retreat hostile @a[tag=mg.flw] -10153 155 -31 1 1 1

execute if score boss:cob BossHealth matches 9 run bossbar set boss:cob value 9
execute if score boss:cob BossHealth matches 8 run bossbar set boss:cob value 8
execute if score boss:cob BossHealth matches 7 run bossbar set boss:cob value 7
execute if score boss:cob BossHealth matches 6 run bossbar set boss:cob value 6
execute if score boss:cob BossHealth matches 5 run bossbar set boss:cob value 5
execute if score boss:cob BossHealth matches 5 run bossbar set boss:cob color yellow
execute if score boss:cob BossHealth matches 4 run bossbar set boss:cob value 4
execute if score boss:cob BossHealth matches 3 run bossbar set boss:cob value 3
execute if score boss:cob BossHealth matches 2 run bossbar set boss:cob value 2
execute if score boss:cob BossHealth matches 1 run bossbar set boss:cob value 1
execute if score boss:cob BossHealth matches 1 run bossbar set boss:cob color red
execute if score boss:cob BossHealth matches 0 run bossbar set boss:cob value 0
