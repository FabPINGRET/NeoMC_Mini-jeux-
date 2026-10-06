# Raté (@s = joueur posé sur un obstacle ou au sol) : retour en haut
execute at @s run particle minecraft:poof ~ ~0.2 ~ 0.3 0.2 0.3 0.05 15
execute at @s run playsound minecraft:entity.villager.no master @a ~ ~ ~ 0.8 1
title @s actionbar [{"text":"✖ Raté ! Retour en haut...","color":"red"}]
function mg:dropper/to_top
