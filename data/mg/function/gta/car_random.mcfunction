# Une voiture au hasard à ce carrefour (remplace une voiture détruite)
execute store result score $gr mg.st run random value 1..10
execute if score $gr mg.st matches 1 positioned ~2 ~ ~ run function mg:gta/car/spawn_1
execute if score $gr mg.st matches 2 positioned ~2 ~ ~ run function mg:gta/car/spawn_2
execute if score $gr mg.st matches 3 positioned ~2 ~ ~ run function mg:gta/car/spawn_3
execute if score $gr mg.st matches 4 positioned ~2 ~ ~ run function mg:gta/car/spawn_4
execute if score $gr mg.st matches 5 positioned ~2 ~ ~ run function mg:gta/car/spawn_5
execute if score $gr mg.st matches 6 positioned ~2 ~ ~ run function mg:gta/car/spawn_6
execute if score $gr mg.st matches 7 positioned ~2 ~ ~ run function mg:gta/car/spawn_7
execute if score $gr mg.st matches 8 positioned ~2 ~ ~ run function mg:gta/car/spawn_8
execute if score $gr mg.st matches 9 positioned ~2 ~ ~ run function mg:gta/car/spawn_9
execute if score $gr mg.st matches 10 positioned ~2 ~ ~ run function mg:gta/car/spawn_10
