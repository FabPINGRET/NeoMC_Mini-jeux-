# @s monte dans un wagonnet (départ immédiat vers l'ouest)
summon minecraft:minecart -118.5 64 0.5 {Tags:["mg.cst","mg.csn"],Motion:[-0.4d,0d,0d]}
ride @s mount @e[type=minecraft:minecart,tag=mg.csn,limit=1]
tag @e[tag=mg.csn] remove mg.csn
playsound minecraft:entity.minecart.riding master @s ~ ~ ~ 0.6 1.2
title @s actionbar {"text":"🎢 Accroche-toi !","color":"gold"}
