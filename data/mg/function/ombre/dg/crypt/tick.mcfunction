# Cryptes de Valdor (w) : chaque seconde
execute unless entity @a[tag=mg.olw,x=-131,y=49,z=-37,dx=27,dy=14,dz=89] run scoreboard players add $odw0 mg.st 1
execute if entity @a[tag=mg.olw,x=-131,y=49,z=-37,dx=27,dy=14,dz=89] run scoreboard players set $odw0 mg.st 0
execute if score $odw0 mg.st matches 40.. unless score $od0 mg.st matches 0 run return run function mg:ombre/dg/crypt/reset
execute store result score $n mg.st if entity @e[tag=mg.oldg0]
execute if score $od0 mg.st matches 0 if entity @a[tag=mg.olw,x=-125,y=50,z=-31,dx=14,dy=5,dz=14] positioned -117.5 50 -23.5 run function mg:ombre/dg/crypt/wave0
execute if score $od0 mg.st matches 1 positioned -117.5 50 -23.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg0] run function mg:ombre/dg/crypt/clear0
execute if score $od0 mg.st matches 2 if entity @a[tag=mg.olw,x=-126,y=50,z=-13,dx=16,dy=6,dz=16] positioned -117.5 50 -4.5 run function mg:ombre/dg/crypt/wave1
execute if score $od0 mg.st matches 3 positioned -117.5 50 -4.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg0] run function mg:ombre/dg/crypt/clear1
execute if score $od0 mg.st matches 4 if entity @a[tag=mg.olw,x=-126,y=50,z=7,dx=16,dy=6,dz=16] positioned -117.5 50 15.5 run function mg:ombre/dg/crypt/wave2
execute if score $od0 mg.st matches 5 positioned -117.5 50 15.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg0] run function mg:ombre/dg/crypt/clear2
execute if score $od0 mg.st matches 6 if entity @a[tag=mg.olw,x=-129,y=50,z=27,dx=22,dy=9,dz=22] positioned -117.5 50 38.5 run function mg:ombre/dg/crypt/alpha
execute if score $od0 mg.st matches 7 run bossbar set mg:oldg0 players @a[x=-131,y=49,z=-37,dx=27,dy=14,dz=89]
execute if score $od0 mg.st matches 7 store result bossbar mg:oldg0 value run data get entity @e[tag=mg.oldga,tag=mg.oldg0,limit=1] Health
execute if score $od0 mg.st matches 7 positioned -117.5 50 38.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldga,tag=mg.oldg0] run function mg:ombre/dg/crypt/win
