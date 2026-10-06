# Paintball — équipement (@s) : pistolet à peinture + armure de la couleur de l'équipe
clear @s
item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[unbreakable={},custom_name=[{"text":"Pistolet à peinture","color":"gold","bold":true,"italic":false}],lore=[{"text":"Clic droit (maintenu) : projette de la peinture","color":"gray","italic":false}],enchantment_glint_override=true]
execute if entity @s[team=mg_red] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=16746496]
execute if entity @s[team=mg_red] run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16746496]
execute if entity @s[team=mg_red] run item replace entity @s armor.legs with minecraft:leather_leggings[dyed_color=16746496]
execute if entity @s[team=mg_red] run item replace entity @s armor.feet with minecraft:leather_boots[dyed_color=16746496]
execute if entity @s[team=mg_blue] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=2003199]
execute if entity @s[team=mg_blue] run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=2003199]
execute if entity @s[team=mg_blue] run item replace entity @s armor.legs with minecraft:leather_leggings[dyed_color=2003199]
execute if entity @s[team=mg_blue] run item replace entity @s armor.feet with minecraft:leather_boots[dyed_color=2003199]
