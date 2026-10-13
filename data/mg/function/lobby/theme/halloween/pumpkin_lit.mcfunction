# 🎃 Halloween : citrouille lit de couleur aléatoire (pack activé)
execute store result score $thp mg.st run random value 1..9
execute if score $thp mg.st matches 1 run item replace entity @s contents with minecraft:leather_horse_armor[minecraft:item_model="mg:pumpkin_lit",minecraft:dyed_color=16747036]
execute if score $thp mg.st matches 2 run item replace entity @s contents with minecraft:leather_horse_armor[minecraft:item_model="mg:pumpkin_lit",minecraft:dyed_color=9321430]
execute if score $thp mg.st matches 3 run item replace entity @s contents with minecraft:leather_horse_armor[minecraft:item_model="mg:pumpkin_lit",minecraft:dyed_color=5227066]
execute if score $thp mg.st matches 4 run item replace entity @s contents with minecraft:leather_horse_armor[minecraft:item_model="mg:pumpkin_lit",minecraft:dyed_color=15527156]
execute if score $thp mg.st matches 5 run item replace entity @s contents with minecraft:leather_horse_armor[minecraft:item_model="mg:pumpkin_lit",minecraft:dyed_color=3814464]
execute if score $thp mg.st matches 6 run item replace entity @s contents with minecraft:leather_horse_armor[minecraft:item_model="mg:pumpkin_lit",minecraft:dyed_color=14035498]
execute if score $thp mg.st matches 7 run item replace entity @s contents with minecraft:leather_horse_armor[minecraft:item_model="mg:pumpkin_lit",minecraft:dyed_color=3832800]
execute if score $thp mg.st matches 8 run item replace entity @s contents with minecraft:leather_horse_armor[minecraft:item_model="mg:pumpkin_lit",minecraft:dyed_color=3131573]
execute if score $thp mg.st matches 9 run item replace entity @s contents with minecraft:leather_horse_armor[minecraft:item_model="mg:pumpkin_lit",minecraft:dyed_color=16740277]
