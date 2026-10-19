# Le Colosse de runes : chaque seconde
execute positioned 0.5 67 188.5 run bossbar set mg:olb6 players @a[tag=mg.olw,distance=..42]
execute store result bossbar mg:olb6 value run data get entity @e[tag=mg.olb_colosse,limit=1] Health
execute positioned 0.5 67 188.5 run tag @a[tag=mg.olw,distance=..24] add mg.olboss_in
execute positioned 0.5 67 188.5 unless entity @e[tag=mg.olb_colosse,distance=..22] run tp @e[tag=mg.olb_colosse] 0.5 67 188.5
execute positioned 0.5 67 188.5 unless entity @a[tag=mg.olw,gamemode=adventure,distance=..38] run scoreboard players add $obr6 mg.st 1
execute positioned 0.5 67 188.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..38] run scoreboard players set $obr6 mg.st 0
execute if score $obr6 mg.st matches 15.. run return run function mg:ombre/boss/colosse_reset
execute as @e[tag=mg.olb_colosse] store result score $hp mg.st run data get entity @s Health
execute if score $hp mg.st matches ..256 as @e[tag=mg.olb_colosse,tag=!mg.olrage] at @s run function mg:ombre/boss/rage
scoreboard players remove $obt6_0 mg.st 1
execute if score $obt6_0 mg.st matches ..0 as @e[tag=mg.olb_colosse,limit=1] at @s run function mg:ombre/boss/colosse/quake
execute if score $obt6_0 mg.st matches ..0 run scoreboard players set $obt6_0 mg.st 8
scoreboard players remove $obt6_1 mg.st 1
execute if score $obt6_1 mg.st matches ..0 as @e[tag=mg.olb_colosse,limit=1] at @s run function mg:ombre/boss/colosse/beam
execute if score $obt6_1 mg.st matches ..0 run scoreboard players set $obt6_1 mg.st 6
scoreboard players remove $obt6_2 mg.st 1
execute if score $obt6_2 mg.st matches ..0 as @e[tag=mg.olb_colosse,limit=1] at @s run function mg:ombre/boss/colosse/rocks
execute if score $obt6_2 mg.st matches ..0 run scoreboard players set $obt6_2 mg.st 15
scoreboard players remove $obt6_3 mg.st 1
execute if score $obt6_3 mg.st matches ..0 as @e[tag=mg.olb_colosse,limit=1] at @s run function mg:ombre/boss/colosse/shield
execute if score $obt6_3 mg.st matches ..0 run scoreboard players set $obt6_3 mg.st 1
