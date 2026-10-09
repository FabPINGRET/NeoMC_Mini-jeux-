# Carrefour 2, arrivée au cap 2
execute store result score $gr mg.st run random value 0..1
execute if score $gr mg.st matches 0 run return run function mg:gta/traffic/n2_2_0
execute if score $gr mg.st matches 1 run return run function mg:gta/traffic/n2_2_1
