# Chaque tick (monde des mini-jeux) : portail d'Ombrelune, session du monde
execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x=39,y=64,z=-9,dx=2,dy=2,dz=0] run function mg:ombre/enter
particle minecraft:dust{color:[0.7,0.45,1.0],scale:1.1} 40.5 67 -8.5 1.0 1.4 0.05 0 3
particle minecraft:reverse_portal 40.5 67 -8.5 1.0 1.4 0.05 0 2
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block 40 63 -9 minecraft:chiseled_polished_blackstone run function mg:ombre/portal_build
execute unless score $olw mg.st matches 1 if entity @a[tag=mg.olw] run function mg:ombre/session_start
execute if score $olw mg.st matches 1 unless entity @a[tag=mg.olw] run function mg:ombre/session_end
execute if score $olw mg.st matches 1 in mg:ombrelune run function mg:ombre/tick
