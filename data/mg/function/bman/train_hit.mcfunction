# Entraînement : renvoyé au départ
execute if score @s mg.yh matches 1.. run return 0
scoreboard players set @s mg.yh 30
scoreboard players add @s mg.ym 1
tp @s -9.5 65 40691.5
title @s actionbar {"text":"💥 Touché ! (entraînement : retour au départ)","color":"red"}
playsound minecraft:entity.player.hurt master @s ~ ~ ~ 1 0.8
