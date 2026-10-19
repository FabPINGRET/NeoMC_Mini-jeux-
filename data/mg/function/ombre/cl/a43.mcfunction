# Bénédiction
playsound minecraft:block.beacon.activate player @a ~ ~ ~ 1 1.4
particle minecraft:totem_of_undying ~ ~1 ~ 2 1 2 0.2 40
effect give @a[tag=mg.olw,distance=..10] minecraft:absorption 20 1
effect give @a[tag=mg.olw,distance=..10] minecraft:resistance 15 0
function mg:ombre/cl/end
