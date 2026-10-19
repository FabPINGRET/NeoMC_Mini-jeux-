# Ignarok, dragon de feu : début du combat
execute positioned 180.5 117 180.5 run function mg:ombre/boss/ignarok_spawn
scoreboard players set $ob5 mg.st 1
scoreboard players set $obr5 mg.st 0
scoreboard players set $obp5 mg.st 0
scoreboard players set $obt5_0 mg.st 9
scoreboard players set $obt5_1 mg.st 15
scoreboard players set $obt5_2 mg.st 25
scoreboard players set $obt5_3 mg.st 11
bossbar set mg:olb5 value 1024
execute positioned 180.5 117 180.5 as @a[tag=mg.olw,gamemode=adventure,distance=..38] run function mg:ombre/cs/boss_ignarok
execute as @e[tag=mg.olb_ignarok] run data merge entity @s {NoAI:1b}
schedule function mg:ombre/boss/wake 120t
