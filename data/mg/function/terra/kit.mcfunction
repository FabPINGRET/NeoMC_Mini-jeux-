# @s : équipement (paliers du RPG gardés : mêlée, fusil, armure, scanner, sifflet)
clear @s
function mg:terra/rpg/kit
item replace entity @s hotbar.7 with minecraft:warped_fungus_on_a_stick[custom_data={tv:9},item_model="minecraft:bell",unbreakable={},custom_name={"text":"📡 Rappel à la colonie","color":"green","italic":false,"bold":true},lore=[{"text":"Clic droit : retour à la colonie en 5 s","color":"gray","italic":false},{"text":"Annulé si tu prends un coup","color":"gray","italic":false}]]
function mg:terra/rpg/qloc
scoreboard players set @s mg.tvnet 0
scoreboard players set @s mg.tvtr 0
effect give @s minecraft:saturation infinite 0 true
