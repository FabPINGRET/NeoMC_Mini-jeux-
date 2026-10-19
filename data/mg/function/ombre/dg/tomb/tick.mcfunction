# Tombeaux d'Azhar (e) : chaque seconde
execute unless entity @a[tag=mg.olw,x=93,y=47,z=35,dx=89,dy=14,dz=27] run scoreboard players add $odw4 mg.st 1
execute if entity @a[tag=mg.olw,x=93,y=47,z=35,dx=89,dy=14,dz=27] run scoreboard players set $odw4 mg.st 0
execute if score $odw4 mg.st matches 40.. unless score $od4 mg.st matches 0 run return run function mg:ombre/dg/tomb/reset
execute store result score $n mg.st if entity @e[tag=mg.oldg4]
execute if score $od4 mg.st matches 0 if entity @a[tag=mg.olw,x=161,y=48,z=41,dx=14,dy=5,dz=14] positioned 168.5 48 48.5 run function mg:ombre/dg/tomb/wave0
execute if score $od4 mg.st matches 1 positioned 168.5 48 48.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg4] run function mg:ombre/dg/tomb/clear0
execute if score $od4 mg.st matches 2 if entity @a[tag=mg.olw,x=141,y=48,z=40,dx=16,dy=6,dz=16] positioned 149.5 48 48.5 run function mg:ombre/dg/tomb/wave1
execute if score $od4 mg.st matches 3 positioned 149.5 48 48.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg4] run function mg:ombre/dg/tomb/clear1
execute if score $od4 mg.st matches 4 if entity @a[tag=mg.olw,x=121,y=48,z=40,dx=16,dy=6,dz=16] positioned 129.5 48 48.5 run function mg:ombre/dg/tomb/wave2
execute if score $od4 mg.st matches 5 positioned 129.5 48 48.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg4] run function mg:ombre/dg/tomb/clear2
execute if score $od4 mg.st matches 6 if entity @a[tag=mg.olw,x=95,y=48,z=37,dx=22,dy=9,dz=22] positioned 106.5 48 48.5 run function mg:ombre/dg/tomb/alpha
execute if score $od4 mg.st matches 7 run bossbar set mg:oldg4 players @a[x=93,y=47,z=35,dx=89,dy=14,dz=27]
execute if score $od4 mg.st matches 7 store result bossbar mg:oldg4 value run data get entity @e[tag=mg.oldga,tag=mg.oldg4,limit=1] Health
execute if score $od4 mg.st matches 7 positioned 106.5 48 48.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldga,tag=mg.oldg4] run function mg:ombre/dg/tomb/win
