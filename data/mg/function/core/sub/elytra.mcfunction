# Sous-menu 🪽 Élytra (@s = joueur) — fenêtre, sinon menu texte
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]
execute unless entity @s[tag=mg.admin] run return 0
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run function mg:rate/d/sub_elytra with storage mg:rate lab
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n🪽 Élytra — Mini-jeu en vol : choisis le mode.","color":"aqua","bold":true}]
tellraw @s ["",{"text":" [🎲 Mode au hasard]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 78"},"hover_event":{"action":"show_text","value":"Un des 3 modes, tiré au sort"}}]
tellraw @s ["",{"text":" [◎ Course d'anneaux]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.go set 75"},"hover_event":{"action":"show_text","value":"20 anneaux dans l'ordre, premier arrivé gagne"}}]
tellraw @s ["",{"text":" [➶ Course + combat]","color":"red","click_event":{"action":"run_command","command":"trigger mg.go set 76"},"hover_event":{"action":"show_text","value":"Arc et charges de vent : un adversaire touché chute"}}]
tellraw @s ["",{"text":" [☁ Survie en vol]","color":"light_purple","click_event":{"action":"run_command","command":"trigger mg.go set 77"},"hover_event":{"action":"show_text","value":"Reste en l'air dans la zone qui rétrécit"}}]
tellraw @s ["",{"text":" [« Retour au menu]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.menu"}}]
