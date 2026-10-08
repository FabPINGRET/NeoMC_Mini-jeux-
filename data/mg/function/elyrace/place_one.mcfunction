# @s = joueur : prend la place suivante sur la plateforme de départ
scoreboard players add $ri mg.st 1
scoreboard players operation @s mg.ri = $ri mg.st
function mg:elyrace/place_tp
