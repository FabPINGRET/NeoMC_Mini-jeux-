# @s : distance de sa balle (tag mg.gfmy) au trou → mg.gfm (blocs)
scoreboard players operation $gfdx mg.st = $gfcx mg.st
scoreboard players operation $gfdx mg.st -= @e[tag=mg.gfmy,limit=1] mg.gfx
scoreboard players operation $gfdz mg.st = $gfcz mg.st
scoreboard players operation $gfdz mg.st -= @e[tag=mg.gfmy,limit=1] mg.gfz
scoreboard players operation $gfdx mg.st /= #gf100 mg.st
scoreboard players operation $gfdz mg.st /= #gf100 mg.st
scoreboard players operation $gfdx mg.st *= $gfdx mg.st
scoreboard players operation $gfdz mg.st *= $gfdz mg.st
scoreboard players operation $gfsq mg.st = $gfdx mg.st
scoreboard players operation $gfsq mg.st += $gfdz mg.st
function mg:golf/isqrt
scoreboard players operation @s mg.gfm = $gfsr mg.st
scoreboard players operation @s mg.gfm /= #gf10 mg.st
