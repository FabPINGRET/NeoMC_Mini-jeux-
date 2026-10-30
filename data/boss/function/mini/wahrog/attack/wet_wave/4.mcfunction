particle instant_effect{color:[0.000,1.000,1.000]} ~7 ~2 ~ 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-7 ~2 ~ 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~ ~2 ~7 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~ ~2 ~-7 0 0 0 1 20 normal

execute positioned ~5 ~ ~1.5 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-5 ~ ~1.5 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~1.5 ~ ~5 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~1.5 ~ ~-5 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~5 ~ ~-1.5 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-5 ~ ~-1.5 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-1.5 ~ ~5 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-1.5 ~ ~-5 run function boss:mini/wahrog/attack/wet_wave/damage

summon minecraft:lightning_bolt ~5 ~ ~1.5
summon minecraft:lightning_bolt ~-5 ~ ~1.5
summon minecraft:lightning_bolt ~1.5 ~ ~5
summon minecraft:lightning_bolt ~1.5 ~ ~-5
summon minecraft:lightning_bolt ~5 ~ ~-1.5
summon minecraft:lightning_bolt ~-5 ~ ~-1.5
summon minecraft:lightning_bolt ~-1.5 ~ ~5
summon minecraft:lightning_bolt ~-1.5 ~ ~-5
