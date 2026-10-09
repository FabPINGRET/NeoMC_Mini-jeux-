# Macro {m, f, g} : ajoute la note de @s ($ra1 mode, $rb1 carte, $rc1 fun) aux totaux, puis recalcule les libellés
$execute if score $ra1 mg.st matches 1.. run scoreboard players operation #g$(g) mg.rgs += $ra1 mg.st
$execute if score $ra1 mg.st matches 1.. run scoreboard players add #g$(g) mg.rgn 1
$execute if score $rc1 mg.st matches 1.. run scoreboard players operation #g$(g) mg.rfs += $rc1 mg.st
$execute if score $rc1 mg.st matches 1.. run scoreboard players add #g$(g) mg.rfn 1
$execute if score $rb1 mg.st matches 1.. run scoreboard players operation #m$(m) mg.rts += $rb1 mg.st
$execute if score $rb1 mg.st matches 1.. run scoreboard players add #m$(m) mg.rtn 1
$execute if score #m$(m) mg.rtn matches 1.. run function mg:rate/lab_map {m:$(m)}
$function mg:rate/lab_fam {f:"$(f)",g:$(g)}
