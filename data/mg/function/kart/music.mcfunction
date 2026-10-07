# Séquenceur de musique du kart (chaque tick de course)
scoreboard players add $kmc mg.st 1
scoreboard players set $kmt mg.st 4
execute if score $kfl mg.st matches 1 run scoreboard players set $kmt mg.st 3
execute if score $kmc mg.st < $kmt mg.st run return 0
scoreboard players set $kmc mg.st 0
scoreboard players add $kms mg.st 1
execute if score $kms mg.st matches 128.. run scoreboard players set $kms mg.st 0
execute store result storage mg:kart mus.s int 1 run scoreboard players get $kms mg.st
execute store result storage mg:kart mus.t int 1 run scoreboard players get $ktr mg.st
function mg:kart/mus_play with storage mg:kart mus
