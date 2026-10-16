# Le Dr Ossei donne le scanner
item replace entity @s hotbar.2 with minecraft:warped_fungus_on_a_stick[custom_data={tv:10},item_model="minecraft:spyglass",unbreakable={},custom_name={"text":"🔬 Scanner du Dr Ossei","color":"aqua","italic":false,"bold":true},lore=[{"text":"Clic droit en visant un dinosaure (16 blocs)","color":"gray","italic":false},{"text":"Ajoute l'espèce au bestiaire : +XP","color":"gray","italic":false}]]
function mg:terra/rpg/ch {n:25}
tellraw @s {"text":"🔬 Scanner reçu (case 3) : vise un dinosaure à moins de 16 blocs et fais clic droit.","color":"aqua"}
