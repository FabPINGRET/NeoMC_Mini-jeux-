# Pion de @s sur sa case (mg.mpi) : le joueur, lui, regarde par la caméra
scoreboard players operation $pp mg.st = @s mg.mpo
scoreboard players operation $pi mg.st = @s mg.mpi
execute as @e[type=minecraft:armor_stand,tag=mg.mppawn] if score @s mg.mpo = $pp mg.st run function mg:party/pawn_place
