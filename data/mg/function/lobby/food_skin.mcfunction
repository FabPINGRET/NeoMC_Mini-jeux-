# Buffet du spawn : présentoirs et enseigne selon le décor saisonnier ($theme) — appelé par food_build et à chaque changement de thème
execute as @e[type=minecraft:item_display,tag=mg.foodd,x=25.5,y=65.4,z=19.5,distance=..0.3] run tag @s add mg.food1
execute as @e[type=minecraft:item_display,tag=mg.foodd,x=26.5,y=66.0,z=19.5,distance=..0.3] run tag @s add mg.food2
execute as @e[type=minecraft:text_display,tag=mg.foodd,x=26.5,y=68.3,z=19.5,distance=..0.3] run tag @s add mg.foodt
# Sans thème : steak et carotte dorée
execute unless score $theme mg.st matches 1..2 run item replace entity @e[tag=mg.food1] contents with minecraft:cooked_beef
execute unless score $theme mg.st matches 1..2 run item replace entity @e[tag=mg.food2] contents with minecraft:golden_carrot
execute unless score $theme mg.st matches 1..2 run data modify entity @e[tag=mg.foodt,limit=1] text set value {"text":"🍖 Buffet gratuit","color":"gold","bold":true}
# 🎃 Halloween : tarte à la citrouille et latte à la citrouille
execute if score $theme mg.st matches 1 run item replace entity @e[tag=mg.food1] contents with minecraft:pumpkin_pie
execute if score $theme mg.st matches 1 if score $rp mg.st matches 1 run item replace entity @e[tag=mg.food2] contents with minecraft:honey_bottle[minecraft:item_model="mg:pumpkin_latte"]
execute if score $theme mg.st matches 1 unless score $rp mg.st matches 1 run item replace entity @e[tag=mg.food2] contents with minecraft:honey_bottle
execute if score $theme mg.st matches 1 run data modify entity @e[tag=mg.foodt,limit=1] text set value {"text":"🎃 Buffet d'Halloween","color":"gold","bold":true}
# 🎄 Noël : sucre d'orge et chocolat chaud
execute if score $theme mg.st matches 2 if score $rp mg.st matches 1 run item replace entity @e[tag=mg.food1] contents with minecraft:cookie[minecraft:item_model="mg:candy_cane"]
execute if score $theme mg.st matches 2 unless score $rp mg.st matches 1 run item replace entity @e[tag=mg.food1] contents with minecraft:cookie
execute if score $theme mg.st matches 2 if score $rp mg.st matches 1 run item replace entity @e[tag=mg.food2] contents with minecraft:honey_bottle[minecraft:item_model="mg:hot_chocolate"]
execute if score $theme mg.st matches 2 unless score $rp mg.st matches 1 run item replace entity @e[tag=mg.food2] contents with minecraft:mushroom_stew
execute if score $theme mg.st matches 2 run data modify entity @e[tag=mg.foodt,limit=1] text set value [{"text":"🎄 ","color":"green"},{"text":"Buffet de Noël","color":"red","bold":true}]
