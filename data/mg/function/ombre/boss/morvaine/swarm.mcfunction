# Morvaine, la mère-sorcière : swarm
tellraw @a[distance=..40] {"text":"Morvaine : « Levez-vous, mes noyés ! »","color":"dark_purple"}
execute positioned ~4.0 ~ ~0.0 run function mg:ombre/m/noye
tag @e[tag=mg.ollast] add mg.olminion_morvaine
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
execute positioned ~-4.0 ~ ~0.0 run function mg:ombre/m/noye
tag @e[tag=mg.ollast] add mg.olminion_morvaine
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
execute positioned ~6.0 ~ ~0.0 run function mg:ombre/m/embourbe
tag @e[tag=mg.ollast] add mg.olminion_morvaine
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
