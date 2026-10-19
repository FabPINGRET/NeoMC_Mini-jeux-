# @s (zone de pluie, chaque seconde) : une volée
scoreboard players remove @s mg.olst 1
particle minecraft:crit ~ ~4 ~ 2 0.2 2 0 60 force
particle minecraft:dust{color:[0.6,1.0,0.5],scale:1} ~ ~2 ~ 2 2 2 0 40 force
playsound minecraft:entity.arrow.hit player @a ~ ~ ~ 1 0.8
scoreboard players operation $own mg.st = @s mg.olo
tag @a remove mg.olcast
execute as @a[tag=mg.olw] if score @s mg.olpid = $own mg.st run tag @s add mg.olcast
execute store result storage mg:ombre s.d int 1 run scoreboard players get @s mg.olpw
execute as @e[tag=mg.olm,distance=..4.5] at @s run function mg:ombre/cl/hit with storage mg:ombre s
tag @a remove mg.olcast
execute if score @s mg.olst matches ..0 run kill @s
