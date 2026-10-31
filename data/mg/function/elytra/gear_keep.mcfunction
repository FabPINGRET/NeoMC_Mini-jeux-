# @s garde-t-il l'équipement du spawn ? 1 ou 0 (au spawn, overworld, en aventure, pas occupé ailleurs)
execute at @s unless dimension minecraft:overworld run return 0
execute unless entity @s[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,gamemode=adventure,tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.pkr,tag=!mg.lk,tag=!mg.ely,tag=!mg.xso,tag=!mg.dl,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.mpp,tag=!mg.pvpc,tag=!mg.thbun,tag=!mg.thmini] run return 0
return 1
