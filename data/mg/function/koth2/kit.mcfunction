# @s : kit (épée en pierre, bâton de recul, armure en cuir à la couleur de l'équipe)
clear @s
give @s minecraft:stone_sword[unbreakable={}]
give @s minecraft:stick[enchantments={knockback:2},custom_name=[{"text":"Bâton de recul","color":"gold","italic":false}]]
give @s minecraft:golden_apple 1
execute if entity @s[team=mg_red] run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16711680,unbreakable={}]
execute if entity @s[team=mg_blue] run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=255,unbreakable={}]
execute unless entity @s[team=mg_red] unless entity @s[team=mg_blue] run item replace entity @s armor.chest with minecraft:leather_chestplate[unbreakable={}]
item replace entity @s armor.feet with minecraft:leather_boots[unbreakable={}]
effect give @s minecraft:saturation infinite 0 true
