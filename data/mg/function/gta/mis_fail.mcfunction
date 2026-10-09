# @s : mission échouée ou abandonnée
execute unless score @s mg.gmt matches 1.. run return 0
function mg:gta/mis_clean
title @s times 5 40 15
title @s title {"text":"MISSION ÉCHOUÉE","color":"red","bold":true}
execute at @s run playsound minecraft:entity.villager.no player @s ~ ~ ~ 1 0.8
scoreboard players set @s mg.gtl 60
