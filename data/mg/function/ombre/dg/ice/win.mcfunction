# Grotte de givre : terminé
scoreboard players set $od2 mg.st 8
bossbar set mg:oldg2 players
particle minecraft:totem_of_undying 54 67 -190 1 1 1 0.3 80 force
execute as @a[tag=mg.olw,x=-31,y=65,z=-203,dx=89,dy=14,dz=27] run function mg:ombre/dg/ice/rw
