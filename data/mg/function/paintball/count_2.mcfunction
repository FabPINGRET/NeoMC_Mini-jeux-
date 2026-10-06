# Paintball — compte les blocs peignables ($pt) (recolore puis restaure)
execute store result score $pt mg.st run fill -40 79 12650 40 84 12714 minecraft:light_gray_concrete replace minecraft:white_concrete
execute store result score $c mg.st run fill -40 79 12715 40 84 12750 minecraft:light_gray_concrete replace minecraft:white_concrete
scoreboard players operation $pt mg.st += $c mg.st
fill -40 79 12650 40 84 12714 minecraft:white_concrete replace minecraft:light_gray_concrete
fill -40 79 12715 40 84 12750 minecraft:white_concrete replace minecraft:light_gray_concrete
