# Aiguillage : table du circuit en cours (générée dans t1/ ou t2/)
execute if score $ktr mg.st matches 2 run function mg:kart/t2/gate_off
execute unless score $ktr mg.st matches 2 run function mg:kart/t1/gate_off
