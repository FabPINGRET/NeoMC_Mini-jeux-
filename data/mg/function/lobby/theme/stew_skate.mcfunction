# 🎃 Ragoût (patinoire : friction -100 %, traînée de l'air -40 %, vitesse -30 %, 25 s, objectif mg.ths) ; @s = joueur
execute if entity @s[tag=mg.thmini] at @s unless block ~ ~1 ~ #minecraft:replaceable run return run function mg:lobby/theme/stew_fizzle
function mg:lobby/theme/stew_clear
attribute @s minecraft:friction_modifier modifier add mg:thstew -1.0 add_multiplied_base
attribute @s minecraft:air_drag_modifier modifier add mg:thstew -0.4 add_multiplied_base
attribute @s minecraft:movement_speed modifier add mg:thstew -0.3 add_multiplied_base
scoreboard players set @s mg.ths 25
execute at @s run playsound minecraft:entity.player.hurt_freeze neutral @a[distance=..16] ~ ~ ~ 1 1
title @s actionbar {"text":"⛸ Patinoire : ça glisse ! (25 s)","color":"aqua"}
