# Railgun (@s = tireur, position = tireur) : rayon de 30 blocs, 1 cœur de dégâts (jamais mortel), recharge 0,6 s
scoreboard players reset @s mg.qs
execute if score @s mg.lcd matches 1.. run return run playsound minecraft:block.dispenser.fail master @s ~ ~ ~ 0.4 1.8
scoreboard players set @s mg.lcd 12
tag @s add mg.lsr
scoreboard players set $lr mg.st 60
# éclair au canon
execute anchored eyes positioned ^-0.3 ^-0.2 ^0.7 run particle minecraft:electric_spark ~ ~ ~ 0.08 0.08 0.08 0.35 14
execute anchored eyes positioned ^-0.3 ^-0.2 ^0.7 run particle minecraft:end_rod ~ ~ ~ 0.04 0.04 0.04 0.1 6
execute anchored eyes positioned ^-0.3 ^-0.2 ^0.7 run particle minecraft:dust{color:[1.0,0.3,0.3],scale:2.0} ~ ~ ~ 0.05 0.05 0.05 0 4
execute anchored eyes positioned ^-0.3 ^-0.2 ^0.7 run function mg:lobby/laser_ray
tag @s remove mg.lsr
# son : décharge électrique + claquement
playsound minecraft:entity.warden.sonic_boom master @a ~ ~ ~ 0.3 2
playsound minecraft:block.beacon.deactivate master @a ~ ~ ~ 0.7 2
playsound minecraft:entity.firework_rocket.shoot master @a ~ ~ ~ 1 1.7
