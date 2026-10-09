# Macro {f, g} : score global du jeu = moyenne des votes « mode » et « fun » réunis
$scoreboard players operation $rs mg.st = #g$(g) mg.rgs
$scoreboard players operation $rs mg.st += #g$(g) mg.rfs
$scoreboard players operation $rn mg.st = #g$(g) mg.rgn
$scoreboard players operation $rn mg.st += #g$(g) mg.rfn
execute if score $rn mg.st matches ..0 run return 0
function mg:rate/avg
execute store result storage mg:rate tmp.i int 1 run scoreboard players get $ra mg.st
$data modify storage mg:rate tmp.k set value "f$(f)"
function mg:rate/fset with storage mg:rate tmp
