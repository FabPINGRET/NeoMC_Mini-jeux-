# Mouton glacé : joueurs à moins de 5 blocs bloqués sur place 3 s
effect give @a[tag=mg.play,distance=..5] minecraft:slowness 3 255 true
title @a[tag=mg.play,distance=..5] actionbar [{"text":"❄ Tu es gelé sur place !","color":"aqua"}]
particle minecraft:snowflake ~ ~1 ~ 2 1 2 0.05 120
playsound minecraft:block.glass.break master @a ~ ~ ~ 1.2 0.8
kill @s
