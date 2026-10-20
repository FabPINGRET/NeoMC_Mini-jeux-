# Fin de duel pour @s (fin normale, forfait, reconnexion, désinstallation) : état effacé, retour au lobby
tag @s remove mg.dl
tag @s remove mg.dla
tag @s remove mg.dlp
tag @s remove mg.dlsc
tag @s remove mg.dlsp
execute unless entity @s[tag=mg.dlpz] run tag @s remove mg.spectate
tag @s remove mg.dlpz
scoreboard players reset @s mg.dli
scoreboard players reset @s mg.dlhp
scoreboard players reset @s mg.dlr
scoreboard players reset @s mg.dlcd
scoreboard players reset @s mg.dlx
scoreboard players reset @s mg.dlkc
title @s reset
execute as @e[type=minecraft:item,x=-22,y=60,z=39928,dx=44,dy=500,dz=945] if items entity @s contents *[custom_data~{mg_dl:1b}] run kill @s
clear @s *[custom_data~{mg_dl:1b}]
# effets du duel (setup) retirés sauf si une partie a pris le joueur (ses effets sont les siens ; ailleurs, enter / reset_player les effacent)
execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.out] run effect clear @s minecraft:resistance
execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.out] run effect clear @s minecraft:saturation
# retour au lobby, sauf si une activité l'a pris entre-temps (reset_player y arracherait la survie, le plot... : garde de elyrace/solo/stop)
execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.out] unless entity @s[tag=mg.surv] unless entity @s[tag=mg.inplot] unless entity @s[tag=mg.visit] unless entity @s[tag=mg.gtw] unless entity @s[tag=mg.tvw] run function mg:core/reset_player
