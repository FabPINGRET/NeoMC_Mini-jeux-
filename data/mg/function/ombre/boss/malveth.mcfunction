# Malveth, l'archimage : chaque seconde
execute positioned -171.5 67 178.5 run bossbar set mg:olb7 players @a[tag=mg.olw,distance=..39]
execute store result bossbar mg:olb7 value run data get entity @e[tag=mg.olb_malveth,limit=1] Health
execute positioned -171.5 67 178.5 run tag @a[tag=mg.olw,distance=..21] add mg.olboss_in
execute positioned -171.5 67 178.5 unless entity @e[tag=mg.olb_malveth,distance=..19] run tp @e[tag=mg.olb_malveth] -171.5 67 178.5
execute positioned -171.5 67 178.5 unless entity @a[tag=mg.olw,gamemode=adventure,distance=..35] run scoreboard players add $obr7 mg.st 1
execute positioned -171.5 67 178.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..35] run scoreboard players set $obr7 mg.st 0
execute if score $obr7 mg.st matches 15.. run return run function mg:ombre/boss/malveth_reset
execute as @e[tag=mg.olb_malveth] store result score $hp mg.st run data get entity @s Health
execute if score $hp mg.st matches ..256 as @e[tag=mg.olb_malveth,tag=!mg.olrage] at @s run function mg:ombre/boss/rage
scoreboard players remove $obt7_0 mg.st 1
execute if score $obt7_0 mg.st matches ..0 as @e[tag=mg.olb_malveth,limit=1] at @s run function mg:ombre/boss/malveth/bolt
execute if score $obt7_0 mg.st matches ..0 run scoreboard players set $obt7_0 mg.st 5
scoreboard players remove $obt7_1 mg.st 1
execute if score $obt7_1 mg.st matches ..0 as @e[tag=mg.olb_malveth,limit=1] at @s run function mg:ombre/boss/malveth/blink
execute if score $obt7_1 mg.st matches ..0 run scoreboard players set $obt7_1 mg.st 9
scoreboard players remove $obt7_2 mg.st 1
execute if score $obt7_2 mg.st matches ..0 as @e[tag=mg.olb_malveth,limit=1] at @s run function mg:ombre/boss/malveth/guards
execute if score $obt7_2 mg.st matches ..0 run scoreboard players set $obt7_2 mg.st 1
scoreboard players remove $obt7_3 mg.st 1
execute if score $obt7_3 mg.st matches ..0 as @e[tag=mg.olb_malveth,limit=1] at @s run function mg:ombre/boss/malveth/dark
execute if score $obt7_3 mg.st matches ..0 run scoreboard players set $obt7_3 mg.st 12
