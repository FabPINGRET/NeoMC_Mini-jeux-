# Boîte de nuit (toutes les 0,5 s si quelqu'un y est) : piste, lasers
execute store result score $gr mg.st run random value 0..3
execute if score $gr mg.st matches 0 in mg:gta run function mg:gta/club_floor_0
execute if score $gr mg.st matches 1 in mg:gta run function mg:gta/club_floor_1
execute if score $gr mg.st matches 2 in mg:gta run function mg:gta/club_floor_2
execute if score $gr mg.st matches 3 in mg:gta run function mg:gta/club_floor_3
execute in mg:gta run particle minecraft:dust{color:[1.0,0.1,0.9],scale:1.6} -59.5 70 32435 3 0.5 4 0 25 force
execute in mg:gta run particle minecraft:dust{color:[0.1,0.9,1.0],scale:1.6} -59.5 70 32435 3 0.5 4 0 25 force
execute in mg:gta run particle minecraft:end_rod -59.5 68 32435 2 0.2 3 0.02 6 force
