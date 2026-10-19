# Rayon fire : un pas de 0,5 bloc
particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.01 3 force
scoreboard players add $olr mg.st 1
execute positioned ~-0.6 ~-0.6 ~-0.6 if entity @e[tag=mg.olm,dx=0.2,dy=0.2,dz=0.2] positioned ~0.6 ~0.6 ~0.6 run return run function mg:ombre/cl/fire_end
execute unless block ~ ~ ~ #mg:tv_pass run return run function mg:ombre/cl/fire_end
execute if score $olr mg.st matches 60.. run return run function mg:ombre/cl/fire_end
execute positioned ^ ^ ^0.5 run function mg:ombre/cl/fire
