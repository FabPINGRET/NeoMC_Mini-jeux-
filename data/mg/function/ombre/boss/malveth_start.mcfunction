# Malveth, l'archimage : début du combat
execute positioned -171.5 67 178.5 run function mg:ombre/boss/malveth_spawn
scoreboard players set $ob7 mg.st 1
scoreboard players set $obr7 mg.st 0
scoreboard players set $obp7 mg.st 0
scoreboard players set $obt7_0 mg.st 8
scoreboard players set $obt7_1 mg.st 12
scoreboard players set $obt7_2 mg.st 4
scoreboard players set $obt7_3 mg.st 15
bossbar set mg:olb7 value 1024
execute positioned -171.5 67 178.5 as @a[tag=mg.olw,gamemode=adventure,distance=..37] run function mg:ombre/cs/boss_malveth
execute as @e[tag=mg.olb_malveth] run data merge entity @s {NoAI:1b}
schedule function mg:ombre/boss/wake 120t
