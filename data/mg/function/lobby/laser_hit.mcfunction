# Impact du laser sur un bloc (@s = tireur) : cibles du stand de tir
execute if block ~ ~ ~ minecraft:target run return run function mg:lobby/laser_bull
execute if block ~ ~ ~ #minecraft:wool run function mg:lobby/laser_ring
particle minecraft:electric_spark ~ ~ ~ 0.2 0.2 0.2 0.4 18
particle minecraft:end_rod ~ ~ ~ 0.15 0.15 0.15 0.08 10
particle minecraft:dust{color:[1.0,0.2,0.2],scale:1.5} ~ ~ ~ 0.15 0.15 0.15 0 10
particle minecraft:smoke ~ ~ ~ 0.1 0.1 0.1 0.02 6
playsound minecraft:block.amethyst_block.chime master @a ~ ~ ~ 0.8 1.6
