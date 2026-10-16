# @s (tourelle, chaque seconde) : tire sur le prédateur le plus proche (16 blocs), puis s'use
scoreboard players remove @s mg.tvst 1
execute if score @s mg.tvst matches ..0 run return run function mg:terra/rpg/cl/turret_end
execute unless entity @e[tag=mg.tvhos,distance=..16] run return 0
scoreboard players set $tvr mg.st 0
execute positioned ~ ~1.2 ~ facing entity @e[tag=mg.tvhos,distance=..16,sort=nearest,limit=1] eyes run function mg:terra/rpg/cl/tray
playsound minecraft:entity.breeze.shoot player @a ~ ~ ~ 0.6 1.9
