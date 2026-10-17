# Toutes les 2 s (core/tick) : zones cliquables des bancs ; refait toutes les zones si leur nombre a changé
execute if score $sitoff mg.st matches 1 run kill @e[type=minecraft:interaction,tag=mg.bench]
execute if score $sitoff mg.st matches 1 run return 0
execute unless score $setup mg.st matches 1 run return 0
# un chunk de bancs pas chargé : on attend (ses zones ne se comptent pas)
execute in minecraft:overworld unless loaded -24 64 -8 run return 0
execute in minecraft:overworld unless loaded -24 64 8 run return 0
execute in minecraft:overworld unless loaded -8 64 -40 run return 0
execute in minecraft:overworld unless loaded -8 64 -24 run return 0
execute in minecraft:overworld unless loaded -8 64 24 run return 0
execute in minecraft:overworld unless loaded -8 64 40 run return 0
execute in minecraft:overworld unless loaded 8 64 -40 run return 0
execute in minecraft:overworld unless loaded 8 64 -24 run return 0
execute in minecraft:overworld unless loaded 8 64 24 run return 0
execute in minecraft:overworld unless loaded 8 64 40 run return 0
execute in minecraft:overworld unless loaded 24 64 -8 run return 0
execute in minecraft:overworld unless loaded 24 64 8 run return 0
execute in minecraft:overworld unless loaded 40 64 -8 run return 0
execute in minecraft:overworld unless loaded 40 64 8 run return 0
execute in minecraft:overworld unless loaded 56 64 -8 run return 0
execute in minecraft:overworld unless loaded 56 64 8 run return 0
# un banc remplacé par un autre bloc perd sa zone
execute as @e[type=minecraft:interaction,tag=mg.bench] at @s unless block ~ ~ ~ minecraft:spruce_stairs[half=bottom] run kill @s
execute store result score #lbc mg.st if entity @e[type=minecraft:interaction,tag=mg.bench]
execute unless score #lbc mg.st = $lbx mg.st run function mg:lobby/sit/benches
