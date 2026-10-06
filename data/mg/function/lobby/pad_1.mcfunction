# Socle 1 (@s = joueur sur le socle) : pistolet laser
execute store result score $apc mg.st run clear @s minecraft:warped_fungus_on_a_stick 0
execute if score $apc mg.st matches 0 run function mg:lobby/pad_1_give
