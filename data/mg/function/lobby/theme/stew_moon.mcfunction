# 🎃 Ragoût (marche lunaire : gravité -75 %, saut +30 %, 20 s, objectif mg.ths) ; @s = joueur
execute if entity @s[tag=mg.thmini] at @s unless block ~ ~1 ~ #minecraft:replaceable run return run function mg:lobby/theme/stew_burp
function mg:lobby/theme/stew_clear
attribute @s minecraft:gravity modifier add mg:thstew -0.75 add_multiplied_base
attribute @s minecraft:jump_strength modifier add mg:thstew 0.3 add_multiplied_base
scoreboard players set @s mg.ths 20
execute at @s run playsound minecraft:entity.enderman.teleport neutral @a[distance=..16] ~ ~ ~ 1 0.6
title @s actionbar {"text":"🌙 Marche lunaire !","color":"aqua"}
