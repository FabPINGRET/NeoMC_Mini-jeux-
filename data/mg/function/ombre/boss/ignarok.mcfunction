# Ignarok, dragon de feu : chaque seconde
execute positioned 180.5 117 180.5 run bossbar set mg:olb5 players @a[tag=mg.olw,distance=..40]
execute store result bossbar mg:olb5 value run data get entity @e[tag=mg.olb_ignarok,limit=1] Health
execute positioned 180.5 117 180.5 run tag @a[tag=mg.olw,distance=..22] add mg.olboss_in
execute positioned 180.5 117 180.5 unless entity @e[tag=mg.olb_ignarok,distance=..20] run tp @e[tag=mg.olb_ignarok] 180.5 117 180.5
execute positioned 180.5 117 180.5 unless entity @a[tag=mg.olw,gamemode=adventure,distance=..36] run scoreboard players add $obr5 mg.st 1
execute positioned 180.5 117 180.5 if entity @a[tag=mg.olw,gamemode=adventure,distance=..36] run scoreboard players set $obr5 mg.st 0
execute if score $obr5 mg.st matches 15.. run return run function mg:ombre/boss/ignarok_reset
execute as @e[tag=mg.olb_ignarok] store result score $hp mg.st run data get entity @s Health
execute if score $hp mg.st matches ..256 as @e[tag=mg.olb_ignarok,tag=!mg.olrage] at @s run function mg:ombre/boss/rage
scoreboard players remove $obt5_0 mg.st 1
execute if score $obt5_0 mg.st matches ..0 as @e[tag=mg.olb_ignarok,limit=1] at @s run function mg:ombre/boss/ignarok/breath
execute if score $obt5_0 mg.st matches ..0 run scoreboard players set $obt5_0 mg.st 6
scoreboard players remove $obt5_1 mg.st 1
execute if score $obt5_1 mg.st matches ..0 as @e[tag=mg.olb_ignarok,limit=1] at @s run function mg:ombre/boss/ignarok/gust
execute if score $obt5_1 mg.st matches ..0 run scoreboard players set $obt5_1 mg.st 12
scoreboard players remove $obt5_2 mg.st 1
execute if score $obt5_2 mg.st matches ..0 as @e[tag=mg.olb_ignarok,limit=1] at @s run function mg:ombre/boss/ignarok/flight
execute if score $obt5_2 mg.st matches ..0 run scoreboard players set $obt5_2 mg.st 22
scoreboard players remove $obt5_3 mg.st 1
execute if score $obt5_3 mg.st matches ..0 as @e[tag=mg.olb_ignarok,limit=1] at @s run function mg:ombre/boss/ignarok/tail
execute if score $obt5_3 mg.st matches ..0 run scoreboard players set $obt5_3 mg.st 8
