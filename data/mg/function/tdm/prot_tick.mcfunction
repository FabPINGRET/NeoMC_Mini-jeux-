# Réapparition protégée (@s = joueur mg.tmp ; mg.tmx = décompte en ticks)
scoreboard players remove @s mg.tmx 1
execute if score @s mg.tmx matches 40 run title @s actionbar [{"text":"2","color":"yellow","bold":true}]
execute if score @s mg.tmx matches 20 run title @s actionbar [{"text":"1","color":"yellow","bold":true}]
execute if score @s mg.tmx matches ..0 run title @s actionbar [{"text":"🎯 FEU !","color":"red","bold":true}]
execute if score @s mg.tmx matches ..0 at @s run playsound minecraft:entity.firework_rocket.blast master @s ~ ~ ~ 0.6 1.4
execute if score @s mg.tmx matches ..0 run tag @s remove mg.tmp
execute if score @s mg.tmx matches ..0 run scoreboard players reset @s mg.tmx
