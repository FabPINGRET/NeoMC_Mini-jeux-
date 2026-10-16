# Manche en préparation (@s = duelliste mg.dlp ; mg.dlx = décompte en ticks)
scoreboard players remove @s mg.dlx 1
execute if score @s mg.dlx matches 40 run title @s actionbar [{"text":"2","color":"yellow","bold":true}]
execute if score @s mg.dlx matches 20 run title @s actionbar [{"text":"1","color":"yellow","bold":true}]
execute if score @s mg.dlx matches ..0 run title @s actionbar [{"text":"⚔ FEU !","color":"red","bold":true}]
execute if score @s mg.dlx matches ..0 at @s run playsound minecraft:entity.firework_rocket.blast master @s ~ ~ ~ 0.6 1.4
execute if score @s mg.dlx matches ..0 run tag @s remove mg.dlp
execute if score @s mg.dlx matches ..0 run scoreboard players reset @s mg.dlx
