# Emote 🎉 Fête (mg.opt 79, @s = joueur) : particules et son à 16 blocs, message à 10 blocs, recharge 3 s
execute unless function mg:lobby/sit/can run return 0
execute store result score #sitn mg.st run time query gametime
scoreboard players operation #sitc mg.st = @s mg.lsc
scoreboard players add #sitc mg.st 60
execute if score @s mg.lsc matches 1.. if score #sitn mg.st < #sitc mg.st run return run title @s actionbar {"text":"⏳ Patiente un instant...","color":"gray"}
scoreboard players operation @s mg.lsc = #sitn mg.st
scoreboard players add $emo3 mg.lsn 1
execute at @s run particle minecraft:firework ~ ~1.5 ~ 0.5 0.6 0.5 0.12 20 normal @a[distance=..16]
execute at @s run playsound minecraft:entity.firework_rocket.twinkle player @a[distance=..16] ~ ~ ~ 1 1
execute at @s run title @a[distance=..10,tag=!mg.play,tag=!mg.pkr,tag=!mg.lk,tag=!mg.ely,tag=!mg.elyf] actionbar [{"text":"🎉 ","color":"light_purple"},{"selector":"@s","color":"yellow"},{"text":" fait la fête !","color":"gray"}]
# mouvement (sit_move.py) : l'image 0 est jouée par core/tick -> move_tick, le même tick
scoreboard players set @s mg.lsk 3
scoreboard players set @s mg.lse -1
tag @s add mg.lsm
