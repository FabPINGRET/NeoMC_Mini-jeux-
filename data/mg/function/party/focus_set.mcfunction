# Le pion de @s devient le pion suivi par la caméra (et brille)
execute as @e[type=minecraft:armor_stand,tag=mg.mpfocus] run data merge entity @s {Glowing:0b}
tag @e[type=minecraft:armor_stand] remove mg.mpfocus
scoreboard players operation $pp mg.st = @s mg.mpo
execute as @e[type=minecraft:armor_stand,tag=mg.mppawn] if score @s mg.mpo = $pp mg.st run tag @s add mg.mpfocus
execute as @e[type=minecraft:armor_stand,tag=mg.mpfocus] run data merge entity @s {Glowing:1b}
