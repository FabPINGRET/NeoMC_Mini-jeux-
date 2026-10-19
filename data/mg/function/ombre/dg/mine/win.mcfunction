# Mines profondes : terminé
scoreboard players set $od6 mg.st 8
bossbar set mg:oldg6 players
particle minecraft:totem_of_undying -48 49 228 1 1 1 0.3 80 force
execute as @a[tag=mg.olw,x=-61,y=47,z=143,dx=27,dy=14,dz=89] run function mg:ombre/dg/mine/rw
