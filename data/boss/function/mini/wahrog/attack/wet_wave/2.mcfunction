particle instant_effect{color:[0.000,1.000,1.000]} ~3 ~2 ~3 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-3 ~2 ~3 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~3 ~2 ~-3 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-3 ~2 ~-3 0 0 0 1 20 normal

execute positioned ~2 ~ ~ run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-2 ~ ~ run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~ ~ ~2 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~ ~ ~-2 run function boss:mini/wahrog/attack/wet_wave/damage


summon minecraft:lightning_bolt ~2 ~ ~
summon minecraft:lightning_bolt ~-2 ~ ~
summon minecraft:lightning_bolt ~ ~ ~2
summon minecraft:lightning_bolt ~ ~ ~-2
