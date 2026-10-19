# Tombeaux d'Azhar : terminé
scoreboard players set $od4 mg.st 8
bossbar set mg:oldg4 players
particle minecraft:totem_of_undying 96 49 48 1 1 1 0.3 80 force
execute as @a[tag=mg.olw,x=93,y=47,z=35,dx=89,dy=14,dz=27] run function mg:ombre/dg/tomb/rw
