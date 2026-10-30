# Élytres rendues sur le socle (@s)
function mg:elytra/free_stop
execute at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 0.8 0.8
title @s actionbar [{"text":"Élytres rendues.","color":"gray"}]
