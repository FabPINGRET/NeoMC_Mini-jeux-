# Téléporte @s au centre de son plot : (2c+1)/2 vise le milieu du bloc, coordonnées négatives comprises
scoreboard players operation $tx mg.t = @s mg.pcx
scoreboard players operation $tx mg.t += @s mg.pcx
scoreboard players add $tx mg.t 1
scoreboard players operation $tz mg.t = @s mg.pcz
scoreboard players operation $tz mg.t += @s mg.pcz
scoreboard players add $tz mg.t 1
execute store result storage mg:c x double 0.5 run scoreboard players get $tx mg.t
execute store result storage mg:c z double 0.5 run scoreboard players get $tz mg.t
function mg:plot/tp_at with storage mg:c
