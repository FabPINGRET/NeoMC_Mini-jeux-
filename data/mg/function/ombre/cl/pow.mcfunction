# @s : puissance des compétences : $pf (Force + 2 × palier), $pa (Agilité + 2 × palier), $pw (Esprit + 2 × palier)
scoreboard players operation $t2 mg.st = @s mg.olwt
scoreboard players operation $t2 mg.st *= #2 mg.st
scoreboard players operation $pf mg.st = @s mg.ols2
scoreboard players operation $pf mg.st += $t2 mg.st
scoreboard players operation $pa mg.st = @s mg.ols3
scoreboard players operation $pa mg.st += $t2 mg.st
scoreboard players operation $pw mg.st = @s mg.ols4
scoreboard players operation $pw mg.st += $t2 mg.st
tag @s add mg.olcast
