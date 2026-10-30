# Anciens portails (GTA, Terra Nova, Ombrelune) : vidés une seule fois, sol rendu au décor du spawn (mg:hub oldclean)
fill 5 64 -23 13 80 -15 minecraft:air
fill 5 63 -23 13 63 -15 minecraft:grass_block
fill -16 64 -23 -5 80 -15 minecraft:air
fill -16 63 -23 -5 63 -15 minecraft:grass_block
fill -18 64 -33 -5 80 -25 minecraft:air
fill -18 63 -33 -5 63 -25 minecraft:grass_block
execute unless data storage mg:lobby olsite if block 40 63 -9 minecraft:chiseled_polished_blackstone run function mg:ombre/old_site
data modify storage mg:hub oldclean set value 1b
