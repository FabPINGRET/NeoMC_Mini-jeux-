# @s (en équipe) marche sur le socle blanc : quitte son équipe
function mg:foot/cleanup
title @s actionbar {"text":"✖ Tu as quitté ton équipe","color":"gray"}
execute at @s run playsound minecraft:block.note_block.bass master @s ~ ~ ~ 1 0.8
