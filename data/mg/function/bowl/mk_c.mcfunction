# marque du lancer #k dans la case (c) : X, - ou le nombre
execute if score #k mg.st matches 10 run return run data modify storage mg:bowl w.c set value "X"
execute if score #k mg.st matches 0 run return run data modify storage mg:bowl w.c set value "-"
execute store result storage mg:bowl w.c int 1 run scoreboard players get #k mg.st
