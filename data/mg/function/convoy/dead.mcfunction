# @s vient de mourir (ou de tomber) : spectateur au-dessus du convoi pendant 5 s
scoreboard players set @s mg.deaths 0
tag @s add mg.cvw
scoreboard players set @s mg.cvrt 100
gamemode spectator @s
execute at @e[type=minecraft:block_display,tag=mg.cvc,limit=1] run tp @s ~ 92 ~6 facing entity @e[type=minecraft:block_display,tag=mg.cvc,limit=1]
title @s times 0 25 5
title @s title {"text":"☠ Éliminé","color":"red","bold":true}
