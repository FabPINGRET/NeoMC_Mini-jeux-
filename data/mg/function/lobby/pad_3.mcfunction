# Socle 3 (@s = joueur sur le socle) : recharge à 16
execute unless items entity @s hotbar.* minecraft:wind_charge run title @s actionbar [{"text":"☁ Lance-vent chargé !","color":"green"}]
execute unless items entity @s hotbar.* minecraft:wind_charge at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.2
execute unless items entity @s hotbar.2 minecraft:wind_charge[count=16..] run item replace entity @s hotbar.2 with minecraft:wind_charge[custom_name=[{"text":"☁ Lance-vent","color":"aqua","bold":true,"italic":false}],lore=[{"text":"Clic droit : rafale de vent (sans danger)","color":"gray","italic":false}]] 16
