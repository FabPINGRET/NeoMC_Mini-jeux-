# Aiguillage : table du circuit en cours (générée dans t1/, t2/ ou t3/ pour l'arène de bataille)
execute if score $ktr mg.st matches 2 run function mg:kart/t2/mm_show
execute if score $ktr mg.st matches 3 run function mg:kart/t3/mm_show
execute unless score $ktr mg.st matches 2..3 run function mg:kart/t1/mm_show
