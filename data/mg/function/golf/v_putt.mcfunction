# Putter : vitesse ∝ puissance, au ras du sol
scoreboard players operation $gfvx mg.st = $gfux mg.st
scoreboard players operation $gfvx mg.st *= $gfpw mg.st
scoreboard players operation $gfvz mg.st = $gfuz mg.st
scoreboard players operation $gfvz mg.st *= $gfpw mg.st
scoreboard players set $gfk mg.st 8
scoreboard players operation $gfvx mg.st *= $gfk mg.st
scoreboard players operation $gfvz mg.st *= $gfk mg.st
scoreboard players operation $gfvx mg.st /= #gf1000 mg.st
scoreboard players operation $gfvz mg.st /= #gf1000 mg.st
scoreboard players set $gfvy mg.st 0
