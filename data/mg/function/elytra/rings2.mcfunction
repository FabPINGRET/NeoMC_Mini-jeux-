# Grand parcours d'élytra : anneaux, échecs, guide, chrono (@s)
execute if score @s mg.ec matches 0 if entity @s[x=-32,y=290,z=-50,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 1 if entity @s[x=-2,y=284,z=-50,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 2 if entity @s[x=28,y=277,z=-50,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 3 if entity @s[x=28,y=270,z=-26,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 4 if entity @s[x=-2,y=264,z=-26,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 5 if entity @s[x=-32,y=258,z=-26,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 6 if entity @s[x=-32,y=251,z=-2,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 7 if entity @s[x=-2,y=244,z=-2,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 8 if entity @s[x=28,y=238,z=-2,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 9 if entity @s[x=28,y=232,z=22,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 10 if entity @s[x=-2,y=225,z=22,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 11 if entity @s[x=-32,y=218,z=22,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 12 if entity @s[x=-32,y=212,z=46,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 13 if entity @s[x=-2,y=206,z=46,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 14 if entity @s[x=28,y=199,z=46,dx=4,dy=4,dz=4] run function mg:elytra/pass
execute if score @s mg.ec matches 15.. run return run function mg:elytra/finish2
execute unless entity @s[y=185,dy=400] run return run function mg:elytra/fail
execute unless entity @s[x=-76,y=-64,z=-76,dx=152,dy=500,dz=152] run return run function mg:elytra/fail
execute if score @s mg.eg matches 40.. run return run function mg:elytra/fail
execute if score @s mg.ec matches 0 run particle minecraft:end_rod -29.5 292.5 -47.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 1 run particle minecraft:end_rod 0.5 286.5 -47.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 2 run particle minecraft:end_rod 30.5 279.5 -47.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 3 run particle minecraft:end_rod 30.5 272.5 -23.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 4 run particle minecraft:end_rod 0.5 266.5 -23.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 5 run particle minecraft:end_rod -29.5 260.5 -23.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 6 run particle minecraft:end_rod -29.5 253.5 0.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 7 run particle minecraft:end_rod 0.5 246.5 0.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 8 run particle minecraft:end_rod 30.5 240.5 0.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 9 run particle minecraft:end_rod 30.5 234.5 24.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 10 run particle minecraft:end_rod 0.5 227.5 24.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 11 run particle minecraft:end_rod -29.5 220.5 24.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 12 run particle minecraft:end_rod -29.5 214.5 48.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 13 run particle minecraft:end_rod 0.5 208.5 48.5 1 1 1 0.01 3 force @s
execute if score @s mg.ec matches 14 run particle minecraft:end_rod 30.5 201.5 48.5 1 1 1 0.01 3 force @s
execute if score @s mg.est matches 1 run function mg:elytra/hud2
