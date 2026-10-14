# Un pas (0,5 bloc) du tir à impulsions
particle minecraft:dust{color:[0.35,0.75,1.0],scale:0.7} ~ ~ ~ 0 0 0 0 1 force
scoreboard players add $tvr mg.st 1
execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[tag=mg.tvd,dx=0,dy=0,dz=0,limit=1] positioned ~0.5 ~0.5 ~0.5 run return run function mg:terra/hit2
execute unless block ~ ~ ~ #mg:tv_pass run return run particle minecraft:electric_spark ~ ~ ~ 0.1 0.1 0.1 0.2 6
execute if score $tvr mg.st matches ..80 positioned ^ ^ ^0.5 run function mg:terra/ray2
