particle minecraft:explosion ~ ~1 ~ 0.5 0.5 0.5 0 3 force
particle minecraft:lava ~ ~1 ~ 1 1 1 0 20 force
playsound minecraft:entity.generic.explode hostile @a ~ ~ ~ 1 0.8
execute as @a[tag=mg.olw,gamemode=adventure,distance=..2.5] run function mg:ombre/boss/fire
kill @s
