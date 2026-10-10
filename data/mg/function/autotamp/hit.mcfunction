# @s (joueur) vient d'être tamponné
scoreboard players remove @s mg.atl 1
title @s actionbar [{"text":"💢 On t'a tamponné ! Coups restants : ","color":"red"},{"score":{"name":"@s","objective":"mg.atl"},"color":"yellow","bold":true}]
execute if score @s mg.atl matches ..0 run function mg:autotamp/out
