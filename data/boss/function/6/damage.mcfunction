scoreboard players remove boss:sh BossHealth 1
execute as @n[tag=boss_sh_loc,distance=0..] at @s run playsound minecraft:entity.slime.hurt hostile @a[tag=mg.flw] ~ ~ ~ 2 0.7
execute as @n[tag=boss_sh_loc,distance=0..] at @s run playsound minecraft:entity.camel.hurt hostile @a[tag=mg.flw] ~ ~ ~ 3 0.7
execute as @n[tag=boss_sh_loc,distance=0..] at @s run playsound minecraft:entity.warden.hurt hostile @a[tag=mg.flw] ~ ~ ~ 3 2

execute if score boss:sh BossHealth matches 9 run bossbar set boss:sh value 9
execute if score boss:sh BossHealth matches 8 run bossbar set boss:sh value 8
execute if score boss:sh BossHealth matches 7 run bossbar set boss:sh value 7
execute if score boss:sh BossHealth matches 6 run bossbar set boss:sh value 6
execute if score boss:sh BossHealth matches 5 run bossbar set boss:sh value 5
execute if score boss:sh BossHealth matches 5 run bossbar set boss:sh color yellow
execute if score boss:sh BossHealth matches 4 run bossbar set boss:sh value 4
execute if score boss:sh BossHealth matches 3 run bossbar set boss:sh value 3
execute if score boss:sh BossHealth matches 2 run bossbar set boss:sh value 2
execute if score boss:sh BossHealth matches 1 run bossbar set boss:sh value 1
execute if score boss:sh BossHealth matches 1 run bossbar set boss:sh color red
execute if score boss:sh BossHealth matches 0 run bossbar set boss:sh value 0

fill -10502 79 -86 -10470 79 -54 minecraft:iron_bars replace minecraft:honey_block
fill -10502 79 -86 -10470 79 -54 minecraft:iron_bars replace minecraft:iron_bars

setblock -10478 42 -72 minecraft:black_wool

execute if score boss:sh BossHealth matches 0 run setblock -10504 42 -46 redstone_block
