# Fin de la Mini Party (résultats affichés, arrêt manuel du plateau, ou plus de participants)
scoreboard players set $mp mg.st 0
tag @a remove mg.mpp
tag @a remove mg.mpa
tag @a remove mg.mpcur
tag @a remove mg.mpsw
tag @a remove mg.mpview
scoreboard players reset * mg.mpv
kill @e[type=minecraft:text_display,tag=mg.mpdice]
kill @e[type=minecraft:text_display,tag=mg.mpstar]
clear @a minecraft:echo_shard
team empty mg_party
