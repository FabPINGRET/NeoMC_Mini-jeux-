# Dérapage : ESPACE + virage à plus de 45 ; étincelles bleues (25 ticks) puis orange (55) ; mini-turbo au relâchement
execute if score @s mg.kdr matches 0 if score $kj mg.st matches 1 if score $kg mg.st matches 1 if score @s mg.ksp matches 45.. if score $kl mg.st matches 1 run function mg:kart/drift_start {d:-1}
execute if score @s mg.kdr matches 0 if score $kj mg.st matches 1 if score $kg mg.st matches 1 if score @s mg.ksp matches 45.. if score $kr mg.st matches 1 run function mg:kart/drift_start {d:1}
execute if score @s mg.kdr matches 1.. if score $kj mg.st matches 1 if score @s mg.ksp matches 30.. run return run function mg:kart/drift_hold
execute if score @s mg.kdr matches 1.. run function mg:kart/drift_end
