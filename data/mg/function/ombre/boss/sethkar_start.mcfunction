# Sethkar, le pharaon-liche : début du combat
execute positioned 198.5 65 -27.5 run function mg:ombre/boss/sethkar_spawn
scoreboard players set $ob4 mg.st 1
scoreboard players set $obr4 mg.st 0
scoreboard players set $obp4 mg.st 0
scoreboard players set $obt4_0 mg.st 16
scoreboard players set $obt4_1 mg.st 19
scoreboard players set $obt4_2 mg.st 10
scoreboard players set $obt4_3 mg.st 4
bossbar set mg:olb4 value 1024
execute positioned 198.5 65 -27.5 as @a[tag=mg.olw,gamemode=adventure,distance=..34] run function mg:ombre/cs/boss_sethkar
execute as @e[tag=mg.olb_sethkar] run data merge entity @s {NoAI:1b}
schedule function mg:ombre/boss/wake 120t
