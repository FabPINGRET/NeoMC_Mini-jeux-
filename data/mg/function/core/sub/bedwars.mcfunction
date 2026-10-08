# Sous-menu ⚑ Bedwars (@s = joueur) — fenêtre, sinon menu texte
execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Le menu est réservé aux admins.","color":"red"}]
execute unless entity @s[tag=mg.admin] run return 0
scoreboard players set $dlg mg.st 0
execute store success score $dlg mg.st run dialog show @s mg:sub_bedwars
execute if score $dlg mg.st matches 1 run return 0
tellraw @s [{"text":"\n⚑ Bedwars — Détruis les lits ennemis : choisis la carte.","color":"light_purple","bold":true}]
tellraw @s ["",{"text":" [🎲 Carte au hasard]","color":"gold","click_event":{"action":"run_command","command":"trigger mg.go set 4"},"hover_event":{"action":"show_text","value":"Une des 4 cartes, tirée au sort"}}]
tellraw @s ["",{"text":" [⚑ Classique]","color":"light_purple","click_event":{"action":"run_command","command":"trigger mg.go set 71"},"hover_event":{"action":"show_text","value":"4 îles de pierre autour du diamant"}}]
tellraw @s ["",{"text":" [🌋 Caldeira]","color":"red","click_event":{"action":"run_command","command":"trigger mg.go set 72"},"hover_event":{"action":"show_text","value":"Volcan de basalte, 4 îlots avec or bonus"}}]
tellraw @s ["",{"text":" [🌸 Hanami]","color":"light_purple","click_event":{"action":"run_command","command":"trigger mg.go set 73"},"hover_event":{"action":"show_text","value":"Jardin des cerisiers, pagode, terrasses"}}]
tellraw @s ["",{"text":" [❄ Banquise]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.go set 74"},"hover_event":{"action":"show_text","value":"Glacier, igloos, plaques de glace"}}]
tellraw @s ["",{"text":" [« Retour au menu]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.menu"}}]
