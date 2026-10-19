# Nyxar, dragon de la Lune Noire : chaque seconde
execute positioned -171.5 102 178.5 run bossbar set mg:olb8 players @a[tag=mg.olw,distance=..39]
execute store result bossbar mg:olb8 value run data get entity @e[tag=mg.olb_nyxar,limit=1] Health
execute positioned -171.5 102 178.5 run tag @a[tag=mg.olw,distance=..21] add mg.olboss_in
execute positioned -171.5 102 178.5 unless entity @e[tag=mg.olb_nyxar,distance=..19] run tp @e[tag=mg.olb_nyxar] -171.5 102 178.5
execute positioned -171.5 102 178.5 unless entity @a[tag=mg.olw,gamemode=adventure,distance=..35] run scoreboard players add $obr8 mg.st 1
execute positioned -171.5 102 178.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..35] run scoreboard players set $obr8 mg.st 0
execute if score $obr8 mg.st matches 15.. run return run function mg:ombre/boss/nyxar_reset
execute as @e[tag=mg.olb_nyxar] store result score $hp mg.st run data get entity @s Health
execute if score $hp mg.st matches ..256 as @e[tag=mg.olb_nyxar,tag=!mg.olrage] at @s run function mg:ombre/boss/rage
scoreboard players remove $obt8_0 mg.st 1
execute if score $obt8_0 mg.st matches ..0 as @e[tag=mg.olb_nyxar,limit=1] at @s run function mg:ombre/boss/nyxar/breath
execute if score $obt8_0 mg.st matches ..0 run scoreboard players set $obt8_0 mg.st 6
scoreboard players remove $obt8_1 mg.st 1
execute if score $obt8_1 mg.st matches ..0 as @e[tag=mg.olb_nyxar,limit=1] at @s run function mg:ombre/boss/nyxar/dive
execute if score $obt8_1 mg.st matches ..0 run scoreboard players set $obt8_1 mg.st 14
scoreboard players remove $obt8_2 mg.st 1
execute if score $obt8_2 mg.st matches ..0 as @e[tag=mg.olb_nyxar,limit=1] at @s run function mg:ombre/boss/nyxar/spectres
execute if score $obt8_2 mg.st matches ..0 run scoreboard players set $obt8_2 mg.st 18
scoreboard players remove $obt8_3 mg.st 1
execute if score $obt8_3 mg.st matches ..0 as @e[tag=mg.olb_nyxar,limit=1] at @s run function mg:ombre/boss/nyxar/roar
execute if score $obt8_3 mg.st matches ..0 run scoreboard players set $obt8_3 mg.st 11
