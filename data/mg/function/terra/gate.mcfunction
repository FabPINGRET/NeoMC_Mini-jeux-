# Chaque seconde : qui est dans la colonie (tag mg.tvout = dehors), messages aux portes
tag @a[tag=mg.tvin2] remove mg.tvin2
tag @a[tag=mg.tvw,x=-28,y=58,z=-28,dx=56,dy=30,dz=56] add mg.tvin2
execute as @a[tag=mg.tvw,tag=mg.tvin2,tag=mg.tvout] run function mg:terra/gate_in
execute as @a[tag=mg.tvw,tag=!mg.tvin2,tag=!mg.tvout] run function mg:terra/gate_out
