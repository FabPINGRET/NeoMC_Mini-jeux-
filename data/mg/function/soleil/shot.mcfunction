# @s a bougé : tir
execute at @s run particle minecraft:dust{color:[0.8,0.0,0.0],scale:2.0} ~ ~1 ~ 0.3 0.6 0.3 0 40 force
execute at @s run particle minecraft:explosion ~ ~1 ~ 0 0 0 0 1 force
execute as @a[tag=!mg.surv] at @s if entity @s[x=-30,y=40,z=36990,dx=60,dy=60,dz=120] run playsound minecraft:entity.firework_rocket.blast master @s ~ ~ ~ 1 0.5
tellraw @a[tag=!mg.surv] [{"text":"💥 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" a bougé !","color":"red"}]
scoreboard players add $sqe mg.st 1
execute if score $n0 mg.st matches 2.. run return run function mg:core/eliminate
function mg:soleil/place
function mg:soleil/mark
title @s actionbar {"text":"💥 Tu as bougé : retour au départ (entraînement)","color":"red"}
