# Sous-menu ★ Mini Party (@s = joueur) — fenêtre, sinon menu texte
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]
execute unless entity @s[tag=mg.admin] run return 0
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run dialog show @s mg:sub_party
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n★ Mini Party — choisis une version","color":"gold","bold":true}]
tellraw @s ["",{"text":" [★ MINI PARTY 5 tours]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 59"},"hover_event":{"action":"show_text","value":"Plateau, dé, étoiles et mini-jeux"}}]
tellraw @s ["",{"text":" [★ MINI PARTY 10 tours]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 60"},"hover_event":{"action":"show_text","value":"Version longue"}}]
tellraw @s ["",{"text":" [« Retour au menu]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.menu"}}]
