# Un pas (0,5 bloc) du scanner
particle minecraft:dust{color:[0.3,0.9,1.0],scale:0.5} ~ ~ ~ 0 0 0 0 1
scoreboard players add $tvr mg.st 1
execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[tag=mg.tvd,tag=!mg.trmount,dx=0,dy=0,dz=0,limit=1] run return run function mg:terra/rpg/scan_id
execute unless block ~ ~ ~ #mg:tv_pass run return 0
execute if score $tvr mg.st matches ..32 positioned ^ ^ ^0.5 run function mg:terra/rpg/scan_ray
