particle minecraft:dust{color:[0.55,0.95,0.2],scale:1.1} ~ ~ ~ 0.05 0.05 0.05 0 2
scoreboard players add $tvr mg.st 1
execute as @a[tag=mg.tvw,gamemode=adventure,distance=..1.0] run return run function mg:terra/rpg/ab/spit_hit
execute unless block ~ ~ ~ #mg:tv_pass run return 0
execute if score $tvr mg.st matches ..22 positioned ^ ^ ^0.7 run function mg:terra/rpg/ab/spit_ray
