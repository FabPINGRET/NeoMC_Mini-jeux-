# Carrefour 11, arrivée au cap 2
execute store result score $gr mg.st run random value 0..2
execute if score $gr mg.st matches 0 run return run function mg:gta/traffic/n11_2_0
execute if score $gr mg.st matches 1 run return run function mg:gta/traffic/n11_2_1
execute if score $gr mg.st matches 2 run return run function mg:gta/traffic/n11_2_2
