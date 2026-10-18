# @s : garde la canne ? Retourne 1 ou 0, sans message (à la position de @s)
execute at @s unless dimension minecraft:overworld run return 0
execute if score $lfoff mg.st matches 1 run return 0
execute unless entity @s[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.pkr,tag=!mg.lk,tag=!mg.ely,tag=!mg.elyf,tag=!mg.xso,tag=!mg.dl,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.mpp,tag=!mg.pvpc,tag=!mg.thbun,tag=!mg.thmini,gamemode=!spectator] run return 0
execute positioned 30.5 64 -29.5 unless entity @s[distance=..12] run return 0
return 1
