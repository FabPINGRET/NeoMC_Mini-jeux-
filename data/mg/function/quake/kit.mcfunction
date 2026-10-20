# Quakecraft — équipement (@s = joueur) : le railgun
# Fichier écrit à la main (pas de générateur) ; icône railgun du pack (modèle mg:laser_gun) quand le pack est actif ($rp mg.st = 1).
clear @s
execute if score $rp mg.st matches 1 run item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[unbreakable={},custom_name=[{"text":"⚡ Railgun","color":"aqua","bold":true,"italic":false}],lore=[{"text":"Clic droit : rayon instantané, un tir = un kill","color":"gray","italic":false}],enchantment_glint_override=true,item_model="mg:laser_gun"]
execute unless score $rp mg.st matches 1 run item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[unbreakable={},custom_name=[{"text":"⚡ Railgun","color":"aqua","bold":true,"italic":false}],lore=[{"text":"Clic droit : rayon instantané, un tir = un kill","color":"gray","italic":false}],enchantment_glint_override=true]
