# Tir perçant
scoreboard players operation $d mg.st = $pa mg.st
scoreboard players add $d mg.st 8
execute store result storage mg:ombre s.d int 1 run scoreboard players get $d mg.st
playsound minecraft:entity.arrow.shoot player @a ~ ~ ~ 1 1.4
scoreboard players set $olr mg.st 0
execute anchored eyes positioned ^ ^ ^0.6 run function mg:ombre/cl/pierce
tag @e[tag=mg.olhitn] remove mg.olhitn
function mg:ombre/cl/end
