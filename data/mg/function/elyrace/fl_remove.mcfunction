# Libère le chargement forcé de la zone de départ du parcours $xc
execute if score $xc mg.st matches 1 run function mg:elyrace/c1/fl_remove
execute if score $xc mg.st matches 2 run function mg:elyrace/c2/fl_remove
