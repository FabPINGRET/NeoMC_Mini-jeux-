# @s (toutes les 10 ticks) : faisceau sur l'objectif + flèche devant soi (visibles par lui seul), distance
execute store result score $px mg.st run data get entity @s Pos[0]
execute store result score $pz mg.st run data get entity @s Pos[2]
scoreboard players operation $px mg.st -= @s mg.olox
scoreboard players operation $pz mg.st -= @s mg.oloz
execute if score $px mg.st matches ..-1 run scoreboard players operation $px mg.st *= #m1 mg.st
execute if score $pz mg.st matches ..-1 run scoreboard players operation $pz mg.st *= #m1 mg.st
scoreboard players operation @s mg.olod = $px mg.st
scoreboard players operation @s mg.olod > $pz mg.st
scoreboard players operation $mn mg.st = $px mg.st
scoreboard players operation $mn mg.st < $pz mg.st
scoreboard players operation $mn mg.st *= #2 mg.st
scoreboard players operation $mn mg.st /= #5 mg.st
scoreboard players operation @s mg.olod += $mn mg.st
execute if score @s mg.olod matches ..4 run return 0
execute store result storage mg:ombre o.x int 1 run scoreboard players get @s mg.olox
execute store result storage mg:ombre o.y int 1 run scoreboard players get @s mg.oloy
execute store result storage mg:ombre o.z int 1 run scoreboard players get @s mg.oloz
function mg:ombre/ind_m with storage mg:ombre o
