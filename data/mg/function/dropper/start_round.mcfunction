# Ouvre le trou du sol de départ : manche en cours (les joueurs sautent eux-mêmes)
function mg:dropper/open_floors
scoreboard players set $dph mg.st 1
scoreboard players set @a[tag=mg.play] mg.cd 10
title @a[tag=mg.play] title [{"text":"⬇ MANCHE ","color":"aqua","bold":true},{"score":{"name":"$rd","objective":"mg.st"},"color":"aqua","bold":true}]
title @a[tag=mg.play] subtitle [{"text":"Saute dans le trou et atterris dans l'eau !","color":"gray"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.piston.extend master @s ~ ~ ~ 1 1.2
