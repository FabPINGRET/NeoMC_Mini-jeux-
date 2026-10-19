# Hrimgar, le géant du givre : chaque seconde
execute positioned 30.5 105 -204.5 run bossbar set mg:olb2 players @a[tag=mg.olw,distance=..41]
execute store result bossbar mg:olb2 value run data get entity @e[tag=mg.olb_hrimgar,limit=1] Health
execute positioned 30.5 105 -204.5 run tag @a[tag=mg.olw,distance=..23] add mg.olboss_in
execute positioned 30.5 105 -204.5 unless entity @e[tag=mg.olb_hrimgar,distance=..21] run tp @e[tag=mg.olb_hrimgar] 30.5 105 -204.5
execute positioned 30.5 105 -204.5 unless entity @a[tag=mg.olw,gamemode=adventure,distance=..37] run scoreboard players add $obr2 mg.st 1
execute positioned 30.5 105 -204.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..37] run scoreboard players set $obr2 mg.st 0
execute if score $obr2 mg.st matches 15.. run return run function mg:ombre/boss/hrimgar_reset
execute as @e[tag=mg.olb_hrimgar] store result score $hp mg.st run data get entity @s Health
execute if score $hp mg.st matches ..250 as @e[tag=mg.olb_hrimgar,tag=!mg.olrage] at @s run function mg:ombre/boss/rage
scoreboard players remove $obt2_0 mg.st 1
execute if score $obt2_0 mg.st matches ..0 as @e[tag=mg.olb_hrimgar,limit=1] at @s run function mg:ombre/boss/hrimgar/slam
execute if score $obt2_0 mg.st matches ..0 run scoreboard players set $obt2_0 mg.st 7
scoreboard players remove $obt2_1 mg.st 1
execute if score $obt2_1 mg.st matches ..0 as @e[tag=mg.olb_hrimgar,limit=1] at @s run function mg:ombre/boss/hrimgar/breath
execute if score $obt2_1 mg.st matches ..0 run scoreboard players set $obt2_1 mg.st 10
scoreboard players remove $obt2_2 mg.st 1
execute if score $obt2_2 mg.st matches ..0 as @e[tag=mg.olb_hrimgar,limit=1] at @s run function mg:ombre/boss/hrimgar/spikes
execute if score $obt2_2 mg.st matches ..0 run scoreboard players set $obt2_2 mg.st 9
scoreboard players remove $obt2_3 mg.st 1
execute if score $obt2_3 mg.st matches ..0 as @e[tag=mg.olb_hrimgar,limit=1] at @s run function mg:ombre/boss/hrimgar/wolves
execute if score $obt2_3 mg.st matches ..0 run scoreboard players set $obt2_3 mg.st 25
