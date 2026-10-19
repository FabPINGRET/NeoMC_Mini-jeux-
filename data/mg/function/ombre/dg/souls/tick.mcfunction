# Puits des âmes (sw) : chaque seconde
execute unless entity @a[tag=mg.olw,x=-223,y=45,z=131,dx=27,dy=14,dz=89] run scoreboard players add $odw7 mg.st 1
execute if entity @a[tag=mg.olw,x=-223,y=45,z=131,dx=27,dy=14,dz=89] run scoreboard players set $odw7 mg.st 0
execute if score $odw7 mg.st matches 40.. unless score $od7 mg.st matches 0 run return run function mg:ombre/dg/souls/reset
execute store result score $n mg.st if entity @e[tag=mg.oldg7]
execute if score $od7 mg.st matches 0 if entity @a[tag=mg.olw,x=-217,y=46,z=137,dx=14,dy=5,dz=14] positioned -209.5 46 144.5 run function mg:ombre/dg/souls/wave0
execute if score $od7 mg.st matches 1 positioned -209.5 46 144.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg7] run function mg:ombre/dg/souls/clear0
execute if score $od7 mg.st matches 2 if entity @a[tag=mg.olw,x=-218,y=46,z=155,dx=16,dy=6,dz=16] positioned -209.5 46 163.5 run function mg:ombre/dg/souls/wave1
execute if score $od7 mg.st matches 3 positioned -209.5 46 163.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg7] run function mg:ombre/dg/souls/clear1
execute if score $od7 mg.st matches 4 if entity @a[tag=mg.olw,x=-218,y=46,z=175,dx=16,dy=6,dz=16] positioned -209.5 46 183.5 run function mg:ombre/dg/souls/wave2
execute if score $od7 mg.st matches 5 positioned -209.5 46 183.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg7] run function mg:ombre/dg/souls/clear2
execute if score $od7 mg.st matches 6 if entity @a[tag=mg.olw,x=-221,y=46,z=195,dx=22,dy=9,dz=22] positioned -209.5 46 206.5 run function mg:ombre/dg/souls/alpha
execute if score $od7 mg.st matches 7 run bossbar set mg:oldg7 players @a[x=-223,y=45,z=131,dx=27,dy=14,dz=89]
execute if score $od7 mg.st matches 7 store result bossbar mg:oldg7 value run data get entity @e[tag=mg.oldga,tag=mg.oldg7,limit=1] Health
execute if score $od7 mg.st matches 7 positioned -209.5 46 206.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldga,tag=mg.oldg7] run function mg:ombre/dg/souls/win
