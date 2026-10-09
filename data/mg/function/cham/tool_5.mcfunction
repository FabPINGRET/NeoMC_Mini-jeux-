# Narguer : sifflet fort, +5 points (recharge 8 s)
execute if score @s mg.cmtc matches 1.. run return run title @s actionbar [{"text":"📢 Recharge : ","color":"gray"},{"score":{"name":"@s","objective":"mg.cmtc"},"color":"white"},{"text":" ticks","color":"gray"}]
scoreboard players set @s mg.cmtc 160
scoreboard players add @s mg.cmpts 5
execute at @s run playsound minecraft:entity.parrot.ambient player @a ~ ~ ~ 2 1.6
execute at @s run playsound minecraft:block.note_block.flute player @a ~ ~ ~ 2 2
execute at @s run particle minecraft:note ~ ~1.5 ~ 0.3 0.3 0.3 1 6
title @s actionbar {"text":"📢 Tu nargues les chasseurs : +5 points","color":"gold"}
