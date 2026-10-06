# Socle 3 (@s = joueur sur le socle) : lance-vent, recharge à 16
execute store result score $apc mg.st run clear @s minecraft:wind_charge 0
execute if score $apc mg.st matches ..15 run function mg:lobby/pad_3_give
