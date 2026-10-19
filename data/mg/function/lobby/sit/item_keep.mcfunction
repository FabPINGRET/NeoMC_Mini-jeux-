# @s : garde l'objet 🎉 Emotes ? Retourne 1 ou 0, sans message (≠ sit/ok : ragoût et élytres le gardent)
# tourne sans « at @s » (core/tick) : la dimension se lit à la position du joueur
execute at @s unless dimension minecraft:overworld run return 0
execute if score $sitoff mg.st matches 1 run return 0
execute unless entity @s[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.pkr,tag=!mg.lk,tag=!mg.xso,tag=!mg.dl,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.mpp,tag=!mg.pvpc,gamemode=!spectator] run return 0
return 1
