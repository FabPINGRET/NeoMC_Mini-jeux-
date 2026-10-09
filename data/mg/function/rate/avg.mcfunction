# $ra = moyenne × 10 arrondie de $rs / $rn
scoreboard players operation $ra mg.st = $rs mg.st
scoreboard players operation $ra mg.st *= #20 mg.st
scoreboard players operation $ra mg.st += $rn mg.st
scoreboard players operation $rd mg.st = $rn mg.st
scoreboard players operation $rd mg.st *= #2 mg.st
scoreboard players operation $ra mg.st /= $rd mg.st
execute if score $ra mg.st matches 51.. run scoreboard players set $ra mg.st 50
