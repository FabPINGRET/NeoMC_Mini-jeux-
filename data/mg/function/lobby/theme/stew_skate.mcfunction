# 🎃 Ragoût (patinoire : friction -90 %, 25 s, objectif mg.ths) ; @s = joueur
execute if entity @s[tag=mg.thmini] at @s unless block ~ ~1 ~ #minecraft:replaceable run return run function mg:lobby/theme/stew_burp
function mg:lobby/theme/stew_clear
attribute @s minecraft:friction_modifier modifier add mg:thstew -0.9 add_multiplied_base
scoreboard players set @s mg.ths 25
execute at @s run playsound minecraft:entity.player.hurt_freeze neutral @a[distance=..16] ~ ~ ~ 1 1
title @s actionbar {"text":"⛸ Patinoire : ça glisse ! (25 s)","color":"aqua"}
