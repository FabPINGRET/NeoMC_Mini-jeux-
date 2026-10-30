particle minecraft:portal -11144 59 430 0 0 0 5 30
particle minecraft:dust_color_transition{from_color:[0.000,0.000,0.000],to_color:[0.529,0.000,0.529],scale:1} -11144 59 430 1 1 1 0 1 force
particle minecraft:dust_color_transition{from_color:[0.000,0.000,0.000],to_color:[0.529,0.000,0.529],scale:2} -11144 59 430 0.5 0.5 0.5 0 1 force
particle minecraft:dust_color_transition{from_color:[0.000,0.000,0.000],to_color:[0.529,0.000,0.529],scale:3} -11144 59 430 0.1 0.1 0.1 0 1 force
execute positioned -11144 58 430 as @a[distance=..2,tag=mg.flw] run damage @s 30 minecraft:dragon_breath
