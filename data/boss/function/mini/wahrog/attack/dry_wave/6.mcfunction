particle instant_effect{color:[0.000,1.000,1.000]} ~11 ~ ~ 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~-11 ~ ~ 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~ ~ ~11 0 0 0 1 20 normal
particle instant_effect{color:[0.000,1.000,1.000]} ~ ~ ~-11 0 0 0 1 20 normal

execute positioned ~9 ~ ~2 run function boss:mini/wahrog/attack/dry_wave/damage
execute positioned ~-9 ~ ~2 run function boss:mini/wahrog/attack/dry_wave/damage
execute positioned ~2 ~ ~9 run function boss:mini/wahrog/attack/dry_wave/damage
execute positioned ~2 ~ ~-9 run function boss:mini/wahrog/attack/dry_wave/damage
execute positioned ~9 ~ ~-2 run function boss:mini/wahrog/attack/dry_wave/damage
execute positioned ~-9 ~ ~-2 run function boss:mini/wahrog/attack/dry_wave/damage
execute positioned ~-2 ~ ~9 run function boss:mini/wahrog/attack/dry_wave/damage
execute positioned ~-2 ~ ~-9 run function boss:mini/wahrog/attack/dry_wave/damage


summon lightning_bolt ~9 ~ ~2
summon lightning_bolt ~-9 ~ ~2
summon lightning_bolt ~2 ~ ~9
summon lightning_bolt ~2 ~ ~-9
summon lightning_bolt ~9 ~ ~-2
summon lightning_bolt ~-9 ~ ~-2
summon lightning_bolt ~-2 ~ ~9
summon lightning_bolt ~-2 ~ ~-9
