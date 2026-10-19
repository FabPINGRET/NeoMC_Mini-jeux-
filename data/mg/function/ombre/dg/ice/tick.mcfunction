# Grotte de givre (n) : chaque seconde
execute unless entity @a[tag=mg.olw,x=-31,y=65,z=-203,dx=89,dy=14,dz=27] run scoreboard players add $odw2 mg.st 1
execute if entity @a[tag=mg.olw,x=-31,y=65,z=-203,dx=89,dy=14,dz=27] run scoreboard players set $odw2 mg.st 0
execute if score $odw2 mg.st matches 40.. unless score $od2 mg.st matches 0 run return run function mg:ombre/dg/ice/reset
execute store result score $n mg.st if entity @e[tag=mg.oldg2]
execute if score $od2 mg.st matches 0 if entity @a[tag=mg.olw,x=-25,y=66,z=-197,dx=14,dy=5,dz=14] positioned -17.5 66 -189.5 run function mg:ombre/dg/ice/wave0
execute if score $od2 mg.st matches 1 positioned -17.5 66 -189.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg2] run function mg:ombre/dg/ice/clear0
execute if score $od2 mg.st matches 2 if entity @a[tag=mg.olw,x=-7,y=66,z=-198,dx=16,dy=6,dz=16] positioned 1.5 66 -189.5 run function mg:ombre/dg/ice/wave1
execute if score $od2 mg.st matches 3 positioned 1.5 66 -189.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg2] run function mg:ombre/dg/ice/clear1
execute if score $od2 mg.st matches 4 if entity @a[tag=mg.olw,x=13,y=66,z=-198,dx=16,dy=6,dz=16] positioned 21.5 66 -189.5 run function mg:ombre/dg/ice/wave2
execute if score $od2 mg.st matches 5 positioned 21.5 66 -189.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg2] run function mg:ombre/dg/ice/clear2
execute if score $od2 mg.st matches 6 if entity @a[tag=mg.olw,x=33,y=66,z=-201,dx=22,dy=9,dz=22] positioned 44.5 66 -189.5 run function mg:ombre/dg/ice/alpha
execute if score $od2 mg.st matches 7 run bossbar set mg:oldg2 players @a[x=-31,y=65,z=-203,dx=89,dy=14,dz=27]
execute if score $od2 mg.st matches 7 store result bossbar mg:oldg2 value run data get entity @e[tag=mg.oldga,tag=mg.oldg2,limit=1] Health
execute if score $od2 mg.st matches 7 positioned 44.5 66 -189.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldga,tag=mg.oldg2] run function mg:ombre/dg/ice/win
