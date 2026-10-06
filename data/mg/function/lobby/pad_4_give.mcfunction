title @s actionbar [{"text":"❄ Lance-neige chargé !","color":"green"}]
execute at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.2
clear @s minecraft:snowball
item replace entity @s hotbar.3 with minecraft:snowball[custom_name=[{"text":"❄ Lance-neige","color":"white","bold":true,"italic":false}],lore=[{"text":"Clic droit : boule de neige (1 cœur, jamais mortel)","color":"gray","italic":false}]] 16
