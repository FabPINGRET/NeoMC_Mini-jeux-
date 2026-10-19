# Drake : souffle de braises en cône
scoreboard players set @s mg.olat 10
playsound minecraft:entity.blaze.shoot hostile @a ~ ~ ~ 1 0.6
execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^1 ^1.5 run particle minecraft:flame ^ ^ ^2 0.6 0.3 0.6 0.04 40 force
execute facing entity @p[tag=mg.olw,gamemode=adventure] eyes positioned ^ ^1 ^4 as @a[tag=mg.olw,gamemode=adventure,distance=..3] run function mg:ombre/m/burn
