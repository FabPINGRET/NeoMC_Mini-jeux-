title @s actionbar [{"text":"☁ Lance-vent chargé !","color":"green"}]
execute at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.2
clear @s minecraft:wind_charge
item replace entity @s hotbar.2 with minecraft:wind_charge[custom_name=[{"text":"☁ Lance-vent","color":"aqua","bold":true,"italic":false}],lore=[{"text":"Clic droit : rafale de vent (sans danger)","color":"gray","italic":false}]] 16
