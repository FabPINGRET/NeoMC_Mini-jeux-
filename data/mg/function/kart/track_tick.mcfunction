# Aiguillage : table du circuit en cours (générée dans t1/ ou t2/)
execute if score $ktr mg.st matches 2 run function mg:kart/t2/track_tick
execute unless score $ktr mg.st matches 2 run function mg:kart/t1/track_tick
