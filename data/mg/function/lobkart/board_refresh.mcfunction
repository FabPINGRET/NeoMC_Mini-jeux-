# Réaffiche le record sur le panneau (après reconstruction du décor)
function mg:lobkart/consts
scoreboard players operation $s mg.st = $klrec mg.st
scoreboard players operation $s mg.st /= #k20 mg.st
scoreboard players operation $d mg.st = $klrec mg.st
scoreboard players operation $d mg.st %= #k20 mg.st
scoreboard players operation $d mg.st /= #k2 mg.st
execute store result storage mg:lk s int 1 run scoreboard players get $s mg.st
execute store result storage mg:lk d int 1 run scoreboard players get $d mg.st
function mg:lobkart/board with storage mg:lk
