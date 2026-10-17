# 🎃 Ragoût (lapin : taille -65 %, saut +30 %, vitesse +20 %, vrai lapin figé, 40 s, objectif mg.ths) ; @s = joueur
execute if entity @s[tag=mg.thmini] at @s unless block ~ ~1 ~ #minecraft:replaceable run return run function mg:lobby/theme/stew_fizzle
function mg:lobby/theme/stew_clear
attribute @s minecraft:scale modifier add mg:thstew -0.65 add_multiplied_base
attribute @s minecraft:jump_strength modifier add mg:thstew 0.3 add_multiplied_base
attribute @s minecraft:movement_speed modifier add mg:thstew 0.2 add_multiplied_base
tag @s add mg.thmini
tag @s add mg.thbun
effect give @s minecraft:invisibility 3 0 true
execute at @s run particle minecraft:poof ~ ~0.4 ~ 0.3 0.3 0.3 0.02 12 normal
function mg:lobby/theme/stew_rabbit_body
scoreboard players set @s mg.ths 40
execute at @s run playsound minecraft:entity.rabbit.jump neutral @a[distance=..16] ~ ~ ~ 1 1.2
title @s actionbar {"text":"🐰 Tu es un lapin ! (40 s)","color":"gold"}
