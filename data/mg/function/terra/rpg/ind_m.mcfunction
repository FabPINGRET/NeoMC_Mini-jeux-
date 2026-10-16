# faisceau (haut de 30 blocs) et flèche (macro : x y z de l'objectif)
$particle minecraft:end_rod $(x).5 $(y).5 $(z).5 0.08 0.6 0.08 0.02 8 force @s
$execute positioned $(x).5 $(y) $(z).5 run particle minecraft:end_rod ~ ~8 ~ 0.08 7 0.08 0 30 force @s
$execute positioned $(x).5 $(y) $(z).5 run particle minecraft:end_rod ~ ~22 ~ 0.08 7 0.08 0 20 force @s
$execute positioned $(x).5 $(y) $(z).5 run particle minecraft:dust{color:[1.0,0.85,0.2],scale:3} ~ ~1 ~ 0.3 0.3 0.3 0 4 force @s
$execute anchored eyes positioned ^ ^-0.5 ^ facing $(x) $(y) $(z) positioned ^ ^ ^2 run particle minecraft:dust{color:[1.0,0.8,0.1],scale:1.2} ~ ~ ~ 0 0 0 0 1 force @s
$execute anchored eyes positioned ^ ^-0.5 ^ facing $(x) $(y) $(z) positioned ^ ^ ^2.6 run particle minecraft:dust{color:[1.0,0.8,0.1],scale:1.0} ~ ~ ~ 0 0 0 0 1 force @s
$execute anchored eyes positioned ^ ^-0.5 ^ facing $(x) $(y) $(z) positioned ^ ^ ^3.2 run particle minecraft:dust{color:[1.0,0.8,0.1],scale:0.8} ~ ~ ~ 0 0 0 0 1 force @s
$execute anchored eyes positioned ^ ^-0.5 ^ facing $(x) $(y) $(z) positioned ^0.25 ^ ^2.9 run particle minecraft:dust{color:[1.0,0.8,0.1],scale:0.7} ~ ~ ~ 0 0 0 0 1 force @s
$execute anchored eyes positioned ^ ^-0.5 ^ facing $(x) $(y) $(z) positioned ^-0.25 ^ ^2.9 run particle minecraft:dust{color:[1.0,0.8,0.1],scale:0.7} ~ ~ ~ 0 0 0 0 1 force @s
