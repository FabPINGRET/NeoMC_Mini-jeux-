# Carrefour 19, arrivée au cap 3
execute store result score $gr mg.st run random value 0..0
execute if score $gr mg.st matches 0 run return run function mg:gta/traffic/n19_3_0
