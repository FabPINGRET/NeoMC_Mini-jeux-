# Sous-menu ➶ One in the Chamber (@s = joueur) — fenêtre, sinon menu texte
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]
execute unless entity @s[tag=mg.admin] run return 0
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run function mg:rate/d/sub_oitc with storage mg:rate lab
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n➶ One in the Chamber — choisis une version","color":"gold","bold":true}]
tellraw @s ["",{"text":" [➶ One in the Chamber]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 26"},"hover_event":{"action":"show_text","value":"3 vies, une épée, une flèche : un tir = un kill"}}]
tellraw @s ["",{"text":" [➶ OITC : Château]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 52"},"hover_event":{"action":"show_text","value":"One in the Chamber 41×41 : donjon à étage, quatre tours à échelles"}}]
tellraw @s ["",{"text":" [➶ OITC : Grande forêt]","color":"dark_green","click_event":{"action":"run_command","command":"trigger mg.go set 53"},"hover_event":{"action":"show_text","value":"One in the Chamber 71×71 : collines, arbres, ruines et tours de guet"}}]
tellraw @s ["",{"text":" [« Retour au PvP]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.opt set 14"}}]
