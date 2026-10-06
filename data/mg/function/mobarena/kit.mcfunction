# Mob Arena — kit de départ (@s)
give @s minecraft:iron_sword[unbreakable={}]
give @s minecraft:bow[unbreakable={}]
give @s minecraft:arrow 32
item replace entity @s armor.head with minecraft:iron_helmet[unbreakable={}]
item replace entity @s armor.chest with minecraft:iron_chestplate[unbreakable={}]
item replace entity @s armor.legs with minecraft:iron_leggings[unbreakable={}]
item replace entity @s armor.feet with minecraft:iron_boots[unbreakable={}]
execute if score $mt mg.st matches 3 run function mg:mobarena/kit_ultra
# Classe choisie (sauf Ultra Hard, kit imposé)
execute unless score $mt mg.st matches 3 if score @s mg.cl matches 2..8 run function mg:mobarena/class_kit
# Bouclier en main secondaire (tous les thèmes PvE)
item replace entity @s weapon.offhand with minecraft:shield[unbreakable={},enchantments={unbreaking:3}]
# Luminosité : vision nocturne permanente (arènes de nuit trop sombres)
effect give @s minecraft:night_vision infinite 0 true
