# Peinture BLEUE : cube 3x3x3 ; compte les blocs repeints
execute store result score $c mg.st run fill ~-1 ~-1 ~-1 ~1 ~1 ~1 minecraft:blue_concrete replace minecraft:orange_concrete
scoreboard players operation $pb mg.st += $c mg.st
scoreboard players operation $pa mg.st -= $c mg.st
execute store result score $c mg.st run fill ~-1 ~-1 ~-1 ~1 ~1 ~1 minecraft:blue_concrete replace minecraft:white_concrete
scoreboard players operation $pb mg.st += $c mg.st
particle minecraft:soul_fire_flame ~ ~ ~ 0.4 0.4 0.4 0.02 8
playsound minecraft:block.slime_block.hit master @a ~ ~ ~ 0.7 1.4
