# Balises du spawn (générées par tools/lobby/gen_beacons.py)
# blanche, élytra
fill 20 62 -16 22 62 -14 minecraft:iron_block
setblock 21 63 -15 minecraft:beacon
fill 21 64 -15 21 319 -15 minecraft:air
# rouge, montagne russe
fill -49 62 40 -47 62 42 minecraft:iron_block
setblock -48 63 41 minecraft:beacon
fill -48 64 41 -48 319 41 minecraft:air
setblock -48 64 41 minecraft:red_stained_glass
data modify storage mg:lobby beacon1 set value 1b
