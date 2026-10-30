particle instant_effect{color:[0.000,1.000,1.000]} ~15 ~2 ~ 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-15 ~2 ~ 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~ ~2 ~15 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~ ~2 ~-15 0 0 0 1 20 normal

execute positioned ~13 ~ ~2.5 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-13 ~ ~2.5 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~2.5 ~ ~13 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~2.5 ~ ~-13 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~13 ~ ~-2.5 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-13 ~ ~-2.5 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-2.5 ~ ~13 run function boss:mini/wahrog/attack/wet_wave/damage
execute positioned ~-2.5 ~ ~-13 run function boss:mini/wahrog/attack/wet_wave/damage


summon lightning_bolt ~13 ~ ~2.5
summon lightning_bolt ~-13 ~ ~2.5
summon lightning_bolt ~2.5 ~ ~13
summon lightning_bolt ~2.5 ~ ~-13
summon lightning_bolt ~13 ~ ~-2.5
summon lightning_bolt ~-13 ~ ~-2.5
summon lightning_bolt ~-2.5 ~ ~13
summon lightning_bolt ~-2.5 ~ ~-13
