title @s actionbar [{"text":"☁ Lance-vent chargé !","color":"green"}]
execute at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.2
clear @s minecraft:wind_charge
item replace entity @s hotbar.2 with minecraft:wind_charge[custom_name=[{"text":"☁ Lance-vent","color":"aqua","bold":true,"italic":false}],lore=[{"text":"Clic droit : rafale de vent (sans danger)","color":"gray","italic":false}]] 16
execute if score $rp mg.st matches 1 run item modify entity @s hotbar.2 {"function":"minecraft:set_components","components":{"minecraft:item_model":"mg:wind_orb"}}
