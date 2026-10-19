# Puits des âmes : terminé
scoreboard players set $od7 mg.st 8
bossbar set mg:oldg7 players
particle minecraft:totem_of_undying -210 47 216 1 1 1 0.3 80 force
execute as @a[tag=mg.olw,x=-223,y=45,z=131,dx=27,dy=14,dz=89] run function mg:ombre/dg/souls/rw
