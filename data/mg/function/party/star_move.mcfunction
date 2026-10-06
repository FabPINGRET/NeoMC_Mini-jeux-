# Nouvelle case pour l'étoile : 1..31, jamais la même que la précédente
execute store result score $tmp mg.st run random value 1..30
execute if score $tmp mg.st >= $mps mg.st run scoreboard players add $tmp mg.st 1
scoreboard players operation $mps mg.st = $tmp mg.st
function mg:party/star_place
