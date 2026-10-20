# Kit du duel (@s) : le sniper en main, le couteau (clic gauche) dans l'inventaire
clear @s *[custom_data~{mg_dl:1b}]
item replace entity @s weapon.mainhand with minecraft:warped_fungus_on_a_stick[custom_data={mg_dl:1b},item_model="minecraft:spyglass",unbreakable={},custom_name={"text":"🎯 Sniper de duel","color":"aqua","bold":true,"italic":false},lore=[{"text":"Clic droit : tir (recharge 2 s)","color":"gray","italic":false},{"text":"Accroupi : lunette — tête = élimination, corps = 2 touches","color":"gray","italic":false}]]
execute unless entity @s[tag=mg.dlp] run item modify entity @s weapon.mainhand {function:"minecraft:set_components",components:{"minecraft:use_cooldown":{seconds:2f,cooldown_group:"mg:dlsn"}}}
give @s minecraft:stone_sword[custom_data={mg_dl:1b,mg_kn:1b},unbreakable={},custom_name={"text":"🔪 Couteau","color":"red","bold":true,"italic":false},lore=[{"text":"Clic gauche : 1 dégât (2 coups = élimination), recharge 1 s","color":"gray","italic":false}]]
