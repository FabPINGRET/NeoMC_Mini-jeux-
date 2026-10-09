# Sous-menu ▓ Paintball (@s = joueur) — fenêtre, sinon menu texte
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]
execute unless entity @s[tag=mg.admin] run return 0
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run function mg:rate/d/sub_paint with storage mg:rate lab
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n▓ Paintball — choisis une version","color":"gold","bold":true}]
tellraw @s ["",{"text":" [▓ Paintball]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 36"},"hover_event":{"action":"show_text","value":"Splatoon : peins le terrain en orange ou en bleu"}}]
tellraw @s ["",{"text":" [▓ Paintball : Mini-terrain]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 54"},"hover_event":{"action":"show_text","value":"Paintball 31×41, parties de 1 min 30"}}]
tellraw @s ["",{"text":" [▓ Paintball : Grand terrain]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 55"},"hover_event":{"action":"show_text","value":"Paintball 81×101, grosse bataille de 3 minutes"}}]
tellraw @s ["",{"text":" [« Retour au menu]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.menu"}}]
