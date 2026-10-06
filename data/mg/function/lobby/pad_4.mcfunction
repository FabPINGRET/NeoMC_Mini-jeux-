# Socle 4 (@s = joueur sur le socle) : recharge à 16
execute unless items entity @s hotbar.* minecraft:snowball run title @s actionbar [{"text":"❄ Lance-neige chargé !","color":"green"}]
execute unless items entity @s hotbar.* minecraft:snowball at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.2
execute unless items entity @s hotbar.3 minecraft:snowball[count=16..] run item replace entity @s hotbar.3 with minecraft:snowball[custom_name=[{"text":"❄ Lance-neige","color":"white","bold":true,"italic":false}],lore=[{"text":"Clic droit : boule de neige inoffensive","color":"gray","italic":false}]] 16
