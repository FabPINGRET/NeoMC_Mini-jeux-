fill -10453 84 427 -10429 119 451 minecraft:white_wool replace light_blue_concrete
fill -10453 84 427 -10429 119 451 minecraft:white_wool replace red_concrete
fill -10453 84 427 -10429 119 451 minecraft:white_wool replace orange_concrete
fill -10453 84 427 -10429 119 451 minecraft:white_wool replace yellow_concrete
fill -10453 84 427 -10429 119 451 minecraft:white_wool replace purple_concrete
fill -10453 84 427 -10429 119 451 minecraft:white_wool replace black_concrete
fill -10453 84 427 -10429 119 451 minecraft:white_wool replace white_concrete
fill -10453 84 427 -10429 119 451 minecraft:white_wool replace blue_concrete

setblock -10441 90 439 air

kill @e[tag=custodian_display,distance=0..]

playsound minecraft:entity.allay.ambient_without_item master @a[tag=mg.flw] -10441 83 439 4 1.5
particle minecraft:flash{color:[1.000,1.000,1.000,1.00]} -10441 89 439 8 3 8 0 50
