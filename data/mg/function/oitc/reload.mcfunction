# Flèche de recharge (@s = joueur)
scoreboard players set @s mg.cd 0
give @s minecraft:arrow[custom_name=[{"text":"Flèche","color":"yellow","italic":false}]] 1
title @s actionbar [{"text":"➶ Flèche rechargée !","color":"green","bold":true}]
execute at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.3
