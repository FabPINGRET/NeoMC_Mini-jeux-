# Fin du vol libre (@s) : élytres et fusées retirées, courte protection à l'atterrissage
tag @s remove mg.elyf
clear @s minecraft:elytra[minecraft:custom_data~{mg_elyf:1b}]
clear @s minecraft:firework_rocket[minecraft:custom_data~{mg_elyf:1b}]
effect clear @s minecraft:levitation
effect clear @s minecraft:resistance
effect give @s minecraft:resistance 5 4 true
