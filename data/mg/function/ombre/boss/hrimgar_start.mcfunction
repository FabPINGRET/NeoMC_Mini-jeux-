# Hrimgar, le géant du givre : début du combat
execute positioned 30.5 105 -204.5 run function mg:ombre/boss/hrimgar_spawn
scoreboard players set $ob2 mg.st 1
scoreboard players set $obr2 mg.st 0
scoreboard players set $obp2 mg.st 0
scoreboard players set $obt2_0 mg.st 10
scoreboard players set $obt2_1 mg.st 13
scoreboard players set $obt2_2 mg.st 12
scoreboard players set $obt2_3 mg.st 28
bossbar set mg:olb2 value 1000
execute positioned 30.5 105 -204.5 as @a[tag=mg.olw,gamemode=adventure,distance=..39] run function mg:ombre/cs/boss_hrimgar
execute as @e[tag=mg.olb_hrimgar] run data merge entity @s {NoAI:1b}
schedule function mg:ombre/boss/wake 120t
