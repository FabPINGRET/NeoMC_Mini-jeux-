execute if entity @s[tag=mg.olg1] run tag @s add mg.olg2
tag @s add mg.olg1
tag @s add mg.olshd
data merge entity @s {Invulnerable:1b,Glowing:1b}
tellraw @a[distance=..40] {"text":"Malveth : « Mes gardes, protégez-moi ! » (tue ses gardes pour briser son bouclier)","color":"dark_purple","bold":true}
execute positioned ~5.0 ~ ~0.0 run function mg:ombre/m/ossement
tag @e[tag=mg.ollast] add mg.olminion_malveth
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
execute positioned ~0.0 ~ ~5.0 run function mg:ombre/m/ossement
tag @e[tag=mg.ollast] add mg.olminion_malveth
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
execute positioned ~-5.0 ~ ~0.0 run function mg:ombre/m/ossement
tag @e[tag=mg.ollast] add mg.olminion_malveth
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
execute positioned ~-0.0 ~ ~-5.0 run function mg:ombre/m/ossement
tag @e[tag=mg.ollast] add mg.olminion_malveth
execute as @e[tag=mg.ollast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.olw,gamemode=adventure,distance=..40]
