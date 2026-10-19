# Sethkar, le pharaon-liche : chaque seconde
execute positioned 198.5 65 -27.5 run bossbar set mg:olb4 players @a[tag=mg.olw,distance=..36]
execute store result bossbar mg:olb4 value run data get entity @e[tag=mg.olb_sethkar,limit=1] Health
execute positioned 198.5 65 -27.5 run tag @a[tag=mg.olw,distance=..18] add mg.olboss_in
execute positioned 198.5 65 -27.5 unless entity @e[tag=mg.olb_sethkar,distance=..16] run tp @e[tag=mg.olb_sethkar] 198.5 65 -27.5
execute positioned 198.5 65 -27.5 unless entity @a[tag=mg.olw,gamemode=adventure,distance=..32] run scoreboard players add $obr4 mg.st 1
execute positioned 198.5 65 -27.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..32] run scoreboard players set $obr4 mg.st 0
execute if score $obr4 mg.st matches 15.. run return run function mg:ombre/boss/sethkar_reset
execute as @e[tag=mg.olb_sethkar] store result score $hp mg.st run data get entity @s Health
execute if score $hp mg.st matches ..256 as @e[tag=mg.olb_sethkar,tag=!mg.olrage] at @s run function mg:ombre/boss/rage
scoreboard players remove $obt4_0 mg.st 1
execute if score $obt4_0 mg.st matches ..0 as @e[tag=mg.olb_sethkar,limit=1] at @s run function mg:ombre/boss/sethkar/storm
execute if score $obt4_0 mg.st matches ..0 run scoreboard players set $obt4_0 mg.st 13
scoreboard players remove $obt4_1 mg.st 1
execute if score $obt4_1 mg.st matches ..0 as @e[tag=mg.olb_sethkar,limit=1] at @s run function mg:ombre/boss/sethkar/mummies
execute if score $obt4_1 mg.st matches ..0 run scoreboard players set $obt4_1 mg.st 16
scoreboard players remove $obt4_2 mg.st 1
execute if score $obt4_2 mg.st matches ..0 as @e[tag=mg.olb_sethkar,limit=1] at @s run function mg:ombre/boss/sethkar/beam
execute if score $obt4_2 mg.st matches ..0 run scoreboard players set $obt4_2 mg.st 7
scoreboard players remove $obt4_3 mg.st 1
execute if score $obt4_3 mg.st matches ..0 as @e[tag=mg.olb_sethkar,limit=1] at @s run function mg:ombre/boss/sethkar/jars
execute if score $obt4_3 mg.st matches ..0 run scoreboard players set $obt4_3 mg.st 1
