# Bois/Fer : vitesse ∝ √puissance (distance ≈ proportionnelle à la jauge), élévation ~25°
scoreboard players operation $gfsq mg.st = $gfpw mg.st
scoreboard players operation $gfsq mg.st *= #gf10000 mg.st
function mg:golf/isqrt
scoreboard players operation $gfvx mg.st = $gfux mg.st
scoreboard players operation $gfvx mg.st *= $gfsr mg.st
scoreboard players operation $gfvz mg.st = $gfuz mg.st
scoreboard players operation $gfvz mg.st *= $gfsr mg.st
scoreboard players set $gfk mg.st 22
scoreboard players operation $gfvx mg.st *= $gfk mg.st
scoreboard players operation $gfvz mg.st *= $gfk mg.st
scoreboard players operation $gfvx mg.st /= #gf10000 mg.st
scoreboard players operation $gfvz mg.st /= #gf10000 mg.st
scoreboard players operation $gfvy mg.st = $gfsr mg.st
