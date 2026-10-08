# @s : chercheur
clear @s
effect clear @s minecraft:invisibility
attribute @s minecraft:scale base set 1
item replace entity @s hotbar.0 with minecraft:iron_sword[unbreakable={}]
item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16711680,unbreakable={}]
item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=16711680,unbreakable={}]
effect give @s minecraft:saturation infinite 0 true
effect give @s minecraft:speed infinite 0 true
