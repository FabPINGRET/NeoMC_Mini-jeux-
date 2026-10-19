# Ignarok, dragon de feu : breath
scoreboard players set @s mg.olat 14
playsound minecraft:entity.blaze.shoot hostile @a ~ ~ ~ 2 0.4
playsound minecraft:item.firecharge.use hostile @a ~ ~ ~ 2 0.6
execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^3 ^4 run particle minecraft:flame ^ ^ ^3 1 0.6 2 0.06 200 force
execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^ ^6 as @a[tag=mg.olw,gamemode=adventure,distance=..5] run function mg:ombre/boss/fire
