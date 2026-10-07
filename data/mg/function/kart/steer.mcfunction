# Direction : virage plus serré à basse vitesse, inversé en marche arrière, tête-à-queue si touché
scoreboard players set $kt mg.st 0
execute if score @s mg.khi matches 1.. run scoreboard players set $kt mg.st 36
execute if score @s mg.khi matches 1.. run return run scoreboard players remove @s mg.khi 1
scoreboard players operation $ka mg.st = @s mg.ksp
execute if score $ka mg.st matches ..-1 run scoreboard players operation $ka mg.st *= #km1 mg.st
scoreboard players set $kT mg.st 0
execute if score $ka mg.st matches 4..24 run scoreboard players set $kT mg.st 6
execute if score $ka mg.st matches 25..59 run scoreboard players set $kT mg.st 5
execute if score $ka mg.st matches 60.. run scoreboard players set $kT mg.st 4
execute if score $kl mg.st matches 1 run scoreboard players operation $kt mg.st -= $kT mg.st
execute if score $kr mg.st matches 1 run scoreboard players operation $kt mg.st += $kT mg.st
execute if score @s mg.ksp matches ..-1 run scoreboard players operation $kt mg.st *= #km1 mg.st
function mg:kart/drift
