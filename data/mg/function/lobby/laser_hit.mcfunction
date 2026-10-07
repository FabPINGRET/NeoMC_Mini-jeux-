# Impact du laser sur un bloc (@s = tireur) : cibles du stand de tir
execute if block ~ ~ ~ minecraft:target run return run function mg:lobby/laser_bull
execute if block ~ ~ ~ #minecraft:wool run function mg:lobby/laser_ring
particle minecraft:end_rod ~ ~ ~ 0.15 0.15 0.15 0.05 10
particle minecraft:firework ~ ~ ~ 0.1 0.1 0.1 0.05 6
playsound minecraft:block.amethyst_block.chime master @a ~ ~ ~ 0.8 1.6
