# Donne « Fusil M14 » dans l'emplacement $(slot), chargeur plein
$execute if score $rp mg.st matches 1 run item replace entity @s $(slot) with minecraft:warped_fungus_on_a_stick[custom_data={gun:4,mg_gun:1b},custom_name=[{"text":"🔫 Fusil M14","color":"yellow","italic":false}],lore=[[{"text":"Clic droit : tirer — accroupi : recharger","color":"gray","italic":false}]],unbreakable={},item_model="mg:gun_rifle"]
$execute unless score $rp mg.st matches 1 run item replace entity @s $(slot) with minecraft:warped_fungus_on_a_stick[custom_data={gun:4,mg_gun:1b},custom_name=[{"text":"🔫 Fusil M14","color":"yellow","italic":false}],lore=[[{"text":"Clic droit : tirer — accroupi : recharger","color":"gray","italic":false}]],unbreakable={},item_model="minecraft:crossbow"]
scoreboard players set @s mg.g4 10
execute if entity @s[tag=mg.gtw] run scoreboard players set @s mg.g4 20
