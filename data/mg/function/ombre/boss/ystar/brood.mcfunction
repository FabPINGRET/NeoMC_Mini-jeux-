# Ysh'tar, la reine-araignée : brood
playsound minecraft:entity.spider.hurt hostile @a ~ ~ ~ 2 0.5
execute positioned ~4.0 ~ ~0.0 run function mg:ombre/m/arachneen
tag @e[tag=mg.ollast] add mg.olminion_ystar
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
execute positioned ~-2.0 ~ ~3.5 run function mg:ombre/m/arachneen
tag @e[tag=mg.ollast] add mg.olminion_ystar
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
execute positioned ~-2.0 ~ ~-3.5 run function mg:ombre/m/arachneen
tag @e[tag=mg.ollast] add mg.olminion_ystar
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
