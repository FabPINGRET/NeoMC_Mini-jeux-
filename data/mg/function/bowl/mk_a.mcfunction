# marque du lancer #k dans la case (a) : X, - ou le nombre
execute if score #k mg.st matches 10 run return run data modify storage mg:bowl w.a set value "X"
execute if score #k mg.st matches 0 run return run data modify storage mg:bowl w.a set value "-"
execute store result storage mg:bowl w.a int 1 run scoreboard players get #k mg.st
