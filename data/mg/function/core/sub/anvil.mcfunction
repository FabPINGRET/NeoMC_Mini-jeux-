# Sous-menu ⚓ Pluie d'Enclumes (@s = joueur) — fenêtre, sinon menu texte
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]
execute unless entity @s[tag=mg.admin] run return 0
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run function mg:rate/d/sub_anvil with storage mg:rate lab
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n⚓ Pluie d'Enclumes — choisis une version","color":"gray","bold":true}]
tellraw @s ["",{"text":" [⚓ Pluie d'Enclumes]","color":"gray","click_event":{"action":"run_command","command":"trigger mg.go set 29"},"hover_event":{"action":"show_text","value":"Esquive les enclumes qui tombent du ciel"}}]
tellraw @s ["",{"text":" [⚓ Enclumes + sol troué]","color":"red","click_event":{"action":"run_command","command":"trigger mg.go set 42"},"hover_event":{"action":"show_text","value":"Pluie d'Enclumes avec des trous qui s'ouvrent dans le sol"}}]
tellraw @s ["",{"text":" [« Retour au menu]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.menu"}}]
