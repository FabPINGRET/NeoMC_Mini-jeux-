# Aiguillage : table du circuit en cours (générée dans t1/, t2/ ou t3/ pour l'arène de bataille)
execute if score $ktr mg.st matches 2 run function mg:kart/t2/gate_on
execute if score $ktr mg.st matches 3 run function mg:kart/t3/gate_on
execute unless score $ktr mg.st matches 2..3 run function mg:kart/t1/gate_on
