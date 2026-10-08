# @s : kit
clear @s
give @s minecraft:iron_sword[unbreakable={}]
give @s minecraft:bow[unbreakable={}]
give @s minecraft:arrow 32
give @s minecraft:cooked_beef 16
item replace entity @s weapon.offhand with minecraft:shield[unbreakable={}]
item replace entity @s armor.chest with minecraft:iron_chestplate[unbreakable={}]
item replace entity @s armor.feet with minecraft:iron_boots[unbreakable={}]
execute if entity @s[team=mg_red] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=16711680,unbreakable={}]
execute if entity @s[team=mg_blue] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=255,unbreakable={}]
execute if entity @s[team=mg_green] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=65280,unbreakable={}]
item replace entity @s armor.legs with minecraft:chainmail_leggings[unbreakable={}]
