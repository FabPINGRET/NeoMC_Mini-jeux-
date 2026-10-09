# Un hélico de remplacement sur une des hélisurfaces (contexte : dimension mg:gta)
execute store result score $gr mg.st run random value 0..3
execute if score $gr mg.st matches 0 in mg:gta positioned -30 66 32430 unless entity @e[type=minecraft:happy_ghast,tag=mg.ghel,distance=..6] run function mg:gta/heli_spawn {c:"red_concrete"}
execute if score $gr mg.st matches 1 in mg:gta positioned 0 66 32432 unless entity @e[type=minecraft:happy_ghast,tag=mg.ghel,distance=..6] run function mg:gta/heli_spawn {c:"blue_concrete"}
execute if score $gr mg.st matches 2 in mg:gta positioned 52 66 32322 unless entity @e[type=minecraft:happy_ghast,tag=mg.ghel,distance=..6] run function mg:gta/heli_spawn {c:"black_concrete"}
execute if score $gr mg.st matches 3 in mg:gta positioned -76 66 32466 unless entity @e[type=minecraft:happy_ghast,tag=mg.ghel,distance=..6] run function mg:gta/heli_spawn {c:"white_concrete"}
