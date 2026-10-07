# Pilote @s : n° de grille, téléporté à sa place
scoreboard players add $gi mg.st 1
scoreboard players operation @s mg.ri = $gi mg.st
function mg:kart/grid_tp
