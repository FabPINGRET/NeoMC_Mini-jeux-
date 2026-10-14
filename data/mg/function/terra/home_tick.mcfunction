# @s attend son rappel (5 s) : un coup reçu annule
execute if score @s mg.tvdt matches 1.. run scoreboard players set @s mg.tvhm 0
execute if score @s mg.tvdt matches 1.. run return run title @s actionbar {"text":"✖ Rappel annulé : tu as pris un coup !","color":"red","bold":true}
scoreboard players remove @s mg.tvhm 1
scoreboard players operation $tvs mg.st = @s mg.tvhm
scoreboard players add $tvs mg.st 19
scoreboard players set #20 mg.st 20
scoreboard players operation $tvs mg.st /= #20 mg.st
title @s actionbar [{"text":"📡 Rappel à la colonie dans ","color":"green"},{"score":{"name":"$tvs","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"green"}]
execute if score @s mg.tvhm matches 0 run function mg:terra/home_go
