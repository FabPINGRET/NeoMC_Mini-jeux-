# Morvaine, la mère-sorcière : chaque seconde
execute positioned 205.5 65 -187.5 run bossbar set mg:olb3 players @a[tag=mg.olw,distance=..38]
execute store result bossbar mg:olb3 value run data get entity @e[tag=mg.olb_morvaine,limit=1] Health
execute positioned 205.5 65 -187.5 run tag @a[tag=mg.olw,distance=..20] add mg.olboss_in
execute positioned 205.5 65 -187.5 unless entity @e[tag=mg.olb_morvaine,distance=..18] run tp @e[tag=mg.olb_morvaine] 205.5 65 -187.5
execute positioned 205.5 65 -187.5 unless entity @a[tag=mg.olw,gamemode=adventure,distance=..34] run scoreboard players add $obr3 mg.st 1
execute positioned 205.5 65 -187.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..34] run scoreboard players set $obr3 mg.st 0
execute if score $obr3 mg.st matches 15.. run return run function mg:ombre/boss/morvaine_reset
execute as @e[tag=mg.olb_morvaine] store result score $hp mg.st run data get entity @s Health
execute if score $hp mg.st matches ..256 as @e[tag=mg.olb_morvaine,tag=!mg.olrage] at @s run function mg:ombre/boss/rage
scoreboard players remove $obt3_0 mg.st 1
execute if score $obt3_0 mg.st matches ..0 as @e[tag=mg.olb_morvaine,limit=1] at @s run function mg:ombre/boss/morvaine/blink
execute if score $obt3_0 mg.st matches ..0 run scoreboard players set $obt3_0 mg.st 8
scoreboard players remove $obt3_1 mg.st 1
execute if score $obt3_1 mg.st matches ..0 as @e[tag=mg.olb_morvaine,limit=1] at @s run function mg:ombre/boss/morvaine/swarm
execute if score $obt3_1 mg.st matches ..0 run scoreboard players set $obt3_1 mg.st 14
scoreboard players remove $obt3_2 mg.st 1
execute if score $obt3_2 mg.st matches ..0 as @e[tag=mg.olb_morvaine,limit=1] at @s run function mg:ombre/boss/morvaine/hex
execute if score $obt3_2 mg.st matches ..0 run scoreboard players set $obt3_2 mg.st 9
scoreboard players remove $obt3_3 mg.st 1
execute if score $obt3_3 mg.st matches ..0 as @e[tag=mg.olb_morvaine,limit=1] at @s run function mg:ombre/boss/morvaine/cloud
execute if score $obt3_3 mg.st matches ..0 run scoreboard players set $obt3_3 mg.st 11
