# Donne « Mitrailleuse RPK » dans l'emplacement $(slot), chargeur plein
$execute if score $rp mg.st matches 1 run item replace entity @s $(slot) with minecraft:warped_fungus_on_a_stick[custom_data={gun:7,mg_gun:1b},custom_name=[{"text":"🔫 Mitrailleuse RPK","color":"red","italic":false}],lore=[[{"text":"Clic droit : tirer — accroupi : recharger","color":"gray","italic":false}]],unbreakable={},item_model="mg:gun_rifle"]
$execute unless score $rp mg.st matches 1 run item replace entity @s $(slot) with minecraft:warped_fungus_on_a_stick[custom_data={gun:7,mg_gun:1b},custom_name=[{"text":"🔫 Mitrailleuse RPK","color":"red","italic":false}],lore=[[{"text":"Clic droit : tirer — accroupi : recharger","color":"gray","italic":false}]],unbreakable={},item_model="minecraft:crossbow"]
scoreboard players set @s mg.g7 60
execute if entity @s[tag=mg.gtw] run scoreboard players set @s mg.g7 120
