# Mode 3 : la plateforme de décollage s'effondre
fill -8 195 28992 8 198 29008 minecraft:air
particle minecraft:cloud 0 195 29000 4 0.5 4 0.05 120 force @a
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.glass.break master @s ~ ~ ~ 1 0.7
scoreboard players set $skpo mg.st 0
title @a[tag=mg.play] actionbar [{"text":"La plateforme s'est effondrée : reste en l'air !","color":"red"}]
