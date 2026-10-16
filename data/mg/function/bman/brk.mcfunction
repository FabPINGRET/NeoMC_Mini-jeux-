# Brique cassée (30 % : un bonus)
fill ~ ~ ~ ~ ~1 ~ minecraft:air
particle minecraft:block{block_state:"minecraft:bricks"} ~ ~0.8 ~ 0.3 0.4 0.3 0 25 force
execute if predicate {condition:"minecraft:random_chance",chance:0.3f} run function mg:bman/pu_spawn
