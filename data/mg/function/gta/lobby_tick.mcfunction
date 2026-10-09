# Chaque tick (core/tick, monde des mini-jeux) : portail de Neo City, session du monde GTA
execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x=9,y=64,z=-20,dx=0,dy=2,dz=2] run function mg:gta/enter
particle minecraft:dust{color:[1.0,0.82,0.1],scale:1.1} 9.5 66.5 -18.5 0.05 1.3 1.1 0 3
particle minecraft:portal 9.5 66.5 -18.5 0.05 1.3 1.1 0.3 4
execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block 9 63 -19 minecraft:chiseled_polished_blackstone run function mg:gta/portal_build
execute unless score $gtw mg.st matches 1 if entity @a[tag=mg.gtw] run function mg:gta/session_start
execute if score $gtw mg.st matches 1 unless entity @a[tag=mg.gtw] run function mg:gta/session_end
execute if score $gtw mg.st matches 1 run function mg:gta/tick
