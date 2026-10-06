# Mouton nauséeux : nausée 10 s aux joueurs à moins de 6 blocs
effect give @a[tag=mg.play,distance=..6] minecraft:nausea 10 0 true
title @a[tag=mg.play,distance=..6] actionbar [{"text":"☣ Tu as la nausée !","color":"green"}]
particle minecraft:happy_villager ~ ~1 ~ 2 1 2 0.1 80
playsound minecraft:entity.sheep.death master @a ~ ~ ~ 1.2 0.6
kill @s
