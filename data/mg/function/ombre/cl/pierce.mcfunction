# Rayon pierce : un pas de 0,5 bloc
particle minecraft:dust{color:[0.6,1.0,0.5],scale:0.8} ~ ~ ~ 0 0 0 0 1 force
scoreboard players add $olr mg.st 1
execute positioned ~-0.6 ~-0.6 ~-0.6 as @e[tag=mg.olm,tag=!mg.olhitn,dx=0.2,dy=0.2,dz=0.2] positioned ~0.6 ~0.6 ~0.6 run function mg:ombre/cl/pierce_hit with storage mg:ombre s
execute unless block ~ ~ ~ #mg:tv_pass run return run function mg:ombre/cl/pierce_end
execute if score $olr mg.st matches 80.. run return run function mg:ombre/cl/pierce_end
execute positioned ^ ^ ^0.5 run function mg:ombre/cl/pierce
