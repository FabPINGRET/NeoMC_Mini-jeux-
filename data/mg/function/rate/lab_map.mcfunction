# Macro {m} : libellé de la carte m = moyenne des votes « carte »
$scoreboard players operation $rs mg.st = #m$(m) mg.rts
$scoreboard players operation $rn mg.st = #m$(m) mg.rtn
function mg:rate/avg
execute store result storage mg:rate tmp.i int 1 run scoreboard players get $ra mg.st
$data modify storage mg:rate tmp.k set value "r$(m)"
function mg:rate/set with storage mg:rate tmp
