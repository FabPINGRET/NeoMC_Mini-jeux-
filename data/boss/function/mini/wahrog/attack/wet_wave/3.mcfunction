particle instant_effect{color:[0.000,1.000,1.000]} ~5 ~ ~1.5 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-5 ~ ~1.5 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~1.5 ~ ~5 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~1.5 ~ ~-5 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~5 ~ ~-1.5 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-5 ~ ~-1.5 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-1.5 ~ ~5 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-1.5 ~ ~-5 0 0 0 1 20 normal

execute positioned ~3 ~ ~3 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-3 ~ ~3 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~3 ~ ~-3 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-3 ~ ~-3 run function boss:mini/wahrog/attack/wet_wave/damage

summon minecraft:lightning_bolt ~3 ~2 ~3
summon minecraft:lightning_bolt ~-3 ~2 ~3
summon minecraft:lightning_bolt ~3 ~2 ~-3
summon minecraft:lightning_bolt ~-3 ~2 ~-3
