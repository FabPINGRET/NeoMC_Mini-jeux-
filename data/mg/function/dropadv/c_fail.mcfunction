execute if score @s mg.cd matches 1.. run return 0
execute at @s run particle minecraft:poof ~ ~0.2 ~ 0.3 0.2 0.3 0.05 15
execute at @s run playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.8 1
title @s actionbar [{"text":"✖ Raté ! Retour en haut...","color":"red"}]
function mg:dropadv/c_spawn
