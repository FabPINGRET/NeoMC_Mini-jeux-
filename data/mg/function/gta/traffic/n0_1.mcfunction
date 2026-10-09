# Carrefour 0, arrivée au cap 1
execute store result score $gr mg.st run random value 0..0
execute if score $gr mg.st matches 0 run return run function mg:gta/traffic/n0_1_0
