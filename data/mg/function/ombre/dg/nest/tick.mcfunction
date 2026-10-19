# Nid des tisseuses (nw) : chaque seconde
execute unless entity @a[tag=mg.olw,x=-225,y=53,z=-211,dx=27,dy=14,dz=89] run scoreboard players add $odw1 mg.st 1
execute if entity @a[tag=mg.olw,x=-225,y=53,z=-211,dx=27,dy=14,dz=89] run scoreboard players set $odw1 mg.st 0
execute if score $odw1 mg.st matches 40.. unless score $od1 mg.st matches 0 run return run function mg:ombre/dg/nest/reset
execute store result score $n mg.st if entity @e[tag=mg.oldg1]
execute if score $od1 mg.st matches 0 if entity @a[tag=mg.olw,x=-219,y=54,z=-143,dx=14,dy=5,dz=14] positioned -211.5 54 -135.5 run function mg:ombre/dg/nest/wave0
execute if score $od1 mg.st matches 1 positioned -211.5 54 -135.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg1] run function mg:ombre/dg/nest/clear0
execute if score $od1 mg.st matches 2 if entity @a[tag=mg.olw,x=-220,y=54,z=-163,dx=16,dy=6,dz=16] positioned -211.5 54 -154.5 run function mg:ombre/dg/nest/wave1
execute if score $od1 mg.st matches 3 positioned -211.5 54 -154.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg1] run function mg:ombre/dg/nest/clear1
execute if score $od1 mg.st matches 4 if entity @a[tag=mg.olw,x=-220,y=54,z=-183,dx=16,dy=6,dz=16] positioned -211.5 54 -174.5 run function mg:ombre/dg/nest/wave2
execute if score $od1 mg.st matches 5 positioned -211.5 54 -174.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg1] run function mg:ombre/dg/nest/clear2
execute if score $od1 mg.st matches 6 if entity @a[tag=mg.olw,x=-223,y=54,z=-209,dx=22,dy=9,dz=22] positioned -211.5 54 -197.5 run function mg:ombre/dg/nest/alpha
execute if score $od1 mg.st matches 7 run bossbar set mg:oldg1 players @a[x=-225,y=53,z=-211,dx=27,dy=14,dz=89]
execute if score $od1 mg.st matches 7 store result bossbar mg:oldg1 value run data get entity @e[tag=mg.oldga,tag=mg.oldg1,limit=1] Health
execute if score $od1 mg.st matches 7 positioned -211.5 54 -197.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldga,tag=mg.oldg1] run function mg:ombre/dg/nest/win
