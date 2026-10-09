# Carrefour 30, arrivée au cap 3
execute store result score $gr mg.st run random value 0..1
execute if score $gr mg.st matches 0 run return run function mg:gta/traffic/n30_3_0
execute if score $gr mg.st matches 1 run return run function mg:gta/traffic/n30_3_1
