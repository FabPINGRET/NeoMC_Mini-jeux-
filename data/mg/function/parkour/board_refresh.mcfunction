# Réaffiche le record du parkour sur le panneau (après reconstruction)
scoreboard players set $pk20 mg.st 20
scoreboard players set $pk2 mg.st 2
scoreboard players operation $s mg.st = $pkrec mg.st
scoreboard players operation $s mg.st /= $pk20 mg.st
scoreboard players operation $d mg.st = $pkrec mg.st
scoreboard players operation $d mg.st %= $pk20 mg.st
scoreboard players operation $d mg.st /= $pk2 mg.st
execute store result storage mg:pk s int 1 run scoreboard players get $s mg.st
execute store result storage mg:pk d int 1 run scoreboard players get $d mg.st
function mg:parkour/board with storage mg:pk
