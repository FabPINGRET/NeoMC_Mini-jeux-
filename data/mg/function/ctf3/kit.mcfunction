# @s : kit
clear @s
give @s minecraft:stone_sword[unbreakable={}]
give @s minecraft:bow[unbreakable={}]
give @s minecraft:arrow 16
give @s minecraft:cooked_beef 16
execute if entity @s[team=mg_red] run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16711680,unbreakable={}]
execute if entity @s[team=mg_blue] run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=255,unbreakable={}]
execute if entity @s[team=mg_red] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=16711680,unbreakable={}]
execute if entity @s[team=mg_blue] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=255,unbreakable={}]
item replace entity @s armor.legs with minecraft:leather_leggings[unbreakable={}]
item replace entity @s armor.feet with minecraft:leather_boots[unbreakable={}]
