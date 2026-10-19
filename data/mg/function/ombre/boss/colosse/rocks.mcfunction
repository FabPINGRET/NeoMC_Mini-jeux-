# Le Colosse de runes : rocks
execute positioned ~6.0 ~ ~0.0 run function mg:ombre/m/troggo
tag @e[tag=mg.ollast] add mg.olminion_colosse
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
execute positioned ~-6.0 ~ ~0.0 run function mg:ombre/m/troggo
tag @e[tag=mg.ollast] add mg.olminion_colosse
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
