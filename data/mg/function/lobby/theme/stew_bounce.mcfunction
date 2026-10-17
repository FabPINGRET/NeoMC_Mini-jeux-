# 🎃 Ragoût (rebond : bounciness +0,8, saut +20 %, 30 s, objectif mg.ths) ; @s = joueur
execute if entity @s[tag=mg.thmini] at @s unless block ~ ~1 ~ #minecraft:replaceable run return run function mg:lobby/theme/stew_fizzle
function mg:lobby/theme/stew_clear
attribute @s minecraft:bounciness modifier add mg:thstew 0.8 add_value
attribute @s minecraft:jump_strength modifier add mg:thstew 0.2 add_multiplied_base
scoreboard players set @s mg.ths 30
execute at @s run playsound minecraft:entity.slime.jump neutral @a[distance=..16] ~ ~ ~ 1 1
title @s actionbar {"text":"🏀 Tu rebondis ! (30 s)","color":"gold"}
