# Nid des tisseuses : terminé
scoreboard players set $od1 mg.st 8
bossbar set mg:oldg1 players
particle minecraft:totem_of_undying -212 55 -208 1 1 1 0.3 80 force
execute as @a[tag=mg.olw,x=-225,y=53,z=-211,dx=27,dy=14,dz=89] run function mg:ombre/dg/nest/rw
