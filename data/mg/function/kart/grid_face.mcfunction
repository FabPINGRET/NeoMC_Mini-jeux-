# Le kart de @s est posé sur sa place de grille, dans l'axe de la piste (et pas dans le sens du regard du joueur)
function mg:kart/kk
scoreboard players operation $gi mg.st = @s mg.ri
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] run function mg:kart/grid_tp
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s on passengers run rotate @s ~ 0
tag @e[tag=mg.kk] remove mg.kk
