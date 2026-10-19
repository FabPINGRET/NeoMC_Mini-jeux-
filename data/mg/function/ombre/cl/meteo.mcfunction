# Rayon meteo : un pas de 0,5 bloc
particle minecraft:small_flame ~ ~ ~ 0 0 0 0 1
scoreboard players add $olr mg.st 1
execute if entity @e[tag=mg.olm,distance=..1.5] run return run function mg:ombre/cl/meteo_end
execute unless block ~ ~ ~ #mg:tv_pass run return run function mg:ombre/cl/meteo_end
execute if score $olr mg.st matches 80.. run return run function mg:ombre/cl/meteo_end
execute positioned ^ ^ ^0.5 run function mg:ombre/cl/meteo
