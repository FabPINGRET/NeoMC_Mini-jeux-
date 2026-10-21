# Duel sniper — tick (core/tick : au moins un duelliste, ou une invitation en attente)
# invitations : décompte, expiration (30 s), invitation orpheline (défieur parti)
scoreboard players remove @a[scores={mg.dlto=1..,mg.dlx=1..},tag=!mg.dl] mg.dlx 1
execute as @a[scores={mg.dlto=1..,mg.dlx=0},tag=!mg.dl] run function mg:duel/expire
# fenêtre d'invitation remplacée (note de fin de partie) ou invité devenu occupé : voir duel/inv_busy
tag @a[tag=mg.dlui,tag=mg.rate] remove mg.dlui
execute as @a[scores={mg.dlto=1..},tag=!mg.dl] run function mg:duel/inv_busy
execute as @a[tag=mg.dlrq] run function mg:duel/rq_check
# duellistes : la pause reste posée (une partie lancée ne les prend pas), lunette avant les tirs
tag @a[tag=mg.dl] add mg.spectate
execute as @a[tag=mg.dl] at @s run function mg:duel/scope
execute as @a[tag=mg.dlp] run function mg:duel/prot_tick
execute as @a[tag=mg.dl,scores={mg.dlcd=1}] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.6 2
execute as @a[tag=mg.dl,tag=!mg.dlp,scores={mg.dlcd=1}] run title @s actionbar [{"text":"🎯 Sniper prêt","color":"aqua"}]
scoreboard players remove @a[tag=mg.dl,scores={mg.dlcd=1..}] mg.dlcd 1
scoreboard players remove @a[tag=mg.dl,scores={mg.dlkc=1..}] mg.dlkc 1
execute as @a[tag=mg.dl,scores={mg.qs=1..}] run function mg:duel/shoot
# le kit (sniper et couteau) est rendu si un effacement (lancement de partie) ou un jet l'a retiré
execute as @a[tag=mg.dl] unless items entity @s container.* minecraft:warped_fungus_on_a_stick[custom_data~{mg_dl:1b}] run function mg:duel/kit
execute as @a[tag=mg.dl] unless items entity @s container.* *[custom_data~{mg_dl:1b,mg_kn:1b}] run function mg:duel/kit
# sniper et couteau jetés ou ramassés par un autre : retirés
execute as @e[type=minecraft:item,x=-22,y=60,z=39928,dx=44,dy=500,dz=945] if items entity @s contents *[custom_data~{mg_dl:1b}] run kill @s
clear @a[tag=!mg.dl] *[custom_data~{mg_dl:1b}]
# hors de l'arène (chute, mort et réapparition au lobby...) : forfait ; puis adversaire parti
execute as @a[tag=mg.dl,scores={mg.dli=1}] unless entity @s[x=-22,dx=44,y=60,dy=500,z=39928,dz=145] run function mg:duel/forfeit
execute as @a[tag=mg.dl,scores={mg.dli=2}] unless entity @s[x=-22,dx=44,y=60,dy=500,z=40328,dz=145] run function mg:duel/forfeit
execute as @a[tag=mg.dl,scores={mg.dli=3}] unless entity @s[x=-22,dx=44,y=60,dy=500,z=40728,dz=145] run function mg:duel/forfeit
execute if entity @a[tag=mg.dl,scores={mg.dli=1}] run function mg:duel/inst {i:1}
execute if entity @a[tag=mg.dl,scores={mg.dli=2}] run function mg:duel/inst {i:2}
execute if entity @a[tag=mg.dl,scores={mg.dli=3}] run function mg:duel/inst {i:3}
