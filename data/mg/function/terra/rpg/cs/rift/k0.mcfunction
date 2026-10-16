# image 0 (tick 0)
title @s title {"text":"LA FAILLE SE REFERME","color":"gold","bold":true}
title @s subtitle ""
execute at @s run playsound minecraft:block.end_portal.spawn master @s ~ ~ ~ 1 1
particle minecraft:reverse_portal 0.5 102 177 1 2 0.3 0.3 400 force @s
