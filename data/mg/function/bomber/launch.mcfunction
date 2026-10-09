# @s : posé au sol et accroupi → catapulté vers le ciel pour rouvrir les élytres
effect give @s minecraft:levitation 1 40 true
particle minecraft:gust ~ ~0.5 ~ 0.3 0.1 0.3 0 3
playsound minecraft:entity.wind_charge.wind_burst player @a ~ ~ ~ 1 0.8
title @s actionbar {"text":"🪽 Appuie sur Espace en l'air pour rouvrir tes élytres","color":"aqua"}
