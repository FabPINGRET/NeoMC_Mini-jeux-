# Sous-menu ✎ Build Battle (@s = joueur) — fenêtre, sinon menu texte
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]
execute unless entity @s[tag=mg.admin] run return 0
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run dialog show @s mg:sub_bb
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n✎ Build Battle — choisis une version","color":"green","bold":true}]
tellraw @s ["",{"text":" [✎ Build Battle : thème aléatoire]","color":"green","click_event":{"action":"run_command","command":"trigger mg.go set 57"},"hover_event":{"action":"show_text","value":"Construis le thème tiré au sort, puis les autres joueurs notent de 1 à 5"}}]
tellraw @s ["",{"text":" [✎ Build Battle : Maître du mot]","color":"dark_aqua","click_event":{"action":"run_command","command":"trigger mg.go set 58"},"hover_event":{"action":"show_text","value":"Un joueur tiré au sort donne le thème à construire (3 joueurs minimum)"}}]
tellraw @s ["",{"text":" [« Retour au menu]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.menu"}}]
