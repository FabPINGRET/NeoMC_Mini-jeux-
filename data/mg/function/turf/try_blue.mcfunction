# Macro : x — le bleu convertit la colonne si elle n'est pas déjà bleue
$execute unless score c$(x) mg.tw matches 2 run function mg:turf/to_blue with storage mg:tf
