# Objet en main (case 1 de la barre) : bâton à champignon tordu, clic droit = utiliser
execute if score @s mg.kit matches 1 run item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[item_model="minecraft:yellow_dye",custom_name=[{"text":"🍌 Banane","color":"yellow","bold":true,"italic":false}],lore=[[{"text":"Clic droit pour l'utiliser","color":"gray","italic":false}]],unbreakable={}]
execute if score @s mg.kit matches 1 run title @s subtitle [{"text":"🍌 Banane","color":"yellow","bold":true}]
execute if score @s mg.kit matches 2 run item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[item_model="minecraft:turtle_scute",custom_name=[{"text":"🟢 Carapace verte","color":"green","bold":true,"italic":false}],lore=[[{"text":"Clic droit pour l'utiliser","color":"gray","italic":false}]],unbreakable={}]
execute if score @s mg.kit matches 2 run title @s subtitle [{"text":"🟢 Carapace verte","color":"green","bold":true}]
execute if score @s mg.kit matches 3 run item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[item_model="minecraft:red_dye",custom_name=[{"text":"🔴 Carapace rouge","color":"red","bold":true,"italic":false}],lore=[[{"text":"Clic droit pour l'utiliser","color":"gray","italic":false}]],unbreakable={}]
execute if score @s mg.kit matches 3 run title @s subtitle [{"text":"🔴 Carapace rouge","color":"red","bold":true}]
execute if score @s mg.kit matches 4 run item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[item_model="minecraft:red_mushroom",custom_name=[{"text":"🍄 Champignon","color":"gold","bold":true,"italic":false}],lore=[[{"text":"Clic droit pour l'utiliser","color":"gray","italic":false}]],unbreakable={}]
execute if score @s mg.kit matches 4 run title @s subtitle [{"text":"🍄 Champignon","color":"gold","bold":true}]
execute if score @s mg.kit matches 5 run item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[item_model="minecraft:nether_star",custom_name=[{"text":"⭐ Étoile","color":"yellow","bold":true,"italic":false}],lore=[[{"text":"Clic droit pour l'utiliser","color":"gray","italic":false}]],unbreakable={}]
execute if score @s mg.kit matches 5 run title @s subtitle [{"text":"⭐ Étoile","color":"yellow","bold":true}]
execute if score @s mg.kit matches 6 run item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[item_model="minecraft:lightning_rod",custom_name=[{"text":"⚡ Éclair","color":"aqua","bold":true,"italic":false}],lore=[[{"text":"Clic droit pour l'utiliser","color":"gray","italic":false}]],unbreakable={}]
execute if score @s mg.kit matches 6 run title @s subtitle [{"text":"⚡ Éclair","color":"aqua","bold":true}]
title @s title ""
execute at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.4
