# @s attend son retour (5 s) : un coup reçu annule
execute if score @s mg.pdt matches 1.. run scoreboard players set @s mg.phc 0
execute if score @s mg.pdt matches 1.. run return run title @s actionbar {"text":"✖ Retour annulé : tu as pris un coup !","color":"red","bold":true}
scoreboard players remove @s mg.phc 1
scoreboard players operation $s mg.st = @s mg.phc
scoreboard players add $s mg.st 19
scoreboard players set #20 mg.st 20
scoreboard players operation $s mg.st /= #20 mg.st
title @s actionbar [{"text":"🏠 Retour au spawn dans ","color":"yellow"},{"score":{"name":"$s","objective":"mg.st"},"color":"gold","bold":true},{"text":" s","color":"yellow"}]
execute if score @s mg.phc matches 0 run function mg:pvpc/leave
