# Aiguillage : table du circuit en cours (générée dans t1/, t2/ ou t3/ pour l'arène de bataille)
execute if score $ktr mg.st matches 2 run function mg:kart/t2/fl_remove
execute if score $ktr mg.st matches 3 run function mg:kart/t3/fl_remove
execute unless score $ktr mg.st matches 2..3 run function mg:kart/t1/fl_remove
