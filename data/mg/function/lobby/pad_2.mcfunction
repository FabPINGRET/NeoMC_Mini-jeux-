# Socle 2 (@s = joueur sur le socle) : baguette feu d'artifice
execute store result score $apc mg.st run clear @s minecraft:blaze_rod 0
execute if score $apc mg.st matches 0 run function mg:lobby/pad_2_give
