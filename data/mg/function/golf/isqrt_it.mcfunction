scoreboard players operation $gfst mg.st = $gfsq mg.st
scoreboard players operation $gfst mg.st /= $gfsr mg.st
scoreboard players operation $gfsr mg.st += $gfst mg.st
scoreboard players operation $gfsr mg.st /= #gf2 mg.st
execute if score $gfsr mg.st matches ..0 run scoreboard players set $gfsr mg.st 1
