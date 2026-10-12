# @s (cacheur) : bruit volontaire, recharge 3 s
execute if score @s mg.phcd matches 1.. run return run title @s actionbar {"text":"📯 Corne en recharge…","color":"gray"}
scoreboard players set @s mg.phcd 60
function mg:ph/taunt_one
playsound minecraft:item.goat_horn.sound.0 player @a ~ ~ ~ 1.5 1.2
title @s actionbar {"text":"📯 Tu as fait du bruit !","color":"gold"}
