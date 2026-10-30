particle instant_effect{color:[0.000,1.000,1.000]} ~13 ~ ~2.5 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-13 ~ ~2.5 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~2.5 ~ ~13 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~2.5 ~ ~-13 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~13 ~ ~-2.5 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-13 ~ ~-2.5 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-2.5 ~ ~13 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-2.5 ~ ~-13 0 0 0 1 20 normal

execute positioned ~11 ~ ~ run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-11 ~ ~ run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~ ~ ~11 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~ ~ ~-11 run function boss:mini/wahrog/attack/wet_wave/damage


summon minecraft:lightning_bolt ~11 ~2 ~
summon minecraft:lightning_bolt ~-11 ~2 ~
summon minecraft:lightning_bolt ~ ~2 ~11
summon minecraft:lightning_bolt ~ ~2 ~-11
