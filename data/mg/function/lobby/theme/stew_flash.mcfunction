# 🎃 Ragoût (flash : vitesse +80 %, pas +0,85, 20 s, objectif mg.ths) ; @s = joueur
execute if entity @s[tag=mg.thmini] at @s unless block ~ ~1 ~ #minecraft:replaceable run return run function mg:lobby/theme/stew_burp
function mg:lobby/theme/stew_clear
attribute @s minecraft:movement_speed modifier add mg:thstew 0.8 add_multiplied_base
attribute @s minecraft:step_height modifier add mg:thstew 0.85 add_multiplied_base
tag @s add mg.thzap
scoreboard players set @s mg.ths 20
execute at @s run playsound minecraft:entity.breeze.wind_burst neutral @a[distance=..16] ~ ~ ~ 1 1.2
title @s actionbar {"text":"⚡ Flash : super vitesse ! (20 s)","color":"yellow"}
