# Lumière guérisseuse
playsound minecraft:block.amethyst_block.chime player @a ~ ~ ~ 1 1.2
particle minecraft:happy_villager ~ ~1 ~ 3 1 3 0 40
particle minecraft:end_rod ~ ~1 ~ 2 1 2 0.05 30
effect give @a[tag=mg.olw,distance=..8] minecraft:instant_health 1 1 true
effect give @a[tag=mg.olw,distance=..8] minecraft:regeneration 4 1 true
execute if score @s mg.ols4 matches 8.. run effect give @a[tag=mg.olw,distance=..8] minecraft:regeneration 6 2 true
function mg:ombre/cl/end
