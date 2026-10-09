# @s : sous-munition (même lanceur, direction écartée au hasard)
tag @s add mg.bomb
data merge entity @s {fuse:400s,explosion_power:0.0f}
scoreboard players operation @s mg.bid = $bid mg.st
scoreboard players set @s mg.bty 4
scoreboard players set @s mg.bc4 20
execute store result score $br mg.st run random value -280..280
scoreboard players operation $br mg.st += $mx mg.st
execute store result entity @s Motion[0] double 0.001 run scoreboard players get $br mg.st
execute store result score $br mg.st run random value -150..80
scoreboard players operation $br mg.st += $my mg.st
execute store result entity @s Motion[1] double 0.001 run scoreboard players get $br mg.st
execute store result score $br mg.st run random value -280..280
scoreboard players operation $br mg.st += $mz mg.st
execute store result entity @s Motion[2] double 0.001 run scoreboard players get $br mg.st
