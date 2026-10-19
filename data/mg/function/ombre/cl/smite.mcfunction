# Rayon smite : un pas de 0,5 bloc
particle minecraft:end_rod ~ ~ ~ 0 0 0 0 1 force
scoreboard players add $olr mg.st 1
execute positioned ~-0.6 ~-0.6 ~-0.6 as @e[tag=mg.olm,dx=0.2,dy=0.2,dz=0.2,limit=1] positioned ~0.6 ~0.6 ~0.6 run return run function mg:ombre/cl/smite_hit with storage mg:ombre s
execute unless block ~ ~ ~ #mg:tv_pass run return run function mg:ombre/cl/smite_end
execute if score $olr mg.st matches 48.. run return run function mg:ombre/cl/smite_end
execute positioned ^ ^ ^0.5 run function mg:ombre/cl/smite
