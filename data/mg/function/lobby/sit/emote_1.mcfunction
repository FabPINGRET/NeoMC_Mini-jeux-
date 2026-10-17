# Emote ✋ Salut (mg.opt 77, @s = joueur) : particules et son à 16 blocs, message à 10 blocs, recharge 3 s
execute unless function mg:lobby/sit/can run return 0
execute store result score #sitn mg.st run time query gametime
scoreboard players operation #sitc mg.st = @s mg.lsc
scoreboard players add #sitc mg.st 60
execute if score @s mg.lsc matches 1.. if score #sitn mg.st < #sitc mg.st run return run title @s actionbar {"text":"⏳ Patiente un instant...","color":"gray"}
scoreboard players operation @s mg.lsc = #sitn mg.st
scoreboard players add $emo1 mg.lsn 1
execute at @s run particle minecraft:happy_villager ~ ~2 ~ 0.4 0.3 0.4 0 8 normal @a[distance=..16]
execute at @s run playsound minecraft:entity.villager.yes player @a[distance=..16] ~ ~ ~ 1 1.2
execute at @s run title @a[distance=..10,tag=!mg.play,tag=!mg.pkr,tag=!mg.lk,tag=!mg.ely,tag=!mg.elyf] actionbar [{"text":"✋ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" salue tout le monde !","color":"gray"}]
