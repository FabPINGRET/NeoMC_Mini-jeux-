# ULTRA HARD — joueurs boostés (@s = joueur) : armure en diamant enchantée, épée et arc enchantés, effets permanents
clear @s minecraft:iron_sword
clear @s minecraft:bow
give @s minecraft:diamond_sword[unbreakable={},enchantments={sharpness:3,unbreaking:3}]
give @s minecraft:bow[unbreakable={},enchantments={power:3,infinity:1,unbreaking:3}]
item replace entity @s armor.head with minecraft:diamond_helmet[unbreakable={},enchantments={protection:3,unbreaking:3}]
item replace entity @s armor.chest with minecraft:diamond_chestplate[unbreakable={},enchantments={protection:3,unbreaking:3}]
item replace entity @s armor.legs with minecraft:diamond_leggings[unbreakable={},enchantments={protection:3,unbreaking:3}]
item replace entity @s armor.feet with minecraft:diamond_boots[unbreakable={},enchantments={protection:3,unbreaking:3}]
effect give @s minecraft:strength infinite 0 true
effect give @s minecraft:speed infinite 0 true
effect give @s minecraft:health_boost infinite 2 true
effect give @s minecraft:instant_health 1 3 true
