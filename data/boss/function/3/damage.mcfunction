scoreboard players remove boss:lod BossHealth 1
execute at @e[tag=lod_boss_loc,distance=0..] run playsound minecraft:entity.ravager.hurt hostile @a[tag=mg.flw] ~ ~ ~ 2 0.7


execute if score boss:lod BossHealth matches 6 run bossbar set boss:lod value 6
execute if score boss:lod BossHealth matches 5 run bossbar set boss:lod value 5
execute if score boss:lod BossHealth matches 4 run bossbar set boss:lod value 4
execute if score boss:lod BossHealth matches 3 run bossbar set boss:lod value 3
execute if score boss:lod BossHealth matches 3 run bossbar set boss:lod color yellow
execute if score boss:lod BossHealth matches 2 run bossbar set boss:lod value 2
execute if score boss:lod BossHealth matches 1 run bossbar set boss:lod value 1
execute if score boss:lod BossHealth matches 1 run bossbar set boss:lod color red
execute if score boss:lod BossHealth matches 0 run bossbar set boss:lod value 0
