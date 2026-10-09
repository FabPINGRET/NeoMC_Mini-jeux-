# @s attend sa réapparition (compte à rebours dans la barre d'action)
scoreboard players remove @s mg.cvrt 1
execute if score @s mg.cvrt matches ..0 run return run function mg:convoy/respawn
scoreboard players operation $cvs mg.st = @s mg.cvrt
scoreboard players add $cvs mg.st 19
scoreboard players set #20 mg.st 20
scoreboard players operation $cvs mg.st /= #20 mg.st
title @s actionbar [{"text":"Réapparition dans ","color":"gray"},{"score":{"name":"$cvs","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"gray"}]
