particle minecraft:dust{color:[1.0,0.6,0.1],scale:0.8} ~ ~ ~ 0 0 0 0 1
scoreboard players add $tvr mg.st 1
execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[tag=mg.tvhos,dx=0,dy=0,dz=0,limit=1] positioned ~0.5 ~0.5 ~0.5 run return run function mg:terra/rpg/cl/thit
execute unless block ~ ~ ~ #mg:tv_pass run return 0
execute if score $tvr mg.st matches ..32 positioned ^ ^ ^0.5 run function mg:terra/rpg/cl/tray
