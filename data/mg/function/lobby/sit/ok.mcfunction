# @s : peut être assis / faire une emote ici ? Retourne 1 ou 0, sans message (sit/tick s'en sert pour relever)
# core/opt tourne sans « at @s » : la dimension se lit à la position du joueur
execute at @s unless dimension minecraft:overworld run return 0
execute if score $sitoff mg.st matches 1 run return 0
execute unless entity @s[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.pkr,tag=!mg.lk,tag=!mg.ely,tag=!mg.elyf,tag=!mg.xso,tag=!mg.dl,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.mpp,tag=!mg.pvpc,tag=!mg.thbun,tag=!mg.thmini,gamemode=!spectator] run return 0
execute if entity @s[x=-12,y=40,z=-10,dx=51,dy=20,dz=45] run return 0
execute if entity @s[x=-17,y=46,z=-41,dx=38,dy=17,dz=27] run return 0
return 1
