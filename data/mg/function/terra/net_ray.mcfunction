# Un pas (0,5 bloc) du filet
particle minecraft:block{block_state:"minecraft:cobweb"} ~ ~ ~ 0.05 0.05 0.05 0 2
scoreboard players add $tvr mg.st 1
execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[tag=mg.tvtg,tag=!mg.tvnetted,dx=0,dy=0,dz=0,limit=1] at @s run return run function mg:terra/net_on
execute unless block ~ ~ ~ #mg:tv_pass run return 0
execute if score $tvr mg.st matches ..48 positioned ^ ^ ^0.5 run function mg:terra/net_ray
