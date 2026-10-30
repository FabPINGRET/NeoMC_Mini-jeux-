particle instant_effect{color:[0.000,1.000,1.000]} ~19 ~2 ~ 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-19 ~2 ~ 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~ ~2 ~19 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~ ~2 ~-19 0 0 0 1 20 normal

execute positioned ~17 ~ ~3 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-17 ~ ~3 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~3 ~ ~17 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~3 ~ ~-17 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~17 ~ ~-3 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-17 ~ ~-3 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-3 ~ ~17 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-3 ~ ~-17 run function boss:mini/wahrog/attack/wet_wave/damage


summon lightning_bolt ~17 ~ ~3
summon lightning_bolt ~-17 ~ ~3
summon lightning_bolt ~3 ~ ~17
summon lightning_bolt ~3 ~ ~-17
summon lightning_bolt ~17 ~ ~-3
summon lightning_bolt ~-17 ~ ~-3
summon lightning_bolt ~-3 ~ ~17
summon lightning_bolt ~-3 ~ ~-17
