# @s (toutes les 10 ticks) : faisceau sur l'objectif + flèche devant soi (visibles par lui seul), distance
execute store result score $px mg.st run data get entity @s Pos[0]
execute store result score $pz mg.st run data get entity @s Pos[2]
scoreboard players operation $px mg.st -= @s mg.trox
scoreboard players operation $pz mg.st -= @s mg.troz
execute if score $px mg.st matches ..-1 run scoreboard players operation $px mg.st *= #m1 mg.st
execute if score $pz mg.st matches ..-1 run scoreboard players operation $pz mg.st *= #m1 mg.st
# distance ≈ max + min × 0,4
scoreboard players operation @s mg.trod = $px mg.st
scoreboard players operation @s mg.trod > $pz mg.st
scoreboard players operation $mn mg.st = $px mg.st
scoreboard players operation $mn mg.st < $pz mg.st
scoreboard players operation $mn mg.st *= #2 mg.st
scoreboard players operation $mn mg.st /= #5 mg.st
scoreboard players operation @s mg.trod += $mn mg.st
execute if score @s mg.trod matches ..5 run return 0
execute store result storage mg:terra o.x int 1 run scoreboard players get @s mg.trox
execute store result storage mg:terra o.y int 1 run scoreboard players get @s mg.troy
execute store result storage mg:terra o.z int 1 run scoreboard players get @s mg.troz
function mg:terra/rpg/ind_m with storage mg:terra o
