# @s : batte, pistolet
clear @s
function mg:gun/reset
execute if score $rp mg.st matches 1 run function mg:gta/bat {m:"mg:bat"}
execute unless score $rp mg.st matches 1 run function mg:gta/bat {m:"minecraft:stick"}
function mg:gun/put_1 {slot:"hotbar.1"}
scoreboard players set @s mg.grk 0
function mg:gta/kit_plus
item replace entity @s hotbar.7 with minecraft:warped_fungus_on_a_stick[custom_data={gtahome:1b},item_model="minecraft:oak_door",unbreakable={},custom_name={"text":"🏠 Retour à la villa","color":"aqua","bold":true,"italic":false},lore=[{"text":"Clic droit : Neo Hills (pas avec la police aux trousses)","color":"gray","italic":false}]]
item replace entity @s hotbar.8 with minecraft:paper[custom_data={gtamap:1b},item_model="minecraft:filled_map",custom_name={"text":"🗺 Carte de Neo City","color":"aqua","bold":true,"italic":false},lore=[{"text":"En main : plan de la ville et ta position","color":"gray","italic":false}]]
effect give @s minecraft:saturation infinite 0 true
effect give @s minecraft:resistance 3 4 true
