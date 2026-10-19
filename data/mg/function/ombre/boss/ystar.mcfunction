# Ysh'tar, la reine-araignée : chaque seconde
execute positioned -204.5 72 -204.5 run bossbar set mg:olb1 players @a[tag=mg.olw,distance=..39]
execute store result bossbar mg:olb1 value run data get entity @e[tag=mg.olb_ystar,limit=1] Health
execute positioned -204.5 72 -204.5 run tag @a[tag=mg.olw,distance=..21] add mg.olboss_in
execute positioned -204.5 72 -204.5 unless entity @e[tag=mg.olb_ystar,distance=..19] run tp @e[tag=mg.olb_ystar] -204.5 72 -204.5
execute positioned -204.5 72 -204.5 unless entity @a[tag=mg.olw,gamemode=adventure,distance=..35] run scoreboard players add $obr1 mg.st 1
execute positioned -204.5 72 -204.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..35] run scoreboard players set $obr1 mg.st 0
execute if score $obr1 mg.st matches 15.. run return run function mg:ombre/boss/ystar_reset
execute as @e[tag=mg.olb_ystar] store result score $hp mg.st run data get entity @s Health
execute if score $hp mg.st matches ..162 as @e[tag=mg.olb_ystar,tag=!mg.olrage] at @s run function mg:ombre/boss/rage
scoreboard players remove $obt1_0 mg.st 1
execute if score $obt1_0 mg.st matches ..0 as @e[tag=mg.olb_ystar,limit=1] at @s run function mg:ombre/boss/ystar/web
execute if score $obt1_0 mg.st matches ..0 run scoreboard players set $obt1_0 mg.st 6
scoreboard players remove $obt1_1 mg.st 1
execute if score $obt1_1 mg.st matches ..0 as @e[tag=mg.olb_ystar,limit=1] at @s run function mg:ombre/boss/ystar/brood
execute if score $obt1_1 mg.st matches ..0 run scoreboard players set $obt1_1 mg.st 15
scoreboard players remove $obt1_2 mg.st 1
execute if score $obt1_2 mg.st matches ..0 as @e[tag=mg.olb_ystar,limit=1] at @s run function mg:ombre/boss/ystar/venom
execute if score $obt1_2 mg.st matches ..0 run scoreboard players set $obt1_2 mg.st 8
scoreboard players remove $obt1_3 mg.st 1
execute if score $obt1_3 mg.st matches ..0 as @e[tag=mg.olb_ystar,limit=1] at @s run function mg:ombre/boss/ystar/leap
execute if score $obt1_3 mg.st matches ..0 run scoreboard players set $obt1_3 mg.st 10
