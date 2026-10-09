# marque du lancer #k dans la case (b) : X, - ou le nombre
execute if score #k mg.st matches 10 run return run data modify storage mg:bowl w.b set value "X"
execute if score #k mg.st matches 0 run return run data modify storage mg:bowl w.b set value "-"
execute store result storage mg:bowl w.b int 1 run scoreboard players get #k mg.st
