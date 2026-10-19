# Brennic, seigneur des brigands : call
execute if score $hp mg.st matches 230.. run return 0
tellraw @a[distance=..40] {"text":"Brennic : « À moi, les gars ! »","color":"red"}
execute positioned ~4.0 ~ ~0.0 run function mg:ombre/m/bandit
tag @e[tag=mg.ollast] add mg.olminion_brennic
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
execute positioned ~6.0 ~ ~0.0 run function mg:ombre/m/archer
tag @e[tag=mg.ollast] add mg.olminion_brennic
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
