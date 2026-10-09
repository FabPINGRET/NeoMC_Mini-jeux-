# $tnlz = profondeur $tndepth dans le camp adverse de $tnside (côté 1 joue vers +z)
scoreboard players operation $tnlz mg.st = $tndepth mg.st
execute if score $tnside mg.st matches 2 run scoreboard players operation $tnlz mg.st *= #tnm1 mg.st
