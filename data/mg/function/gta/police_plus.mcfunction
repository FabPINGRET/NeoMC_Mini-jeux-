# Chaque seconde (@s = joueur recherché, à sa position) : voitures de police, barrage, hélico
execute store result score $gpc mg.st if entity @e[type=minecraft:horse,tag=mg.gpcar,distance=..60]
scoreboard players operation $gpw mg.st = @s mg.gwl
scoreboard players remove $gpw mg.st 1
execute if score @s mg.gwl matches 2.. if score $gpc mg.st < $gpw mg.st as @e[type=minecraft:marker,tag=mg.gix,distance=25..55,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..15] run function mg:gta/pcar_spawn
execute if score @s mg.gwl matches 4.. unless entity @e[type=minecraft:marker,tag=mg.grblk,distance=..60] as @e[type=minecraft:marker,tag=mg.gix,distance=20..45,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..12] run function mg:gta/roadblock
execute if score @s mg.gwl matches 5.. unless entity @e[type=minecraft:marker,tag=mg.gphel] run function mg:gta/pheli_spawn
