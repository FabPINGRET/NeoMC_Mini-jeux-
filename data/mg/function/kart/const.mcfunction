# Aiguillage : table du circuit en cours (générée dans t1/, t2/ ou t3/ pour l'arène de bataille)
execute if score $ktr mg.st matches 2 run function mg:kart/t2/const
execute if score $ktr mg.st matches 3 run function mg:kart/t3/const
execute unless score $ktr mg.st matches 2..3 run function mg:kart/t1/const
execute if score $mp mg.st matches 1 unless score $ktr mg.st matches 3 run scoreboard players set $kLaps mg.st 2
