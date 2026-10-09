# Chaque seconde : voitures de police sans policier, barrages loin de tout joueur recherché
execute as @e[type=minecraft:horse,tag=mg.gpcar] unless predicate mg:has_passenger run function mg:gta/veh_remove
execute as @e[type=minecraft:marker,tag=mg.grblk] at @s unless entity @a[tag=mg.gtw,scores={mg.gwl=1..},distance=..80] run function mg:gta/roadblock_remove
