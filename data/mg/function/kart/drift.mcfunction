# Dérapage : ESPACE + virage à plus de 40 ; mini-turbo bleu (20 ticks), orange (45), violet (80) au relâchement
execute if score @s mg.kdr matches 0 if score $kj mg.st matches 1 if score $kg mg.st matches 1 if score @s mg.ksp matches 40.. if score $kl mg.st matches 1 run function mg:kart/drift_start {d:-1}
execute if score @s mg.kdr matches 0 if score $kj mg.st matches 1 if score $kg mg.st matches 1 if score @s mg.ksp matches 40.. if score $kr mg.st matches 1 run function mg:kart/drift_start {d:1}
execute if score @s mg.kdr matches 1.. if score $kj mg.st matches 1 if score @s mg.ksp matches 30.. run return run function mg:kart/drift_hold
execute if score @s mg.kdr matches 1.. run function mg:kart/drift_end
