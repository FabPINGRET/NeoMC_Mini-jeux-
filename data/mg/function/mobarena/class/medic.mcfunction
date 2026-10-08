# Mob Arena — classe MÉDECIN (@s) : soigne l’équipe (potions persistantes de régénération, soin de zone)
give @s minecraft:iron_sword[unbreakable={}]
give @s minecraft:lingering_potion[potion_contents={potion:"minecraft:strong_regeneration"}] 4
give @s minecraft:splash_potion[potion_contents={potion:"minecraft:strong_healing"}] 6
give @s minecraft:golden_apple 3
item replace entity @s armor.head with minecraft:iron_helmet[unbreakable={}]
item replace entity @s armor.chest with minecraft:leather_chestplate[unbreakable={},dyed_color=16777215]
item replace entity @s armor.legs with minecraft:leather_leggings[unbreakable={},dyed_color=16777215]
item replace entity @s armor.feet with minecraft:iron_boots[unbreakable={}]
