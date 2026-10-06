execute if score $sg mg.st matches 1 run return run function mg:dropper/build_round_s
# Nouvelle disposition d'obstacles tirée au hasard (6 dispositions) dans tous les couloirs
execute store result score $k mg.st run random value 1..6
execute if score $k mg.st matches 1 run function mg:dropper/build_1
execute if score $k mg.st matches 2 run function mg:dropper/build_2
execute if score $k mg.st matches 3 run function mg:dropper/build_3
execute if score $k mg.st matches 4 run function mg:dropper/build_4
execute if score $k mg.st matches 5 run function mg:dropper/build_5
execute if score $k mg.st matches 6 run function mg:dropper/build_6
