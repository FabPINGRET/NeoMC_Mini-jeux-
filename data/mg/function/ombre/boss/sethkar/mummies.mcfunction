# Sethkar, le pharaon-liche : mummies
execute positioned ~5.0 ~ ~0.0 run function mg:ombre/m/momie
tag @e[tag=mg.ollast] add mg.olminion_sethkar
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
execute positioned ~-5.0 ~ ~0.0 run function mg:ombre/m/momie
tag @e[tag=mg.ollast] add mg.olminion_sethkar
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
