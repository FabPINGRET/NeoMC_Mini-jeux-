# Macro : x — le rouge convertit la colonne si elle n'est pas déjà rouge
$execute unless score c$(x) mg.tw matches 1 run function mg:turf/to_red with storage mg:tf
