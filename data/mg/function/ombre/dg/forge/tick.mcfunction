# Forge écarlate (se) : chaque seconde
execute unless entity @a[tag=mg.olw,x=209,y=51,z=125,dx=27,dy=14,dz=89] run scoreboard players add $odw5 mg.st 1
execute if entity @a[tag=mg.olw,x=209,y=51,z=125,dx=27,dy=14,dz=89] run scoreboard players set $odw5 mg.st 0
execute if score $odw5 mg.st matches 40.. unless score $od5 mg.st matches 0 run return run function mg:ombre/dg/forge/reset
execute store result score $n mg.st if entity @e[tag=mg.oldg5]
execute if score $od5 mg.st matches 0 if entity @a[tag=mg.olw,x=215,y=52,z=131,dx=14,dy=5,dz=14] positioned 222.5 52 138.5 run function mg:ombre/dg/forge/wave0
execute if score $od5 mg.st matches 1 positioned 222.5 52 138.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg5] run function mg:ombre/dg/forge/clear0
execute if score $od5 mg.st matches 2 if entity @a[tag=mg.olw,x=214,y=52,z=149,dx=16,dy=6,dz=16] positioned 222.5 52 157.5 run function mg:ombre/dg/forge/wave1
execute if score $od5 mg.st matches 3 positioned 222.5 52 157.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg5] run function mg:ombre/dg/forge/clear1
execute if score $od5 mg.st matches 4 if entity @a[tag=mg.olw,x=214,y=52,z=169,dx=16,dy=6,dz=16] positioned 222.5 52 177.5 run function mg:ombre/dg/forge/wave2
execute if score $od5 mg.st matches 5 positioned 222.5 52 177.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg5] run function mg:ombre/dg/forge/clear2
execute if score $od5 mg.st matches 6 if entity @a[tag=mg.olw,x=211,y=52,z=189,dx=22,dy=9,dz=22] positioned 222.5 52 200.5 run function mg:ombre/dg/forge/alpha
execute if score $od5 mg.st matches 7 run bossbar set mg:oldg5 players @a[x=209,y=51,z=125,dx=27,dy=14,dz=89]
execute if score $od5 mg.st matches 7 store result bossbar mg:oldg5 value run data get entity @e[tag=mg.oldga,tag=mg.oldg5,limit=1] Health
execute if score $od5 mg.st matches 7 positioned 222.5 52 200.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldga,tag=mg.oldg5] run function mg:ombre/dg/forge/win
