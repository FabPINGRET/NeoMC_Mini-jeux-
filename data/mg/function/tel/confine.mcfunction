# @s reste sur (ou autour de) sa parcelle
execute store result storage mg:tel q.x int 1 run scoreboard players get @s mg.tx
execute store result storage mg:tel q.z int 1 run scoreboard players get @s mg.tz
function mg:tel/confine_m with storage mg:tel q
