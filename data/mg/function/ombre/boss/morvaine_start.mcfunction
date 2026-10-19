# Morvaine, la mère-sorcière : début du combat
execute positioned 205.5 65 -187.5 run function mg:ombre/boss/morvaine_spawn
scoreboard players set $ob3 mg.st 1
scoreboard players set $obr3 mg.st 0
scoreboard players set $obp3 mg.st 0
scoreboard players set $obt3_0 mg.st 11
scoreboard players set $obt3_1 mg.st 17
scoreboard players set $obt3_2 mg.st 12
scoreboard players set $obt3_3 mg.st 14
bossbar set mg:olb3 value 1024
execute positioned 205.5 65 -187.5 as @a[tag=mg.olw,gamemode=adventure,distance=..36] run function mg:ombre/cs/boss_morvaine
execute as @e[tag=mg.olb_morvaine] run data merge entity @s {NoAI:1b}
schedule function mg:ombre/boss/wake 120t
