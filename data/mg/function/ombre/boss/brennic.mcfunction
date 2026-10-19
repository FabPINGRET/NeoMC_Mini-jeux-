# Brennic, seigneur des brigands : chaque seconde
execute positioned -204.5 71 -41.5 run bossbar set mg:olb0 players @a[tag=mg.olw,distance=..44]
execute store result bossbar mg:olb0 value run data get entity @e[tag=mg.olb_brennic,limit=1] Health
execute positioned -204.5 71 -41.5 run tag @a[tag=mg.olw,distance=..26] add mg.olboss_in
execute positioned -204.5 71 -41.5 unless entity @e[tag=mg.olb_brennic,distance=..24] run tp @e[tag=mg.olb_brennic] -206.5 71 -41.5
execute positioned -204.5 71 -41.5 unless entity @a[tag=mg.olw,gamemode=adventure,distance=..40] run scoreboard players add $obr0 mg.st 1
execute positioned -204.5 71 -41.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..40] run scoreboard players set $obr0 mg.st 0
execute if score $obr0 mg.st matches 15.. run return run function mg:ombre/boss/brennic_reset
execute as @e[tag=mg.olb_brennic] store result score $hp mg.st run data get entity @s Health
execute if score $hp mg.st matches ..80 as @e[tag=mg.olb_brennic,tag=!mg.olrage] at @s run function mg:ombre/boss/rage
scoreboard players remove $obt0_0 mg.st 1
execute if score $obt0_0 mg.st matches ..0 as @e[tag=mg.olb_brennic,limit=1] at @s run function mg:ombre/boss/brennic/whirl
execute if score $obt0_0 mg.st matches ..0 run scoreboard players set $obt0_0 mg.st 7
scoreboard players remove $obt0_1 mg.st 1
execute if score $obt0_1 mg.st matches ..0 as @e[tag=mg.olb_brennic,limit=1] at @s run function mg:ombre/boss/brennic/call
execute if score $obt0_1 mg.st matches ..0 run scoreboard players set $obt0_1 mg.st 20
scoreboard players remove $obt0_2 mg.st 1
execute if score $obt0_2 mg.st matches ..0 as @e[tag=mg.olb_brennic,limit=1] at @s run function mg:ombre/boss/brennic/charge
execute if score $obt0_2 mg.st matches ..0 run scoreboard players set $obt0_2 mg.st 11
