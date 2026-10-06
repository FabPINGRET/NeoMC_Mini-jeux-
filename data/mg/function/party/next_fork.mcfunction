# Case suivante depuis un embranchement selon $mpch (1 = route 1, 2 = route 2)
execute if score @s mg.mpi matches 13 if score $mpch mg.st matches 1 run return run scoreboard players set @s mg.mpi 14
execute if score @s mg.mpi matches 13 if score $mpch mg.st matches 2 run return run scoreboard players set @s mg.mpi 28
execute if score @s mg.mpi matches 48 if score $mpch mg.st matches 1 run return run scoreboard players set @s mg.mpi 49
execute if score @s mg.mpi matches 48 if score $mpch mg.st matches 2 run return run scoreboard players set @s mg.mpi 69
