# Tapis d'entrée allumé (bloc d'or au centre, core/tick) : particules vertes, puis le joueur dessus descend (foot/go)
particle minecraft:dust{color:[0.35,0.95,0.35],scale:1.0} -5.5 64.2 -38.5 1.0 0.05 1.0 0 3
execute as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x=-6.7,y=63,z=-39.7,dx=1.4,dy=2.5,dz=1.4] run function mg:foot/go
