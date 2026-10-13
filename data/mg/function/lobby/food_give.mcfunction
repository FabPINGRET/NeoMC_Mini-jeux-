# Buffet gratuit (@s = joueur sur le bloc d'or) : nourriture, petite recharge
execute if score @s mg.fd matches 1.. run return 0
execute if score $theme mg.st matches 1 run function mg:lobby/food_halloween
execute if score $theme mg.st matches 2 run function mg:lobby/food_noel
execute unless score $theme mg.st matches 1..2 run give @s minecraft:cooked_beef 3
execute unless score $theme mg.st matches 1..2 run give @s minecraft:golden_carrot 2
scoreboard players set @s mg.fd 600
execute at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 0.8 1.2
execute unless score $theme mg.st matches 1..2 run title @s actionbar [{"text":"🍖 Bon appétit ! (recharge dans 30 s)","color":"gold"}]
