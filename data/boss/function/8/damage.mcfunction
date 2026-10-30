scoreboard players remove boss:fs BossHealth 1

execute as @n[tag=frostbyte_head,distance=0..] at @s run playsound minecraft:entity.snow_golem.death hostile @a[tag=mg.flw] ~ ~ ~ 3 0.1
execute as @n[tag=frostbyte_head,distance=0..] at @s run playsound minecraft:block.conduit.attack.target hostile @a[tag=mg.flw] ~ ~ ~ 3 0.1
execute as @n[tag=frostbyte_head,distance=0..] at @s run playsound minecraft:entity.allay.hurt hostile @a[tag=mg.flw] ~ ~ ~ 3 0.5

execute if score boss:fs BossHealth matches 9 run bossbar set boss:fs value 9
execute if score boss:fs BossHealth matches 8 run bossbar set boss:fs value 8
execute if score boss:fs BossHealth matches 7 run bossbar set boss:fs value 7
execute if score boss:fs BossHealth matches 6 run bossbar set boss:fs value 6
execute if score boss:fs BossHealth matches 5 run bossbar set boss:fs value 5
execute if score boss:fs BossHealth matches 5 run bossbar set boss:fs color yellow
execute if score boss:fs BossHealth matches 4 run bossbar set boss:fs value 4
execute if score boss:fs BossHealth matches 3 run bossbar set boss:fs value 3
execute if score boss:fs BossHealth matches 2 run bossbar set boss:fs value 2
execute if score boss:fs BossHealth matches 1 run bossbar set boss:fs value 1
execute if score boss:fs BossHealth matches 1 run bossbar set boss:fs color red
execute if score boss:fs BossHealth matches 0 run bossbar set boss:fs value 0

execute if score boss:fs BossHealth matches 0 run setblock -10832 67 365 redstone_block
