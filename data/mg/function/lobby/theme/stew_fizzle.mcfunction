# 🎃 Ragoût : pschitt, instantané (@s = joueur) ; repli du coup de vent refusé et du ragoût chronométré sans place (aucun attribut touché, pas de stew_clear)
execute at @s run playsound minecraft:entity.witch.celebrate neutral @a[distance=..16] ~ ~ ~ 1 1.4
execute at @s run particle minecraft:smoke ~ ~1 ~ 0.3 0.3 0.3 0.02 10 normal
execute at @s run particle minecraft:poof ~ ~1 ~ 0.3 0.3 0.3 0.02 6 normal
title @s actionbar {"text":"🫧 Le ragoût fait pschitt… rien ne se passe","color":"gray"}
