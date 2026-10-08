# @s = nouveau porteur de la bombe : TNT sur la tête, plastron rouge, vitesse II, saut, lueur rouge
item replace entity @s armor.head with minecraft:tnt[custom_name=[{"text":"BOMBE","color":"red","bold":true,"italic":false}]]
item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16711680,custom_name=[{"text":"Gilet de la bombe","color":"red","italic":false}],enchantments={"minecraft:binding_curse":1},tooltip_display={hidden_components:["minecraft:enchantments","minecraft:dyed_color"]}]
effect give @s minecraft:speed infinite 1 true
effect give @s minecraft:jump_boost infinite 0 true
effect give @s minecraft:glowing infinite 0 true
team join mg_red @s
title @s title [{"text":"✹ TU AS LA BOMBE !","color":"red","bold":true}]
title @s subtitle [{"text":"Frappe quelqu'un pour la lui passer — tu cours plus vite et sautes plus haut","color":"gray"}]
execute at @s run playsound minecraft:entity.tnt.primed master @a ~ ~ ~ 1.2 1
execute at @s run particle minecraft:explosion ~ ~1 ~ 0.3 0.3 0.3 0 3
