# Nouvelle case pour l'étoile, jamais la même que la précédente
function mg:party/star_pick
execute if score $mpsn mg.st = $mps mg.st run return run function mg:party/star_move
scoreboard players operation $mps mg.st = $mpsn mg.st
function mg:party/star_place
