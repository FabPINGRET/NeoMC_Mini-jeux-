# Pion sur sa case (@s) : centre de la case puis un coin selon l'ordre de passage, pour ne pas se marcher dessus
function mg:party/place_c
scoreboard players operation $po mg.st = @s mg.mpo
scoreboard players operation $po mg.st %= #4 mg.st
execute if score $po mg.st matches 0 at @s run tp @s ~-0.7 ~ ~-0.7
execute if score $po mg.st matches 1 at @s run tp @s ~0.7 ~ ~-0.7
execute if score $po mg.st matches 2 at @s run tp @s ~-0.7 ~ ~0.7
execute if score $po mg.st matches 3 at @s run tp @s ~0.7 ~ ~0.7
