particle instant_effect{color:[0.000,1.000,1.000]} ~9 ~ ~2 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-9 ~ ~2 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~2 ~ ~9 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~2 ~ ~-9 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~9 ~ ~-2 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-9 ~ ~-2 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-2 ~ ~9 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-2 ~ ~-9 0 0 0 1 20 normal

execute positioned ~7 ~ ~ run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-7 ~ ~ run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~ ~ ~7 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~ ~ ~-7 run function boss:mini/wahrog/attack/wet_wave/damage

summon minecraft:lightning_bolt ~7 ~2 ~
summon minecraft:lightning_bolt ~-7 ~2 ~
summon minecraft:lightning_bolt ~ ~2 ~7
summon minecraft:lightning_bolt ~ ~2 ~-7
