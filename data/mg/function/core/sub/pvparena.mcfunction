# Sous-menu ⚔ Arène PvP (@s = joueur) — fenêtre, sinon menu texte
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]
execute unless entity @s[tag=mg.admin] run return 0
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run function mg:rate/d/sub_pvparena with storage mg:rate lab
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n⚔ Arène PvP — choisis une version","color":"gold","bold":true}]
tellraw @s ["",{"text":" [⚔ Arène PvP]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.go set 3"},"hover_event":{"action":"show_text","value":"Lancer l'Arène PvP"}}]
tellraw @s ["",{"text":" [⚔ PvP : classes]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 13"},"hover_event":{"action":"show_text","value":"Arène PvP avec choix de classe d'équipement"}}]
tellraw @s ["",{"text":" [⚔ PvP : Poussière]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 44"},"hover_event":{"action":"show_text","value":"Arène PvP sur la carte Poussière (style Dust)"}}]
tellraw @s ["",{"text":" [⚔ PvP classes : Poussière]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 45"},"hover_event":{"action":"show_text","value":"PvP avec classes sur la carte Poussière"}}]
tellraw @s ["",{"text":" [⚔ PvP : Mirage]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.go set 47"},"hover_event":{"action":"show_text","value":"Arène PvP sur la carte Mirage (style Mirage)"}}]
tellraw @s ["",{"text":" [⚔ PvP classes : Mirage]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.go set 48"},"hover_event":{"action":"show_text","value":"PvP avec classes sur la carte Mirage"}}]
tellraw @s ["",{"text":" [⚔ PvP : Nuketown]","color":"green","click_event":{"action":"run_command","command":"trigger mg.go set 50"},"hover_event":{"action":"show_text","value":"Arène PvP sur la carte Nuketown (style Nuketown)"}}]
tellraw @s ["",{"text":" [⚔ PvP classes : Nuketown]","color":"green","click_event":{"action":"run_command","command":"trigger mg.go set 51"},"hover_event":{"action":"show_text","value":"PvP avec classes sur la carte Nuketown"}}]
tellraw @s ["",{"text":" [« Retour au PvP]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.opt set 14"}}]
