# Grande flaque ORANGE sous les pieds (@s = victime éclaboussée)
execute store result score $c mg.st run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:orange_concrete replace minecraft:blue_concrete
scoreboard players operation $pa mg.st += $c mg.st
scoreboard players operation $pb mg.st -= $c mg.st
execute store result score $c mg.st run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:orange_concrete replace minecraft:white_concrete
scoreboard players operation $pa mg.st += $c mg.st
