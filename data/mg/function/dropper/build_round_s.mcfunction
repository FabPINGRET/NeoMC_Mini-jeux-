# Tube commun : disposition aléatoire (6 dispositions)
execute store result score $k mg.st run random value 1..6
execute if score $k mg.st matches 1 positioned 120 58 5197 run function mg:dropper/tube_1
execute if score $k mg.st matches 2 positioned 120 58 5197 run function mg:dropper/tube_2
execute if score $k mg.st matches 3 positioned 120 58 5197 run function mg:dropper/tube_3
execute if score $k mg.st matches 4 positioned 120 58 5197 run function mg:dropper/tube_4
execute if score $k mg.st matches 5 positioned 120 58 5197 run function mg:dropper/tube_5
execute if score $k mg.st matches 6 positioned 120 58 5197 run function mg:dropper/tube_6
