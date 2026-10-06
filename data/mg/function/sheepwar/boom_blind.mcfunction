# Mouton des ténèbres : cécité 6 s aux joueurs à moins de 8 blocs
effect give @a[tag=mg.play,distance=..8] minecraft:blindness 6 0 true
title @a[tag=mg.play,distance=..8] actionbar [{"text":"☁ Tu n'y vois plus rien !","color":"gray"}]
particle minecraft:squid_ink ~ ~1 ~ 2 1 2 0.1 80
playsound minecraft:entity.sheep.death master @a ~ ~ ~ 1.2 0.5
kill @s
