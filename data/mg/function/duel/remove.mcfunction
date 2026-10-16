# Duel sniper : désinstallation (à appeler depuis mg:desinstaller)
execute as @a[tag=mg.dl] run function mg:duel/stop
kill @e[type=minecraft:marker,tag=mg.dlend]
function mg:duel/build_clear
data remove storage mg:duel built
data remove storage mg:duel m
tag @a remove mg.dla
tag @a remove mg.dlp
tag @a remove mg.dlsc
tag @a remove mg.dlsh
tag @a remove mg.dlvc
tag @a remove mg.dlwn
tag @a remove mg.dlsp
tag @a remove mg.dlrq
tag @a remove mg.dlca
tag @a remove mg.dltg
tag @a remove mg.dlt2
tag @a remove mg.dlq
tag @a remove mg.dlfl
tag @a remove mg.dlpz
scoreboard objectives remove mg.duel
scoreboard objectives remove mg.dlid
scoreboard objectives remove mg.dlto
scoreboard objectives remove mg.dlx
scoreboard objectives remove mg.dli
scoreboard objectives remove mg.dlhp
scoreboard objectives remove mg.dlr
scoreboard objectives remove mg.dlcd
scoreboard objectives remove mg.dlw
# objectif d'une version de développement antérieure (absent d'un monde neuf : sans effet)
scoreboard objectives remove mg.dlsp0
