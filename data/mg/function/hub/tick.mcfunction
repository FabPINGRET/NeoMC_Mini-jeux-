# Chaque tick (core/tick) : témoin du hub, entrées des cinq portails du hub, particules des huit portails
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block 0 63 -53 minecraft:mossy_stone_bricks run function mg:hub/build
execute if score $setup mg.st matches 1 in minecraft:overworld as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x=9,y=64,z=-55,dx=0,dy=2,dz=2] run function mg:hub/enter_pvp
execute if score $setup mg.st matches 1 in minecraft:overworld as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x=-9,y=64,z=-45,dx=0,dy=2,dz=2] run function mg:hub/enter_survie
execute if score $setup mg.st matches 1 in minecraft:overworld as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x=-9,y=64,z=-50,dx=0,dy=2,dz=2] run function mg:hub/enter_filon
execute if score $setup mg.st matches 1 in minecraft:overworld as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x=9,y=64,z=-50,dx=0,dy=2,dz=2] run function mg:hub/enter_floaty
execute if score $setup mg.st matches 1 in minecraft:overworld as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x=9,y=64,z=-45,dx=0,dy=2,dz=2] run function mg:hub/enter_foot
particle minecraft:reverse_portal -8.5 65 -54.5 0.05 1.1 0.9 0 1
particle minecraft:reverse_portal -5.5 65 -58.5 0.05 1.1 0.9 0 1
particle minecraft:reverse_portal 6.5 65 -58.5 0.05 1.1 0.9 0 1
particle minecraft:reverse_portal 9.5 65 -54.5 0.05 1.1 0.9 0 1
particle minecraft:reverse_portal -8.5 65 -44.5 0.05 1.1 0.9 0 1
particle minecraft:reverse_portal -8.5 65 -49.5 0.05 1.1 0.9 0 1
particle minecraft:reverse_portal 9.5 65 -49.5 0.05 1.1 0.9 0 1
particle minecraft:reverse_portal 9.5 65 -44.5 0.05 1.1 0.9 0 1
