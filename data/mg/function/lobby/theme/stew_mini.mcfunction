# 🎃 Ragoût (mini-moi : taille -70 %, 45 s, objectif mg.ths) ; @s = joueur
execute if entity @s[tag=mg.thmini] at @s unless block ~ ~1 ~ #minecraft:replaceable run return run function mg:lobby/theme/stew_fizzle
function mg:lobby/theme/stew_clear
attribute @s minecraft:scale modifier add mg:thstew -0.7 add_multiplied_base
tag @s add mg.thmini
scoreboard players set @s mg.ths 45
execute at @s run playsound minecraft:entity.allay.item_given neutral @a[distance=..16] ~ ~ ~ 1 2
title @s actionbar {"text":"🍄 Mini-moi : tu rétrécis ! (45 s)","color":"light_purple"}
