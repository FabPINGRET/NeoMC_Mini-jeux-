# Socle 4 (@s = joueur sur le socle) : lance-neige, recharge à 16
execute store result score $apc mg.st run clear @s minecraft:snowball 0
execute if score $apc mg.st matches ..15 run function mg:lobby/pad_4_give
