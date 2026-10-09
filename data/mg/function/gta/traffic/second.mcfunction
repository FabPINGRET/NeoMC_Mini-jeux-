# Chaque seconde : 14 voitures PNJ en ville
execute store result score $gtc mg.st if entity @e[type=minecraft:marker,tag=mg.gtraf]
execute if score $gtc mg.st matches ..13 as @e[type=minecraft:marker,tag=mg.gix,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..18] unless entity @e[type=minecraft:marker,tag=mg.gtraf,distance=..6] run function mg:gta/traffic/spawn
