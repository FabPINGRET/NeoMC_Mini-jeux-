# @s : les bombes, les élytres et les fusées
item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[custom_data={bomb:1},item_model="minecraft:tnt",unbreakable={},custom_name={"text":"Bombe","color":"red","bold":true,"italic":false},lore=[{"text":"Rayon 6, recharge 0,6 s","color":"gray","italic":false},{"text":"Clic droit : larguer (dans la direction du regard)","color":"dark_gray","italic":false}],use_cooldown={seconds:0.6f,cooldown_group:"mg:bomb1"}]
item replace entity @s hotbar.1 with minecraft:warped_fungus_on_a_stick[custom_data={bomb:2},item_model="minecraft:tnt_minecart",unbreakable={},custom_name={"text":"Méga-bombe","color":"dark_red","bold":true,"italic":false},lore=[{"text":"Rayon 12, recharge 7 s","color":"gray","italic":false},{"text":"Clic droit : larguer (dans la direction du regard)","color":"dark_gray","italic":false}],use_cooldown={seconds:7.0f,cooldown_group:"mg:bomb2"}]
item replace entity @s hotbar.2 with minecraft:warped_fungus_on_a_stick[custom_data={bomb:3},item_model="minecraft:fire_charge",unbreakable={},custom_name={"text":"Bombe à fragmentation","color":"gold","bold":true,"italic":false},lore=[{"text":"7 sous-munitions, recharge 5 s","color":"gray","italic":false},{"text":"Clic droit : larguer (dans la direction du regard)","color":"dark_gray","italic":false}],use_cooldown={seconds:5.0f,cooldown_group:"mg:bomb3"}]
item replace entity @s armor.chest with minecraft:elytra[custom_data={mg_bomb:1b},unbreakable={},enchantments={"minecraft:binding_curse":1},custom_name={"text":"Élytres du bombardier","color":"red","italic":false}]
item replace entity @s hotbar.8 with minecraft:firework_rocket[custom_data={mg_bomb:1b},fireworks={flight_duration:1},custom_name={"text":"Fusée (illimitée)","color":"gold","italic":false}] 16
effect give @s minecraft:speed infinite 1 true
effect give @s minecraft:saturation infinite 0 true
effect give @s minecraft:resistance infinite 4 true
effect give @s minecraft:night_vision infinite 0 true
