# explosion de la boule de feu
scoreboard players set $olr mg.st 999
particle minecraft:explosion ~ ~ ~ 0.5 0.5 0.5 0 3 force
particle minecraft:flame ~ ~ ~ 1.5 1 1.5 0.05 60 force
playsound minecraft:entity.generic.explode player @a ~ ~ ~ 0.8 1.3
execute as @e[tag=mg.olm,distance=..3] at @s run function mg:ombre/cl/fire_hit with storage mg:ombre s
