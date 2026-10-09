# @s monte dans un wagonnet, en haut de la voie (départ immédiat vers le nord)
tp @s -63.5 86 30.5 180 10
summon minecraft:minecart -63.5 86 30.5 {Tags:["mg.cst","mg.csn"],Motion:[0d,0d,-0.4d]}
ride @s mount @e[type=minecraft:minecart,tag=mg.csn,limit=1]
tag @e[tag=mg.csn] remove mg.csn
playsound minecraft:entity.minecart.riding master @s ~ ~ ~ 0.6 1.2
title @s actionbar {"text":"🎢 Accroche-toi !","color":"gold"}
