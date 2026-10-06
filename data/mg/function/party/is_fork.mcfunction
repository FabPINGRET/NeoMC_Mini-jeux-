# $fk = 1 si la case de @s est un embranchement
scoreboard players set $fk mg.st 0
execute if score @s mg.mpi matches 13 run scoreboard players set $fk mg.st 1
execute if score @s mg.mpi matches 48 run scoreboard players set $fk mg.st 1
