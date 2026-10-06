# One in the Chamber — équipement (@s = joueur) : épée, arc, UNE flèche
clear @s minecraft:stone_sword
clear @s minecraft:bow
clear @s minecraft:arrow
item replace entity @s hotbar.0 with minecraft:stone_sword[unbreakable={},custom_name=[{"text":"Épée","color":"gray","italic":false}]]
item replace entity @s hotbar.1 with minecraft:bow[unbreakable={},custom_name=[{"text":"Arc One-Shot","color":"gold","italic":false}],lore=[{"text":"Une flèche = un kill","color":"gray","italic":false}]]
item replace entity @s hotbar.8 with minecraft:arrow[custom_name=[{"text":"Flèche","color":"yellow","italic":false}]] 1
