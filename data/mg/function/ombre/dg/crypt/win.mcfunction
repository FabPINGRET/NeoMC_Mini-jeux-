# Cryptes de Valdor : terminé
scoreboard players set $od0 mg.st 8
bossbar set mg:oldg0 players
particle minecraft:totem_of_undying -118 51 48 1 1 1 0.3 80 force
execute as @a[tag=mg.olw,x=-131,y=49,z=-37,dx=27,dy=14,dz=89] run function mg:ombre/dg/crypt/rw
