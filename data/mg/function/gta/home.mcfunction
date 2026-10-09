# @s : retour à la villa (Neo Hills), refusé si la police le recherche
scoreboard players reset @s mg.gqs
execute if score @s mg.gwl matches 1.. run return run title @s actionbar {"text":"🚔 Impossible : la police te recherche !","color":"red"}
execute on vehicle run return 0
execute in mg:gta run tp @s 20.5 71 32297.5 180 0
execute in mg:gta run spawnpoint @s 20 71 32297
execute at @s run playsound minecraft:block.portal.travel player @s ~ ~ ~ 0.2 2
title @s actionbar {"text":"🏠 Neo Hills","color":"aqua","bold":true}
