# Le Colosse de runes : début du combat
execute positioned 0.5 67 188.5 run function mg:ombre/boss/colosse_spawn
scoreboard players set $ob6 mg.st 1
scoreboard players set $obr6 mg.st 0
scoreboard players set $obp6 mg.st 0
scoreboard players set $obt6_0 mg.st 11
scoreboard players set $obt6_1 mg.st 9
scoreboard players set $obt6_2 mg.st 18
scoreboard players set $obt6_3 mg.st 4
bossbar set mg:olb6 value 1024
execute positioned 0.5 67 188.5 as @a[tag=mg.olw,gamemode=adventure,distance=..40] run function mg:ombre/cs/boss_colosse
execute as @e[tag=mg.olb_colosse] run data merge entity @s {NoAI:1b}
schedule function mg:ombre/boss/wake 120t
