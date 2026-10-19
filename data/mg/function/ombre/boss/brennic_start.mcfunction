# Brennic, seigneur des brigands : début du combat
execute positioned -206.5 71 -41.5 run function mg:ombre/boss/brennic_spawn
scoreboard players set $ob0 mg.st 1
scoreboard players set $obr0 mg.st 0
scoreboard players set $obp0 mg.st 0
scoreboard players set $obt0_0 mg.st 10
scoreboard players set $obt0_1 mg.st 23
scoreboard players set $obt0_2 mg.st 14
bossbar set mg:olb0 value 320
execute positioned -204.5 71 -41.5 as @a[tag=mg.olw,gamemode=adventure,distance=..42] run function mg:ombre/cs/boss_brennic
execute as @e[tag=mg.olb_brennic] run data merge entity @s {NoAI:1b}
schedule function mg:ombre/boss/wake 120t
