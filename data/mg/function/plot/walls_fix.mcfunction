# Répare les murs du plot de @s (centre mg.pcx / mg.pcz, murs à 12 blocs)
scoreboard players operation $a mg.t = @s mg.pcx
scoreboard players remove $a mg.t 12
execute store result storage mg:plot w.x1 int 1 run scoreboard players get $a mg.t
scoreboard players add $a mg.t 24
execute store result storage mg:plot w.x2 int 1 run scoreboard players get $a mg.t
scoreboard players operation $a mg.t = @s mg.pcz
scoreboard players remove $a mg.t 12
execute store result storage mg:plot w.z1 int 1 run scoreboard players get $a mg.t
scoreboard players add $a mg.t 24
execute store result storage mg:plot w.z2 int 1 run scoreboard players get $a mg.t
function mg:plot/walls with storage mg:plot w
