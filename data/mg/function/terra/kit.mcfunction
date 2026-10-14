# @s : équipement de base (à chaque arrivée : seuls les crédits sont gardés)
clear @s
item replace entity @s hotbar.0 with minecraft:stick[custom_data={tv:1},item_model="minecraft:blaze_rod",custom_name={"text":"⚡ Bâton électrique","color":"yellow","italic":false,"bold":true},lore=[{"text":"Mêlée : étourdit le dinosaure touché","color":"gray","italic":false},{"text":"(lenteur V + faiblesse, 3 s)","color":"gray","italic":false}],attribute_modifiers=[{type:"minecraft:attack_damage",id:"mg:tvprod",amount:5.0,operation:"add_value",slot:"mainhand"}]]
item replace entity @s hotbar.1 with minecraft:warped_fungus_on_a_stick[custom_data={tv:2},item_model="minecraft:crossbow",unbreakable={},custom_name={"text":"🔫 Fusil à impulsions","color":"aqua","italic":false,"bold":true},lore=[{"text":"Clic droit : tir (maintenir = rafale)","color":"gray","italic":false},{"text":"Attention à la surchauffe !","color":"gray","italic":false}]]
item replace entity @s hotbar.7 with minecraft:warped_fungus_on_a_stick[custom_data={tv:9},item_model="minecraft:bell",unbreakable={},custom_name={"text":"📡 Rappel à la colonie","color":"green","italic":false,"bold":true},lore=[{"text":"Clic droit : retour à la colonie en 5 s","color":"gray","italic":false},{"text":"Annulé si tu prends un coup","color":"gray","italic":false}]]
function mg:terra/loc {x:0,y:65,z:0}
item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=9140827,unbreakable={},custom_name={"text":"Uniforme de colon","color":"gold","italic":false,"bold":true}]
item replace entity @s armor.feet with minecraft:leather_boots[dyed_color=5915971,unbreakable={},custom_name={"text":"Bottes de colon","color":"gold","italic":false,"bold":true}]
scoreboard players set @s mg.tvnet 0
scoreboard players set @s mg.tvtr 0
effect give @s minecraft:saturation infinite 0 true
