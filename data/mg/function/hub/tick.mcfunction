# Chaque tick (core/tick) : témoin du hub, entrées des cinq portails du hub, particules des huit portails
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block 0 63 -49 minecraft:mossy_stone_bricks run function mg:hub/build
execute if score $setup mg.st matches 1 in minecraft:overworld as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x=9,y=64,z=-53,dx=0,dy=2,dz=2] run function mg:hub/enter_pvp
execute if score $setup mg.st matches 1 in minecraft:overworld as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x=-9,y=64,z=-46,dx=0,dy=2,dz=2] run function mg:hub/enter_survie
execute if score $setup mg.st matches 1 in minecraft:overworld as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x=-3,y=64,z=-46,dx=0,dy=2,dz=2] run function mg:hub/enter_filon
execute if score $setup mg.st matches 1 in minecraft:overworld as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x=3,y=64,z=-46,dx=0,dy=2,dz=2] run function mg:hub/enter_floaty
execute if score $setup mg.st matches 1 in minecraft:overworld as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x=9,y=64,z=-46,dx=0,dy=2,dz=2] run function mg:hub/enter_foot
particle minecraft:reverse_portal -8.5 66 -52.5 0.05 1.1 0.9 0 1
particle minecraft:reverse_portal -2.5 66 -52.5 0.05 1.1 0.9 0 1
particle minecraft:reverse_portal 3.5 66 -52.5 0.05 1.1 0.9 0 1
particle minecraft:reverse_portal 9.5 66 -52.5 0.05 1.1 0.9 0 1
particle minecraft:reverse_portal -8.5 66 -45.5 0.05 1.1 0.9 0 1
particle minecraft:reverse_portal -2.5 66 -45.5 0.05 1.1 0.9 0 1
particle minecraft:reverse_portal 3.5 66 -45.5 0.05 1.1 0.9 0 1
particle minecraft:reverse_portal 9.5 66 -45.5 0.05 1.1 0.9 0 1
