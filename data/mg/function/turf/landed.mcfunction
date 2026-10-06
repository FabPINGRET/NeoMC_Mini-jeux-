# Flèche plantée (@s = flèche) : colonne visée (x = 100..130)
execute store result storage mg:tf x int 1 run data get entity @s Pos[0] 1
execute store result score $ax mg.st run data get entity @s Pos[0] 1
execute unless score $ax mg.st matches 100..130 run return run kill @s
execute if entity @s[tag=mg.ar_r] run function mg:turf/try_red with storage mg:tf
execute if entity @s[tag=mg.ar_b] run function mg:turf/try_blue with storage mg:tf
kill @s
