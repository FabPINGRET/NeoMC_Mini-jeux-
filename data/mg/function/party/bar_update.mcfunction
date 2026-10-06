# Barre du haut : tour, joueur actif, progression de la partie
bossbar add mg:party ""
bossbar set mg:party color yellow
bossbar set mg:party style notched_10
execute store result bossbar mg:party max run scoreboard players get $mpmax mg.st
execute store result bossbar mg:party value run scoreboard players get $mpround mg.st
bossbar set mg:party name [{"text":"★ MINI PARTY  ·  Tour ","color":"gold","bold":true},{"score":{"name":"$mpround","objective":"mg.st"},"color":"white"},{"text":"/","color":"gold"},{"score":{"name":"$mpmax","objective":"mg.st"},"color":"white"},{"text":"  ·  ","color":"gray"},{"selector":"@a[tag=mg.mpcur]","color":"yellow"},{"text":"  ·  menu : Actions rapides","color":"gray","bold":false}]
bossbar set mg:party players @a[tag=mg.mpp]
bossbar set mg:party visible true
