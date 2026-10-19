# Pluie de flèches : zone visée (30 blocs)
scoreboard players operation $d mg.st = $pa mg.st
scoreboard players operation $d mg.st /= #2 mg.st
scoreboard players add $d mg.st 5
execute store result storage mg:ombre s.d int 1 run scoreboard players get $d mg.st
scoreboard players set $olr mg.st 0
scoreboard players operation $own mg.st = @s mg.olpid
execute anchored eyes positioned ^ ^ ^0.6 run function mg:ombre/cl/aim
playsound minecraft:entity.arrow.shoot player @a ~ ~ ~ 1 0.7
function mg:ombre/cl/end
