# Mines profondes (s) : chaque seconde
execute unless entity @a[tag=mg.olw,x=-61,y=47,z=143,dx=27,dy=14,dz=89] run scoreboard players add $odw6 mg.st 1
execute if entity @a[tag=mg.olw,x=-61,y=47,z=143,dx=27,dy=14,dz=89] run scoreboard players set $odw6 mg.st 0
execute if score $odw6 mg.st matches 40.. unless score $od6 mg.st matches 0 run return run function mg:ombre/dg/mine/reset
execute store result score $n mg.st if entity @e[tag=mg.oldg6]
execute if score $od6 mg.st matches 0 if entity @a[tag=mg.olw,x=-55,y=48,z=149,dx=14,dy=5,dz=14] positioned -47.5 48 156.5 run function mg:ombre/dg/mine/wave0
execute if score $od6 mg.st matches 1 positioned -47.5 48 156.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg6] run function mg:ombre/dg/mine/clear0
execute if score $od6 mg.st matches 2 if entity @a[tag=mg.olw,x=-56,y=48,z=167,dx=16,dy=6,dz=16] positioned -47.5 48 175.5 run function mg:ombre/dg/mine/wave1
execute if score $od6 mg.st matches 3 positioned -47.5 48 175.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg6] run function mg:ombre/dg/mine/clear1
execute if score $od6 mg.st matches 4 if entity @a[tag=mg.olw,x=-56,y=48,z=187,dx=16,dy=6,dz=16] positioned -47.5 48 195.5 run function mg:ombre/dg/mine/wave2
execute if score $od6 mg.st matches 5 positioned -47.5 48 195.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldg6] run function mg:ombre/dg/mine/clear2
execute if score $od6 mg.st matches 6 if entity @a[tag=mg.olw,x=-59,y=48,z=207,dx=22,dy=9,dz=22] positioned -47.5 48 218.5 run function mg:ombre/dg/mine/alpha
execute if score $od6 mg.st matches 7 run bossbar set mg:oldg6 players @a[x=-61,y=47,z=143,dx=27,dy=14,dz=89]
execute if score $od6 mg.st matches 7 store result bossbar mg:oldg6 value run data get entity @e[tag=mg.oldga,tag=mg.oldg6,limit=1] Health
execute if score $od6 mg.st matches 7 positioned -47.5 48 218.5 if loaded ~ ~ ~ unless entity @e[tag=mg.oldga,tag=mg.oldg6] run function mg:ombre/dg/mine/win
