# @s (objet au sol) : minerais → lingots
execute if items entity @s contents minecraft:raw_iron run data modify entity @s Item.id set value "minecraft:iron_ingot"
execute if items entity @s contents minecraft:raw_gold run data modify entity @s Item.id set value "minecraft:gold_ingot"
execute if items entity @s contents minecraft:raw_copper run data modify entity @s Item.id set value "minecraft:copper_ingot"
