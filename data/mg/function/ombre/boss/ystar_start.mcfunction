# Ysh'tar, la reine-araignée : début du combat
execute positioned -204.5 72 -204.5 run function mg:ombre/boss/ystar_spawn
scoreboard players set $ob1 mg.st 1
scoreboard players set $obr1 mg.st 0
scoreboard players set $obp1 mg.st 0
scoreboard players set $obt1_0 mg.st 9
scoreboard players set $obt1_1 mg.st 18
scoreboard players set $obt1_2 mg.st 11
scoreboard players set $obt1_3 mg.st 13
bossbar set mg:olb1 value 650
execute positioned -204.5 72 -204.5 as @a[tag=mg.olw,gamemode=adventure,distance=..37] run function mg:ombre/cs/boss_ystar
execute as @e[tag=mg.olb_ystar] run data merge entity @s {NoAI:1b}
schedule function mg:ombre/boss/wake 120t
