# Annonce la route choisie par @s (case embranchement, choix $mpch)
execute if score @s mg.mpi matches 13 if score $mpch mg.st matches 1 run tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" prend la route de la plage","color":"gray"}]
execute if score @s mg.mpi matches 13 if score $mpch mg.st matches 2 run tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" prend le raccourci du volcan","color":"gray"}]
execute if score @s mg.mpi matches 48 if score $mpch mg.st matches 1 run tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" prend le tour du lac gelé","color":"gray"}]
execute if score @s mg.mpi matches 48 if score $mpch mg.st matches 2 run tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" prend la grotte de glace","color":"gray"}]
