# Donne « Revolver Python » dans l'emplacement $(slot), chargeur plein
$execute if score $rp mg.st matches 1 run item replace entity @s $(slot) with minecraft:warped_fungus_on_a_stick[custom_data={gun:8,mg_gun:1b},custom_name=[{"text":"🔫 Revolver Python","color":"dark_aqua","italic":false}],lore=[[{"text":"Clic droit : tirer — accroupi : recharger","color":"gray","italic":false}]],unbreakable={},item_model="mg:gun_pistol"]
$execute unless score $rp mg.st matches 1 run item replace entity @s $(slot) with minecraft:warped_fungus_on_a_stick[custom_data={gun:8,mg_gun:1b},custom_name=[{"text":"🔫 Revolver Python","color":"dark_aqua","italic":false}],lore=[[{"text":"Clic droit : tirer — accroupi : recharger","color":"gray","italic":false}]],unbreakable={},item_model="minecraft:crossbow"]
scoreboard players set @s mg.g8 6
execute if entity @s[tag=mg.gtw] run scoreboard players set @s mg.g8 12
