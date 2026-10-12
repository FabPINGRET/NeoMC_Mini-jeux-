# @s (innocent) : compte ses pièces d'or
execute store result score @s mg.mmo run clear @s minecraft:gold_ingot 0
execute if score @s mg.mmo matches 10.. run function mg:mm/gold_bow
