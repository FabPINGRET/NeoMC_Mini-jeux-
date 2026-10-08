# @s : kit (blocs de l'équipe pour construire, épée, arc, pioche)
clear @s
give @s minecraft:stone_sword[unbreakable={}]
give @s minecraft:bow[unbreakable={}]
give @s minecraft:stone_pickaxe[unbreakable={}]
give @s minecraft:arrow 16
execute if entity @s[team=mg_red] run give @s minecraft:red_terracotta 64
execute if entity @s[team=mg_blue] run give @s minecraft:blue_terracotta 64
give @s minecraft:golden_apple 1
execute if entity @s[team=mg_red] run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16711680,unbreakable={}]
execute if entity @s[team=mg_blue] run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=255,unbreakable={}]
execute if entity @s[team=mg_red] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=16711680,unbreakable={}]
execute if entity @s[team=mg_blue] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=255,unbreakable={}]
item replace entity @s armor.legs with minecraft:chainmail_leggings[unbreakable={}]
item replace entity @s armor.feet with minecraft:leather_boots[unbreakable={}]
effect give @s minecraft:saturation infinite 0 true
