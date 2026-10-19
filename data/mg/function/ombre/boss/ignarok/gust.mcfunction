# Ignarok, dragon de feu : gust
particle minecraft:gust_emitter_large ~ ~2 ~ 1 1 1 0 3 force
playsound minecraft:entity.ender_dragon.flap hostile @a ~ ~ ~ 2 0.7
execute as @a[tag=mg.olw,gamemode=adventure,distance=..9] at @s facing entity @e[tag=mg.olb_ignarok,limit=1] feet rotated ~180 -20 run function mg:ombre/boss/knock
