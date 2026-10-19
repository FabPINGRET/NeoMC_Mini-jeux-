# Nyxar, dragon de la Lune Noire : début du combat
execute positioned -171.5 102 178.5 run function mg:ombre/boss/nyxar_spawn
scoreboard players set $ob8 mg.st 1
scoreboard players set $obr8 mg.st 0
scoreboard players set $obp8 mg.st 0
scoreboard players set $obt8_0 mg.st 9
scoreboard players set $obt8_1 mg.st 17
scoreboard players set $obt8_2 mg.st 21
scoreboard players set $obt8_3 mg.st 14
bossbar set mg:olb8 value 1024
execute positioned -171.5 102 178.5 as @a[tag=mg.olw,gamemode=adventure,distance=..37] run function mg:ombre/cs/boss_nyxar
execute as @e[tag=mg.olb_nyxar] run data merge entity @s {NoAI:1b}
schedule function mg:ombre/boss/wake 120t
