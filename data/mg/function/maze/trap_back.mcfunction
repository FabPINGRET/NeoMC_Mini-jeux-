spreadplayers -53.5 41100 0.5 2 under 67 false @s
title @s title {"text":"↩ Retour au départ !","color":"red","bold":true}
tellraw @a[tag=mg.play] [{"text":"🌀 ","color":"light_purple"},{"selector":"@s","color":"yellow"},{"text":" est tombé dans un piège : retour au départ !","color":"gray"}]
playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 0.6
