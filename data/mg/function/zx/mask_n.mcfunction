# @s : masque n° $(n) sur la tête, jamais lâché
$item replace entity @s armor.head with minecraft:paper[item_model="mg:zm/mask_$(n)"]
data modify entity @s drop_chances.head set value 0f
tag @s add mg.zmk
