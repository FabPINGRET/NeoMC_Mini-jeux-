# Temple englouti (ne) : chaque seconde
execute unless entity @a[tag=mg.olw,x=132,y=47,z=-213,dx=89,dy=14,dz=27] run scoreboard players add $odw3 mg.st 1
execute if entity @a[tag=mg.olw,x=132,y=47,z=-213,dx=89,dy=14,dz=27] run scoreboard players set $odw3 mg.st 0
execute if score $odw3 mg.st matches 40.. unless score $od3 mg.st matches 0 run return run function mg:ombre/dg/sunken/reset
execute store result score $n mg.st if entity @e[tag=mg.oldg3]
execute if score $od3 mg.st matches 0 if entity @a[tag=mg.olw,x=138,y=48,z=-207,dx=14,dy=5,dz=14] positioned 145.5 48 -199.5 run function mg:ombre/dg/sunken/wave0
execute if score $od3 mg.st matches 1 positioned 145.5 48 -199.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg3] run function mg:ombre/dg/sunken/clear0
execute if score $od3 mg.st matches 2 if entity @a[tag=mg.olw,x=156,y=48,z=-208,dx=16,dy=6,dz=16] positioned 164.5 48 -199.5 run function mg:ombre/dg/sunken/wave1
execute if score $od3 mg.st matches 3 positioned 164.5 48 -199.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg3] run function mg:ombre/dg/sunken/clear1
execute if score $od3 mg.st matches 4 if entity @a[tag=mg.olw,x=176,y=48,z=-208,dx=16,dy=6,dz=16] positioned 184.5 48 -199.5 run function mg:ombre/dg/sunken/wave2
execute if score $od3 mg.st matches 5 positioned 184.5 48 -199.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg3] run function mg:ombre/dg/sunken/clear2
execute if score $od3 mg.st matches 6 if entity @a[tag=mg.olw,x=196,y=48,z=-211,dx=22,dy=9,dz=22] positioned 207.5 48 -199.5 run function mg:ombre/dg/sunken/alpha
execute if score $od3 mg.st matches 7 run bossbar set mg:oldg3 players @a[x=132,y=47,z=-213,dx=89,dy=14,dz=27]
execute if score $od3 mg.st matches 7 store result bossbar mg:oldg3 value run data get entity @e[tag=mg.oldga,tag=mg.oldg3,limit=1] Health
execute if score $od3 mg.st matches 7 positioned 207.5 48 -199.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldga,tag=mg.oldg3] run function mg:ombre/dg/sunken/win
