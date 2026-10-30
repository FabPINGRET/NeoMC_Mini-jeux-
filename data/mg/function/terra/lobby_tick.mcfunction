# Chaque tick (core/tick, monde des mini-jeux) : portail de Terra Nova, session du monde
execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x=-3,y=64,z=-53,dx=0,dy=2,dz=2] run function mg:terra/enter
particle minecraft:dust{color:[0.3,0.85,0.25],scale:1.1} -2.5 66.5 -51.5 0.05 1.3 1.1 0 3
particle minecraft:spore_blossom_air -2.5 66.5 -51.5 0.05 1.3 1.1 0 2
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block -3 63 -52 minecraft:chiseled_tuff_bricks run function mg:terra/portal_build
execute unless score $tvw mg.st matches 1 if entity @a[tag=mg.tvw] run function mg:terra/session_start
execute if score $tvw mg.st matches 1 unless entity @a[tag=mg.tvw] run function mg:terra/session_end
execute if score $tvw mg.st matches 1 in mg:terranova run function mg:terra/tick
