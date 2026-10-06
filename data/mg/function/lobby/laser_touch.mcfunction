# Joueur touché par le laser (@s = joueur touché) : pour rire, aucun dégât
effect give @s minecraft:glowing 3 0 true
particle minecraft:happy_villager ~ ~1 ~ 0.3 0.5 0.3 0.05 12
playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 1 1.3
title @s actionbar [{"text":"⚡ Touché par un laser !","color":"red"}]
